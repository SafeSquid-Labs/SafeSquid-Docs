---
title: "NTP Time Synchronization"
description: "Accurate system time for SafeSquid SWG authentication, TLS, and logging integrity"
keywords:
  - SafeSquid SWG
  - NTP
  - time sync
  - Active Directory
  - TLS validation
  - Kerberos
---

# NTP Time Synchronization

NTP (Network Time Protocol) keeps your SafeSquid server's clock synchronized with enterprise time sources. Accurate time is critical for SSO/Kerberos authentication, TLS certificate validation, and audit log timestamps.

**Why you need this:** Clock drift breaks Kerberos (requires ≤5 minutes skew), causes TLS certificate errors, and makes log correlation impossible.

## Prerequisites

:::info Before You Start

- Linux host with root/sudo access
- Enterprise NTP servers or domain controllers providing time
- Firewall allows UDP port 123 outbound
- Network connectivity to NTP sources

:::

## Installation and Configuration

### 1. Install Time Synchronization Service

**Prefer chrony** (modern, faster sync):

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install -y chrony
```

**RHEL/Rocky/CentOS:**
```bash
sudo dnf install -y chrony
```

**Verify installation:**
```bash
chronyd -v
```
Should print chrony version.

:::tip Alternative: ntpd

If your environment uses `ntpd` instead of `chrony`, install with:
```bash
sudo apt install -y ntp  # Debian/Ubuntu
sudo dnf install -y ntp  # RHEL/CentOS
```
Configuration is similar but uses `/etc/ntp.conf`.

:::

---

### 2. Configure Time Sources

**Edit chrony configuration:**

- **Debian/Ubuntu:** `/etc/chrony/chrony.conf`
- **RHEL/CentOS:** `/etc/chrony.conf`

```bash
sudo nano /etc/chrony/chrony.conf
```

**Replace default pool servers with your enterprise NTP servers:**

```
# For Active Directory environments, prefer domain controllers:
server dc1.company.com iburst
server dc2.company.com iburst

# Or use enterprise NTP servers:
server ntp1.company.com iburst
server ntp2.company.com iburst

# For AD, set minimal sources to 2:
# minsources 2

# Allow large initial time corrections:
makestep 1.0 3

# Drift file (tracks clock frequency):
driftfile /var/lib/chrony/chrony.drift

# Log directory:
logdir /var/log/chrony
```

**Explanation:**
- **server ... iburst** — Speeds up initial synchronization
- **makestep 1.0 3** — Allows step (immediate) corrections if offset >1 second, up to 3 times
- **driftfile** — Saves clock frequency for faster sync after restart
- **logdir** — Where chrony logs are stored

**Save and exit.**

---

### 3. Enable and Start Chrony

```bash
sudo systemctl enable --now chronyd
systemctl is-active chronyd
systemctl is-enabled chronyd
```

**Expected:** Both commands return `active` and `enabled`.

---

### 4. Validate Synchronization

**Check tracking status:**
```bash
chronyc tracking
```

**Expected output:**
```
Reference ID    : 192.168.1.10 (ntp1.company.com)
Stratum         : 3
System time     : 0.000123 seconds slow of NTP time
Last offset     : -0.000045 seconds
RMS offset      : 0.000123 seconds
```

**Key fields:**
- **Reference ID:** Your NTP server
- **Stratum:** Lower is better (1-4 typical)
- **System time offset:** Should be within milliseconds (< 0.1 seconds)

---

**Check source status:**
```bash
chronyc sources -v
```

**Expected output:**
```
  .-- Source mode  '^' = server, '=' = peer
 / .- Source state '*' = current best, '+' = combined, '-' = not combined,
| /             '?' = unreachable, 'x' = time may be in error
||
|| MS Name/IP address         Stratum Poll Reach LastRx Last sample
|| ===============================================================================
^* ntp1.company.com                 2   6   377    25   -123us[ -156us] +/-   12ms
^+ ntp2.company.com                 2   6   377    26   +234us[ +201us] +/-   15ms
```

**Key fields:**
- **\*** (asterisk) — Current best source (should have at least one)
- **Reach** — Should be `377` (all recent polls successful)
- **Last sample** — Time offset in microseconds/milliseconds

---

### 5. Align SafeSquid Authentication

**For SSO/Kerberos with Active Directory:**

Verify time skew is within 5 minutes of the domain controller:

```bash
# Check local time:
date

