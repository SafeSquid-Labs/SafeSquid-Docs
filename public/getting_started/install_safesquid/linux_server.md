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

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/03-Linux_Server.md §Prerequisites (Required dependencies) */}

<Accordion title="Install build and runtime dependencies">

SafeSquid links against these libraries. Install them before running the installer, using the organization's approved repositories.

<Tabs>
  <Tab title="Debian and Ubuntu">

```bash
sudo apt update
sudo apt install -y wget tar libssl-dev libpcre3 libpcre3-dev zlib1g-dev \
  build-essential libc6 libgcc-s1 libstdc++6
```

  </Tab>
  <Tab title="RHEL, CentOS, Rocky">

```bash
sudo yum install -y wget tar openssl-devel pcre-devel zlib-devel \
  gcc gcc-c++ make glibc libgcc libstdc++
```

  </Tab>
  <Tab title="SUSE and openSUSE">

```bash
sudo zypper install -y wget tar libopenssl-devel pcre-devel zlib-devel \
  gcc gcc-c++ make glibc libgcc_s1 libstdc++6
```

  </Tab>
</Tabs>

Package names drift between releases. If one is not found, locate the equivalent for your distribution rather than skipping it — a missing library surfaces later as a service that installs cleanly and then refuses to start.

</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/03-Linux_Server.md §System Preparation */}

<Accordion title="Prepare directories, firewall, SELinux, and time">

**Create the data directories** so the installer writes into a known layout, and so you can mount dedicated volumes underneath them:

```bash
sudo mkdir -p /var/log/safesquid /var/lib/safesquid /var/db/safesquid
```

**Open the proxy and management ports** using whichever firewall the host runs. Restrict the source scope in the same change, as described in [Deployment Checklist](/getting_started/install_safesquid/prerequisites):

```bash
# firewalld (RHEL family)
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --permanent --add-port=8443/tcp
sudo firewall-cmd --reload
```

```bash
# ufw (Debian, Ubuntu)
sudo ufw allow 8080/tcp
sudo ufw allow 8443/tcp
sudo ufw reload
```

```bash
# iptables
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 8443 -j ACCEPT
sudo iptables-save
```

**Set SELinux to permissive for the setup window** on RHEL-family hosts, then write a targeted policy once the deployment is stable:

```bash
sudo setenforce 0
```

**Confirm time synchronisation.** SSL certificate validation and log correlation both depend on it:

```bash
timedatectl status
```

Expected result: NTP synchronisation is active. If it is not, enable it before continuing:

```bash
sudo systemctl enable --now systemd-timesyncd
```

</Accordion>

## Install SafeSquid

Use the approved SafeSquid package or TAR source for the target release. Preserve the source URL, checksum if provided, and install date in the change record.

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/03-Linux_Server.md §Installation Steps */}
{/* TAR URL corroborated independently at public/troubleshooting/installation_issues.md:104 */}

<Accordion title="Download, extract, and run the installer">

Retrieve and unpack the package:

```bash
cd /usr/local/src
wget http://downloads.safesquid.net/appliance/binary/safesquid_latest.tar.gz
tar -zxvf safesquid_latest.tar.gz
```

Expected result: a `_mkappliance` directory is extracted, containing the installation scripts.

Run the installer from the directory you extracted into:

```bash
sudo _mkappliance/installation/setup.sh
```

The installer checks dependencies, creates the `safesquid` system user and group, installs binaries under `/opt/safesquid/`, writes init and systemd service units, and places default configuration under `/etc/safesquid/`.

Confirm every linked library resolved:

```bash
ldd /opt/safesquid/bin/safesquid
```

Expected result: no line reads `not found`. Any that does names a package still to install — resolve it before starting the service, because the failure otherwise appears at runtime as an immediate exit rather than a missing dependency.

If the installer itself fails, the usual causes are a missing library, running without `sudo`, or insufficient free space. Check the terminal output first, then `df -h`.

</Accordion>

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

  {/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/03-Linux_Server.md §Configure Supporting Services (Monit) */}

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

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/03-Linux_Server.md §Post-Install Hardening */}

<Accordion title="Change the default administrator password">

Change the shipped administrator password before the host is reachable from any client network.

{/* NEEDS-SME-REVIEW: the :8443 management interface's TLS certificate was inspected on 2026-08-28 and found expired (self-signed, CN=safesquid.cfg, valid 2021-08-19 to 2022-08-19 — over 4 years past expiry). The "System → User Management" path below is unverified against the live UI as a result; strict certificate validation correctly blocked automated verification, and an expired cert should not be trusted just to check a menu label. Renew the certificate, then re-verify this path. */}

1. Open the management interface at `https://SERVER-IP:8443/` from an approved administrator network.
2. Go to **System** and open **User Management**.
3. Change the password on the `administrator` account.

Record that the change was made in the deployment evidence. A proxy carrying all corporate web traffic on a default credential is a direct compromise path.

</Accordion>

<Accordion title="Configure log rotation">

Without rotation, SafeSquid logs grow until the volume fills and evidence is silently truncated. Create `/etc/logrotate.d/safesquid`:

```
/var/log/safesquid/*.log {
    daily
    rotate 30
    compress
    delaycompress
    missingok
    notifempty
    sharedscripts
    postrotate
        /etc/init.d/safesquid reload > /dev/null
    endscript
}
```

Adjust `rotate` to the retention target agreed in [Log-Retention Planning](/deployment/log_retention_planning), and use the service reload command appropriate to your build. Test the configuration before relying on it:

```bash
sudo logrotate -d /etc/logrotate.d/safesquid
```

Expected result: the dry run reports the files it would rotate, with no configuration errors.

</Accordion>

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
|---|---|---|
| Package installation fails | Dependency or repository issue | Resolve package source and dependency errors before retrying |
| Service does not start | Port conflict or incomplete install | Check service logs and confirm no service owns the proxy port |
| Listener is missing | SafeSquid is stopped or bound differently | Verify service status and configured listener |
| No traffic is logged | Client bypasses proxy | Configure explicit proxy on a pilot client and retest |
| `ldd` reports a library as `not found` | A system dependency is missing | Install the package providing that library with the host's package manager, then recheck |
| Logs show permission denied, but file ownership looks correct | SELinux is enforcing and blocking SafeSquid | Set permissive mode for the setup window with `sudo setenforce 0`, then author a targeted policy |

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - open `http://safesquid.cfg/` safely.
- [Activate Your License](/getting_started/activate) - upload the activation key and run smoke tests.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - route pilot traffic.
