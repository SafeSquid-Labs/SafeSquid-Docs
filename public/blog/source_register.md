---
title: "Blog Source Register"
description: "Claim tracking for SafeSquid blog technical and statistical statements."
keywords: [source_register, claims_tracking, blog_governance]
mode: "center"
---

# Blog claim status register

This register tracks claim verification status for blog content.

Status labels:
- `confirmed`: verified with a primary source and available citation
- `draft`: plausible claim language pending source confirmation
- `missing`: no source captured yet; do not publish as fact

## 2025-05-17 zero-hour-phishing-beyond-url-filters

- Claim: "three-quarters of new phishing campaigns hide on already-allowed assets (Cloudflare Q1 2025)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "strategically aged domains are three times more likely to become malicious (TechRadar)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "average kit lifespan is 50 minutes (zvelo)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "52% of victims click within the first hour (Proofpoint)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "SafeSquid dynamic POST/PUT intercept blocks unknown submit hosts."  
  Status: `draft`  
  Source: Partial support in [Request Profiles](/Request_Profiles) (method-level POST/PUT + host/file matching); no documented "Trusted-Submit list" or explicit form-action interception term in docs yet

## 2025-06-02 cyberslacking

- Claim: "cyberslacking costs US $280B annually (Gartner 2024)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "task-switching can degrade output by 40% (APA 2023)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "SafeSquid path/GraphQL controls block Facebook games while preserving feeds."  
  Status: `draft`  
  Source: "Facebook read-only mode" and selective app controls are documented in [Facebook Read Only Mode](/Facebook_Read_Only_Mode) and request profiling in [Request Profiles](/Request_Profiles); GraphQL-specific control is not documented

## 2025-06-02 last-mile-reassembly-of-drive-by-malware

- Claim: "5 million parked domains and 31% suspicious shift (Palo Alto)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "median downtime after browser-based ransomware drop is 6 days (Coveware Q4 2024)."  
  Status: `missing`  
  Source: not yet recorded
- Claim: "SafeSquid assembly watchdog blocks concat/atob/WebAssembly on untrusted blobs."  
  Status: `missing`  
  Source: No internal product documentation found for concat/atob/WebAssembly assembly blocking; [Native Sandboxing](/Native_Sandboxing) is under construction

## 2025-06-02 csrf-abuse

- Claim: "XSS still ranks in OWASP Top 10."  
  Status: `confirmed`  
  Source: OWASP Top 10 category list
- Claim: "SafeSquid auto-token injection and cookie rewrite behavior."  
  Status: `draft`  
  Source: Cookie/header policy controls are documented in [Cookie Inspection](/Cookie_Inspection) and [Header Re-Write](/Header_Obfuscation), but automatic CSRF token injection/origin enforcement is not documented

## 2025-06-02 dns-tunneling

- Claim: "SafeSquid category DNS allow-list, QPS thresholds, entropy detection behavior."  
  Status: `missing`  
  Source: DNS security docs confirm DNSBL, GeoIP, and homograph controls only ([DNS Security](/DNS_Security), [DNS Blacklisting](/DNSBL)); no internal documentation for DNS QPS thresholds or DNS entropy analytics

## 2026-04-07 rubric-advantages-claims-use-cases-troubleshooting

- Claim: "Use-case library maps directly to documented SafeSquid controls."  
  Status: `confirmed`  
  Source: Control families are documented in [Access Restriction](/Access_Restriction), [Profiling Engine](/Profiling_Engine), [Content Analyser](/Content_Analyser), and [URL Redirection](/URL_Redirection)
- Claim: "Any guide claiming full vendor API edge-case coverage requires periodic revalidation."  
  Status: `draft`  
  Source: Use-case scope is documented in [Allow Specific YouTube Channel and Its Playlist](/Allow_Specific_YouTube_Channel_and_its_Playlist) and [YouTube API Integration With SafeSquid To Allow Specific YouTube Videos](/YouTube_API_Integration_With_SafeSquid_To_Allow_Specific_YouTube_Videos); release-note enforcement process is not formalized in docs yet
- Claim: "Troubleshooting library mirrors major SafeSquid subsystems."  
  Status: `confirmed`  
  Source: Troubleshooting categories align to [Getting Started](/Getting_Started), [SSL Inspection](/SSL_Inspection), [Authentication](/Authentication), [DNS Security](/DNS_Security), and [Access Restriction](/Access_Restriction)
- Claim: "Vendor/browser/OS compatibility behavior is exhaustively covered."  
  Status: `missing`  
  Source: Current troubleshooting docs are symptom-based and do not provide an exhaustive version matrix in [Troubleshooting](/Troubleshooting)

