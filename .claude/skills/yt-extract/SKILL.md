---
name: yt-extract
description: Extract metadata and transcript from a YouTube video into the sources folder.
argument-hint: [youtube-url]
user-invocable: true
---

# YouTube Extraction

Given a YouTube URL via `$ARGUMENTS`:

1. Run the extraction script:
   ```
   uv run .claude/skills/yt-extract/scripts/yt-extract.py '$ARGUMENTS'
   ```
2. Add relevant tags to the generated `meta.md`
3. Append entry to `sources/index.md` (see column format in `sources/README.md`)

Output structure and field definitions: see [sources/README.md](../../../sources/README.md).
