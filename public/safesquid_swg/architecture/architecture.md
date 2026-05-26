---
title: Architecture
description: SafeSquid SWG architecture — deployment model, traffic flow, proxy cluster, intelligence feeds, supporting services, and operational integration points.
keywords:
  - SafeSquid architecture
  - proxy cluster
  - deployment topology
  - traffic flow
  - intelligence feeds
  - reporting
  - DNS security
---

# Architecture

SafeSquid SWG is not a single feature or console. It is a software-defined Secure Web Gateway architecture that places an HTTP(S) proxy cluster on the enterprise egress path, enriches traffic decisions with cloud-delivered intelligence, and gives operations teams the supporting services needed to run inspection safely in production.

## Understand the control boundary first

The architecture matters because SafeSquid changes where web control is enforced, where TLS inspection occurs, where evidence is generated, and which dependencies must be available during deployment.

At a high level, the canonical topology includes:

- SafeSquid Proxy Cluster as the central enforcement point
- enterprise-side components such as users, workstations, application servers, and directory services
- internet egress through the network firewall
- cloud-based intelligence feeds for URL, SSL, malware, application, image, and threat updates
- supporting operational services for reporting, licensing, DNS, backup, and monitoring

This matters operationally because a Secure Web Gateway is only as reliable as the dependencies around it. If time sync fails, Kerberos and TLS validation break. If DNS is misaligned, web access and threat lookups fail. If reporting is ignored, the control exists but cannot be proved to auditors or incident responders.

## Follow the main architecture path

Use this sequence to understand the platform:

1. [SafeSquid SWG Overview](/safesquid_swg/architecture/safesquid_swg) for the main product components and deployment model.
2. [Application Ecosystem](/Application_Ecosystem) for supporting services, feed dependencies, reporting, and portal relationships.
3. [SafeSquid Proxy Cluster](/SafeSquid_Proxy_Cluster) for scale-up, scale-out, and policy replication.
4. [Integrated DNS Security](/Integrated_DNS_Security) for DNS-layer enforcement and tunnelling risk.

## Know what this page does not replace

This page is the architecture hub. It does not replace deployment runbooks such as [Deployment Planning](/Deployment_Planning), [Cloud Deployment](/Cloud_Deployment), [SafeSquid Appliance Builder](/SafeSquid_Appliance_Builder), or [Linux Server](/Linux_Server).

## Next steps

- [SafeSquid SWG Overview](/safesquid_swg/architecture/safesquid_swg)
- [Proxy Clustering](/Proxy_Clustering)
- [Deployment Planning](/Deployment_Planning)
- [Getting Started](/Getting_Started)
