#!/usr/bin/env python3
"""Technical MP4/SRT checks. Does not certify visual quality or word alignment."""
import argparse
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def srt_seconds(value):
    h, m, s, ms = [int(v) for v in re.split(r"[:,.]", value)]
    return h * 3600 + m * 60 + s + ms / 1000


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("video", type=Path)
    ap.add_argument("--srt", type=Path, required=True)
    ap.add_argument("--report", type=Path, required=True)
    ap.add_argument("--min-duration", type=float, default=50.0)
    ap.add_argument("--max-duration", type=float, default=60.0)
    args = ap.parse_args()
    errors = []
    checks = {}

    def check(name, ok, detail):
        checks[name] = {"passed": bool(ok), "detail": detail}
        if not ok:
            errors.append(name)

    try:
        completed = subprocess.run(
            ["ffprobe", "-v", "error", "-count_frames", "-show_streams",
             "-show_format", "-of", "json", str(args.video)],
            check=True, capture_output=True, text=True,
        )
        probe = json.loads(completed.stdout)
        check("decode_errors", not completed.stderr.strip(), completed.stderr.strip())
        videos = [s for s in probe["streams"] if s["codec_type"] == "video"]
        audios = [s for s in probe["streams"] if s["codec_type"] == "audio"]
        check("one_video_stream", len(videos) == 1, len(videos))
        check("audio_stream_present", bool(audios), len(audios))
        if not videos:
            raise ValueError("No video stream")
        v = videos[0]
        duration = float(v.get("duration", probe["format"]["duration"]))
        fps = Fraction(v["avg_frame_rate"])
        frame_count = int(v["nb_read_frames"])
        check("resolution", (v["width"], v["height"]) == (1080, 1920),
              [v["width"], v["height"]])
        check("fps", fps == Fraction(30, 1), str(fps))
        check("reported_frame_rate", Fraction(v["r_frame_rate"]) == Fraction(30, 1), v["r_frame_rate"])
        check("square_pixels", v.get("sample_aspect_ratio", "1:1") in ("1:1", "N/A"),
              v.get("sample_aspect_ratio"))
        check("duration", args.min_duration <= duration <= args.max_duration,
              {"seconds": duration, "allowed": [args.min_duration, args.max_duration]})
        check("decoded_frames_match_duration", abs(frame_count - duration * 30) < 0.1,
              {"frames": frame_count, "duration_times_30": duration * 30})
        check("video_codec", v.get("codec_name") == "h264", v.get("codec_name"))
        if audios:
            a = audios[0]
            ad = float(a.get("duration", probe["format"]["duration"]))
            check("audio_covers_video", abs(ad - duration) <= 0.15,
                  {"video_s": duration, "audio_s": ad})
            check("audio_codec", a.get("codec_name") == "aac", a.get("codec_name"))

        text = args.srt.read_text(encoding="utf-8-sig")
        events = []
        previous_end = 0.0
        for block in re.split(r"\n\s*\n", text.strip()):
            lines = block.strip().splitlines()
            if len(lines) < 3 or "-->" not in lines[1]:
                errors.append("malformed_srt_block")
                continue
            left, right = [x.strip() for x in lines[1].split("-->")]
            start, end = srt_seconds(left), srt_seconds(right)
            content = " ".join(lines[2:]).strip()
            ok = 0 <= start < end <= duration + 0.001 and start >= previous_end - 0.001
            check(f"caption_{len(events)+1}_bounds", ok, [start, end])
            count = len(content.split())
            check(f"caption_{len(events)+1}_short_group", 1 <= count <= 4,
                  {"words": count, "text": content})
            previous_end = end
            events.append({"start": start, "end": end, "text": content})
        check("captions_present", bool(events), len(events))
        summary = {"duration_s": duration, "fps": str(fps), "decoded_frames": frame_count,
                   "dimensions": [v["width"], v["height"]], "caption_events": len(events)}
    except (OSError, ValueError, KeyError, ZeroDivisionError, subprocess.CalledProcessError) as exc:
        errors.append("inspection_failed")
        checks["inspection_failed"] = {"passed": False, "detail": str(exc)}
        summary = {}

    report = {"status": "passed" if not errors else "failed", "video": str(args.video),
              "srt": str(args.srt), "summary": summary, "failed_checks": errors,
              "checks": checks, "limitations": [
                  "Does not verify constant frame timestamps beyond stream rates/count/duration",
                  "Audio presence does not prove narration, intelligibility, loudness or wording",
                  "SRT bounds do not prove audio-word synchronization",
                  "Does not certify rig continuity, shadows, physics, brand identity or image quality",
              ]}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "summary": summary,
                      "failed_checks": errors}, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
