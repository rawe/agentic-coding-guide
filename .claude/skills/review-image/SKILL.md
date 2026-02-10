---
name: review-image
description: Procedural guide for visually reviewing and evaluating a generated or downloaded image. Use after generating an image (e.g. via /chatgpt-image) or whenever Claude needs to inspect an image file to assess quality, composition, suitability, or correctness. Not invoked with arguments — the image path must already be known from prior context.
---

# Review Image

Procedure to visually inspect and evaluate an image file. Follow these steps in order.

## 1. Get image info and resize if needed

Run the bundled script (uses uv with inline Pillow dependency):

```bash
.claude/skills/review-image/scripts/resize-for-review.py <image-path>
```

The script prints file size, dimensions, aspect ratio, and a `READ:` line indicating which file to inspect. If the image is large (>2 MB or >960 px), it saves a resized preview to `/tmp/review-preview.png`.

## 2. Read and evaluate

Use the **Read** tool on the path from the `READ:` output. After viewing, assess:

- **Composition**: Is the layout balanced? Is there space for text overlay if needed?
- **Color palette**: Does it match the intended brand or mood?
- **Clarity**: Are elements sharp and recognizable, or muddy and generic?
- **Relevance**: Does the image actually communicate the intended subject?
- **Text/artifacts**: Any unwanted text, watermarks, or AI artifacts?
- **Aspect ratio**: Does it match the intended use (16:9 for presentations, 1:1 for social, etc.)?

Report findings honestly — flag problems and suggest a re-generation with an improved prompt if the image falls short.
