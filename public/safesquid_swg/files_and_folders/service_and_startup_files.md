---
title: Service and Startup Files
description: SafeSquid SWG service control, startup, TCP tuning, log rotation, Monit, PAM, and system tuning path reference.
keywords:
  - SafeSquid startup files
  - SafeSquid service control
  - SafeSquid logrotate
  - SafeSquid Monit
---

# Service and Startup Files

Service and startup files define how SafeSquid starts, stops, recovers, and tunes the Linux host. Treat them as availability controls. Unapproved changes can stop enforcement, hide startup drift, or make performance symptoms harder to explain during an incident.

## Startup control paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/etc/init.d/safesquid` | Controls the SafeSquid service with `start`, `stop`, `restart`, `status`, and `foreground`. It also sets required startup dependencies and environment variables. | Installation, upgrade, service outage, startup drift, or incident review. | Shows the local service control path. Incorrect edits can prevent SafeSquid from starting after reboot. |
| `/etc/init.d/tcp_tune.sh` | Tunes TCP parameters for connection queues, socket buffers, pending requests, port ranges, overflow handling, TIME-WAIT reuse, keep-alive behavior, and receive or transmit memory. | Capacity tuning, connection surge, slow response, or failed connection investigations. | Writes modified TCP parameters to `/tmp/sysctl_.conf` for debugging. Poor tuning can reduce throughput or exhaust host resources. |
| `/etc/sysctl.conf` | Stores Linux kernel tuning parameters used at runtime under `/proc/sys`. SafeSquid modifies and saves this file for system variables. | Performance review, network tuning, or post-upgrade verification. | Records host-level tuning for memory, connection limits, packet queues, port ranges, socket memory, and TCP buffers. Unreviewed edits can affect every service on the host. |

## Service supervision paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/etc/monit/conf.d/safesquid.monit` | Monit configuration that monitors SafeSquid and restarts it if the process stops. | Service unexpectedly stops, auto-restart fails, or production health checks disagree. | Proves whether SafeSquid has local self-healing configured. Missing or broken rules can leave the proxy down until manual intervention. |
| `/etc/pam.d/safesquid` | PAM configuration for SafeSquid authentication workflows. The wiki references `pam_unix.so` and `pam_permit.so`. | Authentication failures, PAM hardening, or support escalation. | Shows which PAM modules participate in authentication. Treat changes as security-sensitive because PAM can affect user validation and access behavior. |

## Log lifecycle path

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/etc/logrotate.d/safesquid` | Rotates and archives SafeSquid logs. The wiki states SafeSquid logrotate rotates related logs when a log file exceeds `1GB` and compresses rotated logs with gzip. | Disk growth, missing logs, retention review, or SIEM mismatch. | Proves local log lifecycle behavior. Incorrect rotation can fill disks, delete evidence early, or break forensic continuity. |

## Change-control guidance

Back up these files before editing them. Record the change ticket, reviewer, original file hash, modified file hash, restart requirement, and rollback command. After service or startup changes, verify SafeSquid status and confirm a known request appears in local logs.

## Next steps

- Use [Logs and Audit Evidence](/safesquid_swg/files_and_folders/logs_and_audit_evidence) to verify service and log behavior.
- Use [Supporting Services](/safesquid_swg/interface/supporting_services) to validate Monit, BIND, and NTP dependencies.
