#!/bin/bash
# Move the most recent ChatGPT-generated image from ~/Downloads to a target path.
# Usage: move-chatgpt-image.sh <target-path>
set -euo pipefail

TARGET="$1"
DOWNLOADS="${HOME}/Downloads"

# Find the most recent ChatGPT Image file
LATEST=$(ls -t "$DOWNLOADS"/ChatGPT\ Image* 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
    echo "ERROR: No ChatGPT Image files found in $DOWNLOADS" >&2
    exit 1
fi

mkdir -p "$(dirname "$TARGET")"
mv "$LATEST" "$TARGET"
echo "Moved: $(basename "$LATEST") -> $TARGET"
