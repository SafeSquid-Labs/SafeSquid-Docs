---
title: "Supporting Services"
slug: /SafeSquid_SWG/Supporting_Services
description: "Operational services that ensure SafeSquid SWG reliability, performance, and accuracy"
keywords:
  - SafeSquid SWG
  - supporting services
  - Monit
  - DNS
  - BIND
  - NTP
  - time synchronization
---

# Supporting Services

Supporting services ensure SafeSquid SWG operates reliably, performs well, and maintains accurate time synchronization.

**Critical for production:** These services prevent downtime, improve DNS performance, and ensure authentication works correctly.

## Problem statement

When supporting services are ignored, proxy failures become harder to diagnose and easier to misread. A DNS problem can look like a policy problem. A time-sync issue can look like an authentication failure. A crashed process can look like a network outage.

## Client scenario

Use this hub when you are preparing SafeSquid for production operation and need to make sure:

- the proxy restarts or alerts when unhealthy
- DNS behavior is reliable and local where required
- Kerberos, TLS validation, and audit timestamps remain trustworthy

## Why You Need These Services

| **Service** | **Purpose** | **What Happens Without It** |
|-------------|-------------|------------------------------|
| **[Monit](/Supporting_Services_Monit)** | Process monitoring and auto-restart | SafeSquid crashes stay down until manual restart |
| **[BIND](/Bind)** | Local DNS resolver with caching | Slow DNS lookups, dependency on external resolvers |
| **[NTP](/NTP)** | Time synchronization | SSO fails, TLS certificate errors, log timestamps incorrect |

These services are operational dependencies for the controls described elsewhere in the docs. Treat them as part of the deployment, not optional post-install cleanup.

---

## Service Guides

### [Monit](/Supporting_Services_Monit)

**Automated monitoring and self-healing** for SafeSquid and dependent processes.

**What it does:**
- Auto-restarts SafeSquid if it crashes
- Monitors port 8080 for responsiveness
- Cleans up temporary files and rotates logs
- Fetches threat intelligence updates
- Triggers housekeeping tasks

**Install and configure:** [Monit Configuration Guide](/Supporting_Services_Monit)

---

### [BIND](/Bind)

**Local DNS resolver** for fast, reliable domain resolution.

**What it does:**
- Caches DNS responses for faster lookups
- Reduces dependency on external DNS servers
- Improves consistency and auditability
- Enables local DNS overrides for internal domains

**Install and configure:** [BIND Configuration Guide](/Bind)

---

### [NTP](/NTP)

**Time synchronization** critical for authentication and TLS validation.

**What it does:**
- Keeps system time within 5 minutes of Active Directory (required for SSO/Kerberos)
- Ensures accurate TLS certificate validation
- Provides correct timestamps in logs for forensics
- Prevents authentication failures due to clock drift

**Install and configure:** [NTP Configuration Guide](/NTP)

---

## Quick Setup Checklist

For a production-ready SafeSquid deployment:

1. **Install all three services:**
   ```bash
   # Debian/Ubuntu:
   sudo apt install -y monit bind9 chrony
   
   # RHEL/CentOS:
   sudo dnf install -y monit bind chrony
   ```

2. **Configure Monit:**
   - Add SafeSquid process check
   - Enable port 8080 monitoring
   - Configure auto-restart

3. **Configure BIND:**
   - Point to root DNS servers
   - Enable recursion for internal networks only
   - Configure local zone overrides

4. **Configure NTP/Chrony:**
   - Point to enterprise NTP servers or domain controllers
   - Verify time synchronization within 5 minutes of AD

5. **Enable all services:**
   ```bash
   sudo systemctl enable --now monit
   sudo systemctl enable --now bind9  # or named
   sudo systemctl enable --now chronyd
   ```

6. **Verify:**
   ```bash
   # Monit:
   monit summary
   
   # BIND:
   dig @127.0.0.1 example.com
   
   # NTP:
   chronyc tracking
   ```

---

## Source register

| Topic | Status | Source |
| ----- | ------ | ------ |
| Monit / BIND / NTP roles for SafeSquid | **Confirmed** | This hub, linked service guides |
| Kerberos clock skew “5 minutes” rule | **Confirmed** | Common AD constraint; align with [NTP](/NTP) and AD docs |
| Package names (`bind9` vs `named`) | **Confirmed** | Distribution-specific; commands on this page |

---

## Next Steps

1. **Configure each service** using the detailed guides above
2. **[SSL Inspection](/SSL_Inspection)** — NTP is critical for TLS validation
3. **[Authentication](/Authentication)** — NTP is required for SSO/Kerberos
4. **[Audit & Forensics](/Audit_Forensics)** — Accurate timestamps for compliance
