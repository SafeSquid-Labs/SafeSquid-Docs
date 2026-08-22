---
title: User Identification
slug: /Profiling_Engine/User_Identities
description: Configure user identity recognition methods in SafeSquid including IP-based authentication, directory service integration, and credential management for policy enforcement.
keywords:
  - SafeSquid user identification
  - proxy user authentication
  - IP-based authentication
  - directory service integration
  - Kerberos SSO proxy
  - LDAP authentication proxy
  - network signature authentication
---


# User identity drives policy and reporting



## User identity recognition methods

User identity drives policy enforcement, defines digital boundaries, and governs behavior. SafeSquid enables identity recognition through modular methods tailored to network architecture, trust design, and user mobility. Each method not only shapes access but also impacts the authentication experience.

### [IP-Based Recognition](/docs/Authentication/Network_Signature/)

In static networks, identity begins with IP. SafeSquid maps static IP addresses to users or groups, validating identity by network origin. It requires no prompts, credentials, or interaction---identity is inferred and immediate. Ideal where user-device relationships remain constant.

### [OpenLDAP Integration](/docs/Authentication/Directory_Services/OpenLDAP/main/)

As environments adopt directory services, OpenLDAP introduces structured identity. SafeSquid supports two authentication paths:

- **Kerberos SSO** System login provides identity. No user prompts. SafeSquid reads the Kerberos ticket from the session and authenticates silently. Suitable for managed, domain-aware environments.

- **Simple** Where SSO isn't feasible, SafeSquid prompts for credentials. User input is validated against OpenLDAP. Interaction is explicit, but effective for guest or unmanaged devices.

### [Active Directory Integration](/docs/Authentication/Directory_Services/Active_Directory/main/)

For enterprise environments, Active Directory too offers seamless integration with:

- **Kerberos SSO**
- **Simple**

### Without Directory Services

Where directories are absent, SafeSquid provides internal mechanisms:

- [Credential-Based Authentication](/docs/Authentication/BASIC/) User accounts and encrypted credentials are stored locally. SafeSquid presents a login prompt, validates inputs internally, and applies identity-based policies. Entirely self-contained.

- **PAM Authentication** In Linux-based environments, SafeSquid leverages the Pluggable Authentication Module (PAM) framework for user identification. PAM enables SafeSquid to authenticate users through the host system's authentication stack, which may include system accounts, RADIUS, smartcards, biometric modules, or custom PAM configurations.

### [User Groups](/docs/Profiling_Engine/User_Identities/User_Groups/)
Configure user groups for group-based web access policies. User groups enable differentiated security controls for departments, roles, and teams.

### Multifactor Authentication

For elevated security, SafeSquid combines identity sources. A typical flow begins with IP-based recognition---identifying the device---followed by a credential challenge through AD, OpenLDAP, PAM, or local store. Access is granted only when both factors align, ensuring dual-layer assurance without external token systems.

