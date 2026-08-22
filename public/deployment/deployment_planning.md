---
title: Deployment Planning
description: Size and prepare SafeSquid SWG infrastructure, routing, resilience, and evidence retention before installation.
keywords:
  - SafeSquid deployment planning
  - SafeSquid sizing
  - SafeSquid hardware requirements
  - proxy high availability
  - secure web gateway planning
---

# Plan the Control Path First

SafeSquid becomes a production control only when the proxy is sized, reachable, monitored, and able to preserve enforcement evidence. Poor planning causes dropped sessions, weak audit trails, certificate failures, and emergency routing changes during rollout.

## Capture deployment requirements

Record these inputs before choosing an installation path:

- User count and expected concurrent users.
- Peak web throughput and business-hour traffic patterns.
- Expected HTTPS inspection scope.
- Authentication source and group-policy requirements.
- Log retention target and SIEM or reporting destination.
- Availability target for internet egress.
- Rollback method for client proxy settings and routing.

<Accordion title="Site survey checklist">
  Capture the current egress path before selecting a SafeSquid design:

  - Internet circuits, firewalls, NAT devices, and cloud egress points.
  - User networks, server networks, guest networks, VPN users, and remote branches.
  - Existing proxy, PAC, WPAD, DNS, and browser-management policies.
  - Authentication sources, group naming, privileged-user exceptions, and service accounts.
  - Internal destinations that must bypass proxy inspection.
  - Current log destinations, SIEM ownership, and incident-retention requirements.

  {/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Pre-Installation Checklist (Site Survey) */}

  Record these named values before installation starts. Each one blocks a specific install or activation step if it is missing:

  **Portal and keys**

  - Registered email on the Self-Service Portal.
  - C-Code, required for license generation.
  - Activation key, downloaded to the administrator workstation.
  - Root CA certificate decision: self-signed or enterprise-issued, for HTTPS inspection.

  **Network parameters**

  - Proxy hostname or FQDN, for example `proxy.example.com`.
  - Proxy IP address and CIDR, for example `10.200.5.100/24`.
  - Default gateway address.
  - Primary and secondary DNS servers.

  **Directory integration**

  - AD or LDAP server IP address or FQDN.
  - Bind account in UPN format, with its password held under approved credential handling.
  - Base DN, for example `dc=example,dc=com`.
  - LDAP domain name.
</Accordion>

## Size the first node

Use the first deployment as a measured pilot, not a blind production cutover.

| Deployment scale | Recommended planning focus |
|---|---|
| Pilot or branch | Prove traffic flow, activation, logs, and certificate trust with limited users |
| Single production node | Size CPU, RAM, disk I/O, NIC capacity, and log retention for peak sessions |
| High availability | Plan shared routing, health checks, same activation key, and synchronized configuration |
| Disaster recovery | Preserve activation key, configuration backup, certificate material, and rebuild procedure |

Size conservatively when HTTPS inspection, malware scanning, DLP, or detailed logging is enabled. These controls add security value, but they also increase CPU, memory, and disk-write demand.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Hardware sizing */}
{/* NEEDS-SME-REVIEW: connection ceilings below are undated in the source and predate the current build. Confirm before quoting to a customer. */}

### Sizing matrix by peak concurrent connections

Size against **peak** concurrent connections, not average. Averages hide the burst that drops sessions.

| CPU | RAM | NICs (minimum) | Max concurrent connections |
|---|---|---|---:|
| 4 cores | 8 GB | 2 x 1 Gbps | 400 |
| 8 cores | 16 GB | 2 x 1 Gbps | 1,500 |
| 16 cores | 32 GB | 4 x 1 Gbps | 3,000 |
| 24 cores | 64 GB | 8 x 1 Gbps | 4,000 |
| 32 cores | 64 GB | 8 x 1 Gbps | 6,000 |
| 64 cores | 128 GB | 16 x 1 Gbps | 8,000 |

NIC counts are minimums. See the NIC, LACP, and routing checks below for bonding.

