#!/usr/bin/env python3
"""Audit public/ pages against the [M] (mechanical) rules in writing_standards.md.

Read-only: prints a Markdown report, edits nothing, makes no network calls.

Usage, from anywhere:

    python3 .claude/tools/audit_standards.py                    # whole site
    python3 .claude/tools/audit_standards.py public/deployment  # one folder or file
    python3 .claude/tools/audit_standards.py -o report.md

Exits non-zero if any ERROR is found, so it can work as a gate. WARN never fails.
Fenced code, inline code and MDX comments are masked before any pattern runs, so
example log lines and `{/* [VERIFY WITH SAFESQUID TEAM]: ... */}` flags never trip a rule.
"""
import argparse
import collections
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
PUB = REPO / "public"

FENCE = re.compile(r"^([ \t]*)(```|~~~).*?^\1\2[ \t]*$", re.S | re.M)
MDX_COMMENT = re.compile(r"\{/\*.*?\*/\}", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
LINK = re.compile(r"(?<!!)\[([^\]\n]*)\]\(([^)\s]+)[^)]*\)")
HYPE = re.compile(r"\b(revolutionary|game[- ]chang(?:ing|er)|best[- ]in[- ]class)\b", re.I)
# Absolute claims about what the product does. Deliberately narrow: bare "never"/"always" also
# appear in fair operational warnings ("files should never be deleted"), so only match claim shapes.
ABSOLUTE = re.compile(
    r"\b(guarantee[sd]?|100\s?%|foolproof|bulletproof|unbreakable|impossible"
    r"|nullif(?:y|ies|ied)|neutrali[sz](?:e|es|ed)|eliminat(?:e|es|ed)"
    r"|completely (?:blind|eliminat\w+|prevent\w*|block\w*|secure\w*|stop\w*)"
    r"|(?:never|no longer) (?:leaves?|reach(?:es)?|bypass(?:es|ed)?|miss(?:es)?|fail(?:s)?)"
    r"|always (?:block|stop|prevent|detect|catch)s?"
    r"|(?:all|every|any) (?:threats?|attacks?|malware))\b", re.I)
# a hedge or negation just before the match means the page is disclaiming, not promising
NEGATED = re.compile(r"\b(not|no|nor|nearly|almost|rarely|may not|cannot|can't|isn't)\b[\w ,'/-]{0,40}$", re.I)
BAD_ANCHOR =re.compile(r"^\s*(click here|here|read more|learn more|link|this link|more)\s*$", re.I)
BAD_HEADING = re.compile(r"^(overview|introduction)$", re.I)
QUESTION_START = re.compile(r"^(what|why|how|when|where|which|who|can|does|do|is|are|should|will)\b", re.I)

# Legacy sections follow older conventions; tag them so their findings don't bury Style A's.
TAGS = {"configuration": "legacy-C", "use_cases": "legacy-B", "blog": "blog", "snippets": "snippet"}


def mask(text):
    """Blank out code and comments, keeping newlines so line numbers stay correct."""
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    for rx in (FENCE, MDX_COMMENT):
        text = rx.sub(blank, text)
    return INLINE_CODE.sub(blank, text)


def style_tag(path):
    return TAGS.get(path.relative_to(PUB).parts[0], "style-A")



# ---------------------------------------------------------------------------
# Full-rubric checks (docs-house-style + writing_standards.md + SS docs rules.docx)
# ---------------------------------------------------------------------------
BANNED_COMPONENTS = re.compile(r"<(CardGroup|Info|CodeGroup|Check|Columns|Expandable|Update|Icon)\b")
HEDGE = re.compile(r"\b(may|might|perhaps|possibly)\b", re.I)
FIRST_PERSON = re.compile(r"\b(we|our|ours|we're|we'll|we've)\b", re.I)
PAGE_DESCRIBES = re.compile(r"\bThis (page|section|document|guide|article|topic) (describes|explains|covers|provides|shows|outlines)\b", re.I)
EMOJI = re.compile("[✅❌⚠]")
SECRET = re.compile(r"(AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|(?:password|passwd|api[_-]?key|secret)\s*[:=]\s*[\"']?(?!your|<|\*|xxx|example|changeme|password)[A-Za-z0-9/+_-]{8,})", re.I)
MAN_PAGE = re.compile(r"CLI man page|\bsafesquid-\w+\(\d\)", re.I)
# lowercase "safesquid" is a service/account/path name in logs and commands; only flag it as a product name
SPELLING = re.compile(r"\b(Safesquid|Safe Squid)\b|\b(?:in|the|of) safesquid (?:interface|swg|proxy|server)\b")
IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)")
MD_LINK_TARGET = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s")
SPACED_TABLE = re.compile(r"^\|\s+:?-{2,}:?\s+\|")
RUNNABLE = {"bash", "sh", "shell", "powershell", "cmd", "zsh"}
FM_FORBIDDEN = ("slug", "sidebarTitle", "sidebar_position")
_REDIRECTS = None


