#!/usr/bin/env python3
"""Decode every original frame into 10x6 sheets; requires ffmpeg, ffprobe, Pillow."""
import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw


def read_exact(pipe, count):
    chunks = []
    remaining = count
    while remaining:
        chunk = pipe.read(remaining)
        if not chunk:
            break
        chunks.append(chunk)
        remaining -= len(chunk)
    data = b"".join(chunks)
    if data and len(data) != count:
        raise RuntimeError("Truncated raw frame")
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("video", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_streams",
        "-of", "json", str(args.video),
    ], text=True))
    fps = Fraction(probe["streams"][0]["avg_frame_rate"])
    if fps != Fraction(30, 1):
        raise ValueError(f"Expected original 30 fps media, got {fps}; no frame resampling performed")
    args.out.mkdir(parents=True, exist_ok=True)
    w, h, label_h = 144, 256, 24
    per_sheet = 60
    sheet = None
    entries = []
    count = 0

    def save_sheet(im, first, last):
        number = len(entries) + 1
        filename = f"sheet_{number:03d}_{first:05d}-{last:05d}.jpg"
        im.save(args.out / filename, quality=92)
        entries.append({"file": filename, "first_frame": first, "last_frame_inclusive": last,
                        "frames": last-first+1, "start_s": first/30,
                        "end_s_exclusive": (last+1)/30})

    with (args.out / "ffmpeg_decode.log").open("wb") as log:
        command = ["ffmpeg", "-v", "error", "-i", str(args.video), "-map", "0:v:0",
                   "-an", "-vf", f"scale={w}:{h}", "-fps_mode", "passthrough",
                   "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1"]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=log, stdin=subprocess.DEVNULL)
        try:
            while True:
                raw = read_exact(proc.stdout, w*h*3)
                if not raw:
                    break
                local = count % per_sheet
                if local == 0:
                    sheet = Image.new("RGB", (w*10, (h+label_h)*6), (23, 25, 30))
                    draw = ImageDraw.Draw(sheet)
                x, y = (local % 10)*w, (local // 10)*(h+label_h)
                sheet.paste(Image.frombytes("RGB", (w, h), raw), (x, y))
                draw.text((x+3, y+h+4), f"{count:05d}  {count/30:.3f}s", fill="white")
                count += 1
                if count % per_sheet == 0:
                    save_sheet(sheet, count-per_sheet, count-1)
            if count % per_sheet:
                save_sheet(sheet, count-count % per_sheet, count-1)
            if proc.wait() != 0:
                raise RuntimeError("ffmpeg failed; see ffmpeg_decode.log")
        except Exception:
            proc.kill()
            proc.wait()
            raise
        finally:
            proc.stdout.close()
    if not count:
        raise RuntimeError("No frames decoded")
    result = {"video": str(args.video), "fps": 30, "frames": count,
              "sheets": len(entries), "frames_per_full_sheet": per_sheet,
              "duration_from_frames_s": count/30, "full_coverage": True,
              "method": "Sequential decode; no temporal resampling; thumbnails are not full-resolution quality checks",
              "entries": entries}
    (args.out / "INDEX.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["frames", "sheets", "duration_from_frames_s", "full_coverage"]}))


if __name__ == "__main__":
    main()
