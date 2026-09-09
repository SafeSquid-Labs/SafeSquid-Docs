# Verification tools

Two gates that cover what the Mintlify CLI does not. Run them alongside
`npm run validate` and `npm run broken-links`, not instead of them.

```bash
python3 .claude/tools/verify_refs.py before    # snapshot, then make changes
python3 .claude/tools/verify_refs.py after
diff -r .claude/tools/_snap/before .claude/tools/_snap/after

python3 .claude/tools/check_mermaid.py
```

Both exit non-zero on failure. `_snap/` is scratch output — do not commit it.

## Why these exist

`mint broken-links` validates **internal page links only**. `mint validate` does not
parse Mermaid. And there is **no CI**: `.do/app.yaml` runs `npm run build` on a push to
`main` and nothing else. (`README.md` claims a `.github/workflows/build_and_publish.yml`
that does not exist — that claim is stale.)

So four surfaces had nothing checking them, and one of them is large:

| Surface | Volume | Checked by |
|---|---|---|
| Internal page links | ~1,600 | `mint broken-links` |
| Image references | ~650 | **verify_refs.py** |
| Redirect destinations | ~120 | **verify_refs.py** |
| Snippet imports | ~30 | **verify_refs.py** |
| Cross-page anchors | ~7 | **verify_refs.py** |
| Mermaid diagrams | ~45 | **check_mermaid.py** |

`mint broken-links` can cover anchors and snippets with `--check-anchors
--check-snippets`, which the npm scripts do not pass. It still never checks images or
redirect destinations.

## What they have already caught

- **`icap.mdx` had never rendered in production.** Its diagram used `call` as a node id,
  a reserved Mermaid token. Every gate passed; the live page showed a syntax-error box.
- **A rename that breaks image paths is invisible.** During the 2026-09-07 folder rename,
  651 image references moved and nothing else in the repo would have noticed a mistake.
- **Redirect destinations can rot into 404s silently.** 34 destinations pointed into
  `/admin_guide/`; renaming that directory would have turned each into a
  redirect-to-nowhere, which no tool reports.

## Notes

- Paths are derived from the script's own location, so they run from any working
  directory and survive a fresh clone.
- `verify_refs.py` understands frontmatter `slug:` overrides (41 pages publish at a URL
  unrelated to their file path) and nested `docs.json` navigation groups.
- `check_mermaid.py` needs network on first run — `npx` fetches
  `@mermaid-js/mermaid-cli` — and takes a couple of minutes for ~45 blocks.
