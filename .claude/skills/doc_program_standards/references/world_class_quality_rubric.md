# SafeSquid World-Class Documentation Quality Rubric

SafeSquid documentation is world-class only when an enterprise administrator, security engineer, architect, or operations team can use the page alone to understand the problem, deploy the control correctly, validate the outcome, troubleshoot failures, and operate the deployment safely in production.

Judge every page against these dimensions.

## 1. Problem framing and security relevance

- The page explains the real security or operational problem.
- The page states why the problem matters in enterprise terms.
- The page states where the control applies and when to use it.
- The page names the deployment objective precisely.

Fail the page if it reads like a feature tour or UI walkthrough without a clear problem and objective.

## 2. Technical accuracy and precision

- Every statement is technically exact and bounded.
- Product claims are verifiable and scoped.
- Preconditions, exclusions, and trust boundaries are stated.
- Language avoids vague verbs and undefined outcomes.

Fail the page if a reader could misconfigure production because the wording is imprecise.

## 3. Completeness of deployment guidance

- The page covers prerequisites, assumptions, dependencies, and client-side preparation.
- The page covers SafeSquid-side setup and relevant integrations.
- The page covers realistic deployment variations, not only the happy path.
- The page covers architecture implications when they affect behavior.

Fail the page if it omits conditions that a real enterprise deployment depends on.

## 4. Actionability of steps

- Steps are ordered, explicit, and executable.
- Each step says what to do and why it matters.
- UI paths, field names, values, and decision points are precise.
- Steps avoid guesswork and do not rely on implied knowledge.

Fail the page if a capable operator would still need support to interpret the instructions.

## 5. Verification and validation

- The page shows how to prove the setup works.
- The page includes expected results, logs, policy outcomes, and visible indicators.
- The page includes positive and negative tests where relevant.
- The page explains false-confidence risks and what success does not prove.

Fail the page if it only says "verify" without a concrete method.

## 6. Troubleshooting depth

- The page anticipates common failure modes.
- The page links symptoms to likely causes.
- The page explains fault isolation, remediation, and retest steps.
- The page tells the reader what evidence to inspect.

Fail the page if troubleshooting is generic, shallow, or missing.

## 7. Production readiness and operational safety

- The page supports pilot rollout, sequencing, and blast-radius control.
- The page highlights operational impacts, rollback thinking, and monitoring needs.
- The page helps change management and governance.
- The page warns about safety-critical mistakes and irreversible actions.

Fail the page if it is usable only in a lab and unsafe for production.

## 8. Information architecture and usability

- The page is easy to scan during implementation or incident pressure.
- Headings are bottom-line and task-oriented.
- Related setup, validation, and troubleshooting information is easy to find.
- The structure reduces cognitive load.

Fail the page if operators must hunt through prose for critical details.

## 9. Visual evidence and deployment aids

- Visuals materially reduce ambiguity.
- Diagrams clarify topology, flow, trust boundaries, or decision paths.
- Screenshots confirm UI placement when text alone is insufficient.
- Log examples show what readers should expect to see.

Fail the page if visuals are decorative or missing where ambiguity remains high.

## 10. Authority and enterprise credibility

- The page sounds like it was written by people who understand enterprise security operations.
- Tone is factual, confident, and free of hype.
- Trade-offs and limitations are stated plainly.
- The content reduces support dependency by anticipating friction.

Fail the page if it sounds promotional, shallow, or naive about enterprise deployment reality.

## Required structure for most feature and deployment pages

Use this default unless another structure is clearer for the page type:

1. Problem Statement
2. Client Scenario
3. Key Benefits
4. Prerequisites
5. Setup Instructions
6. Verification and Validation
7. Troubleshooting Guide
8. Related Controls / Next Steps

Within **Prerequisites**, cover both:

- Client-side preparations
- SafeSquid-side setup

## Writing standard

- Technical precision
- Concise but complete
- Narrative and problem-first
- Active voice
- No fluff
- No vague claims
- No repetition
- Explain why each step is taken
- Account for realistic deployment cases
- Enterprise-grade tone
- Bottom-line headings
- Use visuals where they reduce ambiguity
- Do not narrate obvious screenshots
- Always show how to test
- Always show how to troubleshoot

## Approval benchmark

A serious enterprise should be able to use the page alone to:

- understand the problem
- configure SafeSquid correctly
- validate the control path
- detect mistakes
- recover from common failures
- operate the deployment safely in production

If the page cannot do that, it is not world-class.
