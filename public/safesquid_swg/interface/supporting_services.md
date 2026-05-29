---
title: Supporting Services
description: Supporting Services reference and operational guidance for SafeSquid SWG administrators.
keywords:
  - supporting services
  - SafeSquid
  - concepts
---

# Supporting Services

Supporting services ensure SafeSquid SWG operates reliably, performs well, and maintains accurate time synchronization.

**Critical for production:** These services prevent downtime, improve DNS performance, and ensure authentication works correctly.

## Why You Need These Services

| Service | Purpose | What Happens Without It |
| --- | --- | --- |
| Monit | Process monitoring and auto-restart | SafeSquid crashes stay down until manual restart |
| BIND | Local DNS resolver with caching | Slow DNS lookups, dependency on external resolvers |
| NTP | Time synchronization | SSO fails, TLS certificate errors, log timestamps incorrect |

## Service Guides

### Monit

**Automated monitoring and self-healing** for SafeSquid and dependent processes.

**What it does:**

- Auto-restarts SafeSquid if it crashes

- Monitors port 8080 for responsiveness

- Cleans up temporary files and rotates logs

- Fetches threat intelligence updates

- Triggers housekeeping tasks

**Install and configure:** [Monit Configuration Guide](/safesquid_swg/interface/supporting_services_monit)

### BIND

**Local DNS resolver** for fast, reliable domain resolution.

**What it does:**

- Caches DNS responses for faster lookups

- Reduces dependency on external DNS servers

- Improves consistency and auditability

- Enables local DNS overrides for internal domains

**Install and configure:** [BIND Configuration Guide](/safesquid_swg/interface/bind)

### NTP

**Time synchronization** critical for authentication and TLS validation.

**What it does:**

- Keeps system time within 5 minutes of Active Directory (required for SSO/Kerberos)

- Ensures accurate TLS certificate validation

- Provides correct timestamps in logs for forensics

- Prevents authentication failures due to clock drift

**Install and configure:** [NTP Configuration Guide](/safesquid_swg/interface/ntp)

## Quick Setup Checklist

For a production-ready SafeSquid deployment:

1. **Install all three services:** `# Debian/Ubuntu: sudo apt install -y monit bind9 chrony # RHEL/CentOS: sudo dnf install -y monit bind chrony`

2. **Configure Monit:** Add SafeSquid process check Enable port 8080 monitoring Configure auto-restart

3. **Configure BIND:** Point to root DNS servers Enable recursion for internal networks only Configure local zone overrides

4. **Configure NTP/Chrony:** Point to enterprise NTP servers or domain controllers Verify time synchronization within 5 minutes of AD

5. **Enable all services:** `sudo systemctl enable --now monit sudo systemctl enable --now bind9 # or named sudo systemctl enable --now chronyd`

6. **Verify:** `# Monit: monit summary # BIND: dig @127.0.0.1 example.com # NTP: chronyc tracking`

## Next Steps

1. **Configure each service** using the detailed guides above

2. **[SSL Inspection](/use_cases/ssl_inspection/ssl_inspection)**  -  NTP is critical for TLS validation

3. **[Authentication](/use_cases/authentication/authentication)**  -  NTP is required for SSO/Kerberos

4. **[Audit & Forensics](/use_cases/audit_and_forensics/audit_forensics)**  -  Accurate timestamps for compliance

## Next steps

- Use [BIND](/safesquid_swg/interface/bind) to operate local DNS services.
- Use [NTP](/safesquid_swg/interface/ntp) to keep logs and authentication time-aligned.
