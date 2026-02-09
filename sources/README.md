# Sources

This folder contains all collected reference materials for the agentic coding knowledge base. Every source gets its own folder with structured metadata, the processed content (transcripts, summaries), and proper attribution to the original.

## Folder Structure

```
sources/
├── README.md          # This file
├── index.md           # Master index — single place to see all sources and their status
├── youtube/           # YouTube videos
│   └── <slug>/
│       ├── meta.md
│       ├── transcript.md
│       └── summary.md
├── articles/          # Blog posts, written content
│   └── <slug>/
│       ├── meta.md
│       └── summary.md
├── docs/              # Official documentation, specs
│   └── <slug>/
│       ├── meta.md
│       └── summary.md
└── papers/            # Research papers, whitepapers
    └── <slug>/
        ├── meta.md
        └── summary.md
```

## Naming Convention

Each source folder uses the pattern: `YYYY-MM-<short-descriptive-slug>`

Examples:
- `2024-03-fireship-ai-coding-agents`
- `2025-01-anthropic-claude-code-deep-dive`
- `2024-11-simon-willison-llm-cli-tools`

The date is the publication date of the source (month precision is enough).

## Source Files

### `meta.md` — Metadata & Attribution

Every source **must** have a `meta.md`. This is the single source of truth for citation and reference info.

Template:

```markdown
# <Title>

| Field       | Value |
|-------------|-------|
| **URL**     | <original URL> |
| **Type**    | youtube / article / docs / paper |
| **Author**  | <name or channel> |
| **Published** | <YYYY-MM-DD or YYYY-MM> |
| **Duration** | <for videos, e.g. "45 min"> |
| **Tags**    | <comma-separated, e.g. "claude, prompt-engineering, harness-design"> |
| **Status**  | raw / transcript-extracted / summarized / processed |

## Description

<Brief description of what this source covers and why it's relevant.>

## Original Description

<Copy of the original video/article description, for reference.>
```

### `transcript.md` — Full Transcript

For videos and talks. Contains the extracted transcript, cleaned up for readability.

### `summary.md` — Processed Summary

The distilled version of the source. Template:

```markdown
# Summary: <Title>

> Source: [<Title>](<URL>) by <Author>

## TL;DR

<2-3 sentence overview>

## Key Points

- <Point 1>
- <Point 2>
- ...

## Detailed Notes

<Structured notes, organized by topic or chronologically>

## Actionable Takeaways

- <What to apply from this source>

## Quotes

> "<Notable quote>" — <timestamp or section>

## Related Sources

- [<Related source title>](../relative-path/meta.md)
```

## Master Index

The file `index.md` tracks all sources in one place. See that file for the current state of all collected materials.

## Processing Workflow

1. **Add source** — Create the folder and `meta.md` with URL and basic info
2. **Extract content** — For videos: extract transcript. For articles: save key content
3. **Summarize** — Write `summary.md` with key points and takeaways
4. **Tag and index** — Update `index.md`, add relevant tags
5. **Cross-reference** — Link related sources to each other
