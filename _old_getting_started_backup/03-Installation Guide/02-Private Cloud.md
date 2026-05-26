---
title: Private Cloud
description: "Deploy SafeSquid SWG in cloud environments: procedures and considerations."
keywords:
  - Install Secure Web Gateway on the cloud
  - Cloud-based SafeSquid SWG deployment
  - SafeSquid cloud SWG
  - Cloud-agnostic web gateway
  - Secure Web Gateway for remote workforce
---

## Adapting IT Infrastructure for Cloud Security

Like most business organizations yours too started with an IT infrastructure designed for a shared workplace. The digital landscape thus had a common perimeter, and on‑premise security measures made logical sense. For scaling the Layer‑7 security you too may have setup a load‑balanced cluster of proxy servers to provide Secure Web Gateway for your workforce.

The digital landscape changes as your organization grows, necessitating changes to the legacy Infrastructure. This manifests particularly when your organization needs to provide geographically distributed workplaces. Escalating cost of managing IT infrastructure for workplaces shared among a small worker group is not easy to justify. Security measures specially like Application Layer Defense require significantly more experienced security technicians, thus dedicating one for a small network may not find easy approval from management.

Your organization too like most organizations may have initially opted to backhaul the traffic to the head office in the early 2000's but later opted to moving the IT infrastructure to commonly accessible data‑centers.

Cloud based IaaS or PaaS present a more cost‑efficient alternative, requiring regular Internet connectivity instead of the more expensive network links. If your organization too has multiple small offices and workers that need to access the organization's information systems, employing such Cloud based private infrastructure, could be a very acceptable idea.

If you have already moved your Information Systems to Cloud based PaaS / IaaS, moving your SWG to the same Cloud service could be a very beneficial.

## On-Premises SWG Struggles with Distributed Workforces

Traditionally, all your employees worked from the headquarters. All your web traffic was routed through a single LAN gateway. To secure the web traffic, an on-premise Secure Web Gateway (SWG) appliance was deployed at the gateway, creating a well-defined network perimeter.

As you expanded globally, you adopted BYOD and remote work policies, causing web traffic to originate from remote endpoints outside your central LAN. The shift dissolved your well-defined perimeter, prompting you to backhaul traffic through your central LAN for on-premise SWG inspection, resulting in a hairpinning pattern.

Hairpinning forced your traffic into inefficient detours, significantly increasing latency and doubling the data volume passing through your single gateway. The degradation impacted user experience, contributed to network congestion, and drove up bandwidth usage and costs.

![Install SafeSquid SWG on cloud or virtual machine](/img/Install_SWG_on_Cloud/image1.webp)

## Shift from On-premises to Cloud SWG

To eliminate the need for backhauling, you transitioned to a cloud SWG model. Remote workers' traffic is now routed directly to the nearest SWG instance, while traffic from remote offices is consolidated at edge devices like an SD-WAN edge controller before reaching the cloud SWG. The shift allows you to enforce centralized security policies across distributed SWG locations such as using SD-WAN overlays to secure and optimize traffic flows dynamically. Inspected traffic is then routed directly to the Internet.

By adopting cloud SWG, you have:

1. Eliminated reliance on N+1 redundancy, simplifying infrastructure.
2. Decentralized traffic inspection, reducing bottlenecks and latency.
3. Leveraged cloud scalability to dynamically allocate resources based on demand.
4. Shifted to a pay-as-you-go model, cutting capital expenses, and aligning costs with actual usage.

## What to Look for in a Cloud SWG Solution

**Ensure Interoperability** When you choose a non-interoperable Cloud SWG, integration with your existing infrastructure becomes disrupted, leading to administrative overhead. Ensuring seamless compatibility with your networking, identity, and security systems allows for consistent enforcement and operational efficiency.

