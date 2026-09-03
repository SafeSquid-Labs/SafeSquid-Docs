---
title: "Configuration"
---

<Note>
  CLI man page: `safesquid-sections(7)`
</Note>

Administrator guides for the Secure Web Gateway. Start with the first-configuration path if you are new; use the section pages when you need detail, code-validated examples, and how to verify a change.

Topic pages ([Architecture](/admin_guide/start_here/architecture), [Authentication](/admin_guide/start_here/authentication), [Feeds](/admin_guide/start_here/cloud_feeds), [Logging](/admin_guide/start_here/logging), …) explain cross-cutting behaviour. Section pages document one Web UI configuration list each.

<Note>
**New here?** Open [First configuration](/admin_guide/start_here/first_configuration) — a short path from service check to a working Allow rule and your first content policy. Two config layers: Web UI (policy) and [startup.ini](/admin_guide/start_here/startup_ini) (process tunables). CLI: `man safesquid`, `man safesquid-access`, etc. (after package install).
</Note>

## Start here

- [First configuration](/admin_guide/start_here/first_configuration) — recommended for new administrators
- [Architecture and request pipeline](/admin_guide/start_here/architecture)
- [Daemon, service, and files](/admin_guide/start_here/daemon)
- [Network settings](/admin_guide/infrastructure_and_access/network_settings)
- [Access restrictions](/admin_guide/infrastructure_and_access/access_restrictions)
- [Authentication](/admin_guide/start_here/authentication)
- [Access Profiles](/admin_guide/policies_and_profiles/access_profiles)
- [Logging and troubleshooting](/admin_guide/start_here/logging)
- [Debug response headers](/admin_guide/start_here/debug_response_headers)
- [startup.ini tunables](/admin_guide/start_here/startup_ini)
- [Cloud / categorisation feeds](/admin_guide/start_here/cloud_feeds)
- [Integrations](/admin_guide/start_here/integrations)
- [Tools and Reports](/admin_guide/start_here/tools_and_reports)

## Infrastructure and access

- [Access restrictions](/admin_guide/infrastructure_and_access/access_restrictions)
- [Network settings](/admin_guide/infrastructure_and_access/network_settings)
- [System configuration](/admin_guide/infrastructure_and_access/system_configuration)
- [Integrate LDAP](/admin_guide/infrastructure_and_access/integrate_ldap)
- [HTTPS Inspection](/admin_guide/infrastructure_and_access/https_inspection)
- [Proxy chain](/admin_guide/infrastructure_and_access/proxy_chain)
- [FTP browsing](/admin_guide/infrastructure_and_access/ftp_browsing)
- [WCCP](/admin_guide/infrastructure_and_access/wccp)
- [Subscription](/admin_guide/infrastructure_and_access/subscription)
- [SSqore](/admin_guide/infrastructure_and_access/ssqore)

## Policies and profiles

- [Access Profiles](/admin_guide/policies_and_profiles/access_profiles)
- [Speed Limits](/admin_guide/policies_and_profiles/speed_limits)
- [Request Types](/admin_guide/policies_and_profiles/request_types)
- [Response Types](/admin_guide/policies_and_profiles/response_types)
- [Time Profiler](/admin_guide/policies_and_profiles/time_profiler)
- [Templates](/admin_guide/policies_and_profiles/templates)
- [Application Signatures](/admin_guide/policies_and_profiles/application_signatures)
- [Content Signatures](/admin_guide/policies_and_profiles/content_signatures)
- [Suggested Profiles](/admin_guide/policies_and_profiles/suggested_profiles)
- [Categorize Web-Sites](/admin_guide/policies_and_profiles/categorize_web_sites)

## Filtering and privacy

- [Cookie filter](/admin_guide/filtering_and_privacy/cookie_filter)
- [Header filter](/admin_guide/filtering_and_privacy/header_filter)
- [Text analyzer](/admin_guide/filtering_and_privacy/text_analyzer)
- [DNS Blacklist](/admin_guide/filtering_and_privacy/dns_blacklist)
- [Redirect](/admin_guide/filtering_and_privacy/redirect)
- [Content modifier](/admin_guide/filtering_and_privacy/content_modifier)
- [Elevated Privacy](/admin_guide/filtering_and_privacy/elevated_privacy)
- [External applications](/admin_guide/filtering_and_privacy/external_applications)

## Performance

- [Caching](/admin_guide/performance/caching)
- [Prefetching](/admin_guide/performance/prefetching)

## Security scanners

- [Clam antivirus](/admin_guide/security_scanners/clam_antivirus)
- [SqScan](/admin_guide/security_scanners/sqscan)
- [Image analyzer](/admin_guide/security_scanners/image_analyzer)
- [DLP](/admin_guide/security_scanners/dlp)
- [ICAP](/admin_guide/security_scanners/icap)
