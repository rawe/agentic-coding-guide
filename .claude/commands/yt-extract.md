---
description: Extract metadata and transcript from a YouTube video into an output folder (default: sources/youtube).
argument-hint: [youtube-url] [output-dir]
context: fork
---

Load the `yt-processing` skill.

Parse `$ARGUMENTS`: first argument is the YouTube URL, second argument is an optional output directory (default: `sources/youtube`).

Extract the video following all steps in the skill (run extraction script, enrich metadata, verify output). If an output directory is provided, use it as the target for the extraction.

After extraction, append an entry to `sources/index.md` (see column format in `sources/README.md`).
