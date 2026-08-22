---
title: Active Directory
description: Integrate SafeSquid with Active Directory for seamless user authentication, SSO, and group-based access control.
keywords:
  - active directory SafeSquid
  - AD integration
  - Kerberos SSO proxy
  - LDAP AD authentication
---

# Active Directory Integration

Integrate SafeSquid with Active Directory (AD) to enable centralized user management, group-based access policies, and seamless Single Sign-On (SSO) for domain-joined users.

## Active Directory Integration Workflow

| Step | Task | Goal |
|------|------|------|
| 1 | [Setup AD Integration](/docs/Authentication/Directory_Services/Active_Directory/Setup_Active_Directory_Integration/) | Link SafeSquid with AD and fetch user/group entities. |
| 2 | **Choose Auth Method** | Decide between Simple (prompt) or SSO (transparent) authentication. |
| 3 | [Simple Authentication](/docs/Authentication/Directory_Services/Active_Directory/Simple_Authentication/) | Browser prompts users for AD credentials. |
| 4 | [SSO Authentication](/docs/Authentication/Directory_Services/Active_Directory/SSO_Authentication/) | Transparent authentication for domain-joined users via Kerberos. |

## Which AD authentication method to use?

| Feature | Simple Authentication | SSO Authentication |
|---------|-----------------------|--------------------|
| **User Experience** | Browser login prompt | Transparent (no prompt) |
| **Domain Requirement** | None (works for any device) | Client must be domain-joined |
| **Complexity** | Low (LDAP bind) | Moderate (Kerberos, DNS, Time Sync) |
| **Primary Use Case** | Guest devices, non-domain PCs | Standard corporate workstations |

:::tip Recommendation
Most enterprises use **SSO Authentication** for corporate domain-joined workstations to provide the best user experience, and **Simple Authentication** as a fallback for guest or non-domain devices.
:::

## Verification

After completing the integration:
1. **Fetch Entries:** Verify that AD users and groups appear in the SafeSquid **LDAP Entities** section.
2. **Test Rule:** Create an access rule that requires AD authentication.
3. **Log Check:** Confirm `identity.log` shows the correct AD username in `DOMAIN\user` or UPN format.

## Next steps

- Start with [Setup Active Directory Integration](/docs/Authentication/Directory_Services/Active_Directory/Setup_Active_Directory_Integration/) to establish the initial connection.
- Configure [Access Restriction](/docs/Access_Restriction/main/) to apply policies based on AD groups.
