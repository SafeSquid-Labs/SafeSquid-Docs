---
title: "Monit Service Governance"
description: "Automated monitoring and self-healing for SafeSquid SWG processes and host resources"
keywords:
  - SafeSquid SWG
  - Monit
  - service monitoring
  - self-healing
  - auto-restart
  - health checks
---

# Monit Service Governance

Monit automatically monitors SafeSquid and restarts it if it crashes or becomes unresponsive. It also performs housekeeping tasks like log rotation and temporary file cleanup.

**Why you need this:** Without Monit, a SafeSquid crash requires manual intervention. In production, this means downtime until someone notices and restarts the service.

## Prerequisites

:::info Before You Start

- Linux host with systemd
- Root or sudo access
- SafeSquid installed and running
- Log storage capacity for Monit logs

:::

## Installation and Configuration

### 1. Install Monit

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install -y monit
```

**RHEL/Rocky/CentOS:**
```bash
sudo dnf install -y monit
```

**Verify installation:**
```bash
monit -V
```
Should print Monit version.

---

### 2. Enable Monit Service

```bash
sudo systemctl enable --now monit
systemctl is-active monit
systemctl is-enabled monit
```

**Expected:** Both commands return `active` and `enabled`.

---

### 3. Configure Monit HTTP Interface (Local Only)

Edit `/etc/monit/monitrc`:

```bash
sudo nano /etc/monit/monitrc
```

Add or uncomment:
```
set httpd port 2812 and
  use address localhost
  allow localhost
```

**Save and reload:**
```bash
sudo monit reload
```

**Verify:**
```bash
curl -s http://localhost:2812 | head -n1
```
Should return HTML header.

---

### 4. Add SafeSquid Process and Port Checks

Create `/etc/monit/conf.d/safesquid`:

```bash
sudo nano /etc/monit/conf.d/safesquid
```

Add:
```
check process safesquid with pidfile /var/run/safesquid.pid
  start program = "/bin/systemctl start safesquid"
  stop  program = "/bin/systemctl stop safesquid"
  if failed port 8080 protocol http then restart
  if 3 restarts within 5 cycles then alert
```

**Explanation:**
- Monitors SafeSquid process via PID file
- Checks port 8080 for HTTP responsiveness
- Auto-restarts if port check fails
- Alerts if SafeSquid restarts 3+ times in 5 cycles (possible persistent issue)

**Reload and verify:**
```bash
sudo monit reload
sudo monit status safesquid
```

**Expected:** Status shows `Running` and `OK`.

---

### 5. Add Housekeeping Checks

**Log Rotation Trigger:**

Create `/etc/monit/conf.d/safesquid-logs`:

```bash
sudo nano /etc/monit/conf.d/safesquid-logs
```

Add:
```
check file ss-log-size with path /var/log/safesquid/access.log
  if size > 500 MB then exec "/usr/sbin/logrotate -f /etc/logrotate.d/safesquid"
```

**Temporary Files Cleanup:**

Add to the same file:
```
check directory ss-tmp with path /tmp
  if timestamp > 24 hours then exec "/usr/bin/find /tmp -type f -mtime +1 -delete"
```

:::caution Cleanup Script Risk

The temp file cleanup example deletes files older than 1 day in `/tmp`. Adjust the path and age to match your environment to avoid deleting needed files.

:::

**Reload:**
```bash
sudo monit reload
sudo monit status
```

---

### 6. Add Update Orchestration (Optional)

If you want Monit to trigger SafeSquid upgrades when an upgrade flag file appears:

Create `/etc/monit/conf.d/safesquid-upgrade`:

```bash
sudo nano /etc/monit/conf.d/safesquid-upgrade
```

Add:
```
check file ss-upgrade-flag with path /var/lib/safesquid/upgrade.flag
  if changed checksum then exec "/usr/local/bin/safesquid-upgrade"
```

**Note:** You'll need to create the `/usr/local/bin/safesquid-upgrade` script separately.

---

### 7. Reload and Validate All Checks

```bash
sudo monit reload
sudo monit summary
sudo monit status
```

**Expected:**
- `monit summary` shows all checks
- `monit status` shows all checks as `Running` and `OK`

---

## Verify Monit is Working

### Test Auto-Restart

**Simulate SafeSquid crash:**

```bash
sudo systemctl stop safesquid
```

**Wait 1-2 minutes** (one Monit check cycle), then check:

```bash
systemctl status safesquid
```

**Expected:** SafeSquid is running again (Monit restarted it automatically).

**Check Monit logs:**

```bash
sudo tail -20 /var/log/monit.log
```

**Expected log entries:**
```
[UTC] info     : 'safesquid' process is not running
[UTC] info     : 'safesquid' trying to restart
[UTC] info     : 'safesquid' process started
```

---

### View Monit Dashboard

**From the SafeSquid server:**

```bash
curl http://localhost:2812
```

Or open in a browser on the server (if GUI available): `http://localhost:2812`

**Expected:** Monit dashboard showing SafeSquid status as green/running.

---

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| Monit won't start | Incorrect permissions on `/etc/monit/monitrc` | `sudo chmod 600 /etc/monit/monitrc && sudo monit reload` |
| Checks not loading | Missing `include` directive | Add `include /etc/monit/conf.d/*` to `/etc/monit/monitrc` |
| Port 8080 check fails | SafeSquid on different port | Update `if failed port` to actual port in config |
| Frequent restarts (3+ in 5 cycles) | Resource exhaustion or dependency failure | Check `journalctl -u safesquid` and system resources (CPU, memory, disk) |
| Monit dashboard not accessible | HTTP interface not configured | Verify `set httpd port 2812` in `/etc/monit/monitrc` |

**Still not working?**

1. **Check Monit configuration syntax:**
   ```bash
   sudo monit -t
   ```
   Should return: `Control file syntax OK`

2. **Check Monit logs:**
   ```bash
   sudo tail -50 /var/log/monit.log
   ```

3. **Verify SafeSquid PID file location:**
   ```bash
   ps aux | grep safesquid
   cat /var/run/safesquid.pid
   ```
   If PID file doesn't exist, update the Monit check to use process name instead.

---

## Next Steps

1. **[BIND](/docs/SafeSquid_SWG/Supporting_Services/Bind/)** — Configure local DNS resolver
2. **[NTP](/docs/SafeSquid_SWG/Supporting_Services/NTP/)** — Ensure accurate time synchronization
3. **[Audit & Forensics](/docs/Audit_Forensics/main/)** — Monitor SafeSquid logs and events
4. **[Troubleshooting](/docs/Troubleshooting/main/)** — Common issues and fixes

**Related:** [Supporting Services Overview](/docs/SafeSquid_SWG/Supporting_Services/main/)
