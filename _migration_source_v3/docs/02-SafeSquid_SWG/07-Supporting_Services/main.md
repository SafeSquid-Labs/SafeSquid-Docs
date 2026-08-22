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

## Why You Need These Services

| **Service** | **Purpose** | **What Happens Without It** |
|-------------|-------------|------------------------------|
| **[Monit](/docs/SafeSquid_SWG/Supporting_Services/Monit/)** | Process monitoring and auto-restart | SafeSquid crashes stay down until manual restart |
| **[BIND](/docs/SafeSquid_SWG/Supporting_Services/Bind/)** | Local DNS resolver with caching | Slow DNS lookups, dependency on external resolvers |
| **[NTP](/docs/SafeSquid_SWG/Supporting_Services/NTP/)** | Time synchronization | SSO fails, TLS certificate errors, log timestamps incorrect |

---

## Service Guides

### [Monit](/docs/SafeSquid_SWG/Supporting_Services/Monit/)

**Automated monitoring and self-healing** for SafeSquid and dependent processes.

**What it does:**
- Auto-restarts SafeSquid if it crashes
- Monitors port 8080 for responsiveness
- Cleans up temporary files and rotates logs
- Fetches threat intelligence updates
- Triggers housekeeping tasks

**Install and configure:** [Monit Configuration Guide](/docs/SafeSquid_SWG/Supporting_Services/Monit/)

---

### [BIND](/docs/SafeSquid_SWG/Supporting_Services/Bind/)

**Local DNS resolver** for fast, reliable domain resolution.

**What it does:**
- Caches DNS responses for faster lookups
- Reduces dependency on external DNS servers
- Improves consistency and auditability
- Enables local DNS overrides for internal domains

**Install and configure:** [BIND Configuration Guide](/docs/SafeSquid_SWG/Supporting_Services/Bind/)

---

### [NTP](/docs/SafeSquid_SWG/Supporting_Services/NTP/)

**Time synchronization** critical for authentication and TLS validation.

**What it does:**
- Keeps system time within 5 minutes of Active Directory (required for SSO/Kerberos)
- Ensures accurate TLS certificate validation
- Provides correct timestamps in logs for forensics
- Prevents authentication failures due to clock drift

**Install and configure:** [NTP Configuration Guide](/docs/SafeSquid_SWG/Supporting_Services/NTP/)

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

## Next Steps

1. **Configure each service** using the detailed guides above
2. **[SSL Inspection](/docs/SSL_Inspection/main/)** — NTP is critical for TLS validation
3. **[Authentication](/docs/Authentication/main/)** — NTP is required for SSO/Kerberos
4. **[Audit & Forensics](/docs/Audit_Forensics/main/)** — Accurate timestamps for compliance
