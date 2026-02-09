# /// script
# dependencies = ["yt-dlp", "youtube-transcript-api"]
# requires-python = ">=3.9"
# ///
"""
Extract metadata and transcript from a YouTube video.
Creates a source folder with meta.md and transcript.md.

Usage: uv run tools/yt-extract.py <youtube-url> [--out sources/youtube]
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    patterns = [
        r'(?:v=)([a-zA-Z0-9_-]{11})',
        r'(?:youtu\.be/)([a-zA-Z0-9_-]{11})',
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    sys.exit(f"Cannot extract video ID from: {url}")


def fetch_metadata(url: str) -> dict:
    opts = {"quiet": True, "no_warnings": True, "skip_download": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        return ydl.extract_info(url, download=False)


def fetch_transcript(video_id: str) -> list[dict]:
    ytt = YouTubeTranscriptApi()
    transcript = ytt.fetch(video_id=video_id)
    return [{"start": s.start, "text": s.text} for s in transcript.snippets]


def make_slug(info: dict) -> str:
    upload = info.get("upload_date", "")
    year_month = f"{upload[:4]}-{upload[4:6]}" if len(upload) >= 6 else date.today().strftime("%Y-%m")
    channel = info.get("channel", "unknown")
    title = info.get("title", "untitled")
    raw = f"{year_month}-{channel}-{title}"
    slug = re.sub(r'[^a-z0-9]+', '-', raw.lower()).strip('-')
    return slug[:80]


def format_duration(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h {m}min"
    return f"{m} min"


def format_timestamp(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def write_meta(folder: Path, info: dict, url: str):
    upload = info.get("upload_date", "")
    published = f"{upload[:4]}-{upload[4:6]}-{upload[6:8]}" if len(upload) == 8 else "unknown"
    duration = format_duration(info.get("duration", 0))
    tags = ", ".join(info.get("tags", [])) if info.get("tags") else ""
    categories = ", ".join(info.get("categories", []))
    description = info.get("description", "").strip()

    content = f"""# {info.get("title", "Untitled")}

| Field         | Value |
|---------------|-------|
| **URL**       | {url} |
| **Type**      | youtube |
| **Channel**   | {info.get("channel", "unknown")} |
| **Published** | {published} |
| **Duration**  | {duration} |
| **Category**  | {categories} |
| **Tags**      | {tags} |

## Description

{description}
"""
    (folder / "meta.md").write_text(content)


def write_transcript(folder: Path, segments: list[dict]):
    lines = ["# Transcript\n"]
    for seg in segments:
        ts = format_timestamp(seg["start"])
        text = seg["text"].strip()
        if text:
            lines.append(f"[{ts}] {text}")
    (folder / "transcript.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Extract YouTube video metadata and transcript")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--out", default="sources/youtube", help="Output directory (default: sources/youtube)")
    args = parser.parse_args()

    url = args.url
    video_id = extract_video_id(url)
    clean_url = f"https://www.youtube.com/watch?v={video_id}"

    print(f"Fetching metadata for {video_id}...")
    info = fetch_metadata(clean_url)

    slug = make_slug(info)
    folder = Path(args.out) / slug
    folder.mkdir(parents=True, exist_ok=True)

    print(f"Writing to {folder}/")
    write_meta(folder, info, clean_url)

    print("Fetching transcript...")
    try:
        segments = fetch_transcript(video_id)
        write_transcript(folder, segments)
        print(f"Done. {len(segments)} transcript segments written.")
    except Exception as e:
        print(f"Transcript unavailable: {e}")
        print("Created meta.md only. Transcript must be added manually.")

    print(f"\nSource folder: {folder}")
    print(f"Slug: {slug}")


if __name__ == "__main__":
    main()
