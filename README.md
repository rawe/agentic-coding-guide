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
└── tools/                 # Scripts for processing materials (phase 3)
```

## Source Types

| Type | Folder | Description |
|------|--------|-------------|
| YouTube videos | `sources/youtube/` | Conference talks, tutorials, deep dives |
| Articles | `sources/articles/` | Blog posts, written tutorials |
| Documentation | `sources/docs/` | Official docs, specs, READMEs |
| Papers | `sources/papers/` | Research papers, whitepapers |

## How to Contribute a Source

1. Add an entry to `sources/index.md`
2. Create a folder under the appropriate type directory
3. Fill in the `meta.md` template
4. Process the source (extract transcript, write summary)
5. Update the index status to `processed`

See [sources/README.md](sources/README.md) for detailed instructions and templates.
