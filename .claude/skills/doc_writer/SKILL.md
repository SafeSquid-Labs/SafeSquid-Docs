---
name: doc_writer
description: >
  ALWAYS invoke this skill before creating or revising ANY SafeSquid SWG documentation page.
  Triggers: writing a new doc, editing an existing doc, drafting a guide, updating a how-to,
  creating a section, adding a main.md, revising content structure, or responding to any request
  that will produce or change documentation files under public/ or blog/. Do not skip this skill
  for "small" edits — invoke it every time.
---

# Doc Writer

**Invoke this skill before every documentation creation or revision task.**

## Read first

1. `references/writing_standards.md` — CISO-grade bar, writing principles, document design, voice, format conventions, content patterns, admonitions, ambiguity rules, security rules.
2. `references/page_templates.md` — frontmatter template, feature page structure, page type templates, good vs bad examples.
3. `references/competitive_context.md` — ICP (Indian regulated enterprises: BFSI, Government/PSU, Critical Infrastructure), competitive displacement map (Zscaler, Netskope, Cisco, Forcepoint, Palo Alto, Blue Coat, custom Squid builds), documentation style benchmarks (Squid/OpenSSL/NoVNC), Indian regulatory compliance drivers (RBI, SEBI, IRDAI, NCIIPC, CERT-In), and ICP-aware writing rules.
4. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/world_class_quality_rubric.md` — quality approval bar.
5. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/source_of_truth_policy.md` — source hierarchy.
6. `public/docs.json` — current navigation; read before adding or moving pages.
7. The target section and its `main.md` — match existing structure and tone.

## Writing goals

Every page must be:

- Single-purpose
- Threat-first or outcome-first
- Technically precise
- CISO-grade in the body copy (not in separate executive callouts)
- Safe for real enterprise deployment
- Validation-ready and troubleshooting-ready
- Review-ready with navigation updated where needed

## Content workflow

1. **Research** — if the topic needs fact-finding, use `doc_researcher` first.
2. **Select content type** — get_started, how_to, admin_guide, concepts, reference, or troubleshooting; single purpose per page.
3. **Plan headings** — bottom-line, 3–7 words; no "Overview" or "Introduction."
4. **Draft** — follow the six-block structure from `writing_standards.md`; PBAC voice; add evidence (diagrams, screenshots, logs); cross-links and next steps.
5. **Validate** — self-check against the pre-publication checklist in `doc_validator`; hand off to `doc_validator` skill for formal validation.

## Source-of-truth rules

- Use the source hierarchy from `doc_program_standards/references/source_of_truth_policy.md`.
- Prefer verified product behavior and live UI over collateral or stale docs.
- **For `admin_guide/` pages describing concrete console steps, fields, or behavior: live-UI
  verification via `safesquid_sysadmin`/the `safesquid_admin` browser plugin is required before
  drafting, not just preferred.** Do not write a UI walkthrough from assumption or general SWG
  knowledge and defer accuracy entirely to doc-validator's Gate 2 — that gate catches mismatches
  after the fact, it doesn't replace checking first. If live access is genuinely unavailable, say
  so explicitly in the handoff to doc-validator instead of drafting silently.
- **Never state that a CLI command, config file, or man page exists unless it is confirmed live,
  confirmed in an already-verified page, or confirmed by engineering.** If a CLI/file-path
  equivalent to a UI setting would be useful but is unconfirmed, don't invent a name for it — flag
  it with `{/* NEEDS-SME-REVIEW: … */}` instead of asserting it. (This is exactly how the fabricated
  `CLI man page: safesquid-*(N)` references got into `admin_guide/` — ported from a raw-HTML source
  verbatim, never checked against anything, and never caught because no rule forbade it.)
- Use `/home/administrator/safesquid-labs/knowledge/` as a major internal source; preserve its caveats and confidence levels.
- Do not turn roadmap items or unverified knowledge into current product claims.

## Placement rules

- Write docs under `public/<section>/`.
- Filenames and folder names: snake_case, no spaces.
- Update the section `main.md` when adding a new page.
- Register new pages in `public/docs.json` under the correct `navigation.tabs` group.
- Store images under `public/images/`; reference as `/images/category/name.webp`.

## Specialist skill handoffs

Use these skills when the task needs deeper treatment:

- `deployment_architect_writer` — topology, rollout, HA, or enterprise design choices
- `evidence_collector` — screenshots, logs, reports, or proof-oriented validation content
- `compliance_mapper` — standards and control mappings
- `troubleshooting_runbook_author` — operational diagnostics and incident-grade troubleshooting
- `information_architect` — page placement, overlap, or navigation
- `version_diff_analyst` — behavior differences by release

## Validation handoff

Before finishing, self-check against the pre-publication checklist in `doc_validator/SKILL.md`. For formal validation, invoke the `doc_validator` skill.
