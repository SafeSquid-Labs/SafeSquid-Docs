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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md §Create Your PAC File */}

<Accordion title="Add proxy failover">

A single `PROXY` return means every browser loses web access when that node is unavailable. The return value accepts an ordered, semicolon-separated list; the browser tries each in turn and moves on when one does not answer.

```javascript
return "PROXY SAFESQUID-A:8080; PROXY SAFESQUID-B:8080";
```

Order the list deliberately — it is the failover order, not a load-balancing hint.

Appending `DIRECT` as a final element makes browsers bypass the proxy entirely when no node answers:

```javascript
return "PROXY SAFESQUID-A:8080; PROXY SAFESQUID-B:8080; DIRECT";
```

<Warning>
  **A trailing `DIRECT` fails open.** If every SafeSquid node is unreachable, clients browse the internet unfiltered and unlogged, and nothing in the browser tells the user or the operator that enforcement stopped. Use it only where an availability requirement has been weighed against losing the control, and where the decision has a named owner. Omitting `DIRECT` fails closed instead: users lose web access, which is visible and reported immediately.
</Warning>

</Accordion>

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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md §Deploy the PAC File, Step 1 */}

<Warning>
  **Serve the file with the correct MIME type.** Browsers expect `application/x-ns-proxy-autoconfig`. Served as `text/plain` or `text/html`, some browsers silently ignore the file and fall back to direct connections — the most common reason a correct PAC file appears to do nothing.

  ```apache
  # Apache
  AddType application/x-ns-proxy-autoconfig .pac
  ```

  ```nginx
  # Nginx
  types { application/x-ns-proxy-autoconfig pac; }
  ```

  Verify the header before rollout:

  ```bash
  curl -I http://proxy-config.example.com/proxy.pac
  ```

  Expected result: the response includes `Content-Type: application/x-ns-proxy-autoconfig`.
</Warning>

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md §Deploy the PAC File, Step 2 */}

<Accordion title="Point clients at the PAC URL">

Hosting the file does nothing until clients are told where it is. Disable auto-detection at the same time, or WPAD discovery may override the URL you set.

**Windows — Chrome, Edge, and most applications**

1. **Settings → Network & Internet → Proxy**.
2. Turn **Automatically detect settings** off.
3. Turn **Use setup script** on.
4. Enter the PAC URL and select **Save**.

**Firefox — all platforms**

1. Menu (☰) **→ Settings → Network Settings → Settings**.
2. Select **Automatic proxy configuration URL**.
3. Enter the PAC URL and select **OK**.

Firefox keeps its own settings and will not pick up the Windows or macOS configuration.

**macOS — Safari, Chrome, and most applications**

1. **System Settings → Network →** select the active service **→ Details → Proxies**.
2. Enable **Automatic Proxy Configuration**.
3. Enter the PAC URL, then select **OK** and **Apply**.

**Linux desktops**

```bash
# GNOME
gsettings set org.gnome.system.proxy mode 'auto'
gsettings set org.gnome.system.proxy autoconfig-url 'http://proxy-config.example.com/proxy.pac'
```

```bash
# KDE
kwriteconfig5 --file kioslaverc --group 'Proxy Settings' \
  --key 'Proxy Config Script' 'http://proxy-config.example.com/proxy.pac'
```

For anything beyond a pilot, deliver the URL through GPO, MDM, or browser policy instead of setting it per machine — see [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment).

</Accordion>

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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md §Common PAC Functions Reference */}

<Accordion title="PAC function reference">

Every function below is available inside `FindProxyForURL(url, host)`.

| Function | Purpose | Example |
|---|---|---|
| `isInNet(host, pattern, mask)` | Test whether the resolved IP falls in a subnet | `isInNet(host, "10.0.0.0", "255.0.0.0")` |
| `dnsDomainIs(host, domain)` | Test whether the host is in a domain | `dnsDomainIs(host, ".example.com")` |
| `shExpMatch(str, pattern)` | Shell-style wildcard match | `shExpMatch(url, "*.pdf")` |
| `localHostOrDomainIs(host, domain)` | Exact host match, or subdomain of it | `localHostOrDomainIs(host, "www.example.com")` |
| `isResolvable(host)` | Test whether the host resolves in DNS | `isResolvable(host)` |
| `isPlainHostName(host)` | True when the hostname contains no dots | `isPlainHostName(host)` |
| `dnsDomainLevels(host)` | Count the domain levels in a hostname | `dnsDomainLevels(host) > 0` |
| `weekdayRange(day1, day2)` | Match a day-of-week range | `weekdayRange("MON", "FRI")` |
| `timeRange(hour1, hour2)` | Match an hour-of-day range | `timeRange(9, 17)` |

