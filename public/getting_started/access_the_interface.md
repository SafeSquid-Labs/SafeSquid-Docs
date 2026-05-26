---
title: Access the Interface
description: Access the SafeSquid Configuration Portal from an approved management path during onboarding.
keywords:
  - SafeSquid interface
  - Configuration Portal
  - safesquid.cfg
  - SafeSquid management access
---

# Access the Management Interface Safely

Management access controls who can activate SafeSquid, change policy, and affect web access. Exposing the interface broadly or testing from an unmanaged client creates credential risk and weak audit evidence.

## Validate prerequisites

Confirm:

- SafeSquid service is running.
- The administrator is on an approved management or pilot client network.
- The browser proxy setting points to SafeSquid when using `http://safesquid.cfg/`.
- Direct management access, if used, is restricted by firewall policy.
- Administrator credentials are handled through approved procedures.

## Choose the access path

| Access path | Use when | Notes |
|---|---|---|
| `http://safesquid.cfg/` | Browser is configured to use SafeSquid as proxy | Validates the proxy path and embedded management name |
| `https://SAFESQUID-IP:8443/` | Direct admin network access is approved | Restrict to administrator networks only |

Do not open management ports to the public internet.

## Verify baseline state

On the SafeSquid host:

```bash
systemctl status safesquid --no-pager
ss -lntp | grep -E ':8080|:8443'
```

From the admin browser, open the chosen access URL and confirm the Configuration Portal loads.

## Capture access evidence

- Approved management source network.
- Interface URL used for onboarding.
- Service status output.
- Firewall rule or access policy for management traffic.
- Administrator role or account owner.

## Troubleshoot access failures

| Symptom | Likely cause | Fix |
|---|---|---|
| `safesquid.cfg` does not resolve | Browser is not using SafeSquid as proxy | Configure pilot proxy settings and retry |
| Direct URL fails | Management port blocked or service down | Verify firewall rules and service status |
| Portal loads from unapproved network | Firewall too broad | Restrict management access immediately |
| Login succeeds but changes are not allowed | Account role lacks permission | Use an approved administrator role |

## Next steps

- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - validate pilot traffic.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - apply baseline controls.

