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

- You need to validate a new SafeSquid deployment from one managed test client.
- You need to isolate client routing problems before PAC, GPO, MDM, or firewall changes.
- You need a low-blast-radius test before enabling SSL inspection or access policy.

Use [PAC File](/getting_started/client_configuration/pac_file) or [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) when the setting must survive user changes or reach many endpoints.

## Validate prerequisites

Before configuring the browser, confirm:

- SafeSquid is installed and listening on the proxy port, usually `8080/tcp`.
- The test client can reach the SafeSquid IP on that port.
- The browser proxy setting can be changed by the tester.
- A rollback note records the original browser or system proxy settings.
- HTTPS testing waits until [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) and Root CA trust are configured.

## Configure a pilot browser

Use placeholders in change records. Replace `SAFESQUID-IP` with the management-approved proxy address.

### Windows system proxy

1. Open **Settings -> Network & Internet -> Proxy**.
2. Enable **Use a proxy server**.
3. Set **Address** to **SAFESQUID-IP**.
4. Set **Port** to **8080** or the configured SafeSquid listener port.
5. Add internal bypasses such as `localhost`, `127.0.0.1`, and approved internal domains.
6. Click **Save**.

Chrome and Edge use the Windows system proxy. Firefox can use either system settings or its own manual proxy settings.

### Firefox manual proxy

1. Open **Menu -> Settings -> Network Settings -> Settings**.
2. Select **Manual proxy configuration**.
3. Set **HTTP Proxy** to **SAFESQUID-IP** and **Port** to **8080**.
4. Enable **Also use this proxy for HTTPS**.
5. Add `localhost`, `127.0.0.1`, and approved internal domains under **No Proxy for**.
6. Click **OK**.

### Linux environment test

Use environment variables only for a temporary shell test. Do not treat this as managed endpoint deployment.

```bash
export http_proxy=http://SAFESQUID-IP:8080
export https_proxy=http://SAFESQUID-IP:8080
export no_proxy=localhost,127.0.0.1,.example.internal
curl -I http://example.com
```

### macOS system proxy

1. Open **System Settings -> Network**.
2. Select the active interface.
3. Open **Details -> Proxies**.
4. Enable **Web Proxy (HTTP)** and **Secure Web Proxy (HTTPS)**.
5. Set both proxy servers to **SAFESQUID-IP** and port **8080**.
6. Add approved bypass domains.
7. Click **OK -> Apply**.

## Verify traffic evidence

Run one HTTP request from the configured client:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

On the SafeSquid server, inspect the access log:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

A valid pilot result shows the client source, destination URL, timestamp, and action. After authentication is enabled, repeat the test and confirm user attribution appears in the log or Reporting Service.

For HTTPS, do not bypass certificate warnings. Install the SafeSquid Root CA through an approved trust path, then test an HTTPS site and confirm the browser shows a trusted connection.

## Troubleshoot pilot failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser reports proxy refused | SafeSquid service is stopped or firewall blocks `8080/tcp` | Check `systemctl status safesquid` and test `SAFESQUID-IP:8080` from the client network |
| Direct internet works but proxied traffic fails | Wrong proxy IP, port, or routing path | Confirm the listener address and security policy before retesting |
| Firefox ignores Windows or macOS settings | Firefox uses manual proxy settings | Configure Firefox manually or set it to use system proxy settings |
| HTTPS shows certificate warnings | Root CA trust is missing or SSL inspection is incomplete | Install the SafeSquid Root CA and retest; never bypass browser warnings |
| No access-log entry appears | Client traffic bypasses SafeSquid | Recheck browser settings, PAC/WPAD settings, and direct internet routes |

## Capture deployment evidence

Record these artifacts before moving to managed rollout:

- Screenshot or change record of the pilot proxy setting.
- SafeSquid service status and listener check.
- Access-log entry for the pilot HTTP request.
- Root CA deployment result before HTTPS testing.
- Rollback steps that restore the original client proxy setting.

## Next steps

- [PAC File](/getting_started/client_configuration/pac_file) - move from manual testing to managed browser routing.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - roll proxy settings to managed endpoints.
- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - enable trusted HTTPS inspection after client routing works.

