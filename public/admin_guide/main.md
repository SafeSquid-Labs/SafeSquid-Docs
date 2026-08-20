---
title: "Admin Guide"
---

<Note>
  CLI man page: `safesquid-sections(7)`
</Note>

Administrator guides for the Secure Web Gateway. Start with the first-configuration path if you are new; use the section pages when you need detail, code-validated examples, and how to verify a change.

Topic pages ([Architecture](/admin_guide/configure/architecture), [Authentication](/admin_guide/infrastructure/authentication), [Feeds](/admin_guide/infrastructure/cloud_feeds), [Logging](/admin_guide/reporting/logging), …) explain cross-cutting behaviour. Section pages document one Web UI configuration list each.

<Note>
**New here?** Open [First configuration](/admin_guide/configure/first_configuration) — a short path from service check to a working Allow rule and your first content policy. Two config layers: Web UI (policy) and [startup.ini](/admin_guide/configure/startup_ini) (process tunables). CLI: `man safesquid`, `man safesquid-access`, etc. (after package install).
</Note>

## Start here

- [First configuration](/admin_guide/configure/first_configuration) — recommended for new administrators
- [Architecture and request pipeline](/admin_guide/configure/architecture)
- [Daemon, service, and files](/admin_guide/configure/daemon)
- [Network settings](/admin_guide/infrastructure/network_settings)
- [Access restrictions](/admin_guide/infrastructure/access_restrictions)
- [Authentication](/admin_guide/infrastructure/authentication)
- [Access Profiles](/admin_guide/policymgr/access_profiles)
- [Logging and troubleshooting](/admin_guide/reporting/logging)
- [Debug response headers](/admin_guide/reporting/debug_response_headers)
- [startup.ini tunables](/admin_guide/configure/startup_ini)
- [Cloud / categorisation feeds](/admin_guide/infrastructure/cloud_feeds)
- [Integrations](/admin_guide/infrastructure/integrations)
- [Tools and Reports](/admin_guide/utilities/tools_and_reports)

## Infrastructure and access

- [Access restrictions](/admin_guide/infrastructure/access_restrictions)
- [Network settings](/admin_guide/infrastructure/network_settings)
- [System configuration](/admin_guide/infrastructure/system_configuration)
- [Integrate LDAP](/admin_guide/infrastructure/integrate_ldap)
- [HTTPS Inspection](/admin_guide/infrastructure/https_inspection)
- [Proxy chain](/admin_guide/infrastructure/proxy_chain)
- [FTP browsing](/admin_guide/infrastructure/ftp_browsing)
- [WCCP](/admin_guide/infrastructure/wccp)
- [Subscription](/admin_guide/infrastructure/subscription)
- [SSqore](/admin_guide/infrastructure/ssqore)

## Policies and profiles

- [Access Profiles](/admin_guide/policymgr/access_profiles)
- [Speed Limits](/admin_guide/policymgr/speed_limits)
- [Request Types](/admin_guide/profilesdef/request_types)
- [Response Types](/admin_guide/profilesdef/response_types)
- [Time Profiler](/admin_guide/profilesdef/time_profiler)
- [Templates](/admin_guide/profilesdef/templates)
- [Application Signatures](/admin_guide/profilesdef/application_signatures)
- [Content Signatures](/admin_guide/profilesdef/content_signatures)
- [Suggested Profiles](/admin_guide/profilesdef/suggested_profiles)
- [Categorize Web-Sites](/admin_guide/profilesdef/categorize_web_sites)

## Filtering and privacy

- [Cookie filter](/admin_guide/filter/cookie_filter)
- [Header filter](/admin_guide/filter/header_filter)
- [Text analyzer](/admin_guide/policymgr/text_analyzer)
- [DNS Blacklist](/admin_guide/policymgr/dns_blacklist)
- [Redirect](/admin_guide/policymgr/redirect)
- [Content modifier](/admin_guide/policymgr/content_modifier)
- [Elevated Privacy](/admin_guide/filter/elevated_privacy)
- [External applications](/admin_guide/policymgr/external_applications)

## Performance

- [Caching](/admin_guide/accelerator/caching)
- [Prefetching](/admin_guide/accelerator/prefetching)

## Security scanners

- [Clam antivirus](/admin_guide/antivirus/clam_antivirus)
- [SqScan](/admin_guide/antivirus/sqscan)
- [Image analyzer](/admin_guide/antivirus/image_analyzer)
- [DLP](/admin_guide/antivirus/dlp)
- [ICAP](/admin_guide/antivirus/icap)
