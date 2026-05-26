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

System-wide proxy settings help validate how a workstation behaves when most OS-aware applications use SafeSquid. This method is useful for controlled workstations, developer endpoints, and pilot hosts. It is not a substitute for enterprise policy enforcement unless settings are managed and protected.

## Use this method when

- One host must route browser and OS-aware application traffic through SafeSquid.
- You need to test impact before GPO, MDM, or PAC rollout.
- A developer or administrator workstation requires broader proxy coverage than one browser.

Some applications ignore OS proxy settings. Use [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) for those exceptions.

## Validate prerequisites

Before changing a host:

- Record the current proxy state for rollback.
- Confirm SafeSquid is reachable on `8080/tcp` or the configured listener port.
- Confirm the user or administrator can change OS network settings.
- Confirm internal bypass domains are approved.
- Confirm Root CA deployment is ready before HTTPS inspection testing.

## Configure Windows

1. Open **Settings -> Network & Internet -> Proxy**.
2. Enable **Use a proxy server**.
3. Set **Address** to **SAFESQUID-IP**.
4. Set **Port** to **8080**.
5. Add approved bypass entries such as `localhost`, `127.0.0.1`, and internal domains.
6. Click **Save**.

Verify the setting:

```powershell
netsh winhttp show proxy
```

If required for services that use WinHTTP, import the user proxy into WinHTTP after change approval:

```powershell
netsh winhttp import proxy source=ie
```

## Configure Linux

For a temporary shell test:

```bash
export http_proxy=http://SAFESQUID-IP:8080
export https_proxy=http://SAFESQUID-IP:8080
export no_proxy=localhost,127.0.0.1,.example.internal
curl -I http://example.com
```

For GNOME, use **Settings -> Network -> Network Proxy -> Manual** and set HTTP and HTTPS proxy to **SAFESQUID-IP** on port **8080**.

For package managers, configure only when package download traffic must traverse SafeSquid:

```bash
sudo tee /etc/apt/apt.conf.d/95safesquid-proxy >/dev/null <<'EOF'
Acquire::http::Proxy "http://SAFESQUID-IP:8080";
Acquire::https::Proxy "http://SAFESQUID-IP:8080";
EOF
```

## Configure macOS

1. Open **System Settings -> Network**.
2. Select the active network interface.
3. Open **Details -> Proxies**.
4. Enable **Web Proxy (HTTP)** and **Secure Web Proxy (HTTPS)**.
5. Set both to **SAFESQUID-IP** and port **8080**.
6. Add approved bypass domains.
7. Click **OK -> Apply**.

Verify the setting:

```bash
scutil --proxy
```

## Verify host coverage

From the configured host, test HTTP traffic:

```bash
curl -I http://example.com
```

Then check SafeSquid logs:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

For HTTPS, install the SafeSquid Root CA first. A valid HTTPS test must not require bypassing certificate warnings.

## Troubleshoot host routing

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser routes but CLI does not | CLI ignores OS proxy | Set application-specific proxy variables or config |
| CLI routes but browser does not | Browser has its own proxy mode | Configure the browser to use system settings |
| Package manager fails | Proxy or certificate trust missing for package tool | Configure tool-specific proxy and trust store |
| Internal sites break | Missing bypass entry | Add approved internal suffixes to bypass list |
| No SafeSquid log entry | Traffic bypasses proxy | Check direct egress, app-specific settings, and OS proxy state |

## Capture deployment evidence

- Original proxy state and rollback command.
- OS proxy setting after change.
- Access-log entry for an HTTP test request.
- HTTPS trust result after Root CA deployment.
- List of applications that still require app-specific configuration.

## Next steps

- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - handle tools that ignore OS proxy settings.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - scale protected proxy settings across managed endpoints.
- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - complete trusted HTTPS inspection.

