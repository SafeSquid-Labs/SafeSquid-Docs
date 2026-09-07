---
title: Application Ecosystem
description: Navigation hub for SafeSquid SWG enforcement, DNS security, browser isolation, reporting, self-service operations, and intelligence feeds.
keywords:
  - SafeSquid application ecosystem
  - SafeSquid proxy service
  - SafeSquid reporting service
  - SafeSquid threat intelligence
---

# Application Ecosystem

SafeSquid SWG is an operating ecosystem, not a single proxy daemon. The proxy service enforces policy, DNS security reduces resolution-time risk, reporting preserves evidence, the Self-Service Portal manages cloud-linked workflows, and threat-intelligence feeds keep controls current.

The legacy source page for Application Eco-system identifies the operating scope as SafeSquid files and folders, startup parameters, Self-Service Portal management, required supporting services, and SIEM log forwarding. This hub maps those topics into the current Architecture tab.

## Quickstart path

1. [Proxy Service](/architecture/application_ecosystem/proxy_service) — understand the enforcement point before designing traffic flow.
2. [Integrated DNS Security](/architecture/overview/integrated_dns_security) — reduce phishing, malware, and DNS tunnelling risk before HTTP policy runs.
3. [Remote Browser Isolation](/architecture/application_ecosystem/remote_browser_isolation) — separate high-risk browsing activity from trusted endpoints.
4. [Reporting Service](/architecture/interface/reporting_service) — preserve audit, forensic, and SIEM-ready evidence.
5. [Self-Service Portal](/architecture/interface/self_service_portal) — manage activation, licensing, categorization, certificate, and backup-linked workflows.
6. [Threat Intelligence Feeds](/architecture/application_ecosystem/threat_intelligence_feeds) — keep classification, malware, SSL, GeoIP, and content signals current.

## Next steps

- Use [Supporting Services](/architecture/interface/supporting_services) to operate Monit, BIND, and NTP dependencies.
- Use [Policy Management Console](/architecture/policy_management_console/main) to configure policy, reports, and support workflows.
- Use [Files and Folders](/architecture/files_and_folders/files_and_folders) to locate server-side configuration and evidence paths.
