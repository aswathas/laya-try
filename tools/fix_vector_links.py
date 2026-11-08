"""Repair vector literals that look like wikilinks.

Obsidian parses `[[10, 20, 30]]` as a link to a note called "10, 20, 30", which
breaks the vault's wikilink gate. Rewrite those to `[10, 20, 30]`.

    python tools/fix_vector_links.py
"""
from __future__ import annotations

import os
import re

BOOK = r"C:\Users\aswat\Aswaths Obsidian Den\Aswaths Mountain Den\Learning\Foundations\Book 1 - Foundations"
LINK = re.compile(r"\[\[([^\[\]]+)\]\]")
VECTOR = re.compile(r"^[\d\s\.\,\-\+]+$")


def main() -> int:
    fixed = 0
    touched = 0
    for name in sorted(os.listdir(BOOK)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(BOOK, name)
        with open(path, encoding="utf-8") as f:
            text = f.read()

        def repl(m: re.Match) -> str:
            nonlocal fixed
            inner = m.group(1)
            if "/" in inner or not VECTOR.match(inner.strip()):
                return m.group(0)
            fixed += 1
            return "[" + inner + "]"

        new = LINK.sub(repl, text)
        if new != text:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            touched += 1
            print("fixed:", name)
    print(f"vector literals fixed: {fixed} in {touched} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
