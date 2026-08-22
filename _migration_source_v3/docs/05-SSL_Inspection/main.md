---
title: SSL Inspection
slug: /SSL_Inspection
description: Configure HTTPS inspection in SafeSquid to decrypt and analyze encrypted traffic for web security, malware detection, and policy enforcement.
keywords:
  - SafeSquid HTTPS inspection
  - SSL inspection SafeSquid
  - decrypt HTTPS traffic SafeSquid
  - web filtering encrypted traffic
  - SSL certificate configuration SafeSquid
  - HTTPS scanning enterprise proxy
---

# SSL Inspection

HTTPS inspection (SSL/TLS interception) allows SafeSquid to decrypt, inspect, and re-encrypt HTTPS traffic. Without this, encrypted traffic remains a blind spot—malware, phishing, and data leakage can pass through undetected.

## When to Use SSL Inspection

| Enable SSL Inspection When | Use Bypass Instead |
|----------------------------|--------------------|
| Enforcing web security policies on HTTPS | Banking and financial sites (compliance) |
| Scanning encrypted downloads for malware | Healthcare portals (HIPAA) |
| DLP on HTTPS uploads (file sharing, webmail) | SSL-pinned mobile apps (cannot inspect) |
| Application control (identify SaaS apps in HTTPS) | Government sites (security requirements) |
| URL filtering on encrypted sites | Personal/sensitive user traffic (privacy policy) |

:::tip Selective Inspection
You don't need to inspect everything. Use bypass policies to exclude sensitive categories while inspecting the rest.
:::

---

## Why HTTPS Inspection Matters

**The Problem:**
- 95%+ of web traffic is HTTPS
- Encrypted traffic hides malicious payloads, phishing attempts, and data exfiltration
- Without inspection, your proxy can only see domain names, not content

**What HTTPS Inspection Enables:**
- URL filtering on HTTPS sites
- Malware scanning of encrypted downloads
- Data Loss Prevention (DLP) on HTTPS uploads
- Application control (detect Google Drive, Dropbox, etc. in HTTPS traffic)
- Content security (block ransomware downloads, malicious scripts)

**Compliance:**
- PCI-DSS 10.x requires visibility into web traffic
- SOC 2 CC6.1 expects monitoring of encrypted traffic where applicable

---

## How It Works

1. **Client → SafeSquid:** Browser connects to SafeSquid using SafeSquid's certificate
2. **SafeSquid → Origin:** SafeSquid creates a separate TLS connection to the destination
3. **Inspection:** SafeSquid sees the decrypted content and applies policies
4. **Re-encryption:** SafeSquid re-encrypts and forwards to the destination

**Result:** Traffic remains encrypted end-to-end, but SafeSquid can inspect the content.

---

## Important Considerations

### Bypass is Required For:

- **SSL-pinned applications** (mobile apps, some desktop software)
- **Banking and financial sites** (compliance/privacy)
- **Healthcare portals** (HIPAA compliance)
- **Government sites** (security requirements)

SafeSquid allows bypass rules to exclude specific domains from inspection.

### Client Trust Required:

All client browsers and applications must trust the SafeSquid Root CA certificate. Without trust, users see certificate warnings on every HTTPS site.

**Deploy the Root CA to:**
- Windows certificate store (for Chrome, Edge, IE)
- Firefox certificate store (separate)
- macOS Keychain (for Safari, system-wide)
- Mobile devices (via MDM)

---

## Configuration Guides

### [Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/)

**Complete setup guide covering:**
- Generate or import Root CA certificate (Self-Service Portal)
- Enable HTTPS inspection in SafeSquid
- Configure bypass policies for sensitive domains
- Deploy Root CA to clients (Windows, macOS, Firefox, mobile)
- Verify inspection is working

**Start here** for first-time SSL Inspection setup.

---

### [Import Certificate into Chrome/IE](/docs/SSL_Inspection/Import_Certificate_Chrome_IE/)

**Step-by-step walkthrough** for importing the SafeSquid Root CA into the Windows Trusted Root Certification Authorities store (used by Chrome, Edge, and Internet Explorer).

**Use this** after enabling HTTPS inspection to eliminate browser certificate warnings on Windows clients.

---

## Quick Start Checklist

1. ✅ **[Generate Root CA](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#generating-ssl-certificates)** in Self-Service Portal
2. ✅ **[Enable HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#enabling-ssl-inspection)** in SafeSquid Configuration Portal
3. ✅ **[Configure bypass policies](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#bypass-policies)** for banking/healthcare sites
4. ✅ **Deploy Root CA** to all clients:
   - [Windows (Chrome/IE)](/docs/SSL_Inspection/Import_Certificate_Chrome_IE/)
   - [Firefox](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#import-certificate-into-firefox)
   - macOS via MDM or Keychain
   - Mobile via MDM
5. ✅ **[Verify](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#verification)** inspection is working (check padlock icon, test bypass)

---

## Common Questions

**Q: Will users see certificate warnings?**  
A: Yes, until you deploy the SafeSquid Root CA to their devices. Once trusted, no warnings appear.

**Q: Can I inspect only some sites and not others?**  
A: Yes, use bypass policies to exclude specific domains (e.g., banking sites).

**Q: What about mobile apps that use certificate pinning?**  
A: Add those apps' domains to the bypass list. They cannot be inspected.

**Q: Does this slow down HTTPS traffic?**  
A: Minimal impact (&lt;50ms latency) if hardware supports AES-NI. Without AES-NI, expect 100-300ms per connection.

---

## Next Steps

1. **[Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/)** — Complete setup guide
2. **[Authentication](/docs/Authentication/main/)** — Enable user-aware policies after SSL Inspection
3. **[Access Restriction](/docs/Access_Restriction/main/)** — Configure URL filtering (now works on HTTPS)
4. **[Data Leakage Prevention](/docs/Data_Leakage_Prevention/main/)** — Scan HTTPS uploads for sensitive data
