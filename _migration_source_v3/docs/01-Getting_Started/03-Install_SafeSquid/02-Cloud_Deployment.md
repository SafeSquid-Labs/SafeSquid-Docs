---
title: Cloud Deployment
description: Deploy SafeSquid Secure Web Gateway on AWS, Azure, DigitalOcean, or any cloud platform using Cloud-IMG, cloud-init, or SAB ISO.
keywords:
  - SafeSquid cloud deployment
  - SafeSquid cloud-init
  - SafeSquid Cloud-IMG
  - cloud SWG
---

# Cloud Deployment

Deploy SafeSquid on AWS, Azure, DigitalOcean, GCP, or private cloud infrastructure using cloud-native methods (Cloud-IMG or cloud-init) or existing installation methods (SAB ISO or TAR package).

**Recommended:** Use Cloud-IMG or cloud-init for cloud-native automation. Use SAB/TAR only when cloud-init is unavailable or you need a custom OS.

## Why Deploy SafeSquid in the Cloud?

**Backhauling** remote and branch traffic to an on-premises SWG creates latency, doubles bandwidth through the gateway, and degrades user experience.

**Cloud deployment eliminates backhauling:**
- Remote workers route to the nearest cloud SWG instance (reduced latency)
- Traffic from remote offices consolidates at edge devices (SD-WAN) before reaching cloud SWG
- Inspected traffic routes directly to the internet
- Dynamically scale resources based on demand
- Pay-as-you-go model reduces capital expenses
- No single-site dependency

**SafeSquid is cloud-agnostic** — deploy on AWS, Azure, GCP, DigitalOcean, or any private cloud without vendor lock-in.

## Choose an Instance Type

