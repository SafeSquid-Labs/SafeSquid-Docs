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

## Portal layout

Confirmed live (2026-09-02, logged-in session, all six tabs inspected): **Manage Key**
(default landing tab — key details, instance list, Download Key), **Manage Categories** (Check
Website Category / Modify Category, single-URL search), **Manage Certificates** (Generate then
Download an SSL certificate for the key), **Manage VPN** (C-code/activation key against a URL
field, Set URL), **Manage Signatures** ("Available Signatures for [C-code]", Add New, a
Keywords/Signature table), **Manage Account** (subscription details, Conserve Subscription). A
standing **Download Key** action and **Download latest ISO** / **Download latest tarball** links
(`downloads.safesquid.com/appliance/safesquid.iso` and `.../binary/safesquid_latest.tar.gz`)
appear on every tab.

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

1. **Log in** to the portal — lands on the **Manage Key** tab by default.
2. **Click Download Key**.
3. Save the `activation_key` file (do not rename it).

The Manage Key tab also lists your key's C-Code, current usage counters, Support Validity date,
and instance details (Service ID, version, last update) — plus **Download latest ISO** and
**Download latest tarball** links for the install media itself.

**Use this key for:** [License activation](/getting_started/activate) during SafeSquid setup, or
upload under [Subscription](/admin_guide/infrastructure_and_access/subscription) when renewing —
status then shows on the [Support](/admin_guide/infrastructure_and_access/support) page's License
Details panel.

---

### Generate and download your SSL certificate

1. **Log in** to the portal.
2. **Open the Manage Certificates tab** — shows your C-code and Key Name against a **Generate**
   action.
3. Click **Generate**, then **Download** the resulting certificate.

Certificate retrieval here must still be paired with endpoint trust deployment and SafeSquid-side
SSL inspection configuration — this step alone doesn't complete an HTTPS Inspection rollout.

**Details:** [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection)

---

### Manage confidential-data signatures

1. **Log in** to the portal.
2. **Open the Manage Signatures tab** — shows "Available Signatures for [C-code]" and an **Add
   New** action, with a Keywords/Signature table (empty until you add one).
3. **Add New** opens an "Editing Signature for [C-code]" form: a **Signature name** field and a
   **Keywords** field (one keyword per line, with live regex detection — the form flags whether
   what you typed reads as a regex pattern). **Submit** to save.

{/* NEEDS-SME-REVIEW: the Add New form's two fields (Signature name, Keywords) and its regex-detection behavior are confirmed live. How and when a saved signature here actually syncs to the appliance's DLP OCR keyword scoring (dlp.mdx's "Enabled OCR rows are walked... each keyword regex match adds Weight") was not tested — this page states the two are related, not that sync was observed. */}

**Use for:** feeding custom keyword-based signatures into
[DLP](/admin_guide/real_time_content_security/dlp) OCR scoring on the appliance.

---

### Check or modify a website's category

1. **Log in** to the portal.
2. **Open the Manage Categories tab** — a **Check Website Category** / **Modify Category**
   toggle.
3. **Check Website Category** takes a URL (protocol selector plus a `www.example.com`-style text
   box) and a **Search** button — looks up how that URL is currently categorized.
4. **Modify Category** instead opens with a **Select Category** field (dropdown/autocomplete over
   existing categories, not a URL search) — pick a category to act on.

{/* NEEDS-SME-REVIEW: confirmed live — Check Website Category is single-URL search; Modify Category starts from an existing-category picker instead, which does imply named categories exist here (unlike an earlier pass through this page which concluded otherwise). What appears after selecting a category in Modify Category — URL list, add/remove controls, anything else — was not observed; don't describe it further without checking. If bulk custom-category upload also exists separately, it may be the local console's [Categorize Web-Sites](/admin_guide/custom_settings/categorize_web_sites) feature instead — the portal homepage's marketing copy for "Custom Category Management" describes uploading category lists "from SafeSquid User Interface," which points at the appliance, not confirmed as this portal tab. */}

**Use for:** looking up a site's current category, or changing which category an existing
category-set applies to.

---

### Check subscription status and conserve or renew

1. **Log in** to the portal.
2. **Open the Manage Account tab.**
3. **View:** Active Subscription status, Subscription ID, C-Code, Key Name, Plan (for example
   Trial or Commercial), Named Users, No of Instances, and Support Validity date.
4. If you need more time before renewing, use **Conserve Subscription** — see
   [Handle expiry](/deployment/manage_subscription_state) for what this does and does not buy you.

<Warning>
A "Renew Subscription" action was not visible on this tab for a Trial-plan account when last
checked (2026-09-02) — only Conserve Subscription showed. Whether Renew appears for a Commercial
plan, or lives somewhere else, is unconfirmed.
</Warning>

---

### Manage VPN client licensing

1. **Log in** to the portal.
2. **Open the Manage VPN tab.**
3. The tab lists your C-code and activation key against a **URL** field (unset by default —
   shows "Not Defined") with a **Set URL** action.

{/* NEEDS-SME-REVIEW: confirmed live that this tab and its C-code/activation-key/URL/Set URL layout exist, but what the URL is used for once set (a roaming-client gateway address, most likely, given faqs.md's existing "Web Security Clients for Roaming users (VPN)" description) was not confirmed by actually setting one. Don't describe the effect of Set URL beyond what's stated here without testing it. */}

**Use for:** licensing SafeSquid's roaming-user VPN web-security clients against this activation
key. This is also where the "Manage VPN settings" topic once flagged as missing from
[Configuration](/admin_guide/main) actually lives — it isn't a local console feature.

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
- [DLP](/admin_guide/real_time_content_security/dlp) for how Manage Signatures' keyword signatures get scanned
- [Support](/admin_guide/infrastructure_and_access/support) for the on-appliance License Details view and Cloud Restore
