# public/

HTML presentation pages visualizing concepts from collected sources.

## Structure

```
public/
  assets/            # Shared images (backgrounds, icons)
  css/
    theme.css        # Global theme: variables, reset, fonts, base link styles
  *.html             # Individual presentation pages
```

## Theme (`css/theme.css`)

Dark design system. Key variables:
- Colors: `--research-primary` (teal #38bdf8), `--plan-primary` (green #34d399), `--implement-primary` (amber #fb923c)
- Backgrounds: `--bg-deep` (#0a0e1a), `--bg-card` (translucent dark), `--border-subtle`
- Text: `--text-primary`, `--text-secondary`, `--text-muted`
- Fonts: `--font-sans` (Inter), `--font-mono` (JetBrains Mono)

All pages link `css/theme.css` for shared aesthetics. Page-specific styles go inline.

## Assets

- `bg-dark-abstract.png` — Dark navy background with subtle teal/amber flowing patterns. Generic, reusable across pages. Generated via ChatGPT/DALL-E.

## Creating a new page

1. Link `css/theme.css` in `<head>`
2. Use theme variables for colors/fonts — don't hardcode
3. Page-specific styles go in inline `<style>`
4. Background images go in `assets/`, reference as `url('assets/...')`
5. Source attribution: fixed bottom-left, links to original source
6. Use `/chatgpt-image` skill for new background images, save to `assets/`

## Existing pages

- `research-plan-implement.html` — RPI workflow (Research → Plan → Implement) from Dex Horthy's "No Vibes Allowed" talk. Three phase cards with IN/OUT flow, insight grid.
