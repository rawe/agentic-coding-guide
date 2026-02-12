# /// script
# dependencies = ["yt-dlp"]
# requires-python = ">=3.9"
# ///
"""
List recent videos from a YouTube channel.

Usage: uv run yt-channel-list.py <channel-url-or-handle> [-n 10]
"""

import argparse
import sys
from datetime import datetime, timezone

import yt_dlp


def normalize_channel_url(input_str: str) -> str:
    """Turn a handle like @NickChapsas into a full channel URL."""
    if input_str.startswith("@"):
        return f"https://www.youtube.com/{input_str}/videos"
    if "youtube.com" in input_str:
        url = input_str.rstrip("/")
        if not url.endswith("/videos"):
            url += "/videos"
        return url
    # Assume it's a handle without @
    return f"https://www.youtube.com/@{input_str}/videos"


def fetch_channel_videos(url: str, count: int) -> list[dict]:
    opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "playlist_items": f"1:{count}",
        "extractor_args": {"youtubetab": {"approximate_date": [""]}},
    }
    print(f"Fetching up to {count} videos from {url}...", file=sys.stderr)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info.get("entries", []) or []


def format_duration(seconds) -> str:
    if not seconds:
        return "?"
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def format_views(count) -> str:
    if not count:
        return "?"
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    if count >= 1_000:
        return f"{count / 1_000:.1f}K"
    return str(count)


def main():
    parser = argparse.ArgumentParser(description="List recent videos from a YouTube channel")
    parser.add_argument("channel", help="Channel URL, handle (@Name), or name")
    parser.add_argument("-n", "--count", type=int, default=10, help="Number of videos (default: 10)")
    args = parser.parse_args()

    url = normalize_channel_url(args.channel)
    entries = fetch_channel_videos(url, args.count)

    if not entries:
        print("No videos found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(entries)} videos.\n", file=sys.stderr)

    for i, entry in enumerate(entries, 1):
        title = entry.get("title", "Untitled")
        video_url = entry.get("url", "")
        if video_url and not video_url.startswith("http"):
            video_url = f"https://www.youtube.com/watch?v={video_url}"
        duration = format_duration(entry.get("duration"))
        views = format_views(entry.get("view_count"))
        timestamp = entry.get("timestamp")
        if timestamp:
            date_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")
        else:
            upload_date = entry.get("upload_date", "")
            if len(upload_date) == 8:
                date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
            else:
                date_str = "?"

        print(f"{i}. {title}")
        print(f"   {video_url}")
        print(f"   {date_str} | {duration} | {views} views")
        print()


if __name__ == "__main__":
    main()
