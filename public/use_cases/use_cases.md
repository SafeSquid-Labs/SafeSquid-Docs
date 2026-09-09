---
title: Use Cases
description: Find the SafeSquid control that closes a specific attack surface, compliance gap, or operational risk.
slug: /Use_Cases
keywords:
  - SafeSquid use cases
  - secure web gateway controls
  - proxy policy examples
  - SafeSquid configuration scenarios
---

# Find the Control for Your Risk

A proxy that only forwards traffic is not a security control. Each use case below closes one
specific gap — encrypted-traffic blindness, credential misuse, DNS-layer evasion, sensitive-data
exfiltration — with a policy you configure and can prove is enforced. Start from the risk you
need to close, not from a feature list.

## Foundation

Controls most deployments configure first, because later use cases depend on them.

- **[SSL Inspection](/use_cases/ssl_inspection/ssl_inspection)** - decrypt and inspect HTTPS traffic; without it, every other control is blind to most of today's web.
- **[Authentication](/use_cases/authentication/authentication)** - attribute every request to a user or group so policy and logs mean something.
- **[Profiling Engine](/use_cases/profiling_engine/profiling_engine)** - classify requests and responses so downstream controls act on the right traffic.

## Threat prevention

- **[DNS Security](/use_cases/dns_security/dns_security)** - block malicious and tunnelling domains before a connection is ever made.
- **[Malware Scanning](/use_cases/malware_scanning/malware_scanners)** - inspect downloads and payloads in the request path, not after the fact.

## Access control

- **[Access Restriction](/use_cases/access_restriction/access_restriction)** - allow or block sites, apps, and categories by user, group, or time window.
- **[Content Modifier](/use_cases/content_modifier/content_modifier)** - rewrite pages in flight to remove risky elements without blocking the whole site.
- **[Cookie Inspection](/use_cases/cookie_inspection/cookie_inspection)** - strip or filter cookies that leak session or tracking data.
- **[Header Rewrite](/use_cases/header_rewrite/header_obfuscation)** - rewrite request and response headers to enforce corporate-account-only access to consumer services.
- **[URL Redirection](/use_cases/url_redirection/url_redirection)** - send a matched request to a different destination instead of blocking it outright.

## Data protection

- **[Data Leakage Prevention](/use_cases/data_leakage_prevention/data_leakage_prevention)** - stop sensitive content leaving over the web egress path, not just email.

## Visibility

- **[Audit & Forensics](/use_cases/audit_and_forensics/audit_forensics)** - preserve evidence an auditor or incident responder can actually use.

## Integrations

- **[Integrations](/use_cases/integrations/integrations)** - connect SafeSquid to ICAP scanners, SIEM, and VPN so existing tooling sees proxy-layer evidence.

## Operations and lifecycle

Day-2 operations for a control already in production — scaling, tuning, customisation, and
upgrades.

- **[Scaling & High Availability](/use_cases/scaling_and_high_availability/proxy_clustering)** - add clustering and failover once a single node is proven.
- **[Performance Acceleration](/use_cases/performance_acceleration/performance_accelerators)** - cache and tune so inspection doesn't cost you latency.
- **[Customisation](/use_cases/customisation/customisation)** - adapt templates, startup parameters, and configuration sync to your environment.
- **[Upgrade](/use_cases/upgrade/version_upgrade)** - plan version and OS upgrades without an enforcement gap.

## Next steps

- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - close the encrypted-traffic blind spot first.
- [Authentication](/use_cases/authentication/authentication) - attribute traffic before you write policy against it.
- [Deployment](/deployment/main) - plan sizing, installation, and rollout before configuring use cases.
