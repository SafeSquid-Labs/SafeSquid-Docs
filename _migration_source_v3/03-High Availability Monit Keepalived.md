---
title: High Availability with Monit and Keepalived
sidebar_label: Monit + Keepalived HA
---

# High Availability with Monit and Keepalived

SafeSquid supports Active-Passive High Availability (HA) using Keepalived for VIP failover and Monit for application-level health monitoring. This combination is the industry-standard approach — Keepalived handles network-level failover via VRRP in 2–3 seconds, while Monit independently monitors the SafeSquid process and restarts it if it fails.

This guide documents a complete HA setup with split-brain protection, tested on Ubuntu VMs using SafeSquid proxy, Monit 5.34.x, and Keepalived 2.x.

## When to use this setup

| Scenario | Solution | Benefit |
|---|---|---|
| SafeSquid proxy becomes unavailable | Keepalived detects failure and moves VIP to Backup | Clients reconnect automatically within 2–3 seconds |
| SafeSquid process crashes | Monit detects missing PID and restarts SafeSquid | No manual intervention needed |
| Network partition between nodes | VRRP priority election keeps VIP on Master | Split-brain is impossible by design |
| Planned maintenance on Master | Stop SafeSquid on Master; Backup takes VIP | Zero-downtime maintenance window |

## Architecture

Each tool owns a distinct responsibility. They do not conflict — they complement each other.

| Layer | Keepalived | Monit |
|---|---|---|
| Purpose | VIP ownership via VRRP protocol | Application health and process management |
| Failover trigger | Health check script exits non-zero | PID file missing or port not responding |
| Failover speed | 2–3 seconds | 30–60 seconds |
| Split-brain protection | Impossible — VRRP priority election | Possible — mitigated by priority weights |
| Auto-restart SafeSquid | No | Yes — restarts SafeSquid on failure |
| SSH dependency | None | Required for cross-VM notification |

**How they integrate:** Keepalived runs a health check script every 5 seconds. If SafeSquid is not serving traffic, Keepalived drops the Master's VRRP priority below the Backup's, triggering automatic VIP handover. Monit independently restarts SafeSquid and logs the event.

## Prerequisites

- 2 SafeSquid instances deployed — one as Master (Active), one as Backup (Passive)
- Both nodes on the same network subnet to allow VRRP multicast communication
- One unused IP address on your network to serve as the Virtual IP (VIP) — must not be assigned to any other host
- Root or sudo access on both nodes
- `keepalived`, `monit`, and `curl` packages available (Ubuntu/Debian)

**Environment used in this guide:**

| Component | Value | Notes |
|---|---|---|
| Master Node (VM1) | 10.200.2.123 | Active / Master — Priority 101 |
| Backup Node (VM2) | 10.200.2.224 | Standby / Backup — Priority 100 |
| Virtual IP (VIP) | 10.200.2.100 | Clients always connect to this IP |
| Network Interface | ens18 | Confirmed on both VMs via `ip a` |
| SafeSquid Port | 8080 | Monitored by Monit and Keepalived |

## Step 1: Install Keepalived and Monit on both nodes

Run the following on both VM1 (Master) and VM2 (Backup):

```bash
sudo apt update && sudo apt install keepalived monit curl -y
```

## Step 2: Create the SafeSquid health check script

Keepalived runs this script every 5 seconds. If the script exits non-zero, Keepalived drops the node's VRRP priority and triggers VIP failover.

Create the script on **both VMs**:

```bash
sudo nano /etc/keepalived/check_safesquid.sh
```

Paste the following:

```bash
#!/bin/bash
# Health check for SafeSquid — used by Keepalived
# Exit 0 = healthy, Exit 1 = failed (triggers priority drop)

VIP="10.200.2.100"
PORT=8080
TIMEOUT=3

# Check 1: Is the SafeSquid process running?
if ! systemctl is-active --quiet safesquid; then
  echo "$(date): SafeSquid service not active" >> /var/log/keepalived_check.log
  exit 1
fi

# Check 2: Is SafeSquid actually responding on port 8080?
if ! curl -s --max-time $TIMEOUT -x 127.0.0.1:$PORT http://safesquid.cfg > /dev/null 2>&1; then
  echo "$(date): SafeSquid port $PORT not responding" >> /var/log/keepalived_check.log
  exit 1
fi

exit 0
```

