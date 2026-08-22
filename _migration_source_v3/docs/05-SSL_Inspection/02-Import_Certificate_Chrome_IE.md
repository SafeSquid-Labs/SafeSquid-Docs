---
title: Import Certificate into Chrome or Internet Explorer
description: Step-by-step import of SafeSquid SSL certificate into Chrome or Internet Explorer for HTTPS inspection trust.
keywords:
  - import SafeSquid certificate Chrome
  - import SafeSquid certificate IE
  - SSL certificate install Chrome IE
  - Trusted Root Certification Authorities
  - HTTPS inspection client trust
---

# Import SafeSquid Root CA into Chrome or Internet Explorer

Chrome, Edge, and Internet Explorer use the Windows certificate store. Follow this guide to import the SafeSquid Root CA into **Trusted Root Certification Authorities** so HTTPS inspection works without certificate warnings.

**Time to complete:** 2-5 minutes per machine

:::tip Automated Deployment

For enterprise environments, deploy the certificate via **Group Policy (GPO)** instead of manual installation:
1. Copy certificate to `\\domain.com\SYSVOL\domain.com\Policies\`
2. GPO → Computer Configuration → Policies → Windows Settings → Security Settings → Public Key Policies → Trusted Root Certification Authorities
3. Import → Select SafeSquid certificate → Apply

:::

:::note Firefox Users

Firefox uses its own certificate store and ignores the Windows trust store. See [Import certificate into Firefox](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#import-certificate-into-firefox).

:::

---

## Prerequisites

:::info Before You Start

- SafeSquid Root CA certificate downloaded (from [Self-Service Portal](https://key.safesquid.com) or SafeSquid Configuration Portal)
- Windows machine with administrative privileges
- Chrome, Edge, or Internet Explorer installed

:::

---

## Import Steps

### 1. Open the Certificate File

Double-click the downloaded SafeSquid certificate file (usually `safesquid.crt` or `safesquid.cer`).

![Opening SafeSquid certificate](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image1.webp)

---

### 2. Click "Install Certificate"

![Install Certificate button](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image2.webp)

---

### 3. Select Store Location

Choose **"Local Machine"** (for all users on this computer) or **"Current User"** (for your account only).

**Recommended:** Local Machine (requires admin rights, applies to all users)

Click **Next**.

![Store location selection](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image3.webp)

---

### 4. Select Certificate Store

Click **"Browse"** to select the certificate store.

![Browse certificate store](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image4.webp)

---

### 5. Choose "Trusted Root Certification Authorities"

**Important:** Select **"Trusted Root Certification Authorities"** (NOT "Intermediate Certification Authorities").

Click **OK**.

![Select Trusted Root Certification Authorities](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image5.webp)

---

### 6. Continue with Import

Click **Next** to continue.

![Continue import](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image6.webp)

---

### 7. Finish Import

Click **Finish** to complete the import.

![Finish import](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image7.webp)

---

### 8. Confirm Success

A confirmation message appears: **"The import was successful."**

Click **OK**.

![Import successful confirmation](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image8.webp)

![Import complete](/img/How_To/Importing_Your_SSL_Certificate_Into_Internet_Explorer_or_Chrome/image9.webp)

---

## Verify Installation

### Test in Chrome/Edge

1. **Open Chrome or Edge**
2. **Browse to** `https://www.google.com` (via SafeSquid proxy)
3. **Click the padlock** in the address bar → **Connection is secure** → **Certificate**
4. **Verify:** Certificate chain shows SafeSquid Root CA as the issuer

**Expected:** No certificate warnings, padlock shows secure connection.

---

### Verify Certificate is in Trust Store

1. **Press Windows + R** → Type `certmgr.msc` → **Enter**
2. **Expand** "Trusted Root Certification Authorities" → **Certificates**
3. **Find** "SafeSquid" (or your organization name) in the list

**Expected:** SafeSquid certificate appears with expiry date and issuer information.

---

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| Still seeing certificate warnings | Certificate installed in wrong store | Verify certificate is in **Trusted Root Certification Authorities** (not Intermediate) |
| "Windows cannot access the file" | No admin privileges | Right-click certificate → **Run as administrator** |
| Import succeeds but warnings persist | Browser cache | Clear browser cache and restart browser: `chrome://settings/clearBrowserData` |
| Certificate not visible in certmgr | Installed for Current User instead of Local Machine | Re-install, select "Local Machine" in step 3 |
| Some sites work, others don't | HTTPS Inspection not enabled or partial bypass | Check SafeSquid Configuration Portal → HTTPS Inspection → Global = True |

**Still not working?**

1. **Restart browser completely** (close all windows)
2. **Check proxy settings:**
   - Chrome: `chrome://net-internals/#proxy`
   - Edge: `edge://net-internals/#proxy`
3. **Verify SafeSquid HTTPS Inspection is enabled:**
   - Navigate to SafeSquid Configuration Portal
   - Real-time Content Security → HTTPS Inspection → Global → Enabled = True

---

## Next Steps

1. **[Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/)** — Complete setup guide (if you haven't enabled inspection yet)
2. **[Import certificate into Firefox](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#import-certificate-into-firefox)** — Firefox uses separate trust store
3. **Deploy to all clients:**
   - **Windows enterprise:** Use GPO (see tip at top of page)
   - **macOS:** Use MDM or manual Keychain import
   - **Mobile:** Use MDM or manual installation
4. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm proxy and SSL Inspection are working

**Related:** [SSL Inspection Overview](/docs/SSL_Inspection/main/) | [Troubleshooting](/docs/Troubleshooting/main/)
