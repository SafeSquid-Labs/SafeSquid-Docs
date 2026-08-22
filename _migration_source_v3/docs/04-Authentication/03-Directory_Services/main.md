---
title: Directory Services
description: Integrate SafeSquid with Active Directory or OpenLDAP for centralized user authentication and group-based access control.
keywords:
  - SafeSquid directory services
  - LDAP integration
  - Active Directory proxy
  - OpenLDAP proxy
---

# Centralized Identity and Group-Based Policy

SafeSquid integrates with directory services to provide centralized user authentication and group-based access control. This ensures that web access policies are tied to enterprise identities and group memberships.

## Supported Directory Services

| Directory Service | Integration Type | Key Features |
|-------------------|------------------|--------------|
| [Active Directory](/docs/Authentication/Directory_Services/Active_Directory/main/) | Kerberos SSO / LDAP | Seamless SSO for domain users, group sync |
| [OpenLDAP](/docs/Authentication/Directory_Services/OpenLDAP/main/) | Simple LDAP | Centralized identity for Linux/Unix environments |

## Why use Directory Services?

- **Centralized Management:** Manage users and groups in one place (AD/LDAP) instead of locally in SafeSquid.
- **Group-Based Policies:** Apply different access rules automatically based on directory group membership (e.g., Finance, IT, Sales).
- **Single Sign-On (SSO):** (Active Directory only) Authenticate users transparently using Kerberos tickets without browser prompts.
- **Granular Audit:** Access logs show exactly which directory user accessed which resource, simplifying compliance reporting.

## Choose your integration method

### [Active Directory (AD)](/docs/Authentication/Directory_Services/Active_Directory/main/)
Best for Windows-centric environments. Supports **SSO Authentication** for the best user experience and **Simple Authentication** for non-domain devices or specific use cases.

### [OpenLDAP](/docs/Authentication/Directory_Services/OpenLDAP/main/)
Best for Linux/Unix-heavy environments or organizations using OpenLDAP for identity. Supports **Simple Authentication** (LDAP bind) to validate credentials against the directory.

## Next steps

1. Choose your directory service above.
2. Follow the **Setup Integration** guide to link SafeSquid with your directory.
3. Configure **Simple** or **SSO** authentication rules.
4. Combine with [Access Restriction](/docs/Access_Restriction/main/) to enforce policies by directory group.
