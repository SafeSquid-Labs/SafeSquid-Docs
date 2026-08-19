# SafeSquid documentation manifest

Master index for man pages (`ui_root/man/`) and HTML guides (`ui_root/docs/`).

**Status legend:** `planned` | `draft` | `review` | `done`

**Conventions**

- **UI title** — label from `sectionMaster.xml` `<comment>` (what administrators see).
- **Man page** — installed to `/usr/share/man/manN/` by the `.deb` build; source troff lives under `ui_root/man/manN/`.
- **HTML** — same topic as `ui_root/docs/<name>.html`, linked from the Web UI.
- **Authoring** — write full prose here first; later trim `sectionMaster.xml` `<desc>` to short inline help only.
- **New-user tone** — lead with outcomes and UI labels; include worked examples and “how to verify”; keep man pages tighter than HTML.

---

## 1. Core (start here)

| Man page | HTML | UI / title | Purpose | Status |
|----------|------|------------|---------|--------|
| — | [first-configuration.html](first-configuration.html) | First configuration | New-admin path: service → listen → Access → test → Profiles → logs | draft |
| [safesquid(8)](../man/man8/safesquid.8) | [daemon.html](daemon.html) | SafeSquid daemon | Start/stop, CLI flags, paths, service, files | draft |
| [safesquid(7)](../man/man7/safesquid.7) | [architecture.html](architecture.html) | Architecture | Request pipeline, profiles, policy flow overview | draft |
| [safesquid-sections(7)](../man/man7/safesquid-sections.7) | [index.html](index.html) | Documentation index | This tree; links to all section and topic pages | draft |

---

## 2. Cross-cutting topics

| Man page | HTML | Purpose | Must cover | SEE ALSO | Status |
|----------|------|---------|------------|----------|--------|
| safesquid-logging(7) | logging.html | Logs and diagnosis | Log families, levels, native/extended/config logs, `putlog` phrases, correlating with policies | safesquid(7), safesquid-tools(1) | draft |
| safesquid-auth(7) | auth.html | Authentication | Kerberos / SSO, System authentication, LDAP, password cache, credential prompts | safesquid-access(5), safesquid-ldap(5) | draft |
| safesquid-feeds(7) | feeds.html | Cloud / categorisation feeds | CCS, SSqore, category updates, DNS_CAT_ZONE, offline behaviour | safesquid-category-editor(5), safesquid-startup(5) | draft |
| safesquid-integrations(7) | integrations.html | External systems | LDAP, Active Directory, Monit, ClamAV, ICAP, WCCP, BIND, rbldnsd | safesquid-* section pages | draft |
| safesquid-debug-headers(7) | debug-headers.html | Debug response headers | `dheader` / System configuration Send Debugging Headers To | safesquid-general(5), safesquid-logging(7) | draft |
| safesquid-startup(5) | startup.html | startup.ini | Process tunables not in sectionMaster (listen, threads, logs, TLS, sync, DNS zone, …) | safesquid(8), safesquid-logging(7) | draft |
| safesquid-tools(1) | tools.html | Bundled utilities | Support tar, encrypt password, upload templates, Reports views, troubleshooting tools | safesquid-logging(7) | draft |

> **Access bypass:** Access restrictions **Bypass** field (skip filters for a role); Access right **Allow bypassing** (temporary Access Profiles DENY cookie).
>
> **Two config layers:** Web UI / `sectionMaster` = policy XML. `/opt/safesquid/startup.ini` = host/process tunables (document in `safesquid-startup(5)`).

---

## 3. UI groups (navigation only — no separate policy lists)

These are menu groups in the Web UI. Document in **safesquid-sections(7)** and link to child sections.

| XML tag | UI title | Child sections |
|---------|----------|----------------|
| configure | Configure | infrastructure, policymgr, profilesdef, … |
| infrastructure | Application Setup | access, network, general, ldap, sslcert, … |
| accelerator | Accelerators | cache, prefetch |
| antivirus | Real time content security | clamav, sqscan, imgfilter, dlp, icap, … |
| filter | Privacy control | cookies-filtering, header-filtering, elevated |
| policymgr | Restriction Policies | profiles, limits, filter children, … |
| profilesdef | Custom Settings | templates, timeProfiles, reqProfiles, respProfiles, signatures, … |
| reporting | Reports | dashboard, logs, stats, live views |
| utilities | Support | password, upload, support tools |

---

## 4. Configuration sections (`man5` + HTML)

One page per configurable section. Filename pattern: `safesquid-<tag>(5)` → `docs/<tag>.html`.

