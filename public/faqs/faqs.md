---
title: "FAQs"
slug: "/FAQs"
description: "Frequently asked questions about SafeSquid Secure Web Gateway covering installation, configuration, licensing, and troubleshooting common issues."
keywords: ["SafeSquid FAQ", "SafeSquid questions", "SafeSquid help", "SafeSquid troubleshooting", "SafeSquid support", "SafeSquid SWG FAQ"]
---

# Use the Authoritative Topic

This page replaces the legacy all-in-one FAQ. The links below lead to maintained procedures and references that include prerequisites, expected results, failure guidance, version scope, and evidence. Keep this index while legacy help-site URLs are redirected.

## Install, activate, and manage

| Question | Authoritative answer |
| --- | --- |
| How do I obtain an activation key? | [Register and Get Your Key](/getting_started/register) |
| How do I activate an instance? | [Activate Your License](/getting_started/activate) |
| How do I confirm activation? | Use the verification checkpoint in [Activate Your License](/getting_started/activate) |
| How do I reach the management interface? | [Access the Interface](/getting_started/access_the_interface) |
| Which installation path should I use? | [Deploy SafeSquid](/deploy/overview) |
| Where do I find product, platform, and readiness requirements? | [Installation Prerequisites](/getting_started/install_safesquid/prerequisites) |
| How do I plan a production deployment? | [Plan and Architect SafeSquid](/plan/overview) |
| How should configuration be backed up and restored? | [Disaster Recovery](/admin_guide/scaling_and_high_availability/disaster_recovery) |
| How should an upgrade be prepared and validated? | [Upgrade SafeSquid](/admin_guide/upgrade/upgrade_safesquid) |

## Connect users and applications

| Question | Authoritative answer |
| --- | --- |
| How do I configure a browser or workstation proxy? | [Explicit Proxy Configuration](/getting_started/client_configuration/explicit_proxy) |
| How do I deploy a PAC file? | [PAC File Configuration](/getting_started/client_configuration/pac_file) |
| How do I deploy settings to managed endpoints? | [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) |
| What if an application ignores system proxy settings? | [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) |
| Does SafeSquid support transparent steering or WCCP? | Review [Transparent Proxy](/admin_guide/scaling_and_high_availability/transparent_proxy) and [WCCP](/admin_guide/scaling_and_high_availability/wccp), then validate release-specific behavior |
| How is user identity established? | [Authentication](/use_cases/authentication/authentication) |

## Inspect HTTPS and apply policy

| Question | Authoritative answer |
| --- | --- |
| Why is HTTPS inspection required for content controls? | [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) |
| How do I deploy certificate trust? | Follow the trust prerequisites and client guidance from [Connect and Identify](/connect/overview) |
| How do I restrict social networks or applications? | [Access Restriction](/use_cases/access_restriction/access_restriction) |
| How do I enforce SafeSearch? | [SafeSearch](/use_cases/access_restriction/safesearch) |
| How do I block or control cookies? | [Cookie Inspection](/use_cases/cookie_inspection/cookie_inspection) |
| How do I prevent uploads of confidential or prohibited data? | [Data Leakage Prevention](/use_cases/data_leakage_prevention/data_leakage_prevention) |
| How do I limit upload or download behavior? | Start with the relevant access, content, and performance controls under [Security Overview](/secure/overview) |

## Reporting, logs, and support

| Question | Authoritative answer |
| --- | --- |
| Where are SafeSquid files and logs documented? | [Files and Folders](/safesquid_swg/files_and_folders/main) and [Audit and Forensics](/use_cases/audit_and_forensics/audit_forensics) |
| How do I configure reporting? | [Reporting Module](/use_cases/audit_and_forensics/reporting_module) |
| How do I investigate one connection? | [Using find\_client\_id.sh for Connection Logs](/troubleshooting/how_to_use_find_client_id_sh_for_getting_complete_connection_log) |
| What if a support archive cannot be generated? | [Unable to Generate Support Tar-ball](/troubleshooting/no_tar_ball_support) |
| What if reports are blank? | [Blank Report Page](/troubleshooting/blank_report_page) |
| What if a performance plot is unavailable? | [Unable to Generate Performance Plot](/troubleshooting/not_generating_performance_plot) |

## Performance and availability

| Question | Authoritative answer |
| --- | --- |
| Why has browsing become slow? | Capture a healthy baseline, then use [Performance Acceleration](/admin_guide/performance_acceleration/performance_accelerators) and the [Troubleshooting Method](/troubleshooting/troubleshooting) |
| What if disk or memory is exhausted? | [Free Disk and RAM to Restore Proxy Operation](/troubleshooting/disk_space_and_ram_are_full) |
| How is high availability designed? | [Proxy Clustering](/admin_guide/scaling_and_high_availability/proxy_clustering) |
| How do I prove the setup is production-ready? | [Verify Your Setup](/getting_started/verify_your_setup) |

## Licensing and commercial questions

Use the SafeSquid Self-Service Portal and the current commercial or support contact for subscription, renewal, entitlement, named-user, purchasing, or account-specific questions. Do not rely on a legacy FAQ for contractual behavior.

<Note>
  If a linked page is marked **Pending lab validation**, use it to plan or test the task and obtain release-specific confirmation before a consequential production change.
</Note>