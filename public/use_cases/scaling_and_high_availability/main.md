---
title: Scaling & High Availability
description: Find the SafeSquid guides for scaling and high availability, from proxy modes to clustering and backup.
keywords:
  - scaling and high availability
  - SafeSquid documentation
---

# Plan Scaling and High Availability

One node is a single point of failure and a ceiling on capacity.

## Quickstart path

1. **[Choose an Architecture](/deployment/choose_an_architecture)** - decide where SafeSquid intercepts traffic — forward, transparent, TCP, reverse, or chained — and what each choice costs you in client configuration, coverage, and bypass risk.
2. **[Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering)** - scale SafeSquid with master-slave clustering, configuration sync, and load balancer integration for high availability and horizontal scaling.
3. **[Backup Strategy](/use_cases/scaling_and_high_availability/disaster_recovery)** - decide what SafeSquid backs up, what it does not, and what the disaster-recovery plan must cover separately before the deployment depends on Cloud Restore.
4. **[Master-Slave](/use_cases/scaling_and_high_availability/master_slave)** - configure SafeSquid master-slave architecture for centralized policy sync and reporting across slave instances.
5. **[VPN Integration](/use_cases/scaling_and_high_availability/vpn)** - configure and manage VPN settings for SafeSquid Web Security Clients via Self-Service Portal, including FQDN setup and verification.
6. **[WCCP](/use_cases/scaling_and_high_availability/wccp)** - configure SafeSquid with Cisco WCCP to enable seamless transparent redirection, ensuring proxy-free client setups, load balancing, high availability, and scalable web traffic management.
7. **[Forward Proxy](/use_cases/scaling_and_high_availability/forward_proxy)** - configure web browsers to use SafeSquid proxy server, including detailed steps for Chrome and Firefox proxy settings to access the SafeSquid WebGUI.
8. **[Proxy Chain](/use_cases/scaling_and_high_availability/proxy_chain)** - deploy SafeSquid behind a parent proxy with proxy chaining, HTTPS inspection, and request forwarding for enterprise integration.
9. **[Reverse Proxy](/use_cases/scaling_and_high_availability/reverse_proxy)** - configure SafeSquid as reverse proxy for performance, SSL termination, security, and caching without client proxy settings.
10. **[TCP Proxy](/use_cases/scaling_and_high_availability/tcp_proxy)** - configure SafeSquid TCP Proxy mode to handle non-HTTP TCP connections, enabling secure proxying of various TCP-based protocols and applications.
11. **[Transparent Proxy](/use_cases/scaling_and_high_availability/transparent_proxy)** - deploy SafeSquid in transparent proxy mode to intercept HTTP/HTTPS without client config for policy enforcement and SSL inspection.

## Next steps

- **[Performance Accelerators](/use_cases/performance_acceleration/performance_accelerators)** - use SafeSquid performance accelerators such as caching, prefetching, bandwidth management, speed limits, and WCCP with deployment-aware expectations.
- **[Upgrade SafeSquid](/use_cases/upgrade/version_upgrade)** - upgrade SafeSquid SWG via Web GUI: prerequisites, cleanup, and applying the new tarball package.
