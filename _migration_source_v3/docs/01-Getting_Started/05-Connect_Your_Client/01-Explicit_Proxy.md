---
title: "Explicit Proxy Configuration"
description: Manual proxy configuration for SafeSquid SWG on Windows, Linux, and macOS browsers and systems.
keywords:
  - SafeSquid explicit proxy
  - manual proxy configuration
  - browser proxy setup
  - Windows proxy settings
  - Linux proxy configuration
  - macOS proxy settings
  - Chrome proxy setup
  - Firefox proxy configuration
---

# Explicit Proxy Configuration

**Explicit proxy** means manually entering the proxy IP and port in browser settings. Use this method for:
- Testing SafeSquid for the first time
- Single-user setups or controlled environments
- Quick validation without organization-wide rollout

**Time to configure:** ~2 minutes per browser

:::tip When to Use This Method

Use explicit proxy for initial testing. For production deployments, use [PAC File](/docs/Getting_Started/Connect_Your_Client/PAC_File/) or [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/) instead.

:::

## Prerequisites

:::info Before You Start

- SafeSquid IP address and port (default: 8080 for HTTP)
- SafeSquid must be running and accessible from the client network
- For system-wide Windows/macOS configuration: Administrator privileges
- For HTTPS sites: [SSL Inspection](/docs/SSL_Inspection/main/) configured (optional for initial testing)

:::

## Configuration Steps

### Windows

**For Chrome, Edge, and Internet Explorer** (uses system proxy):

1. Open **Settings** → **Network & Internet** → **Proxy**
2. Toggle **Use a proxy server** to **On**
3. Enter:
   - **Address:** SafeSquid IP (e.g., `192.168.1.100`)
   - **Port:** `8080`
4. *(Optional)* Add bypass list for internal sites:
   - Click **Edit** under "Use a proxy server"
   - Add: `*.local;*.company.com;localhost`
5. Click **Save**

**Alternative method (Windows 7-10):**
- Control Panel → Internet Options → Connections → LAN Settings
- Same settings as above

---

**For Firefox** (browser-specific settings):

1. Open Firefox → **Menu** (☰) → **Settings**
2. Scroll to **Network Settings** → **Settings**
3. Select **Manual proxy configuration**
4. Enter:
   - **HTTP Proxy:** SafeSquid IP
   - **Port:** `8080`
5. Check **Also use this proxy for HTTPS**
6. Add **No Proxy for:** `localhost, 127.0.0.1, *.local`
7. Click **OK**

### Linux

**GUI method (Ubuntu/GNOME):**

1. **Settings** → **Network** → **Network Proxy**
2. Select **Manual**
3. Enter:
   - **HTTP Proxy:** SafeSquid IP, Port 8080
   - **HTTPS Proxy:** SafeSquid IP, Port 8080
4. Add **Ignore Hosts:** `localhost, 127.0.0.1, *.local`
5. Click **Apply system-wide**
6. Restart browser

---

**Command-line method (works on all distros):**

```bash
# Set environment variables (temporary, current session only)
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8080
export no_proxy=localhost,127.0.0.1,*.local

# Launch browser with proxy
google-chrome &
# or
firefox &
```

**To make permanent** (add to `~/.bashrc` or `~/.profile`):
```bash
echo 'export http_proxy=http://192.168.1.100:8080' >> ~/.bashrc
echo 'export https_proxy=http://192.168.1.100:8080' >> ~/.bashrc
echo 'export no_proxy=localhost,127.0.0.1,*.local' >> ~/.bashrc
source ~/.bashrc
```

**Firefox on Linux:** Same as Windows Firefox steps above.

### macOS

**For Safari, Chrome, and system-wide proxy:**

1. **System Settings** → **Network**
2. Select your active connection (Wi-Fi or Ethernet)
3. Click **Details** → **Proxies**
4. Check **Web Proxy (HTTP)** and **Secure Web Proxy (HTTPS)**
5. Enter:
   - **Web Proxy Server:** SafeSquid IP:8080
   - **Secure Web Proxy Server:** SafeSquid IP:8080
6. Add **Bypass proxy settings for these Hosts & Domains:**
   - `*.local, localhost, 127.0.0.1`
7. Click **OK** → **Apply**
8. Restart browsers

---

**For Firefox** (browser-specific settings):

Same as Windows Firefox steps above.

## Test Your Configuration

**Immediate validation:**

1. Open the configured browser
2. Navigate to `http://example.com`
3. **If it loads:** Proxy is working ✅
4. **If it fails:** See [Troubleshooting](#troubleshooting) below

**Verify SafeSquid is receiving traffic:**

```bash
# On the SafeSquid server:
tail -f /var/log/safesquid/access/extended.log
```

You should see your request logged with client IP, URL, and timestamp.

**Access SafeSquid admin interface:**

- Via proxy: `http://safesquid.cfg/` (embedded Rest UI interface built into SafeSquid; accessible only when your client uses the proxy, but NOT resolved by SafeSquid's DNS resolver)
- Direct: `https://SAFESQUID-IP:8443/`

:::caution HTTPS Certificate Warnings

Until [SSL Inspection](/docs/SSL_Inspection/main/) is configured, HTTPS sites will show certificate warnings. This is expected—click through for now.

:::

## Troubleshooting

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|------------------|---------|
| "Proxy server refusing connections" | SafeSquid not running or firewall blocking | **On SafeSquid server:** `systemctl status safesquid` <br/> **Test connectivity:** `telnet SAFESQUID-IP 8080` |
| Site loads but very slow | Network latency or SafeSquid overloaded | Check ping time: `ping SAFESQUID-IP` <br/> Check SafeSquid load: `top` on server |
| Bypass list not working | Syntax error in bypass list | Windows: Use semicolons `;` <br/> macOS/Linux: Use commas `,` |
| Firefox ignores system proxy | Firefox uses own settings | Configure Firefox manually (see steps above) |
| "This site can't be reached" | Wrong IP or port | Verify SafeSquid IP and port 8080 in settings |
| HTTPS sites don't load at all | SSL inspection not configured | Either [configure SSL inspection](/docs/SSL_Inspection/main/) or disable HTTPS proxy temporarily |

**Still not working?**

1. **Verify proxy settings are actually applied:**
   - Windows: Open Edge, type `edge://net-internals/#proxy`
   - macOS: `scutil --proxy`
   - Linux: `echo $http_proxy`

2. **Check SafeSquid logs for errors:**
   ```bash
   tail -50 /var/log/safesquid/safesquid.log
   ```

3. **Test direct connectivity from command line:**
   ```bash
   # Test HTTP proxy
   curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
   
   # Test HTTPS proxy (expect certificate error if SSL inspection not configured)
   curl -I --proxy http://SAFESQUID-IP:8080 https://example.com
   ```

## Next Steps

1. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Run comprehensive tests to confirm proxy functionality
2. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Enable HTTPS decryption to inspect encrypted traffic
3. **Scale your deployment:**
   - **Small team (10-100 users):** [PAC File](/docs/Getting_Started/Connect_Your_Client/PAC_File/)
   - **Enterprise (100+ endpoints):** [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/)
