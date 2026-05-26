---
title: Getting Started
description: Production onboarding path for deploying, activating, validating, and hardening SafeSquid SWG.
keywords:
  - getting started
  - SafeSquid documentation
  - SafeSquid deployment
  - production onboarding
  - secure web gateway rollout
---

# Start SafeSquid in a Controlled Path

SafeSquid SWG becomes a control point only after traffic is deliberately routed through the proxy, the instance is activated, and baseline policies produce evidence. Treat the first deployment as a controlled pilot: define scope, prove traffic flow, verify logs, then expand to production users.

## Quickstart path

1. [SafeSquid SWG](/getting_started/introduction) - confirm why HTTP and HTTPS traffic must pass through a Layer 7 proxy before internet access.
2. [Register and get your key](/getting_started/register) - create the Self-Service Portal account and download the activation key required for full enforcement.
3. [Plan the deployment](/getting_started/deployment_planning) - size CPU, RAM, disk, NICs, routing, high availability, and evidence retention before installation.
4. [Meet installation prerequisites](/getting_started/install_safesquid/prerequisites) - validate host access, network reachability, DNS, NTP, and certificate rollout ownership.
5. [Install SafeSquid](/getting_started/install_safesquid/prerequisites) - choose the SafeSquid Appliance Builder, cloud, or existing Linux server path.
6. [Route a client through SafeSquid](/getting_started/client_configuration/connect_your_client) - use explicit proxy for a pilot, then PAC, GPO, MDM, or system-wide settings for managed rollout.
7. [Access the interface safely](/getting_started/access_the_interface) - open the Configuration Portal from a managed network and confirm baseline service state.
8. [Activate the license](/getting_started/activate) - upload the activation key and run the smoke test before policy work.
9. [Configure baseline policies](/getting_started/configure_web_security_policies) - enable SSL inspection, identity, DNS security, access controls, malware scanning, DLP, and reporting evidence.

## Production readiness checks

Before routing broad user traffic, confirm:

- The SafeSquid listener is reachable only from approved client networks.
- A proxied test request appears in `/var/log/safesquid/access/extended.log`.
- The Configuration Portal shows an active license.
- HTTPS inspection has a trusted Root CA rollout path through GPO, MDM, or approved manual import.
- Logs are retained locally or forwarded to the Reporting Service or SIEM for audit evidence.
- A rollback path exists for proxy settings, PAC files, GPO links, and firewall routing.

## Next steps

- [Deployment Planning](/getting_started/deployment_planning) - size the first production-ready node or cluster.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - select the right client onboarding method.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - turn proxy traffic into enforceable controls.

