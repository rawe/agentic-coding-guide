# Content Markdown Files

Markdown representations of the HTML guide pages in `docs/`. These serve as the **editable source of truth** — markdown is easier to adjust, review, and iterate on than raw HTML. Changes flow: markdown → HTML.

## Pattern

Each HTML file in `docs/` has a corresponding markdown file here with the same base name:

```
docs/skills-mcp-commands.html  →  docs/content/skills-mcp-commands.md
docs/context-engineering.html  →  docs/content/context-engineering.md
```

## Structure

Each markdown file follows this structure:

1. **Title** as `# heading` — the page's main headline
2. **Subtitle** — one-line description directly below the title
3. **Sections** as `## headings` — matching the HTML page's sections
4. **Content** — all text, lists, code blocks, extracted faithfully from the HTML
5. **Visualization comments** — HTML comments (`<!-- Visualization: ... -->`) describing each SVG or image inline, placed where they appear in the page

## Visualization Documentation

SVGs and images are documented as HTML comments with enough detail to recreate them:

```markdown
<!-- Visualization: [type of diagram]
[Description of what it shows]
[Key elements: nodes, arrows, labels, colors]
[Layout: arrangement, spacing, flow direction] -->
```

This lets someone recreate or modify the visual without reading SVG source code.

## Exclusions

- `index.html` — not a guide page, no markdown needed
- `*-backup.html` — backup files, skip
