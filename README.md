# Production QA helpers

Requirements: Python 3, ffmpeg and ffprobe on PATH. Sheet generation also needs Pillow (`python3 -m pip install Pillow` if permitted). These helpers inspect an existing rendered video; they do not render the new episode or generate speech.

From the package root:

```bash
python3 scripts/validate_video.py output/EPISODE_002_FINAL.mp4 --srt output/EPISODE_002_SUBTITLES.srt --report output/QA_REPORT.json
python3 scripts/make_review_sheets.py output/EPISODE_002_FINAL.mp4 --out output/review_sheets
```

The nominal 54-second / 1620-frame edit produces 27 sheets of 60 frames. A different accepted duration may yield a partial last sheet. Every source frame is decoded without temporal resampling, with frame index/time labels and an INDEX.json coverage map.

Do not call the nominal count a measured result before probing the completed episode. Follow CONTINUITY_AND_QA.md for visual, physics and sound review; a technical pass cannot prove that shoes are attached or words match the narration.
