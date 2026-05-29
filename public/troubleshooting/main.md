---
title: Troubleshooting
description: Diagnostic runbooks for SafeSquid SWG service, policy, DNS, authentication, SSL inspection, reporting, and installation incidents.
keywords:
  - troubleshooting
  - diagnostics
  - SafeSquid SWG
---

# Troubleshooting

SafeSquid troubleshooting must restore service without destroying audit evidence. Start with the broad diagnostic checklist, then use the incident-specific runbook that matches the symptom, affected control, and business impact.

## Quickstart path

1. [Run the base diagnostic checklist](/troubleshooting/troubleshooting) to identify whether the fault is network, DNS, proxy, authentication, SSL inspection, reporting, or local system health.
2. [Find a complete connection log](/troubleshooting/how_to_use_find_client_id_sh_for_getting_complete_connection_log) when a user, device, or URL needs transaction-level evidence.
3. Select the runbook below, collect screenshots and logs before changes, then verify user access and policy enforcement after recovery.

## Service and access failures

- [Website not accessible](/troubleshooting/website_not_accessible)
- [Connection failure on websites](/troubleshooting/connection_failure_on_websites)
- [Proxy server refusing connection error](/troubleshooting/proxy_server_refusing_connection_error)
- [Product failure](/troubleshooting/product_failure)
- [Interface access denied](/troubleshooting/interface_access_denied)
- [Unable to login specific website](/troubleshooting/unable_to_login_specific_website)

## Policy and security failures

- [SSL certification errors](/troubleshooting/ssl_inspection_issues)
- [SafeSearch not working](/troubleshooting/safesearch_not_working)
- [Whitelisted website blocked](/troubleshooting/whitelisted_website_blocked)
- [Custom categorisation not working](/troubleshooting/custom_categorisation_not_working)
- [SSO authentication fail](/troubleshooting/sso_authentication_fail)
- [Failed to fetch LDAP entries](/troubleshooting/failed_to_fetch_ldap_entries)

## Platform and reporting failures

- [DNS failure](/troubleshooting/dns_failure)
- [Disk space and RAM are full](/troubleshooting/disk_space_and_ram_are_full)
- [Blank report page](/troubleshooting/blank_report_page)
- [Not generating performance plot](/troubleshooting/not_generating_performance_plot)
- [Installation issues](/troubleshooting/installation_issues)
- [No tar-ball support](/troubleshooting/no_tar_ball_support)

## Evidence expectations

Each incident record should include the affected user or source IP address, requested URL, timestamp, browser error, SafeSquid log excerpt, screenshots of policy changes, and post-fix verification. Keep this evidence with the incident ticket for SOC 2 change management, ISO 27001 incident handling, and NIST SP 800-53 auditability.

## Next steps

- Use [Audit and Forensics](/use_cases/audit_and_forensics/audit_forensics) to plan retention and investigation evidence.
- Use [Reporting Module](/use_cases/audit_and_forensics/reporting_module) to validate reports after recovery.
- Use [Configuration Portal](/safesquid_swg/interface/configuration_portal) to confirm policy changes in the SafeSquid interface.
