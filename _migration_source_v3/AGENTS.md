# Documentation Agent Guide

**RULE: No files or folders should have space in their name. Always use underscores (_). Example: getting_started, not Getting Started or getting started.**

This guide defines how AI agents create and maintain CISO-grade, enterprise documentation for SafeSquid SWG. Content serves security and network technicians, system administrators, and operations teams as well as CISOs and security leadership.

## Operating Principles

**Content-first. Infrastructure-never.**

**CRITICAL**: This agent exists only for documentation and content creation.

**Contribution:** Documentation changes are submitted via pull request (e.g. GitHub PR). All edits require review before merge. Follow this guide and the pre-publication checklist; link to the repo or contributing guide when directing contributors.

## Agent Scope and Limitations

The agent should:

✅ **DO:**
- Create and edit documents in the `docs/` folder
- Create and edit blog posts in the `blog/` folder
- Research and write technically precise content
- Follow documentation guidelines and standards
- Update existing documentation files
- Add diagrams, screenshots, and log evidence

❌ **DO NOT:**
- Build or modify the Docusaurus project infrastructure
- Change configuration files (docusaurus.config.ts, package.json, etc.)
- Modify build scripts or deployment processes
- Alter the project structure outside of content folders
- Install dependencies or run build commands

## Naming and Path Rules

- No spaces in file or folder names.
- Use **snake_case** for folders and doc names: `getting_started`, `ssl_inspection`, `audit_and_forensics`.
- Use predictable asset names: `feature-short_description.webp`.

## Project Overview

### About and Audience

SafeSquid SWG documentation (Docusaurus 3.7.0) is a technically precise knowledge base for enterprise zero-trust web security. **Audience:** CISOs and security leadership; security and network technicians; system administrators; security architects; compliance and risk teams; operations. Docs serve both "get it done" (task-based) and "justify/audit" (control mapping, evidence, compliance) needs. Start each doc with a clear purpose and outcome so readers can decide quickly if it applies.

**CISO-grade bar (every document):** Write so CISOs can justify controls, support audits, brief the board, and compare solutions. **Criteria:** (1) **Risk-and-control** — tie features to a risk and to the control SafeSquid provides. (2) **Compliance** — where relevant, cite NIST, ISO 27001, PCI-DSS, HIPAA, GDPR, SOC 2 and state what can be shown (logs, reports, config); link configurations and features to control frameworks (e.g. NIST SP 800-53, CIS, SOC 2) so customers can map to audits. (3) **Evidence** — state what is logged, reportable, auditable and how to prove control effectiveness; call out export paths, report names, and log snippets that support audits; where relevant, document retention and log lifecycle (generate, store, access) for incident investigation. (4) **Business impact** — problem and benefits must include impact (reputation, legal, operational, cost). (5) **No fluff** — no marketing superlatives; state facts, assumptions, limitations, trade-offs; every security claim verifiable. Where security reviewers need to assess applicability, state scope, assumptions, and trust boundaries (e.g. topology, on-path vs off-path) explicitly. **Weave this content into the body copy; do not use separate CISO takeaway callouts.**

### Project Structure
- **Content:** `docs/[section-number]-[section-name]/`; `blog/` (date-prefixed); images in `/static/img/` as `/img/category/image-name.webp` (WebP preferred).
- **Infrastructure:** Node ≥18, npm, Docusaurus build; hosting Apache/Nginx; Algolia search; GA analytics. Agent does not modify config, build, or infra.

## Information Architecture

Maintain explicit document types and keep each page single-purpose.

### Content Types

- **get_started** (onboarding): Fastest path to first working deployment.
- **how_to** (task): One task end-to-end with verification.
- **admin_guide** (operational): Day-2 operations, lifecycle, troubleshooting.
- **concepts** (explain): Definitions, models, evaluation order, data flows.
- **reference** (exhaustive): Fields, parameters, defaults, limits, CLI/API.
- **troubleshooting** (symptom-first): Diagnosis → root cause → fix → verify.
- **release_notes** (product changes): Version/date, summary; new features, improvements, fixes. Place in a dedicated release-notes section or CHANGELOG; link from relevant how-to or reference docs so readers can see what changed.

