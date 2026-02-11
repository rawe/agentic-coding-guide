# Document Source Structure

## Folder Layout

```
sources/docs/<YYYY-MM-slug>/
├── _raw-source/        ← gitignored, original binary (PDF, DOCX, etc.)
│   └── <original-filename>
├── meta.md             ← metadata and attribution
├── content.md          ← markdown conversion of the document
├── summary.md          ← structured summary (created separately via /summarize)
└── notes.md            ← optional: personal takeaways
```

- `_raw-source/` is gitignored via `sources/**/_raw-source/`
- Only text files (`meta.md`, `content.md`, `summary.md`) get committed

## Slug Convention

Pattern: `YYYY-MM-short-descriptive-slug`

Examples:
- `2026-02-anthropic-complete-guide-building-skills-for-claude`
- `2025-11-openai-prompt-engineering-guide`

Date = publication or retrieval date (month precision).

## meta.md Template

```markdown
# <Title>

| Field         | Value |
|---------------|-------|
| **URL**       | <source URL or "local"> |
| **Type**      | docs |
| **Author**    | <author or organization> |
| **Published** | <YYYY-MM-DD or YYYY-MM or "unknown"> |
| **Retrieved** | <YYYY-MM-DD> |
| **Format**    | <PDF / DOCX / HTML / etc.> |
| **Tags**      | <comma-separated, lowercase, e.g. "skills, claude-code, prompt-engineering"> |

## Summary

<2 sentences max. What this document covers and why it matters. No filler.>
```

### Field Rules

- **Tags**: 3-8 lowercase keywords, comma-separated. Derived from content topics.
- **Summary**: Exactly 2 sentences. First sentence = what the document is about. Second sentence = key value or insight.
- **Published**: Use document's own date if available, otherwise "unknown".
- **Author**: Organization or person name. Never "unknown" if derivable from content.
