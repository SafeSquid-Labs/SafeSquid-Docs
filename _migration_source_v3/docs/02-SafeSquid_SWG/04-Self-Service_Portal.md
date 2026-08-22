---
title: Self-Service Portal
description: Discover how the SafeSquid Self-Service Portal simplifies centralized management of licenses, custom web categorization, SSL certificates, VPN clients, and DLP signatures across all SafeSquid installations with a unified cloud-based interface.
keywords:
  - SafeSquid Self-Service Portal
  - Manage SafeSquid activation key
  - SafeSquid custom web categorization
  - SafeSquid SSL certificate management
  - SafeSquid Web Security Client VPN
  - SafeSquid confidential data signatures
---

# Self-Service Portal

The Self-Service Portal is a cloud-based interface for managing properties tied to your activation key: licenses, custom web categorization, SSL certificates, subscription details, VPN clients, and DLP signatures.

**Access:** [https://key.safesquid.com](https://key.safesquid.com)

## What You Can Manage

The portal centralizes routine administration tasks:

1. **Activation Keys**  
   Download activation keys for new deployments or re-download if lost.

2. **License Management**  
   View subscription status, product type (Free/Commercial), and expiry dates.

3. **Custom Web Categorization**  
   Add custom URL categories for your organization (e.g., internal tools, approved SaaS apps).

4. **SSL Certificate Management**  
   Generate and manage your enterprise Root CA certificate for SSL inspection. Configure OCSP/CRL settings.

5. **VPN Client Management**  
   Enroll and manage Web Security Client VPN connections.

6. **DLP Signature Management**  
   Configure confidential data signatures for data leakage prevention policies.

7. **Configuration Backup**  
   Cloud-synchronized policy backups with version control for disaster recovery.

---

## Prerequisites

:::info Before You Start

- SafeSquid account (see [Register and Get Your Key](/docs/Getting_Started/Register/) if you haven't registered yet)
- Use your business/corporate email for enterprise benefits
- Have your SafeSquid installation details ready (for license activation)

:::

---

## Access the Portal

**Direct link:** [https://key.safesquid.com](https://key.safesquid.com)

**From SafeSquid.com:**
1. Visit [https://www.safesquid.com](https://www.safesquid.com)
2. Click **Self-Service Portal** in the top menu
3. Login with your registered email and password

:::tip First-Time Users
If you haven't created an account yet, see [Register and Get Your Key](/docs/Getting_Started/Register/) for registration steps.
:::

---

## Common Tasks

### Download Activation Key

1. **Log in** to the portal
2. **Navigate to** Activation Keys
3. **Click Download Key**
4. Save the `activation_key` file (do not rename it)

**Use this key for:** [License activation](/docs/Getting_Started/Activate/) during SafeSquid setup.

---

### Generate SSL Certificate

1. **Log in** to the portal
2. **Navigate to** SSL Certificates
3. **Generate Root CA** for your organization
4. **Download** the certificate
5. **Deploy** to all endpoints for SSL inspection

**Details:** [SSL Inspection](/docs/SSL_Inspection/main/)

---

### Configure Custom Categories

1. **Log in** to the portal
2. **Navigate to** Custom Web Categorization
3. **Add URLs** to custom categories (e.g., "Internal Tools", "Approved Cloud Apps")
4. **Save** — changes apply to all SafeSquid instances using your activation key

**Use for:** Categorizing internal or organization-specific sites for access policies.

---

### View Subscription Status

1. **Log in** to the portal
2. **Navigate to** Subscription
3. **View:**
   - Product type (Free or Commercial)
   - Expiry date (if commercial)
   - Subscription tier and features

**Upgrade:** Contact SafeSquid support or use the portal upgrade option.

---

## Benefits of Using Business Email

When registering with a corporate email domain (not Gmail, Yahoo, Outlook personal):

- **Priority support** during proof-of-concept
- **Team member invitations** (add colleagues to your organization)
- **Extended trial options** for evaluation
- **Access to enterprise features** and dedicated account management

---

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| Cannot login | Wrong credentials or account not activated | Reset password; check email for activation link |
| Activation key download fails | Browser cache or session expired | Clear cache, logout/login, try different browser |
| SSL certificate generation fails | Invalid organization details | Verify organization name and contact info in portal settings |
| Custom categories not applying | Key not uploaded to SafeSquid | Re-upload activation key in SafeSquid interface |

**Still need help?** Contact SafeSquid support with your registered email address.

---

## Next Steps

1. **[Register and Get Your Key](/docs/Getting_Started/Register/)** — Create your account if you haven't already
2. **[Activate Your License](/docs/Getting_Started/Activate/)** — Upload the key to SafeSquid
3. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Deploy the Root CA for HTTPS inspection
4. **[Custom Categorization](/docs/Profiling_Engine/Web_Categorization/)** — Use custom categories in access policies
