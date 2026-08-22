---
title: "Application-Specific Configuration"
description: "Proxy configuration procedures for non-browser applications including email clients, development tools, and command-line utilities with SafeSquid SWG"
keywords:
  - SafeSquid application proxy
  - email client proxy
  - development tools proxy
  - command line proxy
  - Outlook proxy configuration
  - Git proxy settings
---

# Application-Specific Configuration

**Application-specific configuration** is needed for apps that ignore system-wide proxy settings—developer tools (Git, Docker, npm), email clients, and CLI utilities.

**Use this method for:**
- Developer workstations (Git, Docker, npm, pip)
- Email clients (Outlook, Thunderbird)
- Command-line tools (curl, wget, apt, yum)
- Apps that bypass system proxy

**Time to configure:** 2-5 minutes per application

:::tip System Proxy First

Try [System-Wide Proxy](/docs/Getting_Started/Connect_Your_Client/System_Wide_Proxy/) first. Only configure apps individually if they ignore system settings.

:::

## Prerequisites

:::info Before You Start

- SafeSquid IP and port (default: 8080)
- Application installed and accessible
- Admin/sudo access if modifying system config files
- (Optional) Proxy authentication credentials

:::

## Top 10 Applications

### 1. Git

**Set proxy globally:**

```bash
git config --global http.proxy http://192.168.1.100:8080
git config --global https.proxy http://192.168.1.100:8080
```

**Bypass for internal repos:**

```bash
git config --global http.noProxy "*.company.local,*.company.com"
```

**Verify:**

```bash
git config --global --get http.proxy
# Should show: http://192.168.1.100:8080
```

**Test:**

```bash
git clone https://github.com/test/repo.git
```

**Unset proxy:**

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

### 2. Docker

**Configure Docker daemon** (`/etc/docker/daemon.json`):

```json
{
  "proxies": {
    "http-proxy": "http://192.168.1.100:8080",
    "https-proxy": "http://192.168.1.100:8080",
    "no-proxy": "localhost,127.0.0.1,*.local"
  }
}
```

**Restart Docker:**

```bash
sudo systemctl restart docker
```

**Verify:**

```bash
docker info | grep -i proxy
```

**Test:**

```bash
docker pull nginx
```

---

### 3. npm (Node.js Package Manager)

**Set proxy:**

```bash
npm config set proxy http://192.168.1.100:8080
npm config set https-proxy http://192.168.1.100:8080
npm config set registry https://registry.npmjs.org/
```

**Verify:**

```bash
npm config get proxy
npm config get https-proxy
```

**Test:**

```bash
npm install express
```

**Unset proxy:**

```bash
npm config delete proxy
npm config delete https-proxy
```

---

### 4. Python pip

**Via command-line (one-time):**

```bash
pip install --proxy http://192.168.1.100:8080 requests
```

**Via config file (permanent):**

Create `~/.pip/pip.conf` (Linux/macOS) or `%APPDATA%\pip\pip.ini` (Windows):

```ini
[global]
proxy = http://192.168.1.100:8080
```

**Verify:**

```bash
pip config list
```

**Test:**

```bash
pip install requests
```

---

### 5. APT (Debian/Ubuntu Package Manager)

**Create config file:**

```bash
sudo nano /etc/apt/apt.conf.d/95proxies
```

**Add:**

```
Acquire::http::Proxy "http://192.168.1.100:8080";
Acquire::https::Proxy "http://192.168.1.100:8080";
```

**Test:**

```bash
sudo apt update
```

---

### 6. YUM/DNF (RHEL/CentOS/Fedora Package Manager)

**Edit config:**

```bash
sudo nano /etc/yum.conf
```

**Add:**

```ini
proxy=http://192.168.1.100:8080
```

**Test:**

```bash
sudo yum check-update
```

---

### 7. curl

**Via command-line (one-time):**

```bash
curl --proxy http://192.168.1.100:8080 https://example.com
```

**Via environment variable (session):**

```bash
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8080
curl https://example.com
```

**Via config file (`~/.curlrc`):**

```
proxy = "http://192.168.1.100:8080"
```

---

### 8. wget

**Via command-line:**

```bash
wget --proxy=on --http-proxy=192.168.1.100:8080 https://example.com
```

