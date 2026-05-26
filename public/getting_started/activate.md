---
title: Activate Your License
description: Upload the SafeSquid activation key, verify licensed state, and capture evidence before configuring production policy.
keywords:
  - SafeSquid activation
  - activation key
  - SafeSquid license
  - license verification
  - deployment smoke test
---

# Activate Before Policy Rollout

SafeSquid must be activated before the deployment can be treated as ready for policy enforcement. Activation ties the instance to the Self-Service Portal, unlocks licensed capability, and gives operators a clear checkpoint before SSL inspection, authentication, and access controls are enabled.

## Validate prerequisites

Before activation, confirm:

- The activation key was downloaded from the [Self-Service Portal](https://key.safesquid.com).
- SafeSquid service is running.
- A pilot browser can reach `http://safesquid.cfg/` through the proxy path.
- The administrator is on an approved management network.
- Outbound access to licensing and update endpoints is available as required by the subscription.
- The change record includes rollback steps for client routing and firewall changes.

## Activate the instance

1. Configure the pilot browser to use SafeSquid as proxy.
2. Open `http://safesquid.cfg/` from the proxied browser.
3. Sign in with the approved administrator account.
4. Open the activation area in the Configuration Portal.
5. Upload or paste the activation key from the Self-Service Portal.
6. Save the change and wait for the portal to report an active license state.

Do not route production users until activation has been verified and logged.

## Verify activation evidence

Run these checks immediately after activation.

### Service is running

```bash
systemctl status safesquid --no-pager
```

Expected result: the service is active and no startup error appears in the recent log.

### Proxy listener is reachable

```bash
ss -lntp | grep ':8080'
```

Expected result: SafeSquid is listening on the approved proxy port.

### Interface loads through proxy

From the pilot browser, open:

```text
http://safesquid.cfg/
```

Expected result: the Configuration Portal loads through the SafeSquid proxy path. If it does not, verify the browser proxy setting before troubleshooting the service.

### HTTP traffic is logged

From a pilot client:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the access log records source, destination, timestamp, and action.

### HTTPS trust is ready

Do not bypass certificate warnings. Configure [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection), install the SafeSquid Root CA in the client trust store, then test HTTPS. A valid production-readiness test shows no browser certificate warning.

## Troubleshoot activation

| Symptom | Likely cause | Fix |
|---|---|---|
| `safesquid.cfg` does not load | Browser is not using SafeSquid as proxy | Recheck pilot proxy settings and access `http://safesquid.cfg/` again |
| Activation fails | Key, portal reachability, or subscription issue | Confirm key source, outbound reachability, and Self-Service Portal account state |
| Proxy listener missing | Service is stopped or misconfigured | Check `systemctl status safesquid` and service logs |
| HTTP request succeeds but no log appears | Client bypasses SafeSquid or wrong log path checked | Confirm proxy path and inspect `/var/log/safesquid/access/extended.log` |
| HTTPS warning appears | Root CA is not trusted or SSL inspection is incomplete | Deploy Root CA through approved trust path before retesting |

## Capture activation evidence

Store these artifacts with the deployment record:

- Activation key ownership record from the Self-Service Portal.
- Screenshot or export showing active license state.
- SafeSquid service status output.
- Listener check for `8080/tcp`.
- Access-log entry for a pilot HTTP request.
- Root CA rollout plan before HTTPS policy enforcement.

## Move toward production

After activation, configure controls in this order:

1. [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - inspect encrypted traffic only after Root CA trust is deployed.
2. [Authentication](/use_cases/authentication/authentication) - add user and group attribution.
3. [Integrated DNS Security](/use_cases/dns_security/dns_security) - protect name resolution where SafeSquid DNS controls are used.
4. [Access Restriction](/use_cases/access_restriction/access_restriction) - enforce URL category and application rules.
5. [Malware Scanners](/use_cases/malware_scanning/malware_scanners) - scan downloads and content streams.
6. [Data Leakage Prevention](/use_cases/data_leakage_prevention/data_leakage_prevention) - inspect uploads and outbound posts.
7. [Reporting Service](/safesquid_swg/interface/reporting_service) - preserve evidence for operations and audit.

## Next steps

- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - apply the baseline control sequence.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - expand from pilot routing to managed rollout.
- [Troubleshooting](/troubleshooting/troubleshooting) - diagnose activation, routing, certificate, and policy failures.

