---
title: Install SafeSquid
description: Installation path for deploying SafeSquid SWG on an appliance build, cloud instance, or existing Linux server.
keywords:
  - install safesquid
  - SafeSquid documentation
  - SafeSquid Appliance Builder
  - cloud deployment
  - Linux server install
---

# Install SafeSquid on the Right Platform

Installation quality determines whether SafeSquid can inspect traffic safely under production load. Pick the deployment method that matches your ownership model, then verify service health before routing users.

## Choose the install path

| Environment | Recommended path | Production concern |
|---|---|---|
| New bare metal server or VM | [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) | Standard appliance path with Debian base, disk layout, monitoring, and DNS services |
| Public or private cloud | [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) | Restrict proxy ingress, use resilient storage, and plan HA before production rollout |
| Existing Linux host | [Linux Server](/getting_started/install_safesquid/linux_server) | You own OS hardening, service dependencies, log rotation, and supportability |

## Installation sequence

1. [Validate prerequisites](/getting_started/install_safesquid/prerequisites) — confirm host resources, static addressing, DNS, NTP, firewall rules, and activation key readiness.
2. Deploy using one installation method only. Do not mix appliance and manual Linux steps on the same host.
3. Verify `safesquid` service status, listener state on `8080/tcp`, and log directory creation under `/var/log/safesquid/`.
4. Restrict inbound proxy access to pilot client networks before any user testing.
5. Continue to [Activate Your License](/getting_started/activate) after the service is reachable.

## Evidence to capture

- Host sizing and topology decision from [Deployment Planning](/getting_started/deployment_planning).
- Service status output showing SafeSquid running.
- Listener output showing `8080/tcp` bound only as intended.
- Firewall or security group rule set for management and proxy traffic.
- Initial `/var/log/safesquid/` entries after service start.

## Next steps

- [Prerequisites](/getting_started/install_safesquid/prerequisites) — prepare the host and network before install.
- [Access the Interface](/getting_started/access_the_interface) — open the Configuration Portal after deployment.
- [Activate Your License](/getting_started/activate) — unlock policy enforcement and continue the smoke test.
