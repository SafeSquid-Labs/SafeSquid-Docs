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

Before opening the Configuration Portal, confirm:

- SafeSquid is installed and running.
- A pilot browser is configured to use SafeSquid as proxy.
- The administrator is on an approved management network.
- DNS can resolve the special interface name through the proxy path.
- The change record identifies who is allowed to activate and configure the instance.

## Choose the access path

Use a proxied browser for first access:

1. Configure a pilot browser to use the SafeSquid proxy listener.
2. Open `http://safesquid.cfg/`.
3. Sign in with the approved administrator account.
4. Confirm the page is the SafeSquid Configuration Portal before entering credentials.

Avoid direct broad network exposure of the management interface. The first access path should prove the same proxy path that pilot clients will use.

## Verify baseline state

On the SafeSquid server, confirm the service is running:

```bash
systemctl status safesquid --no-pager
```

Expected result: service state is `active` or the platform-specific running state is clear from the output.

From the pilot browser, confirm:

- `http://safesquid.cfg/` loads.
- The Configuration Portal signs in successfully.
- The interface shows expected sections for activation, support, and configuration.
- No certificate warning is used as a workaround for HTTPS testing.

## Capture access evidence

Store:

- Administrator account or role used for first access.
- Pilot client hostname or asset identifier.
- Proxy listener used by the client.
- Screenshot or change record confirming portal access.
- Service status output.
- Any access restriction applied to management networks.

## Troubleshoot access failures

| Symptom | Likely cause | Fix |
|---|---|---|
| `safesquid.cfg` does not load | Browser is not using SafeSquid as proxy | Configure explicit proxy and retry from the same browser |
| Login page appears from the wrong network | Management path is too broad | Restrict access to approved admin networks before continuing |
| Service is not running | Installation or restart failed | Check `systemctl status safesquid --no-pager` and service logs |
| Interface loads but activation fails | Activation key or outbound subscription path is not ready | Continue with [Activate Your License](/getting_started/activate) troubleshooting |

## Next steps

- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - prove pilot traffic flow.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - configure controls after activation.
