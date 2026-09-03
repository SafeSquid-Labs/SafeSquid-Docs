---
title: Hardware Sizing
description: Decide what to measure, then convert peak concurrent connections into CPU, RAM, NIC, and storage decisions for a SafeSquid node, including the AES-NI requirement and NVMe write path.
keywords:
  - SafeSquid capacity inputs
  - SafeSquid sizing matrix
  - proxy hardware requirements
  - AES-NI HTTPS inspection
  - NVMe log storage
  - concurrent connections sizing
---

# Size Against Peak, Not Average

Averages hide the burst that drops sessions. A node sized for the mean sails through the working day and fails between 09:00 and 11:00, when every browser tab, background application, and API client opens connections at once. Sizing from a user count alone produces a node that passes a demo and drops sessions at 09:30.

The inputs that actually drive capacity — peak concurrency, inspection scope, and log volume — are measurable, and a short pilot measures them far more cheaply than a production rollback does.

## Measure before you size

Record these inputs before choosing an installation path:

- User count and expected concurrent users.
- Peak web throughput and business-hour traffic patterns.
- Expected HTTPS inspection scope.
- Authentication source and group-policy requirements.
- Log retention target and SIEM or reporting destination.
- Availability target for internet egress.
- Rollback method for client proxy settings and routing.

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

## Validate prerequisites

Confirm:

- Peak concurrent connections are measured or estimated, not assumed.
- The HTTPS inspection scope is known — it changes CPU demand substantially.
- The log retention target is agreed. Use [Log-Retention Planning](/deployment/log_retention_planning).
- The candidate CPU supports AES-NI.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Hardware sizing */}
{/* NEEDS-SME-REVIEW: connection ceilings below are undated in the source and predate the current build. Confirm before quoting to a customer. */}

## Read the sizing matrix

Size against **peak** concurrent connections, not average.

| CPU | RAM | NICs (minimum) | Max concurrent connections |
|---|---|---|---:|
| 4 cores | 8 GB | 2 x 1 Gbps | 400 |
| 8 cores | 16 GB | 2 x 1 Gbps | 1,500 |
| 16 cores | 32 GB | 4 x 1 Gbps | 3,000 |
| 24 cores | 64 GB | 8 x 1 Gbps | 4,000 |
| 32 cores | 64 GB | 8 x 1 Gbps | 6,000 |
| 64 cores | 128 GB | 16 x 1 Gbps | 8,000 |

NIC counts are minimums. See the bonding guidance below.

<Accordion title="Estimate concurrent connections from a user count instead of measured peak data">
  Assume 3 to 5 concurrent connections per active user at peak. Heavy SaaS or streaming environments reach 6 to 8.

  For example, 200 active users at 5 connections each is 1,000 concurrent connections, which maps to 8 cores and 16 GB above.

  Average session duration is typically 3 to 5 minutes, with peaks between 09:00 and 11:00 and between 14:00 and 16:00. Size for the peak window, not the daily mean.

  **Above 4,000 concurrent connections**, assign multiple WAN IP addresses to avoid outbound NAT pool exhaustion, and evaluate [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) rather than a single larger node.
</Accordion>

## Require AES-NI

A CPU without AES-NI decrypts SSL 3 to 5 times slower, which produces latency spikes and dropped connections under HTTPS inspection load. Verify before committing to hardware:

```bash
grep -m1 aes /proc/cpuinfo
```

Expected result: the flags line includes `aes`. An empty result means this CPU should not carry an inspecting proxy.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Disk and log storage */}

## Choose the storage media

SafeSquid writes continuously for session logging, behavioural analysis, and threat detection. Storage media choice is a correctness concern, not only a performance one: when writes fall behind, log entries are delayed or missed, and the audit trail you depend on during an incident has holes in it.

**Use NVMe SSDs** — M.2 or PCIe-attached — for these paths:

| Path | Holds |
|---|---|
| `/var/log/safesquid` | Access, extended, and service logs |
| `/var/db/safesquid` | Database files |
| `/var/lib/safesquid` | Runtime state and cache |

SATA-connected SSDs have substantially lower write throughput than PCIe-attached NVMe and cause logging delays and missed entries under load. Verify the attachment type, not just the label "SSD".

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Link aggregation (LACP) */}

<Accordion title="NIC, LACP, and routing checks">
  Use one interface for simple pilot deployments unless a separate management or high-availability design has been approved. For production networks with bonded interfaces, confirm switch-side LACP configuration, VLAN tagging, MTU, gateway selection, and failover behavior before routing users.

  Evidence should include interface names, MAC addresses, bond mode, switch ports, VLAN IDs, and the owner of any routing or firewall policy that forwards traffic toward SafeSquid.

  Link Aggregation Control Protocol (LACP) bonding combines physical interfaces into one logical link for bandwidth and redundancy. Without bonding, a single failed NIC can take the proxy offline entirely.

  Match the bonding layout to the number of physical ports available:

  | Physical ports | Recommended bonding configuration |
  |---|---|
  | 2 | One active-backup bond |
  | 4 | Two bonded pairs |
  | 8 | Two four-port bonds |
  | 16 | Two eight-port LACP bonds |

  Bonding is configured on both the host and the switch. A host-side bond without matching switch-side configuration fails open or drops frames, so treat the switch change as part of the same change record.
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

## Capture sizing evidence

Store these artifacts with the deployment record:

- The peak concurrent-connection figure and how it was measured or estimated.
- The matrix row chosen, and the inspection scope it assumes.
- `grep aes /proc/cpuinfo` output for the target CPU.
- Storage attachment type for each of the three write paths.
- Bond mode, switch ports, and VLAN IDs where bonding is used.
- Network placement diagram and firewall/routing approval.
- Rollout and rollback plan, and DR or rebuild assumptions.

## Troubleshoot sizing failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Sizing cannot be approved | User, throughput, or inspection scope is unknown | Run a pilot and record peak concurrent connections before production sizing |
| Node passes the pilot and fails in production | Pilot ran without inspection enabled | Re-measure with the production control set active, not just the proxy path |
| Latency spikes under HTTPS load | CPU lacks AES-NI | Confirm with `grep aes /proc/cpuinfo`; replace the CPU rather than reducing inspection scope |
| Sustained disk I/O wait | SATA-attached storage on a write path that needs NVMe | Move `/var/log/safesquid`, `/var/db/safesquid`, and `/var/lib/safesquid` to PCIe-attached NVMe |
| Connections drop while CPU and disk are healthy | NIC saturation, or host bond without switch-side LACP | Verify switch configuration matches the host bond, then re-test |
| Outbound connections fail above ~4,000 concurrent | NAT pool exhaustion on a single WAN IP | Assign additional WAN addresses, or cluster instead of scaling the node |
| Node meets the matrix but still drops sessions | Sized against average, not peak | Re-measure during the 09:00-11:00 window and resize |
| Logs cannot be retained | Disk or SIEM ownership is unclear | Assign a retention owner and capacity target before installation |

## Next steps

- [Log-Retention Planning](/deployment/log_retention_planning) - size the log volume deliberately against the retention target.
- [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) - scale out rather than up above 4,000 connections.
- [Choose an Architecture](/deployment/choose_an_architecture) - confirm placement before committing to hardware.
