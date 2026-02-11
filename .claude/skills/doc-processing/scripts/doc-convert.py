# /// script
# dependencies = ["docling"]
# requires-python = ">=3.9"
# ///
"""
Convert a document (PDF, DOCX, etc.) to markdown using Docling.

Usage: uv run doc-convert.py <input-file> <output-file>
"""

import argparse
import sys
from pathlib import Path

from docling.document_converter import DocumentConverter


def main():
    parser = argparse.ArgumentParser(description="Convert a document to markdown")
    parser.add_argument("input_file", help="Path to source document (PDF, DOCX, etc.)")
    parser.add_argument("output_file", help="Path for the output markdown file")
    args = parser.parse_args()

    src = Path(args.input_file)
    if not src.exists():
        sys.exit(f"Input file not found: {src}")

    converter = DocumentConverter()
    result = converter.convert(str(src))
    md = result.document.export_to_markdown()

    out = Path(args.output_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md)

    size_kb = out.stat().st_size / 1024
    lines = md.count("\n") + 1
    chars = len(md)
    print(f"file: {out}")
    print(f"size_kb: {size_kb:.1f}")
    print(f"lines: {lines}")
    print(f"chars: {chars}")


if __name__ == "__main__":
    main()
