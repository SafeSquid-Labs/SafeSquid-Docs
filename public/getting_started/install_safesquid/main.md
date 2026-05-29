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

<Steps>
  <Step title="Choose SafeSquid Appliance Builder">
    <Card title="SafeSquid Appliance Builder" icon="hard-drive" href="/getting_started/install_safesquid/safesquid_appliance_builder">
      Build a new VM or hardware appliance from the standard ISO. Use this when the target disk can be dedicated to SafeSquid.
    </Card>

    Confirm the VM or hardware can be rebuilt and the selected disk is disposable.

    If existing data must be preserved, do not use Appliance Builder.
  </Step>
  <Step title="Choose cloud deployment">
    <Card title="Cloud Deployment" icon="cloud" href="/getting_started/install_safesquid/cloud_deployment">
      Place SafeSquid near cloud workloads, remote sites, or hybrid egress with restricted security groups and route-table ownership.
    </Card>

    Confirm route tables and security groups restrict proxy access to approved clients.

    If the proxy is public, tighten source networks before rollout.
  </Step>
  <Step title="Choose Linux Server Install">
    <Card title="Linux Server Install" icon="terminal" href="/getting_started/install_safesquid/linux_server">
      Install on an existing supported Linux host when your team owns OS hardening, monitoring, dependency lifecycle, and rollback.
    </Card>

    Confirm host lifecycle, packages, monitoring, and rollback are already owned.

    If dependencies fail, correct the baseline or rebuild with Appliance Builder.
  </Step>
</Steps>

## Installation sequence

<Steps>
  <Step title="Validate prerequisites">
    Confirm host resources, static addressing, DNS, NTP, firewall rules, and activation key readiness in [Prerequisites](/getting_started/install_safesquid/prerequisites).

    Confirm prerequisite evidence is attached to the deployment record.

    If a prerequisite is missing, block installation until the owner corrects it.
  </Step>
  <Step title="Install using the selected path">
    Build the appliance, launch the cloud instance, or install on the managed Linux host according to the selected deployment model.

    Confirm the installed host matches the approved deployment model and asset record.

    If installation assumptions differ from the plan, stop and select the correct install path.
  </Step>
  <Step title="Verify service and listener state">
    Confirm SafeSquid service health and the approved proxy listener before any managed rollout.

    Confirm service status and listener output show SafeSquid is ready for activation.

    If listener state is missing, inspect service logs and network binding configuration.
  </Step>
  <Step title="Route one pilot client">
    Send one browser or test client through SafeSquid and prove that traffic appears in `/var/log/safesquid/access/extended.log`.

    Confirm the access log records source, destination, timestamp, and action.

    If no log appears, recheck proxy settings and bypass rules before adding users.
  </Step>
  <Step title="Open the interface and activate">
    Open `http://safesquid.cfg/` through the proxy path, then complete [Activate Your License](/getting_started/activate).

    Confirm the Configuration Portal loads and activation evidence is captured.

    If the portal fails, confirm the pilot browser uses SafeSquid as proxy.
  </Step>
</Steps>

## Evidence to capture

Store:

- Install method and version source.
- Hostname, IP address, and deployment environment.
- CPU, RAM, disk, and NIC allocation.
- Service status output.
- Listener check for the approved proxy port.
- Pilot client test and first access-log entry.
- Rollback or rebuild procedure.

## Troubleshoot install choice

| Symptom | Likely cause | Fix |
|---|---|---|
| Installer path is disputed | Ownership model is unclear | Use Appliance Builder for new appliances; use Linux only when OS lifecycle is already owned |
| Cloud proxy is reachable from the internet | Security group is too broad | Restrict source networks before any client rollout |
| Existing Linux host fails dependencies | Baseline OS differs from supported assumptions | Fix dependencies or rebuild with Appliance Builder |

## Next steps

- [Prerequisites](/getting_started/install_safesquid/prerequisites) - confirm install readiness.
- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - build a standard appliance.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - route the first pilot client.
