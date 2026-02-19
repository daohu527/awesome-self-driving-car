#!/usr/bin/env python3
"""
Sync selected top-level sections from README.md into docs/*.md files.

Usage: python scripts/sync_docs_from_readme.py

This script does NOT modify README.md. It extracts sections and writes docs files.
"""
from pathlib import Path
import re
import sys
import argparse

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
DEFAULT_DOCS = ROOT / 'docs'

SECTIONS = {
    'opensource': ['openso', 'opensourc'],
    'datasets': ['dataset', 'datasets'],
    'papers': ['paper', 'papers'],
}


def find_section_lines(lines, keywords):
    # find line index where a top-level section heading (## ) contains any keyword
    for i, l in enumerate(lines):
        if l.startswith('##'):
            low = l.lower()
            for kw in keywords:
                if kw in low:
                    return i
    return None


def extract_section(lines, start_idx):
    # include header line, stop before next top-level '## ' or EOF
    out = []
    n = len(lines)
    for i in range(start_idx, n):
        if i != start_idx and lines[i].startswith('## '):
            break
        out.append(lines[i])
    return ''.join(out).rstrip() + '\n'


def main():
    parser = argparse.ArgumentParser(description='Sync README sections to docs')
    parser.add_argument('--out-dir', help='Output directory for generated docs', default=str(DEFAULT_DOCS))
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    if not README.exists():
        print('README.md not found', file=sys.stderr)
        sys.exit(2)
    txt = README.read_text(encoding='utf-8')
    lines = txt.splitlines(keepends=True)

    for name, kws in SECTIONS.items():
        idx = find_section_lines(lines, kws)
        if idx is None:
            print(f'Warning: could not find section for {name} in README.md', file=sys.stderr)
            continue
        content = extract_section(lines, idx)
        # write to out_dir/<name>.md
        target = out_dir / f'{name}.md'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        print(f'Wrote {target}')


if __name__ == '__main__':
    main()
