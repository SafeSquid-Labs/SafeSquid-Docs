---
name: safesquid_sysadmin
description: Use when you need to verify SafeSquid admin-interface menu paths, labels, tabs, buttons, or field names against the live configuration portal at http://safesquid.cfg or its documented IP fallback.
---

# SafeSquid Sysadmin

Use this skill to verify that documentation matches the live SafeSquid interface.

## Scope

Only verify UI labels and navigation in the SafeSquid configuration portal:

- Page to open: `http://safesquid.cfg`
- **If that times out, the browser's proxy is probably not pointed at the SafeSquid box.**
  SafeSquid is reached *through* itself as a forward proxy, not by navigating to it as a
  destination URL — confirm the proxy address with whoever set up the session (it has changed
  before, e.g. `10.200.2.212:8080`), configure the browser tool to use that as its proxy, then
  navigate to `http://safesquid.cfg` as normal. Navigating directly to the proxy's own IP:port as
  a destination will very likely get DNS-Blacklist-blocked by SafeSquid's own policy (a "454
  Malicious Server" self-block) — don't do that, and don't try to click through its "Get Access"
  self-service link either, since that call depends on the same HTTPS cert that's usually the
  actual blocker (see below).
- The admin HTTPS endpoint's TLS cert is commonly self-signed/untrusted in this environment —
  expect `ERR_CERT_AUTHORITY_INVALID` on `https://safesquid.cfg` and stick to `http://` where the
  task allows it.
- Old IP fallback on record, may be stale: `http://10.200.2.253`.

Use `agent-browser` (or the `safesquid_admin` MCP plugin directly if `agent-browser` is
unavailable — it has been broken across sessions before) for navigation, screenshots, and exact
label checks when needed.

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
- Capture screenshots when they materially help confirm or explain a mismatch. When a screenshot
  is meant for the doc itself (not just internal proof of a mismatch), capture the **full page**,
  not a tight crop, then hand it off to be annotated per `docs-house-style/SKILL.md`'s admin_guide
  screenshot convention (arrow/circle plus a short "Click **X**" callout) — don't publish a bare,
  unannotated capture into a doc.
- If login blocks access, report the block and mark remaining paths as not attempted.