## Writing Guidelines

### Principles (style)

1. **Threat-first** — Lead with risks and problem statements, not feature lists.
2. **Outcome-focused** — Show what users accomplish and the business/security result.
3. **Active & direct** — Active voice, present tense, imperatives for procedures.
4. **Concrete & named** — Real threats, apps, scenarios (e.g. ransomware, TeamViewer); no vague abstractions.
5. **Opinionated** — Warn against bad practices; recommend best paths; state limitations and trade-offs.

All docs must also meet the **CISO-grade bar** (see About and Audience): risk-and-control, compliance where relevant, evidence/audit trail, business impact, no fluff.

### Document design

**Frontmatter:** Every doc: `title`, `description`, `keywords`; optional `sidebar_position` when required.

**Six content blocks (how-to and admin docs)** — in order; use bottom-line headings, not block names as headings:

1. **Problem Statement** — Security challenge; risk and business impact (per CISO bar); real-world scenarios; business context.
2. **Key Benefits** — Desired outcome; control objectives and compliance (per CISO bar); value proposition; competitive advantage (factual).
3. **Prerequisites** — Client-side prep; SafeSquid-side setup; system requirements; call out certs, IAM, etc.
4. **Implementation Actions** — One action per step; exact UI paths and field names; safe defaults and decision points; verification per step; congruence with problem.
5. **Verification and Evidence** — Interface checks; log analysis; performance; auditor-ready evidence (report names, export paths, log snippets).
6. **Troubleshooting** — Symptom → cause → resolution → verification; escalation criteria.

Using different headings, merging blocks, or omitting Verification and Evidence or Troubleshooting is acceptable when the document type or audience makes a different structure clearer.

**Next steps:** Every Section hub (main.md), how-to and get_started must end with "Next steps" (or equivalent) + 1–3 related docs.

**Get_started:** Goal, Prerequisites, minimal Day-1 steps, Verification, Next steps. Prefer general path; defer advanced variants.

**Structure (SaaS and security-product alignment):** Organize by task and user journey (onboarding → first value → advanced) as well as by product area. Use progressive disclosure—basic flows prominent; advanced or edge-case content in linked docs or expandable sections. Where applicable, provide validated deployment guides for common scenarios (branch, HA, cloud) to set expectations and reduce risk.

### Voice, structure, and formatting

- **Voice:** Active voice; imperative for procedures ("Click the Button"). "You" permitted in explanatory prose; avoid abstract "enterprises/organizations." Opinionated; no hedging ("may," "might") or marketing fluff. Sentences ≤20 words; 8–12 preferred.
- **PBAC:** Problem-first; benefit and risk mandatory; advantage factual and comparative; call-to-action procedural and testable. Narrative flow; cover all cases.
- **Headings:** 3–7 words; state conclusion not topic; action-oriented; no "Overview"/"Introduction." Lists: parallel structure; lead with action verbs. Lead paragraphs and list items with the main concept so content is skimmable.
- **Clarity:** Acronyms on first use; name exact target for "configure/set/update"; concrete nouns; descriptive link text (no "click here"); relative paths. Use concrete examples and numbers where helpful ("Block downloads >100MB during business hours"); analogies when they aid understanding. UI: **bold** or `code` for labels and menu paths (e.g. **Configuration → NGFW**).
- **Formatting:** Lead with threat or outcome (never "This section describes…"); tables for comparisons; Mermaid for workflows; paragraphs ≤5 lines. See **Format conventions** and **Icons and visual conventions** below.
- **Content principles (SaaS and security-product research):** **Skimmable** — descriptive headings, short paragraphs, lists; links that describe the target. **Exemplary** — include worked examples, sample configs, and expected outcomes; separate tutorials/examples from dense reference where it helps scanning. **ARID** — accept some repetition for clarity; prefer self-contained docs over over-DRYing (Write the Docs). **Consistent** — one style and terminology across docs; critical for control names, parameters, and log fields. **Current** — incorrect documentation is worse than missing; version docs when behavior differs by version.
- **Evidence:** Images in `/static/img/` → `/img/category/name.webp`; alt text; screenshots and logs per feature. Diagrams: Mermaid preferred; caption or alt. Logs: what to check, where, pattern, success indicator. Code: language tags, comments, expected output when relevant.