def _redirect_sources():
    global _REDIRECTS
    if _REDIRECTS is None:
        import json
        try:
            d = json.loads((PUB / "docs.json").read_text())
            _REDIRECTS = {r["source"].rstrip("/") for r in d.get("redirects", [])}
        except Exception:
            _REDIRECTS = set()
    return _REDIRECTS


def _link_exists(target):
    p = target.split("#")[0].split("?")[0].rstrip("/")
    if not p:
        return True
    rel = p.lstrip("/")
    for cand in (f"{rel}.md", f"{rel}.mdx", f"{rel}/main.md", f"{rel}/index.md", f"{rel}/index.mdx", rel):
        f = PUB / cand
        if f.is_file():
            return True
    return p in _redirect_sources()


def _fences(raw_lines):
    """Yield (open_line_no, info, body_lines) for each fenced block."""
    i, n = 0, len(raw_lines)
    while i < n:
        m = re.match(r"^\s*(```+|~~~+)\s*(.*)$", raw_lines[i])
        if m:
            fence, info, j = m.group(1), m.group(2).strip(), i + 1
            while j < n and not re.match(r"^\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", raw_lines[j]):
                j += 1
            yield i + 1, info, raw_lines[i + 1:j]
            i = j
        i += 1


def _prose(masked_lines, offset):
    """(line_no, text) for plain prose lines: no headings, tables, imports, tag-only lines."""
    for i, l in enumerate(masked_lines, 1):
        if i <= offset:
            continue
        s = l.strip()
        if not s or s.startswith(("#", "|", "import ", "<", ">", "---")) or re.fullmatch(r"[-*]{3,}", s):
            continue
        s = re.sub(r"^([-*+]|\d+\.)\s+", "", s)
        s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"https?://\S+|<[^>]+>|[*_]{1,3}", "", s)
        yield i, s


