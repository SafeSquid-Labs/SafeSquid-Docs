---
title: Logging and Reporting
description: Confirm SafeSquid access logs are being written, retained, forwarded, and reportable before the deployment is treated as audit-ready.
keywords:
  - SafeSquid access log
  - extended.log verification
  - SIEM log forwarding
  - proxy audit evidence
  - deployment validation
---

# Prove the Audit Trail Exists

Enforcement you cannot evidence is enforcement you cannot defend. A deployment that blocks correctly but logs nothing fails the review that matters — and the gap is usually discovered during an incident, when the logs for the window in question turn out never to have been written or forwarded.

Confirm the evidence path end to end before declaring the deployment ready.

## Validate prerequisites

Confirm:

- [Proxy Connectivity](/deployment/proxy_connectivity) passes, so requests are reaching the log.
- The log-retention target and its owner are recorded. Use [Log-Retention Planning](/deployment/log_retention_planning) if this is not yet agreed.
- Time synchronisation is working, so log timestamps match incident timelines.
- Where forwarding is required, the SIEM or syslog destination is reachable and owned.

## Confirm logs are being written

On the SafeSquid server:

```bash
ls -l /var/log/safesquid/access/
```

Expected result: `extended.log` exists and its modification time is current.

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: recent entries record source, destination, timestamp, user where authentication is configured, matched policy, and action.

A log file with an old modification time while traffic is flowing means writes are failing or the path changed. Check disk capacity first — a full log volume truncates evidence silently.

## Confirm retention and forwarding

Check the volume that holds the logs:

```bash
df -h /var/log/safesquid
```

Expected result: free capacity is consistent with the agreed retention target, with headroom for support bundles and packet captures during an incident.

Where logs are forwarded, confirm arrival at the destination rather than departure from the host. A forwarder that is running is not proof that anything is being received.

## Confirm reports load

Open the [Configuration Portal](/safesquid_swg/interface/configuration_portal) and load a report covering the test window.

Expected result: the report renders and its contents match the access-log entries generated during validation.

Empty reports with healthy access logs mean the reporting path — not the proxy — is broken. Verify access logs first, then the reporting integration.

{/* source: _migration_source_v3/docs/01-Getting_Started/06-Verify_Your_Setup.md §SafeSquid Integration Validation */}

<Accordion title="Operations and monitoring checklist">

- [ ] `/var/log/safesquid/` contains current access logs.
- [ ] The host reaches its update servers.
- [ ] An update schedule is defined, whether automatic or manual.
- [ ] Log forwarding to the monitoring or SIEM platform works, where configured.
- [ ] Reports load in the Configuration Portal.

</Accordion>

## Capture logging evidence

Store these artifacts with the deployment record:

- Access-log entries from `/var/log/safesquid/access/extended.log` covering the validation window.
- `df -h` output for the log volume against the agreed retention target.
- Proof of receipt at the SIEM or syslog destination, where forwarding is configured.
- A report exported from the Configuration Portal for the same window.
- The named owner of log retention and the review cadence.

This evidence supports SOC 2 change management, ISO 27001 operational control review, and NIST SP 800-53 audit traceability for first deployment.

## Troubleshoot logging failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Log file exists but is not growing | Log volume is full, or the write path changed | Check `df -h`, free capacity, and restart the service; confirm entries resume |
| Entries appear without usernames | Authentication is not configured or not matching | Confirm identity integration before relying on user-attributed evidence |
| Reports are empty, access logs are healthy | Reporting integration is not connected | Verify access logs first, then the Reporting Service connection |
| Forwarded logs never arrive | Forwarder is running but the destination rejects or drops them | Confirm receipt at the destination, not just forwarder state |
| Timestamps do not match other systems | NTP is unset or drifting | Fix time synchronisation before correlating evidence across systems |

## Next steps

- [Log-Retention Planning](/deployment/log_retention_planning) - set the retention target this evidence has to meet.
- [Reporting Service](/safesquid_swg/interface/reporting_service) - connect and operate reporting.
- [Production-Readiness Checklist](/getting_started/verify_your_setup) - close out the full validation sequence.
