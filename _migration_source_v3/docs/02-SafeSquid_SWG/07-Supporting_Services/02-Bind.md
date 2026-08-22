---
title: "BIND Local DNS Resolver"
description: "Low-latency, reliable DNS resolution for SafeSquid SWG with secure recursion and caching"
keywords:
  - SafeSquid SWG
  - DNS
  - BIND
  - caching resolver
  - root hints
  - DNSSEC
---

# BIND Local DNS Resolver

BIND provides a local DNS resolver for SafeSquid, reducing lookup latency and improving cache hit rates for frequently accessed domains.

**Why you need this:** Relying on external DNS servers introduces latency, rate-limiting, and dependency on third parties. A local BIND resolver improves performance and reliability.

## Prerequisites

:::info Before You Start

- Linux host with root/sudo access
- SafeSquid installed
- Firewall allows UDP/TCP port 53 outbound (to root DNS servers or forwarders)
- NTP configured (for DNSSEC validation)

:::

## Installation and Configuration

### 1. Install BIND

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install -y bind9 bind9-utils
```

**RHEL/Rocky/CentOS:**
```bash
sudo dnf install -y bind bind-utils
```

**Verify installation:**
```bash
named -v
```
Should print BIND version.

---

### 2. Configure BIND Options

**Edit configuration file:**

- **Debian/Ubuntu:** `/etc/bind/named.conf.options`
- **RHEL/CentOS:** `/etc/named.conf`

```bash
sudo nano /etc/bind/named.conf.options
```

**Add/modify:**
```
options {
  directory "/var/cache/bind";
  
  recursion yes;
  allow-recursion { 127.0.0.1; 10.0.0.0/8; 172.16.0.0/12; 192.168.0.0/16; };
  
  listen-on port 53 { 127.0.0.1; 10.0.0.1; };  // Replace 10.0.0.1 with your server IP
  allow-query { any; };
  
  dnssec-validation auto;
  auth-nxdomain no;
  minimal-responses yes;
  
  rate-limit {
    responses-per-second 25;
  };
};
```

**Explanation:**
- **recursion yes** — Enables BIND to query upstream DNS on behalf of clients
- **allow-recursion** — Limits recursion to private IP ranges (prevents open resolver abuse)
- **listen-on** — IP addresses BIND listens on (127.0.0.1 + server IP)
- **dnssec-validation auto** — Validates DNSSEC signatures
- **rate-limit** — Prevents DNS amplification attacks

**Verify configuration syntax:**
```bash
sudo named-checkconf
```
Should return nothing (silence means success).

---

### 3. Configure Root Hints and Local Zones (Optional)

**Download root hints file:**

```bash
sudo curl -o /var/cache/bind/root.hints https://www.internic.net/domain/named.root
```

**Add root hints to configuration:**

Edit `/etc/bind/named.conf` (or `/etc/named.conf`):

```bash
zone "." {
  type hint;
  file "/var/cache/bind/root.hints";
};
```

**Configure local zone overrides** (for internal domains):

Create `/etc/bind/named.conf.local`:

```bash
sudo nano /etc/bind/named.conf.local
```

Add:
```
zone "corp.local" {
  type forward;
  forwarders { 10.0.0.10; 10.0.0.11; };  // Your internal DNS servers
};
```

**Verify zone syntax:**
```bash
sudo named-checkzone corp.local /dev/null
```

---

### 4. Enable and Start BIND

```bash
# Debian/Ubuntu:
sudo systemctl enable --now bind9
systemctl is-active bind9

