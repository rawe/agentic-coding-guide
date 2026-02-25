---
name: generate-html-page
description: Generate a presentation-ready HTML page from a source folder. Use when converting YouTube or document summaries into dark-themed HTML guides for public/.
user-invocable: true
argument-hint: <source-folder-path> [page-name]
context: fork
agent: html-page-generator
---

Generate an HTML presentation page from the source at `$ARGUMENTS[0]`.

## Step 1 — Read source material

Read `meta.md` and `summary.md` from `$ARGUMENTS[0]`. If `notes.md` exists, read it too. Extract: title, URL, author/channel, core content organized by topic.

## Step 2 — Determine page name

If `$ARGUMENTS[1]` is provided, use it as the page name. Otherwise, derive a short slug from the source title (lowercase, hyphens, e.g. `skills-in-practice`).

## Step 3 — Study existing pages

Read `public/STRUCTURE.md` for reading order. Read `public/content/README.md` for the content markdown format. Read 1 similar content file from `public/content/` as a structural reference.

## Step 4 — Draft content markdown

Write `public/content/<page-name>.md` following the established format. Include `<!-- Visualization: ... -->` comments describing any diagrams.

## Step 5 — Choose accent colors

Read `public/css/theme.css`. Reuse existing color variables where they fit. Add new ones to theme.css only if needed.

## Step 6 — Build HTML

Read one existing HTML page as a template reference. Build `public/<page-name>.html` following the html-pages skill.

## Step 7 — Update index and structure

Add the page card to `public/index.html`. Add the page to the appropriate group in `public/STRUCTURE.md` with a "Why here" note.
