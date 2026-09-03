---
title: Deployment Checklist
description: Confirm host, network, trust, licensing, and evidence requirements are satisfied and owned before running any SafeSquid installer.
keywords:
  - SafeSquid prerequisites
  - deployment checklist
  - installation readiness
  - site survey
  - proxy deployment requirements
---

# Confirm Readiness Before Install

Most failed SafeSquid pilots are caused by missing prerequisites: wrong sizing, blocked proxy ports, no DNS or NTP, no activation key, or no plan for Root CA deployment. Every one of them is cheaper to fix now than during the cutover window.

Work this checklist to completion before starting any installer.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Pre-Installation Checklist (Site Survey) */}

<Accordion title="Site survey checklist">
  Capture the current egress path before selecting a SafeSquid design:

  - Internet circuits, firewalls, NAT devices, and cloud egress points.
  - User networks, server networks, guest networks, VPN users, and remote branches.
  - Existing proxy, PAC, WPAD, DNS, and browser-management policies.
  - Authentication sources, group naming, privileged-user exceptions, and service accounts.
  - Internal destinations that must bypass proxy inspection.
  - Current log destinations, SIEM ownership, and incident-retention requirements.

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

## Validate platform readiness

Confirm:

- CPU, RAM, disk, and NIC allocation match the sizing plan from [Hardware Sizing](/deployment/hardware_sizing).
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

The specific ports, endpoints, and source scopes are listed in [Ports and Firewall Rules](/deployment/ports_and_firewall_rules). Agree them with the network owner before installation.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Prepare the host before install, step 8 */}

<Accordion title="Mandatory access controls: SELinux and AppArmor">
  SELinux or AppArmor in enforcing mode can block proxy operations during initial setup, and the failure presents as unexplained permission errors rather than a clear policy denial.

  Set permissive mode for the setup window, or author a policy that covers SafeSquid before you start:

  ```bash
  getenforce
  ```

  Expected result: the current mode is known and recorded before installation begins.

  Once the deployment is operational, review the audit log and write a targeted policy rather than leaving mandatory access control permanently disabled. Record which choice was made and who owns the follow-up; "temporarily permissive" that is never revisited is a finding waiting to happen.
</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Prepare the host before install, steps 6-7 */}

<Accordion title="Firewall ports to open">
  Agree these rules with the network owner before installation. Each has a named source scope; none should be opened to `0.0.0.0/0`.

  **Inbound to the SafeSquid host**

  | Port | Protocol | Purpose | Restrict to |
  |---|---|---|---|
  | `8080` | TCP | HTTP proxy listener | Approved client networks |
  | `8443` | TCP | Management interface | Administrator workstations only |
  | `53` | TCP/UDP | DNS, when integrated DNS security is used | Approved client networks |

  **Outbound from the SafeSquid host**

  | Port | Purpose |
  |---|---|
  | `80`, `443` | Web access on behalf of clients, plus update and subscription paths |
  | `53` | Upstream DNS resolution |

  The specific licensing, update, and categorization hosts that must be reachable on 80 and 443 are listed in [Ports and Firewall Rules](/deployment/ports_and_firewall_rules) and [Activate Your License](/getting_started/activate).
</Accordion>

## Validate identity and trust

Confirm:

- Activation key is available from [Register and Get Your Key](/getting_started/register).
- Root CA rollout owner is assigned for HTTPS inspection.
- Authentication source is known if user-based policy will be enabled.
- Log-retention owner is assigned. See [Log-Retention Planning](/deployment/log_retention_planning).
- Change and rollback owners are named.

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
| Host cannot resolve portal names | DNS is missing or blocked | Fix DNS before installation; every later step depends on it |
| Time is wrong | NTP is blocked or unset | Configure NTP before activation and logging tests |
| Proxy port is exposed too broadly | Firewall rule is unsafe | Restrict source networks; see [Ports and Firewall Rules](/deployment/ports_and_firewall_rules) |
| Activation key is missing | Registration is incomplete | Complete [Register and Get Your Key](/getting_started/register) before installing |
| A checklist item has no owner | Ownership was assumed, not assigned | Assign it now; unowned prerequisites are what stall the rollout later |

## Next steps

- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - install the standard appliance.
- [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) - deploy in a cloud network.
- [Linux Server Install](/getting_started/install_safesquid/linux_server) - install on an existing Linux host.