# Check DC time (if accessible):
net time \\DC1.company.com /set /yes
```

**Or use this to compare:**
```bash
ntpdate -q dc1.company.com
```

**Expected:** Offset less than 300 seconds (5 minutes).

:::caution Kerberos Requirement

Kerberos authentication fails if time skew exceeds 5 minutes. For production Active Directory environments, keep skew under 1 minute.

:::

---

## Verify NTP is Working

### Check Synchronization Status

```bash
chronyc tracking
```

**Expected:**
- **Reference ID:** Shows your NTP server (not `0.0.0.0`)
- **System time offset:** < 0.1 seconds
- **Stratum:** 2-4 (depending on your NTP server)

---

### View Source Statistics

```bash
chronyc sourcestats -v
```

**Expected:** All sources show reasonable offsets and low jitter.

---

### Monitor Logs

```bash
# Check recent sync events:
sudo journalctl -u chronyd -n 50

# Or check chrony log:
sudo tail -f /var/log/chrony/tracking.log
```

**Expected log entries:**
```
Selected source 192.168.1.10
System time wrong by 0.123 seconds
Clock was stepped
```

---

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| No synchronization | UDP 123 blocked or wrong server names | Allow UDP 123 outbound; verify server names resolve: `dig ntp1.company.com` |
| Frequent step corrections | Unstable time source or VM host time interference | Use stable NTP sources; disable VM time sync if using NTP |
| Stratum shows 16 | Can't reach any NTP server | Check firewall, network connectivity, server names |
| SSO/Kerberos failures | Time skew >5 minutes | Force sync: `sudo chronyd -q 'server ntp1.company.com iburst'` |
| "System clock wrong" errors | Large initial offset | Run `sudo chronyd -q` to step clock, then restart chronyd |

**Still not working?**

1. **Test NTP server connectivity:**
   ```bash
   ntpdate -q ntp1.company.com
   ```
   Should show offset.

2. **Check chrony configuration:**
   ```bash
   chronyc sources
   chronyc tracking
   ```

3. **Force time sync:**
   ```bash
   sudo chronyd -q 'server ntp1.company.com iburst'
   sudo systemctl restart chronyd
   ```

4. **Check logs:**
   ```bash
   sudo journalctl -u chronyd -n 50
   ```

---

## Production Best Practices

1. **Use at least 3 NTP sources** for redundancy:
   ```
   server ntp1.company.com iburst
   server ntp2.company.com iburst
   server ntp3.company.com iburst
   ```

2. **For Active Directory, prefer domain controllers:**
   ```
   server dc1.company.com iburst prefer
   server dc2.company.com iburst
   ```

3. **Monitor time drift with Monit:**
   
   Add to `/etc/monit/conf.d/chrony`:
   ```
   check process chronyd matching chronyd
     start program = "/bin/systemctl start chronyd"
     stop program = "/bin/systemctl stop chronyd"
   ```

4. **Alert on large offsets:**
   - Configure monitoring to alert if offset >1 second
   - Investigate VM host time sync conflicts
   - Check for network latency to NTP servers

---

## Next Steps

1. **[Monit](/docs/SafeSquid_SWG/Supporting_Services/Monit/)** — Monitor chronyd and auto-restart if needed
2. **[BIND](/docs/SafeSquid_SWG/Supporting_Services/Bind/)** — DNSSEC validation requires accurate time
3. **[Authentication](/docs/Authentication/main/)** — Configure SSO/Kerberos (requires NTP)
4. **[SSL Inspection](/docs/SSL_Inspection/main/)** — TLS certificate validation requires accurate time

**Related:** [Supporting Services Overview](/docs/SafeSquid_SWG/Supporting_Services/main/)
