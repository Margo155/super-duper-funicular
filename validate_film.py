#!/usr/bin/env python3
"""Technical film/PTS/SRT checks, not a visual or listening certification."""
import argparse
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def probe(arguments):
    proc = subprocess.run(['ffprobe', '-v', 'error', *arguments, '-of', 'json'],
                          text=True, capture_output=True, check=True)
    if proc.stderr.strip():
        raise ValueError('ffprobe reported decoding/inspection errors: '+proc.stderr.strip())
    return json.loads(proc.stdout)


def seconds(s):
    h,m,v,ms = [int(x) for x in re.split(r'[:,.]', s)]
    return h*3600+m*60+v+ms/1000


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('video',type=Path)
    ap.add_argument('--srt',type=Path,required=True)
    ap.add_argument('--report',type=Path,required=True)
    ap.add_argument('--voice-text',type=Path)
    ap.add_argument('--width',type=int,default=1920)
    ap.add_argument('--height',type=int,default=1080)
    ap.add_argument('--fps',type=int,default=30)
    ap.add_argument('--duration',type=float,default=600.0)
    ap.add_argument('--frames',type=int,default=18000)
    a=ap.parse_args();checks={};errors=[];summary={}

    def check(name,condition,detail):
        checks[name]={'passed':bool(condition),'detail':detail}
        if not condition:errors.append(name)

    try:
        p=probe(['-show_streams','-show_format',str(a.video)])
        vv=[s for s in p['streams'] if s['codec_type']=='video']
        aa=[s for s in p['streams'] if s['codec_type']=='audio']
        check('one_video',len(vv)==1,len(vv));check('audio_present',bool(aa),len(aa))
        if not vv:raise ValueError('Missing video')
        v=vv[0];duration=float(v.get('duration',p['format']['duration']))
        check('dimensions',[v['width'],v['height']]==[a.width,a.height],[v['width'],v['height']])
        check('average_fps',Fraction(v['avg_frame_rate'])==a.fps,v['avg_frame_rate'])
        check('reported_fps',Fraction(v['r_frame_rate'])==a.fps,v['r_frame_rate'])
        check('video_duration',abs(duration-a.duration)<=.001,{'actual':duration,'expected':a.duration})
        check('h264',v.get('codec_name')=='h264',v.get('codec_name'))
        check('yuv420p',v.get('pix_fmt')=='yuv420p',v.get('pix_fmt'))
        check('square_pixels',v.get('sample_aspect_ratio','1:1') in ('1:1','N/A'),v.get('sample_aspect_ratio'))
        ptsdata=probe(['-select_streams','v:0','-show_frames','-show_entries',
                       'frame=best_effort_timestamp_time',str(a.video)])
        timestamps=[float(f['best_effort_timestamp_time']) for f in ptsdata['frames']]
        check('decoded_frames',len(timestamps)==a.frames,{'actual':len(timestamps),'expected':a.frames})
        check('first_frame_time',bool(timestamps) and abs(timestamps[0])<=.000002,
              timestamps[0] if timestamps else None)
        maximum_error=max((abs((y-x)-1/a.fps) for x,y in zip(timestamps,timestamps[1:])),default=1)
        check('constant_frame_timestamps',len(timestamps)>1 and maximum_error<=.000002,
              {'max_delta_error_s':maximum_error})
        if aa:
            ad=float(aa[0].get('duration',p['format']['duration']))
            check('audio_duration',abs(ad-a.duration)<=.15,ad)
            check('aac',aa[0].get('codec_name')=='aac',aa[0].get('codec_name'))
        events=[];previous_end=0.0
        for block in re.split(r'\n\s*\n',a.srt.read_text(encoding='utf-8-sig').strip()):
            lines=block.strip().splitlines()
            if len(lines)<3 or '-->' not in lines[1]:raise ValueError('Malformed SRT event')
            left,right=[x.strip() for x in lines[1].split('-->')]
            start,end=seconds(left),seconds(right);text=' '.join(lines[2:]).strip()
            number=len(events)+1
            check(f'caption_{number}_bounds',0<=start<end<=a.duration+.001 and start>=previous_end-.001,[start,end])
            check(f'caption_{number}_words',1<=len(text.split())<=4,text)
            previous_end=end;events.append(text)
        check('captions_present',bool(events),len(events))
        if a.voice_text:
            expected=' '.join(a.voice_text.read_text(encoding='utf-8').split())
            actual=' '.join(' '.join(events).split())
            check('caption_text_covers_voice_text',actual==expected,
                  {'caption_words':len(actual.split()),'expected_words':len(expected.split())})
        summary={'duration_s':duration,'frames':len(timestamps),'fps':a.fps,
                 'dimensions':[v['width'],v['height']],'caption_events':len(events)}
    except (OSError,ValueError,KeyError,ZeroDivisionError,subprocess.CalledProcessError) as exc:
        errors.append('inspection_failed');checks['inspection_failed']={'passed':False,'detail':str(exc)}
    report={'status':'passed' if not errors else 'failed','summary':summary,
            'failed_checks':errors,'checks':checks,'limitations':[
                'Does not listen to or transcribe audio; an audio stream may be silent or wrong',
                'Caption text/bounds do not prove word-level alignment to recorded speech',
                'Does not assess image quality, character rig, history, physics or action continuity']}
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'summary':summary,'failed_checks':errors},ensure_ascii=False))
    return 0 if not errors else 1


if __name__=='__main__':sys.exit(main())
