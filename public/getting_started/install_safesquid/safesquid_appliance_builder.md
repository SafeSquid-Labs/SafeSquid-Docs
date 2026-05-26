---
title: SafeSquid Appliance Builder
description: Deploy SafeSquid SWG with the standard Debian-based appliance path for new bare metal or virtual machine deployments.
keywords:
  - SafeSquid Appliance Builder
  - SAB ISO
  - SafeSquid appliance
  - Debian SafeSquid deployment
---

# Build the Standard Appliance

SafeSquid Appliance Builder (SAB) is the standard path for new SafeSquid deployments on bare metal or virtual machines. It provides a repeatable Debian-based appliance build with SafeSquid and supporting services. Completion time depends on hardware, storage, network, and package mirror reachability; do not treat setup-time claims as guarantees.

## Use this method when

- You are building a new SafeSquid node.
- You want a repeatable appliance baseline.
- The server or VM can boot from the SAB ISO.
- Operations can dedicate the host to SafeSquid.

Use [Linux Server](/getting_started/install_safesquid/linux_server) only when an existing supported Linux host must be reused.

## Validate prerequisites

Before booting the ISO, confirm:

- `8+` CPU cores, `8 GB+` RAM, `4+` NICs, and `50 GB+` disk.
- Static IP, gateway, DNS, hostname, and NTP decisions are documented.
- Installation media is obtained from an approved SafeSquid source.
- The target disk can be overwritten.
- Activation key is available for post-install activation.
- Proxy and management firewall rules are approved.

## Install the appliance

1. Boot the server or VM from the SAB ISO.
2. Select the target disk and confirm the destructive install step.
3. Configure network parameters using the approved deployment values.
4. Select the appropriate package mirror or repository path.
5. Allow the installer to complete OS, SafeSquid, and supporting service setup.
6. Reboot into the installed appliance.
7. Sign in locally or through the approved management path for first validation.

Do not route user traffic until service health and access-log evidence are confirmed.

## Verify installation

Check service state:

```bash
systemctl status safesquid --no-pager
```

Check the proxy listener:

```bash
ss -lntp | grep ':8080'
```

Check logs:

```bash
tail -50 /var/log/safesquid/safesquid.log
```

From a pilot client, test HTTP through the proxy and confirm an access-log entry.

## Capture appliance evidence

Record:

- ISO source and version.
- Host or VM sizing.
- Network parameters used during installation.
- Service status output.
- Listener check for `8080/tcp`.
- First pilot access-log entry.
- Disk layout for SafeSquid logs and data.

## Troubleshoot installation

| Symptom | Likely cause | Fix |
|---|---|---|
| Installer cannot reach packages | DNS, gateway, or mirror problem | Verify network settings and selected mirror |
| Service not running after reboot | Install or service startup failure | Check `systemctl status safesquid` and SafeSquid logs |
| Proxy port not listening | Service failed or listener config differs | Validate service state and configured listener |
| Client cannot connect | Firewall or route missing | Test from client network and update firewall rules |
| Disk layout is wrong | Wrong target disk or VM storage | Stop rollout and rebuild before activation |

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - open the Configuration Portal through an approved path.
- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - route pilot traffic through SafeSquid.

