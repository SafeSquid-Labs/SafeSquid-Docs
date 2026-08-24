---
title: Deployment
description: Plan, install, connect, verify, and scale SafeSquid SWG from first node to high availability.
keywords:
  - SafeSquid deployment
  - SafeSquid installation
  - SafeSquid rollout
  - secure web gateway deployment
---

# Deploy SafeSquid Into Production

SafeSquid only enforces policy on traffic that reaches it. This section takes a deployment from sizing and network placement, through installation and client routing, to a verified control with evidence an auditor can read — and then to the scaling, resilience, and upgrade decisions that keep it running.

## Quickstart path

1. **[Deployment Planning](/deployment/deployment_planning)** - size the node, choose network placement, and confirm firewall and DNS readiness before anything is installed. Planning gaps surface later as dropped sessions and missing audit trails.
2. **[Install SafeSquid](/getting_started/install_safesquid/main)** - choose appliance, cloud, or managed Linux, then install against verified prerequisites. The install method determines who owns patching and rebuild.
3. **[Register](/getting_started/register)** and **[Activate](/getting_started/activate)** - obtain and apply the activation key so subscription, category, and signature updates flow.
4. **[Connect Your Client](/getting_started/client_configuration/connect_your_client)** - route a pilot client first, then roll out by PAC, GPO, or MDM with a rollback owner named.
5. **[Verify Your Setup](/getting_started/verify_your_setup)** - prove traffic is inspected, logged, and attributable before widening the rollout.
6. **[Scaling and High Availability](/use_cases/scaling_and_high_availability/proxy_clustering)** - add clustering, failover, and disaster recovery once the single node is proven.

## Next steps

- [Deployment Planning](/deployment/deployment_planning) - start here for a new deployment.
- [Choose an Architecture](/deployment/choose_an_architecture) - choose forward, transparent, TCP, or reverse proxy placement.
- [Upgrade SafeSquid](/use_cases/upgrade/version_upgrade) - plan version and OS lifecycle.
