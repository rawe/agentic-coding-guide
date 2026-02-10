---
name: chatgpt-image
description: Generate images using ChatGPT (DALL-E) via Chrome browser automation. Use when the user wants to create, generate, or produce an image using ChatGPT. Requires the Claude-in-Chrome browser extension to be active. Invoked as /chatgpt-image with an image description.
argument-hint: [image description]
user-invocable: true
---

# ChatGPT Image Generation

Generate an image via ChatGPT/DALL-E using Chrome browser automation, download it, and save it to the project's `generated-images/` directory with a descriptive filename.

## Prerequisites

- Claude-in-Chrome browser extension is active
- User is logged into chatgpt.com

## Workflow

Given an image description via `$ARGUMENTS`:

1. **Get browser context**: Call `tabs_context_mcp` to discover available tabs.

2. **Open ChatGPT**: Check if a chatgpt.com tab exists. If yes, reuse it. If not, create a new tab and navigate to `https://chatgpt.com`.

3. **Enter prompt**: Click the input field ("Ask anything"), type:
   ```
   Generate an image: <$ARGUMENTS>
   ```

4. **Submit**: Click the submit button (circular arrow icon, bottom-right of input field).

5. **Wait for generation**: Take screenshots every 5–8 seconds to monitor. The image is ready when the "Creating image" placeholder is replaced by the actual image with "Image created" label. Timeout after 60 seconds if not complete.

6. **Download the image**: Use `read_page` with `filter: "interactive"` to find the button labeled **"Download this image"** in the accessibility tree. Click it via its `ref` ID. For detailed interaction specifics, see [references/browser-workflow.md](references/browser-workflow.md).

7. **Wait for download**: Wait 3 seconds for the file to appear in `~/Downloads/`.

8. **Move and rename**: Derive a filename slug from `$ARGUMENTS` (lowercase, hyphens, no special chars, max 60 chars, `.png` extension). Run:
   ```bash
   .claude/skills/chatgpt-image/scripts/move-chatgpt-image.sh generated-images/<slug>.png
   ```

9. **Confirm**: Report the saved path to the user.
