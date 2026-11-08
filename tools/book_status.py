"""Keep the book index's status column honest.

Reads each chapter's frontmatter `status` and rewrites the matching row in
`00 - Book Index.md`. Run it after chapters land.

    python tools/book_status.py
"""
from __future__ import annotations

import os
import re

BOOK = r"C:\Users\aswat\Aswaths Obsidian Den\Aswaths Mountain Den\Learning\Foundations\Book 1 - Foundations"
INDEX = os.path.join(BOOK, "00 - Book Index.md")
STATUS_RE = re.compile(r"^status:\s*(\S+)\s*$", re.M)


def chapter_status(path: str) -> str | None:
    with open(path, encoding="utf-8") as f:
        head = f.read(2000)
    m = STATUS_RE.search(head)
    return m.group(1) if m else None


def main() -> int:
    with open(INDEX, encoding="utf-8") as f:
        lines = f.read().split("\n")

    by_number: dict[str, str] = {}
    for name in os.listdir(BOOK):
        if not name.endswith(".md") or name.startswith("00 -") or not name[:2].isdigit():
            continue
        number = name[:2]
        status = chapter_status(os.path.join(BOOK, name))
        if number and status:
            by_number[number] = status

    changed = 0
    for i, line in enumerate(lines):
        m = re.match(r"^\|\s*(\d{2})\s*\|", line)
        if not m:
            continue
        status = by_number.get(m.group(1))
        if status is None:
            continue
        cells = line.rstrip().rstrip("|").split("|")
        if len(cells) < 3:
            continue
        label = "Written" if status == "draft" else status.title()
        new_cell = f" {label} "
        if cells[-1] != new_cell:
            lines[i] = "|".join(cells[:-1]) + "|" + new_cell + "|"
            changed += 1

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    written = sum(1 for s in by_number.values() if s == "draft")
    print(f"chapters tracked: {len(by_number)}   written: {written}   rows updated: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
