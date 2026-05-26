---
name: safesquid_sysadmin
description: Use when you need to verify SafeSquid admin-interface menu paths, labels, tabs, buttons, or field names against the live configuration portal at http://safesquid.cfg or its documented IP fallback.
---

# SafeSquid Sysadmin

Use this skill to verify that documentation matches the live SafeSquid interface.

## Scope

Only verify UI labels and navigation in the SafeSquid configuration portal:

- Primary URL: `http://safesquid.cfg`
- IP fallback: `http://10.200.2.253`

Use `agent-browser` for navigation, screenshots, and exact label checks when needed.

## Workflow

1. Start with the ordered list of UI paths to verify.
2. Open the SafeSquid portal.
3. Try each path in order, following every menu level exactly.
4. Compare labels case-sensitively.
5. Stop if the portal redirects outside the approved host scope or requires credentials you do not have.

## Result format

Return one line per path, in the same order:

- `CONFIRMED: <path>`
- `MISMATCH: <path> — found "<actual label or structure>"`
- `NOT FOUND: <path>`
- `BLOCKED: <reason>`
- `NOT ATTEMPTED: <path>`

## Rules

- Report only what you can directly verify.
- Do not infer likely labels.
- Do not edit files.
- Do not browse unrelated hosts while verifying.
- Capture screenshots when they materially help confirm or explain a mismatch.
- If login blocks access, report the block and mark remaining paths as not attempted.
