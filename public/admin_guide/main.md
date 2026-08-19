---
title: Admin Guide
description: Migrated legacy reference for SafeSquid SWG — runtime mechanics, section-by-section field behaviour, and documented code quirks.
keywords:
  - admin guide
  - SafeSquid administration
  - runtime mechanics
  - code quirks
---

# Admin Guide

Section-by-section reference migrated from the legacy SafeSquid documentation site. These pages document
**how each Web UI section behaves at runtime**, including fields that are stored in configuration but not
read by the engine. Task-based and conceptual coverage lives under Use Cases.

## Sections

- [Start here](/admin_guide/start_here/main) — Architecture, daemon, diagnostics, feeds, and first-run operations for SafeSquid SWG administrators.
- [Infrastructure and access](/admin_guide/infrastructure_and_access/main) — Listeners, global settings, directory integration, TLS inspection, upstream routing, and licensing.
- [Policies and profiles](/admin_guide/policies_and_profiles/main) — Labelling and policy sections that tag connections and decide what may be fetched.
- [Filtering and privacy](/admin_guide/filtering_and_privacy/main) — Header, cookie, keyword, DNS, redirect, rewrite, and privacy filters.
- [Performance](/admin_guide/performance/main) — Rate limiting, quotas, caching, and prefetching behaviour.
- [Security scanners](/admin_guide/security_scanners/main) — Malware, image, DLP, and ICAP inspection engines.

## Looking for day-2 operations?

Scaling, performance tuning, customisation, and upgrade content previously served from
`/admin_guide/` now lives under Use Cases:

- [Scaling & High Availability](/use_cases/scaling_and_high_availability/proxy_clustering)
- [Performance Acceleration](/use_cases/performance_acceleration/performance_accelerators)
- [Customisation](/use_cases/customisation/customisation)
- [Upgrade](/use_cases/upgrade/upgrade_safesquid)
