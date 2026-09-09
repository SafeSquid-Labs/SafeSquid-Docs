#!/usr/bin/env python3
"""Render every ```mermaid block under public/ with mermaid-cli, to prove it parses.

`mint validate` does not parse Mermaid. A broken diagram therefore passes every gate in
this repo and ships as a syntax-error box on the live page. This found exactly that on
2026-09-07: icap.mdx used `call` as a node id — a reserved Mermaid token — so its
diagram had never rendered in production and nothing had ever flagged it.

Usage, from anywhere:

    python3 .claude/tools/check_mermaid.py

Exits non-zero if any block fails, so it works as a gate. Needs network on first run
(npx fetches @mermaid-js/mermaid-cli) and takes a couple of minutes for ~45 blocks.

Gotchas this catches, all seen for real:
  - reserved node ids (`call`, `end`, `graph`, `class`, `click`)
  - unquoted labels containing ( ) , : / # or an apostrophe
  - a fence indented inside <Tab> whose closing ``` is mis-indented
"""
import pathlib
import re
import subprocess
import sys
import tempfile
import textwrap

REPO = pathlib.Path(__file__).resolve().parents[2]
PUB = REPO / "public"

# captures the fence's own indentation so blocks nested in <Tab> dedent correctly
FENCE = re.compile(r"^([ \t]*)```mermaid[ \t]*\n(.*?)^\1```[ \t]*$", re.S | re.M)

blocks = []
for p in sorted(PUB.rglob("*")):
    if p.suffix not in (".md", ".mdx"):
        continue
    src = p.read_text(encoding="utf-8", errors="replace")
    for m in FENCE.finditer(src):
        line = src[: m.start()].count("\n") + 1
        blocks.append((p, line, textwrap.dedent(m.group(2))))

print(f"found {len(blocks)} mermaid blocks")
bad = []
with tempfile.TemporaryDirectory() as td:
    td = pathlib.Path(td)
    for p, line, code in blocks:
        src_file = td / "d.mmd"
        src_file.write_text(code)
        r = subprocess.run(
            ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", str(src_file), "-o", str(td / "d.svg")],
            capture_output=True, text=True, cwd=td,
        )
        where = f"{p.relative_to(PUB)}:{line}"
        if r.returncode != 0:
            err = [l for l in (r.stderr or r.stdout).strip().splitlines() if l.strip()]
            bad.append((where, err[-4:]))
            print(f"  FAIL {where}")
        else:
            print(f"  ok   {where}")

print()
if bad:
    print(f"{len(bad)} BROKEN diagram(s):")
    for where, err in bad:
        print(f"\n  {where}")
        for l in err:
            print(f"    {l}")
    sys.exit(1)
print(f"all {len(blocks)} diagrams parse")
