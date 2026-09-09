---
name: doc_writer
description: Mandatory driver for drafting and revising SafeSquid documentation. Enforces PBAC structure, reads local references, coordinates UI verification, and manages validator gates.
---

# Doc Writer Execution Driver

**Invoke this skill before drafting or modifying content in `public/` or `public/blog/`.**

## 1. Context & References
Before writing, load these local references to understand the ICP and tone:
1. `Read ./references/competitive_context.md` (ICP, displacement mapping, Indian regulatory drivers).
2. `Read ./references/page_templates.md` (Template structure).
3. `Read .claude/skills/docs-house-style/SKILL.md` (Baseline markdown formatting rules).

## 2. Execution Workflow
1. **Scope:** Run `graphify query "<topic>"` to locate existing references. If the task is vague, use `prompt-master` first.
2. **Live Verification:** For console paths, verify via `safesquid_admin` MCP at `http://safesquid.cfg`. Tag unverifiable items with `{/* NEEDS-SME-REVIEW: ... */}` and `**Missing:**`. 
3. **Drafting (PBAC Standard):** Write the page following the strict PBAC structure (see below).
4. **Validation Handoff:** Submit draft to `doc-validator`.

## 3. The PBAC Writing Framework
Every page MUST follow this exact structural flow:
- **P - Problem definition:** Lead immediately with the security challenge, threat, or operational risk. 
- **B - Benefit:** Explain the exact outcome, compliance win, or operational advantage achieved after using the SafeSquid solution.
- **A - Act on it:** Provide the concrete procedure. Use active imperative voice. Wrap technical depth in `<Accordion>`. Put `Expected result:` after runnable commands.
- **C - Call to action:** Conclude with testing/verification steps, troubleshooting tables, and exactly 3 glossed links under `## Next steps`.