`isInNet` and `isResolvable` force DNS lookups on every evaluation. Prefer `dnsDomainIs` and `shExpMatch` in hot paths, and keep DNS-dependent tests below the cheap string tests.

Time-based and day-based routing belongs in SafeSquid [Time Profiles](/use_cases/profiling_engine/time_profiles), not in the PAC file. A PAC rule is enforced by the client and can be bypassed; a SafeSquid profile cannot.

</Accordion>

<Accordion title="Debug PAC behavior">

Test PAC retrieval and browser behavior before assigning the file broadly.

```bash
curl -I http://proxy-config.example.com/proxy.pac
curl http://proxy-config.example.com/proxy.pac
```

Use browser proxy diagnostics such as `chrome://net-export` or Firefox `about:networking` only on approved pilot endpoints. Store the export with the change record if it proves a routing defect.

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md §Debug Your PAC File */}

Test routing decisions offline, before any endpoint receives the file. `pactester` evaluates `FindProxyForURL` without a browser:

```bash
sudo apt install pacparser
pactester -p proxy.pac -u http://example.com -h example.com
```

Expected result: the command prints the proxy string the client would use, such as `PROXY SAFESQUID-IP:8080` or `DIRECT`.

`pactester` ships in the `pacparser` package. On other distributions, search for `pacparser` or `pactester`.

Run one test per routing rule you added, including at least one destination that must go `DIRECT`. Save the output with the change record as proof the file was validated before rollout.

A PAC file is JavaScript, so a syntax error breaks proxy selection for every rule, not only the faulty one. The common causes are a missing semicolon, bracket, or quote; a misspelled function name; and a file served with the wrong MIME type or from an unreachable URL.

</Accordion>

<Accordion title="Plan WPAD carefully">

Web Proxy Auto-Discovery (WPAD) can reduce manual configuration, but it expands the trust boundary to DNS and DHCP discovery. Use WPAD only when DNS, DHCP, and endpoint teams approve ownership, spoofing controls, and rollback.

Required evidence includes the WPAD DNS or DHCP record, PAC file checksum, pilot endpoint result, and rollback record.

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/02-PAC_File.md §Advanced: WPAD (Auto-Discovery) */}

If WPAD is approved, three conditions must all hold or discovery silently fails:

1. A DNS A record for `wpad.<your-domain>` points at the host serving the file.

   ```
   wpad.example.com.  IN  A  PAC-SERVER-IP
   ```

2. The file is served as `wpad.dat`, not `proxy.pac`. Browsers request that exact name.

   ```
   http://wpad.example.com/wpad.dat
   ```

3. Clients are set to **Automatically detect settings**.

Verify retrieval before enabling it broadly:

```bash
curl -I http://wpad.example.com/wpad.dat
```

Expected result: the server returns a successful response for the `wpad.dat` path specifically.

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
|---|---|---|
| Browser ignores PAC | PAC URL is wrong or blocked | Confirm URL retrieval from the client network |
| All traffic goes direct | PAC logic returns `DIRECT` too broadly | Narrow bypass rules and retest |
| Internal sites route to SafeSquid | Missing internal bypass rule | Add exact internal suffixes and avoid broad public-domain bypasses |
| Changes do not apply | Browser cached the PAC file | Clear browser cache or change PAC version path according to endpoint policy |
| Remote users cannot retrieve PAC | Hosting path is internal-only | Use approved public hosting or VPN-reachable hosting for remote cohorts |
| Browser reports the PAC script failed | JavaScript syntax error in the file | Open the browser console and correct the reported error; validate offline with `pactester` before redeploying |
| Browser fetches the file but behaves as if there is none | Wrong MIME type on the response | Confirm `Content-Type: application/x-ns-proxy-autoconfig` with `curl -I` and fix the web server type mapping |
| Pages load slowly across the board | PAC logic performs DNS lookups on every evaluation | Move `isInNet` and `isResolvable` below the cheap string tests, or remove them |

## Next steps

- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - deploy PAC through endpoint management.
- [System-Wide Proxy Settings](/getting_started/client_configuration/system_wide_proxy) - test host-level routing.
- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - handle tools that ignore browser PAC.
