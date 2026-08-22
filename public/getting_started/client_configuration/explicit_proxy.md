---
title: "Explicit Proxy Configuration"
description: Use explicit proxy settings to validate SafeSquid traffic flow on one pilot browser or workstation before managed rollout.
keywords:
  - SafeSquid explicit proxy
  - pilot proxy configuration
  - browser proxy setup
  - SafeSquid client routing
---

# Validate One Client First

Explicit proxy configuration is the fastest way to prove that a client can reach SafeSquid, send HTTP and HTTPS traffic through the proxy listener, and generate access-log evidence. Use it for a pilot or troubleshooting session only. Do not rely on manual browser settings for production-wide enforcement.

## Use this method when

Use explicit proxy when:

- You need a fast pilot before GPO, MDM, or PAC rollout.
- You are testing one browser or workstation.
- You are isolating routing, DNS, certificate, or policy behavior.

Do not use manual explicit proxy as the final enterprise control. Users can remove it unless endpoint policy prevents changes.

## Validate prerequisites

Confirm:

- SafeSquid is installed and activated.
- Proxy listener IP and port are known.
- Pilot client can reach the proxy network.
- Access-log review is available.
- Root CA trust is planned before HTTPS inspection tests.

## Configure a pilot browser

<Tabs>
  <Tab title="Windows">
    Open **Settings** > **Network & Internet** > **Proxy**, enable manual proxy, set HTTP proxy to `SAFESQUID-IP`, and set the port to `8080` or the approved listener port. Add only approved internal bypass entries.
  </Tab>
  <Tab title="Linux">
    Use the desktop environment proxy settings for a browser pilot, or use a command-line test with `curl --proxy`. For production desktop rollout, prefer PAC, GPO-equivalent endpoint management, or configuration management instead of manual user settings.
  </Tab>
  <Tab title="macOS">
    Open **System Settings** > **Network** > selected interface > **Details** > **Proxies**, enable Web Proxy and Secure Web Proxy, then enter `SAFESQUID-IP` and the approved listener port.
  </Tab>
  <Tab title="Browser">
    Use browser proxy settings only for a controlled pilot or troubleshooting session. Apply the same proxy for HTTP and HTTPS traffic, save the settings, and browse to `http://example.com`.
  </Tab>
</Tabs>

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/01-Explicit_Proxy.md §Configuration Steps */}

<Accordion title="Firefox: configure separately from the OS">

Firefox maintains its own proxy settings and ignores the operating system configuration by default. A pilot that only sets the OS proxy will show Chrome and Edge routing through SafeSquid while Firefox goes direct — and the traffic that bypasses the proxy is the traffic you will not see in any log.

Configure it explicitly, on every platform:

1. Open the menu (☰) and select **Settings**.
2. Scroll to **Network Settings** and select **Settings**.
3. Choose **Manual proxy configuration**.
4. Set **HTTP Proxy** to `SAFESQUID-IP` and **Port** to `8080`, or the approved listener port.
5. Enable **Also use this proxy for HTTPS**.
6. Set **No Proxy for** to the approved internal bypass entries, comma-separated.
7. Select **OK**.

For managed fleets, deliver these through Firefox enterprise policy rather than by hand — see [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment).

</Accordion>

<Accordion title="Windows: legacy Internet Options path">

On older Windows builds, or where the Settings app is restricted by policy, the same WinINET configuration is reachable through Control Panel:

**Control Panel → Internet Options → Connections → LAN Settings**

Enter the proxy address and port there. The values apply to Chrome, Edge, and most Windows applications, because they read the same WinINET store.

</Accordion>

<Note>
  **Bypass list syntax differs by platform.** Windows separates entries with semicolons (`;`); macOS and Linux use commas (`,`). Using the wrong separator makes the whole list parse as a single entry, so every internal destination silently routes through the proxy instead of bypassing it.
</Note>

<Steps>
  <Step title="Set proxy host and port">
    Set HTTP proxy to `SAFESQUID-IP` and port `8080` or the approved listener port.

    Confirm the client setting uses the approved proxy IP and listener port.

    If the client cannot reach the proxy, confirm firewall policy, route, and listener state.
  </Step>
  <Step title="Apply HTTPS proxy settings">
    Apply the same proxy for HTTPS traffic before testing encrypted destinations.

    Confirm HTTPS destinations use SafeSquid rather than direct internet access.

    If HTTPS produces certificate warnings, deploy the SafeSquid Root CA before production testing.
  </Step>
  <Step title="Add reviewed bypasses">
    Add only approved internal bypass entries and record the owner for each exception.

    Confirm each bypass maps to an approved internal destination and owner.

    If internal sites fail, add exact reviewed bypasses instead of broad wildcard entries.
  </Step>
  <Step title="Save and test">
    Save the settings and browse to `http://example.com`.

    Confirm the request returns an HTTP response through SafeSquid and appears in the access log.

    If no log appears, retest with `curl --proxy http://SAFESQUID-IP:8080 http://example.com`.
  </Step>
</Steps>

For command-line validation, run:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

Expected result: the request returns an HTTP response through SafeSquid.

## Verify traffic evidence

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the access log shows the pilot client, destination, timestamp, and action.

For a negative check, remove or bypass the proxy setting only in the test window and confirm the request no longer appears in SafeSquid logs. Restore the proxy setting immediately after the test.

## Capture deployment evidence

Store:

- Pilot client hostname.
- Proxy IP and port.
- Browser or OS used.
- Internal bypass list.
- Access-log sample.
- Rollback steps.

## Troubleshoot pilot failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser cannot browse | Wrong proxy IP, port, or firewall rule | Confirm listener with `ss -lntp` and test reachability |
| Request does not appear in logs | Browser is not using the proxy | Reopen proxy settings and retest with `curl --proxy` |
| Internal site breaks | Missing bypass entry | Add exact internal host or suffix approved by the network owner |
| HTTPS warning appears | Root CA is not trusted | Deploy the SafeSquid Root CA before testing HTTPS inspection |
| Firefox ignores the proxy while other browsers use it | Firefox does not read the operating system proxy setting | Configure Firefox directly, or deliver the setting through Firefox enterprise policy |
| Sites load but noticeably slowly | Network latency to the proxy, or the proxy is loaded | Check round-trip time with `ping SAFESQUID-IP`, then check load on the SafeSquid host |
| Internal destinations still route through the proxy | Bypass-list separator is wrong for the platform | Use `;` on Windows and `,` on macOS and Linux |

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/01-Explicit_Proxy.md §Still not working? */}

Before assuming the proxy is at fault, confirm the client is actually applying the setting you think it is:

```powershell
# Windows
netsh winhttp show proxy
```

```bash
# macOS
scutil --proxy
```

```bash
# Linux
echo $http_proxy
```

Expected result: the reported proxy matches the approved SafeSquid listener. A setting that was entered but not applied looks identical to a proxy that is not answering.

## Next steps

- [PAC File Configuration](/getting_started/client_configuration/pac_file) - automate browser routing.
- [System-Wide Proxy Settings](/getting_started/client_configuration/system_wide_proxy) - test host-level settings.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - roll out through endpoint management.