Make it executable on both VMs:

```bash
sudo chmod +x /etc/keepalived/check_safesquid.sh
```

## Step 3: Configure Keepalived

The configuration differs on each VM — only `state` and `priority` differ.

:::note
The `auth_pass` must be identical on both VMs and is **limited to 8 characters** (Keepalived truncates longer values). The `virtual_router_id` (51) must also match exactly on both nodes.
:::

### On VM1 (10.200.2.123) — Master

```bash
sudo nano /etc/keepalived/keepalived.conf
```

```
global_defs {
  router_id PROXY_HA
  script_user root
  enable_script_security
}

vrrp_script check_safesquid {
  script "/etc/keepalived/check_safesquid.sh"
  interval 5       # Run check every 5 seconds
  weight -101      # Drop priority by 101 on failure (101 - 101 = 0, below Backup's 100)
  fall 2           # Fail after 2 consecutive failures
  rise 2           # Recover after 2 consecutive successes
}

vrrp_instance SAFESQUID_VIP {
  state MASTER
  interface ens18
  virtual_router_id 51
  priority 101            # Higher than Backup (100) — always wins election
  advert_int 1            # Send VRRP advertisement every 1 second
  nopreempt               # VIP stays on Backup after failback until manually moved

  authentication {
    auth_type PASS
    auth_pass SafeSquid   # Must be identical on both VMs (max 8 chars)
  }

  virtual_ipaddress {
    10.200.2.100/32 dev ens18
  }

  track_script {
    check_safesquid
  }
}
```

### On VM2 (10.200.2.224) — Backup

```bash
sudo nano /etc/keepalived/keepalived.conf
```

```
global_defs {
  router_id PROXY_HA
  script_user root
  enable_script_security
}

vrrp_script check_safesquid {
  script "/etc/keepalived/check_safesquid.sh"
  interval 5
  weight -101
  fall 2
  rise 2
}

vrrp_instance SAFESQUID_VIP {
  state BACKUP
  interface ens18
  virtual_router_id 51
  priority 100            # Lower than Master (101) — yields to Master
  advert_int 1
  nopreempt

  authentication {
    auth_type PASS
    auth_pass SafeSquid   # Must match VM1 exactly
  }

  virtual_ipaddress {
    10.200.2.100/32 dev ens18
  }

  track_script {
    check_safesquid
  }
}
```

### Why weight -101?

Master starts at priority 101. When the health check fails:

