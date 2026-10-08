#!/usr/bin/env python3
"""Keyword checks (docx rules 2, 4, 15-19) for pages that declare frontmatter `keywords`.

Read-only, no network. Pages without `keywords` are skipped: keywords are never invented.
The first keyword is treated as the primary, the rest as secondary/related.

Keywords are search phrases, not literal on-page strings ("SafeSquid proxy service" is
satisfied by "the proxy service in SafeSquid"), so a keyword matches a text when all its
content words are present, in any order. "SafeSquid" and stopwords are ignored.

Usage:
    python3 .claude/tools/audit_keywords.py                  # table of findings
    python3 .claude/tools/audit_keywords.py -o kw.json       # also dump per-page data as JSON
"""
import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
PUB = REPO / "public"
STOP = set("a an and are as at be by for from how in into is it of on or the to with your you using use via vs what when why which".split()) | {"safesquid"}
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
STUFF_DENSITY = 0.03  # exact-phrase share of all words; threshold chosen after reviewing pages above 3%


def stem(w):
    return w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w


def tokens(s):
    return [stem(w) for w in re.findall(r"[a-z0-9]+", s.lower())]


def content(kw):
    t = [w for w in tokens(kw) if w not in STOP]
    return t or tokens(kw)  # a keyword that is only "SafeSquid" falls back to all its words


def matches(kw, text_tokens):
    return all(w in text_tokens for w in content(kw))


def parse(path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = FM.match(raw)
    fm, body = (m.group(1), raw[m.end():]) if m else ("", raw)
    kw = []
    if "keywords:" in fm:
        kw = re.findall(r"^\s+-\s+[\"']?(.+?)[\"']?\s*$", fm.split("keywords:", 1)[1], re.M)
    g = lambda f: (re.search(rf"^{f}:\s*[\"']?(.+?)[\"']?\s*$", fm, re.M) or [None, ""])[1]
    body = re.sub(r"\{/\*.*?\*/\}|^import .*$", "", body, flags=re.S | re.M)
    h1 = (re.search(r"^# (.+)$", body, re.M) or [None, ""])[1]
    prose = re.sub(r"```.*?```", "", body, flags=re.S)
    prose = re.sub(r"^#+ .*$|<[^>]+>", "", prose, flags=re.M)
    return kw, g("title"), g("description"), h1, " ".join(prose.split()[:100]), body


def audit(path):
    kw, title, desc, h1, lead, body = parse(path)
    if not kw:
        return None
    prim, sec = kw[0], kw[1:]
    out = {"primary": prim, "secondary": sec, "flags": []}
    for name, text in (("title", title), ("h1", h1), ("description", desc), ("lead", lead)):
        if name == "h1" and not h1:
            continue  # no body H1: reported by audit_standards.py, not a keyword issue
        ok = matches(prim, set(tokens(text)))
        out[f"primary_in_{name}"] = ok
        if not ok:
            out["flags"].append(("kw-primary-missing-" + name, f'"{prim}" not in {name}'))
    btok = set(tokens(body))
    hit = [k for k in sec if matches(k, btok)]
    out["secondary_covered"] = f"{len(hit)}/{len(sec)}"
    out["secondary_share"] = round(len(hit) / len(sec), 2) if sec else None
    dtext = re.sub(r"\]\([^)]*\)", "]", body)  # link targets repeat the topic by construction
    words = max(len(dtext.split()), 1)
    dens = {k: len(re.findall(re.escape(k.lower()), dtext.lower())) * len(k.split()) / words for k in kw}
    # a bare brand or single-word subject (SafeSquid, NTP, Monit) repeats because the page is about it
    dens = {k: v for k, v in dens.items() if len(content(k)) > 1 and content(k) != ["safesquid"]} or {"-": 0}
    top = max(dens, key=dens.get)
    out["max_density"], out["max_density_kw"] = round(dens[top], 4), top
    if dens[top] > STUFF_DENSITY and words >= 120 and path.name != "main.md":  # hubs are link lists named after the topic
        out["flags"].append(("kw-stuffing-risk", f'"{top}" is {dens[top]:.1%} of words'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output")
    args = ap.parse_args()
    res = {}
    for p in sorted(PUB.rglob("*")):
        if p.suffix in (".md", ".mdx") and "snippets" not in p.relative_to(PUB).parts and "node_modules" not in p.parts:
            r = audit(p)
            if r:
                res[str(p.relative_to(REPO))] = r
    for path, r in res.items():
        for rule, d in r["flags"]:
            print(f"{path} | {rule} | {d}")
    if args.output:
        pathlib.Path(args.output).write_text(json.dumps(res, indent=1))
    print(f"{len(res)} pages with keywords checked; {sum(bool(r['flags']) for r in res.values())} with findings", file=sys.stderr)


if __name__ == "__main__":
    main()
