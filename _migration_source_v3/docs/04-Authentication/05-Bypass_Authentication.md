---
title: Bypass Authentication
description: Configure authentication bypass for specific destinations or applications in SafeSquid to allow non-interactive clients to work without prompts.
keywords:
  - bypass authentication SafeSquid
  - SafeSquid proxy authentication bypass
  - bypass proxy authentication dropbox
  - SafeSquid authentication policy
  - allow application without authentication SafeSquid
---

# Bypass Authentication

Bypass rules allow specific destinations (e.g., update servers) or applications (e.g., Dropbox) to skip the authentication requirement. This is critical for automated services and non-interactive clients that cannot send proxy credentials.

## When to use Bypass Authentication

| Use Bypass When | Use Authentication Instead |
|-----------------|-----------------------------|
| Application cannot prompt for credentials | Interactive web browsing (Chrome, Firefox) |
| OS updates (Windows Update, Yum, Apt) | Access to corporate resources |
| Background sync apps (Dropbox, OneDrive) | Sensitive data access |
| Security updates (Antivirus, Malware) | Any flow where user attribution is required |

:::caution Compliance Note
Bypassed traffic is not attributed to a specific user. Keep your bypass list as narrow as possible (FQDNs vs. broad domains) to maintain security and auditability.
:::

## Step 1: Enable Global Bypass

1. **Access Configuration:** Open the [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/).
2. **Enable Section:** Click **Search** → search for **BYPASS AUTHENTICATION**.
3. **Set Enabled:** Edit the policy and set **Enabled** to **TRUE**.

![Enable bypass authentication](/img/How_To/Bypass_Authentication/image5.webp)

## Step 2: Define Bypassed Destinations

1. **Navigate to Request Types:** **Application Setup** → **Request Types**.
2. **Create New Type:** Click **Add New**.
   - **Host:** Enter the domain pattern (e.g., `.*\.dropbox\.com`).
   - **Smart TLD:** Set to **TRUE** if you want to match all subdomains.
3. **Assign Profile:** In **Added Request Type**, give it a name like `BYPASS_LIST`.

## Step 3: Link Bypass to Access Profile

1. **Navigate to Access Profiles:** **Restriction Policies** → **Access Profiles**.
2. **Create Profile:** Click **Add New**.
   - **Request Types:** Add the profile you created (e.g., `BYPASS_LIST`).
   - **Added Profiles:** Assign a name like `AUTHENTICATION_BYPASS`.
3. **Apply to Authentication Rule:** 
   In **Access Restrictions** → **Allow List**, ensure your authentication rule includes this bypass profile in the **Bypass** field.

![Bind request type](/img/How_To/Bypass_Authentication/image13.webp)

## Verification

| Action | Method | Expected Result |
|--------|--------|-----------------|
| **Bypass Test** | Access a bypassed URL (e.g., Dropbox) from a client. | The site/app loads immediately without a login prompt. |
| **Auth Test** | Access a non-bypassed site (e.g., google.com). | A login prompt appears as expected. |
| **Check Logs** | `tail -f /var/log/safesquid/access.log` | Bypassed requests will show no username or a `-` in the identity field. |

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Still prompted for login | Profile not in bypass field | Ensure your `AUTHENTICATION_BYPASS` profile is added to the **Bypass** field of the active Allow List rule. |
| Update service still fails | Missing domains | Check logs for other domains the app uses and add them to your `BYPASS_LIST` request type. |
| Too much traffic bypassed | Pattern too broad | Narrow your host pattern; avoid using `.*` if you can use specific FQDNs. |

## Next steps

- [Local Credential Store (BASIC)](/docs/Authentication/BASIC/)
- [Directory Services](/docs/Authentication/Directory_Services/main/)
- [Access Restriction](/docs/Access_Restriction/main/)
