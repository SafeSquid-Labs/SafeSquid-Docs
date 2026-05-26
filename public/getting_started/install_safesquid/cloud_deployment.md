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

Cloud deployment places SafeSquid close to cloud workloads, remote users, or hybrid egress paths. The main risks are exposed proxy ports, undersized instances, weak storage planning, and missing high availability. Treat cloud deployment as a network security change, not just an instance launch.

## Use this method when

- Users or workloads egress through a cloud network.
- A cloud-hosted proxy reduces routing complexity.
- Cloud security groups, routing, and storage are centrally managed.
- High availability can be designed before broad rollout.

For new VM builds where ISO boot is supported, [SafeSquid Appliance Builder](/getting_started/install_safesquid/safesquid_appliance_builder) remains the standard appliance path.

## Validate prerequisites

Before deployment, confirm:

- Instance sizing follows [Deployment Planning](/getting_started/deployment_planning).
- Security groups restrict proxy access to approved client or VPN ranges.
- Management access is limited to administrator networks.
- Storage is sized for logs and evidence retention.
- Outbound access exists for licensing, updates, and subscribed intelligence services.
- A rollback path exists for routes, security groups, and client proxy settings.

## Choose a deployment pattern

| Pattern | Use when | Production note |
|---|---|---|
| Cloud image | A supported image exists for the target cloud | Validate image provenance and storage layout |
| Cloud-init | The organization standardizes bootstrap scripts | Store scripts in change-controlled repositories |
| SAB ISO on cloud VM | The cloud supports ISO boot or image import | Use the appliance validation path after install |
| Existing Linux VM | A managed Linux host must be reused | You own OS hardening and service dependencies |

## Secure cloud networking

Minimum controls:

- Do not allow `0.0.0.0/0` to `8080/tcp`.
- Allow proxy ingress only from approved client, VPN, or ZTNA networks.
- Restrict management access to administrator networks.
- Route outbound web traffic intentionally through SafeSquid.
- Use cloud firewall logs or flow logs to verify expected paths.

## Verify deployment

On the SafeSquid instance:

```bash
systemctl status safesquid --no-pager
ss -lntp | grep ':8080'
tail -50 /var/log/safesquid/safesquid.log
```

From a pilot client inside the approved source range:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

Then check the access log:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

## Plan availability

Before production rollout, define:

- Whether one node is acceptable for the pilot only.
- Load balancer or failover design for production.
- Configuration sync ownership.
- Health checks for service and proxy listener.
- Log forwarding to Reporting Service or SIEM.
- Disaster recovery region or restore path.

## Troubleshoot cloud issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Client cannot reach proxy | Security group, route table, or VPN path blocks traffic | Test from source range and update cloud network policy |
| Proxy exposed publicly | Overbroad security group | Restrict `8080/tcp` immediately and review logs |
| Service starts but logs are missing | Storage path or permissions issue | Verify `/var/log/safesquid/` and disk mounts |
| Activation fails | Outbound licensing path blocked | Verify DNS and outbound HTTPS reachability |
| Failover sends users direct | Load balancer or route design bypasses SafeSquid | Correct routing and retest access-log evidence |

## Capture deployment evidence

- Instance type, disk layout, and region.
- Security group or firewall rules.
- Service status and listener check.
- Pilot access-log entry.
- Health check and failover design.
- Rollback plan for routes, security groups, and client proxy settings.

## Next steps

- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - route pilot traffic through the cloud proxy.
- [Proxy Clustering](/admin_guide/scaling_and_high_availability/proxy_clustering) - design high availability for production.

