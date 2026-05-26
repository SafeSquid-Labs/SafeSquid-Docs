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

- Hardware or VM sizing matches [Deployment Planning](/getting_started/deployment_planning).
- SAB deployments meet the appliance baseline: `8+` CPU cores, `8 GB+` RAM, `4+` NICs, and `50 GB+` disk.
- Debian 13 is the primary baseline for new appliance deployments.
- Current Ubuntu LTS is supported in parallel where selected.
- Root or sudo access is available for installation and service validation.

## Validate network readiness

Confirm:

- Static SafeSquid IP, gateway, DNS, and NTP source are assigned.
- Client networks can reach the proxy listener, usually `8080/tcp`.
- Management access is limited to administrator networks.
- Outbound access exists for licensing, updates, and subscribed intelligence services.
- Direct client egress is controlled where mandatory proxy enforcement is required.

## Validate identity and trust

Confirm:

- Activation key is available from the [Self-Service Portal](https://key.safesquid.com).
- Directory integration owner is assigned if authentication is in scope.
- Root CA deployment method is selected before SSL inspection testing.
- Reporting Service or SIEM owner is assigned for audit evidence.
- Rollback owner is named for routing, proxy settings, and firewall changes.

## Choose the install method

| Environment | Recommended method | Operational responsibility |
|---|---|---|
| New bare metal server | [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) | Standard appliance deployment |
| New VM | [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) | Repeatable appliance build |
| Public or private cloud | [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) | Cloud networking, storage, and ingress controls |
| Existing Linux host | [Linux Server](/getting_started/install_safesquid/linux_server) | Local OS hardening, services, monitoring, and rollback |

For most new deployments, start with SafeSquid Appliance Builder.

## Verify prerequisite evidence

Capture:

- Sizing decision and expected peak concurrent connections.
- Static network parameters.
- Firewall approvals.
- Activation key ownership record.
- Certificate rollout path.
- Log retention and forwarding plan.
- Rollback procedure for client routing.

## Next steps

- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - deploy the standard appliance path.
- [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) - deploy in a cloud network.
- [Linux Server](/getting_started/install_safesquid/linux_server) - install on an existing supported Linux host.

