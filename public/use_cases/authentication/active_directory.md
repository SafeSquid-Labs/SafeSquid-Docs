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

## Problem statement

Large Windows environments need proxy policy and reporting tied to Active Directory identities and groups. Without that linkage, audit evidence degrades into IP addresses and generic browsing records.

## Active Directory Integration Workflow

| Step | Task | Goal |
|------|------|------|
| 1 | [Setup AD Integration](/Setup_Active_Directory_Integration) | Link SafeSquid with AD and fetch user/group entities. |
| 2 | **Choose Auth Method** | Decide between Simple (prompt) or SSO (transparent) authentication. |
| 3 | [Simple Authentication](/AD_Simple_Authentication) | Browser prompts users for AD credentials. |
| 4 | [SSO Authentication](/AD_SSO_Authentication) | Transparent authentication for domain-joined users via Kerberos. |

## Which AD authentication method to use?

| Feature | Simple Authentication | SSO Authentication |
|---------|-----------------------|--------------------|
| **User Experience** | Browser login prompt | Transparent (no prompt) |
| **Domain Requirement** | None (works for any device) | Client must be domain-joined |
| **Complexity** | Low (LDAP bind) | Moderate (Kerberos, DNS, Time Sync) |
| **Primary Use Case** | Guest devices, non-domain PCs | Standard corporate workstations |

:::tip
**Recommendation**
Most enterprises use **SSO Authentication** for corporate domain-joined workstations to provide the best user experience, and **Simple Authentication** as a fallback for guest or non-domain devices.
:::

## Critical dependencies

Active Directory integration depends on:

- directory reachability
- correct DNS
- correct time synchronization for Kerberos
- correct client assumptions for domain-joined and non-domain devices

If DNS or NTP is wrong, AD authentication can fail even when the proxy itself is healthy.

## Verification

After completing the integration:
1. **Fetch Entries:** Verify that AD users and groups appear in the SafeSquid **LDAP Entities** section.
2. **Test Rule:** Create an access rule that requires AD authentication.
3. **Log Check:** Confirm `identity.log` shows the correct AD username in `DOMAIN\user` or UPN format.

## Troubleshooting

**Symptom:** Domain users still see browser prompts.  
**Likely cause:** Kerberos SSO prerequisites are not satisfied, or the device is not eligible for transparent auth.  
**Isolation:** Check DNS, NTP, and domain-join assumptions.  
**Remediation:** Fix the dependency or use the simple-auth path for that device class.  
**Retest:** Retry the same flow and confirm transparent or expected authentication behavior.

**Symptom:** Users authenticate but group-based policy does not apply.  
**Likely cause:** Group retrieval or rule mapping is incomplete.  
**Isolation:** Confirm group visibility in SafeSquid and compare rule matching.  
**Remediation:** Refresh directory entities and correct the rule scope.  
**Retest:** Compare users from different AD groups against the same policy target.

## Source register

| Topic | Status | Source |
| ----- | ------ | ------ |
| Setup → Simple → SSO flow | **Confirmed** | Linked task pages in this hub |
| Kerberos / time sync prerequisites | **Confirmed** | [SSO Authentication](/AD_SSO_Authentication), [NTP](/NTP) |
| RODC path | **Confirmed** | [Kerberos with RODC](/Configure_Kerberos_Authentication_With_RODC) |

## Next steps

- Start with [Setup Active Directory Integration](/Setup_Active_Directory_Integration) to establish the initial connection.
- Configure [Access Restriction](/Access_Restriction) to apply policies based on AD groups.
