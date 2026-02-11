---
description: Download/copy a document and extract its content as markdown into sources/docs.
argument-hint: [url-or-filepath]
context: fork
---

Load the `doc-processing` skill, then process the document at `$ARGUMENTS`.

Determine if the argument is a URL (starts with `http`) or a local file path.
Follow all steps in the skill (obtain, convert, create meta.md, enrich metadata, update index).
