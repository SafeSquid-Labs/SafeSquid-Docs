---
title: "System-Wide Proxy Settings"
description: "Operating system-level proxy configuration for SafeSquid SWG affecting all applications across Windows, Linux, and macOS environments"
keywords:
  - SafeSquid system proxy
  - OS-level proxy configuration
  - Windows proxy settings
  - Linux proxy environment
  - macOS proxy configuration
  - universal proxy settings
---

# System-Wide Proxy Settings

**System-wide proxy** configures the operating system to route all application traffic through SafeSquid—browsers, email clients, CLI tools, and background apps.

**Use this method for:**
- Complete traffic coverage on individual machines
- Developer workstations (CLI tools, package managers, Git)
- Endpoints where all apps must use the proxy
- When individual app configuration is impractical

**Time to configure:** ~5 minutes per OS

:::tip When to Use System-Wide Proxy

Use system-wide proxy for complete coverage on a single machine. For enterprise rollout (100+ endpoints), use [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/) to push settings via GPO/MDM.

:::

:::caution Not All Apps Respect System Proxy

Some applications (Docker, Git, npm, Python pip) ignore system proxy settings and require [application-specific configuration](/docs/Getting_Started/Connect_Your_Client/Application_Specific_Configuration/).

:::

## Prerequisites

:::info Before You Start

- SafeSquid IP address and port (default: 8080)
- Administrator/root privileges (for system-level changes)
- SafeSquid must be running and accessible
- Disable WPAD ("Automatically detect settings") to avoid conflicts

:::

## Configuration Steps

### Windows

**Method 1: Settings App (Windows 10/11)**

1. **Settings** → **Network & Internet** → **Proxy**
2. Turn **OFF**: "Automatically detect settings" (disables WPAD)
3. Turn **ON**: "Use a proxy server"
4. Enter:
   - **Address:** SafeSquid IP (e.g., `192.168.1.100`)
   - **Port:** `8080`
5. *(Optional)* Add bypass list:
   - Click **Edit** under "Use a proxy server"
   - Add: `*.local;*.company.com;localhost;127.0.0.1`
   - Use semicolons (`;`) to separate entries
6. Click **Save**

:::tip Verify Applied
Open Edge and type `edge://net-internals/#proxy` to confirm settings are active.
:::

---

**Method 2: Internet Options (Windows 7-11, legacy method)**

1. **Control Panel** → **Internet Options** → **Connections** tab
2. Click **LAN Settings**
3. Uncheck "Automatically detect settings" (disable WPAD)
4. Check "Use a proxy server for your LAN"
5. Enter:
   - **Address:** `192.168.1.100`
   - **Port:** `8080`
6. *(Optional)* Click **Advanced** for per-protocol settings:
   - HTTP: `192.168.1.100:8080`
   - HTTPS: `192.168.1.100:8080`  
   - FTP: `192.168.1.100:8080`
   - SOCKS: Leave blank (unless needed)
7. Add bypass list: `*.local;*.company.com;127.0.0.1`
8. Click **OK** on all dialogs

**Applies to:** Chrome, Edge, Internet Explorer, and most Windows apps

---

### Linux

**GUI Method (GNOME/Ubuntu):**

1. **Settings** → **Network** → **Network Proxy**
2. Select **Manual**
3. Enter for each:
   - **HTTP Proxy:** `192.168.1.100` Port `8080`
   - **HTTPS Proxy:** `192.168.1.100` Port `8080`
   - **FTP Proxy:** `192.168.1.100` Port `8080`
4. **Ignore Hosts:** `localhost,127.0.0.1,*.local,*.company.com`
5. Click **Apply system-wide**
6. Log out and back in (or restart apps)

---

**Command-Line Method (all distros):**

**Temporary (current session only):**

```bash
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8080
export ftp_proxy=http://192.168.1.100:8080
export no_proxy=localhost,127.0.0.1,*.local,*.company.com
```

**Permanent (system-wide):**

1. Edit `/etc/environment` (system-wide for all users):
   ```bash
   sudo nano /etc/environment
   ```

2. Add these lines:
   ```
   http_proxy="http://192.168.1.100:8080"
   https_proxy="http://192.168.1.100:8080"
   ftp_proxy="http://192.168.1.100:8080"
   no_proxy="localhost,127.0.0.1,*.local,*.company.com"
   ```

3. Save and reboot (or run `source /etc/environment`)

**Permanent (per-user):**

Add to `~/.bashrc` or `~/.profile`:

```bash
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8080
export no_proxy=localhost,127.0.0.1,*.local
```

Apply immediately:
```bash
source ~/.bashrc
```

---

**Package Manager Proxy (APT/YUM):**

**APT (Debian/Ubuntu):**