**Optimize Control in SWG Architecture** You adopt multi-tenant SWG for simplified management. However, restricted payload inspection, standardized security policies, and shared resource constraints create operational limitations. Single-tenant SWG offers you greater control, enabling deep traffic inspection, custom security policies, and dedicated resource allocation for enhanced security.

**Avoid Vendor Lock-In** Relying on a vendor-controlled Cloud SWG, customization, and flexibility increase your dependency on a single provider, and migration becomes restricted. Proprietary architectures limit policy adjustments and multi-cloud integration. Choosing a provider-agnostic SWG gives you greater adaptability and long-term scalability.

**Evaluate Outbound Data Transfer Costs** Cloud providers charge per GB for outbound traffic from your Cloud SWG to the internet, while inbound and return traffic are typically free. Inter-cloud and inter-region transfers incur additional costs, increasing expenses in multi-cloud and hybrid deployments. Assessing data flow and provider pricing helps you control bandwidth costs.

## SafeSquid SWG: The Cloud-Agnostic Solution

1. SafeSquid SWG simplifies cloud adoption, enabling seamless integration with your preferred cloud platform.
2. Instant deployment capability reduces setup time and complexity, allowing for a quick and efficient start.
3. By optimizing web traffic performance, SafeSquid SWG helps minimize latency and ensures a smoother user experience.
4. Reduces bandwidth consumption, significantly lowering operational costs and improving resource efficiency.
5. With support for multi-cloud connectivity, SafeSquid SWG offers greater flexibility to adapt to diverse cloud environments and organizational needs.

## Cloud Deployment Options for SafeSquid SWG

There are 4 ways to deploy SafeSquid Secure Web Gateway on cloud platforms.

### Cloud-IMG framework

[The SafeSquid Cloud-IMG](http://downloads.safesquid.com/appliance/cloud-img/safesquid-swg.img) framework allows for quick deployment of SafeSquid-SWG with minimal configuration using custom image ingestion.

### Cloud-Init framework

[SafeSquid's cloud-init](https://github.com/SafeSquid-Github/safesquid_cloud-init/blob/main/safesquid_cloud-init.yaml) script ensures installation and configuration on clouds including Microsoft Azure, AWS, and Digital Ocean.

### Deployment on existing VM

#### [SafeSquid Appliance Builder](/docs/Getting%20Started/Installation%20Guide/SafeSquid%20Appliance%20Builder)

SAB is an ISO of the latest minimal Ubuntu LTS 20.04, designed to simplify deployment in environments where full automation is not feasible. SAB automates the installation of Ubuntu, followed by downloading and deploying SafeSquid SWG, streamlining the setup process.

#### TAR-ball Package

SafeSquid SWG can be set up on existing infrastructure or with a Linux OS other than Ubuntu using the TAR package. Additional configurations are required for services such as Monit and BIND9 to ensure proper functionality and seamless integration.

## Validation

Gain the console or CLI access to the SWG server and execute the following commands to verify the SWG status:

```jsx npm2yarn
netstat -lntp
```

```jsx npm2yarn
/etc/init.d/SafeSquid status
```

```jsx npm2yarn
Lsblk
```

## Prevent unauthorized SWG access on cloud

**Identity & Access Management (IAM) Enforcement** Implement Multi-Factor Authentication (MFA), Role-Based Access Control (RBAC), and Directory-Based Authentication using cloud-native IAM services and on-premises directory solutions.

**Secure Access Control (SAC)** Require Virtual Private Network (VPN) and Zero Trust Network Access (ZTNA) to authenticate users through secure access gateways and enterprise VPN solutions.

**Network Security & Threat Prevention** Restrict SWG access using Cloud Security Groups, Firewalls, Intrusion Prevention Systems (IPS), and Intrusion Detection Systems (IDS) with geo-blocking and anomaly detection.

**Network Segmentation & Private Connectivity** Implement Virtual Private Cloud (VPC), Virtual Network (VNet), VLAN Segmentation, and Network Access Control (NAC) to isolate SWG and prevent unauthorized exposure.
