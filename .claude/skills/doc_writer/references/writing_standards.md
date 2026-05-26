# SafeSquid Writing Standards

## CISO-grade bar

Every document must satisfy all five criteria — weave into body copy, no separate CISO callouts:

1. **Risk-and-control** — tie each feature to a specific risk and to the SafeSquid control that addresses it.
2. **Compliance** — cite NIST, ISO 27001, PCI-DSS, HIPAA, GDPR, SOC 2 where relevant; map configurations to control frameworks (NIST SP 800-53, CIS, SOC 2) so customers can map to audits.
3. **Evidence** — state what is logged, reportable, and auditable; include export paths, report names, and log snippets; document retention and log lifecycle (generate, store, access) for incident investigation.
4. **Business impact** — problem and benefits must name reputation, legal, operational, and cost impact.
5. **No fluff** — facts, assumptions, limitations, trade-offs only; state scope, trust boundaries, and topology explicitly.

## Writing principles

1. **Threat-first** — lead with risks and problem statements, not feature lists.
2. **Outcome-focused** — show what users accomplish and the business/security result.
3. **Active & direct** — active voice, present tense, imperatives for procedures.
4. **Concrete & named** — real threats, apps, scenarios (ransomware, TeamViewer, data exfiltration); no vague abstractions.
5. **Opinionated** — warn against bad practices; recommend best paths; state limitations and trade-offs.

## Document design

### Six content blocks (how-to and admin docs)

Use bottom-line headings, not block names. Order:

1. **Problem Statement** — security challenge; risk and business impact; real-world scenarios.
2. **Key Benefits** — desired outcome; control objectives and compliance; factual competitive advantage.
3. **Prerequisites** — client-side prep; SafeSquid-side setup; system requirements; certs, IAM, trust boundaries.
4. **Implementation Actions** — one action per step; exact UI paths and field names; safe defaults and decision points; verification per step.
5. **Verification and Evidence** — interface checks; log analysis; auditor-ready evidence (report names, export paths, log snippets).
6. **Troubleshooting** — symptom → cause → resolution → verification; escalation criteria.

Merging blocks, using different headings, or omitting Verification/Troubleshooting is acceptable when the document type makes a different structure clearer.

### Next steps

Every section hub (`main.md`), how-to, and get_started must end with "Next steps" (or equivalent) + 1–3 related docs.

### get_started structure

Goal → Prerequisites → minimal Day-1 steps → Verification → Next steps. Prefer general path; defer advanced variants.

### main.md

Every `public/<section>/` folder must have `main.md` as the navigation hub.

Contents: (1) section overview (one paragraph); (2) **Quickstart path** — sequential steps with links to main child docs and a brief PBAC summary per step.

## Voice, structure, and formatting

- **Voice:** Active; imperative for procedures ("Click **Save**"). "You" permitted in explanatory prose. No hedging ("may," "might") or marketing fluff. Sentences ≤20 words; 8–12 preferred.
- **PBAC:** Problem-first; benefit and risk mandatory; advantage factual and comparative; call-to-action procedural and testable.
- **Headings:** 3–7 words; state conclusion not topic; action-oriented; no "Overview" or "Introduction." Lists: parallel structure; lead with action verbs. Lead paragraphs and list items with the main concept.
- **Clarity:** Acronyms on first use; name exact target for "configure/set/update"; descriptive link text (no "click here"); relative paths. Concrete examples and numbers ("Block downloads >100 MB during business hours").
- **Formatting:** Lead with threat or outcome (never "This section describes…"); tables for comparisons; Mermaid for workflows; paragraphs ≤5 lines.
- **Evidence:** Images in `public/images/` → `/images/category/name.webp` with alt text. Mermaid preferred for diagrams. Language tags and expected output on code blocks.

## Format conventions

- **User-entered text vs system output:** **Bold** for what the user types or selects (e.g. **your-domain.com**, **Save**). `code` for system output, command names, file paths, and config (e.g. `Connection refused`, `/etc/safesquid/config`). Do not bold output or use code for user input.
- **Menu paths:** **Menu → Submenu → Item** project-wide (e.g. **Configuration → SSL Inspection**). Bold every clickable element.
- **UI elements:** **Bold** for buttons, tabs, and field labels; `code` for values, paths, and commands.

## Icons and visual conventions

- **✅** success / recommended / "use when" — **❌** failure / not recommended / "don't use when" — **⚠️** warning / caution / "requires care"
- Use in lists, decision tables, Before/After comparisons. Do not mix with other symbols for the same meaning in the same doc.
- Callout boxes carry their own visual weight; at most one of each type per section.

## Content patterns

- **Threat narrative:** Open feature pages with a vivid scenario (who, data at risk, consequence, why current approaches fail); 2–4 short paragraphs; name real threats.
- **Before/After table:** `| Scenario | Without [Feature] | With [Feature] |` with ❌/✅.
- **When to use / When not:** ✅ Use when… / ❌ Don't use when… with requirements and anti-patterns.
- **Common Pitfalls:** On config-heavy pages: **⚠️ Common Pitfalls** — **[Mistake]:** [What breaks] → [Fix or link].
- **Decision tables:** Requirements as rows, options as columns (✅/❌/⚠️); one-line **Recommendation**.
- **Workflow:** Mermaid for multi-step flows; clear node labels and decisions.
- **Deployment scenarios:** Brief recommendations per scenario (small office, branch, HA, cloud) — when to use it, key constraints, pointer to task doc.
- **Runbooks:** Step-by-step with verification and expected results per step. Prerequisites in a dedicated section — not inside callouts.

## Admonitions and callouts

- Use ≤1 of each type per section. Never put critical instructions inside callouts — those belong in the main flow.
- Labels: **Note** (extra context); **Tip** (optional shortcut — skippable without failure); **Important** (could cause rework if missed); **Warning** (irreversible or security risk); **Caution** (unintended side effects).
- Keep callouts short. Long notes → own section with a heading. Consolidate related points into one block rather than scattering multiple callouts.

## Avoiding ambiguity

1. **UI location:** Give breadcrumb context: "In the SafeSquid interface header → click **Configure**."
2. **Cross-references:** Add a short purpose to links: "Use [Configuration Portal](/docs/.../Configuration_Portal/) for policy and system settings."
3. **Implicit assumptions:** State prerequisites before steps: "Ensure you have root access. Run `/path/to/setup.sh`."
4. **Undefined terminology:** Define on first use or link to glossary: "**LACP bonding** (Link Aggregation Control Protocol — combines multiple interfaces for bandwidth and redundancy)."
5. **Troubleshooting symptoms:** Name failure indicators: "If you see `Bad archive mirror` or `Failed to retrieve pre-configuration`, check DNS and gateway settings."
6. **Screenshot-dependent steps:** Describe the element in text: "Click the **Generate** button (green, in the Certificate Management section) as shown below."

Flag for follow-up: missing screenshots, version-specific UI notes, missing default ports or full file paths.

## Security content rules

- No real credentials, API keys, or passwords in examples. Use placeholders: `your-secret-key`, `your-domain.com`.
- Warn on risky settings; provide rollback guidance.
- No real user data; anonymized examples only.
- Validate external links and third-party references.
