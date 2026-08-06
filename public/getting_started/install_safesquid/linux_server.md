---
title: "Linux Server Install"
description: "Install SafeSquid SWG on an existing supported Linux server when the appliance path is not suitable."
keywords: ["SafeSquid Linux install", "SafeSquid TAR package", "existing Linux server", "SafeSquid deployment"]
---

# Install on a Managed Linux Host

Use the Linux server path only when the organization already owns the operating system lifecycle, hardening baseline, monitoring, backup, and rollback. For new deployments, the SafeSquid Appliance Builder is the standard path because it provides a repeatable appliance build and supporting services.

## Use this method when

Use an existing Linux host when:

- The host is dedicated to SafeSquid or the security exception is approved.
- The OS version, packages, services, and hardening baseline are managed.
- Operations can install dependencies and troubleshoot service failures.
- Backup and rollback are already defined.

Do not use this method as a shortcut around appliance planning. A poorly managed host creates unstable inspection, missing logs, and difficult incident response.

## Validate prerequisites

Confirm:

- Root or approved sudo access is available.
- The host has static IP, DNS, gateway, and NTP configuration.
- Required outbound paths are reachable.
- Required packages and libraries can be installed.
- No local service conflicts with the approved SafeSquid proxy port.
- Activation key and rollback plan are available.

## Prepare the host

Record OS details:

```bash
uname -a
cat /etc/os-release
```

Update package metadata according to the organization's change process:

```bash
sudo apt update
```

Check disk and memory:

```bash
df -h
free -m
```

Expected result: disk and memory match the sizing plan, with enough free space for logs, reports, updates, and support bundles.

<Tabs>
  <Tab title="Debian and Ubuntu">
    Use the organization's approved package repositories and change window:

    ```bash
    sudo apt update
    sudo apt install -y bind9 monit
    ```

    Confirm that local hardening does not block SafeSquid, Monit, or BIND9 service management.
  </Tab>
  <Tab title="RHEL family">
    Use the organization's approved repository and package names for the target distribution:

    ```bash
    sudo dnf makecache
    sudo dnf install -y bind monit
    ```

    Confirm SELinux, firewalld, and local hardening rules before starting SafeSquid.
  </Tab>
</Tabs>

## Install SafeSquid

Use the approved SafeSquid package or TAR source for the target release. Preserve the source URL, checksum if provided, and install date in the change record.

After extracting or installing the package, start SafeSquid:

```bash
sudo systemctl start safesquid
```

If the platform uses the legacy service script, use the approved service command for that build:

```bash
sudo /etc/init.d/safesquid start
```

## Verify service health

Check service state:

```bash
systemctl status safesquid --no-pager
```

Check listener state:

```bash
ss -lntp | grep ':8080'
```

Check access-log creation after a pilot request:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: SafeSquid runs, listens on the approved port, and records pilot traffic.

## Configure supporting services

<Accordion title="Monit process monitoring">
  Monit helps operators detect and restart failed services when it is part of the approved operations baseline. Confirm Monit is installed, enabled, and configured to monitor SafeSquid before relying on UI-triggered restarts or unattended recovery.

  ```bash
  systemctl status monit --no-pager
  systemctl enable monit
  systemctl restart monit
  ```

  Expected result: Monit runs, starts after reboot, and its configuration is included in the deployment record.
</Accordion>

<Accordion title="BIND9 local DNS service">
  BIND9 is commonly used as the local DNS service on SafeSquid appliance-style deployments. On managed Linux hosts, confirm whether local DNS is required or whether enterprise resolvers will be used directly.

  ```bash
  systemctl status bind9 --no-pager
  named-checkconf
  nslookup example.com 127.0.0.1
  ```

  Expected result: BIND9 runs when required, configuration syntax passes, and local resolution succeeds. If the distribution uses a different service name, use the approved equivalent and record it.
</Accordion>

## Harden before rollout

Before routing users:

- Restrict proxy access to approved client networks.
- Restrict management access to approved administrators.
- Enable log forwarding or retention.
- Confirm OS patching and backup ownership.
- Confirm Root CA rollout path.
- Document service restart and rollback steps.

## Capture deployment evidence

Store:

- OS release and kernel details.
- Package or TAR source.
- Install date and operator.
- Service status output.
- Listener check.
- Pilot access-log sample.
- Firewall and management-access approval.
- Rollback or rebuild procedure.

## Troubleshoot installation

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Package installation fails | Dependency or repository issue | Resolve package source and dependency errors before retrying |
| Service does not start | Port conflict or incomplete install | Check service logs and confirm no service owns the proxy port |
| Listener is missing | SafeSquid is stopped or bound differently | Verify service status and configured listener |
| No traffic is logged | Client bypasses proxy | Configure explicit proxy on a pilot client and retest |

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - open `http://safesquid.cfg/` safely.
- [Activate Your License](/getting_started/activate) - upload the activation key and run smoke tests.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - route pilot traffic.