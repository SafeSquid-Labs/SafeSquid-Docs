# Deployment tab — migration log

Traceability for content brought into the Mintlify **Deployment** tab from the SafeSquid-Labs Docusaurus site, a read-only copy of which is at `_migration_source_v3/`.

- **Date:** 2026-08-22
- **Branch:** `restructure/legacy-migration-and-admin-move`
- **Source:** `_migration_source_v3/` (read-only, not modified)
- **Rule applied:** additive only. No existing page, section, or paragraph was deleted or rewritten. Two nav *placements* changed; see [Navigation changes](#navigation-changes).

Every block listed below also carries an MDX comment at its head naming the same source path and heading, so the citation survives independently of this file.

Items marked `NEEDS-SME-REVIEW` carry a factual claim that could not be verified against the current release from the source alone. They are published because the source is the SafeSquid documentation site, but they need engineering sign-off before a customer acts on them.

---

## New pages

| Target page | Source | Notes |
|---|---|---|
| `public/use_cases/scaling_and_high_availability/ha_monit_keepalived.md` | `_migration_source_v3/03-High Availability Monit Keepalived.md` (repo root, not under `docs/`) | Only source page with zero prior coverage in `public/`. Rewritten in six-block structure; lab IPs replaced with placeholders. **NEEDS-SME-REVIEW** |
| `public/deployment/main.md` | none — authored | Section hub required by `CLAUDE.md`. `public/deployment/` was the only section folder without one. Deliberately unregistered in `docs.json`, matching all 34 other `main.md` files. |

### NEEDS-SME-REVIEW — `ha_monit_keepalived.md`

- Source states the procedure was tested on Ubuntu VMs with Monit 5.34.x and Keepalived 2.x only. Behaviour on RHEL-family hosts and against the current SafeSquid release is unverified.
- The `weight -101` rationale asserts that `weight -60` "may not reliably trigger the BACKUP state transition in all Keepalived versions." Directionally correct and the `-101` recommendation is safe either way, but the version-specific claim is not sourced to a Keepalived changelog.
- The health-check script probes `http://safesquid.cfg` through `127.0.0.1:8080`. Confirm this remains the right liveness target for the shipping build.

---

## Sections added to existing pages

All added as `<Accordion>` blocks inside the section they belong to. Surrounding prose is unchanged.

| Target page | Section added | Source (all under `_migration_source_v3/docs/`) |
|---|---|---|
| `public/deployment/deployment_planning.md` | `Sizing matrix by peak concurrent connections` | `01-Getting_Started/01-Deployment_Planning.md` §Hardware sizing |
| `public/deployment/deployment_planning.md` | `Outbound endpoint reference` | `01-Getting_Started/01-Deployment_Planning.md` §Firewall Whitelist Requirements |
| `public/deployment/deployment_planning.md` | Named parameter fields appended to the existing `Site survey checklist` accordion | `01-Getting_Started/01-Deployment_Planning.md` §Pre-Installation Checklist (Site Survey) |
| `public/getting_started/client_configuration/pac_file.md` | `PAC function reference` | `01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md` §Common PAC Functions Reference |
| `public/getting_started/client_configuration/pac_file.md` | `pactester` workflow appended to the existing `Debug PAC behavior` accordion | same file §Debug Your PAC File |
| `public/getting_started/client_configuration/pac_file.md` | `wpad.dat` naming and DNS A-record requirements appended to the existing `Plan WPAD carefully` accordion | same file §Advanced: WPAD (Auto-Discovery) |
| `public/getting_started/client_configuration/system_wide_proxy.md` | `Persist proxy settings on Linux` | `01-Getting_Started/05-Connect_Your_Client/03-System_Wide_Proxy.md` §Linux |
| `public/getting_started/client_configuration/system_wide_proxy.md` | `Desktop proxy settings by GUI path` | same file §Linux (GUI Method) and §macOS |

### NEEDS-SME-REVIEW — `deployment_planning.md` §Sizing matrix

The CPU / RAM / NIC to max-concurrent-connection table is undated in the source and predates the current build. The AES-NI requirement and the 3–5-connections-per-active-user estimate are stated without measurement context. Confirm the ceilings before quoting them to a customer.

### NEEDS-SME-REVIEW — `deployment_planning.md` §Outbound endpoint reference

Four categorization endpoints — `prourl.itsecure.co.in:8080`, `encurl.itsecure.co.in:8080`, `klassify.itsecure.co.in:8080`, `prourl.itonlinesecure.in:8080` — are third-party domains that appear nowhere else in `public/`. Confirm they are current for the shipping release before an operator allowlists them. The `safesquid.net` / `safesquid.com` endpoints in the same table are corroborated by `public/getting_started/activate.md`.

---

## Navigation changes

`public/docs.json`, Deployment tab. Two new groups mirror the source's `17-Proxy_Clustering` / `19-Operational_Modes` / `22-Disaster_Recovery` split, which the tab previously flattened into a single group.

**Added**

- Group **Operational Modes** — `operational_modes`, `forward_proxy`, `transparent_proxy`, `tcp_proxy`, `reverse_proxy`, `proxy_chain`.
- Group **Disaster Recovery** — `disaster_recovery`, `configure_cloud_restore`.
- Page `use_cases/scaling_and_high_availability/ha_monit_keepalived` under **Scaling & High Availability**.

**Placement moves — flagged, reversible**

These are the only edits in this pass that are not purely additive. No file moved, no URL changed, no redirect is needed; only the sidebar listing changed.

| Page | Was | Now | Rationale |
|---|---|---|---|
| `use_cases/customisation/configure_cloud_restore` | Customisation | Disaster Recovery | Source location is `22-Disaster_Recovery/01-Configure_Cloud_Restore.md` |
| `use_cases/customisation/configuration_sync` | Customisation | Scaling & High Availability | Source location is `17-Proxy_Clustering/02-Configuration_Sync.md` |

To revert either, move the entry back into the Customisation group's `pages` array. The new groups stand independently of both moves.

---

# Pass 2 — full section-by-section reconciliation (2026-08-22)

Pass 1 compared the trees at page level and by topic-marker greps, and concluded coverage was near-complete. That was too coarse. Pass 2 read all 15 files under `_migration_source_v3/docs/01-Getting_Started/` and all 20 pages on the Deployment side in full and lined them up section by section. Roughly **60 source sections had no home in `public/`**, concentrated in installation mechanics, licensing detail, and client-side verification.

Decisions taken for this pass:

- Undated or unverifiable numeric values are **not written**, however well sourced. They are recorded under *Held* below.
- Where SafeSquid documentation contradicts itself, **neither variant is written**. See *Contradictions*.
- No existing content was deleted, reworded, or restructured.

## Pass 2 — sections added

All added as `<Accordion>` or `<Warning>` blocks inside the section they belong to, each carrying an MDX `{/* source: … */}` comment. Source paths are relative to `_migration_source_v3/docs/01-Getting_Started/`.

| Target page | Section added | Source |
|---|---|---|
| `deployment/deployment_planning.md` | LACP bonding table | `01-Deployment_Planning.md` §Link aggregation (LACP) |
| `deployment/deployment_planning.md` | Storage media and retention defaults | `01-Deployment_Planning.md` §Disk and log storage |
| `deployment/deployment_planning.md` | Disaster recovery site design, RTO/RPO definitions, failover methods | `01-Deployment_Planning.md` §Disaster recovery |
| `deployment/deployment_planning.md` | Post-install baseline and stress test, failure interpretation | `01-Deployment_Planning.md` §Verify and document for audits |
| `install_safesquid/prerequisites.md` | Firewall ports to open, inbound and outbound | `01-Deployment_Planning.md` §Prepare the host, steps 6–7 |
| `install_safesquid/prerequisites.md` | SELinux and AppArmor guidance | `01-Deployment_Planning.md` §Prepare the host, step 8 |
| `install_safesquid/main.md` | Environment → method decision table | `03-Install_SafeSquid/main.md` §Which Method Should I Use? |
| `install_safesquid/safesquid_appliance_builder.md` | ISO URL, physical prep, VM prep, **default credentials warning** | `…/01-SafeSquid_Appliance_Builder.md` §Before You Begin, §Default Credentials |
| `install_safesquid/safesquid_appliance_builder.md` | GRUB target-disk warning | same file, §Installation Steps step 7 |
| `install_safesquid/safesquid_appliance_builder.md` | Install-console monitoring, ALT+F1–F4 | same file, §Monitoring Installation Progress |
| `install_safesquid/safesquid_appliance_builder.md` | What the appliance installs, path and port table | same file, §What Gets Installed |
| `install_safesquid/safesquid_appliance_builder.md` | 3 troubleshooting rows | same file, §Troubleshooting |
| `install_safesquid/linux_server.md` | Per-distro dependency lists | `…/03-Linux_Server.md` §Prerequisites |
| `install_safesquid/linux_server.md` | Directories, firewall, SELinux, time sync | same file, §System Preparation |
| `install_safesquid/linux_server.md` | TAR download, extract, `setup.sh`, `ldd` check | same file, §Installation Steps |
| `install_safesquid/linux_server.md` | Admin password UI path, logrotate stanza | same file, §Post-Install Hardening |
| `install_safesquid/linux_server.md` | 2 troubleshooting rows | same file, §Troubleshooting |
| `install_safesquid/cloud_deployment.md` | Backhauling rationale | `…/02-Cloud_Deployment.md` §Why Deploy SafeSquid in the Cloud? |
| `install_safesquid/cloud_deployment.md` | Cloud-IMG URL and per-provider import | same file, §Cloud-IMG |
| `install_safesquid/cloud_deployment.md` | cloud-init script URL, user-data locations, progress check | same file, §Cloud-Init |
| `install_safesquid/cloud_deployment.md` | `lsblk` mount verification | same file, §Verify the Deployment |
| `install_safesquid/cloud_deployment.md` | Topology, IAM identity, encryption, TLS, logging | same file, §Security Configuration |
| `install_safesquid/cloud_deployment.md` | Load-balancer health-check spec | same file, §Load Balancing |
| `install_safesquid/cloud_deployment.md` | 4 troubleshooting rows | same file, §Troubleshooting |
| `getting_started/activate.md` | Free vs Commercial tier table | `04-Activate.md` §Key Benefits |
| `getting_started/activate.md` | Activation-blocking vs ongoing endpoints, categorization engine table | same file, §Readiness Checklist |
| `getting_started/activate.md` | Licence expiry behaviour, update cadence, renewal, conservation period | same file, §Troubleshooting case4 |
| `getting_started/activate.md` | Wrong licence tier troubleshooting row | same file, §Troubleshooting case5 |
| `getting_started/register.md` | Corporate-domain rationale | `02-Register.md` §Use Your Business Email |
| `getting_started/register.md` | Key does not expire, re-download anytime | same file, §About Your Activation Key |
| `getting_started/verify_your_setup.md` | Certificate-issuer positive check | `06-Verify_Your_Setup.md` §5 HTTPS Traffic Flows |
| `getting_started/verify_your_setup.md` | Client-side checklist | same file, §Post-Installation Client Checklist |
| `getting_started/verify_your_setup.md` | Integration validation checklist, incl. EICAR | same file, §SafeSquid Integration Validation |
| `client_configuration/connect_your_client.md` | External-IP proof, scale guidance | `05-Connect_Your_Client/main.md` §Testing Your Configuration |
| `client_configuration/explicit_proxy.md` | **Firefox configuration**, Windows legacy path, bypass-syntax note | `…/01-Explicit_Proxy.md` §Configuration Steps |
| `client_configuration/explicit_proxy.md` | Per-platform "is it applied" checks, 3 troubleshooting rows | same file, §Troubleshooting |
| `client_configuration/pac_file.md` | Proxy failover chain, fail-open warning | `…/02-PAC_File.md` §Create Your PAC File |
| `client_configuration/pac_file.md` | MIME type warning, Apache and Nginx directives | same file, §Deploy the PAC File step 1 |
| `client_configuration/pac_file.md` | Pointing clients at the PAC URL, incl. `gsettings` and `kwriteconfig5` | same file, §Deploy the PAC File step 2 |
| `client_configuration/pac_file.md` | 3 troubleshooting rows | same file, §Troubleshooting |
| `client_configuration/system_wide_proxy.md` | **WinHTTP vs WinINET warning**, Settings app, Internet Options, registry values | `…/03-System_Wide_Proxy.md` §Windows |
| `client_configuration/system_wide_proxy.md` | Per-platform verification, conflicting-source checklist | same file, §Test Your Configuration |
| `client_configuration/system_wide_proxy.md` | WPAD prerequisite, 3 troubleshooting rows | same file, §Prerequisites, §Troubleshooting |
| `client_configuration/enterprise_deployment.md` | Tool decision table incl. SCCM | `…/04-Enterprise_Deployment.md` §Which Method Should I Use? |
| `client_configuration/enterprise_deployment.md` | GPO console paths, registry preference values, refresh window, verification, delete-link rollback | same file, §Windows: Group Policy |
| `client_configuration/enterprise_deployment.md` | Intune and Jamf console paths | same file, §macOS: MDM |
| `client_configuration/enterprise_deployment.md` | Complete Ansible playbook and rollback playbook | same file, §Linux: Ansible |
| `client_configuration/enterprise_deployment.md` | Complete Puppet class and template | same file, §Linux: Puppet |
| `client_configuration/enterprise_deployment.md` | Ring sizes and dwell time, PAC hosting, monitoring | same file, §Best Practices |
| `client_configuration/enterprise_deployment.md` | 5 troubleshooting rows | same file, §Troubleshooting |
| `client_configuration/application_specific_configuration.md` | Git `noProxy` and unset; npm registry and delete; pip one-time flag and Windows path | `…/05-Application_Specific_Configuration.md` §1–4 |
| `client_configuration/application_specific_configuration.md` | `~/.curlrc`, `~/.wgetrc`; Docker `daemon.json` and `docker info` | same file, §2, §7, §8 |
| `client_configuration/application_specific_configuration.md` | Outlook and Thunderbird navigation | same file, §9, §10 |
| `client_configuration/application_specific_configuration.md` | Java, Ruby, Go patterns and the unlisted-app method | same file, §Other Applications |
| `client_configuration/application_specific_configuration.md` | 3 troubleshooting rows | same file, §Troubleshooting |

## Contradictions — unresolved, NEEDS-SME-REVIEW

Neither variant was written. Both are SafeSquid-authored; picking one arbitrarily would make the docs confidently wrong half the time.

### 1. Monit PID file path

| Variant | Cited by |
|---|---|
| `/var/run/safesquid.pid` | `03-Linux_Server.md:279` · source `02-SafeSquid_SWG/07-Supporting_Services/01-Monit.md:103` · **our** `public/safesquid_swg/interface/supporting_services_monit.md:104` |
| `/var/run/safesquid/safesquid.pid` | source `03-High Availability Monit Keepalived.md:219` · **our** `public/admin_guide/start_here/daemon.mdx:15` · **our** `public/use_cases/scaling_and_high_availability/ha_monit_keepalived.md:240` |

`linux_server.md` now carries a `**Missing:**` flag in place of the stanza, telling the operator to check `ls -l /var/run/safesquid*` on their own host.

**Note:** `ha_monit_keepalived.md`, written in pass 1, silently took the second variant. If the SME confirms the first is correct, that page needs correcting.

**NEEDS-SME-REVIEW:** which path does the shipping build write?

### 2. Licensing endpoint set

`01-Deployment_Planning.md` contradicts itself within one file:

| Section | Endpoints named |
|---|---|
| §Prepare the host before install, step 7 | `key.safesquid.com`, `updates.safesquid.com`, `repo.safesquid.net` |
| §Firewall Whitelist Requirements | `swgupdates2.safesquid.net`, `swgupdates.safesquid.net`, `sslupdates.safesquid.com`, `key.safesquid.com` |

`updates.safesquid.com` and `repo.safesquid.net` appear nowhere else in either repository. Neither was written.

**NEEDS-SME-REVIEW:** are `updates.safesquid.com` and `repo.safesquid.net` current, superseded, or wrong?

### 3. Not a contradiction

`/opt/safesquid/` for binaries and `/usr/local/safesquid/` for security, policy, and UI material are used consistently across both repositories. Safe to state; now documented in the appliance page's path table.

## Held — sourced but undated, NEEDS-SME-REVIEW

Traceable to a real source passage, but the value could not be verified against the current build. Not written to any page. Where a page would naturally carry the value, it instead carries a `**Missing:**` flag naming the gap.

| Item | Source | Blocker | Flag placed at |
|---|---|---|---|
| Cloud instance-type mapping, AWS/Azure/GCP by connection count | `…/02-Cloud_Deployment.md` §Choose an Instance Type | Instance generations undated; SKUs may be retired | `cloud_deployment.md`, load-balancing accordion |
| Auto-scaling CPU thresholds, min/max instance counts | same file, §Auto-Scaling | Undated; depends on the sizing figures also held | same |
| Disk capacity table by peak burst; ~50–100 GB/day log volume | `01-Deployment_Planning.md` §Disk and log storage | Undated, unverified against current logging behaviour | `deployment_planning.md`, storage accordion |
| Distribution version matrix; minimum kernel 3.10 | `…/03-Linux_Server.md` §Supported Distributions | Undated; wrong version = failed install | `linux_server.md`, dependencies accordion |
| Failover RTO figures: DNS 5–30 min, BGP Anycast <5 min, LB <1 min | `01-Deployment_Planning.md` §Disaster recovery | SLA-shaped claims; consistent with the existing flag at `disaster_recovery.md:35` | `deployment_planning.md`, DR accordion |
| Performance baseline: latency <50 ms, CPU <20% idle, I/O wait <5% | `01-Deployment_Planning.md` §Verify and document for audits | Undated; no measurement context given | `deployment_planning.md`, baseline accordion |
| NIC sizing thresholds: 2×1GbE to 1,500; 10GbE above; 4 ports at 3,000+ | `01-Deployment_Planning.md` §NIC sizing | Keyed to the same undated connection counts | not flagged separately; covered by the sizing note |
| Minimum specs: 4 cores / 8 GB / 100 GB disk | `main.md` §Before you start; `…/01-SafeSquid_Appliance_Builder.md` §System Requirements | Undated floor figures | not written |

### Open inconsistency to resolve

The **sizing matrix added in pass 1** (`public/deployment/deployment_planning.md`, "Sizing matrix by peak concurrent connections") carries exactly the staleness that disqualified every item in the table above. It was left in place because the no-deletion rule is absolute and its removal was not requested. It already carries a `NEEDS-SME-REVIEW` comment.

**Decision needed:** either the matrix comes out to match the standard applied here, or the held items above are admitted on the same terms the matrix was. The current state is inconsistent.

## Deliberate exclusions — not gaps

Recorded so future passes do not re-raise them:

- **Install-time estimates** (SAB 15–20 min, cloud 10–15, Linux 5–15) — `public/getting_started/install_safesquid/safesquid_appliance_builder.md` states setup-time claims are not guarantees. Consistent editorial position.
- **Third-party online PAC tester** — an external service; `pactester` covers the same need locally.
- **`alert()`-based PAC debugging** — teaches a pattern that ships to production by accident. `pactester` covers it.
- **Per-method "time to deploy" figures** on client-configuration pages — same basis as install times.

---

## Verified as already covered

Checked topic-by-topic rather than by heading, since the Mintlify pages were rewritten into the six-block PBAC structure and headings do not align with the source.

Every other deployment-relevant page in `_migration_source_v3/docs/` has an equivalent already in `public/`: `01-Getting_Started` (planning, register, install ×3, activate, connect ×5, verify), `16-Performance_Accelerators`, `17-Proxy_Clustering`, `18-Customisation`, `19-Operational_Modes`, `20-Integrations/02-VPN`, `22-Disaster_Recovery`, `24-Upgrade_SafeSquid`.

Several Mintlify pages are substantially larger than their source: `register.md` (1,616 words vs 468), `activate.md` (1,363 vs 1,122), `disaster_recovery.md` (621 vs 369). Word-count deltas on the remaining pages come from the PBAC rewrite, not lost coverage.

`main.md` hub pages under `getting_started/install_safesquid/` and `getting_started/client_configuration/` remain unregistered in `docs.json`. That matches the repo-wide pattern — all 34 `main.md` files are deliberately nav-orphaned — and is not treated as a gap.

## Known pre-existing issues, not addressed

Out of scope for an additive pass, recorded so they are not lost:

- `public/use_cases/scaling_and_high_availability/master_slave.md:60,146` uses legacy absolute links (`/Configuration_Portal`, `/Configuration_Sync`, `/Reporting_Service`) that do not resolve in the Mintlify site. Several sibling pages share the pattern.
- `public/docs.json` banner still reads `TODO before merge — set release version and link.`
