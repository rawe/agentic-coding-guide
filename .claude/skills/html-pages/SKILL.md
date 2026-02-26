---
name: html-pages
description: Create and maintain dark-themed HTML presentation pages in docs/. Use when asked to create a new HTML page from markdown content, add a presentation page, build a guide page, or work with existing pages in docs/. Covers page structure, theme colors, teaser images, image optimization, and index page integration.
---

# HTML Presentation Pages

## Project Structure

```
docs/
├── index.html                    # Links to all guide pages
├── css/theme.css                 # Shared color variables and base styles
├── assets/
│   ├── bg-dark-abstract.png      # Shared background image
│   ├── teaser-*.png              # Optimized card images (720x450)
│   └── originals/                # Full-resolution originals (not committed)
├── research-plan-implement.html  # Example guide page
└── skills-mcp-commands.html      # Example guide page
```

## Theme & Colors

All accent colors live in `docs/css/theme.css` as CSS variables. Never hardcode hex values in page styles.

Existing variable groups:
- `--research-primary`, `--research-glow` (blue #38bdf8)
- `--plan-primary`, `--plan-glow` (green #34d399)
- `--implement-primary`, `--implement-glow` (orange #fb923c)
- `--skills-primary`, `--skills-glow` (purple #7c6ef0)
- `--mcp-primary`, `--mcp-glow` (pink #c466f5)
- `--commands-primary`, `--commands-glow` (green #3ec97a)

When creating a new page with new accent colors:
1. Add `--newname-primary` and `--newname-glow` to `theme.css` `:root`
2. Reference them via `var()` in the page's inline `<style>`
3. Never define `:root` variables in inline page styles

## Creating a New Page

### 1. Choose accent colors

Pick 2-3 accent colors for the page's cards/sections. Add them to `theme.css` if new.

### 2. Page structure

Every page follows this skeleton. Read an existing page (e.g. `research-plan-implement.html`) for the full pattern:

- `<link rel="stylesheet" href="css/theme.css">`
- Inline `<style>` for page-specific layout only (not colors)
- Background: `bg-dark-abstract.png` with dark overlay gradient
- `.page-wrapper` container (max-width 1200px, centered)
- Header: `.badge` + `h1` with gradient text + `.subtitle`
- Content: `.pipeline` with `.phase-card` cards or similar
- Footer: `.source-attribution` (fixed bottom-left)

### 3. H1 gradient

The page title uses `background-clip: text` gradient. Must reference CSS variables:

```css
background: linear-gradient(135deg, var(--accent1) 0%, var(--accent2) 50%, var(--accent3) 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### 4. Card pattern

Cards use the card-image + card-body pattern:

```html
<div class="phase-card cardclass">
  <div class="card-image">
    <img src="assets/teaser-name.png" alt="Description">
  </div>
  <div class="card-body">
    <!-- title, description, lists -->
  </div>
</div>
```

Card image CSS: `width: 100%`, `aspect-ratio: 16/10`, `overflow: hidden`, `object-fit: cover`.

## Teaser Images

### When to create

Always for card-based pages. Ask the user if images are wanted when the page layout doesn't obviously need them.

### Generation

Use the `/chatgpt-image` skill. Prompt pattern:

> [Subject description] on a dark navy background (#0a0e1a), with [accent color name] (#hex) glow effects. Minimal, modern tech illustration style. Square 1:1 ratio.

Key requirements:
- Dark background that blends with the page
- Accent color as dominant glow/highlight
- Minimal, not busy — reads well at small sizes
- Square (1:1) generation ratio

### Optimization

Generated images are large (1024x1024+). Always optimize before use:

1. Save originals to `docs/assets/originals/` first (never delete these)
2. Determine the actual display size from the HTML/CSS context (container width, aspect-ratio, object-fit). Multiply by 2 for retina.
   - Example: card images in a 360px-wide card with `aspect-ratio: 16/10` → 720x450px
   - Example: a hero banner at 1200px wide → 2400px wide at 2x
3. Resize to the determined dimensions: `sips --resampleWidth <W> --resampleHeight <H> <file>`
4. Optimized images go in `docs/assets/`, originals stay in `originals/`
5. Do NOT commit originals (they stay local only)

## Index Page Integration

When adding a new page, update `docs/index.html`. Note: the index h1 gradient uses its own variables (`--index-gradient-*` in `theme.css`) and is never modified when adding pages.

### 1. Add a card variant

Define the accent using `--_accent` with `color-mix()`:

```css
.index-card.newclass {
  --_accent: var(--newname-primary);
  background: linear-gradient(160deg, color-mix(in srgb, var(--_accent) 6%, transparent) 0%, var(--bg-card) 100%);
  box-shadow: 0 0 40px color-mix(in srgb, var(--_accent) 4%, transparent);
  border-left: 3px solid color-mix(in srgb, var(--_accent) 30%, transparent);
}
.index-card.newclass:hover {
  box-shadow: 0 8px 48px color-mix(in srgb, var(--_accent) 14%, transparent);
  border-left-color: var(--_accent);
}
.index-card.newclass .card-title { color: var(--newname-primary); }
```

### 2. Add the card HTML

```html
<a href="new-page.html" class="index-card newclass">
  <div class="card-title">Page Title</div>
  <p class="card-subtext">One-line description.</p>
  <span class="card-arrow">&rsaquo;</span>
</a>
```

## Checklist

For every new HTML page:
1. Add accent color variables to `theme.css` (if new colors)
2. Create the page using the skeleton pattern from existing pages
3. Generate teaser images with `/chatgpt-image` if needed
4. Optimize images (720x450), archive originals
5. Add index card with `color-mix()` accent pattern
6. Verify in browser (spawn HTTP server, check with Chrome)
