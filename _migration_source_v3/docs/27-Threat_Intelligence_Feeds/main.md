---
title: Threat Intelligence Feeds
slug: /Threat_Intelligence_Feeds
description: Real-time cloud-integrated threat intelligence for web categorization, application identification, SSL security, and malware scanning in SafeSquid SWG.
keywords:
  - SafeSquid threat intelligence
  - threat intelligence feeds
  - real-time security feeds
  - web categorization feeds
  - SafeSquid cloud security updates
  - malware signature updates
---


# Cloud threat intelligence keeps enforcement current

Static blocklists and outdated signatures create blind spots that attackers exploit within hours of a new campaign. SafeSquid's cloud-integrated threat intelligence delivers real-time updates to web categorization, application signatures, SSL security, image analysis, malware scanning, and geo-location databases. Feed refresh timestamps and category versions appear in the SafeSquid interface and logs; audit reports confirm current threat posture.

## Outdated threat data creates exploitable gaps

Threat actors register and rotate domains, change hosting infrastructure, and modify payloads faster than manual updates can track. Enterprises relying on static blocklists or weekly feed refreshes face a window of exposure measured in hours. Compliance frameworks (NIST SP 800-53 SI-5, ISO 27001 A.12.2.1) require timely threat intelligence to maintain control effectiveness.

SafeSquid addresses this with automatic, cloud-backed feed updates that keep enforcement aligned with the latest threat landscape.



## Feeds cover categorization, signatures, and reputation

SafeSquid cloud services deliver real-time updates across six intelligence domains:

| Feed | Purpose | Used by |
|---|---|---|
| **Web Categorization** | URL and domain classification into categories (malware, phishing, adult, social media, etc.) | [Web Categorization](/docs/Profiling_Engine/Web_Categorization/), [Access Restriction](/docs/Access_Restriction/main/) |
| **Application Signatures** | Identify applications by traffic patterns and user-agent strings | [Application Signatures](/docs/Profiling_Engine/Application_Signatures/) |
| **SSL Security** | Certificate reputation, pinning data, and trust chain intelligence | [SSL Inspection](/docs/SSL_Inspection/main/) |
| **Image Analysis** | Classification models for inappropriate or non-compliant visual content | [Image Analyser AI](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/) |
| **Malware Scanning** | Signature databases and behavioral indicators for ClamAV and SqScan | [Malware Scanners](/docs/Malware_Scanners/main/) |
| **Geo-Location** | IP-to-country and IP-to-ASN mapping for geographic policy enforcement | [GeoIP](/docs/DNS_Security/GeoIP/) |

Feed delivery and refresh schedules are managed by the SafeSquid cloud service. SafeSquid instances pull updates automatically when connected to the cloud. Custom categorization overrides (managed via the [Self-Service Portal](/docs/SafeSquid_SWG/Self-Service_Portal/)) merge with cloud feeds on each refresh.



## Prerequisites

- **SafeSquid activation**: A valid product activation key from [key.safesquid.com](https://key.safesquid.com). The activation key links the instance to the cloud feed service.
- **Internet connectivity**: SafeSquid must reach the SafeSquid cloud endpoints for feed updates. If SafeSquid operates behind a firewall, allow outbound HTTPS to `*.safesquid.com`.
- **Subscription**: Some feed categories (e.g. DLP signatures, advanced application signatures) require a premium subscription. Check the [Self-Service Portal](/docs/SafeSquid_SWG/Self-Service_Portal/) for active subscriptions.



## Verification and evidence

- **Interface Checks**: In the [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), check the Support page for feed version numbers and last-update timestamps. Web Categorization, Application Signatures, and malware databases each show their current version.
- **Log Analysis**: SafeSquid logs feed update events including success, failure, and version changes. Search logs for feed-related entries to confirm refresh frequency.
- **Custom Categorization**: Verify custom categories created in the Self-Service Portal appear in SafeSquid's categorization engine after the next feed sync. Test by browsing a custom-categorized URL and checking the access log for the expected category.



## Next steps

- [Web Categorization](/docs/Profiling_Engine/Web_Categorization/) to configure category-based policies.
- [DNS Security](/docs/DNS_Security/main/) for DNSBL, GeoIP, and homograph detection.
- [Malware Scanners](/docs/Malware_Scanners/main/) for ClamAV, ICAP, and SqScan configuration.
- [Self-Service Portal](/docs/SafeSquid_SWG/Self-Service_Portal/) to manage custom categorization and subscriptions.

