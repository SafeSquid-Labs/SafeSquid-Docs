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

## Next steps

- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - move from host pilot to managed rollout.
- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - configure tools that bypass OS settings.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - apply controls after routing is proven.
