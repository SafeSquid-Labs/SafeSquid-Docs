---
title: Linux Server Install
description: Install SafeSquid SWG on an existing supported Linux server when the appliance path is not suitable.
keywords:
  - SafeSquid Linux install
  - SafeSquid TAR package
  - existing Linux server
  - SafeSquid deployment
---

# Install on a Managed Linux Host

Use the Linux server path only when the organization already owns the operating system lifecycle, hardening baseline, monitoring, backup, and rollback. For new deployments, the SafeSquid Appliance Builder is the standard path because it provides a repeatable appliance build and supporting services.

## Use this method when

- A new appliance build is not possible.
- The Linux host is already managed by the server operations team.
- OS patching, service monitoring, DNS, log rotation, and backup are owned locally.
- Change control can validate dependencies before routing users.

Do not use this path to bypass appliance planning. A manually installed proxy still needs production sizing, network segmentation, and evidence retention.

## Validate prerequisites

Confirm before installation:

- Host is a supported Linux x86_64 platform. Debian 13 is the primary documented baseline; current Ubuntu LTS releases are supported in parallel.
- CPU, RAM, disk, and NIC capacity match [Deployment Planning](/getting_started/deployment_planning).
- Static IP, DNS, NTP, and default gateway are configured.
- Inbound proxy access is limited to approved client networks.
- Outbound access is available for licensing, updates, and subscribed intelligence services.
- Root or sudo access is available for installation and service management.

## Prepare the host

Create the SafeSquid log path and verify disk capacity before installation.

```bash
sudo mkdir -p /var/log/safesquid
sudo df -h /var/log/safesquid
```

Allow the proxy listener only from approved client networks. Example commands must be adapted to the local firewall standard.

```bash
sudo ufw allow from CLIENT-CIDR to any port 8080 proto tcp
```

Confirm time sync. Authentication, logs, and audit evidence depend on accurate time.

```bash
timedatectl status
```

## Install SafeSquid

Follow the approved package or TAR procedure supplied for the deployment. Keep the source package, checksum, and installation log with the change record.

After extraction or package installation, enable and start the service according to the host init system.

```bash
sudo systemctl enable safesquid
sudo systemctl start safesquid
sudo systemctl status safesquid --no-pager
```

If the host does not use systemd, use the supported service manager for that distribution and record the equivalent status output.

## Verify service health

Check the proxy listener:

```bash
sudo ss -lntp | grep ':8080'
```

Check SafeSquid logs:

```bash
sudo tail -50 /var/log/safesquid/safesquid.log
```

From a pilot client, test HTTP through the proxy:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

Then confirm the request appears in the access log:

```bash
sudo tail -20 /var/log/safesquid/access/extended.log
```

## Harden before rollout

Before routing production users:

- Restrict `8080/tcp` to approved client networks.
- Restrict management access to approved administrator networks.
- Configure log rotation for `/var/log/safesquid/`.
- Configure service monitoring through Monit, systemd, or the approved monitoring stack.
- Validate DNS and NTP services used by the deployment.
- Record backup and restore ownership for SafeSquid configuration.

## Troubleshoot installation

| Symptom | Likely cause | Fix |
|---|---|---|
| Service fails to start | Port conflict, permission issue, or invalid config | Check `systemctl status safesquid` and `/var/log/safesquid/safesquid.log` |
| Port `8080` is not listening | Service did not bind or wrong listener config | Verify service status and listener configuration |
| Client cannot connect | Firewall or routing blocks client network | Test from client network and update firewall rules |
| Logs do not appear | Log path missing or permissions wrong | Verify `/var/log/safesquid/` ownership and disk space |
| Authentication or logs have wrong time | NTP not synchronized | Fix time sync before production testing |

## Capture deployment evidence

- Package source, version, checksum, and installation log.
- Service status output.
- Listener check for `8080/tcp`.
- First successful access-log entry from a pilot client.
- Firewall rule or security policy restricting proxy access.
- Rollback plan for package removal and proxy routing.

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - open the Configuration Portal from an approved admin path.
- [Activate Your License](/getting_started/activate) - upload the activation key and run smoke tests.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - route pilot traffic through SafeSquid.