def extra_checks(path, raw, masked_lines, offset, tag, fm, own_words, add):
    raw_lines = raw.split("\n")
    strict = tag == "style-A"
    is_page = tag != "snippet"
    long_page = own_words >= 120

    # frontmatter
    if is_page:
        if not re.search(r"^keywords:", fm, re.M):
            add(1, "WARN", "frontmatter-keywords", "missing keywords")
        elif strict:
            n = len(re.findall(r"^\s+-\s+\S", fm, re.M))
            if not 4 <= n <= 6:
                add(1, "WARN", "frontmatter-keywords-count", f"{n} keywords (house style: 4-6)")
        if strict:
            for k in FM_FORBIDDEN:
                if re.search(rf"^{k}:", fm, re.M):
                    add(1, "WARN", "frontmatter-forbidden-key", k)

    # H1 / heading depth
    heads = [(i, len(m.group(1)), m.group(2)) for i, l in enumerate(masked_lines, 1)
             if i > offset and (m := HEADING.match(l))]
    h1 = [h for h in heads if h[1] == 1]
    tm = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", fm, re.M)
    if is_page and long_page and not h1:
        add(1, "WARN", "no-body-h1", "no H1 in body")
    if h1 and tm and h1[0][2].strip().lower() == tm.group(1).strip().lower():
        add(h1[0][0], "WARN", "h1-restates-title", h1[0][2])
    if strict:
        for i, lvl, t in heads:
            if lvl >= 4:
                add(i, "WARN", "heading-h4", t)
    titles = [t.lower() for _, _, t in heads]

    # page structure
    if is_page and long_page and path.name != "main.md":
        if not any(re.match(r"next steps?|related", t) for t in titles):
            add(1, "WARN", "missing-next-steps", "no Next steps section")
        elif strict:
            idx = next(i for i, t in enumerate(titles) if re.match(r"next steps?|related", t))
            start = heads[idx][0]
            end = next((h[0] for h in heads[idx + 1:] if h[1] <= heads[idx][1]), len(masked_lines) + 1)
            links = sum(len(MD_LINK_TARGET.findall(masked_lines[k])) for k in range(start, end - 1))
            if links != 3:
                add(start, "WARN", "next-steps-count", f"{links} links (house style: exactly 3)")
    has_proc = bool(re.search(r"<Steps>|^\s*\d+\.\s", raw, re.M)) or any(i.split()[:1] and i.split()[0] in RUNNABLE for _, i, _ in _fences(raw_lines))
    ref_section = path.relative_to(PUB).parts[0] in ("troubleshooting", "architecture", "faqs", "reporting") or path.name == "main.md"
    if is_page and has_proc and own_words >= 300 and not ref_section:  # troubleshooting/reference pages are not how-tos
        if not any("verif" in t or "validat" in t or "confirm" in t for t in titles):
            add(1, "WARN", "missing-verification", "procedural page, no Verify heading")
        if not any("troubleshoot" in t or "symptom" in t or "fail" in t for t in titles):
            add(1, "WARN", "missing-troubleshooting", "procedural page, no Troubleshoot heading")

    # code fences
    nofence = runnable = 0
    for ln, info, body in _fences(raw_lines):
        lang = info.split()[0] if info else ""
        if not lang:
            nofence += 1
        if lang in RUNNABLE:
            runnable += 1
        if lang == "mermaid" and body and not re.match(r"\s*flowchart TB", body[0]):
            add(ln, "WARN", "mermaid-style", body[0].strip())
    if nofence:
        add(1, "WARN", "fence-no-language", f"{nofence} fenced blocks without a language tag")
    exp = len(re.findall(r"Expected result", raw, re.I))
    if runnable and exp < runnable:
        add(1, "WARN" if strict else "INFO", "missing-expected-result", f"{runnable} runnable fences, {exp} 'Expected result' lines")

    # prose rules
    sent_long, hedges, fp = [], [], []
    para_run, para_long = 0, 0
    prose = list(_prose(masked_lines, offset))
    prev = -2
    for ln, s in prose:
        if LIST_ITEM.match(raw_lines[ln - 1]):
            para_run, prev = 0, ln  # list items are not paragraphs
            continue
        para_run = para_run + 1 if ln == prev + 1 else 1
        if para_run == 6:
            para_long += 1
        prev = ln
        for sent in re.split(r"(?<=[.!?])\s+", s):
            if len(sent.split()) > 20:
                sent_long.append((ln, len(sent.split()), sent))
        for m in HEDGE.finditer(s):
            hedges.append((ln, s[max(0, m.start() - 25): m.end() + 25]))
        for m in FIRST_PERSON.finditer(s):
            fp.append((ln, s[max(0, m.start() - 25): m.end() + 25]))
        if PAGE_DESCRIBES.search(s):
            add(ln, "WARN", "lead-describes-page", s)
        if SPELLING.search(re.sub(r"\S*/\S*|\S+\.(com|org|log|net)\S*", "", s)):
            add(ln, "WARN", "term-spelling", s)
    if sent_long:
        w = max(sent_long, key=lambda x: x[1])
        add(w[0], "WARN" if strict else "INFO", "sentence-over-20-words", f"{len(sent_long)} sentences; longest {w[1]} words")
    if para_long:
        add(1, "WARN" if strict else "INFO", "paragraph-over-5-lines", f"{para_long} paragraphs")
    if hedges:
        add(hedges[0][0], "WARN" if strict else "INFO", "hedging-may-might", f"{len(hedges)}x e.g. {hedges[0][1]}")
    if fp:
        add(fp[0][0], "WARN", "first-person-we-our", f"{len(fp)}x e.g. {fp[0][1]}")

    # whole-file patterns
    for i, l in enumerate(masked_lines, 1):
        if i <= offset:
            continue
        if BANNED_COMPONENTS.search(l):
            add(i, "WARN", "banned-component", l)
        if "<!--" in l:
            add(i, "ERROR", "html-comment", l)
        if "PBAC" in l:
            add(i, "WARN", "pbac-string", l)
        if re.match(r"^#{2,}\s+Available items", l):
            add(i, "WARN", "stub-hub-available-items", l)
        if SPACED_TABLE.match(l.strip()):
            add(i, "INFO", "table-delimiter-spaced", l)
        for m in MD_LINK_TARGET.finditer(l):
            t = m.group(1)
            if re.match(r"(https?:|mailto:|tel:|#)", t) or t.startswith("{"):
                continue
            if re.search(r"\.mdx?(#|$)", t):
                add(i, "WARN", "link-has-extension", t)
            elif re.match(r"^/[A-Z]", t):
                add(i, "WARN", "link-legacy-capitalized-slug", t)
            elif not t.startswith("/"):
                add(i, "WARN", "link-relative", t)
            if not _link_exists(t):
                add(i, "ERROR", "broken-internal-link", t)
        for m in IMG.finditer(l):
            alt, src = m.group(1).strip(), m.group(2)
            if not alt:
                add(i, "WARN", "image-alt-empty", src)
            if not re.match(r"https?:", src):
                if not src.startswith("/images/"):
                    add(i, "WARN", "image-path", src)
                elif not src.lower().endswith(".webp"):
                    add(i, "WARN", "image-not-webp", src)
                if src.startswith("/") and not (PUB / src.lstrip("/")).is_file():
                    add(i, "ERROR", "image-missing", src)
        # <Frame><img/></Frame> is the house convention for console screenshots (docs-house-style); flag only a bare <img>
        if re.search(r"<img\b", l) and not re.search(r"<Frame\b", " ".join(raw_lines[max(0, i - 3):i])):
            add(i, "WARN", "raw-img-tag", l)
    for i, l in enumerate(raw_lines, 1):
        if MAN_PAGE.search(l):
            add(i, "WARN", "fabricated-man-page-ref", l)
        if SECRET.search(l):
            add(i, "ERROR", "possible-secret", re.sub(r"[A-Za-z0-9/+_-]{12,}", "<redacted>", l))
    if strict:
        # emoji markers: house style forbids, writing_standards.md prescribes. Flag to surface the conflict.
        if EMOJI.search(raw):
            add(1, "INFO", "emoji-markers", "uses ✅/❌/⚠️ (house style forbids; writing_standards.md prescribes)")