**Missing:** these connection ceilings are undated in the legacy source and predate the current build. Treat them as a starting point for a measured pilot, not as certified capacity — escalate to the CTO before quoting a figure to a customer.

**Require AES-NI.** A CPU without AES-NI decrypts SSL 3 to 5 times slower, which produces latency spikes and dropped connections under HTTPS inspection load. Verify with `grep -m1 aes /proc/cpuinfo` before committing to hardware.

**Estimating concurrent connections from user counts.** Assume 3 to 5 concurrent connections per active user at peak. Heavy SaaS or streaming environments reach 6 to 8. For example, 200 active users at 5 connections each is 1,000 concurrent connections, which maps to 8 cores and 16 GB above.

Each browser tab, background application, and API client opens its own connections. Average session duration is typically 3 to 5 minutes, with peaks between 09:00 and 11:00 and between 14:00 and 16:00.

**Above 4,000 concurrent connections**, assign multiple WAN IP addresses to avoid outbound NAT pool exhaustion, and evaluate [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) rather than a single larger node.

Use NVMe SSDs for log and cache volumes. See the disk and retention planning below.

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

## Design network placement

Choose where SafeSquid will intercept traffic:

- Explicit proxy for pilot clients and controlled validation.
- PAC file or managed OS proxy for browser rollout.
- Firewall or routing policy only when the network team can enforce bypass controls safely.
- Cloud egress placement for workloads or remote sites that already route through a cloud network.

Document source networks, proxy listener ports, DNS servers, NTP sources, upstream gateways, and firewall rules. SafeSquid cannot enforce policy on traffic that bypasses the proxy.

<Accordion title="Firewall and DNS readiness">
  Confirm these dependencies before installation:

  - Inbound proxy access is allowed only from approved client networks.
  - Management access is allowed only from approved administrator networks.
  - Outbound DNS, NTP, activation, subscription, update, category, certificate, and antivirus-signature paths are reviewed.
  - DNS resolution works for `key.safesquid.com`, `api.safesquid.net`, and `swgupdates2.safesquid.net`.
  - Firewall change records include owner, source CIDRs, destination services, test window, and rollback.
</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Firewall Whitelist Requirements */}
{/* NEEDS-SME-REVIEW: the itsecure.co.in and itonlinesecure.in categorization endpoints appear nowhere else in public/. Confirm they are current for the shipping release before an operator allowlists them. */}

<Accordion title="Outbound endpoint reference">
  The SafeSquid host needs outbound reachability for DNS resolution, license validation, categorization, and security updates.

  **DNS resolution (port 53)**

  Outbound DNS to the root servers `A.ROOT-SERVERS.NET` through `M.ROOT-SERVERS.NET`, or to the upstream resolvers your network team designates. SafeSquid cannot categorize or resolve destinations without it.

  **SafeSquid infrastructure**

  | Endpoint | Port | Purpose |
  |---|---:|---|
  | `key.safesquid.com` | `443` | License management and Self-Service Portal |
  | `api.safesquid.net` | `443` | License activation |
  | `swgupdates2.safesquid.net` | `443` | Software and package updates |
  | `swgupdates.safesquid.net` | `80` | Legacy update repository |
  | `sslupdates.safesquid.com` | `443` | SSL inspection and security updates |

  **URL categorization and classification**

  | Endpoint | Port |
  |---|---:|
  | `category.safesquid.net` | `443` |
  | `prourl.itsecure.co.in` | `8080` |
  | `encurl.itsecure.co.in` | `8080` |
  | `klassify.itsecure.co.in` | `8080` |
  | `prourl.itonlinesecure.in` | `8080` |

  **Antivirus signature updates**

  | Endpoint | Port |
  |---|---:|
  | `download.quickheal.com` | `80` |

  Treat this table as a deployment checklist, not a firewall exception template. Confirm current endpoint requirements through the approved release or support channel before production allowlisting.
</Accordion>

