# SafeSquid Page Templates (PBAC Framework)

Every feature, how-to, and deployment page in the SafeSquid documentation must strictly adhere to the PBAC (Problem, Benefit, Act, Call to Action) framework.

## Default PBAC Page Anatomy

### 1. P - Problem Definition
- **Execution:** The opening 1-2 paragraphs. 
- **Content:** State the real security or operational problem. Name the threat vectors (ransomware, MITM, data exfiltration) and the business impact (downtime, compliance failure).
- **Rule:** Never use the heading `## Problem Statement`. Just write the prose.

### 2. B - Benefit
- **Execution:** The 3rd paragraph or a comparative markdown table immediately following the problem.
- **Content:** State the exact outcome, compliance win (NIST, ISO, PCI-DSS), or operational advantage achieved after using the SafeSquid solution. 

### 3. A - Act on it
- **Execution:** The core procedure of the page.
- **Content:** Ordered, imperative steps. 
- **Rules:**
  - One action per step.
  - Explain *why* each step matters.
  - Every runnable command must be followed by `Expected result:`.
  - Wrap advanced depth, OS variations, or legacy reference tables inside `<Accordion>` tags to keep the main flow clean.

### 4. C - Call to Action
- **Execution:** The final sections of the page.
- **Content:** Must include testing/verification, troubleshooting, and next steps.
- **Rules:**
  - Use `## Verify [Feature]` to show how to prove the setup works (log snippets, UI state).
  - Use `## Troubleshoot [Feature]` with a markdown table (`| Symptom | Likely cause | Fix |`).
  - End the page with `## Next steps` containing exactly 3 glossed bullet links.

## Quality Benchmarks
- **Consequence-first:** Lead with what breaks if this isn't configured, then what the page gives you.
- **Tone:** Factual, confident, free of hype. No "we" or "our".
- **Visuals:** Use Mermaid diagrams or annotated screenshots (`safesquid_admin` MCP) only when text is insufficient.