---
title: "Threat Intelligence Feeds"
description: "SafeSquid threat-intelligence feed role for URL classification, malware signatures, SSL updates, GeoIP, and content-aware enforcement."
keywords: ["SafeSquid threat intelligence feeds", "URL classification", "malware signatures", "GeoIP", "SSL updates"]
---

# Threat Intelligence Feeds

Threat-intelligence feeds keep SafeSquid policy decisions current. Static rules decay quickly against phishing kits, malware delivery domains, remote-access tooling, and newly abused cloud services.

The application ecosystem places feed delivery beside the proxy, DNS, reporting, and Self-Service Portal paths. That placement matters: a feed outage can weaken classification and detection even when the proxy service itself is healthy.

## Feed categories

SafeSquid ecosystem documentation identifies these intelligence categories:

| Feed | Control value |
| --- | --- |
| Threat Intelligence | Identifies malicious destinations and suspicious behavior. |
| URL Classification | Supports category-based access policy and exception handling. |
| Application Identification | Helps distinguish sanctioned and unsanctioned application use. |
| Image Analysis AI Feed | Supports content-aware inspection and visual-risk decisions. |
| Content Fingerprints | Identifies known content patterns for inspection and policy. |
| Malware Signatures | Improves file and payload detection. |
| Geo-Location | Adds country or region context to destination policy. |
| SSL Updates | Keeps certificate and TLS-related decisions current. |

## Operational checks

Verify feed health during deployment and incident response:

1. Confirm the deployment can reach approved SafeSquid cloud dependencies.
2. Confirm feed update status in the appropriate operating view or logs.
3. Test a known category, malware-test, or policy-safe indicator.
4. Confirm the Reporting Service or SIEM receives the resulting event.

## Failure symptoms

| Symptom | Likely cause | Verification |
| --- | --- | --- |
| New malicious sites are not classified | Feed update path blocked | Check cloud allowlists and update status. |
| Category policy behaves inconsistently | Outdated or unsynced feed state | Compare feed timestamps across nodes. |
| SSL trust decisions look stale | SSL update path unavailable | Review update logs and certificate behavior. |

## Next steps

- Use [Self-Service Portal](/safesquid_swg/interface/self_service_portal) to understand cloud-linked operational workflows.
- Use [Reporting Service](/safesquid_swg/interface/reporting_service) to verify intelligence-driven policy events.