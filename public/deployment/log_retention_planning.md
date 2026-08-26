---
title: Log-Retention Planning
description: Set the SafeSquid log retention target, choose local versus forwarded storage, and size the log volume so enforcement evidence survives an incident.
keywords:
  - SafeSquid log retention
  - proxy audit trail
  - SIEM log forwarding
  - access log storage
  - compliance retention
---

# Decide How Long Evidence Survives

SafeSquid deployment evidence must survive troubleshooting and audit review. The default retention is shorter than most compliance regimes require, and a full log volume truncates evidence silently — the gap is discovered during an incident, when the window you need turns out to have rolled off.

Set the target before installation. Retention is a storage decision, and storage is a sizing input.

## Plan what has to be retained

- Local access logs under `/var/log/safesquid/access/`.
- Reporting Service or SIEM forwarding where required.
- Change records for activation, policy, Root CA rollout, and client routing.
- Time synchronization so log timestamps match incident timelines.
- Disk capacity for access logs, reports, support bundles, and packet captures used during incidents.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Disk and log storage */}

## Set the retention target

**Default local retention is 30 days.** For compliance regimes that require 90 days or more, forward logs rather than extending local disk alone:

- External syslog — rsyslog, Splunk, ELK.
- [Reporting Service](/safesquid_swg/interface/reporting_service).
- Cloud object storage such as S3 or Azure Blob.

Forwarding does not remove the need for local retention. Keep enough local history to diagnose an outage and to recover from a forwarder failure — the forwarder is exactly what breaks during the incident you need the logs for.

<Accordion title="Disk and retention planning">
  Separate high-write log and cache storage where the deployment model allows it. For production nodes, record the retention target for:

  - `/var/log/safesquid/access/` access logs.
  - Configuration backups and exported reports.
  - Support bundles and temporary diagnostics.
  - OS logs, Monit logs, BIND9 logs, and package-manager logs.

  If logs are forwarded to a SIEM, still preserve enough local retention for outage diagnosis and forwarder-failure recovery.
</Accordion>

Monitor `/var/log/safesquid` usage on a schedule and alert before the volume fills. Storage media choice matters here too — see the NVMe write paths in [Sizing](/deployment/sizing).

**Missing:** daily log-volume estimates per deployment scale are not stated here. They exist in the legacy source but are undated and unverified against the current build, so the retention target cannot be converted into a disk figure from this documentation alone. Measure during the pilot, or escalate to the CTO before sizing storage from a number.

## Assign the ownership

Retention fails on ownership more often than on capacity. Record:

- Who owns the retention target and reviews it.
- Who owns the SIEM or syslog destination.
- Who is alerted when the log volume approaches capacity.
- Who confirms, after an incident, that the relevant window was actually retained.

## Capture retention evidence

Store these artifacts with the deployment record:

- The agreed retention target and the requirement that drove it.
- `df -h /var/log/safesquid` output against that target.
- The forwarding destination and proof of receipt, where configured.
- The named owner of retention and the review cadence.

## Troubleshoot retention gaps

| Symptom | Likely cause | Fix |
|---|---|---|
| Log volume fills without warning | No capacity alert configured | Add monitoring on `/var/log/safesquid` with an owner for the alert |
| Required window has rolled off | Local retention shorter than the compliance requirement | Forward logs, and raise local retention to cover outage diagnosis |
| Forwarded logs are incomplete | Forwarder failed during the incident window | Keep local retention as the fallback; confirm receipt, not just forwarder state |
| Timestamps do not correlate across systems | NTP is unset or drifting | Fix time synchronization before treating logs as correlated evidence |
| Retention target cannot be approved | No named owner for storage or SIEM | Assign the owner before installation, not at the first audit |

## Next steps

- [Logging and Reporting](/deployment/logging_and_reporting) - prove the evidence path works once deployed.
- [Sizing](/deployment/sizing) - convert the retention target into a storage decision.
- [Reporting Service](/safesquid_swg/interface/reporting_service) - connect reporting and forwarding.
