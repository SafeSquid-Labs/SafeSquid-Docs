---
title: Authentication
description: Find the SafeSquid guides for authentication with local credentials, PAM, Active Directory and OpenLDAP.
keywords:
  - authentication
  - SafeSquid documentation
---

# Set Up Authentication Before Applying Policy

Policy by user or group works only when SafeSquid knows who is browsing.

## Quickstart path

### Choose a method

1. **[Authentication](/use_cases/authentication/authentication)** - configure user authentication in SafeSquid using BASIC, Network Signature, Directory Services (including Kerberos SSO), PAM, and bypass rules.
2. **[Directory Services](/use_cases/authentication/directory_services)** - integrate SafeSquid with Active Directory or OpenLDAP for centralized user authentication and group-based access control.
3. **[User Identification](/use_cases/authentication/user_identities)** - configure user identity recognition methods in SafeSquid including IP-based authentication, directory service integration, and credential management for policy enforcement.
4. **[User Groups](/use_cases/authentication/user_groups)** - configure user groups in SafeSquid for group-based web access policies, enabling differentiated security controls for departments, roles, and teams.

### Integrate Active Directory

5. **[Setup Active Directory Integration](/use_cases/authentication/setup_active_directory_integration)** - link SafeSquid with Active Directory to synchronize users and groups for identity-based web security policies.
6. **[Active Directory](/use_cases/authentication/active_directory)** - integrate SafeSquid with Active Directory for seamless user authentication, SSO, and group-based access control.
7. **[Active Directory Simple Authentication](/use_cases/authentication/ad_simple_authentication)** - configure Active Directory simple (LDAP) authentication in SafeSquid for browser-prompted user identification.
8. **[Active Directory SSO Authentication](/use_cases/authentication/ad_sso_authentication)** - configure Kerberos-based Single Sign-On (SSO) with Active Directory for transparent user authentication in SafeSquid.
9. **[Active Directory SSO With RODC](/use_cases/authentication/configure_kerberos_authentication_with_rodc)** - integrate Active Directory for SSO using Read-Only Domain Controllers (RODC). Includes RWDC preparation, lookup logic, and LDAP configuration.

### Integrate OpenLDAP

10. **[OpenLDAP](/use_cases/authentication/openldap)** - integrate SafeSquid with OpenLDAP for centralized user authentication and group-based access control in Linux/Unix environments.
11. **[OpenLDAP Simple Authentication](/use_cases/authentication/openldap_simple_authentication)** - configure OpenLDAP simple bind authentication in SafeSquid for directory-backed user identification.
12. **[OpenLDAP SSO Authentication](/use_cases/authentication/openldap_sso_authentication)** - enable transparent authentication for OpenLDAP users in SafeSquid using directory profiles and access restrictions.

### Use local and network-based identity

13. **[Local Credential Store](/use_cases/authentication/basic)** - configure SafeSquid for browser-based user authentication without Active Directory using local credential storage.
14. **[PAM Authentication](/use_cases/authentication/pam)** - configure PAM (Pluggable Authentication Modules) integration with SafeSquid for system-level authentication.
15. **[Internal User Authentication](/use_cases/authentication/internal_users)** - authenticate users by assigning usernames and passwords via the SafeSquid interface when no Active Directory is available.
16. **[Network Signature](/use_cases/authentication/network_signature)** - map client IP addresses or ranges to user groups so rules apply by network segment without a user login.
17. **[Bypass Authentication](/use_cases/authentication/bypass_authentication)** - configure tightly scoped authentication bypass in SafeSquid for non-interactive destinations and applications that cannot complete proxy authentication.


## Next steps

- **[Access Restriction](/use_cases/access_restriction/access_restriction)** - build SafeSquid access policies that make web decisions by identity, destination, time, application, and content so enforcement stays precise and auditable.
- **[Audit & Forensics](/use_cases/audit_and_forensics/audit_forensics)** - comprehensive network monitoring, security analysis, and forensic capabilities for enterprise web security management.
