---
title: "Configuration"
---

Every Configuration group below mirrors a menu you can actually click in the SafeSquid Configure console — **Application Setup**, **Real Time Content Security**, **Custom Settings**, and **Restriction Policies** match the console's own left-hand navigation, verified against a live instance. **Administration Basics** and **Licensing and Self-Service Portal** cover day-2 operator tasks that sit above any single Configure section.

<Warning>
  **Administration Basics and Licensing and Self-Service Portal are mid-restructure.** They currently list the closest existing pages, not the final task list — some topics (Save and activate configuration, Reload versus restart, Use the command line, and others) don't have a page here yet. Treat these two groups as a work in progress, not a finished reference.
</Warning>

"Manage VPN settings" — previously listed here as a missing local topic — turned out not to be a
local Configure/Support page at all: it's a **Manage VPN** tab on
[key.safesquid.com](https://key.safesquid.com) itself (confirmed live), tied to roaming-user VPN
client licensing. See [Self-Service Portal](/architecture/interface/self_service_portal).

## Quickstart path

1. **[First configuration](/configuration/start_here/first_configuration)** - confirm the service is running and reachable before you touch policy.
2. **[Access restrictions](/configuration/application_setup/access_restrictions)** - lock down who can reach the proxy before you open any content policy.
3. **[Access Profiles](/configuration/restriction_policies/access_profiles)** - write your first content-access rule.
4. **[Logging and troubleshooting](/configuration/start_here/logging)** - confirm the rule actually fired before you trust it.

## Administration Basics

- [First configuration](/configuration/start_here/first_configuration) — recommended for new administrators
- [Architecture and request pipeline](/configuration/start_here/architecture)
- [Daemon, service, and files](/configuration/start_here/daemon)
- [Authentication](/configuration/start_here/authentication)
- [Logging and troubleshooting](/configuration/start_here/logging)
- [Debug response headers](/configuration/start_here/debug_response_headers)
- [startup.ini tunables](/configuration/start_here/startup_ini)
- [Cloud / categorisation feeds](/configuration/start_here/cloud_feeds)
- [Integrations](/configuration/start_here/integrations)
- [Tools and Reports](/configuration/start_here/tools_and_reports)

## Licensing and Self-Service Portal

- [Subscription](/configuration/infrastructure_and_access/subscription) — upload the activation key
- [Support](/configuration/infrastructure_and_access/support) — License Details panel and appliance tools

## Application Setup

- [Network settings and listeners](/configuration/application_setup/network_settings_and_listeners)
- [Integrate LDAP](/configuration/application_setup/integrate_ldap)
- [Access restrictions](/configuration/application_setup/access_restrictions)
- [Accelerators](/configuration/application_setup/accelerators/caching)
- [System configuration](/configuration/application_setup/system_configuration)
- [Proxy chain](/configuration/application_setup/proxy_chain)
- [FTP browsing](/configuration/application_setup/ftp_browsing)
- [WCCP](/configuration/application_setup/wccp)
- [SSqore](/configuration/application_setup/ssqore)

## Real Time Content Security

- [HTTPS Inspection](/configuration/real_time_content_security/https_inspection)
- [Clam antivirus](/configuration/real_time_content_security/clam_antivirus)
- [Text analyzer](/configuration/real_time_content_security/text_analyzer)
- [Redirect](/configuration/real_time_content_security/redirect)
- [DNS Blacklist](/configuration/real_time_content_security/dns_blacklist)
- [Image analyzer](/configuration/real_time_content_security/image_analyzer)
- [Content modifier](/configuration/real_time_content_security/content_modifier)
- [DLP](/configuration/real_time_content_security/dlp)
- [ICAP](/configuration/real_time_content_security/icap)
- [SqScan](/configuration/real_time_content_security/sqscan)

## Custom Settings

- [Categorize Web-Sites](/configuration/custom_settings/categorize_web_sites)
- [Time Profiler](/configuration/custom_settings/time_profiler)
- [Response Types](/configuration/custom_settings/response_types)
- [Request Types](/configuration/custom_settings/request_types)
- [Templates](/configuration/custom_settings/templates)
- [External applications](/configuration/custom_settings/external_applications)
- [Application Signatures](/configuration/custom_settings/application_signatures) — not in the current live console; legacy reference
- [Content Signatures](/configuration/custom_settings/content_signatures) — not in the current live console; legacy reference
- [Suggested Profiles](/configuration/custom_settings/suggested_profiles) — not in the current live console; legacy reference

## Restriction Policies

- [Privacy control](/configuration/restriction_policies/privacy_control/cookie_filter) — Cookie filter, Header filter, Elevated Privacy
- [Access Profiles](/configuration/restriction_policies/access_profiles)
- [Speed Limits](/configuration/restriction_policies/speed_limits)

## Next steps

- [Deployment](/deployment/licensing_requirements) - size and schedule the rollout before you configure policy.
- [Choose an Architecture](/deployment/choose_an_architecture) - confirm the proxy mode this guide's settings apply to.
- [Troubleshooting](/troubleshooting/troubleshooting) - diagnose a symptom instead of reading section by section.
