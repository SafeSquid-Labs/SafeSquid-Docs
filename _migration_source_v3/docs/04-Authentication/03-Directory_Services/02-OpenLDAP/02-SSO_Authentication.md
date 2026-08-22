---
title: SSO Authentication
description: Enable transparent authentication for OpenLDAP users in SafeSquid using directory profiles and access restrictions.
keywords:
  - OpenLDAP integration
  - SSO authentication
  - SafeSquid LDAP setup
  - LDAP configuration
  - SafeSquid authentication
---

# OpenLDAP SSO Authentication

Configure Access Restrictions to utilize OpenLDAP identities. This enables identity-based policies where users are recognized by their directory username and group membership.

:::info Prerequisites
- [OpenLDAP Simple Authentication](/docs/Authentication/Directory_Services/OpenLDAP/Simple_Authentication/) configured and successful.
- LDAP users and groups must be visible in the **LDAP Entities** tab.
:::

## Enable Authentication in Access Rules

1. **Access Restrictions:** Go to **Application Setup** → **Access Restrictions** → **Allow List**.
2. **Edit Rule:** Edit the rule matching your client segment or create a new one.
3. **Apply LDAP Profiles:**
   - **LDAP Profiles:** Select specific LDAP groups (e.g., `IT_Admins`) from the dropdown. 
   - Leave blank to apply this rule to all directory users.
4. **Enable PAM:** Ensure **PAM Authentication** is set to **TRUE**.
5. **Save Policy:** Click the checkmark to save.

![selecting the users or user groups you want to set the authentication for](/img/How_To/Enable_authentication_for_LDAP_users/image11.webp)

:::tip Note on Default Rules
SafeSquid includes default entries under the **Allow List**. You can edit these to quickly map specific LDAP groups to default user-groups like `admins` or `users`.
:::

## Verification

| Action | Method | Expected Result |
|--------|--------|-----------------|
| **Test Access** | Browse from a client belonging to a mapped LDAP group. | Access is allowed/denied according to the rule. |
| **Check Identity Log** | `tail -f /var/log/safesquid/identity.log` | Shows the authenticated OpenLDAP username for each request. |
| **Review Dashboard** | **Reports** → **Detailed Logs** | Verify the **Username** column is populated with directory names. |

![Confirming SSO authentication by seeing the username in SafeSquid detailed logs](/img/How_To/Enable_authentication_for_LDAP_users/image35.webp)

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Authentication prompt appears | No match in LDAP Profiles | Ensure the user is a member of the group specified in the LDAP Profiles field. |
| User recognized but blocked | Policy restriction | Check the access rules applied to the user-group assigned in the Allow List entry. |
| No username in logs | PAM set to FALSE | Ensure **PAM Authentication** is set to **TRUE** in the matching Allow List rule. |

## Next steps

- [Access Restriction](/docs/Access_Restriction/main/) to define policies for your different LDAP groups.
- [SSL Inspection](/docs/SSL_Inspection/main/) to attribute encrypted traffic to specific users.
- [Bypass Authentication](/docs/Authentication/Bypass_Authentication/) for automated services.
