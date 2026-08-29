---
title: Resource Planning
description: Decide what to measure before sizing a SafeSquid node, and record the capacity inputs that drive CPU, memory, storage, and network decisions.
keywords:
  - SafeSquid capacity inputs
  - proxy resource planning
  - deployment sizing worksheet
  - concurrent connections
  - pilot sizing
---

# Measure Before You Size

Sizing from a user count alone produces a node that passes a demo and drops sessions at 09:30. The inputs that actually drive capacity — peak concurrency, inspection scope, and log volume — are measurable, and a short pilot measures them far more cheaply than a production rollback does.

This page decides what to record. [Sizing](/deployment/sizing) turns those numbers into hardware.

## Capture deployment requirements

Record these inputs before choosing an installation path:

- User count and expected concurrent users.
- Peak web throughput and business-hour traffic patterns.
- Expected HTTPS inspection scope.
- Authentication source and group-policy requirements.
- Log retention target and SIEM or reporting destination.
- Availability target for internet egress.
- Rollback method for client proxy settings and routing.

## Match the plan to the deployment scale

Use the first deployment as a measured pilot, not a blind production cutover.

| Deployment scale | Recommended planning focus |
|---|---|
| Pilot or branch | Prove traffic flow, activation, logs, and certificate trust with limited users |
| Single production node | Size CPU, RAM, disk I/O, NIC capacity, and log retention for peak sessions |
| High availability | Plan shared routing, health checks, same activation key, and synchronized configuration |
| Disaster recovery | Preserve activation key, configuration backup, certificate material, and rebuild procedure |

Size conservatively when HTTPS inspection, [malware scanning](/use_cases/malware_scanning/malware_scanners), [DLP](/use_cases/data_leakage_prevention/data_leakage_prevention), or detailed logging is enabled. These controls add security value, but they also increase CPU, memory, and disk-write demand — a node sized for plain forwarding will not carry the same user count once inspection is on.

<Accordion title="Capacity factors to record">
  Include these values in the sizing worksheet:

  - Concurrent users and concurrent connections during peak hours.
  - Expected inspected HTTPS percentage.
  - Malware scanning and DLP scope.
  - Average and peak bandwidth.
  - Cache usage expectations.
  - Log volume, reporting retention, and SIEM forwarding rate.
  - Support-bundle and packet-capture storage needed during incidents.
</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Verify and document for audits */}

<Accordion title="Post-install baseline and stress test">
  Pre-install connectivity checks prove the host can reach what it needs. They do not prove the host can carry the load you sized it for. Run a baseline after installation, before production users arrive, so you have a known-good reference to compare against during a later incident.

  **Establish a light-load baseline.** Record session latency from `/var/log/safesquid/extended.log`, CPU utilisation, and disk I/O wait while a small number of clients browse. Keep the figures with the deployment record — the absolute values matter less than having a comparison point.

  **Stress test to the sizing target.** Simulate the peak concurrent connections you sized for, using a load generator configured for HTTP proxy mode such as JMeter, or multiple concurrent browser sessions driven by Selenium. Confirm session counts hold without dropped connections.

  **Check logs during and after the run:**

  ```bash
  journalctl -u safesquid --no-pager | tail -50
  ```

  Expected result: no resource-exhaustion warnings or connectivity errors during the load window.

  **If the test fails, read the symptom:**

  | Symptom | Likely cause |
  |---|---|
  | CPU saturates well below the target connection count | Undersized CPU, or a CPU without AES-NI under HTTPS inspection |
  | Sustained high disk I/O wait | SATA-attached storage where NVMe is required |
  | Connections drop while CPU and disk are healthy | NIC saturation, or bonding configured on the host but not the switch |

  Document the sizing decision, topology diagram, and stress-test result for change control and compliance review.

</Accordion>

## Capture planning evidence

Store these artifacts:

- Sizing worksheet or change record.
- Network placement diagram.
- Firewall and routing approval.
- Log retention target.
- Activation key storage reference.
- Rollout and rollback plan.
- DR or rebuild assumptions.

## Troubleshoot planning gaps

| Symptom | Likely cause | Fix |
|---|---|---|
| Sizing cannot be approved | User, throughput, or inspection scope is unknown | Run a pilot and record peak concurrent connections before production sizing |
| Node passes the pilot and fails in production | Pilot ran without inspection enabled | Re-measure with the production control set active, not just the proxy path |
| Logs cannot be retained | Disk or SIEM ownership is unclear | Assign a retention owner and capacity target before installation |
| HA design is unclear | Failover and synchronization requirements are undefined | Document routing, health checks, same-key activation, and restore steps |

## Next steps

- [Sizing](/deployment/sizing) - convert these inputs into CPU, memory, and NIC decisions.
- [Pilot Versus Production](/deployment/pilot_versus_production) - decide what the first deployment has to prove.
- [Log-Retention Planning](/deployment/log_retention_planning) - set the storage target that sizing depends on.
