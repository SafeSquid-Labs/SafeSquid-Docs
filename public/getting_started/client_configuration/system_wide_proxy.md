---
title: "System-Wide Proxy Settings"
description: Configure one managed operating system to send browser and supported application traffic through SafeSquid.
keywords:
  - SafeSquid system proxy
  - operating system proxy
  - Windows proxy settings
  - Linux proxy settings
  - macOS proxy settings
---

# Route One Host Through SafeSquid

System-wide proxy settings help validate how a workstation behaves when OS-aware applications use SafeSquid. This method is useful for controlled workstations, developer endpoints, and pilot hosts. It is not a substitute for enterprise policy enforcement unless settings are managed and protected.

## Use this method when

Use system-wide proxy when:

- You need more coverage than one browser setting.
- The host is managed by the organization.
- Applications honor operating system proxy settings.
- You can roll back quickly if business apps fail.

Do not assume all applications will use these settings. Some tools need application-specific proxy configuration.

## Validate prerequisites

Confirm:

- Explicit proxy pilot passed.
- Proxy IP, port, and bypass entries are approved.
- User or device is in a pilot group.
- Root CA rollout is ready before HTTPS inspection tests.
- Rollback commands are documented.
- WPAD auto-detection is disabled on the host, so discovery cannot override the manual setting.

## Configure by operating system

<Tabs>
  <Tab title="Windows">

Use approved endpoint management where possible. For a controlled pilot, set WinHTTP proxy from an elevated shell:

```powershell
netsh winhttp set proxy SAFESQUID-IP:8080 "localhost;*.internal.example.com"
```

Verify:

```powershell
netsh winhttp show proxy
```

Expected result: the proxy and bypass list match the approved pilot values.

  </Tab>
  <Tab title="Linux">

Set proxy variables for a pilot shell:

```bash
export http_proxy=http://SAFESQUID-IP:8080
export https_proxy=http://SAFESQUID-IP:8080
export no_proxy=localhost,127.0.0.1,.internal.example.com
```

Persist settings only through the organization's approved profile, package-manager, or configuration-management process.

Verify:

```bash
curl -I http://example.com
```

Expected result: the request succeeds and appears in SafeSquid access logs.

  </Tab>
  <Tab title="macOS">

Use MDM for managed rollout. For a pilot, configure the active network service:

```bash
networksetup -setwebproxy "Wi-Fi" SAFESQUID-IP 8080
networksetup -setsecurewebproxy "Wi-Fi" SAFESQUID-IP 8080
```

Verify:

```bash
networksetup -getwebproxy "Wi-Fi"
```

Expected result: proxy settings match the approved SafeSquid listener.

  </Tab>
</Tabs>

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/03-System_Wide_Proxy.md §Windows */}

<Warning>
  **Windows keeps two separate proxy stores.** The `netsh winhttp` command above configures **WinHTTP**, used by services and by some background components. Browsers and most desktop applications read **WinINET**, configured through the Settings app, Internet Options, or the `HKCU` registry values below.

  Setting one does not set the other. A host configured only through `netsh winhttp` will show a correct proxy in `netsh winhttp show proxy` while Chrome and Edge continue to browse direct. For host-wide coverage, set both.
</Warning>

<Accordion title="Windows: configure the WinINET store">

**Settings app — Windows 10 and 11**

1. **Settings → Network & Internet → Proxy**.
2. Turn **Automatically detect settings** off, which disables WPAD.
3. Turn **Use a proxy server** on.
4. Enter the SafeSquid address and port `8080`, or the approved listener port.
5. Under **Edit**, add the approved bypass entries, separated with semicolons (`;`).
6. Select **Save**.

Confirm it applied by opening `edge://net-internals/#proxy` in Edge.

**Internet Options — all supported Windows versions**

Use this path when the Settings app is restricted by policy, or when per-protocol values are needed.

1. **Control Panel → Internet Options → Connections → LAN Settings**.
2. Clear **Automatically detect settings**.
3. Select **Use a proxy server for your LAN** and enter the address and port.
4. Select **Advanced** for separate HTTP, HTTPS (Secure), and FTP entries. Leave SOCKS blank unless it is specifically required.
5. Add the bypass list, semicolon-separated, then confirm each dialog.

**Registry values**

These are the underlying WinINET values, useful for automation or for confirming what a host actually has set. Under `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings`:

| Value | Type | Data |
|---|---|---|
| `ProxyEnable` | `REG_DWORD` | `1` |
| `ProxyServer` | `REG_SZ` | `SAFESQUID-IP:8080` |
| `ProxyOverride` | `REG_SZ` | `*.local;*.internal.example.com;localhost;127.0.0.1` |

Deploy these through Group Policy preferences rather than by hand where more than one machine is involved — see [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment).

</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/03-System_Wide_Proxy.md §Linux */}

<Accordion title="Persist proxy settings on Linux">

Shell exports last only for the current session. Use one of these files when the pilot must survive a reboot, and record which one you changed so it can be reverted.

**All users on the host** — edit `/etc/environment`:

```
http_proxy="http://SAFESQUID-IP:8080"
https_proxy="http://SAFESQUID-IP:8080"
ftp_proxy="http://SAFESQUID-IP:8080"
no_proxy="localhost,127.0.0.1,.internal.example.com"
```