- `weight -101` → effective priority becomes `101 - 101 = 0`
- `0 < 100` (Backup's priority) → Backup wins the VRRP election
- Backup sends a higher-priority advertisement → Master transitions to BACKUP state and **releases the VIP**

Using `weight -60` (as in some guides) results in `101 - 60 = 41`, which is still below 100 but may not reliably trigger the BACKUP state transition in all Keepalived versions. Using `-101` is definitive.

## Step 4: Configure Monit on both nodes

Monit monitors the SafeSquid process, auto-restarts it on failure, and sends alerts. It does **not** manage the VIP — Keepalived handles that.

```bash
sudo nano /etc/monit/conf.d/safesquid.monit
```

```
check process safesquid_proxy_service with pidfile /var/run/safesquid/safesquid.pid
  group root
  start program = "/usr/bin/systemctl start safesquid.service" with timeout 60 seconds
  stop program  = "/usr/bin/systemctl stop safesquid.service" with timeout 60 seconds
  if does not exist then restart
  if 3 restarts within 5 cycles then alert
  mode active
```

## Step 5: Start services on both nodes

```bash
# Enable and start Keepalived
sudo systemctl enable keepalived
sudo systemctl start keepalived

# Enable and start Monit
sudo systemctl enable monit
sudo systemctl restart monit
```

Verify the VIP is assigned to VM1 (Master):

```bash
ip a show ens18 | grep 10.200.2.100
```

Expected output on VM1 only:

```
inet 10.200.2.100/32 scope global proto keepalived ens18
```

The `proto keepalived` tag confirms Keepalived is managing the VIP and will remove it automatically on failover.

## Verification

### Check Keepalived status

```bash
# Check service status (should show MASTER state in logs)
sudo systemctl status keepalived

# View recent VRRP events
sudo journalctl -u keepalived -n 30 --no-pager
```

**Healthy Master output** should include:

```
(SAFESQUID_VIP) Entering MASTER STATE
VRRP_Script(check_safesquid) succeeded
```

### Test failover — stop SafeSquid on Master

Open two terminals. On VM2, watch the Keepalived log. On VM1, stop SafeSquid.

```bash
# Terminal 1 — VM2: watch logs
sudo journalctl -u keepalived -f

# Terminal 2 — VM1: trigger failure
sudo systemctl stop safesquid
```

Within 10–15 seconds you should see on VM2:

```
(SAFESQUID_VIP) Changing effective priority from 101 to 0
(SAFESQUID_VIP) Master received advert from 10.200.2.224 with higher priority 100
(SAFESQUID_VIP) Entering BACKUP STATE        ← on VM1
(SAFESQUID_VIP) Transition to MASTER STATE   ← on VM2
Sending gratuitous ARP on ens18 for 10.200.2.100
```

Confirm VIP has moved to VM2:

```bash
ip a show ens18 | grep 10.200.2.100
```

Restore SafeSquid on VM1 after the test:

```bash
sudo systemctl start safesquid
```

:::note
Because `nopreempt` is set, the VIP stays on VM2 after SafeSquid recovers on VM1. To move the VIP back to VM1 manually, restart Keepalived on VM1: `sudo systemctl restart keepalived`.
:::


## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| Both VMs show MASTER | `virtual_router_id` or `auth_pass` mismatch | Ensure `virtual_router_id 51` and identical `auth_pass` on both VMs |
| VIP not assigned on Master startup | Invalid VIP format in config | Run `keepalived --config-test -f /etc/keepalived/keepalived.conf` — VIP must be a valid 4-octet IP |
| VIP not removed from Master after failover | `weight` not sufficient to drop below Backup priority | Use `weight -101` so effective priority becomes 0 (below Backup's 100) |
| Keepalived fails to start | Configuration syntax error | `keepalived --config-test -f /etc/keepalived/keepalived.conf` |
| `auth_pass` truncation warning in logs | Password longer than 8 characters | Keepalived truncates to 8 chars — ensure both VMs use the same ≤8 char password |
| VRRP advertisements not received | Firewall blocking VRRP protocol 112 | `sudo ufw allow proto 112` or add iptables rule |
| Monit `address option specified twice` | Duplicate global settings in `safesquid.monit` | Remove `set daemon` and `set httpd` from `safesquid.monit` — keep them in `/etc/monit/monitrc` only |
| VIP stays on Backup after Master recovers | `nopreempt` is set (by design) | Restart Keepalived on Master to manually move VIP back: `sudo systemctl restart keepalived` |

## Quick reference

### File locations

| File Path | Purpose |
|---|---|
| `/etc/keepalived/keepalived.conf` | VRRP config — state, priority, VIP, health check link |
| `/etc/keepalived/check_safesquid.sh` | Health check script run by Keepalived every 5 seconds |
| `/etc/monit/monitrc` | Monit global config — daemon interval, logging, web UI |
| `/etc/monit/conf.d/safesquid.monit` | SafeSquid process monitoring — auto-restart, alerting |
| `/var/log/keepalived_check.log` | Health check failure log |
| `/var/log/monit.log` | Monit general activity log |

### VM1 vs VM2 configuration differences

| Config Item | VM1 — Master (10.200.2.123) | VM2 — Backup (10.200.2.224) |
|---|---|---|
| `state` | MASTER | BACKUP |
| `priority` | 101 | 100 |
| `weight` | -101 | -101 |
| `nopreempt` | Yes | Yes |
| `check_safesquid.sh` | Identical on both | Identical on both |
| `virtual_router_id` | 51 (must match) | 51 (must match) |
| `auth_pass` | SafeSquid (must match) | SafeSquid (must match) |
| `virtual_ipaddress` | 10.200.2.100/32 | 10.200.2.100/32 |

```

**Related**: [Proxy Clustering](https://docs.safesquid.com/docs/Proxy_Clustering/), [Disaster Recovery](https://docs.safesquid.com/docs/Disaster_Recovery/), [Troubleshooting](https://docs.safesquid.com/docs/Troubleshooting/)
