# Competitive Context, ICP, and Documentation Style Benchmarks

Use this reference before writing or revising any SafeSquid SWG documentation. It establishes who the reader is, why they are evaluating SafeSquid, what they are comparing it against, and how to write for their specific context.

---

## Section 1 — Ideal Customer Profile

**Sources:** K-016 (`icp_synthesis.md`), K-001 (`identity.md`), K-007 (`customers_and_segments.md`)

SafeSquid's primary customers are Indian organisations in regulated, sovereign, or sanction-affected sectors that require on-premise web security with compliance traceability. The buying trigger is an inability to use cloud-hosted or foreign SWG tools — due to regulatory mandate, data sovereignty policy, or sanctions restriction.

**Named segments (in priority order):**

1. **Government / Sovereign-Mandate PSUs** — DAE-affiliated organisations (NPCIL, NFC, HWB, BARC confirmed active customers). US sanctions on DAE prohibit US-origin technology. Make in India / GeM procurement mandated. Committee-based approval; SI-navigated process.

2. **Indian BFSI** — RBI-regulated banks (PSU and cooperative), NBFCs, insurers. RBI Master Direction 2023, SEBI CSCRF, and IRDAI 2023 mandate web security controls and internet access management. RBI data localisation circular (2018) creates institutional resistance to cloud-hosted SWG. Satara District Co-operative Bank is a confirmed active customer.

3. **Indian Critical Infrastructure PSUs** — NCIIPC-designated entities in power, energy, telecom, defence. CEA Cyber Security Guidelines (2021) and CERT-In Directions (April 2022) impose perimeter control and logging requirements.

4. **International inbound (tertiary)** — Organic only; no active outreach. Sovereignty-sensitive orgs outside India, typically in MENA, South/South-East Asia, and Africa where data sovereignty regulations are emerging.

**Buying committee:**

| Role | Function | Authority |
|---|---|---|
| CISO / GM IT Security / CIO | Initiates evaluation; holds veto | Can kill the deal regardless of technical recommendation |
| Security Administrator / Web Information Manager | Technical evaluator; internal champion | Recommends; does not approve spend |
| Procurement Department | Signs purchase order | Process-only; no technical veto |

Every confirmed won deal had at least one Security Administrator or Web Information Manager as an internal champion.

**Top CISO objections (confirmed):**
1. "We've never heard of you" — brand recognition gap vs. global incumbents
2. "You don't have certifications" — ISO 27001, CERT-In empanelment on roadmap; not yet obtained

**Primary win reasons:** On-premise deployment (sovereignty), Indian origin (sanctions / Make in India compliance), price advantage over global vendors, customised deployment support, and responsive technical support.

**Disqualify immediately when:**
- Active cloud SWG contract (Zscaler, Netskope) with no regulatory objection and multi-year term remaining
- MNC subsidiary with a group-level cloud-first SWG mandate
- Fewer than 200–300 internet-connected users with no compliance driver
- Full cloud-native infrastructure — no on-premise network to proxy through

---

## Section 2 — Competitive Landscape

**Sources:** K-011 (`go_to_market_and_competitive.md`), K-016 (`icp_synthesis.md`), K-015 (`icp_triggers_and_disqualifiers.md`)

**Direct displacement targets:**

| Competitor | Displacement condition | SafeSquid win angle |
|---|---|---|
| Zscaler | Cloud-only; rejected on data sovereignty / RBI localisation | On-prem; Indian data residency; no traffic leaves the org |
| Netskope | Cloud-first; rejected on sovereignty grounds | Same as Zscaler |
| Cisco Umbrella / WSA | Cloud-first or US-origin block under DAE sanctions | Indian origin; on-prem deployment |
| Forcepoint | US-origin; expensive; EOL risk post-acquisition | Indian origin; price advantage; local support |
| Palo Alto Prisma | Cloud-first; US-origin; expensive; complex on-prem option | Simpler on-prem deployment; significantly lower cost |
| Blue Coat / Broadcom | EOL displacement post-2022 Broadcom acquisition | Active replacement cycle; Blue Coat was dominant in Indian enterprises in the 2010s |
| Custom-built Squid proxy | Scaling failure; TLS 1.3 incompatible; maintenance burden; internal skill loss | Commercial SWG with full TLS inspection, identity-aware policy, DLP, compliance logging, and active support |

**Custom-built Squid displacement is the highest-volume latent opportunity.** Thousands of early-2000s Squid-based proxy deployments in Indian government and PSU organisations are at or past end-of-maintainability. These organisations need a supported commercial SWG — not that Squid is a bad product, but that a self-maintained build without TLS 1.3 support, identity-aware policy, and compliance-grade logging no longer meets modern regulatory requirements.

**Key framing rule:** Never disparage competitors. State factual capability differences with ✅/❌/⚠️ comparison tables. Let the technical facts do the positioning.

---

## Section 3 — Documentation Style Benchmarks

Squid Web Proxy, OpenSSL, and NoVNC represent the documentation standard that enterprise readers trust for stable, self-hosted software. These products earn credibility through precision, not marketing. Apply these lessons to SafeSquid documentation.

