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

SafeSquid SWG becomes a security control only after traffic is deliberately routed through the proxy, the instance is activated, and logs prove policy decisions. Treat the first deployment as a controlled pilot: define scope, prove traffic flow, verify logs, then expand to production users.

![SafeSquid SWG control path showing proxy policy, configuration, reporting, and DNS security](/images/getting_started/getting_started_01_safesquid_swg_proxy_layer_policy_and_configuration_repor.webp)

## Quickstart path

<Steps>
  <Step title="Understand the control path">
    Read [Understand SafeSquid SWG](/getting_started/welcome) to confirm why HTTP and HTTPS traffic must pass through a Layer 7 proxy before internet access.

    Confirm the deployment record states which traffic must traverse SafeSquid.

    If ownership is unclear, pause onboarding until the proxy control path is approved.
  </Step>
  <Step title="Register and protect the key">
    Use [Register and Get Your Key](/getting_started/register) to create the Self-Service Portal account and download the `activation_key` file into approved secure storage.

    Confirm the key is stored in approved secure storage and only the storage reference is recorded.

    If the key was copied into tickets or chat, treat it as secret exposure and replace it through the approved process.
  </Step>
  <Step title="Plan deployment and prerequisites">
    Complete [Deployment](/deployment/main) and [Deployment Checklist](/getting_started/install_safesquid/prerequisites) before installing. Record CPU, RAM, disk, NIC, DNS, NTP, firewall, HA, and evidence-retention decisions.

    Confirm the change record includes sizing, network, DNS, NTP, firewall, rollback, and log-retention decisions.

    If a prerequisite is missing, resolve it before installation rather than accepting an undocumented exception.
  </Step>
  <Step title="Install the selected platform">
    Choose the correct install path from [Install SafeSquid](/getting_started/install_safesquid), then verify service health and listener state before routing users.

    Confirm service and listener evidence exists before any client rollout.

    If service health is unclear, keep client routing disabled and inspect installation logs.
  </Step>
  <Step title="Route one pilot client">
    Use [Connect Your Client](/getting_started/client_configuration/connect_your_client) to send one controlled pilot through SafeSquid and prove an access-log entry.

    Confirm `/var/log/safesquid/access/extended.log` records the pilot request.

    If no log appears, verify proxy settings, PAC rules, bypass lists, and route ownership.
  </Step>
  <Step title="Activate and configure controls">
    Open [Access the Interface](/getting_started/access_the_interface), complete [Activate Your License](/getting_started/activate), then apply the baseline sequence in [Configure Web Security Policies](/getting_started/configure_web_security_policies).

    Confirm the Configuration Portal shows active license details and baseline control changes are recorded.

    If activation cannot be proven, re-upload the key and confirm subscription path reachability.
  </Step>
  <Step title="Verify before expansion">
    Run [Production-Readiness Checklist](/getting_started/verify_your_setup) and capture activation, routing, policy, DNS, and log evidence before broad rollout.

    Confirm all readiness checks pass and evidence is attached to the deployment record.

    If any check fails, keep the rollout in pilot scope until the failed control is corrected and retested.
  </Step>
</Steps>

## Choose the right start point

<Steps>
  <Step title="Choose the pilot planning path">
    <Card title="First production pilot" icon="route" href="/deployment/main">
      Start here when you need a controlled first deployment with sizing, firewall, DNS, logging, and rollback evidence.
    </Card>

    Confirm the planning path names deployment owner, change record, and rollout scope.

    If deployment scope is unclear, resolve ownership before choosing an install path.
  </Step>
  <Step title="Choose the install platform">
    <Card title="Install platform" icon="server" href="/getting_started/install_safesquid">
      Choose Appliance Builder, cloud deployment, or managed Linux based on ownership and operational constraints.
    </Card>

    Confirm the install platform matches ownership, rollback, and lifecycle requirements.

    If platform ownership is disputed, use deployment planning to decide before installation.
  </Step>
  <Step title="Choose the client routing path">
    <Card title="Client routing" icon="network" href="/getting_started/client_configuration">
      Select explicit proxy, PAC, system-wide proxy, enterprise deployment, or application-specific settings.
    </Card>

    Confirm one routing method can produce an access-log entry for a pilot client.

    If pilot traffic bypasses SafeSquid, revisit client routing before policy rollout.
  </Step>
  <Step title="Choose the verification path">
    <Card title="Production verification" icon="clipboard-check" href="/getting_started/verify_your_setup">
      Prove service state, activation, proxy flow, DNS, policy action, and access-log evidence.
    </Card>

    Confirm verification evidence covers service, listener, activation, routing, policy, DNS, and logs.

    If any evidence is missing, keep the deployment in pilot scope.
  </Step>
</Steps>

## Production readiness checks

Before routing broad user traffic, confirm:

- A deployment owner and change record exist.
- The SafeSquid listener is reachable only from approved client networks.
- A proxied test request appears in `/var/log/safesquid/access/extended.log`.
- The Configuration Portal shows active license details.
- HTTPS inspection has a trusted Root CA rollout path through GPO, MDM, or approved manual import.
- Logs are retained locally, forwarded to the Reporting Service, or exported to a SIEM.
- Rollback exists for proxy settings, PAC files, GPO links, MDM profiles, firewall routing, and DNS changes.

## Evidence to capture

Store these artifacts with the deployment record:

- Activation key storage reference.
- Deployment sizing decision.
- Installation method and host identity.
- Pilot client routing test.
- Configuration Portal access test.
- License activation screenshot or exported record.
- First HTTP access-log entry through SafeSquid.
- Root CA rollout owner and schedule.

## Troubleshoot onboarding gaps

| Symptom | Likely cause | Fix | Verify |
|---|---|---|---|
| Pilot traffic bypasses SafeSquid | Client proxy setting, PAC file, or route is wrong | Reconfigure one pilot client before expanding rollout | `/var/log/safesquid/access/extended.log` records the request |
| Configuration Portal does not load | Browser is not using SafeSquid as proxy | Configure explicit proxy and retry `http://safesquid.cfg/` | Configuration Portal loads through the proxy path |
| Activation cannot be proven | Activation key was not uploaded or evidence was not captured | Complete [Activate Your License](/getting_started/activate) and save the license-state record | Product and subscription details are visible |
| HTTPS test produces warnings | Root CA rollout is incomplete | Finish CA deployment before production HTTPS inspection | Managed endpoint trusts the SafeSquid Root CA |

## Next steps

- [Deployment](/deployment/main) - size the first production-ready node or cluster.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - select the right client onboarding method.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - turn proxy traffic into enforceable controls.
- [Production-Readiness Checklist](/getting_started/verify_your_setup) - confirm the pilot is ready for production review.
