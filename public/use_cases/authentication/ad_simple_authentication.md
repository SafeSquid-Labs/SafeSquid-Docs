---
title: "Simple Authentication"
description: "Configure Active Directory simple (LDAP) authentication in SafeSquid for browser-prompted user identification."
keywords: ["active directory integration", "ldap authentication SafeSquid", "simple authentication SafeSquid", "ldap configuration", "sso authentication SafeSquid"]
---

# AD Simple Authentication

Simple authentication validates domain users via LDAP bind. When users browse the web, they are prompted by their browser to enter their Active Directory credentials.

## Problem statement

Not every device can participate in Kerberos SSO. Guest devices, non-domain systems, and troubleshooting cases still need directory-backed identity without falling back to anonymous IP-only control.

## When to use Simple Authentication

| Use Simple Auth When | Use SSO (Kerberos) Instead |
| --- | --- |
| Client devices are not joined to the domain | Corporate workstations are domain-joined |
| Fast setup is required (no Kerberos config) | Best user experience (no prompt) is required |
| Troubleshooting authentication issues | Production environment for domain users |

:::note **Prerequisites**

- [Setup Active Directory Integration](/Setup_Active_Directory_Integration) must be completed.
- SafeSquid must be able to fetch LDAP entities (verify in **LDAP Entities** tab).
- DNS and NTP must be healthy, even for prompt-based AD-backed authentication, because directory reachability and environment consistency still matter. :::

## Configure Simple Authentication

1. **Access SafeSquid Interface:** Go to **Application Setup** → **Integrate LDAP**.
2. **Enable Section:** Ensure the **Integrate LDAP** global section is set to **TRUE**.
3. **Configure LDAP Server:**
   - Go to **LDAP Servers** tab.
   - Edit your AD server entry.
   - Ensure **LDAP Bind Method** is set to **SIMPLE** (for browser-prompt authentication).
4. **Save Configuration:** Click the checkmark to save.

![Ensure LDAP Enabled](/images/How_To/Integrate_Active_Directory_For_Simple_Authentication/image4.webp)

## Enable Authentication in Access Rules

1. **Go to Access Restrictions:** **Application Setup** → **Access Restrictions** → **Allow List**.
2. **Edit Rule:** Find the rule matching your client IPs or create a new one.
3. **Configure Auth:**
   - **PAM Authentication:** Set to **TRUE**.
   - **LDAP Profiles:** (Optional) Select specific AD groups if this rule only applies to them. Leave blank for all AD users.
4. **Save Policy:** Click the checkmark to save.

## Operational notes

- Use simple authentication when transparent SSO is not viable for the target device class.
- Keep the prompt-based user experience explicit in rollout planning so support teams know this is expected behavior, not a failure.
- Narrow bypasses carefully, because overbroad bypass weakens user attribution in logs and reports.

## Verification

| Action | Method | Expected Result |
| --- | --- | --- |
| **Browser Test** | Access any website from a client. | A browser login prompt should appear. |
| **Login Test** | Enter valid AD credentials. | Access is granted; the website loads. |
| **Identity Log** | `tail -f /var/log/safesquid/identity.log` | The log shows the authenticated AD username. |
| **Detailed Log** | **Reports** → **Detailed Logs** | Requests are tagged with the directory username and group. |

## Troubleshooting

## Troubleshooting

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| No login prompt | Rule order or IP mismatch | Ensure the authentication rule is above general allow rules; verify client IP matches rule scope. |
| Prompt keeps reappearing | Incorrect AD credentials or Bind DN | Verify user password in AD; ensure the bind account in LDAP integration has read access. |
| Authentication fails | Directory reachability, DNS, or time issue | Verify AD reachability, sync time with AD, and ensure AD FQDN resolution works. |
| Valid users blocked | Group membership issue | Check whether the user is a member of the group specified in **LDAP Profiles**. |

## Source register

| Topic | Status | Source |
| --- | --- | --- |
| Browser prompt \+ AD bind | **Confirmed** | This page |
| Time skew / DNS with AD | **Confirmed** | Troubleshooting, [NTP](/NTP) |

## Next steps

- [Configure SSO Authentication](/AD_SSO_Authentication) for a transparent user experience.
- [Access Restriction](/Access_Restriction) to define policies by AD group.
- [SSL Inspection](/SSL_Inspection) to attribute HTTPS traffic to AD users.