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
  </Tab>
  <Tab title="cloud-init build">
    Use cloud-init when automated instance build is required. Review user data before launch and avoid embedding activation keys, administrator passwords, or certificate private keys in cloud-init text.

    Keep cloud-init focused on baseline OS configuration, package source selection, network settings, log-forwarder bootstrap, and management hardening. Upload the `activation_key` through the approved SafeSquid activation workflow after the instance is reachable.
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

<Accordion title="Load balancing and auto-scaling guidance">
  Use load balancers only when the selected traffic model is compatible with proxy semantics, source attribution, health checks, and authentication. Record how clients reach the proxy, how failed nodes are removed, and how logs preserve user and source identity.

  Auto-scaling is suitable only when configuration, activation context, certificate trust, logging, and policy state can be synchronized before a node receives traffic. Do not scale out stateless instances that cannot enforce the same policy and logging behavior as the active node.
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

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - verify management access.
- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - roll out client routing safely.
