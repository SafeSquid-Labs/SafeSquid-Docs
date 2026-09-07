#!/usr/bin/env python3
"""Check the reference surfaces `mint broken-links` does not.

`mint broken-links` validates internal PAGE links only. It does not look at image
paths, redirect destinations, snippet imports, or cross-page anchors, and `mint
validate` does not parse Mermaid (see check_mermaid.py for that). There is also no CI
in this repo — .do/app.yaml runs `npm run build` and nothing else — so a rename that
breaks 600+ image references passes every existing gate silently.

Usage, from anywhere:

    python3 .claude/tools/verify_refs.py before      # snapshot before a refactor
    ... make changes ...
    python3 .claude/tools/verify_refs.py after       # snapshot after
    diff -r .claude/tools/_snap/before .claude/tools/_snap/after

Exits non-zero if anything is unresolvable, so it works as a gate.

Written 2026-09-07 during the Phase 3 folder rename, where it was the only thing
standing between a 90-URL migration and a wave of production 404s.
"""
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
PUB = REPO / "public"
SNAP = pathlib.Path(__file__).resolve().parent / "_snap"

out_dir = SNAP / (sys.argv[1] if len(sys.argv) > 1 else "snapshot")
out_dir.mkdir(parents=True, exist_ok=True)

content = sorted(p for p in PUB.rglob("*") if p.suffix in (".md", ".mdx"))
rel = lambda p: str(p.relative_to(PUB))
read = lambda p: p.read_text(encoding="utf-8", errors="replace")

# --- publishable URLs: file path, unless frontmatter slug: overrides it ---------------
SLUGS: set[str] = set()
urls = []
for p in content:
    body = read(p)
    m = re.match(r"^---\n(.*?)\n---", body, re.S)
    slug = re.search(r"^slug:\s*(\S+)", m.group(1), re.M) if m else None
    if slug:
        s = slug.group(1).strip().strip("\"'").lstrip("/")
        SLUGS.add(s)
        urls.append(f"/{s}\t(slug)\t{rel(p)}")
    else:
        urls.append(f"/{p.relative_to(PUB).with_suffix('')}\t(path)\t{rel(p)}")
(out_dir / "urls.txt").write_text("\n".join(sorted(urls)) + "\n")


def page_exists(url: str) -> bool:
    """A docs URL resolves if a .md/.mdx sits at that path, or a slug: claims it."""
    u = url.split("#")[0].split("?")[0].strip("/")
    if not u:
        return True
    return any((PUB / f"{u}{ext}").is_file() for ext in (".md", ".mdx")) or u in SLUGS


def scan(pattern, label, filename):
    """Collect every match of `pattern` across content and check it resolves on disk."""
    rows, bad = [], 0
    for p in content:
        for ref in re.findall(pattern, read(p)):
            ref = ref.rstrip(".,;:")
            ok = (PUB / ref.lstrip("/")).is_file()
            bad += not ok
            rows.append(f"{'OK ' if ok else 'MISSING'}\t{ref}\t{rel(p)}")
    (out_dir / filename).write_text("\n".join(sorted(rows)) + "\n")
    return label, len(rows), bad


results = [
    scan(r"/images/[^\s\"')\]>]+", "image refs", "images.txt"),
    scan(r'from\s+["\'](/snippets/[^"\']+)["\']', "snippet imports", "snippets.txt"),
]

# --- docs.json: nav pages (incl. nested groups) and redirect destinations -------------
cfg = json.loads((PUB / "docs.json").read_text())
pages: list[str] = []


def walk(o):
    if isinstance(o, dict):
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for x in o:
            pages.append(x) if isinstance(x, str) else walk(x)


walk(cfg["navigation"])
page_rows = [f"{'OK ' if page_exists(x) else 'MISSING'}\t/{x}" for x in pages]
(out_dir / "nav_pages.txt").write_text("\n".join(sorted(page_rows)) + "\n")
results.append(("nav pages", len(page_rows), sum(r.startswith("MISSING") for r in page_rows)))

red_rows = []
for r in cfg.get("redirects", []):
    d = r["destination"]
    wild = ":" in d or "*" in d
    state = "WILDCARD" if wild else ("OK " if page_exists(d) else "MISSING")
    red_rows.append(f"{state}\t{r['source']}\t->\t{d}")
(out_dir / "redirects.txt").write_text("\n".join(red_rows) + "\n")
results.append(("redirect dests", len(red_rows), sum(r.startswith("MISSING") for r in red_rows)))

# --- cross-page anchors ---------------------------------------------------------------
anchor_rows = []
for p in content:
    for ref in re.findall(r"\]\((/[^)\s]*#[^)\s]+)\)", read(p)):
        anchor_rows.append(f"{'OK ' if page_exists(ref) else 'MISSING'}\t{ref}\t{rel(p)}")
(out_dir / "anchors.txt").write_text("\n".join(sorted(anchor_rows)) + "\n")
results.append(("cross-page anchors", len(anchor_rows), sum(r.startswith("MISSING") for r in anchor_rows)))

print(f"snapshot -> {out_dir}")
print(f"  content files      {len(content):>5}")
print(f"  publishable URLs   {len(urls):>5}  ({len(SLUGS)} slug overrides)")
for label, total, bad in results:
    print(f"  {label:<18} {total:>5}  MISSING {bad}")

sys.exit(1 if any(bad for _, _, bad in results) else 0)
