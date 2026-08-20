# Legacy docs migration — source snapshot and instructions

This folder is a verified snapshot of all 45 pages from `https://www.safesquid.com/docs/`, captured 2026-08-19. It is the **source of truth** for migrating legacy content into the Mintlify `admin_guide` section — use these files instead of re-crawling the live site, since this snapshot has already been reviewed for accuracy and flagged for quality issues (see below).

## Files
- `01-start-here-and-operations.md` — architecture/pipeline, daemon, debug headers, startup.ini, feeds, integrations, tools, access/auth/profiles, logging
- `02-infrastructure-and-access.md` — network, general, LDAP, HTTPS Inspection, forward proxy, FTP, WCCP, subscription, SSqore
- `03-policies-filtering-performance-security.md` — limits, request/response types, time profiler, templates, signatures, cookie/header/text filters, DNSBL, redirect, rewrite, elevated privacy, external apps, cache, prefetch, ClamAV, SqScan, image analyzer, DLP, ICAP

## Known issues in the source — handle these during migration, don't just copy through

1. **Character encoding is broken on several live pages** (sslcert, forward, limits, reqProfiles, and others) — em-dashes and smart quotes render as garbage sequences (`ΓÇö`, `├óΓé¼ΓÇ¥`). This snapshot has already been cleaned; verify no corruption re-enters if you re-fetch anything.
2. **"Code quirks" sections are the most valuable content on this site and must be preserved verbatim, not summarized away.** These document fields that are stored in the config UI but silently unused at runtime (dead controls). Examples: SqScan's Malware Security Level (only BYPASS works), Limits' Action field (never read), Content Signatures (doesn't tag live traffic at all), HTTPS Inspection's Setup subsection (unused), Prefetch's Threads field (compiled out). **Losing these during rewrite would make the new docs actively misleading** — an admin could configure a field expecting it to work.
3. **This content is technically precise and source-validated** — don't run it through the Writer Agent's voice/PBAC rewriting pass. Preserve the technical mechanics as-is. PBAC framing (if wanted at all here) belongs only in a short intro paragraph per page, never inside the mechanics.

## Instructions for Claude Code

1. You are on branch `restructure/legacy-migration-and-admin-move`, with the Mintlify Admin MCP server connected and bound to this branch.
2. **First**, confirm the `admin_guide/*` → `use_cases/*` move (from the earlier task) is already complete and merged, or do it first if not — this migration writes into the vacated `admin_guide/` path.
3. For each of the three snapshot files above, create corresponding MDX pages under `admin_guide/` using Mintlify's structure conventions (frontmatter title + description, one file per page-level heading in the snapshots).
4. Preserve every "Core mechanics" and "Code quirk" block verbatim in the new pages — these are the asset. Reformat for Mintlify syntax (callouts, code blocks) but do not paraphrase the technical claims.
5. Update `docs.json` navigation to add the new `admin_guide` structure, grouped to roughly mirror the legacy taxonomy (Start here / Infrastructure and access / Policies and profiles / Filtering and privacy / Performance / Security scanners) rather than flattening everything.
6. Cross-check against the existing Mintlify corpus (`use_cases/*`, `safesquid_swg/*`) for overlapping topics (e.g. SSL Inspection, Authentication, DLP) — where both sources cover the same feature, keep the current site's conceptual/how-to content in its existing location and add the legacy source's mechanics/quirks as supplementary detail, cross-linked rather than duplicated.
7. Flag explicitly in the PR description: pages with no current-site equivalent at all (architecture/request-pipeline, debug-headers, ssqore, startup.ini tunables, CLI/man-page references) as net-new content, since these need a human sanity check before merging, not just a structural review.
8. Stop at PR creation — do not merge.