```bash
# Create APT proxy config
sudo nano /etc/apt/apt.conf.d/95proxies
```

Add:
```
Acquire::http::Proxy "http://192.168.1.100:8080";
Acquire::https::Proxy "http://192.168.1.100:8080";
```

**YUM/DNF (RHEL/CentOS/Fedora):**

```bash
sudo nano /etc/yum.conf
```

Add:
```ini
proxy=http://192.168.1.100:8080
```

---

### macOS

**System-Wide Method (Safari, Chrome, most apps):**

1. **System Settings** → **Network**
2. Select your active connection (Wi-Fi or Ethernet)
3. Click **Details** → **Proxies**
4. **Uncheck** "Auto Proxy Discovery" (disable WPAD)
5. **Check** these:
   - **Web Proxy (HTTP)**
   - **Secure Web Proxy (HTTPS)**
6. For each, enter:
   - **Web Proxy Server:** `192.168.1.100:8080`
   - **Secure Web Proxy Server:** `192.168.1.100:8080`
7. **Bypass proxy settings for these Hosts & Domains:**
   ```
   *.local, localhost, 127.0.0.1, *.company.com
   ```
   Use commas (`,`) to separate entries
8. **Check** "Exclude simple hostnames"
9. Click **OK** → **Apply**

:::tip Network Locations
Create separate network locations (Home, Office) with different proxy settings. Switch via **System Settings → Network → Location**.
:::

---

**Terminal/CLI Apps:**

Add to `~/.bash_profile` or `~/.zshrc`:

```bash
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8080
export no_proxy=localhost,127.0.0.1,*.local
```

Apply immediately:
```bash
source ~/.bash_profile
# or
source ~/.zshrc
```

## Test Your Configuration

**1. Test browser traffic:**

Open any browser (without explicit proxy config) and navigate to `http://example.com`

**2. Verify proxy is being used:**

```bash
# On SafeSquid server:
tail -f /var/log/safesquid/access/extended.log
```

You should see requests from your client IP.

**3. Test CLI tools:**

```bash
# Test with curl
curl -I http://example.com

# Check environment variables (Linux/macOS)
echo $http_proxy
echo $https_proxy

# Windows PowerShell:
[System.Net.WebRequest]::DefaultWebProxy
```

**4. Test bypass list:**

Navigate to an internal site (e.g., `http://intranet.local`)
- Should load directly (not via proxy)
- Should NOT appear in SafeSquid logs

## Troubleshooting

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|------------------|---------|
| Browser works, CLI tools don't | Environment variables not set | Add to `/etc/environment` or shell profile (see steps above) |
| "Proxy refusing connections" | SafeSquid not running or firewall blocking | **Server:** `systemctl status safesquid` <br/> **Client:** `telnet 192.168.1.100 8080` |
| Settings don't persist after reboot | Not saved to system config | Use `/etc/environment` (Linux) or System Settings (Win/Mac), not session exports |
| Some apps ignore proxy | App uses own proxy settings | See [Application-Specific Configuration](/docs/Getting_Started/Connect_Your_Client/Application_Specific_Configuration/) |
| Bypass list not working | Syntax error (semicolons vs commas) | Windows: use `;` <br/> Linux/macOS: use `,` |
| WPAD conflicts with manual proxy | Auto-detect enabled | Disable "Automatically detect settings" / "Auto Proxy Discovery" |

**Still not working?**

1. **Verify settings are actually applied:**
   - **Windows:** `netsh winhttp show proxy`
   - **macOS:** `scutil --proxy`
   - **Linux:** `env | grep proxy`

2. **Check SafeSquid accessibility:**
   ```bash
   curl -I --proxy http://192.168.1.100:8080 http://example.com
   ```

3. **Check for conflicting proxy settings:**
   - Browser extensions (proxy switchers)
   - VPN software
   - Security software

## Advanced: Windows Registry Method

For automation or GPO deployment, configure proxy via registry:

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings]
"ProxyEnable"=dword:00000001
"ProxyServer"="192.168.1.100:8080"
"ProxyOverride"="*.local;*.company.com;127.0.0.1;localhost"
```

Save as `proxy.reg` and run, or deploy via GPO.

:::caution Registry Edits

Only use this method if you're comfortable with registry editing. Incorrect changes can break networking. Use Settings app for manual configuration.

:::

## Next Steps

1. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm all application traffic flows through SafeSquid
2. **[Application-Specific Configuration](/docs/Getting_Started/Connect_Your_Client/Application_Specific_Configuration/)** — Configure Docker, Git, npm, and other tools that ignore system proxy
3. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Deploy SafeSquid root CA for HTTPS inspection
4. **Scale to enterprise:** [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/) — Push system proxy via GPO/MDM for 100+ endpoints
