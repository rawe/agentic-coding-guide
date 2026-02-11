# /// script
# dependencies = ["httpx"]
# requires-python = ">=3.9"
# ///
"""
Download a document from a URL to a target folder.

Usage: uv run doc-download.py <url> <output-folder>
"""

import argparse
from pathlib import Path
from urllib.parse import unquote, urlparse

import httpx


def filename_from_url(url: str) -> str:
    path = urlparse(url).path
    name = unquote(Path(path).name)
    return name if name else "document"


def main():
    parser = argparse.ArgumentParser(description="Download a document from a URL")
    parser.add_argument("url", help="URL to download")
    parser.add_argument("output_folder", help="Folder to save the file into")
    args = parser.parse_args()

    folder = Path(args.output_folder)
    folder.mkdir(parents=True, exist_ok=True)

    filename = filename_from_url(args.url)
    dest = folder / filename

    with httpx.stream("GET", args.url, follow_redirects=True) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_bytes():
                f.write(chunk)

    size_kb = dest.stat().st_size / 1024
    print(f"file: {dest}")
    print(f"size_kb: {size_kb:.1f}")
    print(f"filename: {filename}")


if __name__ == "__main__":
    main()
