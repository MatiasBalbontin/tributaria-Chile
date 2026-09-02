#!/usr/bin/env python3
"""MarkItDown conversion helper — convierte archivos grandes a Markdown."""

from markitdown import MarkItDown
from pathlib import Path
import sys

def to_markdown(filepath: str) -> str:
    """Convierte archivo → Markdown (PDF, DOCX, PPTX, XLSX, etc)."""
    md = MarkItDown()
    result = md.convert_local(filepath)
    return result.text_content

def to_markdown_file(filepath: str, output: str = None) -> str:
    """Convierte y guarda en archivo."""
    content = to_markdown(filepath)
    out = output or str(Path(filepath).with_suffix(".md"))
    Path(out).write_text(content, encoding="utf-8")
    print(f"✓ Guardado: {out}")
    return out

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python md_convert.py <archivo> [output.md]")
        sys.exit(1)

    filepath = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        to_markdown_file(filepath, output)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
