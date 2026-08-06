---
title: "Deployment Planning"
description: "Size and prepare SafeSquid SWG infrastructure, routing, resilience, and evidence retention before installation."
keywords: ["SafeSquid deployment planning", "SafeSquid sizing", "SafeSquid hardware requirements", "proxy high availability", "secure web gateway planning"]
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
</Accordion>

## Size the first node

Use the first deployment as a measured pilot, not a blind production cutover.

| Deployment scale | Recommended planning focus |
| --- | --- |
| Pilot or branch | Prove traffic flow, activation, logs, and certificate trust with limited users |
| Single production node | Size CPU, RAM, disk I/O, NIC capacity, and log retention for peak sessions |
| High availability | Plan shared routing, health checks, same activation key, and synchronized configuration |
| Disaster recovery | Preserve activation key, configuration backup, certificate material, and rebuild procedure |

Size conservatively when HTTPS inspection, malware scanning, DLP, or detailed logging is enabled. These controls add security value, but they also increase CPU, memory, and disk-write demand.

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

<Accordion title="NIC, LACP, and routing checks">
  Use one interface for simple pilot deployments unless a separate management or high-availability design has been approved. For production networks with bonded interfaces, confirm switch-side LACP configuration, VLAN tagging, MTU, gateway selection, and failover behavior before routing users.

  Evidence should include interface names, MAC addresses, bond mode, switch ports, VLAN IDs, and the owner of any routing or firewall policy that forwards traffic toward SafeSquid.
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
    <Card title="Cluster or DR design" icon="refresh-cw" href="/admin_guide/scaling_and_high_availability/proxy_clustering">
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
| --- | --- | --- |
| Sizing cannot be approved | User, throughput, or inspection scope is unknown | Run a pilot and record peak concurrent connections before production sizing |
| Logs cannot be retained | Disk or SIEM ownership is unclear | Assign retention owner and capacity target before installation |
| HTTPS rollout stalls | Root CA deployment path is missing | Choose GPO, MDM, or approved manual trust deployment before enabling inspection |
| HA design is unclear | Failover and synchronization requirements are undefined | Document routing, health checks, same-key activation, and restore steps |

## Next steps

- [Prerequisites](/getting_started/install_safesquid/prerequisites) - convert the plan into install readiness checks.
- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - build a standard appliance.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - plan the first pilot route.