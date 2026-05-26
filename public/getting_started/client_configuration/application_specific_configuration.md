---
title: "Application-Specific Configuration"
description: Configure proxy exceptions for tools that do not inherit browser or operating system proxy settings.
keywords:
  - SafeSquid application proxy
  - Git proxy
  - Docker proxy
  - npm proxy
  - pip proxy
  - command-line proxy
---

# Handle Applications That Bypass OS Proxy

Some applications ignore browser or operating-system proxy settings. Developer tools, package managers, container runtimes, and email clients often need their own proxy configuration and trust store. Treat application-specific configuration as an exception path, not the default rollout model.

## Use this method when

- PAC, GPO, MDM, or system proxy settings do not affect the application.
- The application must reach the internet through SafeSquid for audit or policy reasons.
- The tool has a documented proxy setting and a safe rollback method.
- Credentials and certificates can be stored without exposing secrets.

Prefer [System-Wide Proxy](/getting_started/client_configuration/system_wide_proxy), [PAC File](/getting_started/client_configuration/pac_file), or [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) when those methods cover the application reliably.

## Validate prerequisites

Before configuring an application:

- Confirm the application really bypasses the managed proxy path.
- Confirm the required proxy syntax from the vendor documentation.
- Confirm where the application stores proxy settings and credentials.
- Install the SafeSquid Root CA in the application trust store if HTTPS inspection applies.
- Record rollback commands for every changed tool.

Do not place proxy passwords in command history, scripts, shared files, or examples. Use enterprise identity or the application's secure credential store where authentication is required.

## Configure common tools

Replace `SAFESQUID-IP` and `8080` with approved deployment values.

### Git

```bash
git config --global http.proxy http://SAFESQUID-IP:8080
git config --global https.proxy http://SAFESQUID-IP:8080
git config --global --get http.proxy
```

Rollback:

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### Docker daemon

Create or update the Docker service proxy override.

```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo tee /etc/systemd/system/docker.service.d/http-proxy.conf >/dev/null <<'EOF'
[Service]
Environment="HTTP_PROXY=http://SAFESQUID-IP:8080"
Environment="HTTPS_PROXY=http://SAFESQUID-IP:8080"
Environment="NO_PROXY=localhost,127.0.0.1,.example.internal"
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

Verify:

```bash
systemctl show --property=Environment docker
```

### npm

```bash
npm config set proxy http://SAFESQUID-IP:8080
npm config set https-proxy http://SAFESQUID-IP:8080
npm config get proxy
```

Rollback:

```bash
npm config delete proxy
npm config delete https-proxy
```

### Python pip

Use a per-user pip config when only one administrator or developer needs the setting.

```ini
[global]
proxy = http://SAFESQUID-IP:8080
```

Linux path: `~/.config/pip/pip.conf`.
Windows path: `%APPDATA%\pip\pip.ini`.

### APT

```bash
sudo tee /etc/apt/apt.conf.d/95safesquid-proxy >/dev/null <<'EOF'
Acquire::http::Proxy "http://SAFESQUID-IP:8080";
Acquire::https::Proxy "http://SAFESQUID-IP:8080";
EOF
sudo apt update
```

Rollback:

```bash
sudo rm /etc/apt/apt.conf.d/95safesquid-proxy
```

### YUM and DNF

Add the proxy setting to the approved package-manager configuration file:

```ini
proxy=http://SAFESQUID-IP:8080
```

Then test a metadata refresh from a controlled host.

### curl and wget

Use command options for one-time tests:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
wget --proxy=on --execute=http_proxy=http://SAFESQUID-IP:8080 http://example.com
```

Use environment variables or config files only when change control approves persistent behavior.

## Verify application evidence

For each application, prove:

- The application stores the expected proxy setting.
- A test request succeeds through SafeSquid.
- `/var/log/safesquid/access/extended.log` records the request.
- User identity appears after authentication is enabled.
- HTTPS works without certificate warnings after Root CA trust is configured.

## Troubleshoot application failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Application ignores proxy | Wrong config file, service not restarted, or unsupported proxy setting | Verify vendor syntax and restart the service or shell |
| TLS or certificate error | Application trust store lacks SafeSquid Root CA | Import the Root CA into the application or runtime trust store |
| Proxy authentication fails | Credentials are missing or stored unsafely | Use the approved credential method; do not embed passwords in URLs |
| Package downloads work for one user only | Setting is per-user, not system-wide | Move config to the approved system path or device-management policy |
| No SafeSquid log entry | Application still uses direct egress | Block direct egress or correct the application proxy setting |

## Capture exception evidence

For every application exception, record:

- Application name, owner, host group, and business reason.
- Exact proxy setting location.
- Trust-store change if HTTPS inspection applies.
- Access-log entry for the test request.
- Rollback command or config restore path.

## Next steps

- [System-Wide Proxy](/getting_started/client_configuration/system_wide_proxy) - cover OS-aware applications first.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - convert repeated exceptions into managed policy.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - validate policy results after traffic reaches SafeSquid.

