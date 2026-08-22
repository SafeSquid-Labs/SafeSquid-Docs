---
title: Connect Your Client
slug: /Getting_Started/Connect_Your_Client
description: Configure browsers and applications to use SafeSquid as an HTTP proxy — from explicit proxy to enterprise deployment.
keywords:
  - SafeSquid proxy setup
  - browser proxy configuration
  - explicit proxy
  - PAC file
  - enterprise proxy deployment
---

# Connect Your Client

Web traffic flows through SafeSquid only when clients are configured to use it as their HTTP proxy. Choose a configuration method based on your deployment scale and environment:

- **Explicit Proxy** — Manual browser configuration (testing, single users)
- **PAC File** — Automated proxy selection for all browsers (medium deployments)
- **System-Wide Proxy** — OS-level configuration for all applications (complete coverage)
- **Enterprise Deployment** — Mass rollout via GPO, MDM, or config management (production at scale)
- **Application-Specific** — Individual app configuration (Git, Docker, CLI tools)

:::info Before You Start

- SafeSquid installed and running (verify by accessing `https://SERVER-IP:8443`)
- License activated (see [Activate Your License](/docs/Getting_Started/Activate/)) for full feature access
- Note your SafeSquid server IP address and port (default: 8080)
- For HTTPS sites, you'll need [SSL Inspection](/docs/SSL_Inspection/main/) configured later

:::

## Which Method Should I Use?

| **Scenario** | **Recommended Method** | **Why** |
|--------------|------------------------|---------|
| Testing SafeSquid for the first time | [Explicit Proxy](#explicit-proxy) | Fastest way to validate installation |
| Single user, multiple browsers | [PAC File](#pac-file) | Configure once, applies to all browsers |
| Need all apps on a machine proxied | [System-Wide Proxy](#system-wide-proxy) | OS-level proxy covers browsers + CLI tools |
| Rolling out to 10-1000+ endpoints | [Enterprise Deployment](#enterprise-deployment) | GPO/MDM push for consistent configuration |
| Only specific apps need proxy (e.g., Docker) | [Application-Specific](#application-specific-configuration) | Configure individual apps without affecting others |

**For production:** Start with [Explicit Proxy](#explicit-proxy) to test, then use [Enterprise Deployment](#enterprise-deployment) for full rollout.

## Configuration Methods

### [Explicit Proxy](/docs/Getting_Started/Connect_Your_Client/Explicit_Proxy/)

**Manual browser configuration.** Set proxy IP and port in browser settings for quick testing or controlled environments.

**Use this for:** Initial testing, single-user setups, or when you need immediate validation that SafeSquid is working.

**Time to deploy:** 2 minutes per browser.

---

### [PAC File](/docs/Getting_Started/Connect_Your_Client/PAC_File/)

**Automated proxy selection.** Deploy a Proxy Auto-Configuration (PAC) file that all browsers reference. Supports conditional routing (e.g., direct access for internal sites, proxy for internet).

**Use this for:** Medium deployments (10-100 users), branch offices, or when you need flexible proxy rules without reconfiguring every browser.

**Time to deploy:** 10 minutes to create PAC file + distribute URL.

---

### [System-Wide Proxy](/docs/Getting_Started/Connect_Your_Client/System_Wide_Proxy/)

**OS-level configuration.** Configure Windows, macOS, or Linux to route all application traffic through SafeSquid—browsers, CLI tools, and background apps.

**Use this for:** Complete traffic coverage on individual machines, developer workstations, or endpoints where all apps must use the proxy.

**Time to deploy:** 5 minutes per OS.

---

### [Enterprise Deployment](/docs/Getting_Started/Connect_Your_Client/Enterprise_Deployment/)

**Mass rollout via GPO, MDM, or config management.** Push proxy settings to hundreds or thousands of endpoints using Group Policy (Windows), MDM (macOS/mobile), Puppet, Ansible, or SCCM.

**Use this for:** Production deployments, organization-wide rollouts, or when you need centralized control and consistent configuration.

**Time to deploy:** Initial setup 1-2 hours, then automatic for all endpoints.

---

### [Application-Specific Configuration](/docs/Getting_Started/Connect_Your_Client/Application_Specific_Configuration/)

**Configure individual applications.** Set proxy for Git, npm, Docker, email clients, and CLI tools that don't inherit system proxy settings.

**Use this for:** Developer tools, containerized apps, or when only specific applications need proxy access.

**Time to deploy:** 2-5 minutes per application.

## Testing Your Configuration

After configuring any method, test immediately:

1. **Open a browser** configured to use SafeSquid
2. **Navigate to** `http://example.com`
3. **Check SafeSquid logs:**
   ```bash
   tail -20 /var/log/safesquid/access/extended.log
   ```
   You should see the request logged with client IP, URL, and timestamp
   
   *(Use `tail -f` to follow live logs; press Ctrl+C to exit)*

**Verify proxy is being used:**
Visit a site like [whatismyip.com](https://whatismyip.com) — the displayed IP should match your SafeSquid server's WAN IP, not your client's direct IP.

**If the site doesn't load:**
- Verify SafeSquid is running: `systemctl status safesquid`
- Check firewall allows port 8080
- Confirm proxy IP and port in client settings
- See [Troubleshooting](/docs/Troubleshooting/main/) for common issues

**For HTTPS sites:** You'll see certificate warnings until [SSL Inspection](/docs/SSL_Inspection/main/) is configured.

## Next Steps

1. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Run comprehensive smoke tests to confirm traffic flows
2. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Enable HTTPS decryption so SafeSquid can inspect encrypted traffic
3. **[Configure Policies](/docs/Access_Restriction/main/)** — Set up access controls and content filtering
4. **[Scale Your Deployment](#enterprise-deployment)** — If testing succeeded, roll out to all endpoints using Enterprise Deployment methods
