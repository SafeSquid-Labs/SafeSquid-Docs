---
title: Cloud Deployment
description: Deploy SafeSquid SWG in a cloud network with controlled ingress, resilient storage, and production evidence checks.
keywords:
  - SafeSquid cloud deployment
  - SafeSquid AWS
  - SafeSquid Azure
  - SafeSquid cloud-init
  - cloud secure web gateway
---

# Deploy SafeSquid in Cloud

Cloud deployment places SafeSquid near cloud workloads, remote users, or hybrid egress paths. The main risks are exposed proxy ports, undersized instances, weak storage planning, and missing high availability. Treat cloud deployment as a network security change, not just an instance launch.

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Why Deploy SafeSquid in the Cloud? */}

## Avoid backhauling remote traffic

Routing remote and branch traffic back to an on-premises gateway before it reaches the internet adds a round trip to every request, consumes bandwidth twice through the gateway link, and degrades the experience for exactly the users who are least able to report it well.

Placing the gateway in the cloud removes that detour:

- Remote workers reach the nearest instance rather than head office.
- Branch traffic consolidates at an edge device, such as an SD-WAN appliance, before reaching the gateway.
- Inspected traffic egresses to the internet directly from the cloud.
- Capacity scales with demand instead of being provisioned for peak.
- Cost shifts from capital purchase to consumption.
- No single site becomes the dependency for every user's internet access.

SafeSquid is cloud-agnostic. The same deployment model applies on AWS, Azure, GCP, DigitalOcean, or a private cloud, without vendor lock-in.

## Use this method when

Use cloud deployment when:

- Cloud workloads must egress through SafeSquid.
- Remote sites or users already route through a cloud network.
- The organization needs fast pilot capacity without hardware procurement.
- Security groups, routing, logging, and snapshots are centrally managed.

Do not use this path when the cloud network cannot restrict proxy access to approved sources.

## Validate prerequisites

Confirm:

- VPC or virtual network routing is approved.
- Security groups restrict proxy and management ports.
- Instance size matches the sizing plan.
- Persistent disk capacity supports logs and updates.
- DNS, NTP, activation, and update paths are reachable.
- Snapshot and rebuild procedures are documented.

## Choose a deployment pattern

<Tabs>
  <Tab title="Cloud-IMG or prebuilt image">
    Use a Cloud-IMG, marketplace, or prebuilt SafeSquid image only when the image source, release, checksum or publisher identity, and update path are approved.

    Record the image ID, region, launch date, SafeSquid version, disk mapping, and initial security group rules. After first boot, verify service state, listener state, DNS resolution, activation reachability, and log creation.

    {/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Cloud-IMG (Recommended) */}

    The prebuilt image is published at:

    ```text
    http://downloads.safesquid.com/appliance/cloud-img/safesquid-swg.img
    ```

    Import it through the provider's custom-image path, then launch an instance from the imported image:

    | Provider | Import path |
    |---|---|
    | AWS | Import as an AMI using VM Import/Export |
    | Azure | Upload as a managed disk, then create an image from it |
    | GCP | Create a custom image from the disk |
    | DigitalOcean | Use the Custom Images feature |

    The image ships with the account `administrator` and the password `safesquid`. Change it at first login with `passwd`, before the instance is reachable from any client network.
  </Tab>
  <Tab title="cloud-init build">
    Use cloud-init when automated instance build is required. Review user data before launch and avoid embedding activation keys, administrator passwords, or certificate private keys in cloud-init text.

    Keep cloud-init focused on baseline OS configuration, package source selection, network settings, log-forwarder bootstrap, and management hardening. Upload the `activation_key` through the approved SafeSquid activation workflow after the instance is reachable.

    {/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Cloud-Init */}

    Retrieve the published cloud-init configuration:

    ```bash
    curl -O https://raw.githubusercontent.com/SafeSquid-Github/safesquid_cloud-init/main/safesquid_cloud-init.yaml
    ```

    Review and adjust the network settings, hostname, and disk layout before use, then pass it as user data at launch:

    | Provider | User-data field |
    |---|---|
    | AWS | User data, during EC2 launch |
    | Azure | Custom data, during VM creation |
    | GCP | Metadata, key `user-data` |
    | DigitalOcean | User data section |

    Follow provisioning from the instance:

    ```bash
    tail -f /var/log/cloud-init-output.log
    ```

    Expected result: the log reaches completion without error. A cloud-init failure often leaves a reachable instance running no proxy at all, so check this before assuming the launch succeeded.
  </Tab>
  <Tab title="Existing cloud VM">
    Use an existing cloud VM only when the operating system lifecycle is already owned. Confirm dependencies, hardening, backup, monitoring, and rollback before installing SafeSquid.

    Existing VMs need extra review for local services that may conflict with the proxy listener, disk layouts that cannot handle logs, and security groups that were created for a different workload.
  </Tab>
</Tabs>

## Secure cloud networking

Before routing clients, enforce:

- No public `0.0.0.0/0` access to proxy or management ports.
- Management access limited to approved admin networks.
- Egress allowed only where needed for activation, updates, DNS, NTP, and business routing.
- Cloud flow logs or equivalent network evidence enabled where required.
- Route tables reviewed by the network owner.

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Security Configuration */}