Requested edits:
- Keep customer-facing promises scoped to documented behavior; avoid "all edge cases" wording for vendor APIs.
- Add a compatibility-matrix task for major browsers/OS versions if marketing or sales collateral requires exhaustive coverage claims.
- Keep the `Advantages` sections status-tagged (`confirmed`, `draft`, `missing`) until SSOT and release-note governance are explicit.

## Escalations

- Technical accuracy review requested from CTO for all `draft` product-behavior claims.
- Citation backfill required before publishing any `missing` statistical claim as fact.

## 2026-04-07 getting-started-comparative-and-performance-claims-safa-258

- Claim: "SafeSquid provides three supported install paths (SAB, cloud, Linux TAR)."  
  Status: `confirmed`  
  Source: [Install SafeSquid hub](/Install_SafeSquid), [SafeSquid Appliance Builder](/SafeSquid_Appliance_Builder), [Cloud Deployment](/Cloud_Deployment), [Linux Server Install](/Linux_Server)
- Claim: "SAB enables a rapid first deployment (~15 to 20 minutes total)."  
  Status: `confirmed`  
  Source: [What is SafeSquid SWG?](/What_is_SafeSquid_SWG) and [SafeSquid Appliance Builder](/SafeSquid_Appliance_Builder)
- Claim: "SafeSquid supports multiple client-routing models (explicit, PAC, system-wide, enterprise, app-specific)."  
  Status: `confirmed`  
  Source: [Connect Your Client hub](/Connect_Your_Client) and child docs
- Claim: "Commercial activation unlocks real-time threat intelligence features."  
  Status: `confirmed`  
  Source: [Activate](/Activate), [What is SafeSquid SWG?](/What_is_SafeSquid_SWG), [Threat Intelligence Feeds](/Threat_Intelligence_Feeds)
- Claim: "Operational telemetry exposes thread-pool counters in performance logs."  
  Status: `confirmed`  
  Source: [What is SafeSquid SWG?](/What_is_SafeSquid_SWG), [Security Logs](/Security_Logs)
- Claim: "SafeSquid offers better throughput/latency than competing gateways."  
  Status: `missing`  
  Source: No in-repo benchmark or external validated comparative dataset linked from Getting Started pages
- Claim: "SafeSquid SMP/shared-memory internals are proven differentiators versus multi-process proxies."  
  Status: `missing`  
  Source: No architecture deep-dive or benchmark evidence in this doc set; explicitly marked as not documented in [What is SafeSquid SWG?](/What_is_SafeSquid_SWG)
- Claim: "One client deployment model is universally best."  
  Status: `missing`  
  Source: [Connect Your Client hub](/Connect_Your_Client) marks model choice as deployment-dependent
- Claim: "Verify-your-setup checklist alone proves production readiness."  
  Status: `draft`  
  Source: [Verify Your Setup](/Verify_Your_Setup) includes baseline checks but references further HA and hardening docs for production-grade assurance

## 2026-04-07 remaining-sections-rubric-pass-safa-259

- Claim: "Rubric pass now covers the major remaining sections (SWG, DNS Security, Authentication, SSL Inspection, Use Cases, Troubleshooting)."  
  Status: `confirmed`  
  Source: Edited hubs and child docs under [SafeSquid SWG](/SafeSquid_SWG), [DNS Security](/DNS_Security), [Authentication](/Authentication), [SSL Inspection](/SSL_Inspection), [Use Cases](/Use_Cases), and [Troubleshooting](/Troubleshooting)
- Claim: "All comparative and performance assertions in these sections are fully benchmark-backed and publish-ready as hard facts."  
  Status: `missing`  
  Source: No single benchmark or third-party validation pack is linked across all updated sections; keep comparative wording constrained to documented behavior
- Claim: "Current section-hub quickstart paths and 'next steps' links are complete enough for guided navigation, pending final QA."  
  Status: `draft`  
  Source: Updated `main.md` files and related child pages; requires final navigation QA against [docs.json](/docs.json) before publication

## 2026-04-07 what-is-safesquid-swg-clarifications-safa-270

- Claim: "What is SafeSquid SWG page now uses explicit claim-status governance (`confirmed`, `draft`, `missing`) for all positioning/performance statements."  
  Status: `confirmed`  
  Source: [What is SafeSquid SWG?](/What_is_SafeSquid_SWG)
- Claim: "Comparative performance and architecture differentiator wording is constrained to `missing` until benchmark/architecture SSOT exists."  
  Status: `confirmed`  
  Source: [What is SafeSquid SWG?](/What_is_SafeSquid_SWG) (`Architecture and positioning claims` and `Source register` sections)
- Claim: "No CTO escalation required in this pass because no new draft technical behavior claim was introduced."  
  Status: `draft`  
  Source: This pass removed/normalized wording but did not add new unverified behavior; escalate to CTO if a future revision introduces draft product-mechanism claims