<Accordion title="NIC, LACP, and routing checks">
  Use one interface for simple pilot deployments unless a separate management or high-availability design has been approved. For production networks with bonded interfaces, confirm switch-side LACP configuration, VLAN tagging, MTU, gateway selection, and failover behavior before routing users.

  Evidence should include interface names, MAC addresses, bond mode, switch ports, VLAN IDs, and the owner of any routing or firewall policy that forwards traffic toward SafeSquid.

  {/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Link aggregation (LACP) */}

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

## Plan logs and evidence

SafeSquid deployment evidence must survive troubleshooting and audit review. Plan for:

- Local access logs under `/var/log/safesquid/access/`.
- Reporting Service or SIEM forwarding where required.
- Change records for activation, policy, Root CA rollout, and client routing.
- Time synchronization so log timestamps match incident timelines.
- Disk capacity for access logs, reports, support bundles, and packet captures used during incidents.

<Accordion title="Disk and retention planning">
  Separate high-write log and cache storage where the deployment model allows it. For production nodes, record the retention target for:

  - `/var/log/safesquid/access/` access logs.
  - Configuration backups and exported reports.
  - Support bundles and temporary diagnostics.
  - OS logs, Monit logs, BIND9 logs, and package-manager logs.

  If logs are forwarded to a SIEM, still preserve enough local retention for outage diagnosis and forwarder-failure recovery.
</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Disk and log storage */}

<Accordion title="Storage media and retention defaults">
  SafeSquid writes continuously for session logging, behavioural analysis, and threat detection. Storage media choice is a correctness concern, not only a performance one: when writes fall behind, log entries are delayed or missed, and the audit trail you depend on during an incident has holes in it.

  **Use NVMe SSDs** — M.2 or PCIe-attached — for these paths:

  | Path | Holds |
  |---|---|
  | `/var/log/safesquid` | Access, extended, and service logs |
  | `/var/db/safesquid` | Database files |
  | `/var/lib/safesquid` | Runtime state and cache |

  SATA-connected SSDs have substantially lower write throughput than PCIe-attached NVMe and cause logging delays and missed entries under load. Verify the attachment type, not just the label "SSD".

  **Default local retention is 30 days.** For compliance regimes that require 90 days or more, forward logs rather than extending local disk alone:

  - External syslog — rsyslog, Splunk, ELK.
  - [Reporting Service](/safesquid_swg/interface/reporting_service).
  - Cloud object storage such as S3 or Azure Blob.

  Monitor `/var/log/safesquid` usage on a schedule. A full log volume truncates evidence silently.

  **Missing:** per-scale disk capacity figures and daily log-volume estimates are not stated here — they exist in the legacy source but are undated and unverified against the current build. Escalate to the CTO before sizing storage from a number.
</Accordion>

## Choose deployment scenario

<Steps>
  <Step title="Choose new appliance deployment">
    <Card title="New VM or hardware appliance" icon="hard-drive" href="/getting_started/install_safesquid/safesquid_appliance_builder">
      Use the Appliance Builder when a dedicated disk and bootable ISO workflow are approved.
    </Card>

    Confirm the appliance has approved CPU, RAM, disk, NIC, and rebuild ownership.

    If the disk cannot be dedicated, choose cloud or managed Linux instead.
  </Step>
  <Step title="Choose cloud or hybrid egress">
    <Card title="Cloud or hybrid egress" icon="cloud" href="/getting_started/install_safesquid/cloud_deployment">
      Use cloud deployment when security groups, route tables, snapshots, and egress paths are owned.
    </Card>

    Confirm security groups, routes, snapshots, and egress paths have named owners.

    If egress ownership is unclear, pause deployment until network ownership is assigned.
  </Step>
  <Step title="Choose managed Linux server">
    <Card title="Existing managed Linux server" icon="terminal" href="/getting_started/install_safesquid/linux_server">
      Use Linux install only when OS hardening, dependencies, monitoring, and rollback are already owned.
    </Card>

    Confirm OS lifecycle and rollback are approved by the server owner.

    If dependency drift is likely, use Appliance Builder for a cleaner baseline.
  </Step>
  <Step title="Choose cluster or DR design">
    <Card title="Cluster or DR design" icon="refresh-cw" href="/use_cases/scaling_and_high_availability/proxy_clustering">
      Add HA or DR planning when uptime requirements need failover, configuration sync, and tested restore.
    </Card>

    Confirm RTO, RPO, failover, restore, and configuration-sync requirements are documented.

    If HA ownership is missing, keep the first deployment single-node until DR controls are approved.
  </Step>