def tree_checks():
    """Cross-file rules: main.md hubs, snake_case names, docs.json registration."""
    import json
    out = []  # (relpath, line, sev, rule, snippet)
    skip = {"images", "styles", "snippets", "node_modules"}
    dirs = {p.parent for p in PUB.rglob("*") if p.suffix in (".md", ".mdx") and not (set(p.relative_to(PUB).parts) & skip)}
    for d in sorted(dirs):
        if d != PUB and not (d / "main.md").exists() and not (d / "main.mdx").exists():
            out.append((d.relative_to(REPO), 1, "WARN", "missing-main-md", "folder has pages but no main.md hub"))
    for p in sorted(PUB.rglob("*")):
        if set(p.relative_to(PUB).parts) & skip or p.name.startswith(".") or p.is_dir() and p == PUB:
            continue
        if p.suffix in (".md", ".mdx") and (re.search(r"[A-Z\s-]", p.stem) or " " in p.name):
            out.append((p.relative_to(REPO), 1, "WARN", "filename-not-snake-case", p.name))
    d = json.loads((PUB / "docs.json").read_text())
    reg = []

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "pages":
                    for it in v:
                        reg.append(it) if isinstance(it, str) else walk(it)
                else:
                    walk(v)
        elif isinstance(x, list):
            for it in x:
                walk(it)
    walk(d["navigation"])
    regset = set(reg)
    for r, c in collections.Counter(reg).items():
        if c > 1:
            out.append((pathlib.Path("public/docs.json"), 1, "WARN", "page-registered-twice", r))
    for r in sorted(regset):
        if not any((PUB / f"{r}{e}").is_file() for e in (".md", ".mdx")):
            out.append((pathlib.Path("public/docs.json"), 1, "ERROR", "registered-page-missing", r))
    for p in sorted(PUB.rglob("*")):
        if p.suffix in (".md", ".mdx") and not (set(p.relative_to(PUB).parts) & skip) and p.name not in ("main.md", "main.mdx"):
            rel = str(p.relative_to(PUB).with_suffix(""))
            if rel not in regset:
                out.append((p.relative_to(REPO), 1, "WARN", "page-not-in-docs-json", rel))
    return out


