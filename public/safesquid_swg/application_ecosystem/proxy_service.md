---
title: "Proxy Service"
description: "SafeSquid proxy service role, startup dependency, policy enforcement path, and operational evidence for enterprise SWG deployments."
keywords: ["SafeSquid proxy service", "SafeSquid startup parameters", "Secure Web Gateway enforcement", "proxy evidence"]
---

# Proxy Service

The SafeSquid proxy service is the enforcement point for user web traffic. It receives client requests, evaluates policy, applies inspection controls, and generates evidence that administrators use for operations, audit, and incident response.

The Application Eco-system source calls out SafeSquid startup parameters as part of the operating model. Treat those parameters as production controls because incorrect service startup can change listening behavior, logging behavior, or enforcement availability.

## Risks the service controls

- Uncontrolled web access to phishing, malware, remote-access, and data-exfiltration destinations
- Policy drift when proxy instances do not start with the intended runtime settings
- Evidence gaps when access, extended, native, or configuration logs are not generated or forwarded
- Availability loss when the proxy process is not monitored by supporting services

## Operational responsibilities

The proxy service depends on a clear operating boundary:

| Responsibility | Control value | Evidence to retain |
| --- | --- | --- |
| Start with approved parameters | Prevents accidental listener, cache, or log changes | Service unit, startup parameters, change ticket |
| Enforce Layer 7 policy | Blocks or allows HTTP and HTTPS traffic by rule | `extended.log`, policy reports, SIEM events |
| Preserve configuration history | Supports audit and rollback | `config.log`, backup record |
| Stay supervised | Reduces downtime after process failure | Monit status, service restart events |

## Production checks

Verify the proxy service after installation, upgrade, and major policy changes:

1. Confirm the SafeSquid service is running under the expected service manager.
2. Confirm the client traffic path uses the intended proxy listener.
3. Trigger a known allowed and known blocked request.
4. Confirm the event appears in local logs or the Reporting Service.
5. Confirm Monit or the approved service supervisor reports healthy status.

## Related controls

- [SafeSquid Proxy Cluster](/safesquid_swg/architecture/safesquid_proxy_cluster) for scale-out and failover design.
- [Monit Service Governance](/safesquid_swg/interface/supporting_services_monit) for process supervision.
- [Reporting Service](/safesquid_swg/interface/reporting_service) for audit and forensic evidence.

## Next steps

- Use [Integrated DNS Security](/safesquid_swg/architecture/integrated_dns_security) to add DNS-layer protection.
- Use [Configure](/safesquid_swg/policy_management_console/configure) to manage policy through the console.