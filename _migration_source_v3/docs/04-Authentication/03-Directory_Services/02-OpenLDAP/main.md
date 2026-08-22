---
title: OpenLDAP
description: Integrate SafeSquid with OpenLDAP for centralized user authentication and group-based access control in Linux/Unix environments.
keywords:
  - openldap integration
  - SafeSquid ldap setup
  - ldap authentication
  - linux directory integration
---

# OpenLDAP Integration

Integrate SafeSquid with OpenLDAP to enable centralized user identification and group-based access control for Linux/Unix-centric environments.

## Integration Workflow

| Step | Task | Goal |
|------|------|------|
| 1 | [Simple Authentication](/docs/Authentication/Directory_Services/OpenLDAP/Simple_Authentication/) | Configure LDAP server connection and enable browser-prompt authentication. |
| 2 | [SSO Authentication](/docs/Authentication/Directory_Services/OpenLDAP/SSO_Authentication/) | Enable transparent authentication for LDAP users via Access Restrictions. |

## Why use OpenLDAP with SafeSquid?

- **Centralized Identity:** Use your existing OpenLDAP directory for proxy authentication.
- **Group-Based Access:** Categorize users into groups (e.g., `developers`, `marketing`) and apply different filtering rules.
- **Linux Compatibility:** Ideal for environments that don't use Active Directory but require identity-based security.
- **Audit Trails:** Identity logs attribute all web activity to specific LDAP usernames.

## Verification

After configuring OpenLDAP:
1. **Fetch Entries:** Confirm that LDAP users and groups are listed in the **LDAP Entities** section of the SafeSquid interface.
2. **Log Check:** Verify successful LDAP binds in `/var/log/safesquid/safesquid.log`.
3. **Policy Test:** Ensure that a rule restricted to an LDAP group correctly allows members and blocks others.

## Next steps

- [Configure Simple Authentication](/docs/Authentication/Directory_Services/OpenLDAP/Simple_Authentication/) to establish the connection.
- [Configure SSO Authentication](/docs/Authentication/Directory_Services/OpenLDAP/SSO_Authentication/) to enable user-aware policies.
- [Access Restriction](/docs/Access_Restriction/main/) to define what your LDAP groups can access.