| Man page | HTML | XML tag | UI title | Type | Globals / subsections (summary) | Processing notes | Status |
|----------|------|---------|----------|------|--------------------------------|------------------|--------|
| safesquid-access(5) | access.html | access | Access restrictions | section | Default Access Policy, Kerberos / SSO; Allow list, Deny list | Deny default → Allow list first, then Deny; Allow default → reverse; top-down first match | draft |
| safesquid-network(5) | network.html | network | Network settings | section | Listen; Interface | Interface: first match selects source IP; Listen falls back to startup.ini | draft |
| safesquid-general(5) | general.html | general | System configuration | section | hostname, pool, …; Compression and buffering; Connection pool; Send Debugging Headers To | First matching profile entry | draft |
| safesquid-ldap(5) | ldap.html | ldap | Integrate LDAP | section | LDAP servers; LDAP Entries | Directory setup, not allow/deny list | draft |
| safesquid-cache(5) | cache.html | cache | Caching | section | Global cache options; Store; Refresh; Manage cached objects | Refresh: first match; disk Store select currently disabled in daemon | draft |
| safesquid-prefetch(5) | prefetch.html | prefetch | Prefetching | section | Prefetch; Prefetch now | First successful URL match | draft |
| safesquid-profiles(5) | profiles.html | profiles | Access Profiles | section | Default Policies; Secondary Policies | Defaults then secondary; all matches; last action wins | draft |
| safesquid-limits(5) | limits.html | limits | Speed Limits | section | Set limits | All matching limits apply | draft |
| safesquid-cookies-filtering(5) | cookies-filtering.html | cookies-filtering | Cookie filter | section | Policy; Allow; Deny | Dual-list allow/deny like access | draft |
| safesquid-header-filtering(5) | header-filtering.html | header-filtering | Header filter | section | Policy; Allow; Deny; Insert; View headers | Dual-list; Insert all matches | draft |
| safesquid-dnsbl(5) | dnsbl.html | dnsbl | DNS Blacklist | section | Global limits; DNS and IP Black Listing Policies | Top-down until block | draft |
| safesquid-keywords-filtering(5) | keywords-filtering.html | keywords-filtering | Text analyzer | section | Threshold; Filtering policies | Score sum vs threshold | draft |
| safesquid-redirect(5) | redirect.html | redirect | Redirect | section | Redirection policies | First match | draft |
| safesquid-forward(5) | forward.html | forward | Proxy chain | section | CARP; Forwarding proxies | Collect all matches, then select peer | draft |
| safesquid-rewrite(5) | rewrite.html | rewrite | Content modifier | module | Rewriting policies | All matches in order | draft |
| safesquid-external(5) | external.html | external | External applications | section | Application policies | Top-down until done | draft |
| safesquid-sslcert(5) | sslcert.html | sslcert | HTTPS Inspection | section | Inspection Policies; Setup; SSL Certs/Cache | First https_scan match | draft |
| safesquid-reqProfiles(5) | reqProfiles.html | reqProfiles | Request Types | section | Domains and Urls; Request Types | All matches add/remove tags | draft |
| safesquid-respProfiles(5) | respProfiles.html | respProfiles | Response Types | section | Response Types | All matches add/remove tags | draft |
| safesquid-timeProfiles(5) | timeProfiles.html | timeProfiles | Time Profiler | section | Time profiles | All matching time windows | draft |
| safesquid-templates(5) | templates.html | templates | Templates | section | Manage templates | First profile+name match | draft |
| safesquid-clamav(5) | clamav.html | clamav | Clam antivirus | section | Global; clamav policies | First match | draft |
| safesquid-sqscan(5) | sqscan.html | sqscan | SqScan | module | Virus scanning policies | First match | draft |
| safesquid-imgfilter(5) | imgfilter.html | imgfilter | Image analyzer | module | Filtering policies | First match | draft |
| safesquid-dlp(5) | dlp.html | dlp | DLP | module | DLP policies; OCR policies | DLP last match; OCR score | draft |
| safesquid-icap(5) | icap.html | icap | ICAP | module | ICAP | Stop on first success | draft |
| safesquid-elevated(5) | elevated.html | elevated | Elevated Privacy | module | Elevated policies | First match | draft |
| safesquid-wccp(5) | wccp.html | wccp | WCCP | module | WCCP policies | All enabled routers | draft |
| safesquid-ftp(5) | ftp.html | ftp | FTP browsing | section | Globals only | Settings, no policy list | draft |
| safesquid-category-editor(5) | category-editor.html | category_editor | Categorize Web-Sites | section | CATEGORY EDITOR | UI app | draft |
| safesquid-applicationSignatures(5) | applicationSignatures.html | applicationSignatures | Application Signatures | section | Application Signatures List; Categories | All matches | draft |
| safesquid-contentSignatures(5) | contentSignatures.html | contentSignatures | Content Signatures | section | Content lists; libmagic DB | Request-time hooks stubbed; use Response Types for live tags | draft |
| safesquid-buitins(5) | buitins.html | buitins | Suggested Profiles | section | Default Policies | UI-only cookie tag suggestions; no runtime section | draft |
| safesquid-subscription(5) | subscription.html | subscription | Subscription | section | subscription view | License info | draft |
| safesquid-ssqore(5) | ssqore.html | ssqore | SSqore | section | SSqore policies | Cloud categorisation feed | draft |

### Web UI apps (tools / reports — document under safesquid-tools(1))

