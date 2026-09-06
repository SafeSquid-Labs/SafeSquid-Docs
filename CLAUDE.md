# Documentation Agent Guide

**RULE: No files or folders should have space in their name. Always use underscores (_). Example: getting_started, not Getting Started or getting started.**

This repo contains CISO-grade, enterprise documentation for SafeSquid SWG. Agents create and maintain content for security and network technicians, system administrators, operations teams, CISOs, and security leadership.

## Operating Principles

**Content-first. Infrastructure-never.**

**CRITICAL**: This agent exists only for documentation and content creation.

**Contribution:** Documentation changes are submitted via pull request. All edits require review before merge.

**Branching (current, set 2026-09-04 — supersedes the single-worktree note of 2026-09-03):**
`main` is never touched directly — no commits, no work. Work flows through **three tiers**:

| Tier | What it is | Current instance |
|---|---|---|
| 1. `main` | Merge destination. Never worked in. | `main` |
| 2. **Integration branch** | Collects finished task work; the branch a PR to `main` is opened *from*. The main checkout at the repo root sits here. | `docs/config-tab-content` |
| 3. **Task branches, each in its own worktree** | Where changes are actually made, one per task chunk. Merges into tier 2 when done, then the worktree and branch are deleted. | `docs/broken-links-reconcile` (bringing `docs/broken-links` up to date with `main`'s PR #8 restructure so it can open its own PR cleanly); `docs/broken-links` is a deliberate exception — left unmerged pending its own separate PR to `main`, not tier 2 |

Never commit task work directly onto the integration branch — that collapses tiers 2 and 3 and
means a PR under review keeps changing underneath the reviewer. (That is exactly what went
wrong before 2026-09-04: `docs/deployment-scroll-reduction` was simultaneously the only
worktree, the working branch, and the head of PR #8, so every commit landed in the open PR.)

Worktree convention — sibling directory, name matching the task suffix:

```sh
git worktree add ../SafeSquid-Docs-<task> -b docs/<task> docs/config-tab-content
# ... work, commit in that worktree ...
git -C /Users/sriharichari/Documents/SafeSquid-Docs merge docs/<task>
git worktree remove ../SafeSquid-Docs-<task> && git branch -d docs/<task>
```

To preview a worktree with `npm run dev`, add a `.claude/launch.json` entry pointing
`--prefix` at that worktree path (that file is gitignored — personal per machine, so repoint
or remove any stale entry from a deleted worktree rather than trusting it blindly).

When merging a task branch up, resolve conflicts by hand rather than force-picking one side —
both sides can carry independent restructuring that needs reconciling (see the 2026-09-03
merge commit `2348d94` for a worked example: two independently-restructured versions of the
same tab had to be combined, not overwritten; and the 2026-09-04 reconciliation of PR #8's
merge to `main` against `docs/config-tab-content` for a case where both sides had independently
live-verified the same admin-console pages and reached different conclusions on some of them —
resolved by re-checking the live console per page rather than picking a side by recency).

**PR #8 merged to `main` on 2026-09-04.** `docs/deployment-scroll-reduction` (its head) and
`docs/main-reconcile` (the task branch that reconciled tier 2 against the merge) are both
retired and deleted locally. `docs/broken-links` predates PR #8 too — it branched before the
restructure and was never part of that reconciliation, so it hit the same class of conflicts
independently when merged against current `main` via `docs/broken-links-reconcile` (2026-09-06):
several files had identical pre-merge content to what `docs/main-reconcile` had already resolved
(safe to reuse that resolution directly), plus 4 files where `docs/broken-links`'s own link-fixing
work turned out to be a verified superset of the one fix PR #8 happened to make in each.

Update this table whenever a branch here is created, renamed, merged, or retired.

**Before merging into any named branch** (not just `main`), confirm it's actually live and current, don't assume the name alone means it's the right target: check whether it still exists on the remote (`gh api repos/<org>/<repo>/branches/<name>`; GitHub deletes a branch by default after a squash-merge) and whether it's already content-identical to `main` (`git diff main <branch>` — empty means it's stale and redundant, a likely sign it was already squash-merged and abandoned). `restructure/legacy-migration-and-admin-move` was exactly this on 2026-09-03: content-identical to `main`, deleted on GitHub, safe to skip rather than merge into.

**Pull requests are drafted for approval before creation.** Write the title and full body, share it, and wait for an explicit go-ahead before running `gh pr create` — don't create the PR first and refine after. When drafting the body in a scratch file, keep it to *only* the body text; a file that also carries a `# Title` / `# Base branch` header for your own reference must be trimmed to the body section before it's passed to `--body-file`, or that scaffolding leaks into the live PR.

## Agent Scope and Limitations

✅ **DO:**
- Create and edit documents in the `public/` folder
- Create and edit blog posts in the `public/blog/` folder
- Research and write technically precise content
- Update existing documentation files; add diagrams, screenshots, and log evidence
- Use the `graphify-out/` directory as a temporary scratchpad for drafting and multi-agent handoffs before committing final files to `public/`.

❌ **DO NOT:**
- Build or modify Mintlify hosting bindings outside this repository without an explicit ticket
- Change root CI secrets, deployment credentials, or `package.json` dependencies without an explicit ticket
- Modify build scripts, deployment processes, or project structure outside content folders
- Install dependencies or run build commands

## Naming and Path Rules

- No spaces in file or folder names.
- Use **snake_case** for folders and doc names: `getting_started`, `ssl_inspection`, `audit_and_forensics`.
- Use predictable asset names: `feature-short_description.webp`.

## Project Overview

SafeSquid SWG documentation (Mintlify) is a technically precise knowledge base for enterprise zero-trust web security. Docs serve both "get it done" (task-based) and "justify/audit" (control mapping, evidence, compliance) needs. Every page must match the house style in `.claude/skills/docs-house-style/SKILL.md` and meet the CISO-grade bar in `.claude/skills/doc_writer/references/writing_standards.md`.

## Content Types

- **get_started** — fastest path to first working deployment.
- **how_to** — one task end-to-end with verification.
- **admin_guide** — day-2 operations, lifecycle, troubleshooting.
- **concepts** — definitions, models, evaluation order, data flows.
- **reference** — fields, parameters, defaults, limits, CLI/API.
- **troubleshooting** — diagnosis → root cause → fix → verify.
- **release_notes** — version/date, summary; link from relevant docs.

---

## Repository Setup and Commands

Node >=20.17.0 (LTS). No `.nvmrc` — pin explicitly:

```sh
nvm install 20 && nvm use 20
node -v   # must print v20.x
```

```sh
npm install            # run once from repo root
npm run dev            # local preview → http://localhost:3000
npm run validate       # must exit 0 before any PR
npm run broken-links   # optional: find dead links
```

All scripts change into `public/` before invoking the `mint` CLI. **Never run `mint` commands directly** from the repo root.

CI runs `npm run validate` on every push and PR to `main`, `dev`, and `mintlify-docs`.

---

## Repository Layout

The tree under `public/` is the Mintlify project root (`docs.json` lives there); run `ls public/`
for the current section list rather than trusting a copy here. Images go in `public/images/` and
are referenced as `/images/category/name.webp`; blog posts in `public/blog/` are date-prefixed
`YYYY-MM-DD-Title.md`. Sub-agent definitions are in `.claude/agents/`, project skills in
`.claude/skills/`, and `AGENTS.md` is a symlink to this file.

Every `public/<section>/` folder must contain a `main.md` navigation hub.
New pages must be registered in `public/docs.json` under the correct `navigation.tabs` group.

---

## File Patterns — Do Not Edit

- `package.json`, `package-lock.json` — infrastructure
- `.github/` — CI workflows
- `public/docs.json` — navigation structure. **Exception:** add new pages to `navigation` when adding content.
- `public/robots.txt` — search indexing
- `.claude/settings.json` — agent runtime
- `_old_getting_started_backup/` — archived; do not use

---

## Agent Context and Bootstrap

### Skill invocation mandate

**Read `.claude/skills/docs-house-style/SKILL.md` before writing or modifying any content.**
It is the authoritative description of current house style — voice, page structure,
component rules, source-provenance comments, and `docs.json` navigation conventions. Where
it conflicts with `doc_writer/references/writing_standards.md`, the house-style skill wins.

**ALWAYS invoke the `doc_writer` skill before any documentation creation or revision task.** This applies to every page, section, main.md, blog post, or content edit — no exceptions for "small" changes.

**ALWAYS live-verify any step, menu path, field name, default value, or behavioral claim about the admin console against `http://safesquid.cfg` before it ships** (added 2026-09-04) — via the `safesquid_admin` MCP browser plugin (deferred tools, load via `ToolSearch`; drive it directly — the `safesquid-sysadmin` subagent was non-functional as of 2026-09-03). No exceptions for content migrated from a legacy source, edits to existing pages, or "it matches what's already there." Full rule, scope, and the not-possible-to-verify fallback (`NEEDS-SME-REVIEW` + `**Missing:**`) are in `.claude/skills/docs-house-style/SKILL.md`'s "Third hard rule" — read it before writing anything console-related.

Skill invocation order for common tasks:
- **Writing or editing a doc** → `doc_writer` (always first)
- **Research needed** → `doc_researcher` before `doc_writer`
- **Validation** → `doc_validator` after drafting
- **Topology or HA content** → `deployment_architect_writer`
- **Compliance mapping** → `compliance_mapper`
- **Troubleshooting content** → `troubleshooting_runbook_author`
- **Screenshots or log evidence** → `evidence_collector`
- **Navigation or IA decisions** → `information_architect`
- **UI path verification** → `safesquid_sysadmin` (mandatory, not optional — see above)

### Model routing — plan on Opus, execute on Sonnet (set 2026-09-04)

`opusplan` is discontinued. The replacement is an explicit split between the **main session**
and **subagents**:

| Layer | Model | Owns |
|---|---|---|
| Main session | **Opus** (user sets it with `/model opus`) | Planning, IA and navigation decisions, resolving contradictions between sources, deciding what to write and where, reviewing subagent output, drafting PR bodies |
| Subagents (`.claude/agents/*.md`) | **Sonnet** (pinned via `model: sonnet` frontmatter) | Executing a decided plan: drafting a page from a brief, research passes, validation gates, browser UI verification |

**The main session cannot change its own model** — only the user can, via `/model`. So the
division holds only if the session starts on Opus and *delegates execution* rather than doing
it inline. When a task is mostly mechanical (apply an agreed edit to 6 pages, run the validator
loop), hand it to a subagent instead of burning Opus on it.

**Per-invocation override**: the `Agent` tool's `model` parameter beats the frontmatter. Use
`model: opus` for a subagent task that is genuinely hard reasoning rather than execution — for
example rewriting `admin_guide/start_here/architecture.mdx`'s request-pipeline prose, or
reconciling two sources that disagree on a core mechanic. Don't use it as a default.

**What counts as planning (Opus, main session):** deciding whether a legacy-source claim is
trustworthy; choosing which of two contradictory descriptions is correct; page decomposition
and `docs.json` placement; scoping a restructure; deciding what needs a `NEEDS-SME-REVIEW`
flag versus a real answer.

**What counts as execution (Sonnet, subagent):** writing prose to an agreed outline; applying
a known correction across pages; running `npm run validate` and fixing what it reports; live
UI verification via the `safesquid_admin` plugin against a supplied list of paths; capturing
screenshots.

### What to read before starting

1. `.claude/skills/docs-house-style/SKILL.md` — house style: voice, structure, sourcing, navigation
2. `CLAUDE.md` (this file) — scope, naming, repo structure, skill routing
3. `public/docs.json` — existing navigation
4. The target section and its `main.md`

Skip: `.github/`, `package.json`, `package-lock.json`, `_old_getting_started_backup/`.

### Agent system bootstrap

**Claude Code** — reads `CLAUDE.md` and `.claude/` directly. Sub-agents in `.claude/agents/`. `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` set in `.claude/settings.json`.

**Gemini CLI / GitHub Copilot / all other frameworks** — read `AGENTS.md` (symlink → `CLAUDE.md`). Do not create framework-specific config files without a ticket.

### Sub-agent workflow

| Agent | Role | Entry point |
|---|---|---|
| `doc-researcher` | Web research; returns structured notes; never edits files | Called by `doc-writer` |
| `doc-writer` | Lead writer; drives researcher; drafts docs; sends to validator | Top-level invocation |
| `doc-validator` | Gatekeeper; runs 3 gates (checklist, UI verify, build); PASS/FAIL only | Called by `doc-writer` |
| `safesquid-sysadmin` | Browser-verifies SafeSquid UI paths at `http://safesquid.cfg` | Called by `doc-validator` |

Full definitions in `.claude/agents/`. Invoke `doc-writer` to start a documentation task.

### Test expectations

`npm run validate` must exit `0` before any pull request. CI enforces this on every push. A passing validate is the minimum bar; it does not replace content review.
