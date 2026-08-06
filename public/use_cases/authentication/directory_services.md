---
title: "Directory Services"
description: "Integrate SafeSquid with Active Directory or OpenLDAP for centralized user authentication and group-based access control."
keywords: ["SafeSquid directory services", "LDAP integration", "Active Directory proxy", "OpenLDAP proxy"]
---

# Centralized Identity and Group-Based Policy

SafeSquid integrates with directory services to provide centralized user authentication and group-based access control. This ensures that web access policies are tied to enterprise identities and group memberships.

## Problem statement

IP-based proxy control is not enough for enterprise governance. Administrators need directory-backed user and group identity so policy, reporting, and investigations reflect the real actor behind the request.

## Supported Directory Services

| Directory Service | Integration Type | Key Features |
| --- | --- | --- |
| [Active Directory](/Active_Directory) | Kerberos SSO / LDAP | Seamless SSO for domain users, group sync |
| [OpenLDAP](/OpenLDAP) | Simple LDAP | Centralized identity for Linux/Unix environments |

Confirmed directory-related product capabilities today:

- Active Directory
- LDAP
- Kerberos

Do not document these as current shipping directory capabilities:

- SAML
- RADIUS

## Why use Directory Services?

- **Centralized Management:** Manage users and groups in one place (AD/LDAP) instead of locally in SafeSquid.
- **Group-Based Policies:** Apply different access rules automatically based on directory group membership (e.g., Finance, IT, Sales).
- **Single Sign-On (SSO):** (Active Directory only) Authenticate users transparently using Kerberos tickets without browser prompts.
- **Granular Audit:** Access logs show exactly which directory user accessed which resource, simplifying compliance reporting.

## Operational requirements

- Reliable DNS and NTP are required for stable directory-backed authentication.
- Kerberos is the documented transparent path for Active Directory environments.
- If transparent authentication is not viable, use prompt-based authentication and keep the user-experience trade-off explicit.

## Choose your integration method

### [Active Directory (AD)](/Active_Directory)

Best for Windows-centric environments. Supports **SSO Authentication** for the best user experience and **Simple Authentication** for non-domain devices or specific use cases.

### [OpenLDAP](/OpenLDAP)

Best for Linux/Unix-heavy environments or organizations using OpenLDAP for identity. Supports **Simple Authentication** (LDAP bind) to validate credentials against the directory.

## Verification and validation

After integration, confirm:

- users and groups are visible in the SafeSquid directory view
- authentication succeeds with a known test account
- group-based policies differentiate users as expected
- logs and reports show directory-backed identity instead of anonymous IP-only attribution

## Source register

| Topic | Status | Source |
| --- | --- | --- |
| AD: SSO \+ Simple paths | **Confirmed** | [Active Directory hub](/Active_Directory) |
| OpenLDAP: Simple LDAP integration | **Confirmed** | [OpenLDAP hub](/OpenLDAP) |
| Group-based policy linkage | **Confirmed** | [Access Restriction](/Access_Restriction) |

## Next steps

1. Choose your directory service above.
2. Follow the **Setup Integration** guide to link SafeSquid with your directory.
3. Configure **Simple** or **SSO** authentication rules.
4. Combine with [Access Restriction](/Access_Restriction) to enforce policies by directory group.