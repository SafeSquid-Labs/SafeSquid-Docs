---
title: "Troubleshooting Installation Issues"
description: "Diagnose and resolve SafeSquid troubleshooting installation issues incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "installation issues"]
---

# Troubleshooting Installation Issues

Troubleshooting Installation Issues can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

If you see **Bad archive mirror**, **Failed to retrieve pre-configuration**, or other installation failures, use the sections below to diagnose and fix. Symptoms are grouped by stage: before install, during install, and network-related.

## Before Installation

Common issues in this stage include system compatibility, creating a bootable USB or attaching the appropriate .iso file, and correctly setting up the BIOS/UEFI settings.

Solutions involve checking system requirements, verifying the integrity of the installation media, and ensuring correct boot order.

## During Installation

Issues during installation can range from partitioning errors, and network configuration problems, to software selection difficulties.

Resolutions may include checking disk space, reviewing network settings, and ensuring proper selection of software packages.

For network-related issues such as those mentioned below, you can use the installer console to identify the root cause of the issue and act based on it.

## Network Checks for Issue Identification

Network issues can significantly impact the installation and functionality of SafeSquid. If you see **"Bad archive mirror"** or **"Failed to retrieve the pre-configuration file"** during installation, use the checks below to fix DNS and gateway settings.

Administrators can perform various checks to identify and resolve network-related problems:

1. **Network Configuration**: Review and modify network settings using the `ip` commands. `ip addr show # Display all interface IP addresses ip route show # Display routing table` **What to check:** IP address is assigned to the correct interface (e.g., `eth0: inet 192.168.1.100/24`) Default gateway is present in routing table (e.g., `default via 192.168.1.1 dev eth0`) **Common issues:** No IP address shown -\> interface not configured or DHCP failed No default route -\> gateway not set during network configuration step
2. **DNS Resolution and Ping check**: Since busybox is a minimal Linux environment, use `ping` to verify both DNS resolution and connectivity. `ping -c 3 google.com` **Expected success output:** `PING google.com (142.250.x.x): 56 data bytes 64 bytes from 142.250.x.x: icmp_seq=0 ttl=xx time=x.x ms` **Failure symptoms:** `ping: bad address 'google.com'` -\> DNS resolution failed (check `/etc/resolv.conf` for nameserver entries) `Network is unreachable` -\> No default gateway configured `Request timeout` or 100% packet loss -\> Firewall blocking ICMP, or no internet connectivity
3. **Firewall Rules**: check your network firewall rules for possible port blocking.

By performing these network checks and using the available networking commands, administrators can pinpoint network-related problems and take corrective actions.

Once you have identified and solved your network problem, come back to the installer tty using ctrl \+ alt \+ F1 and select continue.

Select continue again.

Select the "Download debconf preconfiguration file" step.

Follow the steps of standard installation and continue your installation process.

## Conclusion

For additional assistance, consult the SafeSquid forums and community resources.

## ISO Installation Failure

### Symptoms

**"Failed to retrieve the pre-configuration file"** Appears during installation when the installer cannot download the automated configuration script from SafeSquid servers. This typically indicates DNS or gateway misconfiguration.

**"Bad archive mirror"** Appears when the installer cannot reach Debian package repositories. This indicates:

- Firewall blocking outbound HTTP/HTTPS on the assigned proxy IP
- No default gateway configured
- DNS resolution failure for `deb.debian.org` or `downloads.safesquid.net`

### Root Causes

- **DNS misconfiguration:** Wrong DNS server IP, or DNS server is unreachable
- **Gateway misconfiguration:** No default route, or gateway IP is incorrect
- **NIC configuration:** Wrong interface selected, or interface is down
- **Firewall rules:** Network firewall blocking installation traffic from the SafeSquid server's IP

If you face any error while installing SafeSquid Appliance Builder (SAB-ISO), you will get debugging logs information by pressing **ALT\+F4**. To return to the previous screen press **ALT\+F1**.

![Bad Archive Mirror Template](/images/troubleshooting/installation_issues_05_bad_archive_mirror_template.webp)

![Failed to retrieve the pre-configuration file error template](/images/troubleshooting/installation_issues_06_failed_to_retrieve_the_pre_configuration_file_er.webp)

## Capture useful evidence

Collect evidence before restarting services or changing policy. Keep screenshots, command output, and relevant SafeSquid logs with the incident ticket.

```sh
tail -100 /var/log/safesquid/safesquid.log
tail -100 /var/log/syslog
```

Record the affected user, source IP address, requested URL, timestamp, browser error, SafeSquid policy section changed, and verification result.

## Next steps

- Use [Find a complete connection log](/troubleshooting/how_to_use_find_client_id_sh_for_getting_complete_connection_log) to trace a specific client transaction.
- Use [Troubleshooting](/troubleshooting/troubleshooting) for the broader diagnostic checklist.