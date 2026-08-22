---
title: "PAC File Configuration"
description: "Client-side Proxy Auto-Configuration (PAC) file setup and deployment for automated SafeSquid proxy selection across browsers and operating systems"
keywords:
  - SafeSquid PAC file
  - proxy auto-configuration
  - automatic proxy selection
  - PAC file deployment
  - WPAD configuration
  - browser PAC setup
---

# PAC File Configuration

**PAC (Proxy Auto-Configuration)** files use JavaScript to automatically select the right proxy for each request. Browsers fetch the PAC file from a URL and execute it for every connection.

**Use this method for:**
- Medium deployments (10-100 users)
- Conditional routing (internal sites direct, external via proxy)
- Load balancing across multiple SafeSquid nodes
- Automatic failover when a proxy is down

**Time to deploy:** 10 minutes to create PAC + distribute URL

:::tip When to Use PAC Files

Use PAC files when you need flexibility (different rules for different sites) without reconfiguring every browser. For enterprise scale (100+ endpoints), use [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/) to push PAC URLs via GPO/MDM.

:::

## Prerequisites

:::info Before You Start

- Web server to host PAC file (Apache, Nginx, IIS, or any HTTP server)
- SafeSquid IP address and port (default: 8080)
- (Optional) Multiple SafeSquid IPs for load balancing/failover
- Basic JavaScript knowledge to customize PAC logic

:::

## Hosting Methods

| **Method** | **When to Use** | **Pros** | **Cons** |
|------------|-----------------|----------|----------|
| **HTTP Server** | Production, multiple users | Centralized updates, automatic distribution | Requires web server |
| **File Protocol** | Testing, single machine | No server needed, instant changes | Must copy file to every machine |

**Recommended:** Use HTTP for anything beyond single-user testing.

## Create Your PAC File

PAC files contain a single JavaScript function: `FindProxyForURL(url, host)`

**Basic example** (save as `proxy.pac`):

```javascript
function FindProxyForURL(url, host) {
    // Direct connection for localhost and internal IPs
    if (isInNet(host, "192.168.0.0", "255.255.0.0") ||
        isInNet(host, "10.0.0.0", "255.0.0.0") ||
        host == "localhost" ||
        host == "127.0.0.1") {
        return "DIRECT";
    }

    // Direct connection for internal domains
    if (dnsDomainIs(host, ".company.local") ||
        dnsDomainIs(host, ".internal.company.com")) {
        return "DIRECT";
    }

    // Use SafeSquid proxy for external traffic with failover
    // If first proxy fails, browser tries second automatically
    return "PROXY 192.168.1.100:8080; PROXY 192.168.1.101:8080; DIRECT";
}
```

**What each line does:**

- **`isInNet(host, network, mask)`** — True if host IP is in network range
- **`dnsDomainIs(host, domain)`** — True if host ends with domain
- **`PROXY ip:port`** — Use this proxy
- **`DIRECT`** — Connect directly (no proxy)
- **Semicolons** — Separate fallback options (try first, if fails try next)

---

**Advanced example** (load balancing by URL):

```javascript
function FindProxyForURL(url, host) {
    // Direct for internal
    if (isInNet(host, "10.0.0.0", "255.0.0.0")) {
        return "DIRECT";
    }

    // Load balance by hashing hostname
    var hash = 0;
    for (var i = 0; i < host.length; i++) {
        hash = ((hash << 5) - hash) + host.charCodeAt(i);
    }
    
    // Distribute across 3 proxies
    var proxyNum = Math.abs(hash) % 3;
    
    if (proxyNum == 0) {
        return "PROXY 192.168.1.100:8080; PROXY 192.168.1.101:8080";
    } else if (proxyNum == 1) {
        return "PROXY 192.168.1.101:8080; PROXY 192.168.1.102:8080";
    } else {
        return "PROXY 192.168.1.102:8080; PROXY 192.168.1.100:8080";
    }
}
```

