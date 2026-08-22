---
title: Proxy Clustering
slug: /Proxy_Clustering
description: Scale SafeSquid with master-slave clustering, configuration sync, and load balancer integration for high availability and horizontal scaling.
keywords:
  - SafeSquid proxy clustering
  - SafeSquid high availability
  - SafeSquid master-slave setup
  - proxy failover configuration
  - SafeSquid configuration sync
  - enterprise proxy scaling
---


# Master-slave clustering for high availability

SafeSquid supports clustered deployments for high availability, failover, and horizontal scaling. A master node holds policy and reporting; slave nodes enforce policy and forward data. Use a load balancer in front of slaves for distribution and failover.

## When to use clustering

| Scenario | Solution | Benefit |
|---|---|---|
| Single proxy is overwhelmed by traffic | Add slave nodes behind load balancer | Distribute load horizontally |
| Proxy downtime causes network outage | Master-slave with failover | High availability |
| Managing policies on multiple proxies | Configuration sync from master | Consistent enforcement across nodes |
| Compliance requires centralized reporting | Master aggregates slave data | Unified audit trail |

## Prerequisites

- Same SafeSquid version on all nodes
- Same activation key on master and slaves
- Network connectivity: slaves can reach master Configuration Portal (port 8888 by default)
- Load balancer configured to distribute traffic to slave nodes (not to master)
- Time synchronization (NTP) across all nodes

## Architecture overview

**Master node:**
- Hosts Configuration Portal for policy management
- Aggregates reporting data from slaves
- Does NOT process client traffic directly

**Slave nodes:**
- Enforce policies synced from master
- Process client traffic
- Forward reporting data to master

**Load balancer:**
- Distributes client requests across slave nodes
- Provides failover if a slave goes down
- Does NOT route to master (master is for management only)

The documents below cover master-slave setup and configuration sync.



## Clustering configuration guides

### [Master-Slave](/docs/Proxy_Clustering/Master_Slave/)
Single-node deployments lack failover and scale limits. Master-Slave describes how to configure a master node for policy and reporting and slave nodes for traffic enforcement. Centralized policy and unified reporting reduce administrative overhead. Follow this document to set up master-slave relationships.

### [Configuration Sync](/docs/Proxy_Clustering/Configuration_Sync/)
Configuration drift across nodes causes inconsistent enforcement and troubleshooting difficulty. Configuration Sync enables automatic propagation of policy and configuration from master to slaves. All nodes stay aligned without manual copy. Configure sync using this document.

## Next steps

Place a load balancer in front of slave nodes; see [Disaster Recovery](/docs/Disaster_Recovery/main/) for backup and restore, and [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/) for post-cluster validation.
