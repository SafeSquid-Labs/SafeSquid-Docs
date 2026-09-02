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

## Problem statement

Single-node deployments create both scale risk and availability risk. Clustering is the documented way to reduce that risk while keeping policy consistent across enforcement nodes.

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
{/* source: live UI verification, Support → Startup params, and use_cases/scaling_and_high_availability/master_slave.md's own screenshot evidence (image3, image5, image6, image15) */}
{/* NEEDS-SME-REVIEW: this line previously stated the master Configuration Portal listens on "port 8888 by default". No UI section or product log on the verified live instance names 8888. The MASTER_PORT field entered in master_slave.md's own screenshots is 8080, matching the master's configured LISTEN_PORT, and that page's image15 shows a raw sync log recording the actual sync connection as `192.168.221.222:8080` — evidence against 8888 specifically for the master-slave sync channel. This does not resolve the separate ":8888" address question flagged on use_cases/customisation/configure_cloud_restore.md (external Configuration Portal access URL) — confirm whether that is a distinct, genuine listener before reconciling the two pages. */}
- Network connectivity: slaves can reach the master's configured proxy port (the same LISTEN_PORT the master serves its Configuration Portal on — 8080 in verified evidence; confirm the actual value on your master under Support → Startup params)
- Load balancer configured to distribute traffic to slave nodes (not to master)
- Time synchronization (NTP) across all nodes
- A reporting plan so evidence from all active nodes remains visible

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

Internal product knowledge confirms automatic policy replication across cluster nodes and no documented hard ceiling on total cluster node count. Treat single-instance capacity and cluster capacity as separate planning questions.

## Verification and validation

After clustering is configured, validate:

- policy changes replicate to every node
- the load balancer does not send client traffic to the master
- a failed slave is removed from active service
- reporting still captures traffic from each surviving node
- authentication and SSL inspection behavior remain consistent across nodes

The documents below cover master-slave setup and configuration sync.



## Clustering configuration guides

### [Master-Slave](/Master_Slave)
Single-node deployments lack failover and scale limits. Master-Slave describes how to configure a master node for policy and reporting and slave nodes for traffic enforcement. Centralized policy and unified reporting reduce administrative overhead. Follow this document to set up master-slave relationships.

### [Configuration Sync](/Configuration_Sync)
Configuration drift across nodes causes inconsistent enforcement and troubleshooting difficulty. Configuration Sync enables automatic propagation of policy and configuration from master to slaves. All nodes stay aligned without manual copy. Configure sync using this document.

## Next steps

Place a load balancer in front of slave nodes; see [Disaster Recovery](/Disaster_Recovery) for backup and restore, and Verify your setup for post-cluster validation.
