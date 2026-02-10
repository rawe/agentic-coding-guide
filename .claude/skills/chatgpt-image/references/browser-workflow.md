# ChatGPT Image Generation — Browser Interaction Details

## Entering the Prompt

- The input field is labeled "Ask anything" in the center of the page.
- Click the input field to focus it, then type the prompt.
- Prefix the description with `Generate an image:` so ChatGPT routes to DALL-E.

## Submitting

- The submit button is a circular arrow icon at the bottom-right of the input field.
- After submission, ChatGPT shows a "Creating image" placeholder with a loading state.

## Waiting for Generation

- Generation takes 10–30 seconds.
- Use `screenshot` actions to monitor progress.
- The image is ready when the placeholder is replaced by the actual image with an "Image created" label.
- Wait at least 5 seconds between screenshot checks to avoid excessive polling.

## Downloading — Critical Details

Two approaches exist. **Use the inline approach** — it is more reliable.

### Inline approach (recommended)

1. Call `read_page` with `filter: "interactive"` to scan all interactive elements.
2. Look for a button labeled **"Download this image"** in the accessibility tree.
   - This button is a small icon beneath the generated image — not visually obvious.
   - The accessibility tree reliably exposes it by label.
3. Click the button via its `ref` ID.

### Full-view approach (fallback)

1. Click the generated image to open the full-screen overlay.
2. Find the "Save" button with download icon in the top-right corner.
3. Click to trigger download.

## Download Location & Filename

- Files save to `~/Downloads/` automatically.
- ChatGPT names files: `ChatGPT Image <Mon DD, YYYY, HH_MM_SS AM/PM>.png`
- Example: `ChatGPT Image Feb 10, 2026, 10_47_50 AM.png`