## Common PAC Functions Reference

| **Function** | **Purpose** | **Example** |
|--------------|-------------|-------------|
| `isInNet(host, pattern, mask)` | Check if IP is in subnet | `isInNet(host, "10.0.0.0", "255.0.0.0")` |
| `dnsDomainIs(host, domain)` | Check if domain matches | `dnsDomainIs(host, ".google.com")` |
| `shExpMatch(str, pattern)` | Shell-style wildcard match | `shExpMatch(url, "*.pdf")` |
| `localHostOrDomainIs(host, domain)` | Exact match or subdomain | `localHostOrDomainIs(host, "www.company.com")` |
| `isResolvable(host)` | Check if DNS resolves | `isResolvable(host)` |
| `isPlainHostName(host)` | No dots in hostname | `isPlainHostName(host)` |
| `dnsDomainLevels(host)` | Count domain levels | `dnsDomainLevels(host) > 0` |
| `weekdayRange(day1, day2)` | Day of week | `weekdayRange("MON", "FRI")` |
| `timeRange(h1, h2)` | Time of day | `timeRange(9, 17)` |

**Full reference:** [MDN PAC Functions](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file)

## Deploy the PAC File

### Step 1: Host the PAC File

**On HTTP server (recommended):**

```bash
# Apache/Nginx: Place in web root
sudo cp proxy.pac /var/www/html/
sudo chmod 644 /var/www/html/proxy.pac

# Verify accessible:
curl http://YOUR-SERVER-IP/proxy.pac
```

**MIME type** (required for some browsers to recognize PAC files):
```
application/x-ns-proxy-autoconfig
```

If browsers fail to load your PAC file, verify the web server sends the correct Content-Type header. Add to Apache: `AddType application/x-ns-proxy-autoconfig .pac` or Nginx: `types { application/x-ns-proxy-autoconfig pac; }`

**For file:// protocol** (testing only):
- Windows: `C:\PAC\proxy.pac` → `file:///C:/PAC/proxy.pac`
- Linux/macOS: `/home/user/proxy.pac` → `file:///home/user/proxy.pac`

---

### Step 2: Configure Browsers

**Windows (Chrome, Edge, IE — system-wide):**

1. **Settings** → **Network & Internet** → **Proxy**
2. Toggle **Automatically detect settings** to **Off** (disable WPAD)
3. Toggle **Use setup script** to **On**
4. Enter PAC URL: `http://pac-server.company.com/proxy.pac`
5. Click **Save**

**Firefox (all platforms):**

1. **Menu** (☰) → **Settings** → **Network Settings** → **Settings**
2. Select **Automatic proxy configuration URL**
3. Enter PAC URL
4. Click **OK**

**macOS (Safari, Chrome — system-wide):**

1. **System Settings** → **Network** → Select connection → **Details** → **Proxies**
2. Check **Automatic Proxy Configuration**
3. Enter PAC URL
4. Click **OK** → **Apply**

**Linux (system-wide):**

```bash
# GNOME/Ubuntu:
gsettings set org.gnome.system.proxy mode 'auto'
gsettings set org.gnome.system.proxy autoconfig-url 'http://pac-server.company.com/proxy.pac'

# KDE:
kwriteconfig5 --file kioslaverc --group 'Proxy Settings' --key 'Proxy Config Script' 'http://pac-server.company.com/proxy.pac'
```

## Debug Your PAC File

PAC files are JavaScript — errors break proxy selection.

**Method 1: Browser Developer Console**

1. Open DevTools (F12)
2. Go to **Console** tab
3. Reload page — PAC errors appear here

**Method 2: Add alert() statements**

```javascript
function FindProxyForURL(url, host) {
    alert("Testing PAC for: " + host);  // Debug line
    
    if (isInNet(host, "10.0.0.0", "255.0.0.0")) {
        alert("Matched internal IP, going DIRECT");
        return "DIRECT";
    }
    
    alert("Using proxy");
    return "PROXY 192.168.1.100:8080";
}
```

