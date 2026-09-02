---
title: Self-Service Portal
description: SafeSquid Self-Service Portal — cloud-managed activation, licensing, backup, categorization, certificate, and related operational workflows for SafeSquid deployments.
keywords:
  - SafeSquid Self-Service Portal
  - Manage SafeSquid activation key
  - SafeSquid custom web categorization
  - SafeSquid SSL certificate management
  - SafeSquid Web Security Client VPN
  - SafeSquid confidential data signatures
---

# Self-Service Portal

The Self-Service Portal is a SafeSquid-managed cloud service at `https://key.safesquid.com`. It is part of the product operating model, not just a convenience website. It handles activation-key distribution and other cloud-managed workflows that influence licensing, categorization, backup, and certificate-related operations.

**Access:** [https://key.safesquid.com](https://key.safesquid.com)

## Problem statement

If licensing, categorization, backup, or certificate workflows are scattered across email threads and manual files, deployments become fragile and support-dependent. Teams need a controlled place to retrieve activation material, manage cloud-linked settings, and align multiple installations to the same organizational context.

## Client scenario

Use the portal when you need to:

- register and obtain activation keys
- manage licensing and subscription state
- support SSL certificate workflows
- manage custom categorization or cloud-linked policy data
- understand cloud dependencies in restricted or sovereignty-sensitive deployments

## Key benefits

- Reduces dependence on manual support for routine licensing tasks
- Centralizes cloud-linked deployment metadata by activation key
- Supports repeatable rollout across multiple SafeSquid instances
- Makes cloud dependency explicit so teams can design around it where needed

## What the portal is used for

Internal product knowledge confirms the portal is used for:

1. **Activation key distribution**  
   Obtain and re-download the activation key used to bind a deployment to SafeSquid licensing workflows.

2. **License management**  
   Track subscription and activation status for SafeSquid instances.

3. **Custom categorization and related cloud-managed settings**  
   Support organization-specific categorization workflows tied to the activation context.

4. **Certificate-related workflows**  
   Support SSL inspection deployment workflows that depend on trusted certificate handling.

5. **Configuration and policy synchronization functions**  
   The knowledge base identifies the Self-Service Portal as part of the cloud path for licensing, activation-key distribution, threat-intelligence delivery, and policy or configuration synchronization across deployments.

6. **Backup and restore support**  
   The broader architecture model places configuration backup and restore as a peer operational service in the SafeSquid ecosystem.

---

## Prerequisites

<Note>
**Before you start**

- SafeSquid account (see [Register and get your key](/getting_started/register) if you haven't registered yet)
- Use your business/corporate email for enterprise benefits
- Have your SafeSquid installation details ready (for license activation)
</Note>

---

## Access the portal

**Direct link:** [https://key.safesquid.com](https://key.safesquid.com)

**From SafeSquid.com:**
1. Visit [https://www.safesquid.com](https://www.safesquid.com)
2. Click **Self-Service Portal** in the top menu
3. Login with your registered email and password

<Tip>
**First-time users:** if you haven't created an account yet, see [Register and get your key](/getting_started/register) for registration steps.
</Tip>

---

## Common tasks

### Download Activation Key

1. **Log in** to the portal
2. **Navigate to** Activation Keys
3. **Click Download Key**
4. Save the `activation_key` file (do not rename it)

**Use this key for:** [License activation](/getting_started/activate) during SafeSquid setup, or
upload under [Subscription](/admin_guide/infrastructure_and_access/subscription) when renewing —
status then shows on the [Support](/admin_guide/infrastructure_and_access/support) page's License
Details panel.

---

### Support SSL certificate workflows

Use the portal to support certificate workflows required for SSL inspection deployment. Certificate generation, retrieval, or related management must be paired with endpoint trust deployment and SafeSquid-side SSL inspection configuration.

**Details:** [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection)

---

### Configure custom categories

1. **Log in** to the portal
2. **Navigate to** Custom Web Categorization
3. **Add URLs** to custom categories (e.g., "Internal Tools", "Approved Cloud Apps")
4. **Save** — changes apply to all SafeSquid instances using your activation key

**Use for:** Categorizing internal or organization-specific sites for access policies.

---

### View subscription status

1. **Log in** to the portal
2. **Navigate to** Subscription
3. **View:**
   - Product type (Free or Commercial)
   - Expiry date (if commercial)
   - Subscription tier and features

## Verification and validation

After using the portal, verify all of the following:

- the activation key is accepted by the SafeSquid deployment
- the expected license or subscription state appears on the instance
- custom categorization or related cloud-managed changes appear after sync
- SSL-related assets required for inspection workflows are available where expected

## Troubleshooting

| **Issue** | **Likely Cause** | **Fix** |
|-----------|------------------|---------|
| Cannot login | Wrong credentials or account not activated | Reset password; check email for activation link |
| Activation key download fails | Browser cache or session expired | Clear cache, logout/login, try different browser |
| SSL-related workflow fails | Missing organization details or incomplete certificate workflow | Verify the portal state and then complete the SafeSquid-side SSL steps |
| Custom categories not applying | The instance is not synced to the correct activation context | Recheck the activation key and synchronization path |
| Cloud-linked features do not update | Restricted network path blocks portal or feed communication | Allowlist the required SafeSquid cloud dependencies |

## Related controls / next steps

- [Register and get your key](/getting_started/register) to establish the activation path
- [Activate your license](/getting_started/activate) to bind the deployment to the key
- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) for certificate-dependent HTTPS inspection workflows
- [Threat Intelligence Feeds](/safesquid_swg/application_ecosystem/threat_intelligence_feeds) for cloud-delivered intelligence dependencies
- [Support](/admin_guide/infrastructure_and_access/support) for the on-appliance License Details view and Cloud Restore
