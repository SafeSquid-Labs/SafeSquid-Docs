---
title: "PAC File Configuration"
description: Deploy a Proxy Auto-Configuration file so managed browsers route approved web traffic through SafeSquid with controlled exceptions.
keywords:
  - SafeSquid PAC file
  - proxy auto configuration
  - managed browser proxy
  - SafeSquid client rollout
---

# Route Browsers With PAC

A Proxy Auto-Configuration (PAC) file gives managed browsers a repeatable routing decision. Use it when explicit proxy testing has passed and you need controlled exceptions for internal sites, cloud services, or pilot groups.

## Use this method when

- Browsers must use SafeSquid without per-browser manual settings.
- Internal domains must bypass the proxy.
- Different client networks need different SafeSquid nodes.
- Rollback must be as simple as removing or changing a PAC URL.

Do not use PAC as the only control if endpoints can ignore browser settings and reach the internet directly. Pair it with network egress controls for production enforcement.

## Validate prerequisites

Before publishing a PAC file, confirm:

- SafeSquid listener addresses are stable and documented.
- The PAC file will be hosted over a trusted internal web server.
- Change control owns who can edit the PAC file.
- Pilot clients can reach the PAC URL before browser startup.
- Bypass domains are approved by network and security owners.

## Create a controlled PAC file

Start with a small policy. Add complexity only after pilot validation.

```javascript
function FindProxyForURL(url, host) {
  if (isPlainHostName(host) || dnsDomainIs(host, ".example.internal")) {
    return "DIRECT";
  }

  if (shExpMatch(host, "localhost") || isInNet(host, "127.0.0.0", "255.0.0.0")) {
    return "DIRECT";
  }

  return "PROXY SAFESQUID-IP:8080";
}
```

For two SafeSquid nodes, use ordered failover:

```javascript
function FindProxyForURL(url, host) {
  if (isPlainHostName(host) || dnsDomainIs(host, ".example.internal")) {
    return "DIRECT";
  }

  return "PROXY SAFESQUID-A:8080; PROXY SAFESQUID-B:8080";
}
```

Avoid broad `DIRECT` rules for public SaaS unless the risk has been accepted. A direct bypass removes SafeSquid inspection, policy, and audit evidence for that traffic.

## Host the PAC file

1. Store the PAC file on an internal HTTPS web server.
2. Use a predictable URL such as `https://proxy.example.internal/proxy.pac`.
3. Restrict write access to the service owner.
4. Log PAC file changes through normal change control.
5. Test file retrieval from a pilot client.

```bash
curl -I https://proxy.example.internal/proxy.pac
```

The response should return `200 OK` and an appropriate JavaScript or PAC content type.

## Deploy to pilot clients

Configure the pilot browser or OS to use the PAC URL.

- Windows: **Settings -> Network & Internet -> Proxy -> Use setup script**.
- macOS: **System Settings -> Network -> Details -> Proxies -> Automatic Proxy Configuration**.
- Firefox: **Settings -> Network Settings -> Automatic proxy configuration URL**.
- Enterprise rollout: distribute the PAC URL through GPO, Intune, Jamf, or MDM.

Keep the pilot group small until logs show expected routing and bypass behavior.

## Verify routing decisions

Test three paths:

1. Public HTTP site routes through SafeSquid.
2. Public HTTPS site routes through SafeSquid after Root CA trust is deployed.
3. Approved internal domain uses `DIRECT` and does not appear as internet proxy traffic.

Check SafeSquid evidence:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

A successful public request shows client source, URL, action, and timestamp. After authentication is enabled, repeat the test and confirm user identity appears.

## Troubleshoot PAC rollout

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser does not fetch PAC | PAC URL unreachable or blocked | Test the URL from the client and fix DNS, TLS trust, or firewall rules |
| Public sites bypass SafeSquid | PAC rule returns `DIRECT` too broadly | Reduce bypass patterns and retest with a public test URL |
| Internal sites route to SafeSquid | Missing internal bypass rule | Add exact internal suffixes and avoid wildcarding public domains |
| Some browsers ignore PAC | Browser has manual proxy override | Remove manual proxy settings or enforce PAC through device management |
| Failover does not work | Secondary proxy unreachable or misordered | Test each SafeSquid node directly and update PAC order |

## Capture rollout evidence

Record:

- PAC file URL and checksum or change version.
- Approved bypass list and business owner.
- Pilot test results for proxied and direct destinations.
- Access-log entries for public traffic.
- Rollback plan that restores previous PAC URL or disables the setup script.

## Next steps

- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - distribute PAC settings through central management.
- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - inspect HTTPS after Root CA deployment.
- [Access Restriction](/use_cases/access_restriction/access_restriction) - enforce category and application rules once routing is stable.