**Method 3: Online PAC tester**

- [PAC File Tester](http://www.proxytester.com/)
- Paste PAC content, test URLs

**Method 4: Command-line (pactester)**

```bash
# Install pactester (Debian/Ubuntu)
sudo apt install pacparser

# Test PAC function directly
pactester -p proxy.pac -u http://example.com -h example.com
```

*`pactester` is part of the `pacparser` package. For other distros: search for "pacparser" or "pactester" in your package manager.*

**Common errors:**

- **Syntax error:** Missing semicolon, bracket, or quote
- **Function undefined:** Typo in `isInNet`, `dnsDomainIs`, etc.
- **PAC file not loading:** Wrong MIME type or URL unreachable

## Test Your Configuration

1. **Open browser configured with PAC URL**
2. **Navigate to external site:** `http://example.com`
3. **Check if it loads** ✅
4. **Verify proxy was used:**
   ```bash
   # On SafeSquid server:
   tail -f /var/log/safesquid/access/extended.log
   ```
   Should show request from your client IP

5. **Test internal bypass:**
   - Navigate to internal site (e.g., `http://intranet.company.local`)
   - Should load instantly (DIRECT, not via proxy)
   - Should NOT appear in SafeSquid logs

**Debug proxy selection:**

- **Chrome:** `chrome://net-internals/#proxy`
- **Firefox:** `about:networking#dnslookuptool`
- **Edge:** `edge://net-internals/#proxy`

## Troubleshooting

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|------------------|---------|
| "PAC script failed" | JavaScript syntax error | Check browser console (F12) for errors |
| PAC file not loading | Wrong URL or unreachable | Test: `curl http://pac-server.com/proxy.pac` |
| All sites go DIRECT | PAC logic error or wrong fallback | Add `alert()` statements to debug |
| Internal sites use proxy | Bypass logic missing | Add `isInNet()` or `dnsDomainIs()` checks |
| Browser ignores PAC | WPAD enabled | Disable "Automatically detect settings" |
| Slow page loads | PAC function takes too long | Simplify logic, avoid DNS lookups in PAC |

**Still not working?**

1. **Verify PAC file content:**
   ```bash
   curl http://pac-server.company.com/proxy.pac
   ```
   Should return JavaScript, not HTML error page

2. **Test PAC function manually:**
   ```bash
   pactester -p proxy.pac -u http://google.com -h google.com
   ```

3. **Check web server MIME type:**
   ```bash
   curl -I http://pac-server.company.com/proxy.pac
   ```
   Should include: `Content-Type: application/x-ns-proxy-autoconfig`

## Advanced: WPAD (Auto-Discovery)

WPAD (Web Proxy Auto-Discovery) lets browsers find the PAC file automatically without manual URL entry.

**Requirements:**

1. DNS record: `wpad.company.com` pointing to PAC server IP
2. PAC file named `wpad.dat` (not `proxy.pac`)
3. Browsers set to "Automatically detect settings"

**DNS configuration:**

```bash
# Add to DNS zone:
wpad.company.com. IN A 192.168.1.10
```

**Place PAC at:**
```
http://wpad.company.com/wpad.dat
```

:::caution WPAD Security Risk

WPAD can be hijacked on untrusted networks (coffee shops, airports) through DNS or DHCP poisoning attacks—an attacker can serve a malicious PAC file that routes traffic through their proxy. For production, use explicit PAC URLs distributed via GPO/MDM instead of relying on WPAD auto-discovery.

:::

## Next Steps

1. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm traffic flows through SafeSquid
2. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Enable HTTPS decryption
3. **Scale your deployment:**
   - **Enterprise (100+ endpoints):** [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/) — Push PAC URL via GPO/MDM
   - **Application-specific:** [Application Configuration](/docs/Getting_Started/Connect_Your_Client/Application_Specific_Configuration/) — Configure non-browser apps
