---
title: Activate Your License
description: Upload your activation key to SafeSquid and verify license activation.
keywords:
  - SafeSquid license activation
  - SafeSquid activation key
  - SafeSquid licensing
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Activate Your License

An unactivated SafeSquid instance operates with limited features. Activation ties your key to this instance and unlocks your chosen tier (Free or Commercial), enabling full update feeds and commercial features where applicable.

## Key Benefits

- **Unlock commercial features** - threat intelligence, URL categorization database, 365-day DR backup, and email support (see table below).
- **Receive updates** - subscription and malware definition feeds require successful activation.
- **Prove licensing for audits** - activation status is visible in the SafeSquid interface for compliance evidence.

SafeSquid offers two licensing tiers:

|  | Free | Commercial |
| -- | :--: | :--: |
| Core proxy and filtering | ✅ | ✅ |
| SSL inspection | ✅ | ✅ |
| Custom policies and profiles | ✅ | ✅ |
| Real-time threat intelligence | ❌ | ✅ |
| URL categorization database | ❌ | ✅ |
| DR backup (365 days) | ❌ | ✅ |
| Email support | ❌ | ✅ |

The free license has no time limit. You can upgrade to commercial at any time through the [Self-Service Portal](https://key.safesquid.com).



## Readiness Checklist

Your SafeSquid server needs outbound access to these endpoints. Ensure your firewall allows the traffic.

**Required for activation**

| Host              | Port | Purpose            |
| ----------------- | ---- | ------------------ |
| api.safesquid.net | 443  | License activation |

**Required for ongoing updates** *(not needed for initial activation)*

| Host                      | Port | Purpose                           |
| ------------------------- | ---- | --------------------------------- |
| swgupdates2.safesquid.net | 443  | Subscription, malware definitions |
| swgupdates.safesquid.net  | 80   | Seqrite updates                   |
| sslupdates.safesquid.com  | 443  | SSL certificate updates           |
| category.safesquid.net    | 443  | Category DB updates               |
| download.quickheal.com    | 80   | Virus signature updates           |

**URL Categorization Engines** *(commercial license)*

| Host                     | Port | Path                                 |
| ------------------------ | ---- | ------------------------------------ |
| prourl.itsecure.co.in    | 8080 | /URLCategorizerService/URLCategorize |
| encurl.itsecure.co.in    | 8080 | /URLCategorizerService/URLCategorize |
| klassify.itsecure.co.in  | 8080 | /URLCategorizerService/URLCategorize |
| prourl.itonlinesecure.in | 8080 | /URLCategorizerService/URLCategorize |
| encurl.itonlinesecure.in | 8080 | /URLCategorizerService/URLCategorize |



## Activation Steps

1. **Configure the browser** to use SafeSquid as the HTTP proxy (SafeSquid IP, port 8080). See [Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/) if the browser is not yet configured.

2. **Open the SafeSquid interface** by navigating to [http://safesquid.cfg/](http://safesquid.cfg/) in your browser (an embedded Rest UI interface built into SafeSquid; accessible only when your client uses the proxy, but NOT resolved by SafeSquid's DNS resolver).

   When accessing for the first time, the interface prompts for upload of the activation key.

   ![Upload activation key prompt](/img/License_Activation/image13.webp)
   *Initial activation prompt in the SafeSquid interface*

3. **Select the activation key file** and click **Upload**.

   ![Select and upload key](/img/License_Activation/image14.webp)
   *Key upload dialog*

4. **Click Restart** to apply the license.

   ![Restart SafeSquid](/img/License_Activation/image15.webp)
   *Apply changes and restart notice*

5. **Verify activation.** After the page reloads, go to **Support** in the menu.

   ![Support menu](/img/License_Activation/image17.webp)
   *Support and diagnostics menu*

6. **Confirm activation details.** Ensure the **Activation Details** section shows your product type, expiry (if applicable), and subscription status.

   ![Activation details](/img/License_Activation/image18.webp)
   *Subscription and activation status display*

:::tip Proxy Cluster Sync
To synchronize SSL certificates and configuration across a proxy cluster, upload the same activation key on every SafeSquid instance.
:::

:::note Verification
After activation and restart, **Support** → **Activation Details** shows your product type, status, and expiry. Use this screen for compliance evidence that the gateway is correctly licensed.
:::

## Troubleshooting

<Tabs>
  <TabItem value="case1" label="Key Not Detected" default>

**Symptom:** After uploading, the interface shows "Failed to set Subscription details."

**Cause:** The activation key file is missing or misnamed.

**Fix:**

1. Verify the key file exists:

   ```bash
   ls -lrt /usr/local/safesquid/security/
   ```

   Look for a file named `activation_key`.

2. If missing, re-upload the key through the interface.

3. Restart SafeSquid:

   ```bash
   /etc/init.d/safesquid stop
   /etc/init.d/safesquid start
   ```

  </TabItem>

  <TabItem value="case2" label="Server Unreachable">

**Symptom:** After uploading the key, the browser shows "proxy server refusing connections."

**Cause:** SafeSquid cannot reach the subscription server.

**Fix:**

1. Test connectivity:

   ```bash
   ping swgupdates2.safesquid.net
   nslookup swgupdates2.safesquid.net
   ```

2. If DNS or connectivity fails, check firewall rules against the endpoint tables above.

3. Restart after fixing:

   ```bash
   /etc/init.d/safesquid start
   ```

  </TabItem>

  <TabItem value="case3" label="Service Not Restarted">

**Symptom:** Subscription details remain empty after uploading the key, or the browser shows the proxy is refusing connections.

**Cause:** SafeSquid was not restarted after the key upload.

**Fix:**

1. If Monit is configured, it should restart SafeSquid automatically. Otherwise, restart manually:

   ```bash
   /etc/init.d/safesquid stop
   /etc/init.d/safesquid start
   ```

  </TabItem>
  <TabItem value="case4" label="License Expired">

**Symptom:** SafeSquid displays "subscription expired" banner in the interface.

**Cause:** Commercial subscription has expired. Free licenses do not expire.

**What happens after expiration:**

- Core proxy and filtering continues to work
- Security update frequency reduces to free-tier schedule:
  - Anti-virus engine: weekly
  - Web categorization: weekly  
  - SSL security updates: weekly
  - Application/content signatures: monthly
- Commercial features (real-time threat intel, DR backup, email support) become unavailable

**Solutions:**

**Option 1: Renew Subscription**

1. Visit [key.safesquid.com](https://key.safesquid.com) and sign in
2. Go to **Manage Account** → **Renew Subscription**
3. After payment, download the updated activation key
4. Upload the new key in SafeSquid interface (same steps as initial activation)

**Option 2: Extend Conservation Period (3-day grace period)**

If you need time before renewing:

1. Visit [key.safesquid.com](https://key.safesquid.com) and sign in
2. Go to **Manage Account**  
3. Click **Extend Conservation Period** (adds 3 days to your subscription)  
4. The "expired" banner will disappear during the conservation period
5. Restart SafeSquid from the web interface for changes to take effect

![Extend Conservation Period](/img/License_Activation/image23.webp)  
*Extend Conservation Period button in the Self-Service Portal*

:::note Conservation Period Limits
The conservation period can be extended multiple times, each extension adding 3 days. However, this is a temporary measure — renew your subscription for continued commercial feature access.
:::

  </TabItem>

  <TabItem value="case5" label="Wrong License Tier">

**Symptom:** Activation succeeds but commercial features (URL categorization, threat intel) don't work.

**Cause:** Free license uploaded instead of commercial, or key expired.

**Fix:**

1. Check **Activation Details** in the SafeSquid interface:
   - **Product Type** should show "Commercial" if you purchased a commercial license
   - **Expiry** should be in the future

2. If showing Free or expired:
   - Download the correct key from the [Self-Service Portal](https://key.safesquid.com)
   - Re-upload following the steps above

3. Contact support if you purchased commercial but still see Free tier.

  </TabItem>
</Tabs>

## Next steps

1. [Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/) - configure at least one browser or client to use the proxy.
2. [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/) - run smoke tests to confirm the proxy is receiving traffic.
