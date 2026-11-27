# Helpers for production and review

Python 3, ffmpeg and ffprobe are required. Review sheets also need Pillow. These scripts do not render 3D scenes or generate speech.

Check and concatenate completed visual shot clips:

```bash
python3 scripts/assemble_checked_clips.py --manifest shot_manifest.json --clips output/shot_clips --output output/VISUAL_MASTER.mp4
```

This output is an intermediate VISUAL master, not the completed film. Add new narration, the sound mix and aligned captions in the production edit. Keep final output exactly 600 seconds / 18000 frames.

Validate the completed audiovisual film:

```bash
python3 scripts/validate_film.py output/ODDPLOT_LONG_001_FINAL.mp4 --srt output/SUBTITLES_EN.srt --voice-text audio/VOICEOVER_EN.txt --report output/QA_REPORT.json
python3 scripts/make_review_sheets.py output/ODDPLOT_LONG_001_FINAL.mp4 --out output/review_sheets
```

The validator inspects stream parameters and actual decoded frame timestamps, checks all 18000 frames are present at 30 fps, checks subtitle bounds and optionally compares subtitle text with the supplied voice text. It does not listen to the speech or certify image quality/physics/continuity. Default film targets are 1920x1080, 600 seconds and 18000 frames; override CLI flags only for clearly identified helper tests.

All-frame sheets contain 60 original frames, 10 by 6, with indices and times. For the full film the expected result is 300 sheets. Aspect-preserving 192x108 thumbnails help navigate; inspect full-size consecutive frames for feet, hands, noise and details.

planning/RENDER_PROGRESS_TEMPLATE.json is a template with every shot pending. Copy it into output/RENDER_PROGRESS.json and update with actual completed paths, frame counts and hashes. Do not call pending shots complete.

rebuild_draft_documents.py regenerates only draft planning/script/SRT files from planning/scenes_source.json; it does not render the movie. Run it only when deliberately revising the package. If the spoken words change, remeasure the text and update the timing/measurement report before claiming a duration.
