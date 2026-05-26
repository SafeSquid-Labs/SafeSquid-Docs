---
title: Authentication
slug: /Authentication
description: Configure user authentication in SafeSquid using BASIC, Network Signature, Directory Services (including Kerberos SSO), PAM, and bypass rules.
keywords:
  - SafeSquid authentication
  - proxy authentication
  - SSO
  - Kerberos
---

# Authentication

## Problems addressed

Without attributable user or device context, HTTPS and HTTP policy, reporting, and forensics collapse to anonymous IP addresses. Regulators and incident responders expect **who accessed what** when proxies sit in the path.

## Outcomes operators expect

- Directory-backed accounts, SSO, or local credentials for interactive users.
- IP-to-group mapping where login prompts are impossible.
- Controlled bypass for break-glass and non-interactive workloads.
- Identity lines in logs for audit—see verification steps on this page.

## Supported identity backends

Confirmed product knowledge supports these identity integrations:

- Active Directory
- LDAP
- Kerberos

Roadmap items that should **not** be documented as current product capabilities:

- RADIUS
- SAML

## Advantages vs “proxy without identity”

SafeSquid ties **Authentication** rules to the same policy engine as URL, content, and time rules ([Access Restriction](/Access_Restriction)). **MFA:** SafeSquid does not render MFA UI itself; MFA arrives via directory or PAM backends (see note below).

**Comparative authentication feature matrix vs other SWG products:** **Not SSOT-backed in this doc set**—see [What is SafeSquid SWG?](/safesquid_swg/what_is_safesquid_swg#architecture-and-positioning-claims-draft-vs-confirmed).

## Acquire, deploy, use

Pick one primary method from the table below, configure it in the SafeSquid administration UI, then validate `identity.log` and browser behavior per **Verification**.

SafeSquid identifies users through multiple authentication methods to enable identity-based access control and audit trails. Methods can be used individually or in combination to suit enterprise requirements.

:::note
**Multi-factor authentication**
SafeSquid itself does not provide MFA prompts. To enforce MFA, integrate with directory services (Active Directory with MFA-enabled accounts) or use PAM with MFA modules (e.g., Google Authenticator PAM). SafeSquid enforces the authentication decision but delegates credential validation to the backend system.
:::

## Choose your authentication method

| Method | Use When | User Experience | Infrastructure Required |
|--------|----------|-----------------|-------------------------|
| [BASIC Authentication](/BASIC) | No directory service available | Browser login prompt | None |
| [Architecture](/safesquid_swg/architecture/safesquid_swg) | IP-based policy needed (devices, legacy apps) | Transparent (no login) | Static IP addressing or DHCP reservations |
| [Directory Services](/Directory_Services) | Centralized identity required | Browser prompt or SSO | Active Directory or OpenLDAP |
| [PAM Authentication](/PAM) | OS credentials should apply to proxy | Browser login prompt | PAM-capable OS |
| [Bypass Authentication](/Bypass_Authentication) | Some apps cannot authenticate | Transparent for bypassed apps | None |

## Authentication methods

### [BASIC Authentication](/BASIC)
BASIC authentication (RFC 7617) with credentials stored locally in SafeSquid. Browser-prompt authentication with no directory infrastructure required; credentials managed locally. Use when you need identity-based policies without Active Directory or LDAP.

### [IP-based recognition in architecture](/safesquid_swg/architecture/safesquid_swg)
Maps source IPs or subnets to user-groups for group-based access restriction and reporting. No user login required; policy applies by IP. Use when user identity is unavailable (device-only, legacy apps) but you need group-based rules.

### [Directory Services](/Directory_Services)
Integrates with Active Directory or OpenLDAP to leverage existing user accounts and group memberships. Supports simple authentication and Kerberos-based SSO where configured. Use when you need centralized identity management and don't want to duplicate user accounts in SafeSquid.

### [PAM Authentication](/PAM)
Validates proxy users via the system PAM stack so OS and proxy share credentials. Use when you want a single credential set for both OS login and proxy access in PAM-based environments (Linux, Unix).

### [Bypass Authentication](/Bypass_Authentication)
Allows specific destinations or request types to skip authentication while other traffic remains authenticated. Use for automatic updates or apps that cannot send proxy credentials.

## Combining authentication methods

SafeSquid evaluates authentication rules in the order they appear in the policy. The first matching rule applies (no fall-through). Common combinations:

- **Directory + Bypass:** AD/LDAP for users, bypass for OS updates and app sync
- **Network Signature + Directory:** IP-based groups for IoT/devices, AD for user workstations
- **PAM + Bypass:** OS credentials for interactive users, bypass for service accounts

:::tip
Apply authentication rules from most specific to most general. Place narrow bypass rules before broader authentication requirements.
:::

## Production considerations

- Authentication is not only for access control. It is also required for meaningful reporting, audit evidence, and incident investigation.
- Kerberos and other directory-based methods depend on reliable time synchronization. If NTP is unhealthy, authentication can fail even when the proxy path is otherwise correct.
- Bypass rules should be kept narrow. Overbroad bypass weakens attribution and creates false confidence in reporting.

## Verification

After configuring authentication:

1. **Test login flow:** Browse through the proxy from a client; confirm authentication prompt appears (or SSO succeeds)
2. **Check identity logs:** Verify `/var/log/safesquid/identity.log` shows authenticated usernames for proxied requests
3. **Test bypass (if configured):** Confirm bypassed destinations work without prompts
4. **Check reporting impact:** Confirm the authenticated user identity appears in the reporting path and detailed logs

## Troubleshooting

**Symptom:** Users browse, but logs show anonymous IPs.  
**Likely cause:** Authentication is not actually applied to the tested path, or bypass rules are matching first.  
**Isolation:** Compare the request against the authentication rule order and identity logs.  
**Remediation:** Reorder or narrow the rules.  
**Retest:** Repeat the same request and confirm the user identity appears.

**Symptom:** Kerberos or SSO fails unexpectedly.  
**Likely cause:** Directory integration, time synchronization, or client trust assumptions are wrong.  
**Isolation:** Check directory reachability, NTP health, and the exact client path.  
**Remediation:** Restore time sync and correct the AD or Kerberos integration settings.  
**Retest:** Repeat the SSO flow and confirm silent or expected authentication behavior.

**Symptom:** Some applications fail only after authentication is enabled.  
**Likely cause:** The application cannot handle proxy authentication.  
**Isolation:** Test the same application with and without a narrow bypass rule.  
**Remediation:** Add a tightly scoped bypass for that application path if justified.  
**Retest:** Confirm the application works without weakening broad user attribution.

## Source register

| Topic | Status | Source |
| ----- | ------ | ------ |
| BASIC, Network Signature, Directory, PAM, Bypass flows | **Confirmed** | Linked method pages in this section |
| MFA via directory / PAM (not SafeSquid UI) | **Confirmed** | Note on this page |
| First-match rule order | **Confirmed** | **Combining authentication methods** above |
| SAML as a first-class auth mode in UI | **Not current** | Internal knowledge marks SAML as roadmap, not shipping capability |

## Next steps

1. Choose an authentication method above and configure it
2. Combine with [Access Restriction](/Access_Restriction) for identity-based policies
3. Enable [SSL Inspection](/SSL_Inspection) to decrypt HTTPS traffic — without it, SafeSquid can only authenticate based on CONNECT requests, not actual HTTPS content
