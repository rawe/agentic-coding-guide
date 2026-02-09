---
name: yt-summarize
description: Interactively summarize an already-extracted YouTube video source. Requires transcript.md and meta.md to exist in the source folder.
argument-hint: [source-folder-path]
user-invocable: true
---

# YouTube Summarization

Summarize the source at `$ARGUMENTS`. The folder must contain `meta.md` and `transcript.md`.

## Process

Work section by section. Present each section as a draft, wait for user feedback before moving on.

### Step 1 — Read source

Read `meta.md` and `transcript.md` from the given folder.

### Step 2 — Overview

Draft 2-3 sentences: what the video covers, who the speaker is, why it matters. Present to user for approval.

### Step 3 — Key Takeaways

Extract the core insights as bullet points. Each point self-contained, no filler. Present to user for approval.

### Step 4 — Notes

Organize the substance by topic (not chronologically). Use `###` headers for each topic section. Include concepts, techniques, examples, and relevant quotes inline. Present to user for approval.

### Step 5 — Write summary.md

Assemble approved sections into `summary.md` using this format:

```markdown
# <Title>

> Source: [<Title>](<URL>) by <Channel>

## Overview

<approved overview>

## Key Takeaways

<approved takeaways>

## Notes

<approved notes with ### topic headers>
```
