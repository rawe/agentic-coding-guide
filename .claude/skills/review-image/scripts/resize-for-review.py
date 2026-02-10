#!/usr/bin/env -S uv run --with Pillow
"""Resize an image for visual review. Outputs dimensions, file size, and a resized preview if needed."""

import sys
import os
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print("Usage: resize-for-review.py <image-path> [max-dimension] [output-path]")
        print("  max-dimension: max width or height in px (default: 960)")
        print("  output-path:   where to save preview (default: /tmp/review-preview.png)")
        sys.exit(1)

    image_path = sys.argv[1]
    max_dim = int(sys.argv[2]) if len(sys.argv) > 2 else 960
    output_path = sys.argv[3] if len(sys.argv) > 3 else "/tmp/review-preview.png"

    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found")
        sys.exit(1)

    file_size = os.path.getsize(image_path)
    img = Image.open(image_path)
    w, h = img.size

    print(f"File: {image_path}")
    print(f"Size: {file_size / 1024:.0f} KB ({file_size / (1024*1024):.1f} MB)")
    print(f"Dimensions: {w}x{h}")
    print(f"Mode: {img.mode}")
    print(f"Aspect ratio: {w/h:.2f}:1")

    if file_size > 2 * 1024 * 1024 or w > max_dim or h > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
        img.save(output_path)
        print(f"\nResized preview saved to: {output_path}")
        print(f"Preview dimensions: {img.size[0]}x{img.size[1]}")
        print(f"READ: {output_path}")
    else:
        print(f"\nImage is small enough to read directly.")
        print(f"READ: {image_path}")

if __name__ == "__main__":
    main()
