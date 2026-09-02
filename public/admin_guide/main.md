---
title: "Admin Guide"
---

Every Admin Guide group below mirrors a menu you can actually click in the SafeSquid Configure console — **Application Setup**, **Real Time Content Security**, **Custom Settings**, and **Restriction Policies** match the console's own left-hand navigation, verified against a live instance. **Administration Basics** and **Licensing and Self-Service Portal** cover day-2 operator tasks that sit above any single Configure section.

<Warning>
  **Administration Basics and Licensing and Self-Service Portal are mid-restructure.** They currently list the closest existing pages, not the final task list — some topics (Save and activate configuration, Reload versus restart, Use the command line, Manage VPN settings, and others) don't have a page here yet. Treat these two groups as a work in progress, not a finished reference.
</Warning>

## Quickstart path

1. **[First configuration](/admin_guide/start_here/first_configuration)** - confirm the service is running and reachable before you touch policy.
2. **[Access restrictions](/admin_guide/application_setup/access_restrictions)** - lock down who can reach the proxy before you open any content policy.
3. **[Access Profiles](/admin_guide/restriction_policies/access_profiles)** - write your first content-access rule.
4. **[Logging and troubleshooting](/admin_guide/start_here/logging)** - confirm the rule actually fired before you trust it.

## Administration Basics

- [First configuration](/admin_guide/start_here/first_configuration) — recommended for new administrators
- [Architecture and request pipeline](/admin_guide/start_here/architecture)
- [Daemon, service, and files](/admin_guide/start_here/daemon)
- [Authentication](/admin_guide/start_here/authentication)
- [Logging and troubleshooting](/admin_guide/start_here/logging)
- [Debug response headers](/admin_guide/start_here/debug_response_headers)
- [startup.ini tunables](/admin_guide/start_here/startup_ini)
- [Cloud / categorisation feeds](/admin_guide/start_here/cloud_feeds)
- [Integrations](/admin_guide/start_here/integrations)
- [Tools and Reports](/admin_guide/start_here/tools_and_reports)

## Licensing and Self-Service Portal

- [Subscription](/admin_guide/infrastructure_and_access/subscription)

## Application Setup

- [Network settings and listeners](/admin_guide/application_setup/network_settings_and_listeners)
- [Integrate LDAP](/admin_guide/application_setup/integrate_ldap)
- [Access restrictions](/admin_guide/application_setup/access_restrictions)
- [Accelerators](/admin_guide/application_setup/accelerators)
- [System configuration](/admin_guide/application_setup/system_configuration)
- [Proxy chain](/admin_guide/application_setup/proxy_chain)
- [FTP browsing](/admin_guide/application_setup/ftp_browsing)
- [WCCP](/admin_guide/application_setup/wccp)
- [SSqore](/admin_guide/application_setup/ssqore)

## Real Time Content Security

- [HTTPS Inspection](/admin_guide/real_time_content_security/https_inspection)
- [Clam antivirus](/admin_guide/real_time_content_security/clam_antivirus)
- [Text analyzer](/admin_guide/real_time_content_security/text_analyzer)
- [Redirect](/admin_guide/real_time_content_security/redirect)
- [DNS Blacklist](/admin_guide/real_time_content_security/dns_blacklist)
- [Image analyzer](/admin_guide/real_time_content_security/image_analyzer)
- [Content modifier](/admin_guide/real_time_content_security/content_modifier)
- [DLP](/admin_guide/real_time_content_security/dlp)
- [ICAP](/admin_guide/real_time_content_security/icap)
- [SqScan](/admin_guide/real_time_content_security/sqscan)

## Custom Settings

- [Categorize Web-Sites](/admin_guide/custom_settings/categorize_web_sites)
- [Time Profiler](/admin_guide/custom_settings/time_profiler)
- [Response Types](/admin_guide/custom_settings/response_types)
- [Request Types](/admin_guide/custom_settings/request_types)
- [Templates](/admin_guide/custom_settings/templates)
- [External applications](/admin_guide/custom_settings/external_applications)
- [Application Signatures](/admin_guide/custom_settings/application_signatures) — not in the current live console; legacy reference
- [Content Signatures](/admin_guide/custom_settings/content_signatures) — not in the current live console; legacy reference
- [Suggested Profiles](/admin_guide/custom_settings/suggested_profiles) — not in the current live console; legacy reference

## Restriction Policies

- [Privacy control](/admin_guide/restriction_policies/privacy_control) — Cookie filter, Header filter, Elevated Privacy
- [Access Profiles](/admin_guide/restriction_policies/access_profiles)
- [Speed Limits](/admin_guide/restriction_policies/speed_limits)

## Next steps

- [Deployment Planning](/deployment/deployment_planning) - size and schedule the rollout before you configure policy.
- [Choose an Architecture](/deployment/choose_an_architecture) - confirm the proxy mode this guide's settings apply to.
- [Troubleshooting](/troubleshooting/troubleshooting) - diagnose a symptom instead of reading section by section.
