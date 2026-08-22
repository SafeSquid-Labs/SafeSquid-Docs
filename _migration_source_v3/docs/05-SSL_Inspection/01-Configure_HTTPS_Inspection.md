---
title: Configure HTTPS Inspection
description: Prerequisites, certificate generation, enabling SSL inspection, client certificate import, bypass rules, and verification for SafeSquid HTTPS inspection.
keywords:
  - configure SSL inspection SafeSquid
  - HTTPS inspection setup
  - SafeSquid certificate generation
  - bypass SSL inspection
  - Firefox certificate import
---

# Configure HTTPS Inspection

This guide covers the complete HTTPS inspection setup: generate or import a Root CA certificate, enable inspection in SafeSquid, deploy the certificate to clients, and configure bypass rules for sensitive domains.

**Time to complete:** 30-60 minutes (including client certificate deployment)

## Prerequisites

:::info Before You Start

**SafeSquid side:**
- SafeSquid installed and licensed
- Access to [Self-Service Portal](https://key.safesquid.com) (for certificate generation)
- Access to SafeSquid Configuration Portal (`http://safesquid.cfg/`—embedded Rest UI interface built into SafeSquid; accessible only when your client uses the proxy, but NOT resolved by SafeSquid's DNS resolver—or `https://SERVER-IP:8443/` for direct access)

**Client side:**
- List of domains to bypass (banking, healthcare, SSL-pinned apps)
- Method to deploy Root CA to all clients (GPO, MDM, or manual)
- Administrative access to client systems (for certificate import)

:::

---

## Step 1: Generate or Import Root CA Certificate

You have three options for the Root CA certificate:

| **Option** | **When to Use** | **Pros** | **Cons** |
|------------|-----------------|----------|----------|
| **Self-Signed** | Testing, small deployments | Quick, no external dependencies | Not trusted by default, harder to revoke |
| **Enterprise CA (with passphrase)** | Production with existing CA | Centralized trust, auditable | Requires CA infrastructure |
| **Enterprise CA (without passphrase)** | Production, new passphrase | Same as above | Need to set new passphrase |

**Recommended:** Use self-signed for testing/pilot. Use enterprise CA for production.

---

### Generate Certificate in Self-Service Portal

1. **Log in** to the [Self-Service Portal](https://key.safesquid.com/)

   ![Self-Service Portal login](/img/SSL_Inspection/image1.webp)

2. **Navigate to Certificate Management**

   In the dashboard → find your deployment → click **Manage Certificate**

   ![Manage Certificate button](/img/SSL_Inspection/image2.webp)

---

### Option A: Self-Signed Certificate

3. **Click Generate** (appears if no certificate exists yet)

   ![Generate button](/img/SSL_Inspection/image3.webp)

4. **Select "General self-signed"** → **Enter passphrase** → **Generate**

   :::caution Save Your Passphrase
   
   The passphrase is **non-recoverable**. Save it securely—you'll need it to reuse the certificate with different activation keys.
   
   :::

   ![Generate self-signed certificate](/img/SSL_Inspection/image4.webp)

5. **Click Close** to continue

   ![Certificate generated](/img/SSL_Inspection/image5.webp)

---

### Option B: Enterprise CA with Existing Passphrase

3. **Click Regenerate** → **Upload enterprise CA files** → **Select "has passphrase"**

   ![Upload enterprise CA with passphrase](/img/SSL_Inspection/image6.webp)

4. **Select CA certificate files** (`.crt` and `.key`)

   ![Select CA files](/img/SSL_Inspection/image7.webp)

5. **Enter passphrase** → **Click "Validate private key"**

   ![Enter passphrase](/img/SSL_Inspection/image8.webp)

6. **Select "Retain password"** → **Upload**

   ![Retain password and upload](/img/SSL_Inspection/image9.webp)

7. **Click Close**

   ![Upload complete](/img/SSL_Inspection/image10.webp)

---

### Option C: Enterprise CA Without Passphrase (Set New One)

3. **Click Regenerate** → **Upload enterprise CA** → **Select "does not have passphrase"**

   ![Upload enterprise CA without passphrase](/img/SSL_Inspection/image11.webp)

4. **Select CA certificate files**

   ![Select CA files](/img/SSL_Inspection/image12.webp)

5. **Enter new passphrase** → **Upload**

   :::caution Save Your Passphrase
   
   This new passphrase is **non-recoverable**. Save it securely.
   
   :::

   ![Enter new passphrase](/img/SSL_Inspection/image13.webp)

6. **Click Close**

   ![Upload complete](/img/SSL_Inspection/image14.webp)

---

### Download Certificate

7. **Enter passphrase** (if prompted) → **Click Download**

   ![Download certificate](/img/SSL_Inspection/image15.webp)
   ![Certificate download](/img/SSL_Inspection/image16.webp)

**Save this file** — you'll deploy it to all client systems.

---

## Step 2: Enable HTTPS Inspection in SafeSquid

### Access Configuration Portal

1. **Open SafeSquid interface** → **Click "Configure"**

   ![Click Configure](/img/SSL_Inspection/image17.webp)

2. **Expand "Real Time Content Security"** in the sidebar

   ![Real Time Content Security](/img/SSL_Inspection/image18.webp)

3. **Click "HTTPS Inspection"**

   ![HTTPS Inspection](/img/SSL_Inspection/image19.webp)

---

### Enable Global HTTPS Inspection

4. **Click the "Global" tab** → **Click Edit** (pencil icon)

   :::note Version Change
   
   SafeSquid versions after June 2017 have three tabs: **Global**, **Inspection Policies**, and **Bypass Policies**.
   
   :::

   ![Global tab](/img/SSL_Inspection/image20.webp)
   ![Click Edit](/img/SSL_Inspection/image21.webp)

5. **Set "Enabled" to "True"** → **Save Policy**

   ![Enable HTTPS Inspection](/img/SSL_Inspection/image22.webp)
   ![Save Policy](/img/SSL_Inspection/image23.webp)

---

### Enable Inspection Policies

6. **Click "Inspection Policies" tab**

   ![Inspection Policies tab](/img/SSL_Inspection/image24.webp)

7. **Verify default policies are enabled**

   ![Default policies](/img/SSL_Inspection/image25.webp)

8. **Find "Enforce SSL scanning for all websites"** → **Click Edit**

   ![Edit enforce policy](/img/SSL_Inspection/image26.webp)

9. **Set "Enabled" to "True"** → **Save Policy**

   ![Enable enforce policy](/img/SSL_Inspection/image27.webp)
   ![Save Policy](/img/SSL_Inspection/image28.webp)

---

### Save Configuration

10. **Click "Save Configuration"** (floppy disk icon, bottom left)

    ![Save Configuration](/img/SSL_Inspection/image29.webp)

11. **Select "No"** (unless deploying to a cluster) → **Submit**

    :::tip Cloud Config
    
    Select "Yes" only if:
    - You're deploying the same config to multiple SafeSquid instances (cluster)
    - All sections are fully configured for production
    
    Otherwise, select "No" to save locally only.
    
    :::

---

## Step 3: Deploy Root CA to Clients

All clients must trust the SafeSquid Root CA to avoid certificate warnings.

### Windows (Chrome, Edge, IE)

**See detailed guide:** [Import Certificate into Chrome/IE](/docs/SSL_Inspection/Import_Certificate_Chrome_IE/)

**Quick summary:**
1. Double-click the downloaded certificate
2. **Install Certificate** → **Local Machine** → **Next**
3. **Browse** → **Trusted Root Certification Authorities** → **OK**
4. **Next** → **Finish**

**For enterprise deployment:** Use GPO to push the certificate to all Windows machines.

---

### Firefox (All Platforms)

Firefox uses its own certificate store.

1. **Download the SafeSquid Root CA** (from Step 1)
2. **Open Firefox** → **Settings** → **Privacy & Security** → **Certificates** → **View Certificates**
3. **Authorities tab** → **Import**
4. **Select the SafeSquid certificate file**
5. **Check "Trust this CA to identify websites"** → **OK**

**Verify:**
- Visit `https://www.google.com` (via SafeSquid proxy)
- Click padlock → **More information** → **View Certificate**
- Certificate chain should show SafeSquid Root CA

---

### macOS

**Via System Keychain:**
1. Double-click the certificate file
2. **Add** → Enter admin password
3. **Open Keychain Access** → **System** keychain
4. Find SafeSquid certificate → **Get Info**
5. **Trust** section → **When using this certificate** → **Always Trust**

**For enterprise:** Use MDM (Jamf, Intune) to deploy to all Macs.

---

### Mobile Devices

**iOS/Android:**
- Deploy via MDM (Jamf, Intune, Workspace ONE)
- Manual: Email certificate → Open on device → Install

---

## Step 4: Configure Bypass Policies

Bypass HTTPS inspection for:
- Banking and financial sites (compliance)
- Healthcare portals (HIPAA)
- SSL-pinned applications (will break otherwise)
- Government sites

---

### Enable Default Bypass Policy

1. **Click "Configure"** in SafeSquid interface

   ![Click Configure](/img/SSL_Inspection/image30.webp)

2. **Click Search** (magnifying glass icon, top right)

   ![Click Search](/img/SSL_Inspection/image31.webp)

3. **Type "BYPASS SSL INSPECTION"** → **Enter**

   ![Search bypass](/img/SSL_Inspection/image32.webp)

4. **Click Edit** on the bypass policy

   ![Edit bypass policy](/img/SSL_Inspection/image33.webp)

5. **Set "Enabled" to "True"** → **Save Policy**

   ![Enable bypass](/img/SSL_Inspection/image34.webp)
   ![Save bypass policy](/img/SSL_Inspection/image35.webp)

6. **Review and enable related bypass policies** (for banking apps, Windows Update, etc.)

   ![Review bypass policies](/img/SSL_Inspection/image36.webp)

---

### Create Custom Bypass for Specific Domains

**Example:** Bypass HTTPS inspection for Dropbox.

![Custom bypass example](/img/SSL_Inspection/image37.webp)

**Step 1: Define Request Type**

1. **Sidebar** → **Profiling Engine** → **Request Types** → **Add New**

   ![Request Types](/img/SSL_Inspection/image38.webp)
   ![Add New](/img/SSL_Inspection/image39.webp)

2. **Comment:** "Dropbox domains"  
   **Match pattern:** `.*dropbox.*`  
   **Smart TLD:** True

   ![Define Dropbox pattern](/img/SSL_Inspection/image40.webp)
   ![Enable Smart TLD](/img/SSL_Inspection/image41.webp)

**Step 2: Create Access Policy**

3. **Sidebar** → **Access Policies** → **Access Profiles** → **Add New**

   ![Access Profiles](/img/SSL_Inspection/image42.webp)

4. **Comment:** "Bypass SSL for Dropbox"  
   **Request Type:** Select "Dropbox domains" (from Step 1)  
   **Added profiles:** Select "BYPASS SSL INSPECTION"

   ![Create bypass policy](/img/SSL_Inspection/image43.webp)

5. **Save Policy**

   ![Save bypass](/img/SSL_Inspection/image44.webp)

6. **Save Configuration** (floppy disk icon, bottom left)

**Test:** Upload/download files via Dropbox to verify bypass works.

---

## Verification

### Test HTTPS Inspection is Working

**On a client with SafeSquid Root CA installed:**

1. **Browse to** `https://www.google.com`
2. **Click padlock** → **Certificate** → **View**
3. **Verify:** Certificate chain shows SafeSquid Root CA as the issuer
4. **No certificate warnings** should appear

**Expected certificate chain:**
```
www.google.com (issued by SafeSquid Root CA)
  └─ SafeSquid Root CA (self-signed or your enterprise CA)
```

---

### Test Bypass is Working

**On the same client:**

1. **Browse to a bypassed site** (e.g., banking site you added to bypass)
2. **Click padlock** → **Certificate** → **View**
3. **Verify:** Certificate shows the **original site's CA** (not SafeSquid)

**Expected:** Bypassed sites show their original certificates (e.g., DigiCert, Let's Encrypt).

---

### Check SafeSquid Logs

**On SafeSquid server:**

```bash
tail -f /var/log/safesquid/access/extended.log
```

**Expected for inspected sites:**
- Full URL logged (including path, not just domain)
- `200 OK` or similar HTTP status

**Expected for bypassed sites:**
- Only `CONNECT` method logged
- No detailed path information

---

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| Certificate warnings on all HTTPS sites | Root CA not installed on client | Install SafeSquid Root CA in Trusted Root store (see Step 3) |
| Firefox shows warnings, Chrome works | Firefox uses separate cert store | Import certificate into Firefox separately (see above) |
| Banking/healthcare sites broken | HTTPS inspection enabled, no bypass | Add sites to bypass policy (Step 4) |
| Mobile apps not working | SSL pinning | Add app's domains to bypass policy |
| "NET::ERR_CERT_AUTHORITY_INVALID" | Root CA not trusted | Verify certificate installed in **Trusted Root Certification Authorities** (not Intermediate) |
| Inspection works, then stops | SafeSquid restart cleared config | Re-save configuration; check if config was saved to cloud |
| Some sites work, others don't | Partial bypass or incorrect policy | Review bypass policies; check logs for CONNECT vs full requests |

**Still not working?**

1. **Verify HTTPS Inspection is enabled:**
   - Configuration Portal → Real-time Content Security → HTTPS Inspection → Global = True

2. **Check certificate is deployed:**
   - Windows: Run `certmgr.msc` → Trusted Root Certification Authorities → Certificates
   - Firefox: Settings → Privacy & Security → Certificates → View Certificates → Authorities
   - macOS: Keychain Access → System → Find SafeSquid cert

3. **Test with curl:**
   ```bash
   # Should work without cert if bypass is correct:
   curl --proxy http://SAFESQUID-IP:8080 https://www.google.com
   ```

4. **Check SafeSquid logs:**
   ```bash
   tail -50 /var/log/safesquid/safesquid.log
   grep -i "ssl\|cert\|handshake" /var/log/safesquid/safesquid.log
   ```

---

## Next Steps

1. **[Authentication](/docs/Authentication/main/)** — Enable user-aware policies (SSL Inspection must be working first)
2. **[Access Restriction](/docs/Access_Restriction/main/)** — Configure URL filtering (now works on HTTPS)
3. **[Data Leakage Prevention](/docs/Data_Leakage_Prevention/main/)** — Scan HTTPS uploads for sensitive data
4. **[Troubleshooting](/docs/Troubleshooting/main/)** — SSL-specific issues and diagnostics

**Related:**
- [Self-Service Portal](/docs/SafeSquid_SWG/Self-Service_Portal/) — Manage certificates
- [Import Certificate into Chrome/IE](/docs/SSL_Inspection/Import_Certificate_Chrome_IE/) — Detailed Windows guide
