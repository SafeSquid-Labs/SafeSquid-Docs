---
name: doc_validator
description: Use when validating SafeSquid SWG documentation for repo standards, navigation integrity, evidence quality, UI-path accuracy, and Mintlify readiness before review or pull request submission.
---

# Doc Validator

Use this skill after a SafeSquid documentation page is drafted or revised.

## Goal

Decide whether the page is review-ready by checking structure, accuracy, and repo integration. Focus on problems first.

## Read first

1. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/world_class_quality_rubric.md`
2. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/source_of_truth_policy.md`
3. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/page_requirements.md`

## Validation gates

Run these gates in order and report all findings:

1. Pre-publication checklist
2. UI-path verification
3. Repo validation readiness

## Gate 1: Pre-publication checklist

### Content

- Frontmatter fields present: `title`, `description`, `keywords`
- Correct content type and single page goal
- Opens with threat or outcome (not "This section describes…")
- Problem statement, client scenario, setup, verification, and troubleshooting depth where applicable
- CISO-grade body content: risk, controls, compliance citations, evidence (export paths, report names, log snippets), business impact — no separate CISO callouts
- Jargon defined on first use or linked to glossary
- Real threats and app names used (not vague abstractions)
- Concrete examples and numbers where helpful
- Common Pitfalls section on config-heavy pages
- Next steps present on section hubs, how-to, and get_started pages
- No unsupported product claims

### Formatting

- Correct formatting: **bold** for UI labels and menu paths; `code` for values, paths, commands, and output
- Menu path style consistent project-wide (**Menu → Submenu → Item**)
- ✅❌⚠️ used consistently; not mixed with other symbols for the same meaning
- No marketing fluff, hedging ("may," "might"), or passive voice in procedures

### Structure

- Headings 3–7 words; state conclusion not topic; no "Overview" or "Introduction"
- `main.md` present and updated when a new page was added
- `public/docs.json` updated when a new page was added

### Technical

- Markdown valid; no broken syntax
- Internal links relative and working
- Images in `public/images/`; paths correct (`/images/category/name.webp`); alt text present
- Frontmatter valid YAML
- Code blocks have syntax highlighting
- Screenshots current; code tested or clearly scoped
- No real credentials, API keys, or passwords — placeholders only (`your-secret-key`, `your-domain.com`)

### For release notes

- Version and date present; summary included
- Linked from relevant how-to or reference docs

## Gate 2: UI-path verification

Extract all UI paths and button labels from the doc. When browser verification is in scope, use the `safesquid_sysadmin` skill to confirm them against the SafeSquid interface at `http://safesquid.cfg`. If UI verification cannot be performed, call that out explicitly as an open risk.

## Gate 3: Repo validation readiness

This repo's operating guide says `npm run validate` is the minimum pre-PR check, but the same guide also says agents should not run build commands unless explicitly ticketed. Respect the stricter instruction in force for the current task. If you do not run validation, report that clearly instead of implying a clean pass.

## Reporting format

When you find issues, report:

- Severity and impact first
- File references when available
- The specific fix needed
- Any residual risk or unverified area

If no findings remain, state that explicitly and note any checks you could not perform.
