---
description: Download/copy a document and extract its content as markdown into sources/docs.
argument-hint: [url-or-filepath]
---

Load the `doc-extract` skill, then process the document at `$ARGUMENTS`.

Determine if the argument is a URL (starts with `http`) or a local file path.

1. **If URL**: download with `doc-download.py`, then convert with `doc-convert.py`
2. **If local path**: copy into `_raw-source/`, then convert with `doc-convert.py`

Follow all steps in the skill: create slug, folder structure, `meta.md`, convert to `content.md`, update `sources/index.md`.