Match your cloud instance to the [hardware sizing matrix](/docs/Getting_Started/Deployment_Planning/#hardware-sizing):

| **Concurrent Connections** | **AWS** | **Azure** | **GCP** |
|-----------------------------|---------|-----------|---------|
| Up to 400 (pilot) | t3.large | Standard_D2s_v3 | e2-standard-2 |
| Up to 1,500 | t3.xlarge | Standard_D4s_v3 | e2-standard-4 |
| Up to 3,000 | c6i.2xlarge | Standard_F8s_v2 | c2-standard-8 |
| 3,000+ | c6i.4xlarge+ | Standard_F16s_v2+ | c2-standard-16+ |

**Storage:** Use NVMe-backed instance storage or premium SSD managed disks (minimum 100 GB).

**Networking:** Ensure instance type supports Enhanced Networking (AWS SR-IOV, Azure Accelerated Networking).

## Deployment Methods

### Cloud-IMG (Recommended)

Import the prebuilt SafeSquid image directly into your cloud platform's custom image system.

**Download:** [safesquid-swg.img](http://downloads.safesquid.com/appliance/cloud-img/safesquid-swg.img)

**Steps:**
1. **Upload** the image to your provider:
   - **AWS:** Import as AMI via VM Import/Export
   - **Azure:** Upload as managed disk, create image
   - **GCP:** Create custom image from disk
   - **DigitalOcean:** Use Custom Images feature
2. **Launch** an instance from the imported image
3. **Access via SSH** with default credentials: `administrator` / `safesquid`

:::caution Change Default Password

Default credentials: **administrator** / **safesquid**

Change immediately after first login: `passwd` or via SafeSquid admin interface.

:::

---

### Cloud-Init

Use the SafeSquid cloud-init script for automated provisioning on any cloud-init-compatible platform.

**Steps:**
1. **Download the cloud-init configuration:**
   ```bash
   curl -O https://raw.githubusercontent.com/SafeSquid-Github/safesquid_cloud-init/main/safesquid_cloud-init.yaml
   ```

2. **Review and customize** the YAML (network settings, hostname, disk layout)

3. **Pass as user-data** when launching your instance:
   - **AWS:** User data field during EC2 launch
   - **Azure:** Custom data in VM creation
   - **GCP:** Metadata → user-data
   - **DigitalOcean:** User data section

4. **Wait for provisioning** (~10-15 minutes). Check progress:
   ```bash
   tail -f /var/log/cloud-init-output.log
   ```

---

### Alternative Methods

**For existing cloud VMs:**
- Use the [TAR package method](/docs/Getting_Started/Install_SafeSquid/Linux_Server/) if you already have a Linux VM

**For platforms without cloud-init:**
- Attach the [SAB ISO](/docs/Getting_Started/Install_SafeSquid/SafeSquid_Appliance_Builder/) to a cloud VM and follow the standard installation

## Verify the Deployment

SSH into the instance and confirm SafeSquid is running:

```bash
# Check SafeSquid service status
systemctl status safesquid

# Verify port 8080 is listening
netstat -lntp | grep 8080
# Expected: safesquid listening on 0.0.0.0:8080

# Check disk partitions (Cloud-IMG only)
lsblk
# Verify /var/log/safesquid and /var/lib/safesquid are mounted
```

**Access the admin interface:**
- Direct: `https://INSTANCE-PUBLIC-IP:8443/`
- Via proxy: `https://safesquid.cfg/` (embedded Rest UI interface built into SafeSquid; accessible via proxy, NOT resolved by DNS)

If the interface loads, deployment succeeded.

## Security Configuration

:::caution Never Expose Port 8080 to Public Internet

Do not allow `0.0.0.0/0` access to port 8080 without authentication and strict access controls.

:::

**Cloud security best practices:**

1. **Security Groups / Firewall Rules:**
   - Allow inbound port 8080 only from trusted IPs (office, VPN, ZTNA gateway)
   - Allow inbound port 8443 (admin) only from admin jump box or VPN
   - Deny all other inbound traffic

2. **Network Topology:**
   - Deploy SafeSquid in a **private subnet** (no direct internet access)
   - Use NAT gateway or internet gateway for outbound traffic only
   - Front with Application Load Balancer (AWS ALB, Azure App Gateway) for HA

3. **IAM and Access Control:**
   - **AWS:** Use IAM roles for EC2 (avoid embedding credentials)
   - **Azure:** Use Managed Identity for VM
   - **GCP:** Use service accounts with least-privilege scopes

4. **Encryption:**
   - Enable disk encryption (AWS EBS encryption, Azure Disk Encryption, GCP persistent disk encryption)
   - Use TLS 1.2+ for admin interface (configure in SafeSquid SSL settings)

5. **Monitoring and Logging:**
   - Forward logs to cloud-native logging (CloudWatch, Azure Monitor, Stackdriver)
   - Enable flow logs on VPC/VNet for traffic visibility
   - Configure alerts for proxy downtime or high connection drops

## High Availability and Auto-Scaling

**For production deployments:**

### Load Balancing

Deploy multiple SafeSquid instances behind a load balancer:

- **AWS:** Network Load Balancer (TCP port 8080) or Application Load Balancer
- **Azure:** Azure Load Balancer or Application Gateway
- **GCP:** TCP/UDP Load Balancer

Configure health checks on port 8080 (HTTP GET to `/`).

### Auto-Scaling

Use cloud auto-scaling groups to match instance count to load:

1. Create a launch template with Cloud-IMG or cloud-init
2. Configure auto-scaling group (min 2, max 10 instances)
3. Set scaling policies based on:
   - CPU utilization (>70% scale up, &lt;30% scale down)
   - Network throughput
   - Connection count (via CloudWatch custom metrics)

### Configuration Sync

Use [Configuration Sync](/docs/Proxy_Clustering/Configuration_Sync/) to replicate policies across instances in the auto-scaling group.

## Troubleshooting

| Symptom | Likely cause | Fix |
| ------- | ------------ | --- |
| Instance not reachable on port 8080 | Security group blocks port | Update security group: allow inbound TCP 8080 from your IP/VPN range |
| Cloud-init script fails | Syntax error or network timeout | SSH to instance, check `/var/log/cloud-init-output.log` for errors |
| Image import rejected | Image format or size | Check provider limits (AWS: 50 GB max, Azure: VHD required); convert with `qemu-img` |
| SafeSquid not listening after boot | Service failed to start | Run `systemctl status safesquid` and check `/var/log/safesquid/safesquid.log` |
| High latency from remote users | Instance in wrong region | Deploy SafeSquid instances in regions closest to users (multi-region) |
| Auto-scaling instances fail health check | Policy sync delay | Ensure new instances pull config from master or S3 bucket on startup |

## Next Steps

1. **[Activate Your License](/docs/Getting_Started/Activate/)** — Upload your activation key to make SafeSquid fully operational
2. **[Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/)** — Configure a browser to use the cloud proxy
3. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm traffic flows through SafeSquid
4. **[Enable SSL Inspection](/docs/SSL_Inspection/main/)** — Decrypt and inspect HTTPS traffic
5. **[Set up HA](/docs/Proxy_Clustering/main/)** — Configure load balancing and failover for production
