---
name: doc_validator
description: Use when validating SafeSquid SWG documentation for repo standards, navigation integrity, evidence quality, UI-path accuracy, and Mintlify readiness.
---

# Doc Validator

Use this skill after a SafeSquid documentation page is drafted or revised. Focus on problems first.

## Validation Gates
Run these gates in order and report all findings:

### Gate 1: Pre-publication Checklist
- **Style Compliance:** Check against `.claude/skills/docs-house-style/SKILL.md`. (No ✅❌⚠️ emojis, no "Overview" headers, no PBAC header blocks).
- **Frontmatter:** `title`, `description`, `keywords` present.
- **Content:** CISO-grade body content (risk, controls, compliance citations, log snippets). No marketing fluff.
- **Paths & Links:** Internal links relative. Images in `public/images/`.

### Gate 2: UI-Path Verification
- Extract all UI paths and button labels.
- Ensure they are verified via the `safesquid_admin` MCP browser tool at `http://safesquid.cfg`. 
- Flag invented CLI/man-page references or unverified console paths with `{/* NEEDS-SME-REVIEW: ... */}` and `**Missing:**`.

### Gate 3: Repo Validation Readiness
- Execute `npm run validate` from the repository root. Note any build failures.

## Reporting Format
Report severity and impact first, followed by exact file references and the specific fix needed.