#### Format conventions

Use these consistently so readers can scan and follow procedures:

- **User-entered text vs system output:** In commands and examples, use **bold** for what the user types or selects (e.g. **your-domain.com**, **Save**). Use `code` or a code block for system output, command names, file paths, and config (e.g. `Connection refused`, `/etc/safesquid/config`, `curl -v https://example.com`). Do not use bold for output or code for user input.
- **Menu paths:** One style project-wide: **Menu → Submenu → Item** or **Menu > Item** (e.g. **Configuration → NGFW**, **File > Save**). Use **bold** for each clickable element.
- **Key actions and UI:** **Bold** for buttons, tabs, and field labels; `code` for values, paths, and commands.

#### Icons and visual conventions

Use icons and symbols consistently so meaning is clear at a glance:

- **✅** — Success, recommended, or "use when." **❌** — Failure, not recommended, or "don't use when." **⚠️** — Warning, caution, or "requires care."
- Use ✅❌⚠️ in lists, decision tables, and Before/After comparisons; avoid mixing with other symbols for the same meaning in the same doc.
- Callout boxes (Note, Tip, Warning/Caution) carry their own visual weight; use at most one of each type per section. For long content, prefer a short callout plus a dedicated section.

**Frontmatter + body template:**
```markdown
---
title: "Document Title"
description: "Brief purpose statement"
keywords: [keyword1, keyword2, keyword3]
# optional: sidebar_position
---
# Bottom-line title
## Bottom-line section heading
### Specific subheading
`inline code` and code blocks with syntax highlighting
```

### Standard feature page structure (optional full template)