| XML tag | UI title | Notes |
|---------|----------|-------|
| configure | Configure | Top-level menu group |
| reporting | Reports | Dashboard, logs, stats, live monitors |
| password | password | Encrypt password |
| upload | Upload templates | Template upload |
| utilities | Support | Support page, license refresh |
| sample | Sample module | Developer sample only — omit from user docs |

---

## 5. Build and install

| Artifact | Repository path | On appliance after `.deb` install |
|----------|-----------------|-----------------------------------|
| Man source | `ui_root/man/man{1,5,7,8}/*.N` | `/usr/share/man/manN/` (deb build copies here) |
| HTML | `ui_root/docs/*.html` | Served at `http://safesquid.cfg/docs/` (via Web UI) |
| This manifest | `ui_root/docs/MANIFEST.md` | Not served; authoring only |

**Deb requirements (future):** copy `ui_root/man/*` → `/usr/share/man/`; optional `Recommends: man-db`; `mandb` via man-db triggers.

---

## 6. Writing status

All manifest pages are **draft**. Next steps outside content:
deb install of man pages; optional review pass; later trim `sectionMaster.xml` inline help to link here.

---

## 7. Change log

| Date | Change |
|------|--------|
| 2026-08-13 | Initial manifest and page tree |
| 2026-08-13 | Pilot pages: safesquid(8), safesquid(7), safesquid-sections(7), safesquid-access(5) + HTML |
| 2026-08-13 | Topic pages: safesquid-logging(7), safesquid-auth(7) + HTML |
| 2026-08-13 | Added safesquid-debug-headers(7) (`dheader`) |
| 2026-08-13 | Access Bypass / Allow bypassing help; general + profiles pages |
| 2026-08-13 | Added safesquid-startup(5) for startup.ini |
| 2026-08-13 | Removed retired module docs from the published tree |
| 2026-08-13 | Section pages: ldap, network, cache |
| 2026-08-13 | Section pages: sslcert, forward, limits |
| 2026-08-13 | Remaining sections + feeds/integrations/tools completed |
| 2026-08-13 | New-user depth: first-configuration.html; examples on access, profiles, auth, logging, network, architecture |
| 2026-08-13 | sectionMaster Access/Network/Profiles help: hyphen IP ranges (no CIDR); Bypass vs Allow bypassing; Action clarified |
| 2026-08-14 | Full docs + man5: cookies-filtering, header-filtering, keywords-filtering, redirect, dnsbl, external, limits (code-validated examples) |
| 2026-08-14 | Profilesdef batch: reqProfiles, respProfiles, timeProfiles, templates, applicationSignatures, contentSignatures, buitins, subscription, category-editor HTML + man5 (access.html depth); reqProfiles postdata min/max ambiguity noted; wccp skipped |
| 2026-08-14 | Section pages (code-validated depth): clamav, sqscan, dlp, icap, imgfilter, rewrite, elevated, ssqore, sslcert — HTML + man5; documents DLP last-match MIME regex, SqScan BYPASS-only scan levels, sslcert Setup unused, ssqore Heuristic unused, rewrite MIME BODY-only |
| 2026-08-14 | Infrastructure batch: network, general, forward, ftp, prefetch, cache, ldap — full HTML + man5 (access.html depth, code-validated examples) |
| 2026-08-17 | Access batch: enriched access.md (ordering, two-pass LDAP, XFF, ntlm=Negotiate); access.html with SVG flowchart; config-swg.xml ~20 teaching rows; doc.css flowchart styles |
| 2026-08-17 | Batch 1: network, general, cache, ftp, ldap — md/html/man5 + config teaching rows; Listen fallback nuance documented |
| 2026-08-17 | Batch 2–3: reqProfiles, respProfiles, timeProfiles, templates, profiles — md/html/man5; fixed timeProfiles lunch row; disabled dead urlcommand row |
| 2026-08-17 | Batch 4–5: sslcert, clamav, dnsbl, keywords, limits, cookies, header, redirect, rewrite, imgfilter, external, forward, elevated, prefetch, dlp, sqscan, icap — md/html/man5; keywords porn lists removed; header private domains sanitized |
| 2026-08-17 | Batch 6–7: md for ssqore, subscription, category-editor; applicationSignatures/contentSignatures/buitins HTML + man5; topic pages enriched; config teaching rows for signatures/buitins |
| 2026-08-17 | config-swg.xml cleanup: removed fprot, kaspersky, sophie, url-filtering, svscan, sscore; network RFC5737 IPs; general row order fixed (catch-all last) |
| 2026-08-17 | architecture.html: SVG mental-model + request-pipeline flowcharts; pipeline list aligned to main.cpp; architecture.md + safesquid(7) HIGH-LEVEL FLOW updated |
| 2026-08-17 | architecture.html / architecture.md / safesquid(7): request pipeline sequenced by Web UI section titles in call order (Time Profiler → … → Proxy chain) |
| 2026-08-17 | architecture.html: queued DLP and malware scanners as distinct upload vs downloaded-body steps (DLP upload-only; Clam antivirus / SqScan both) |
