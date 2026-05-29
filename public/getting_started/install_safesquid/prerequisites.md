---
title: Prerequisites
description: Confirm host, network, trust, licensing, and evidence requirements before installing SafeSquid SWG.
keywords:
  - SafeSquid prerequisites
  - SafeSquid installation readiness
  - proxy deployment prerequisites
  - SafeSquid network requirements
---

# Confirm Readiness Before Install

Most failed SafeSquid pilots are caused by missing prerequisites: wrong sizing, blocked proxy ports, no DNS or NTP, no activation key, or no plan for Root CA deployment. Validate these items before starting any installer.

## Validate platform readiness

Confirm:

- CPU, RAM, disk, and NIC allocation match the pilot or production sizing plan.
- Storage can handle access logs, reports, support bundles, and update files.
- The host has a stable hostname and static IP address.
- Administrative access is available through an approved management path.
- Backup, snapshot, or rebuild procedure is documented.

Do not start production installation on a temporary address or unmanaged host. That creates later certificate, logging, and routing rework.

## Validate network readiness

Confirm:

- DNS resolution works from the SafeSquid host network.
- NTP is reachable and synchronized.
- The approved proxy listener port is open only to intended client networks.
- Outbound access exists for activation, updates, category data, and subscription checks.
- The management path is restricted to approved administrators.

Use these quick checks before installation:

```bash
nslookup key.safesquid.com
ping -c 3 key.safesquid.com
```

Expected result: the host resolves and reaches the Self-Service Portal path needed for key and activation workflows.

## Validate identity and trust

Confirm:

- Activation key is available from [Register and Get Your Key](/getting_started/register).
- Root CA rollout owner is assigned for HTTPS inspection.
- Authentication source is known if user-based policy will be enabled.
- Log-retention owner is assigned.
- Change and rollback owners are named.

## Choose the install method

<Steps>
  <Step title="Choose a new appliance">
    <Card title="New appliance" icon="hard-drive" href="/getting_started/install_safesquid/safesquid_appliance_builder">
      Use SafeSquid Appliance Builder for a new VM or hardware appliance with a dedicated target disk.
    </Card>

    Confirm the target disk is dedicated and can be overwritten.

    If any existing workload must remain, do not use Appliance Builder.
  </Step>
  <Step title="Choose cloud or hybrid egress">
    <Card title="Cloud or hybrid egress" icon="cloud" href="/getting_started/install_safesquid/cloud_deployment">
      Use cloud deployment when security groups, route tables, snapshots, and egress paths are controlled.
    </Card>

    Confirm route tables, security groups, snapshots, and egress paths have named owners.

    If proxy exposure is broad, restrict source networks before rollout.
  </Step>
  <Step title="Choose a managed Linux host">
    <Card title="Managed Linux host" icon="terminal" href="/getting_started/install_safesquid/linux_server">
      Use Linux Server Install only when OS lifecycle, dependencies, monitoring, and rollback are owned.
    </Card>

    Confirm OS lifecycle, dependencies, monitoring, and rollback are documented.

    If host dependencies are unmanaged, rebuild with Appliance Builder.
  </Step>
</Steps>

## Verify prerequisite evidence

Store:

- Host resource allocation.
- Static IP and DNS record.
- NTP source.
- Firewall approval.
- Activation key storage reference.
- Root CA rollout owner.
- Log retention target.
- Rollback plan.

## Troubleshoot readiness failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Host cannot resolve portal names | DNS is missing or blocked | Fix DNS before installation |
| Time is wrong | NTP is blocked or unset | Configure NTP before activation and logging tests |
| Proxy port is exposed too broadly | Firewall rule is unsafe | Restrict source networks before deployment |
| Activation key is missing | Registration is incomplete | Complete [Register and Get Your Key](/getting_started/register) before installing |

## Next steps

- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - install the standard appliance.
- [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) - deploy in a cloud network.
- [Linux Server Install](/getting_started/install_safesquid/linux_server) - install on an existing Linux host.
