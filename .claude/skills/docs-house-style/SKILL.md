---
name: docs-house-style
description: >
  READ THIS FIRST before creating or modifying ANY content under public/ or blog/.
  Defines the current SafeSquid docs house style: voice, page structure, Mintlify
  component rules, source-provenance comments, NEEDS-SME-REVIEW flags, and docs.json
  navigation conventions. Triggers: writing a new page, editing an existing page,
  drafting a guide or how-to, adding a main.md, restructuring a section, updating
  navigation. Applies to "small" edits too.
---

# SafeSquid Docs House Style

This file describes **how pages in this repo are actually written today**. Where it
conflicts with `.claude/skills/doc_writer/references/writing_standards.md`, this file
wins — see [Known conflicts](#known-conflicts-flagged-not-fixed) at the end.

## Which pages are the model

The tree holds three styles. Match **Style A** — the newest hand-written work:

| Read these before writing | Why |
|---|---|
| `public/deployment/deployment_planning.md` | Richest example: accordions, sourcing, `**Missing:**`, Steps+Cards |
| `public/use_cases/scaling_and_high_availability/ha_monit_keepalived.md` | The only fully new page. Best procedural exemplar |
| `public/getting_started/client_configuration/pac_file.md` | Lean main flow + accordion depth |
| `public/deployment/main.md` | Quickstart-path hub |

**Do not** pattern-match on `public/use_cases/**` generally (Style B: `## Problem statement`
/ `## Advantages` / `## Call to action` headings, `slug:` frontmatter, screenshot dumps)
or on `public/admin_guide/**.mdx` (Style C: reference-manual voice). Those are legacy.

---

## Voice

**Consequence-first, imperative, unhedged.** Lead with what breaks, then what the page
gives you. Never "This page describes…".

> SafeSquid becomes a production control only when the proxy is sized, reachable,
> monitored, and able to preserve enforcement evidence. Poor planning causes dropped
> sessions, weak audit trails, certificate failures, and emergency routing changes
> during rollout.
> — `public/deployment/deployment_planning.md:14`

**Person.** Bare imperative with implied "you" is the default. `you` is rare (2–4 uses
per page) and reserved for reader state: "the peak concurrent connections **you** sized
for". `we` / `our` appear **zero** times in `public/`. Never introduce them.

**Explain why, right after the command.** Every procedure step closes with the reason it
matters:

> The second check matters. A process that is running but not accepting connections still
> fails users, and a PID check alone will not catch it.
> — `ha_monit_keepalived.md:124`

**Opinionated one-liners.** Short standalone sentences that state a hard truth:

- `Untested failover is not high availability.`
- `A full log volume truncates evidence silently.`
- `SafeSquid cannot enforce policy on traffic that bypasses the proxy.`

**Ownership and evidence framing** is pervasive vocabulary: *named owner*, *change record*,
*rollback owner*, *attach to the deployment record*, *keep the evidence*.

**Sentence length** ≤20 words, 8–12 preferred. Paragraphs ≤5 lines. No hedging ("may",
"might"), no marketing language.

### PBAC — where it applies

PBAC is an **internal writing framework**, not a product term: Problem → Benefit →
Advantage → Call to action. The string "PBAC" appears **zero** times in `public/` and must
never be written into a page.

- **Style B used it as literal headings** — `## Problem statement`, `## Key benefits`,
  `## Advantages`, `## Call to action`. Do not add these to new pages.
- **Style A dissolves it into prose.** The problem is the opening paragraph; the benefit is
  the second paragraph; the advantage is a comparison table; the call to action is the
  procedure itself and `## Next steps`.
- The one place a PBAC *summary* is still explicit is a hub's `## Quickstart path`, where
  each numbered step carries a one-clause consequence gloss.

### Leaner vs full-section writing

The main flow carries only what an operator must do. Depth goes in `<Accordion>`. If a
reader skipped every accordion on the page, they must still be able to complete the task.

---

## Page structure

Canonical Style A order:

1. Frontmatter
2. `{/* source: … */}` (+ `{/* NEEDS-SME-REVIEW: … */}`) if the whole page derives from one source
3. `# Imperative Title-Cased H1` — a conclusion, not the frontmatter title
4. Consequence-first lead, 2–3 short paragraphs
5. `## Use this method when` — decision gate, closing with a `Do not …` anti-pattern line
6. `## Prerequisites` or `## Validate prerequisites` — bullets, sometimes a value table
7. A comparison/decision table or a Mermaid diagram
8. Procedure sections — one imperative `##` per phase, each with a fence and `Expected result:`
9. `## Verify …` — server-side proof
10. `## Capture … evidence` — bulleted artifact list
11. `## Troubleshoot …` — `| Symptom | Likely cause | Fix |` table
12. `## File reference` (optional) — `| Path | Purpose |`
13. `## Next steps` — exactly 3 glossed links

Merging or omitting steps is fine when the page type warrants it. 5, 8, 11 and 13 are
effectively mandatory for how-to pages.

### Frontmatter

```yaml
---
title: High Availability with Monit and Keepalived
description: Build active-passive SafeSquid high availability using Keepalived for VIP failover and Monit for process supervision, with split-brain protection and tested failover.
keywords:
  - SafeSquid high availability
  - Keepalived VRRP failover
  - Monit process monitoring
  - SafeSquid active-passive cluster
  - proxy virtual IP failover
---
```

- `title`, `description`, `keywords` on every page. Nothing else.
- `description` is a one-sentence **outcome**, not a topic.
- `keywords` is a YAML block list of 4–6 lowercase search phrases.
- **Do not add** `slug:` (legacy redirect-compat only), `icon:` (only on the 16
  `core_features/*.mdx` snippet wrappers), `sidebarTitle:` or `sidebar_position:` —
  none appear in any `.md` page.

### Headings

- **H1** — Title Case, imperative, states the outcome. Exactly one per page.
  `# Survive a Proxy Node Failure` · `# Plan the Control Path First` · `# Route Browsers With PAC`
- **H2/H3** — **sentence case**, verb-first, 2–5 words, state the conclusion.
  `## Split responsibilities between two tools` · `## Verify and evidence failover`
- Never `## Overview`, `## Introduction`, or a bare noun heading.
- `###` for sub-sections only. **No `####`** in Style A.

### `main.md`

Every `public/<section>/` folder needs one. It is a hub, **not** registered in `docs.json`
(all 31 are deliberately unregistered). Two acceptable shapes:

- **Quickstart-path hub** (preferred, e.g. `public/deployment/main.md`) — H1 + lead,
  `## Quickstart path` as a numbered list where each item is `**[Link](/path)** - gloss
  naming the consequence`, then `## Next steps`.
- **Full hub** (e.g. `getting_started/install_safesquid/main.md`) — indistinguishable from a
  content page: `<Steps>` of `<Card>` choices, `## Evidence to capture`,
  `## Troubleshoot …`, `## Next steps`.

**Do not** produce the stub `## Available items` hub found in 20 `main.md` files (17 of
them under `use_cases/`) — bare links, no gloss, description duplicating the lead. That is
the low-quality pattern to replace, not copy.

### `## Next steps`

Ends every how-to, get_started and hub. Exactly 3 links, each with a lowercase gloss after
a hyphen:

```markdown
## Next steps

- [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) - scale enforcement across more than two nodes.
- [Configuration Sync](/use_cases/customisation/configuration_sync) - keep policy identical on both HA nodes.
- [Disaster Recovery](/use_cases/scaling_and_high_availability/disaster_recovery) - plan rebuild and restore beyond node failover.
```

Use `-` (hyphen), not an em dash. Both exist in the tree; hyphen is the newer majority.

---

## Mintlify components

**In use:** `<Accordion>` (62), `<Note>` (68), `<Tip>` (100), `<Warning>` (29),
`<Steps>`/`<Step>` (26), `<Tabs>`/`<Tab>` (15), `<Card>` (32), `<Frame>` (30, admin_guide only),
`<AccordionGroup>` (1).

**Never used — do not introduce:** `<CardGroup>`, `<Info>`, `<CodeGroup>`, `<Check>`,
`<Columns>`, `<Expandable>`, `<Update>`, `<Icon>`.

### `<Accordion>` — the load-bearing rule

An accordion holds **optional depth**: migrated legacy detail, platform variants, reference
tables, advanced paths. It never holds a step required to complete the task.

Inline (never in an accordion): prerequisites, the primary command sequence, verification
commands, the evidence list, the troubleshooting table.

In an accordion: site-survey checklists, endpoint reference tables, per-OS GUI paths,
advanced/optional configuration, stress-test procedures, "when settings look right but
traffic still bypasses".

Titles are **sentence-case descriptive phrases**, unique across the page:
`"Site survey checklist"` · `"Add proxy failover"` · `"Storage media and retention defaults"` ·
`"Windows: configure the WinINET store"` · `"When settings look right but traffic still bypasses"`.

Accordions may contain tables, fences, and nested `<Warning>` / `<Tip>`. Two body
indentations exist (2-space indented, or blank-line unindented) — match the surrounding file.

`<AccordionGroup>` is used once, wrapping symptom-named troubleshooting accordions in
`getting_started/quickstart.mdx`. Reserve it for that shape.

### `<Steps>` / `<Step>`

For **decision sequences and multi-page paths**, not shell commands. Shell procedures use
plain `##` headings plus fences. Every `<Step>` body follows the same triad —
**action → `Confirm …` → `If … , …`**:

```markdown
  <Step title="Prove service and listener state">
    Confirm the proxy listener, process ID, and service state from the SafeSquid server.

    Confirm the listener, process, and service checks all show SafeSquid is running.

    If any check fails, inspect service logs before routing more users.
  </Step>
```

### `<Card>`

Only inside a `<Step>`, only to route to another page. Always `title` + `icon` + `href` plus
a one-sentence "use this when" body. Icons seen: `hard-drive`, `cloud`, `terminal`,
`refresh-cw`, `route`, `server`, `network`, `clipboard-check`. Never a standalone grid.

### `<Tabs>` / `<Tab>`

Platform or role variants of the **same** step — `Windows` / `Linux` / `macOS`, or
`Master node` / `Backup node`. Always precede with a framing sentence naming what differs:

> Only `state` and `priority` differ between the two files. Everything else must match exactly.
> — `ha_monit_keepalived.md:128`

**Second use case — a live console section that is itself a "header" with no content of its
own**: when a sidebar item in the SafeSquid Configure console doesn't open a page but only
expands into child items (verified live — e.g. **Restriction Policies → Privacy control →**
Cookie filter / Header filter / Elevated Privacy, or **Application Setup → Accelerators →**
Caching / Prefetching), build **one consolidated doc page** for the parent, one `<Tab>` per
child item, named after that item exactly. Precede with a framing sentence naming the parent
section, same as the platform-variant case: `**Privacy control** groups the three sections that
shape what leaves and enters the browser.` — `restriction_policies/privacy_control.mdx`. Confirm
via live navigation that the parent truly has no page of its own before consolidating — a section
with real content of its own plus sub-items is a different shape and should not be forced into
this pattern.

### `<Warning>` / `<Note>` / `<Tip>`

- `<Warning>` — irreversible, fail-open, or silent-misconfiguration risk. Often a bold lead
  clause: ``**A trailing `DIRECT` fails open.**``
- `<Note>` — non-blocking context, gotcha, or scoping clarification.
- `<Tip>` — a genuinely optional shortcut, skippable without failure.

≤1 of each type per section. Never put a required instruction inside a callout.

---

## Sourcing and provenance

### `{/* source: … */}`

Every block of content lifted from `_migration_source_v3/` carries an MDX comment naming
its origin. Use `{/* … */}` — **not** `<!-- … -->`, which renders visibly in Mintlify MDX
and appears zero times in `public/`.

```
{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Hardware sizing */}
{/* source: _migration_source_v3/03-High Availability Monit Keepalived.md (whole page) */}
{/* source: …/03-System_Wide_Proxy.md §Linux (GUI Method) and §macOS */}
```

Grammar: `{/* source: <repo-relative path> §<Section Name> */}`, or `(whole page)`. Combine
multiple sections with `and`.

Placement: top of page when the whole page derives from one source; immediately **before**
the block that consumed the section; or indented inside an accordion to mark a mid-accordion
graft.

Content you write yourself — from live product behaviour, UI verification, or engineering
confirmation — carries **no** source comment. The comment is a migration-provenance marker,
not a citation requirement.

### `{/* NEEDS-SME-REVIEW: … */}`

An invisible flag for a human SME, always paired with a `{/* source: … */}` line directly
above it. Grammar: `{/* NEEDS-SME-REVIEW: <what is unverified>. <what to confirm and why it
matters>. */}`

```
{/* NEEDS-SME-REVIEW: connection ceilings below are undated in the source and predate the current build. Confirm before quoting to a customer. */}
{/* NEEDS-SME-REVIEW: source states testing on Ubuntu VMs with Monit 5.34.x and Keepalived 2.x only. Platform scope unverified for RHEL-family hosts and the current SafeSquid release. */}
```

**Use it when** — and only when:

- A numeric claim is inherited from an undated legacy source.
- An endpoint or hostname has no corroboration elsewhere in `public/`.
- A platform/version scope is asserted by the source but untested against the shipping release.

**Do not use it** as a general "I'm unsure" marker. If the content is verifiable from the
product, the UI, or an existing page, just write it. Three flags exist across the whole tree
— that scarcity is the point.

### `**Missing:**` — the reader-facing twin

Where `NEEDS-SME-REVIEW` warns the SME, `**Missing:**` warns the reader, in the body copy.
Shape: *what is absent* — *why it is absent* — *what to do instead / who to escalate to*.

> **Missing:** these connection ceilings are undated in the legacy source and predate the
> current build. Treat them as a starting point for a measured pilot, not as certified
> capacity — escalate to the CTO before quoting a figure to a customer.
> — `deployment_planning.md:95`

The same fact is often flagged both ways: `deployment_planning.md:78` (SME) and `:95` (reader).

### Two hard editorial rules

From `DEPLOYMENT_MIGRATION_LOG.md`, and honoured throughout Style A:

1. **Undated or unverifiable numeric values are not written**, however well sourced. Write
   the `**Missing:**` paragraph instead.
2. **Where SafeSquid documentation contradicts itself, neither variant is written.** Name
   the conflict and tell the reader how to determine the answer on their own system — see
   the PID-path example at `getting_started/install_safesquid/linux_server.md:265`.

---

## Navigation and `docs.json`

`public/docs.json` is otherwise do-not-edit; **adding a new page to `navigation` is the
sanctioned exception.**

- **Exactly two levels site-wide**: `tab → group → flat array of page-path strings`.
  Commit `4ce2f50` deliberately flattened the only nested groups. **Never** nest a group
  object inside a `pages` array, and never add a `root` key — both were removed on purpose.
- Two tabs (`Troubleshooting`, `FAQs`) use a bare `pages` list with no groups. That is fine
  for small flat sections.
- Page paths carry **no file extension**. `main.md` files are **not** registered.
- **Groups are task-based; folders are topic-based.** They do not map 1:1 — the Deployment
  tab draws 42 pages from six different folders. Place a page in the folder that matches its
  topic, and in the group that matches the reader's task.
- **The first page in a group is that group's landing page, named after the group** —
  `use_cases/ssl_inspection/ssl_inspection`, `use_cases/authentication/authentication`.
  Keep that slot filled so no page is orphaned.
- Group labels are Title Case (`Client Configuration`, `Scaling & High Availability`).
  Admin Guide's sentence-case labels are an unresolved inconsistency — follow Title Case for
  new groups.
- **Moving a page's file (renaming or relocating its path) requires a `redirects` entry;
  reassigning which tab/group lists it does not.** A page's URL comes from its file path, not
  its nav placement — confirmed 2026-09-03 splitting Architecture/Configuration/Reporting out
  of SafeSquid SWG/Admin Guide, which relisted dozens of pages under new tabs without moving a
  single file or adding a redirect.
- **A tab with a bare `pages` list (no groups) needs a dedicated landing page as its first
  entry, named after the tab/section** — same pattern as `troubleshooting/troubleshooting` and
  `faqs/faqs`. Without one, clicking the tab lands on whatever page happens to be listed first,
  which reads as broken if that page is actually a narrow sub-topic (e.g. a new `Reporting` tab
  whose first page was a Deployment-owned planning doc — confirmed as a real, reported bug
  2026-09-03, fixed by adding `reporting/reporting.md`).
- **A page must appear in exactly one tab's registration.** If it's left listed under both its
  old and new tab during a restructure, Mintlify resolves it to whichever tab comes first in
  the `tabs` array — the sidebar and tab-bar silently show the *wrong* tab as active. After
  moving any page, grep `docs.json` for its path to confirm the stale entry is gone (confirmed
  as a real, reported bug 2026-09-03: two Reporting-tab pages left registered under Deployment
  kept bouncing back to it).
- **A tab's own click-through target — its first registered page — is what a generic prose
  link named after that tab/section should point to**, not an unregistered `main.md` hub, even
  though the hub is otherwise a legitimate destination. Two links reading "Deployment" that
  resolve to different pages depending on where you click is a real, reported confusion
  (2026-09-03) — match the tab's actual behavior instead of defaulting to its hub.
- **Link text doesn't have to equal the destination's title** — shorthand aliases are the norm
  tree-wide (`Caching` → *Cache settings*, `Register` → *Register Your Key*) and not worth
  chasing. But a link text semantically far enough from the real title that a reader can't
  predict the destination (`Prerequisites` → a page titled *Deployment Checklist*) is a real
  bug, confirmed reported 2026-09-03 across 7 files. Check the destination's frontmatter title
  before choosing link text for a new cross-link.

---

## Naming, links, code, tables

- **snake_case, no spaces**, for every file and folder. Enforced by `CLAUDE.md` line 3.
- **`.md` for new hand-written content.** `.mdx` is used by `admin_guide/`, `core_features/`,
  `snippets/`, and `getting_started/welcome|quickstart`. Note `{/* … */}` comments and
  component tags work in `.md` here regardless.
- **Links** are absolute, extension-less: `/use_cases/scaling_and_high_availability/proxy_clustering`.
  Hub links include `/main`. Every link carries a purpose gloss; never "click here". Never
  the legacy `/Capitalized_Slug` form.
- **Bold vs code**: `**Bold**` for what the user clicks or types and for menu paths
  (`**Settings → Network & Internet → Proxy**`); `` `code` `` for commands, paths, config
  values, and system output (`` `Connection refused` ``, `` `/etc/safesquid/config` ``).
- **Placeholders** are SHOUTY-HYPHEN tokens, never real values: `SAFESQUID-IP`, `VIP-ADDRESS`,
  `MASTER-IP`, `INTERFACE`, plus `example.com` / `.internal.example.com`. No real credentials.
- **Images** at `/images/<category>/<name>.webp` with descriptive alt text. Mermaid preferred
  over screenshots for conceptual/process-flow content. `<Frame>` wrappers are an admin_guide
  convention only.
  - **Exception — `admin_guide/` UI walkthroughs and worked examples**: a real, annotated console
    screenshot is required, not just preferred, wherever a page currently just describes a
    click-through sequence or a worked example in prose with no visual (this doesn't replace the
    existing `*_flowchart.svg` logic diagrams, which stay — they show processing order, a
    screenshot shows the console). Capture the **full page**, not a tight crop, from the live
    console via `safesquid_sysadmin`/`safesquid_admin`. Annotate with an arrow or circle plus a
    short imperative callout naming the control (`Click **Get Access**`, not just a bare
    screenshot) — an unannotated screenshot is the same "walls of undescribed screenshots"
    anti-pattern flagged below. Save as `public/images/admin_guide/<page>-<slug>.webp`, wrapped in
    `<Frame>`, same as the existing flowcharts.
- **Never invent a CLI command, config file, or man-page name.** State one exists only if it's
  confirmed live, confirmed in an already-verified page, or confirmed by engineering — otherwise
  flag it with `{/* NEEDS-SME-REVIEW: … */}` instead of asserting it. (Every `admin_guide/` page
  used to carry a fabricated `CLI man page: safesquid-*(N)` reference ported verbatim from a
  raw-HTML source and never checked against anything; they were removed — don't reintroduce the
  pattern.)
- **Code fences always carry a language tag.** `bash` dominates, for Linux CLI with `sudo`
  shown explicitly; `powershell` for Windows; `text` — the second most common — for URLs and
  anything read rather than run; `conf`, `javascript`, `yaml`, `mermaid` as appropriate. Bare
  fences are used only for log excerpts and config-file bodies.
- **Every runnable command is followed by `Expected result:`** — around 100 occurrences
  tree-wide. Prose form, or prose plus a fenced literal. Prefix a fence with a scoping sentence — "Run on both
  nodes:" — and use inline `#` comments to name the machine or role.
- **Tables** use the compact `|---|---|---|` delimiter (not space-padded), with `|---:|` for
  numeric and port columns. Four recurring archetypes: `| Symptom | Likely cause | Fix |`,
  comparison/decision, `| Failure | What happens | Result for users |`, and `| Path | Purpose |`.
- **Mermaid**: `flowchart TB`, plain-ASCII node labels (hyphens, no parentheses or commas
  inside labels), always introduced by a sentence explaining what it shows.
- **No ✅ / ❌ / ⚠️ emoji.** They survive in only four files — three `snippets/*.mdx` and
  `safesquid_swg/what_is_safesquid_swg.md`. Zero Style A pages use them. Use a `<Warning>`
  or a plain declarative sentence instead.
- **British/American spelling is mixed** (`behavioural` alongside `analyzer`). Not normalized
  — match the surrounding page rather than introducing a global change.

---

## Anti-patterns

`public/use_cases/scaling_and_high_availability/master_slave.md` is the clearest
counter-example. Do not reproduce:

- No H1, or an H1 that just restates the frontmatter title.
- `##` used for individual procedure steps and their sub-steps inconsistently.
- Walls of consecutive undescribed screenshots with no prose between them.
- Checkbox lists (`- [ ] …`) instead of an `Expected result:` line.
- Troubleshooting as bold-headed bullet groups rather than a table.
- Ending with `**Related**: [a], [b]` instead of `## Next steps`.
- `## Available items` stub hubs.

---

## Before you write anything

1. Read this file, then `CLAUDE.md` for scope and naming.
2. Open the two exemplars closest to your page type — `deployment_planning.md` for a
   planning/reference page, `ha_monit_keepalived.md` for a procedure.
3. Open the target section's `main.md`. Match its tone; plan the entry you will add to it.
4. Open `public/docs.json`. Decide the **tab and group** (task-based) before you decide the
   folder (topic-based). Confirm two-level nesting still holds.
5. Decide the page type and lock the section order from [Page structure](#page-structure).
6. Draft the H1 as an imperative conclusion, and the lead as consequence-first. If your lead
   starts "This page describes", rewrite it.
7. As you write: language tag on every fence, `Expected result:` after every command,
   depth into `<Accordion>`, main flow inline.
8. For anything lifted from `_migration_source_v3/`, add `{/* source: … §Heading */}`. For an
   undated number, unverified endpoint, or untested platform scope, add
   `{/* NEEDS-SME-REVIEW: … */}` **and** a reader-facing `**Missing:**` paragraph — and do
   not write the number.
9. Close with `## Next steps` — exactly 3 glossed links.
10. Register the page in `docs.json`, add it to the section `main.md`, and add a `redirects`
    entry if you moved it.
11. Run `npm run validate` — it must exit `0`.

---

## Known conflicts (flagged, not fixed)

Older governance files contradict current practice. This file is authoritative; the items
below need a separate decision and edit.

| Where | Conflict |
|---|---|
| `doc_writer/references/writing_standards.md` §Icons, §Content patterns | Prescribes ✅/❌/⚠️ markers, Before/After tables, "When to use / When not" with emoji. No Style A page uses any of it; emoji survive in only four legacy files. |
| `writing_standards.md` §Document design vs `doc_program_standards/references/page_requirements.md` and `.claude/agents/doc-writer.md` | **Six-block** vs **eight-block** default page anatomy (the eight adds *Client Scenario* at 2 and *Related Controls / Next Steps* at 8). `CLAUDE.md` and `README.md` both say "six-block". Unresolved. |
| `doc_writer/SKILL.md` items 4–5, §Source-of-truth rules; plus 7 other skill/agent files | Dead absolute paths `/home/administrator/Mintlify-Docs/…` and `/home/administrator/safesquid-labs/knowledge/`. The knowledge base at source-hierarchy position 5 is unreachable on this machine. |
| `CLAUDE.md` §Repository Layout, and the same block in `README.md` | Stale — lists `getting-started/`, `guides/`, `api/`, `cli/`, `use-cases/` (hyphens), violating the repo's own snake_case rule. Actual tree is `getting_started/`, `use_cases/`, `admin_guide/`, `core_features/`, `deployment/`, `safesquid_swg/`, `snippets/`. |
| `public/docs.json` `banner.content` | Live in production config: `"TODO before merge — set release version and link. [Placeholder](/)"`. |
| No governance file | The `public/snippets/*.mdx` reuse pattern (single-source a feature blurb, import into both `core_features/` and `use_cases/`) is undocumented. Also unruled: `.md` vs `.mdx`, group-label casing, `&` vs `and`. |
