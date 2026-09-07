# Documentation Agent Guide

**RULE: No spaces in file or folder names. Always use snake_case.**

This repository contains CISO-grade, enterprise documentation for SafeSquid SWG (Mintlify). Content targets security engineers, network administrators, and CISOs.

## 1. Graphify (Codebase Navigation)
This project has a knowledge graph at `graphify-out/` with god nodes, community structure, and cross-file relationships.
- **MANDATORY:** For codebase questions, first run `graphify query "<question>"` when `graphify-out/graph.json` exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than raw grep output. Do this before reading raw files.
- If `graphify-out/wiki/index.md` exists, use it for broad navigation instead of raw source browsing.
- Read `graphify-out/GRAPH_REPORT.md` only for broad architecture review.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## 2. Prompt Master & Workflow
Before writing or editing any documentation, follow this execution sequence:
1. **Prompt Master:** If the task is vague or lacks boundaries, invoke the `prompt-master` skill to generate a structured, load-bearing execution prompt with strict file scopes and stop conditions.
2. **Graphify:** Use the commands above to locate exact files. Never grep blindly.
3. **Execution:** Pass the shaped prompt and exact file paths to `doc-writer`.

## 3. Model Routing
`opusplan` is deprecated. Use the following explicit split:
| Layer | Model | Responsibility |
|---|---|---|
| **Main Session** | **Opus** | Planning, IA decisions, resolving contradictions, running Prompt Master. |
| **doc-writer** | **Sonnet** | Executing plans, drafting content, and running UI verification. |
| **doc-validator / researcher** | **Haiku** | Mechanical checks, link validation, and grep checks. |

## 4. Operating Principles & Branching
- **Content-first. Infrastructure-never.** Never touch `package.json`, `.github/`, or root scripts.
- **3-Tier Branching:**
  1. `main` — Merge destination only. Never commit directly.
  2. `docs/config-tab-content` (Integration) — Aggregates finished work; PR target.
  3. `docs/<task>` (Worktree) — Where changes happen. Merged up and deleted when done.
- **Filesystem Warning (`core.ignorecase=true`):** Never delete apparent duplicate casing directories (e.g., `Troubleshooting` vs `troubleshooting`). On macOS, this deletes tracked content. Use `git checkout HEAD -- <path>` to restore.

## 5. Style Authority & Verification
- **Style Standard:** Strictly follow `.claude/skills/docs-house-style/SKILL.md` (Style A). It supersedes all legacy `writing_standards.md` rules.
- **Live UI Verification:** Console claims must be live-verified against `http://safesquid.cfg` via the `safesquid_admin` MCP browser plugin (`ToolSearch`). Do not use the deprecated `safesquid-sysadmin` agent. If inaccessible, flag with `{/* NEEDS-SME-REVIEW: ... */}` and a reader-facing `**Missing:**` block.
- **Build Gate:** `npm run validate` must exit 0 before drafting a PR. (Note: Always run `mint` commands from within `public/`, never the repo root).