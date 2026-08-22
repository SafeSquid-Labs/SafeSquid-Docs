---
title: Install SafeSquid
slug: /Getting_Started/Install_SafeSquid
description: Choose an installation method for SafeSquid — Appliance Builder (SAB), cloud deployment, or Linux TAR package.
keywords:
  - SafeSquid installation
  - SafeSquid Appliance Builder
  - SAB
  - SafeSquid cloud deployment
  - SafeSquid TAR install
---

# Install SafeSquid

SafeSquid offers three installation paths depending on your infrastructure:

- **Appliance Builder (SAB)** — Full turnkey image (OS + SafeSquid + services) for bare metal or VM
- **Cloud Deployment** — Deploy on AWS, Azure, DigitalOcean, or private cloud
- **Linux Server** — Install SafeSquid on an existing Linux server using TAR package

All methods produce an operational node ready for license activation and client connectivity.

:::info Prerequisites

- Complete [Deployment Planning](/docs/Getting_Started/Deployment_Planning/) to size hardware and prepare your environment
- Download your [activation key](/docs/Getting_Started/Register/) (you'll need it after installation)
- Server or VM meeting [hardware requirements](/docs/Getting_Started/Deployment_Planning/#hardware-sizing)

:::

## Which Method Should I Use?

| **Environment** | **Recommended Method** | **Why** |
|-----------------|------------------------|---------|
| New bare metal server | [SafeSquid Appliance Builder](/docs/Getting_Started/Install_SafeSquid/SafeSquid_Appliance_Builder/) | Turnkey image with hardened OS and all dependencies |
| New VM (VMware, Hyper-V, KVM) | [SafeSquid Appliance Builder](/docs/Getting_Started/Install_SafeSquid/SafeSquid_Appliance_Builder/) | Pre-configured networking, monitoring, and DNS |
| AWS, Azure, DigitalOcean | [Cloud Deployment](/docs/Getting_Started/Install_SafeSquid/Cloud_Deployment/) | Cloud-optimized images and cloud-init support |
| Existing Linux server | [Linux Server](/docs/Getting_Started/Install_SafeSquid/Linux_Server/) | Minimal footprint; you manage OS and services |
| Private cloud (OpenStack, Proxmox) | [SafeSquid Appliance Builder](/docs/Getting_Started/Install_SafeSquid/SafeSquid_Appliance_Builder/) | Complete appliance for self-managed infrastructure |

**Still unsure?** Start with [Deployment Planning](/docs/Getting_Started/Deployment_Planning/) to size hardware and plan topology.

## Installation Methods

### [SafeSquid Appliance Builder](/docs/Getting_Started/Install_SafeSquid/SafeSquid_Appliance_Builder/)

**Recommended for new deployments.** SAB builds a turnkey ISO with a security-hardened OS, SafeSquid, Monit, BIND9, and optimized disk layout. Boot from ISO, answer a few prompts, and deploy.

**Use this when:** You need a complete appliance on bare metal or a new VM.

**Installation time:** ~15-20 minutes (10 min prompts + 5-10 min automated install).

---

### [Cloud Deployment](/docs/Getting_Started/Install_SafeSquid/Cloud_Deployment/)

Deploy SafeSquid on AWS, Azure, DigitalOcean, or private cloud using cloud images or cloud-init. Full policy and inspection capabilities in the cloud with auto-scaling and cloud-native networking.

**Use this when:** You're deploying to public or private cloud infrastructure.

**Installation time:** ~10-15 minutes (cloud instance provisioning + SafeSquid setup).

---

### [Linux Server](/docs/Getting_Started/Install_SafeSquid/Linux_Server/)

Install SafeSquid from a TAR package on an existing Debian, Ubuntu, or RHEL-based server. You manage OS updates, networking, and supporting services separately.

**Use this when:** You already have a configured Linux server and want to add SafeSquid only.

**Installation time:** ~5-15 minutes (extract TAR + dependency install + service setup).

## After Installation

Once SafeSquid is installed, complete these steps in order:

1. **[Activate Your License](/docs/Getting_Started/Activate/)** — Upload your activation key to make the gateway fully operational
2. **[Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/)** — Configure at least one browser or endpoint to use the proxy
3. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm the service is running, licensed, and proxying traffic

Once verified, proceed to [SSL Inspection](/docs/SSL_Inspection/main/) to enable HTTPS filtering.
