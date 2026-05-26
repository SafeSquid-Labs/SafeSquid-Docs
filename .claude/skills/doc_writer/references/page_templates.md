# SafeSquid Page Templates

## Frontmatter + body template

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

## Standard feature page structure

For feature overviews, sections in this order:

1. **Hero** — threat-focused headline + 2–3 sentence hook: **The problem** / **What SafeSquid does** / **Outcome**
2. **Why This Matters** — threat narrative: scenario, cost, why current approaches fail
3. **How [Feature] Works** — components with examples; Mermaid if helpful
4. **Before/After** table — `| Scenario | Without [Feature] | With [Feature] |` with ❌/✅
5. **When to Use / When NOT** — ✅ Use when… / ❌ Don't use when…
6. **How to Configure** — links to task docs; optional config snippet
7. **⚠️ Common Pitfalls** — **[Mistake]:** [What breaks] → [Fix or link]
8. **Related Topics** — Prerequisites, Next Steps, Troubleshooting

**Threat narrative shape:** **[Scenario]** — who does what; what data is at risk; consequence. **[Cost]** — quantify if possible. **[Problem]** — why current approaches fail.

## Page type templates

### Feature overview

Hero → Why This Matters → How It Works → Before/After → When to Use / When NOT → Config overview (links) → Common Pitfalls → Related.

### Task guide

Action-oriented title → Prerequisites (links) → numbered steps with screenshots where helpful → Verification → link to troubleshooting → Related tasks.

### Use case

Clear goal as title → business context (one paragraph) → requirements → configuration steps → testing → variations for different environments.

### get_started

Goal → Prerequisites → minimal Day-1 steps → Verification → Next steps. Prefer general path; defer advanced variants.

## Writing quality — good vs bad

### Opening prose

**Bad** (feature-focused, passive):
> "This section provides information about Application Signatures and how they work."

**Good** (threat-focused, active):
> "Your proxy sees thousands of requests per second. Is that your CEO downloading an M&A contract? A contractor uploading customer data? Without application profiling, every request is a mystery box."

### Config instructions

**Bad** (passive, vague):
> "The certificate must be deployed to clients using various methods depending on OS."

**Good** (active, specific):
> "Deploy the Root CA to your clients: **Windows (AD):** Group Policy → Trusted Root store; **macOS:** MDM or Keychain import; **Linux:** copy to `/usr/local/share/ca-certificates/` and run `update-ca-certificates`."

### Feature descriptions

**Bad** (abstract):
> "Application Signatures enable identification by application."

**Good** (concrete):
> "Block **TeamViewer** and **AnyDesk** for contractors; detect **Tor Browser** and **Psiphon**; allow **Zoom** and **Teams** but block **Discord** and **Telegram**. SafeSquid inspects SNI, headers, and behavioral patterns."

## Code blocks

- Complete and working; syntax highlighting; include context and expected output.
- Test before publishing or scope clearly ("example only — adjust paths for your environment").
