#!/usr/bin/env python3
"""Every source frame, 60 per sheet. ffmpeg/ffprobe/Pillow required."""
import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path
from PIL import Image, ImageDraw


def exact_read(pipe,n):
    chunks=[];left=n
    while left:
        b=pipe.read(left)
        if not b:break
        chunks.append(b);left-=len(b)
    out=b''.join(chunks)
    if out and len(out)!=n:raise RuntimeError('Incomplete raw frame')
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('video',type=Path);ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    p=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0',
        '-show_streams','-of','json',str(a.video)],text=True))
    if Fraction(p['streams'][0]['avg_frame_rate'])!=30:raise ValueError('Expected original 30 fps video; no resampling performed')
    a.out.mkdir(parents=True,exist_ok=True)
    width,height,label=192,108,24;count=0;entries=[];sheet=None
    def save(first,last):
        name=f'sheet_{len(entries)+1:03d}_{first:05d}-{last:05d}.jpg'
        sheet.save(a.out/name,quality=93)
        entries.append({'file':name,'first_frame':first,'last_frame_inclusive':last,
                        'frames':last-first+1,'start_s':first/30,'end_s_exclusive':(last+1)/30})
    vf=f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2'
    with (a.out/'ffmpeg_decode.log').open('wb') as log:
        proc=subprocess.Popen(['ffmpeg','-v','error','-i',str(a.video),'-map','0:v:0','-an',
          '-vf',vf,'-fps_mode','passthrough','-f','rawvideo','-pix_fmt','rgb24','pipe:1'],
          stdout=subprocess.PIPE,stderr=log,stdin=subprocess.DEVNULL)
        try:
            while True:
                raw=exact_read(proc.stdout,width*height*3)
                if not raw:break
                local=count%60
                if local==0:
                    sheet=Image.new('RGB',(10*width,6*(height+label)),(22,24,29));draw=ImageDraw.Draw(sheet)
                x=local%10*width;y=local//10*(height+label)
                sheet.paste(Image.frombytes('RGB',(width,height),raw),(x,y))
                draw.text((x+4,y+height+4),f'{count:05d} | {count/30:.3f}s',fill='white')
                count+=1
                if count%60==0:save(count-60,count-1)
            if count%60:save(count-count%60,count-1)
            if proc.wait()!=0:raise RuntimeError('ffmpeg failed; read ffmpeg_decode.log')
        except Exception:
            proc.kill();proc.wait();raise
        finally:proc.stdout.close()
    if not count:raise RuntimeError('No decoded frames')
    result={'video':str(a.video),'fps':30,'frames':count,'sheets':len(entries),
            'frames_per_sheet':60,'full_coverage':True,'duration_from_frames_s':count/30,
            'method':'Sequential original-frame decode; aspect-preserving thumbnails; no frame-rate resampling',
            'entries':entries}
    (a.out/'INDEX.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('frames','sheets','full_coverage','duration_from_frames_s')}))


if __name__=='__main__':main()