**Via config file (`~/.wgetrc`):**

```
http_proxy = http://192.168.1.100:8080
https_proxy = http://192.168.1.100:8080
use_proxy = on
```

---

### 9. Microsoft Outlook (Windows)

Outlook typically uses system proxy settings. If manual configuration needed:

1. **File** → **Account Settings** → **Account Settings**
2. Select account → **Change** → **More Settings**
3. **Connection** tab
4. **Connect using Internet Explorer or a 3rd party dialer**
   - This makes Outlook use Windows system proxy

**For Exchange/Office 365:**
- Outlook inherits Windows proxy settings automatically
- No manual configuration needed if system proxy is set

**Troubleshooting:** If Outlook won't connect, disable "Cached Exchange Mode" temporarily

---

### 10. Thunderbird (Email Client)

1. **Menu** (☰) → **Settings** → **General**
2. Scroll to **Network & Disk Space** → **Connection Settings**
3. Select **Manual proxy configuration**
4. Enter:
   - **HTTP Proxy:** `192.168.1.100` **Port:** `8080`
   - **Use this proxy server for all protocols**
5. **No Proxy for:** `localhost, 127.0.0.1, *.local`
6. Click **OK**

---

## Other Applications

**General approaches for unlisted apps:**

1. **Check app documentation** for proxy settings location
2. **Try system environment variables** (many apps respect them):
   ```bash
   export http_proxy=http://192.168.1.100:8080
   export https_proxy=http://192.168.1.100:8080
   ```
3. **Search for config files** in:
   - Linux/macOS: `~/.config/[appname]/` or `~/.appname/`
   - Windows: `%APPDATA%\[AppName]\`
4. **Look for command-line flags**: `--proxy`, `-x`, `--http-proxy`

**Common config patterns:**

- **Java apps:** Set `-Dhttp.proxyHost=192.168.1.100 -Dhttp.proxyPort=8080`
- **Ruby gems:** `gem install --http-proxy http://192.168.1.100:8080 package`
- **Go modules:** `export GOPROXY=http://192.168.1.100:8080`

---

## Test Your Configuration

**For each app:**

1. **Run a network operation:**
   - Git: `git clone https://github.com/test/repo.git`
   - Docker: `docker pull nginx`
   - npm: `npm install express`
   - pip: `pip install requests`

2. **Check SafeSquid logs:**
   ```bash
   # On SafeSquid server:
   tail -f /var/log/safesquid/access/extended.log
   ```
   Should show requests from your IP with app's user-agent

3. **Verify bypass works:**
   - Configure bypass for internal repos/registries
   - Internal traffic should NOT appear in SafeSquid logs

---

## Troubleshooting

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|------------------|---------|
| "Connection refused" | Wrong proxy IP or port | Verify: `telnet 192.168.1.100 8080` |
| "Proxy authentication required" | SafeSquid requires auth | Add credentials: `http://user:pass@192.168.1.100:8080` |
| "SSL certificate verify failed" | SSL inspection enabled, CA not trusted | Install SafeSquid root CA (see [SSL Inspection](/docs/SSL_Inspection/main/)) |
| App ignores proxy setting | Environment variables override config | Unset: `unset http_proxy https_proxy` then retry |
| Docker pull fails | No-proxy misconfigured | Add Docker registry to no-proxy list |
| Git clone very slow | Large repo + proxy overhead | Use SSH instead of HTTPS, or bypass for internal Git |

**Still not working?**

1. **Test direct connectivity first:**
   ```bash
   # Without proxy:
   unset http_proxy https_proxy
   curl https://example.com
   ```
   If this fails, issue isn't proxy—check network/firewall

2. **Test proxy manually:**
   ```bash
   curl --proxy http://192.168.1.100:8080 https://example.com
   ```
   If this works, app config is wrong

3. **Check SafeSquid logs for errors:**
   ```bash
   tail -50 /var/log/safesquid/safesquid.log
   ```

---

## Next Steps

1. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm all application traffic flows through SafeSquid
2. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Install root CA for apps that validate certificates (Git, pip, npm, Docker)
3. **[Access Restriction](/docs/Access_Restriction/main/)** — Set policies for specific applications or protocols