</Steps>

<Accordion title="Disaster recovery checks">
  Before declaring production readiness, confirm:

  - Activation key storage is recoverable without exposing the key contents.
  - Configuration backup and restore are tested.
  - Root CA material, if used, is backed up according to certificate-handling policy.
  - Rebuild steps exist for appliance, cloud, or Linux deployment.
  - DNS, PAC, GPO, MDM, firewall, and route rollback owners are named.
  - A second node or restore target can use the same activation context when cluster or DR behavior requires it.
</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Disaster recovery */}

<Accordion title="Disaster recovery site design">
  A DR stack keeps web security enforced during a regional outage. Without one, a site failure removes the control rather than degrading it, and users either lose internet access or get it unfiltered.

  **Site requirements**

  - **Geography** — a different city, data centre, and power grid than primary. Co-locating the DR stack with production negates continuity.
  - **Capacity** — mirror production sizing across CPU, RAM, NICs, and disk. The DR site carries full load during failover, not a fraction of it.
  - **Configuration** — replicate policy through [Configuration Sync](/use_cases/customisation/configuration_sync) or a documented manual procedure.

  **Recovery objectives**

  - **RTO (Recovery Time Objective)** — how long it may take to redirect traffic to the DR site.
  - **RPO (Recovery Point Objective)** — how much policy and configuration lag is acceptable. Real-time sync approaches zero; manual replication does not.

  **Failover methods**

  | Method | How it works |
  |---|---|
  | DNS-based | Repoint A records at the DR address; recovery time is bounded by record TTL |
  | BGP Anycast | Advertise the same address from the DR site |
  | Load-balancer health check | Balancer withdraws the failed site and redirects automatically |

  Set the RTO and RPO targets with the business, then test failover on a schedule and keep the result as audit evidence. Quarterly is a common cadence.

  **Missing:** recovery-time figures per failover method are not stated here — the legacy source gives numbers, but they are undated and unverified. Escalate to the CTO for SLA-style claims, consistent with [Disaster Recovery](/use_cases/scaling_and_high_availability/disaster_recovery).
</Accordion>

## Verify readiness

Run these checks before installation:

```bash
ping -c 3 key.safesquid.com
nslookup key.safesquid.com
```

Expected result: DNS resolves and the host can reach the Self-Service Portal path required for activation-key workflows.

Also confirm:

- DNS and NTP are reachable from the SafeSquid host network.
- Firewall rules allow required outbound update and subscription paths.
- Proxy listener ports are approved.
- Root CA deployment owner is assigned.
- Rollback owners exist for routing, PAC, GPO, MDM, and firewall changes.

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

  **Missing:** target thresholds for latency, CPU headroom, and I/O wait are not stated here — the legacy source gives figures, but they are undated and unverified against the current build. Escalate to the CTO before treating any number as a pass or fail line.
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
| Logs cannot be retained | Disk or SIEM ownership is unclear | Assign retention owner and capacity target before installation |
| HTTPS rollout stalls | Root CA deployment path is missing | Choose GPO, MDM, or approved manual trust deployment before enabling inspection |
| HA design is unclear | Failover and synchronization requirements are undefined | Document routing, health checks, same-key activation, and restore steps |

## Next steps

- [Prerequisites](/getting_started/install_safesquid/prerequisites) - convert the plan into install readiness checks.
- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - build a standard appliance.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - plan the first pilot route.