# RHEL/CentOS:
sudo systemctl enable --now named
systemctl is-active named
```

**Expected:** Service shows `active`.

---

### 5. Point SafeSquid to Local Resolver

**Edit `/etc/resolv.conf` on the SafeSquid server:**

```bash
sudo nano /etc/resolv.conf
```

**Set:**
```
nameserver 127.0.0.1
```

**Or if BIND is on a different server:**
```
nameserver 10.0.0.1  # BIND server IP
```

**Test DNS resolution:**
```bash
dig @127.0.0.1 example.com
```

**Expected:** Answer section with IP address and low query time.

---

### 6. Harden Resolver (Production)

**Enable logging:**

Edit `/etc/bind/named.conf` (or `/etc/named.conf`):

```bash
logging {
  channel default_log {
    file "/var/log/named/default.log" versions 5 size 10m;
    severity info;
    print-time yes;
  };
  category resolver { default_log; };
  category security { default_log; };
};
```

**Create log directory:**
```bash
sudo mkdir -p /var/log/named
sudo chown bind:bind /var/log/named
```

**Restart BIND:**
```bash
sudo systemctl restart bind9  # or named
```

**Additional hardening:**

- **Restrict recursion** to SafeSquid server IP only (tighten `allow-recursion`)
- **Enable Response Policy Zones (RPZ)** for threat blocking (optional)
- **Monitor logs** for unusual query patterns

---

## Verify BIND is Working

### Test DNS Query

```bash
dig @127.0.0.1 example.com +stats
```

**Expected output:**
- **ANSWER SECTION** with IP address
- **Query time** in milliseconds
- **SERVER: 127.0.0.1#53** (confirming local resolver)

**Check cache hit:**

Run the same query twice:
```bash
dig @127.0.0.1 google.com
dig @127.0.0.1 google.com
```

Second query should be faster (cached response).

---

### Check BIND Status

```bash
sudo rndc status
```

**Expected:** Shows version, uptime, and statistics.

---

### Monitor Logs

```bash
# Debian/Ubuntu:
sudo journalctl -u bind9 -f

# RHEL/CentOS:
sudo journalctl -u named -f

# Or custom log:
sudo tail -f /var/log/named/default.log
```

**Expected log entries:**
```
[date] info: client 192.168.1.1#port: query: example.com IN A
[date] info: resolver: success for example.com
```

---

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| SERVFAIL on DNSSEC domains | NTP not configured or trust anchors missing | Configure NTP first, verify `dnssec-validation auto` |
| High query latency | No caching or blocked egress to root servers | Check firewall allows UDP/TCP 53 outbound; verify `root.hints` |
| "Refused" queries | Recursion restricted or listen-on mismatch | Check `allow-recursion` includes client IP; verify `listen-on` has server IP |
| Port 53 already in use | Another resolver (systemd-resolved, dnsmasq) running | Stop conflicting service: `sudo systemctl disable --now systemd-resolved` |
| Cache not working | BIND restarting frequently or low memory | Check `journalctl -u bind9` for errors; increase memory if needed |

**Still not working?**

1. **Test DNS path:**
   ```bash
   dig @8.8.8.8 example.com +short
   ```
   If this works but local doesn't, BIND config issue.

2. **Check BIND configuration:**
   ```bash
   sudo named-checkconf
   sudo rndc status
   ```

3. **Trace DNS query:**
   ```bash
   dig @127.0.0.1 example.com +trace
   ```
   Shows full resolution path from root to answer.

4. **Check logs:**
   ```bash
   sudo journalctl -u bind9 -n 50
   ```

---

## Next Steps

1. **[Monit](/docs/SafeSquid_SWG/Supporting_Services/Monit/)** — Monitor BIND and auto-restart if it crashes
2. **[NTP](/docs/SafeSquid_SWG/Supporting_Services/NTP/)** — Required for DNSSEC validation
3. **[Integrated DNS Security](/docs/SafeSquid_SWG/Integrated_DNS_Security/)** — Configure DNSBL for malicious domain blocking
4. **[Troubleshooting](/docs/Troubleshooting/main/)** — DNS-specific troubleshooting

**Related:** [Supporting Services Overview](/docs/SafeSquid_SWG/Supporting_Services/main/)
