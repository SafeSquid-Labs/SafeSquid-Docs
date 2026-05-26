---
title: Elevated Privacy
description: Use SafeSquid Elevated Privacy to block third-party cookies, suppress referrer data, and reduce user-agent exposure with profile-aware deployment.
keywords:
  - elevated privacy
  - third-party cookies blocking
  - block third-party tracking
  - referrer header removal
  - anonymize user agent
  - SafeSquid privacy policy
  - enforce privacy profiles
  - hide referrer and user-agent
  - privacy levels SafeSquid
  - paranoid privacy mode
---

# Reduce tracking without breaking everything

## Problem statement

Many websites and third-party services track user behavior through cookies, referrer headers, and user-agent details. That exposure can weaken privacy posture and increase unnecessary data disclosure, but aggressive privacy controls can also break federated login, embedded services, and browser-specific web behavior if rolled out carelessly.

## Client scenario

Use Elevated Privacy when you need to:

- block third-party cookies
- reduce referral leakage to external sites
- reduce browser fingerprint exposure
- apply stronger privacy controls to selected users or traffic profiles

## Key benefits

Elevated Privacy gives SafeSquid a graduated privacy model instead of a single all-or-nothing switch. That lets administrators tighten privacy where it matters while still allowing business exceptions where SSO, third-party identity providers, or application compatibility require them.

## Prerequisites

### Client-side preparations

- Identify the user groups, applications, and websites that depend on third-party sign-in or third-party cookies.
- Choose pilot users first before broad rollout.

### SafeSquid-side setup

- Confirm the Elevated Privacy section is available and enabled only when you are ready to test it.
- Decide which profiles need strict privacy and which need a bypass.

## Setup instructions

### Enable the global section

Set the Elevated Privacy global **Enabled** field to `TRUE`.

![Elevated Privacy restriction profile or configuration](/images/Configure/Restriction_Profiles/Elevated_Privacy/image1.webp)

Without the global switch, policy entries do not take effect.

### Create privacy policies in top-down order

Elevated Privacy entries are evaluated from top to bottom, so place narrow exceptions above broad privacy rules when a business workflow must stay functional.

![Elevated Privacy policy or profile options](/images/Configure/Restriction_Profiles/Elevated_Privacy/image2.webp)

### Choose the privacy level deliberately

Available privacy levels are:

- `NOT_REQUIRED`: disable Elevated Privacy for matching traffic
- `LOW`: block third-party cookies only
- `STANDARD`: block third-party cookies and hide HTTP and HTTPS referrer information
- `PARANOID`: block third-party cookies, hide referrer information, and hide different user agents

Use `PARANOID` carefully. Some websites and applications depend on user-agent behavior and can malfunction when that signal is suppressed or normalized.

### Build a strict privacy rule where it is appropriate

For high-privacy use cases, create a rule that applies a stronger privacy level to a dedicated profile.

The existing example remains useful:

- remove third-party cookies
- hide referrer data
- modify user-agent exposure

That helps reduce online tracking but can also break sign-in paths that depend on third-party cookies.

![Elevated Privacy rule or entry configuration](/images/Configure/Restriction_Profiles/Elevated_Privacy/image3.webp)

### Create a bypass for known business exceptions

Some sites require third-party identity providers for login. In those cases, create a bypass profile rather than weakening privacy globally.

The existing example remains valid: connections tagged with a bypass profile can skip Elevated Privacy where third-party authentication is required.

![Elevated Privacy save or apply configuration](/images/Configure/Restriction_Profiles/Elevated_Privacy/image4.webp)

## Verification and validation

### Positive tests

Test a site where privacy controls should apply.

Expected result:

- third-party cookies are blocked at the selected privacy level
- referrer exposure is reduced when using `STANDARD` or `PARANOID`
- the privacy policy applies only to the intended users or profiles

### Negative tests

Test a site that relies on federated or third-party login.

Expected result:

- the site fails when strong privacy is enforced, if it genuinely depends on third-party cookies
- the site works again when the intended bypass profile is applied

That negative test is important because it proves both the restriction and the exception path.

## Troubleshooting guide

### Users cannot sign in to sites that use external identity providers

Likely causes:

- third-party cookies are being blocked
- the wrong privacy level is applied
- the bypass profile is missing or placed too low in rule order

Isolation steps:

- identify whether the site uses third-party SSO
- inspect which privacy rule actually applied
- test the same site with and without the bypass profile

Remediation:

- add or correct the bypass profile
- move the exception above the broad rule
- retest the login flow

### Websites behave differently or render incorrectly

Likely causes:

- `PARANOID` mode is suppressing user-agent behavior needed by the site
- referrer suppression changes the application flow

Isolation steps:

- compare behavior under `STANDARD` and `PARANOID`
- identify whether user-agent-dependent content is involved

Remediation:

- reduce the privacy level for that workflow
- scope `PARANOID` mode to only the users or sites that truly need it

## Related controls / next steps

- Use [Access Restriction](/Access_Restriction) and [Request Profiles](/Request_Profiles) to scope privacy controls more precisely.
- Use [Security Logs](/Security_Logs) and privacy-related records to validate that the right policy path applied.
