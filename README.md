# Agentic Coding — Best Practices & Knowledge Base

A personal knowledge base for collecting, processing, and documenting best practices around agentic coding — working effectively with AI coding agents across multiple dimensions: steering agents, building harnesses, prompt engineering, workflow design, and more.

## Project Phases

1. **Material Collection** (current) — Gather and process source materials (videos, articles, docs)
2. **Guide Writing** — Distill processed sources into actionable guides and best practices
3. **Tooling** — Build scripts to automate material processing (transcript extraction, summarization)

## Project Structure

```
.
├── README.md              # This file — project overview
├── sources/               # All collected reference materials
│   ├── README.md          # How to add, organize, and process sources
│   ├── index.md           # Master index of all sources with status
│   └── youtube/           # YouTube video sources (one folder per video)
│       └── <slug>/        # e.g. "2024-03-fireship-ai-agents"
│           ├── meta.md    # URL, title, author, date, tags
│           ├── transcript.md   # Full transcript (when extracted)
│           └── summary.md     # Key points, takeaways
├── guides/                # Processed guides and best practices (phase 2)
└── .claude/skills/        # Claude Code skills (e.g. /yt-extract)
```

## Source Types

| Type | Folder | Description |
|------|--------|-------------|
| YouTube videos | `sources/youtube/` | Conference talks, tutorials, deep dives |
| Articles | `sources/articles/` | Blog posts, written tutorials |
| Documentation | `sources/docs/` | Official docs, specs, READMEs |
| Papers | `sources/papers/` | Research papers, whitepapers |

## Adding Sources

For YouTube videos: `/yt-extract <url>` (Claude Code skill) or run the script directly.

For all source types and templates, see [sources/README.md](sources/README.md).
