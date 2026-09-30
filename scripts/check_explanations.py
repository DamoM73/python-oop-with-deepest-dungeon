"""Check that every Code explanation box matches the snippet above it.

For every snippet include (--8<-- "path" or --8<-- "path:start:end")
that is followed by a ??? note "Code explanation" box, report:

- BAD: a reference to a blank line, a comment or a line past the end
- MISSING: a code line with no explanation

Line numbers are the ones shown on the page, so a fence with
linenums="81" starts counting at 81. When the fence has hl_lines,
only the highlighted code lines need an explanation, because the
other lines were explained when they first appeared.

Run from the repo root: python scripts/check_explanations.py
"""

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
SNIPPET = re.compile(r'--8<--\s+"([^":]+)(?::(\d+):(\d+))?"')
FENCE = re.compile(r"^\s*```")
LINENUMS = re.compile(r'linenums="(\d+)"')
HL_LINES = re.compile(r'hl_lines="([^"]+)"')
BOX = re.compile(r'^\?\?\?\+?\s+note\s+"Code explanation"')
REF = re.compile(r"\*\*lines?\s+(\d+)(?:\s*[–-]\s*(\d+))?\*\*")


def parse_hl(text, first):
    """Turn hl_lines="1 3-5" (counted from 1) into shown line numbers."""
    shown = set()
    for part in text.split():
        start, _, end = part.partition("-")
        for number in range(int(start), int(end or start) + 1):
            shown.add(number + first - 1)
    return shown


def shown_lines(path, start, end, first):
    """Return {shown line number: text} for the included lines."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if start:
        lines = lines[int(start) - 1:int(end)]
    return {first + offset: text for offset, text in enumerate(lines)}


def check_page(page):
    issues = []
    lines = page.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines):
        match = SNIPPET.search(lines[index])
        if not match:
            index += 1
            continue
        snippet, start, end = match.groups()
        # the fence header is the nearest fence line above the snippet
        header = ""
        for back in range(index - 1, -1, -1):
            if FENCE.match(lines[back]):
                header = lines[back]
                break
        first = int(LINENUMS.search(header).group(1)) if LINENUMS.search(header) else 1
        highlight = HL_LINES.search(header)
        # find the next explanation box before the next snippet
        look = index + 1
        box_start = None
        while look < len(lines):
            if SNIPPET.search(lines[look]):
                break
            if BOX.match(lines[look]):
                box_start = look
                break
            look += 1
        if box_start is None:
            index += 1
            continue
        source = DOCS / snippet
        if not source.exists():
            issues.append(f"{page.name}: missing file {snippet}")
            index = look
            continue
        shown = shown_lines(source, start, end, first)
        code = {n for n, t in shown.items() if t.strip() and not t.strip().startswith("#")}
        required = code & parse_hl(highlight.group(1), first) if highlight else code
        covered = set()
        body = box_start + 1
        while body < len(lines) and (lines[body].startswith("    ") or not lines[body].strip()):
            for ref in REF.finditer(lines[body]):
                ref_start = int(ref.group(1))
                ref_end = int(ref.group(2) or ref_start)
                for endpoint in {ref_start, ref_end}:
                    if endpoint not in code:
                        issues.append(f"{page.name}: BAD line {endpoint} in {snippet}")
                covered.update(range(ref_start, ref_end + 1))
            body += 1
        for number in sorted(required - covered):
            issues.append(f"{page.name}: MISSING line {number} in {snippet}")
        index = body
    return issues


def main():
    issues = []
    for page in sorted(DOCS.rglob("*.md")):
        issues.extend(check_page(page))
    for issue in issues:
        print(issue)
    print(f"{len(issues)} issue(s) found")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