**Squid (`squid-cache.org`):**
- Names exactly what it does and what it doesn't — caching, forwarding, access control
- States supported protocols, platforms, and ssl-bump complexity honestly (ssl-bump requires manual certificate management; TLS 1.3 requires specific build options in older releases)
- No marketing language; enterprise readers trust this over any vendor claim
- **Lesson:** Acknowledge where Squid alone is adequate. When HTTPS inspection, identity-aware policy, DLP, or compliance-grade logging are required, state why a custom Squid build doesn't satisfy those requirements — without implying Squid itself is defective

**OpenSSL (`openssl.org`):**
- Precise version and algorithm scoping — states which TLS versions, cipher suites, and FIPS modes are supported
- Declares known limitations and deprecations explicitly
- No vague claims about security; states assumptions and boundaries
- **Lesson:** Scope every SafeSquid capability claim. State which TLS versions are inspected, which log fields are captured, what compliance frameworks the logs map to, and what SafeSquid does not do

**NoVNC (`novnc.com`):**
- Architecture-first: explains the WebSocket → VNC protocol bridge in the first paragraph
- States browser requirements precisely (no vague "modern browser" language)
- No bloat; no feature tours
- **Lesson:** Lead with how SafeSquid works architecturally before listing features. A deployment diagram communicates the proxy position, TLS termination point, and log path faster than any prose

---

## Section 4 — Indian Regulatory Compliance Drivers

**Source:** K-013 (`icp_regulatory_mandate_map.md`)

Reference these frameworks when writing for primary ICP segments. Use the specific mandate name and what it requires — not vague "compliance" language.

| Framework | Requirement relevant to SafeSquid |
|---|---|
| **RBI Master Direction on IT Governance, Risk and Controls (January 2023)** | Internet access management, web content filtering, HTTPS inspection, audit-ready logging for banks and NBFCs |
| **RBI Data Localisation Circular (April 2018)** | Payment system data must remain on servers in India — institutional basis for rejecting cloud-hosted SWG in BFSI |
| **SEBI CSCRF (2019, updated 2023)** | URL filtering, perimeter security, internet access controls for Market Infrastructure Institutions, brokers, and DPs |
| **IRDAI Cybersecurity Guidelines (2023)** | Web security controls and internet access management for licensed insurers |
| **NCIIPC CII Guidelines (IT Act Section 70A)** | Mandatory network perimeter controls for CII-designated entities; preference for domestically controlled security tools |
| **CEA Cyber Security Guidelines (October 2021)** | Network segmentation and internet security controls for power sector corporate IT |
| **CERT-In Directions (April 2022)** | Mandatory logging and 6-hour incident reporting; audit trail requirements |
| **DPDP Act 2023** | Data processing rules for Indian citizens; implementing rules for Significant Data Fiduciaries pending as of August 2025; may strengthen on-prem argument once notified |
| **DAP 2020** | Made-in-India preference for defence IT procurement; Indian-origin software satisfies indigenisation criteria |

> **Verification caveat:** All regulatory citations are from training knowledge (cutoff August 2025). Verify current versions at the respective issuing authority before using in external-facing compliance claims or proposals.

**Compliance log mapping for audit evidence:**

SafeSquid per-transaction logs cover: user identity, URL, content category, policy rule matched, TLS certificate chain, and disposition. Maps to:
- RBI MD 2023 — audit-ready internet access logs
- SEBI CSCRF — internet access evidence for regulated entities
- NIST SP 800-92 — log management guidance
- PCI-DSS Requirement 10 — audit log requirements
- SOC 2 CC7.2 — monitoring of system components
- ISO 27001 A.12.4 — logging and monitoring

---

## Section 5 — Writing Rules for ICP-Aware Documentation

Apply these rules to every page written for SafeSquid SWG documentation.

1. **Frame threat narratives for the primary ICP** — regulated Indian enterprises facing audit obligations, sovereignty constraints, and compliance mandates. Not a generic enterprise network. Name the specific regulatory pressure (RBI audit finding, CERT-In directive, NCIIPC review) rather than a generic "compliance requirement."

2. **Write for two personas simultaneously:**
   - The CISO: compliance evidence, sovereignty, business risk, regulatory exposure, cost of non-compliance
   - The Security Administrator: feature precision, exact deployment steps, verification commands, what the log looks like

3. **When positioning against cloud SWGs (Zscaler, Netskope):** sovereignty and data residency is the factual win, not a preference. RBI 2018, SEBI CSCRF, and NCIIPC guidelines provide the structural argument. State this factually, not defensively.

4. **When positioning against custom-built Squid:** the argument is maintainability, TLS 1.3 inspection capability, identity-aware policy, and compliance-grade logging — not that Squid is a poor product. A well-maintained Squid deployment is appropriate for pure HTTP caching. The argument for SafeSquid is what Squid alone cannot provide: a commercial product with deep TLS inspection, a policy engine, DLP, SIEM-ready per-user logs, and an active support contract.

5. **Cite confirmed active customers by vertical only** — nuclear/DAE sector, cooperative banking — not by name as endorsements, unless explicit permission is obtained.

6. **Scale statements:** 10,000+ instances deployed, 20M+ users globally (source: K-001, LinkedIn showcase 2026-04-09).

7. **Pricing reference (do not publish in docs without checking current rate card):** Concept Edition is free; Standard Edition is ₹93,750 / USD 1,700 per 500 users per year. Use "Concept Edition" (not "Community Edition") for the free tier.

8. **GeM listing:** SafeSquid is listed on Government e-Marketplace (GeM) as of 2026-04-09 — relevant when writing for government/PSU procurement context.
