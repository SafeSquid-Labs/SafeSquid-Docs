---
title: Reports
description: Reports entry point for SafeSquid SWG policy evidence, forensic investigation, SIEM forwarding, and operational review.
keywords:
  - SafeSquid reports
  - SafeSquid SIEM
  - proxy reporting
  - audit evidence
---

# Reports

Use **Reports** to prove what SafeSquid allowed, blocked, inspected, bypassed, or forwarded. A policy without reportable evidence cannot support audit, incident response, or executive risk decisions.

The Application Eco-system source identifies SIEM log forwarding over UDP for real-time access, extended, and native logs. Treat Reports as the console entry point for that evidence flow.

## Evidence to review

- access outcomes by user, group, source, destination, and policy
- blocked malware, phishing, category, and application events
- bypass or exception activity
- configuration and privileged-access changes
- SIEM forwarding status for real-time investigation

## Verification

After a policy change, trigger a controlled request and confirm:

1. The expected allow or block decision appears in Reports.
2. The event includes enough identity and destination context for investigation.
3. The same event reaches the SIEM when forwarding is configured.

## Next steps

- Use [Reporting Service](/safesquid_swg/interface/reporting_service) for deployment patterns and troubleshooting.
- Use [Configure](/safesquid_swg/policy_management_console/configure) to adjust the policy that generated the report.
