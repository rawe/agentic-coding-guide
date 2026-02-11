# Sources

This folder contains all collected reference materials for the agentic coding knowledge base. Every source gets its own folder with structured metadata, the processed content (transcripts, summaries), and proper attribution to the original.

## Folder Structure

```
sources/
├── README.md          # This file
├── index.md           # Master index — single place to see all sources
├── youtube/           # YouTube videos
│   └── <slug>/
│       ├── meta.md
│       ├── transcript.md
│       ├── summary.md
│       └── notes.md       # optional: personal takeaways
└── docs/              # Documents (PDFs, guides, whitepapers, etc.)
    └── <slug>/
        ├── _raw-source/   # gitignored, original binary
        ├── meta.md
        ├── content.md
        ├── summary.md
        └── notes.md       # optional: personal takeaways
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

| Field         | Value |
|---------------|-------|
| **URL**       | <original URL> |
| **Type**      | youtube / docs |
| **Channel**   | <name or channel> |
| **Published** | <YYYY-MM-DD or YYYY-MM> |
| **Duration**  | <for videos, e.g. "20 min"> |
| **Category**  | <e.g. "Science & Technology"> |
| **Tags**      | <comma-separated, e.g. "context-engineering, claude-code, harness-design"> |

## Description

<Original description from the source.>
```

For YouTube videos, `meta.md` and `transcript.md` are auto-generated:

```
uv run .claude/skills/yt-extract/scripts/yt-extract.py <youtube-url>
```

Or via the skill: `/yt-extract <youtube-url>`

### `transcript.md` — Full Transcript

For videos and talks. Contains the extracted transcript, cleaned up for readability.

### `summary.md` — Processed Summary

The distilled version of the source. Three sections, no filler.

```markdown
# <Title>

> Source: [<Title>](<URL>) by <Channel>

## Overview

<2-3 sentences: what it covers, who the speaker is, why it matters.>

## Key Takeaways

- <Core insights — each point self-contained>

## Notes

### <Topic A>

<Substance organized by topic, not chronologically.
Concepts, techniques, examples. Inline quotes where relevant.>

### <Topic B>

...
```

For YouTube videos, use the skill `/yt-summarize <source-folder-path>` for guided summarization.

### `notes.md` — Personal Takeaways

Optional. Personal observations, conclusions, and connections added after the summary. This is where subjective interpretation lives — what matters most for building guides, what to apply, what to investigate further.

## Master Index

The file `index.md` tracks all sources in one place. See that file for the current state of all collected materials.

## Processing Workflow

### YouTube Videos

Use the skills for extraction and summarization:

1. Skill `/yt-extract <url>` — creates folder, `meta.md`, and `transcript.md`
2. Skill `/yt-summarize <source-folder-path>` — interactive section-by-section summarization
3. Update `index.md`

### Documents

Use the command for extraction:

1. Command `/doc-extract <url-or-filepath>` — creates folder, downloads/copies file, converts to `content.md`, enriches `meta.md`
2. Update `index.md`
