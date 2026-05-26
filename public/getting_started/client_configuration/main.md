---
title: Client Configuration
description: Client onboarding path for routing pilot, managed, and application traffic through SafeSquid SWG.
keywords:
  - client configuration
  - SafeSquid documentation
  - explicit proxy
  - PAC file
  - enterprise proxy deployment
---

# Route Clients Without Losing Control

SafeSquid enforces policy only for traffic that traverses the proxy. Client onboarding must prove traffic flow, preserve user attribution, and avoid bypass paths before production users depend on the gateway.

## Choose the routing method

| Method | Use when | Avoid when |
|---|---|---|
| [Explicit Proxy](/getting_started/client_configuration/explicit_proxy) | You need a fast pilot on one browser or test workstation | You need repeatable enterprise rollout or bypass control |
| [PAC File](/getting_started/client_configuration/pac_file) | You need flexible routing rules across managed browsers | You cannot host and protect the PAC file reliably |
| [System-Wide Proxy](/getting_started/client_configuration/system_wide_proxy) | One managed host must route most applications through SafeSquid | Applications ignore OS proxy settings or require separate trust stores |
| [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) | You manage fleets through GPO, MDM, Jamf, Intune, Ansible, or Puppet | You have not completed pilot validation and rollback planning |
| [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) | A specific tool ignores system settings | You can solve the problem with PAC, GPO, MDM, or OS proxy settings |

## Rollout sequence

1. Start with [Connect Your Client](/getting_started/client_configuration/connect_your_client) to select the method and verify the first proxied request.
2. Use [Explicit Proxy](/getting_started/client_configuration/explicit_proxy) only for lab or pilot validation.
3. Move managed users to [PAC File](/getting_started/client_configuration/pac_file) or [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment).
4. Use [System-Wide Proxy](/getting_started/client_configuration/system_wide_proxy) for controlled single-host coverage.
5. Apply [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) only where tools bypass system or browser settings.

## Evidence to capture

- Browser or OS proxy setting that points to the SafeSquid address and port.
- A test request recorded in `/var/log/safesquid/access/extended.log`.
- Matched user identity after authentication is enabled.
- Root CA deployment evidence before HTTPS inspection is enforced.
- Rollback procedure for the selected method.

## Next steps

- [Connect Your Client](/getting_started/client_configuration/connect_your_client) — choose and test the first client path.
- [PAC File](/getting_started/client_configuration/pac_file) — prepare flexible managed browser routing.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) — scale routing through central management.
