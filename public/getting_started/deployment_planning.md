---
title: Deployment Planning
description: Size and prepare SafeSquid SWG infrastructure, routing, resilience, and evidence retention before installation.
keywords:
  - SafeSquid deployment planning
  - SafeSquid sizing
  - SafeSquid hardware requirements
  - proxy high availability
  - secure web gateway planning
---

# Plan the Control Path First

SafeSquid becomes a production control only when the proxy is sized, reachable, monitored, and able to preserve enforcement evidence. Poor planning causes dropped sessions, weak audit trails, certificate failures, and emergency routing changes during rollout.

## Capture deployment requirements

Record these inputs before selecting hardware or topology:

- User count and estimated peak concurrent connections.
- Expected HTTPS inspection scope.
- Client networks, VLANs, and egress firewall paths.
- Directory service and authentication method.
- Root CA rollout method for SSL inspection.
- Log retention target and SIEM or Reporting Service destination.
- Availability target and rollback owner.

## Size the first node

Use peak concurrent connections, not average users, for sizing. If only user count is known, estimate `3` to `5` concurrent connections per active user for general office traffic. Heavy SaaS, browser-tab, or streaming environments need a higher measured estimate.

Published reference tiers for SSL-inspected deployments:

| CPU | RAM | Disk | Max concurrent connections | Approximate users |
|---|---:|---:|---:|---:|
| 4 cores | 8 GB | 500 GB | 100 | 25 |
| 4 cores | 16 GB | 1 TB | 500 | 150 |
| 8 cores | 16 GB | 2 TB | 1,000 | 350 |
| 8 cores | 32 GB | 4 TB | 1,500 | 600 |
| 16 cores | 32 GB | 4 TB | 2,000 | 1,000 |
| 16 cores | 64 GB | 8 TB | 2,500 | 1,500 |

SafeSquid has a confirmed per-instance ceiling of `5,000` concurrent connections. Plan clustering before approaching that boundary. Do not cite unverified throughput figures as tested performance.

## Plan platform baseline

For new deployments, use [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) where possible. The confirmed SAB minimum is:

- `8+` CPU cores.
- `8 GB+` RAM.
- `4+` network interfaces.
- `50 GB+` disk.
- Debian 13 (Trixie) x86_64 as the primary baseline.

Current Ubuntu LTS releases are supported in parallel. Existing Linux server installs require local ownership of OS hardening, service monitoring, and dependency management.

## Design network placement

Define traffic paths before installation:

- Client networks that may connect to SafeSquid proxy ports.
- Management networks that may access the Configuration Portal.
- Upstream firewall rules for internet, licensing, updates, and intelligence services.
- DNS and NTP sources.
- Direct egress blocks or controls that prevent client bypass.
- Optional load balancer or cluster path for high availability.

Do not expose the proxy listener to the public internet. Restrict `8080/tcp` to approved client networks.

## Plan logs and evidence

SafeSquid evidence supports incident response and audit only if logs are retained and searchable. Decide before go-live:

- Local disk allocated to `/var/log/safesquid/`.
- Reporting Service or SIEM forwarding owner.
- Retention period for access logs and policy evidence.
- Alert owner for disk usage, service health, and feed/update failures.
- Export method for audit requests.

## Choose deployment scenario

| Scenario | Use when | Production note |
|---|---|---|
| Single-node pilot | Lab, evaluation, or small pilot | Not high availability; define production path before rollout |
| Branch deployment | One site or limited user group | Size to peak traffic and validate local support coverage |
| Clustered deployment | Outage cannot stop web access | Plan load balancing, configuration sync, and monitoring |
| Cloud deployment | Cloud-first or off-premises sites | Restrict ingress and use resilient storage |
| Disaster recovery | Regional outage must preserve web security | Test failover and policy consistency on a schedule |

## Verify readiness

Before installation, confirm:

```bash
ping -c 3 key.safesquid.com
nslookup key.safesquid.com
timedatectl status
```

Also verify firewall approvals, certificate rollout ownership, and storage allocation for logs.

## Capture planning evidence

Attach these to the change record:

- Sizing calculation and selected reference tier.
- Network diagram or traffic-flow note.
- Firewall rule request and approval.
- Certificate trust rollout plan.
- Log retention and SIEM or Reporting Service plan.
- Rollback path for routing and client proxy changes.

## Next steps

- [Prerequisites](/getting_started/install_safesquid/prerequisites) - confirm host and network readiness.
- [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) - deploy the standard appliance path.
- [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) - deploy in public or private cloud.

