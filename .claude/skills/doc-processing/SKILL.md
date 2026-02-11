---
name: doc-processing
description: Extract and convert documents (PDF, DOCX, etc.) into the sources/docs knowledge base. Use when processing a document from a URL or local file into a structured source folder with metadata and markdown content.
user-invocable: false
---

# Document Extraction

Extract a document into `sources/docs/` with structured metadata and markdown content.

For folder layout, slug convention, and `meta.md` template see [references/structure.md](references/structure.md).

## Process

### 1. Obtain document and create folder

Determine slug (`YYYY-MM-short-descriptive-slug`), create folder structure.

**If URL** — download into `_raw-source/`:
```
uv run .claude/skills/doc-processing/scripts/doc-download.py '<URL>' 'sources/docs/<slug>/_raw-source'
```

**If local file** — copy into `_raw-source/`:
```
mkdir -p sources/docs/<slug>/_raw-source
cp <local-path> sources/docs/<slug>/_raw-source/
```

### 2. Convert to markdown

```
uv run .claude/skills/doc-processing/scripts/doc-convert.py 'sources/docs/<slug>/_raw-source/<filename>' 'sources/docs/<slug>/content.md'
```

### 3. Create meta.md

Write initial `meta.md` using the template from [references/structure.md](references/structure.md).
Fill in known fields: title, URL, author, retrieved date, format.

### 4. Enrich metadata

Read `content.md` and enrich `meta.md` with:
- **Tags**: 3-8 keywords derived from the document's topics
- **Summary**: Exactly 2 sentences — what it covers and why it matters
- **Published**: Extract from content if available

Follow the field rules in [references/structure.md](references/structure.md).

### 5. Update index

Add entry to `sources/index.md`.

## Script Interfaces

| Script | Input | Output (stdout) |
|--------|-------|-----------------|
| `doc-download.py` | `<url> <output-folder>` | `file:`, `size_kb:`, `filename:` |
| `doc-convert.py` | `<input-file> <output-file>` | `file:`, `size_kb:`, `lines:`, `chars:` |

Both use `uv run` with inline dependencies — no global installs needed.
