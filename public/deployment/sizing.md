---
title: CPU, Memory, Storage, and Throughput Sizing
description: Convert peak concurrent connections into CPU, RAM, NIC, and storage decisions for a SafeSquid node, including the AES-NI requirement and NVMe write path.
keywords:
  - SafeSquid sizing matrix
  - proxy hardware requirements
  - concurrent connections sizing
  - AES-NI HTTPS inspection
  - NVMe log storage
---

# Size Against Peak, Not Average

Averages hide the burst that drops sessions. A node sized for the mean sails through the working day and fails between 09:00 and 11:00, when every browser tab, background application, and API client opens connections at once.

Bring the inputs from [Resource Planning](/deployment/resource_planning) before using this page.

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

## Require AES-NI

A CPU without AES-NI decrypts SSL 3 to 5 times slower, which produces latency spikes and dropped connections under HTTPS inspection load. Verify before committing to hardware:

```bash
grep -m1 aes /proc/cpuinfo
```

Expected result: the flags line includes `aes`. An empty result means this CPU should not carry an inspecting proxy.

## Estimate connections from user counts

Assume 3 to 5 concurrent connections per active user at peak. Heavy SaaS or streaming environments reach 6 to 8.

For example, 200 active users at 5 connections each is 1,000 concurrent connections, which maps to 8 cores and 16 GB above.

Average session duration is typically 3 to 5 minutes, with peaks between 09:00 and 11:00 and between 14:00 and 16:00. Size for the peak window, not the daily mean.

**Above 4,000 concurrent connections**, assign multiple WAN IP addresses to avoid outbound NAT pool exhaustion, and evaluate [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) rather than a single larger node.

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

## Capture sizing evidence

Store these artifacts with the deployment record:

- The peak concurrent-connection figure and how it was measured or estimated.
- The matrix row chosen, and the inspection scope it assumes.
- `grep aes /proc/cpuinfo` output for the target CPU.
- Storage attachment type for each of the three write paths.
- Bond mode, switch ports, and VLAN IDs where bonding is used.

## Troubleshoot sizing failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Latency spikes under HTTPS load | CPU lacks AES-NI | Confirm with `grep aes /proc/cpuinfo`; replace the CPU rather than reducing inspection scope |
| Sustained disk I/O wait | SATA-attached storage on a write path that needs NVMe | Move `/var/log/safesquid`, `/var/db/safesquid`, and `/var/lib/safesquid` to PCIe-attached NVMe |
| Connections drop while CPU and disk are healthy | NIC saturation, or host bond without switch-side LACP | Verify switch configuration matches the host bond, then re-test |
| Outbound connections fail above ~4,000 concurrent | NAT pool exhaustion on a single WAN IP | Assign additional WAN addresses, or cluster instead of scaling the node |
| Node meets the matrix but still drops sessions | Sized against average, not peak | Re-measure during the 09:00-11:00 window and resize |

## Next steps

- [Resource Planning](/deployment/resource_planning) - revisit the inputs if a figure here cannot be met.
- [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) - scale out rather than up above 4,000 connections.
- [Log-Retention Planning](/deployment/log_retention_planning) - size the log volume deliberately.
