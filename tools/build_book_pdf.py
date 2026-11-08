"""Build the whole book into one PDF.

Markdown chapters -> one styled HTML file -> headless Chrome -> PDF.

    python tools/build_book_pdf.py

Output: build/AI-Foundations-Book1.pdf
"""
from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
import sys

VAULT = r"C:\Users\aswat\Aswaths Obsidian Den\Aswaths Mountain Den"
BOOK = os.path.join(VAULT, "Learning", "Foundations", "Book 1 - Foundations")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
HTML_PATH = os.path.join(BUILD, "book.html")
PDF_PATH = os.path.join(BUILD, "AI-Foundations-Book1.pdf")

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
WIKILINK = re.compile(r"\[\[([^\[\]|]+)(?:\|[^\[\]]+)?\]\]")
# a double-bracket span holding only numbers is a Python literal, not a link
NUMERIC = re.compile(r"^[\d\s\.\,\-\+]+$")

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm; }
html { -webkit-print-color-adjust: exact; }
body {
  font-family: "Georgia", "Times New Roman", serif;
  font-size: 10.5pt; line-height: 1.55; color: #16181d; max-width: none;
}
h1 {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22pt;
  color: #0b3d63; border-bottom: 3px solid #0b3d63; padding-bottom: 6pt;
  margin: 0 0 4pt 0; break-before: page; break-after: avoid;
}
h1 .num { color: #c2410c; }
h1 + .meta {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 8.5pt;
  color: #6b7280; text-transform: uppercase; letter-spacing: .06em;
  margin: 0 0 14pt 0;
}
h2 {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 13pt;
  color: #0b3d63; margin: 18pt 0 6pt 0; break-after: avoid;
}
h3 {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 11pt;
  color: #334155; margin: 14pt 0 4pt 0; break-after: avoid;
}
p { margin: 0 0 7pt 0; text-align: justify; }
ul, ol { margin: 0 0 8pt 0; padding-left: 18pt; }
li { margin-bottom: 3pt; }
code {
  font-family: "Consolas", "SF Mono", monospace; font-size: 9pt;
  background: #f1f5f9; padding: 1px 4px; border-radius: 3px; color: #7c2d12;
}
pre {
  background: #0f172a; color: #e2e8f0; padding: 9pt 10pt; border-radius: 4pt;
  font-family: "Consolas", "SF Mono", monospace; font-size: 8.2pt;
  line-height: 1.4; overflow-wrap: break-word; white-space: pre-wrap;
  break-inside: avoid; margin: 8pt 0 10pt 0;
}
pre code { background: none; color: inherit; padding: 0; font-size: 8.2pt; }
table {
  border-collapse: collapse; width: 100%; margin: 8pt 0 12pt 0;
  font-size: 8.8pt; break-inside: avoid;
}
th {
  background: #e7eef5; color: #0b3d63; text-align: left;
  border: 1px solid #c3d3e0; padding: 4pt 5pt;
}
td { border: 1px solid #d8e2ea; padding: 4pt 5pt; vertical-align: top; }
tr:nth-child(even) td { background: #f8fafc; }
hr { border: none; border-top: 1px solid #d8e2ea; margin: 14pt 0; }
blockquote {
  margin: 8pt 0; padding: 6pt 10pt; border-left: 3pt solid #c2410c;
  background: #fff7ed; color: #7c2d12;
}
a { color: #0b3d63; text-decoration: none; }
.cover { break-before: page; text-align: center; padding-top: 120pt; }
.cover .title {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 34pt;
  color: #0b3d63; font-weight: 700; line-height: 1.15; margin-bottom: 10pt;
}
.cover .sub { font-size: 13pt; color: #475569; font-style: italic; }
.cover .meta { margin-top: 30pt; font-size: 10pt; color: #64748b; }
.cover .rule { width: 120pt; border-top: 3px solid #c2410c; margin: 22pt auto; }
.toc h2 { margin-top: 0; }
.toc ol { list-style: none; padding-left: 0; }
.toc li { margin-bottom: 3pt; font-size: 10pt; }
.toc .part {
  font-family: "Helvetica Neue", Arial, sans-serif; font-weight: 700;
  color: #c2410c; margin-top: 12pt; font-size: 11pt;
}
"""


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    raise SystemExit("no Chrome or Edge found")


def strip_frontmatter(text: str) -> tuple[str, dict]:
    meta: dict[str, str] = {}
    m = FRONTMATTER.match(text)
    if not m:
        return text, meta
    for line in m.group(0).strip().strip("-").splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return text[m.end():], meta


def clean_wikilinks(text: str) -> str:
    """Turn Obsidian wikilinks into plain text; leave Python literals alone."""
    def repl(m: re.Match) -> str:
        inner = m.group(1)
        if NUMERIC.match(inner.strip()):
            return m.group(0)
        return inner
    return WIKILINK.sub(repl, text)


def chapter_files() -> list[str]:
    files = []
    for name in os.listdir(BOOK):
        if not name.endswith(".md"):
            continue
        if not name[:2].isdigit() or name.startswith("00 -"):
            continue
        files.append(name)
    return sorted(files)


def build() -> int:
    os.makedirs(BUILD, exist_ok=True)
    from markdown_it import MarkdownIt
    md = MarkdownIt("commonmark", {"html": True, "linkify": False})
    md.enable(["table", "strikethrough"])

    names = chapter_files()
    toc_parts: list[str] = []
    body_parts: list[str] = []
    current_part = ""

    for name in names:
        raw = open(os.path.join(BOOK, name), encoding="utf-8").read()
        content, meta = strip_frontmatter(raw)
        content = clean_wikilinks(content)
        title = meta.get("title") or name[:-3]
        number = name[:2]
        part = meta.get("part", "")

        # drop the file's own H1 - the book supplies its own
        content = re.sub(r"^#\s+.*?\n", "", content, count=1)

        if part != current_part:
            current_part = part
            toc_parts.append(f'<div class="part">{html.escape(part)}</div>')
            body_parts.append(
                f'<h1 style="break-before:page;border-bottom-width:2px">{html.escape(part)}</h1>'
            )

        anchor = f"ch{number}"
        toc_parts.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
        meta_line = " · ".join(x for x in (part, meta.get("concepts", "")) if x)
        body_parts.append(
            f'<h1 id="{anchor}"><span class="num">{number}</span> · {html.escape(re.sub(r"^\d{2}\s*-\s*", "", title))}</h1>'
            f'<p class="meta">{html.escape(meta_line)}</p>'
        )
        body_parts.append(md.render(content))

    index_raw = open(os.path.join(BOOK, "00 - Book Index.md"), encoding="utf-8").read()
    index_content, _ = strip_frontmatter(index_raw)
    index_content = re.sub(r"^#\s+.*?\n", "", index_content, count=1)

    start_html = ""
    start_path = os.path.join(BOOK, "START HERE.md")
    if os.path.exists(start_path):
        raw = open(start_path, encoding="utf-8").read()
        content, meta = strip_frontmatter(raw)
        content = re.sub(r"^#\s+.*?\n", "", content, count=1)
        start_html = (
            '<h1>Start Here</h1>'
            f'<p class="meta">{html.escape(meta.get("type", ""))}</p>'
            + md.render(clean_wikilinks(content))
        )

    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Book 1 - AI Foundations</title>
<style>{CSS}</style></head><body>
<section class="cover">
  <div class="title">AI Foundations</div>
  <div class="rule"></div>
  <div class="sub">From Vectors to Decision Models</div>
  <div class="meta">Book 1 of 2 &nbsp;·&nbsp; {len(names)} chapters &nbsp;·&nbsp; 5 parts<br>
  A companion build: <code>labkit/</code>, written chapter by chapter</div>
</section>
<section class="toc"><h1 style="break-before:page">Contents</h1>
{''.join(toc_parts)}
</section>
{start_html}
{''.join(body_parts)}
</body></html>"""

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(document)

    chrome = find_chrome()
    profile = os.path.join(BUILD, "_chrome_profile")
    if os.path.exists(profile):
        shutil.rmtree(profile, ignore_errors=True)
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={profile}",
        "--no-pdf-header-footer",
        "--generate-pdf-document-outline",
        f"--print-to-pdf={PDF_PATH}",
        "file:///" + HTML_PATH.replace("\\", "/"),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if not os.path.exists(PDF_PATH):
        print(result.stdout[-2000:])
        print(result.stderr[-2000:])
        return 1

    data = open(PDF_PATH, "rb").read()
    pages = data.count(b"/Type /Page") or data.count(b"/Type/Page")
    print(f"chapters: {len(names)}")
    print(f"pdf: {PDF_PATH}")
    print(f"size: {len(data) / 1_048_576:.1f} MB, ~{pages} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
