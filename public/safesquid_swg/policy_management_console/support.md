---
title: Support
description: Support entry point for SafeSquid SWG troubleshooting evidence, configuration context, and escalation readiness.
keywords:
  - SafeSquid support
  - SafeSquid troubleshooting
  - support evidence
  - proxy diagnostics
---

# Support

Use **Support** when an issue needs structured evidence, not guesswork. Good support data shortens outages and prevents risky emergency changes that bypass security controls.

The Application Eco-system source highlights server files, folders, startup parameters, supporting services, and log forwarding. Those are the first evidence areas to collect before escalation.

## Evidence to collect

- SafeSquid version and activation state
- affected user, source IP, destination, and time window
- relevant Reports entries or SIEM events
- service health for SafeSquid, Monit, BIND, and NTP
- recent configuration changes from `config.log`
- startup parameters and service unit state

## Escalation checks

Before escalating, confirm:

1. The issue is reproducible or bounded to a clear time window.
2. Local logs show the same result users report.
3. Supporting services are healthy.
4. A rollback option exists for recent policy changes.

## Next steps

- Use [Files and Folders](/safesquid_swg/files_and_folders/files_and_folders) to locate server-side evidence.
- Use [Supporting Services](/safesquid_swg/interface/supporting_services) to validate dependencies.
