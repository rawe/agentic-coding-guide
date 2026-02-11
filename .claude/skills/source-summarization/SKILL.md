---
name: source-summarization
description: Process and pattern for interactively summarizing any source in the sources/ knowledge base. Covers YouTube videos, documents, and any source folder containing meta.md and either transcript.md or content.md.
user-invocable: false
---

# Source Summarization

Interactive, section-by-section summarization of a source folder. The folder must contain `meta.md` and either `transcript.md` or `content.md`.

## Process

Work section by section. Present each section as a draft, wait for user feedback before moving on.

### Step 1 — Read source

Read `meta.md` from the folder. Then read whichever content file exists:
- `transcript.md` (YouTube videos, talks)
- `content.md` (documents, PDFs)

Extract from `meta.md`: title, URL, author/channel, type.

### Step 2 — Overview

Draft 2-3 sentences: what the source covers, who created it, why it matters. Present to user for approval.

### Step 3 — Key Takeaways

Extract the core insights as bullet points. Each point self-contained, no filler. Present to user for approval.

### Step 4 — Notes

Organize the substance by topic (not chronologically). Use `###` headers for each topic section. Include concepts, techniques, examples, and relevant quotes inline. Present to user for approval.

### Step 5 — Write summary.md

Assemble approved sections into `summary.md` in the source folder:

```markdown
# <Title>

> Source: [<Title>](<URL>) by <Author>

## Overview

<approved overview>

## Key Takeaways

<approved takeaways>

## Notes

<approved notes with ### topic headers>
```