<Accordion title="Network topology, identity, and encryption">

**Topology.** Place SafeSquid in a private subnet with no direct inbound internet path. Give it outbound access through a NAT gateway, and front it with a load balancer when clients must reach it from outside the VPC. The proxy needs to reach the internet; the internet does not need to reach the proxy.

**Instance identity.** Do not embed long-lived cloud credentials on the instance. Use the platform's workload identity mechanism instead:

| Provider | Mechanism |
|---|---|
| AWS | IAM role attached to the EC2 instance |
| Azure | Managed Identity assigned to the VM |
| GCP | Service account with least-privilege scopes |

**Encryption at rest.** Enable volume encryption — EBS encryption, Azure Disk Encryption, or GCP persistent-disk encryption. SafeSquid volumes hold access logs that identify users and destinations, so treat them as sensitive data at rest, not as operational scratch.

**Transport for management.** Require TLS 1.2 or higher on the management interface.

{/* NEEDS-SME-REVIEW: no menu section named "SSL settings" (or similar) exists in the live safesquid.cfg admin UI as of 2026-08-28 — SSL/TLS-related controls only appear as individual Access Profile rule entries (e.g. "BYPASS SSL INSPECTION", "ALLOW SELF SIGNED SSL CERTIFICATE"), not as a distinct management-interface TLS-version setting. Confirm whether minimum TLS version for the management interface is actually admin-UI-configurable, or is a server/OS-level setting outside this page's scope, and update this claim accordingly. */}

**Logging.** Forward SafeSquid logs to the platform's logging service — CloudWatch, Azure Monitor, or Cloud Logging — and enable VPC or VNet flow logs for network-level visibility. Alert on proxy downtime and on sustained connection-drop rates.

</Accordion>

<Accordion title="Load balancing and auto-scaling guidance">
  Use load balancers only when the selected traffic model is compatible with proxy semantics, source attribution, health checks, and authentication. Record how clients reach the proxy, how failed nodes are removed, and how logs preserve user and source identity.

  Auto-scaling is suitable only when configuration, activation context, certificate trust, logging, and policy state can be synchronized before a node receives traffic. Do not scale out stateless instances that cannot enforce the same policy and logging behavior as the active node.

  {/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Load Balancing */}

  Where a load balancer is used, configure the health check against the proxy listener on port `8080` using an HTTP `GET` to `/`. A check that only tests TCP reachability will keep sending traffic to an instance whose proxy has stopped answering.

  Per-platform options are the Network or Application Load Balancer on AWS, Azure Load Balancer or Application Gateway, and the TCP/UDP load balancer on GCP.

</Accordion>

<Accordion title="Configuration sync expectations">
  Production cloud deployments need a repeatable way to keep policy and operational state consistent:

  - Use the same activation context where cluster or synchronized behavior requires it.
  - Preserve configuration backups outside the instance disk.
  - Define when policy is promoted from pilot to production nodes.
  - Test restore into a replacement instance before relying on snapshots for DR.
  - Confirm certificates, Root CA material, and logging configuration are included or deliberately excluded.
</Accordion>

## Verify deployment

Check DNS and activation reachability:

```bash
nslookup key.safesquid.com
```

Check service health:

```bash
systemctl status safesquid --no-pager
```

Check listener state:

```bash
ss -lntp | grep ':8080'
```

Expected result: DNS resolves, SafeSquid runs, and the proxy listener is present only on approved interfaces.

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Verify the Deployment */}

When the instance was launched from a prebuilt image, confirm the dedicated volumes actually mounted:

```bash
lsblk
```

Expected result: `/var/log/safesquid` and `/var/lib/safesquid` appear as mounted filesystems. If they are folded into the root volume instead, log growth will fill the OS disk and take the service down with it.

## Plan availability

For production cloud egress, document:

- Availability zone placement.
- Health-check method.
- Failover route or load-balancer behavior.
- Same activation key usage across nodes where synchronization is required.
- Snapshot and restore procedure.
- Log forwarding destination.

## Capture deployment evidence

Store:

- Cloud account and region.
- Instance identifier, image source, and launch method.
- Security group and route table approvals.
- Service and listener checks.
- Activation key storage reference.
- Snapshot or rebuild plan.
- First pilot access-log entry.

## Troubleshoot cloud issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Proxy is reachable publicly | Security group source is too broad | Restrict source CIDRs before continuing |
| Activation fails | Egress or DNS is blocked | Restore DNS and outbound subscription reachability |
| Clients cannot reach proxy | Route table or security group is wrong | Verify source network, route, and listener port |
| Logs fill disk | Disk size or retention is too small | Increase disk, adjust retention, or forward logs |
| Image import is rejected | Format or size is outside the provider's limits | Check the provider's import constraints and convert the image with `qemu-img` if a different format is required |
| Remote users see high latency | The instance is in a distant region | Deploy instances in regions close to the user population rather than routing everyone to one region |
| Auto-scaled instances fail the health check | New nodes serve traffic before policy and activation state sync | Ensure instances pull configuration on startup and only join the pool once the proxy answers |
| cloud-init instance is reachable but not proxying | Provisioning failed partway | Check `/var/log/cloud-init-output.log` for the failing step |

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - verify management access.
- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - roll out client routing safely.
