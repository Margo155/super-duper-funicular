# Continuity and release checks — Episode 002

## Approved evidence

assets/hero_reference.png is the original head reference.
assets/continuity/ODDPLOT_APPROVED_TEST_001_V3.mp4 is the accepted 15-second style test, 1080x1920/30 fps.
The PNGs are frames extracted from that V3, scaled to 540x960 for inspection:

| File | Time in V3 | Purpose |
|---|---:|---|
| hero_feet_approved.png | 3.20 s | Both legs connect to shoes; grounded pose |
| hero_valve_pose_approved.png | 4.80 s | Head/body proportions, orange vest, arm/prop interaction |
| hero_expression_approved.png | 12.40 s | Expressive eyebrows, mouth and head tilt |

Retain the proportions and flat 2D drawing. Do not carry over episode-specific ship props. V1/V2 failure: legs bent/lifted while shoes stayed on the floor. V3 corrected it. Prevent that rig error in all new actions, including a hand reaching high, a body lean and knee bends.

## Before rendering the full episode

- Read the actual reference images/video, not only their descriptions.
- Verify coin-to-hand attachment followed by coin-to-shelf attachment at release.
- Verify shelf is parented to the pendulum, pendulum rotates about a fixed pivot, and the rod geometry never shrinks.
- Render a few representative frames and a short local animation segment to check the rig and quality; continue to the full episode autonomously when successful.
- Generate the narration first and keep its wording unchanged. Re-time the draft storyboard/SRT to it.

## Final technical pass

Run from the package root (substitute actual paths):

```bash
python3 scripts/validate_video.py output/EPISODE_002_FINAL.mp4 --srt output/EPISODE_002_SUBTITLES.srt --report output/QA_REPORT.json
python3 scripts/make_review_sheets.py output/EPISODE_002_FINAL.mp4 --out output/review_sheets
ffmpeg -hide_banner -i output/EPISODE_002_FINAL.mp4 -vn -af volumedetect -f null - 2> output/QA_AUDIO_CHECK.txt
```

The validator decodes/counts the video frames with ffprobe and checks size, frame rate, duration, audio presence and basic subtitle bounds. It does NOT establish audio intelligibility, exact word alignment, foot contact, identities or correctness of physics. A successful JSON is not a substitute for visual/audio review.

## Visual/audio pass

Inspect the full-coverage sheets and normal-speed playback. For any suspect motion inspect full-resolution consecutive frames. Record actual reviewed frame/time ranges, fixes and remaining limitations in VISUAL_QA.md.

- Every visible leg is attached continuously to its shoe. Knees, ankles, elbows and wrists remain connected. Planted feet do not drift. Show both shoes clearly in multiple medium/wide shots.
- Hero head, hair, vest, eye style and scale remain consistent. Expressions respond to the coin and explanation.
- No hand penetrates the tray; the coin is not duplicated across hand and shelf; the stack does not slide through the rod or hover.
- Normal-rate pendulum: about two seconds per beat / four seconds for a complete out-and-back cycle. No dramatic tempo increase or amplitude jump after adding one penny.
- Numeric overlay means rate change: approximately +0.4 seconds PER DAY per added old penny relative to the prior rate. No instantaneous 0.4-second reset. Time compression and enlarged differences are labelled.
- Physical rod stays the same length. Effective-length graphic is a labelled model, not a reconstruction measurement. Do not reduce all physical pendulum behaviour to centre-of-mass height alone.
- Four clock faces are explained without needing four separate detailed exterior models. Big Ben is not labelled as the pendulum or mechanism.
- Image is clean, lit consistently, with legible coin and face; check rails/gear silhouettes for aliasing, noise and flicker.
- Captions remain in a consistent raised band, 1–4 words per event, readable and aligned to actual voice. No sentence is clipped at the end.
- Compare the clean narration words against audio/VOICEOVER_EN.txt. Confirm no missing/extra words; listen to 'Elizabeth Tower', 'pendulum', 'two fifths' and 'five tonnes'.
- Sound is audible, clear and not clipped; coin clicks/ticking/music do not mask narration. A reference clip or a subtitle track alone is not new narration.

Nominal 54 seconds means 1620 frames. If real voice leads to another duration within 50–60 seconds, use the actual frame count and update all labels. Do not claim a specific frame count without probing the exported MP4.
