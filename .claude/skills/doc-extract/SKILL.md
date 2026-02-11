---
name: doc-extract
description: Extract and convert documents (PDF, DOCX, etc.) into the sources/docs knowledge base. Use when processing a document from a URL or local file into a structured source folder with metadata and markdown content.
user-invocable: false
---

# Document Extraction

Extract a document into `sources/docs/` with structured metadata and markdown content.

## Folder Structure

```
sources/docs/<YYYY-MM-slug>/
├── _raw-source/        ← gitignored, original binary
│   └── <filename>
├── meta.md             ← title, URL, author, date, format
└── content.md          ← markdown conversion (committed)
```

`_raw-source/` is gitignored via `sources/**/_raw-source/`.

## Process

### 1. Create source folder and obtain document

Determine the slug using pattern `YYYY-MM-short-descriptive-slug`.

**If URL provided** — download into `_raw-source/`:
```
uv run .claude/skills/doc-extract/scripts/doc-download.py '<URL>' 'sources/docs/<slug>/_raw-source'
```

**If local file provided** — copy into `_raw-source/`:
```
mkdir -p sources/docs/<slug>/_raw-source
cp <local-path> sources/docs/<slug>/_raw-source/
```

### 2. Create meta.md

Write `sources/docs/<slug>/meta.md`:

```markdown
# <Title>

| Field         | Value |
|---------------|-------|
| **URL**       | <url or "local"> |
| **Type**      | docs |
| **Author**    | <author or "unknown"> |
| **Retrieved** | <YYYY-MM-DD> |
| **Format**    | <PDF/DOCX/etc.> |
```

### 3. Convert to markdown

```
uv run .claude/skills/doc-extract/scripts/doc-convert.py 'sources/docs/<slug>/_raw-source/<filename>' 'sources/docs/<slug>/content.md'
```

Output confirms: file path, size_kb, lines, chars.

### 4. Finalize

- Add relevant tags to `meta.md` if known
- Update `sources/index.md` with the new entry

## Script Interfaces

| Script | Input | Output (stdout) |
|--------|-------|-----------------|
| `doc-download.py` | `<url> <output-folder>` | `file:`, `size_kb:`, `filename:` |
| `doc-convert.py` | `<input-file> <output-file>` | `file:`, `size_kb:`, `lines:`, `chars:` |

Both use `uv run` with inline dependencies — no global installs needed.