def audit(path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    out = []  # (line, severity, rule, snippet)
    add = lambda line, sev, rule, snip="": out.append((line, sev, rule, snip.strip()[:90]))

    fm_match = FRONTMATTER.match(raw)
    fm = fm_match.group(1) if fm_match else ""
    # snippets are includes rendered inside other pages: no title/description of their own
    if style_tag(path) != "snippet":
        if not re.search(r"^title:\s*\S", fm, re.M):
            add(1, "ERROR", "frontmatter-title", "missing title")
        if not re.search(r"^description:\s*\S", fm, re.M):
            add(1, "WARN", "frontmatter-description", "missing description")

    offset = raw[: fm_match.end()].count("\n") if fm_match else 0
    lines = mask(raw).split("\n")

    for i, l in enumerate(raw.split("\n"), 1):
        if "NEEDS-SME-REVIEW" in l:
            add(i, "ERROR", "old-marker", l)
        # masked text has comments blanked, so a hit here is a marker readers would see
        if "VERIFY WITH SAFESQUID TEAM" in lines[i - 1]:
            add(i, "ERROR", "visible-marker", l)

    h1s, prev = 0, 0
    for i, l in enumerate(lines, 1):
        if i <= offset:
            continue
        m = HEADING.match(l)
        if m:
            level, text = len(m.group(1)), m.group(2)
            h1s += level == 1
            if prev and level > prev + 1:
                add(i, "WARN", "heading-skip", f"H{prev} -> H{level}: {text}")
            prev = level
            if BAD_HEADING.match(text):
                add(i, "WARN", "heading-banned-word", text)
        for lm in LINK.finditer(l):
            if BAD_ANCHOR.match(lm.group(1)):
                add(i, "ERROR", "link-text", f"[{lm.group(1)}]({lm.group(2)})")
        for hm in HYPE.finditer(l):
            add(i, "WARN", "hype-word", l[max(0, hm.start() - 30): hm.end() + 30])
        for am in ABSOLUTE.finditer(l):
            if NEGATED.search(l[max(0, am.start() - 50): am.start()]):
                continue  # "not a compliance guarantee", "nearly impossible": hedges, the wording we want
            add(i, "WARN", "absolute-claim", l[max(0, am.start() - 40): am.end() + 40])

    # the frontmatter title is the page H1 in Mintlify, so a body H1 is already a second one
    if h1s > 1:
        add(1, "WARN", "multiple-h1", f"{h1s} H1 headings in body")

    t_body = re.sub(r"^import .*$|\{/\*.*?\*/\}|<[A-Z]\w*\s*/>", "", raw[fm_match.end():] if fm_match else raw, flags=re.S | re.M)
    extra_checks(path, raw, lines, offset, style_tag(path), fm, len(t_body.split()), add)

    h23 = [HEADING.match(l) for l in lines[offset:]]
    h23 = [m.group(2) for m in h23 if m and len(m.group(1)) in (2, 3)]
    return out, (sum(bool(QUESTION_START.match(t) or t.endswith("?")) for t in h23), len(h23))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="*", help="files or folders (default: public/)")
    ap.add_argument("-o", "--output", help="write report here instead of stdout")
    args = ap.parse_args()

    roots = [pathlib.Path(t).resolve() for t in args.targets] or [PUB]
    files = sorted({p for r in roots for p in ([r] if r.is_file() else r.rglob("*"))
                    if p.suffix in (".md", ".mdx") and PUB in p.parents})

    findings = collections.defaultdict(list)  # tag -> [(path, line, sev, rule, snippet)]
    qstats = collections.defaultdict(lambda: [0, 0])
    for p in files:
        res, (q, n) = audit(p)
        tag = style_tag(p)
        qstats[tag][0] += q
        qstats[tag][1] += n
        findings[tag] += [(p.relative_to(REPO), *r) for r in res]

    if not args.targets:  # cross-file rules only make sense for a whole-site run
        findings["site-structure"] += [(r[0], *r[1:]) for r in tree_checks()]

    rep = [f"# Standards audit: {len(files)} pages\n"]
    errors = sum(1 for v in findings.values() for f in v if f[2] == "ERROR")
    for tag in sorted(set(findings) | set(qstats)):
        fs = findings[tag]
        q, n = qstats[tag]
        rep.append(f"## {tag}: {len(fs)} findings, question-style H2/H3: {q}/{n}\n")
        counts = collections.Counter((f[3], f[2]) for f in fs)
        rep += [f"- `{rule}` ({sev}): {c}" for (rule, sev), c in counts.most_common()]
        rep.append("\n| Page | Line | Sev | Rule | Snippet |\n|---|---|---|---|---|")
        for path, line, sev, rule, snip in sorted(fs, key=lambda f: (f[2] != "ERROR", str(f[0]), f[1])):
            snip = snip.replace("|", "\\|")
            rep.append(f"| {path} | {line} | {sev} | {rule} | {snip} |")
        rep.append("")
    text = "\n".join(rep)
    if args.output:
        pathlib.Path(args.output).write_text(text, encoding="utf-8")
        print(f"wrote {args.output}: {len(files)} pages, {errors} errors")
    else:
        print(text)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
