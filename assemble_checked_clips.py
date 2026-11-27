#!/usr/bin/env python3
"""Validate per-shot lengths and concatenate VISUAL clips. Does not add narration."""
import argparse
import json
import re
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--clips',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--width',type=int,default=1920)
    ap.add_argument('--height',type=int,default=1080)
    a=ap.parse_args();manifest=json.loads(a.manifest.read_text());rows=manifest['shots']
    paths=[];profile=None;cursor=0
    for row in rows:
        if not re.fullmatch(r'S\d{3}',row['id']):raise ValueError('Unexpected shot ID')
        if row['start_frame']!=cursor:raise ValueError('Non-contiguous shot timeline')
        path=(a.clips/(row['id']+'.mp4')).resolve()
        if not path.is_file():raise FileNotFoundError(path)
        p=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0',
            '-count_frames','-show_streams','-of','json',str(path)],text=True))['streams'][0]
        expected=row['end_frame_exclusive']-row['start_frame']
        if int(p['nb_read_frames'])!=expected:raise ValueError(f'{row["id"]}: frame count mismatch')
        if (p['width'],p['height'])!=(a.width,a.height):raise ValueError('Wrong clip dimensions')
        if Fraction(p['avg_frame_rate'])!=30 or Fraction(p['r_frame_rate'])!=30:raise ValueError('Wrong fps')
        if p['codec_name']!='h264' or p['pix_fmt']!='yuv420p':raise ValueError('Expected H.264 yuv420p')
        current=tuple(p.get(k) for k in ('codec_name','profile','level','pix_fmt','time_base','sample_aspect_ratio'))
        if profile is not None and profile!=current:raise ValueError('Incompatible clip encoding settings')
        profile=current;paths.append(path);cursor=row['end_frame_exclusive']
    expected_total=round(manifest['duration_seconds']*30)
    if cursor!=expected_total:raise ValueError('Manifest does not cover expected duration')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    name=None
    try:
        with tempfile.NamedTemporaryFile('w',suffix='.ffconcat',encoding='utf-8',delete=False) as f:
            name=Path(f.name);f.write('ffconcat version 1.0\n')
            for path in paths:
                escaped=path.as_posix().replace("'", "'\\''")
                f.write(f"file '{escaped}'\n")
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(name),
                        '-map','0:v:0','-an','-c:v','copy','-movflags','+faststart',str(a.output)],check=True)
    finally:
        if name is not None:name.unlink(missing_ok=True)
    print(json.dumps({'status':'visual_master_created','shots':len(paths),'expected_frames':cursor,
                      'output':str(a.output),'audio_added':False,
                      'next':'Add aligned narration, sound mix and captions, then validate the final film'}))


if __name__=='__main__':main()
