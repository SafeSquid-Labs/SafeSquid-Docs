---
name: doc_researcher
description: Use when researching SafeSquid SWG documentation topics and you need structured notes covering threats, business risk, compliance mappings, SafeSquid-specific controls, gaps, contradictions, and source URLs before drafting documentation.
---

# Doc Researcher

Use this skill when a documentation task needs fact-finding before writing.

## Goal

Produce a structured research note that a writer can turn into SafeSquid documentation without guessing.

## Read first

1. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/source_of_truth_policy.md`
2. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/knowledge_integration_rules.md`

## Inputs

Start with:

- The topic
- A numbered list of specific questions

If the request has only a topic and no concrete questions, pause and ask for the missing questions or derive a short, explicit question list before researching.

## Research workflow

1. Search verified SafeSquid sources first: this repo, `/home/administrator/safesquid-labs/knowledge/` when available, and official release notes or product docs.
2. Prefer direct product truth, official docs, release-aligned content, and bounded internal knowledge over marketing summaries.
3. Gather threat and risk context from credible primary or authoritative sources.
4. Collect at least one relevant standards reference (NIST, ISO 27001, PCI-DSS, HIPAA, GDPR, SOC 2) when it materially applies.
5. Gather competitor context when it is factual and sourceable — do not use marketing language.
6. Prefer sourceable facts over broad claims.
7. Separate confirmed SafeSquid specifics from unknowns, roadmap items, and contradictions.

Produce a short research note using the output format below — for agent use only, not published in the doc.

## Output format

Return every research result in this structure:

**Problem** — The security challenge or threat. Name concrete risks such as ransomware, data exfiltration, command-and-control traffic, or TLS inspection gaps.

**Risk** — Operational, legal, financial, and reputational impact. Quantify where the source material supports it.

**Standards** — Applicable standards and control IDs, such as NIST SP 800-53, ISO 27001, PCI DSS, HIPAA, GDPR, or SOC 2.

**SafeSquid angle** — How SafeSquid addresses the problem. Include feature names, UI paths, logs, reports, or settings only when you can source them.

**Differentiators** — Factual differences from generic alternatives. Do not use marketing language. If this cannot be supported, say so.

**Gaps** — Unverified or missing information, listed as bullets.

**Contradictions** — Conflicting claims across sources, if any.

**Sources** — One URL per line for every source used.

## Rules

- Never invent SafeSquid feature names, UI paths, log fields, or report names.
- Do not let lower-authority product collateral override verified behavior or higher-authority internal knowledge.
- Put unconfirmed product details in **Gaps**.
- Mark roadmap items explicitly as roadmap.
- Keep each response scoped to the current questions.
- Do not draft the final documentation page unless the user explicitly asks for that too.