**One user only** — append the same `export` lines to `~/.profile` or `~/.bashrc`, then `source` the file.

Package managers do not read these variables. Configure them separately or updates fail while browsing works.

**APT (Debian, Ubuntu)** — create `/etc/apt/apt.conf.d/95proxies`:

```
Acquire::http::Proxy "http://SAFESQUID-IP:8080";
Acquire::https::Proxy "http://SAFESQUID-IP:8080";
```

**YUM or DNF (RHEL, CentOS, Fedora)** — add to `/etc/yum.conf`:

```ini
proxy=http://SAFESQUID-IP:8080
```

Verify after any change:

```bash
env | grep -i proxy
sudo apt update
```

Expected result: the variables show the approved proxy, and the package index refreshes through SafeSquid with matching access-log entries.

For applications that ignore both the environment and the package-manager configuration, see [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration).

</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/03-System_Wide_Proxy.md §Linux (GUI Method) and §macOS */}

<Accordion title="Desktop proxy settings by GUI path">

Use these paths when walking a pilot user through the change, or when confirming what an endpoint is actually set to.

**GNOME (Ubuntu and derivatives)**

1. Open **Settings** and select **Network**.
2. Open **Network Proxy** and select **Manual**.
3. Set **HTTP Proxy**, **HTTPS Proxy**, and **FTP Proxy** to the SafeSquid address and port `8080`.
4. Set **Ignore Hosts** to `localhost,127.0.0.1,*.local,*.internal.example.com`.
5. Select **Apply system-wide**, then sign out and back in.

**macOS**

1. Open **System Settings** and select **Network**.
2. Select the active service, Wi-Fi or Ethernet, then **Details**.
3. Open **Proxies** and clear **Auto Proxy Discovery** to disable WPAD.
4. Enable **Web Proxy (HTTP)** and **Secure Web Proxy (HTTPS)**, and set both to the SafeSquid address and port `8080`.
5. Set **Bypass proxy settings for these Hosts & Domains** to a comma-separated list such as `*.local, localhost, 127.0.0.1, *.internal.example.com`.
6. Enable **Exclude simple hostnames**, then select **OK** and **Apply**.

<Tip>
On macOS, create separate network locations for office and remote use under **System Settings → Network → Location**. A user can then switch proxy settings without editing fields, which reduces mistyped exceptions during a pilot.
</Tip>

These paths configure the graphical session only. Terminal applications still need the environment variables above.

</Accordion>

<Accordion title="Advanced Windows registry method">

Use registry-based proxy settings only through approved endpoint management or an administrator-controlled pilot. Manual registry edits are hard to audit and easy to leave behind.

```powershell
reg query "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyServer
```

Expected result: the registry value matches the approved proxy or PAC deployment. Prefer GPO or MDM for production enforcement.

</Accordion>

## Verify host coverage

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: OS-aware applications from the pilot host generate log entries.

Also test one internal destination that should bypass SafeSquid.

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/03-System_Wide_Proxy.md §Test Your Configuration and §Still not working? */}

Confirm the host is applying the setting, per platform:

```powershell
# Windows: WinHTTP store, then the store browsers read
netsh winhttp show proxy
[System.Net.WebRequest]::DefaultWebProxy
```

```bash
# macOS
scutil --proxy
```

```bash
# Linux
env | grep -i proxy
```

Expected result: the reported values match the approved SafeSquid listener and bypass list.

<Accordion title="When settings look right but traffic still bypasses">

Something else on the host is usually overriding the proxy. Check, in order:

- **Browser extensions** — proxy switchers and privacy extensions override browser-level settings without changing anything visible in the OS.
- **VPN clients** — split-tunnel and full-tunnel configurations reroute traffic before it reaches the proxy setting.
- **Security software** — endpoint agents that inspect traffic locally can intercept connections ahead of the configured proxy.
- **WPAD** — if auto-detection is still enabled, a discovered PAC file takes precedence over the manual entry.

Test the proxy path directly to separate a client problem from a proxy problem:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

Expected result: the request succeeds. If it does, the proxy is healthy and the fault is in the client configuration.

</Accordion>

## Capture deployment evidence

Store:

- Hostname and operating system.
- Proxy settings and bypass list.
- Management tool or manual pilot method.
- Access-log sample.
- Internal bypass test result.
- Rollback command.

## Troubleshoot host routing

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser works but CLI bypasses proxy | Tool ignores OS proxy or environment is missing | Configure application-specific proxy settings |
| Internal sites break | Missing bypass entry | Add approved internal suffixes |
| Settings disappear | User or policy overwrote manual settings | Move rollout to GPO, MDM, or configuration management |
| HTTPS warning appears | Root CA is missing | Install Root CA through approved trust path |
| Settings are lost after a reboot | Applied as a session export rather than persisted | Use `/etc/environment` on Linux, or the Settings app and registry on Windows, rather than shell exports |
| Proxy setting is silently replaced | WPAD auto-detection is still enabled and a discovered PAC file takes precedence | Disable **Automatically detect settings** on Windows, or **Auto Proxy Discovery** on macOS |
| Browsers use the proxy but Windows services do not, or the reverse | Only one of the WinHTTP and WinINET stores was configured | Set both; see the Windows accordion above |

## Next steps

- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - move from host pilot to managed rollout.
- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - configure tools that bypass OS settings.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - apply controls after routing is proven.