For feature overviews, sections in this order: **Hero** (threat-focused headline + 2–3 sentence hook; **The problem** / **What SafeSquid does** / **Outcome**) → **Why This Matters** (threat narrative: scenario, cost, why current approaches fail) → **How [Feature] Works** (components with examples; Mermaid if helpful) → **Before/After** table (Scenario | Without [Feature] | With [Feature] | ❌/✅) → **When to Use / When NOT** (✅ Use when… / ❌ Don't use when…) → **How to Configure** (links to task docs; optional config snippet) → **⚠️ Common Pitfalls** ([Mistake]: [What breaks] → [Fix or link]) → **Related Topics** (Prerequisites, Next Steps, Troubleshooting).

Threat narrative shape: **[Scenario]** Who does what; what data is at risk; consequence. **[Cost]** Quantify if possible. **[Problem]** Why current approaches fail.

### Content patterns

- **Threat narrative:** Open feature pages with vivid scenario (who, data at risk, consequence, why current approaches fail); 2–4 short paragraphs; name real threats.
- **Before/After table:** | Scenario | Without [Feature] | With [Feature] | with ❌/✅.
- **When to use / When not:** ✅ Use when… / ❌ Don't use when… with requirements and anti-patterns.
- **Common Pitfalls:** On config-heavy pages: **⚠️ Common Pitfalls** — **[Mistake]:** [What breaks] → [Fix or link].
- **Decision tables:** Requirements as rows, options as columns (✅/❌/⚠️); one-line **Recommendation**.
- **Workflow:** Mermaid for multi-step flows; clear node labels and decisions.
- **Deployment-scenario recommendations:** In deployment, architecture, or get_started docs, add brief recommendations by scenario (e.g. small office, branch, high-availability, cloud). For each scenario: when to use it, key constraints, and a pointer to the relevant task doc or config section. Helps readers choose a path and compare options.
- **Runbooks and operational content:** Step-by-step deployment, configuration, operational procedures, rollback, and troubleshooting; include verification steps and expected results per step. Prerequisites and requirements go in a dedicated section or clearly before steps—not hidden in callouts.
- **Concrete examples:** Sample configs, CLI snippets, and (where applicable) IaC examples for repeatable deployments; specify version or compatibility when it matters. Release notes: version/date, summary; link from relevant how-tos so readers see what changed.

### Page type templates

- **Feature overview:** Hero → Why This Matters → How It Works → Before/After → When to Use / When NOT → Config overview (links) → Common Pitfalls → Related.
- **Task guide:** Action-oriented title; Prerequisites (links); time estimate if helpful; numbered steps with screenshots where helpful; Verification; link to troubleshooting; Related tasks.
- **Use case:** Clear goal as title; business context (one paragraph); requirements; configuration steps; testing; variations for different environments.

### Admonitions, code, and examples

- **Callouts:** Note (extra info/scope); Tip (recommended approach); Warning/Caution (risk before step). At most one of each per section; short; at point of relevance. Follow the research-backed rules in **Tips and recommendations** below.

#### Tips and recommendations (research-backed)

Evidence from Nielsen Norman Group, Google Developer Documentation Style Guide, GitHub Docs, and tech-writing sources:

- **Use sparingly.** Overuse dilutes impact. Prefer at most one callout per section; avoid two or more notices in a row. Readers often skip out-of-flow elements.
- **Reserve tips for supplemental content only.** Tips = helpful but not essential; if the reader skips it, they still succeed. Never put critical instructions, prerequisites, constraints, or must-follow steps inside a tip or callout—that content belongs in the main flow or a dedicated section.
- **Use clear, conventional labels:** Note (extra context); Tip (optional shortcut or efficiency hint); Important (key details that could cause extra work if missed); Warning (irreversible harm or security risk); Caution (unintended side effects).
- **Keep callouts short and in context.** If a note is long or has many bullets, make it its own section with a heading. Place the callout next to the text it supports; assume many users will not open tips—for those who do, give clear, in-the-moment guidance.
- **Prefer one consolidated block over many scattered callouts.** When several related points apply (e.g. restart warning, permissions, pre-checks), use a single section (e.g. **Configuration considerations** or **Before you start**) with a short bullet list instead of multiple Note/Tip/Warning boxes.
- **When to use vs skip:** Use a callout for an optional shortcut (Tip), an important point that doesn't fit the flow (Note), key details that could cause extra work (Important), or irreversible/security risk (Warning). Skip callouts when the info is already in the main steps, belongs in intro/prerequisites, the note is long (use a section), or the note states the obvious.

#### Code and examples

- **Code:** Complete, working; syntax highlighting; context and expected output; test before publish.
- **Good vs bad:**
  - **Opening:** Bad = feature-focused, passive ("This section provides information about…"). Good = threat-focused, active ("Your proxy sees thousands of requests per second… Is that your CEO downloading an M&A contract? A contractor uploading customer data? Without profiling, every request is a mystery box…").
  - **Config:** Bad = passive, vague ("The certificate must be deployed… various methods depending on OS."). Good = active, specific ("Deploy the Root CA to your clients: **Windows (AD):** Group Policy → Trusted Root store → [link]; **macOS:** MDM or Keychain import → [link]; **Linux:** copy to `/usr/local/share/ca-certificates/` and run `update-ca-certificates` → [link].").
  - **Features:** Bad = abstract ("Application Signatures enable identification by application."). Good = concrete ("Block **TeamViewer** and **AnyDesk** for contractors; detect **Tor Browser** and **Psiphon**; allow **Zoom** and **Teams** but block **Discord** and **Telegram**. SafeSquid inspects SNI, headers, and patterns.").

## Research methodology

Before drafting: gather SafeSquid sources (docs, guides, release notes); at least one relevant standard or framework (NIST, ISO 27001, PCI-DSS, HIPAA, etc.); threat/risk context; competitor context (factual, non-derogatory); related SafeSquid sections. Verify technical steps and UI paths; verify regulatory refs; ensure competitor claims are sourceable. Produce a short research note (problem, risk, standards, how SafeSquid addresses it, differentiators)—for agent use only, not published in the doc.

## Content creation workflow

1. **Research** — per Research methodology.
2. **Select content type and page goal** — get_started, how_to, admin_guide, concepts, reference, or troubleshooting; single purpose.
3. **Plan headings** — bottom-line, 3–7 words (per Writing Guidelines).
4. **Draft** — problem, benefits, prerequisites, implementation (and verification/troubleshooting where appropriate; headings may differ or blocks merged/omitted); PBAC; add evidence (diagrams, screenshots, logs); cross-links and next steps.
5. **Run pre-publication checklist** — verify against Writing Guidelines, structure, technical, review.

**Placement:** Docs in `docs/[section-number]-[section-name]/`; blog in `blog/` with date prefix (YYYY-MM-DD-Title.md); images in `/static/img/`; internal links relative.

### Main file (main.md)

**CRITICAL:** Every `docs/<section>/` folder must have `main.md` as the navigation hub. Headings follow Voice, structure, and formatting.

**Contents:** (1) Section overview (one paragraph). (2) Navigation: should be **Quickstart path** — sequential steps with links to the main child docs or sub-section hubs and a brief PBAC summary description per step; sub-section folders may be linked via their `main.md` or listing nested docs.


### Avoiding ambiguity

When writing or editing docs, apply these patterns so readers are never left guessing:

1. **UI location:** Don't say only "Click Configure." Give breadcrumb context: "In the SafeSquid interface header → click **Configure**."
2. **Cross-references:** Don't use bare links. Add a short purpose: "Use [Configuration Portal](/docs/.../Configuration_Portal/) for policy and system settings." In section hub (main.md) pages, link text plus the immediately following sentence or phrase can serve as the purpose; not every link needs an inline "— purpose" when context is clear.
3. **Implicit assumptions:** State prerequisites before steps. Don't say "Run the installer"; say "Ensure you have root access. Run the installer: `/path/to/setup.sh`."
4. **Undefined terminology:** Define technical terms on first use or link to glossary. E.g. "**LACP bonding** (Link Aggregation Control Protocol — combines multiple interfaces for bandwidth and redundancy)."
5. **Troubleshooting:** Include failure symptoms, not only "if it fails, check X." E.g. "If you see 'Bad archive mirror' or 'Failed to retrieve pre-configuration', check DNS and gateway settings."
6. **Screenshot-dependent steps:** Don't say "Click the button as shown below." Describe it in text: "Click the **Generate** button (green button in the Certificate Management section) as shown below."

Flag for follow-up: missing screenshots, version-specific UI notes, missing default ports or full file paths.

## Testing Instructions

### Pre-publication checklist

Verify against the sections above; no need to duplicate every rule here.

- **Content:** Frontmatter complete; correct content type and page goal; content covers problem, benefits, prerequisites, implementation (and verification/troubleshooting where appropriate—different headings or merged/omitted blocks are acceptable); opens with threat/outcome; jargon defined; real threats/apps named; concrete examples; Common Pitfalls on config-heavy pages; Next steps at end. CISO bar met in body copy (risk and business impact, compliance where relevant, evidence/audit trail, trade-offs stated)—no separate CISO callouts. PBAC and voice/formatting per Writing Guidelines.
- **Structure:** Headings per guidelines; main.md present with section overview and quickstart path as applicable; main.md updated for new/changed docs.
- **Technical:** Markdown valid; internal links relative and working; images in `/static/img/`, paths correct; frontmatter valid YAML; code blocks with syntax highlighting. Screenshots current; code tested or scoped; procedures produce expected results.
- **Review:** Terminology and formatting consistent; format conventions followed (user-entered bold, output code, consistent menu style); icons used consistently (✅❌⚠️); cross-references correct; ready for publication and proper file placement. For release notes: version/date and summary present; linked from relevant docs where appropriate.

## Security and delivery

**Content security:** No real credentials, API keys, or passwords in examples; use placeholders (`your-secret-key`, `your-domain.com`). Mark sensitive config points; promote secure configs and hardened defaults; warn on risky settings; provide rollback guidance. No real user data; anonymized examples; validate external links and third-party refs.

**Delivery:** Create → validate against guidelines → ready for build (handled by others). Post-creation: address feedback, schedule reviews, keep content fresh; show last-reviewed/updated date where the pipeline allows.