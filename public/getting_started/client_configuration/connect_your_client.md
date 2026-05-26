---
title: Connect Your Client
description: Choose the right client routing method and prove that pilot traffic reaches SafeSquid before production rollout.
keywords:
  - SafeSquid client configuration
  - proxy client routing
  - SafeSquid proxy setup
  - managed proxy rollout
---

# Prove Client Traffic Reaches SafeSquid

SafeSquid cannot enforce policy on traffic that bypasses the proxy. Client onboarding must prove that web requests traverse SafeSquid, appear in logs, and can later be tied to user identity. Start with a pilot client, then move to managed rollout.

## Validate prerequisites

Before configuring clients, confirm:

- SafeSquid is installed, running, and listening on the approved proxy port.
- Client networks can reach the SafeSquid listener.
- Activation is complete or scheduled before production policy rollout.
- Root CA deployment is planned before HTTPS inspection testing.
- Direct internet egress is controlled where mandatory proxy use is required.
- Rollback steps exist for the selected client configuration method.

## Choose the routing method

| Method | Best fit | Production note |
|---|---|---|
| [Explicit Proxy](/getting_started/client_configuration/explicit_proxy) | One pilot browser or workstation | Use only for validation or troubleshooting |
| [PAC File](/getting_started/client_configuration/pac_file) | Managed browsers with routing exceptions | Host and protect the PAC file through change control |
| [System-Wide Proxy](/getting_started/client_configuration/system_wide_proxy) | One host where OS-aware apps should use SafeSquid | Some tools still need app-specific settings |
| [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) | Fleet rollout through GPO, MDM, Jamf, Intune, Ansible, or Puppet | Stage rollout and validate rollback before expansion |
| [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) | Tools that ignore OS or browser proxy settings | Treat as an exception with its own evidence record |

## Start with a pilot

1. Select one managed test client.
2. Configure explicit proxy or PAC routing for that client.
3. Browse an HTTP test site.
4. Confirm the request appears in `/var/log/safesquid/access/extended.log`.
5. Record the client setting and rollback path.
6. Expand only after routing, logging, and support ownership are clear.

## Verify traffic evidence

From a pilot client:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected evidence includes source address, destination, timestamp, and action. After authentication is enabled, repeat the test and confirm user attribution.

For HTTPS, first deploy the SafeSquid Root CA through the approved trust path. A valid HTTPS test must show a trusted browser connection without certificate warnings.

## Prevent bypass

For production enforcement, client configuration is not enough by itself. Confirm that network controls prevent clients from reaching the internet directly when policy requires SafeSquid inspection. Exceptions must have a business owner, a reason, and an expiry or review date.

## Troubleshoot client routing

| Symptom | Likely cause | Fix |
|---|---|---|
| No access-log entry | Client is not using SafeSquid | Recheck proxy settings, PAC URL, and direct egress path |
| Some apps bypass SafeSquid | App ignores OS or browser proxy | Use application-specific configuration or restrict direct egress |
| HTTPS warning appears | Root CA trust is missing | Deploy Root CA and retest without bypassing warnings |
| Internal apps fail | Missing bypass or routing exception | Add an approved PAC or OS bypass rule |
| User identity is missing | Authentication is not configured | Configure authentication and repeat the test |

## Capture onboarding evidence

- Client method selected and reason.
- Proxy or PAC setting used by the pilot client.
- First access-log entry.
- Authentication evidence when enabled.
- Root CA trust result before HTTPS inspection.
- Rollback path for the client setting.

## Next steps

- [Explicit Proxy](/getting_started/client_configuration/explicit_proxy) - validate one pilot browser quickly.
- [PAC File](/getting_started/client_configuration/pac_file) - move to managed browser routing.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - scale endpoint rollout safely.
