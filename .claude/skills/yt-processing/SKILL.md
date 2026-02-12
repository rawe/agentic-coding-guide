---
name: yt-processing
description: Extract YouTube video metadata and transcripts into source folders, or list recent videos from a channel. Use when working with YouTube sources, extracting videos, browsing channels, or preparing video content for the knowledge base.
user-invocable: false
---

# YouTube Processing

Two tools for working with YouTube as a source: extract a single video into the knowledge base, or browse a channel's recent uploads.

For folder layout, slug convention, and `meta.md` template see [sources/README.md](../../../sources/README.md).

## Video Extraction

Extract metadata and transcript from a single YouTube video into a structured source folder.

### Output structure

Each extracted video produces a subfolder with:

- `meta.md` — title, URL, channel, published date, duration, category, tags, description
- `transcript.md` — timestamped transcript (if available)

Subfolder naming: `YYYY-MM-channel-title` (auto-generated slug, max 80 chars).

### Process

1. **Extract video**
   ```
   uv run .claude/skills/yt-processing/scripts/yt-extract.py '<youtube-url>'
   ```
   Creates the subfolder with `meta.md` and `transcript.md`.

2. **Enrich metadata** — read the generated `meta.md` and add/refine:
   - **Tags**: 3-8 topic keywords relevant to the knowledge base (go beyond auto-generated YouTube tags)
   - **Summary field**: if missing, add exactly 2 sentences — what it covers and why it matters

3. **Verify output** — check that `meta.md` has all required fields and `transcript.md` was created. If transcript is unavailable, note it — the source can still be used with manual transcription.

## Channel Listing

List recent videos from a YouTube channel. Use this for discovery — browsing what's available before extracting specific videos.

```
uv run .claude/skills/yt-processing/scripts/yt-channel-list.py '<channel>' [-n count]
```

Returns a numbered list to stdout with title, URL, date, duration, and view count for each video. No files are created.

## Script Interfaces

| Script | Purpose | Usage |
|--------|---------|-------|
| `yt-extract.py` | Extract single video metadata + transcript | `uv run .claude/skills/yt-processing/scripts/yt-extract.py '<url>' [--out dir]` |
| `yt-channel-list.py` | List recent videos from a channel | `uv run .claude/skills/yt-processing/scripts/yt-channel-list.py '<channel>' [-n count]` |

### yt-extract.py

- Input: YouTube video URL
- `--out <dir>`: base directory for the slug subfolder (default: `sources/youtube`)
- Output: creates `<dir>/<slug>/meta.md` and `<dir>/<slug>/transcript.md`
- Prints folder path and slug to stdout

### yt-channel-list.py

- Input: channel URL, handle (`@Name`), or bare channel name
- `-n` flag: number of videos to list (default: 10)
- Output: numbered list to stdout with title, URL, date, duration, view count

Both scripts use `uv run` with inline dependencies — no global installs needed.
