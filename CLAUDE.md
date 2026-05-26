# Documentation Agent Guide

**RULE: No files or folders should have space in their name. Always use underscores (_). Example: getting_started, not Getting Started or getting started.**

This repo contains CISO-grade, enterprise documentation for SafeSquid SWG. Agents create and maintain content for security and network technicians, system administrators, operations teams, CISOs, and security leadership.

## Operating Principles

**Content-first. Infrastructure-never.**

**CRITICAL**: This agent exists only for documentation and content creation.

**Contribution:** Documentation changes are submitted via pull request. All edits require review before merge.

## Agent Scope and Limitations

✅ **DO:**
- Create and edit documents in the `public/` folder
- Create and edit blog posts in the `blog/` folder (repo root, not inside public/)
- Research and write technically precise content
- Update existing documentation files; add diagrams, screenshots, and log evidence

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

SafeSquid SWG documentation (Mintlify) is a technically precise knowledge base for enterprise zero-trust web security. Docs serve both "get it done" (task-based) and "justify/audit" (control mapping, evidence, compliance) needs. Every page must meet the CISO-grade bar — see `.claude/skills/doc_writer/references/writing_standards.md`.

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

```
/
├── public/                  ← Mintlify project root (docs.json lives here)
│   ├── docs.json            ← Navigation, theme, tabs — do not modify except to add pages
│   ├── images/              ← All images — reference as /images/category/name.webp
│   ├── getting-started/
│   ├── guides/
│   ├── api/
│   ├── architecture/
│   ├── cli/
│   ├── faqs/
│   ├── integrations/
│   ├── interface/
│   ├── troubleshooting/
│   └── use-cases/
├── blog/                    ← Date-prefixed blog posts (YYYY-MM-DD-Title.md)
├── .claude/
│   ├── settings.json
│   └── agents/              ← Sub-agent definitions
│       ├── doc-researcher.md
│       ├── doc-writer.md
│       ├── doc-validator.md
│       └── safesquid-sysadmin.md
│   └── skills/              ← Project skills
├── .agents -> .claude
├── CLAUDE.md                ← This file
├── AGENTS.md -> CLAUDE.md
├── README.md
├── package.json             ← do not modify
└── .github/                 ← do not modify without a ticket
```

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

**ALWAYS invoke the `doc_writer` skill before any documentation creation or revision task.** This applies to every page, section, main.md, blog post, or content edit — no exceptions for "small" changes.

Skill invocation order for common tasks:
- **Writing or editing a doc** → `doc_writer` (always first)
- **Research needed** → `doc_researcher` before `doc_writer`
- **Validation** → `doc_validator` after drafting
- **Topology or HA content** → `deployment_architect_writer`
- **Compliance mapping** → `compliance_mapper`
- **Troubleshooting content** → `troubleshooting_runbook_author`
- **Screenshots or log evidence** → `evidence_collector`
- **Navigation or IA decisions** → `information_architect`
- **UI path verification** → `safesquid_sysadmin`

### What to read before starting

1. `CLAUDE.md` (this file) — scope, naming, repo structure, skill routing
2. `public/docs.json` — existing navigation
3. The target section and its `main.md`

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
