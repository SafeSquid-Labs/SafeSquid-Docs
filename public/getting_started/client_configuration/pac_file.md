---
title: "PAC File Configuration"
description: "Deploy a Proxy Auto-Configuration file so managed browsers route approved web traffic through SafeSquid with controlled exceptions."
keywords: ["SafeSquid PAC file", "proxy auto configuration", "managed browser proxy", "SafeSquid client rollout"]
---

# Route Browsers With PAC

A Proxy Auto-Configuration (PAC) file gives managed browsers a repeatable routing decision. Use it when explicit proxy testing has passed and you need controlled exceptions for internal sites, cloud services, or pilot groups.

## Use this method when

Use PAC when:

- Browser routing needs centralized logic.
- Internal destinations must bypass SafeSquid.
- Different networks need different proxy decisions.
- Rollout will later be managed through GPO, MDM, or browser policy.

Do not use complex PAC logic without change control. A small syntax error can send users direct to the internet or break business apps.

## Validate prerequisites

Confirm:

- Explicit proxy pilot passed.
- PAC hosting location is approved and highly available.
- Browsers can retrieve the PAC URL.
- Internal bypass list is reviewed.
- Rollback method is documented.

## Create a controlled PAC file

Use exact internal bypasses and a default SafeSquid proxy route:

```javascript
function FindProxyForURL(url, host) {
  if (isPlainHostName(host)) {
    return "DIRECT";
  }

  if (dnsDomainIs(host, ".internal.example.com")) {
    return "DIRECT";
  }

  return "PROXY SAFESQUID-IP:8080";
}
```

Replace `SAFESQUID-IP` and `.internal.example.com` with approved values. Avoid wildcarding public domains unless the exception has a business owner.

## Host the PAC file

Host the PAC file on an approved web location. Choose a method that operations can monitor and roll back.

<Tabs>
  <Tab title="Internal Web Server">
    Host `proxy.pac` on a highly available internal HTTP or HTTPS service. Use this when all managed endpoints can reach the internal network before browsing.
  </Tab>
  <Tab title="Cloud Storage or CDN">
    Host the PAC file on approved object storage or CDN when remote users need access before VPN or office connectivity.
  </Tab>
  <Tab title="Endpoint Management">
    Deliver the PAC URL through GPO, MDM, or browser policy. Keep the URL stable and version the file body.
  </Tab>
</Tabs>

Confirm clients can retrieve it:

```bash
curl -I http://proxy-config.example.com/proxy.pac
```

Expected result: the server returns a successful response and the PAC file content is current.

## Deploy to pilot clients

1. Configure one pilot browser with the PAC URL.
2. Browse to an internet site that should route through SafeSquid.
3. Browse to an internal site that should bypass SafeSquid.
4. Inspect SafeSquid logs for the internet request.
5. Confirm the internal request does not create unwanted proxy traffic.

<Accordion title="Common PAC functions">
  Use simple PAC functions first. Keep logic short enough for operations to review during incidents.

  ```javascript
  isPlainHostName(host)
  dnsDomainIs(host, ".internal.example.com")
  shExpMatch(host, "*.trusted.example.com")
  isInNet(host, "10.0.0.0", "255.0.0.0")
  ```

  Avoid broad `DIRECT` matches for public domains unless the exception has a business owner and review date.
</Accordion>

<Accordion title="Debug PAC behavior">
  Test PAC retrieval and browser behavior before assigning the file broadly.

  ```bash
  curl -I http://proxy-config.example.com/proxy.pac
  curl http://proxy-config.example.com/proxy.pac
  ```

  Use browser proxy diagnostics such as `chrome://net-export` or Firefox `about:networking` only on approved pilot endpoints. Store the export with the change record if it proves a routing defect.
</Accordion>

<Accordion title="Plan WPAD carefully">
  Web Proxy Auto-Discovery (WPAD) can reduce manual configuration, but it expands the trust boundary to DNS and DHCP discovery. Use WPAD only when DNS, DHCP, and endpoint teams approve ownership, spoofing controls, and rollback.

  Required evidence includes the WPAD DNS or DHCP record, PAC file checksum, pilot endpoint result, and rollback record.
</Accordion>

## Verify routing decisions

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: proxied internet requests appear; intended internal bypasses do not.

## Capture rollout evidence

Store:

- PAC file URL.
- PAC file version or checksum.
- Approved bypass entries.
- Pilot browser and user.
- Positive proxy log sample.
- Internal bypass test result.
- Rollback method.

## Troubleshoot PAC rollout

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Browser ignores PAC | PAC URL is wrong or blocked | Confirm URL retrieval from the client network |
| All traffic goes direct | PAC logic returns `DIRECT` too broadly | Narrow bypass rules and retest |
| Internal sites route to SafeSquid | Missing internal bypass rule | Add exact internal suffixes and avoid broad public-domain bypasses |
| Changes do not apply | Browser cached the PAC file | Clear browser cache or change PAC version path according to endpoint policy |
| Remote users cannot retrieve PAC | Hosting path is internal-only | Use approved public hosting or VPN-reachable hosting for remote cohorts |

## Next steps

- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - deploy PAC through endpoint management.
- [System-Wide Proxy Settings](/getting_started/client_configuration/system_wide_proxy) - test host-level routing.
- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - handle tools that ignore browser PAC.