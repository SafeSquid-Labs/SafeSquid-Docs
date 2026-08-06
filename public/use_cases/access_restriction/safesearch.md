---
title: "Enforce SafeSearch"
description: "Enforce SafeSearch on Google, Yahoo, and Bing through SafeSquid so users cannot disable search-result filtering locally."
keywords: ["enforce safesearch SafeSquid", "google safesearch SafeSquid", "yahoo safesearch SafeSquid", "bing safesearch SafeSquid", "filter explicit content SafeSquid"]
---

# Keep search filtering enforced at the proxy

## Problem statement

Search engines can expose explicit or otherwise inappropriate results even when the destination itself is not blocked. Relying on users to keep SafeSearch enabled is not operationally safe because the setting can be changed locally in a few clicks.

## Client scenario

Use this control when you need to:

- enforce safer search results for schools, shared terminals, or supervised user groups
- prevent users from disabling SafeSearch locally
- keep search-result filtering active on major search engines without depending on endpoint settings

## Key benefits

SafeSquid can enforce SafeSearch centrally for supported search engines so the proxy, not the user, controls the setting. That reduces policy drift and makes acceptable-use enforcement easier to maintain across many devices.

## Prerequisites

### Client-side preparations

- Ensure client search traffic passes through SafeSquid.
- If search traffic uses HTTPS, deploy the SafeSquid Root CA to relevant clients.

### SafeSquid-side setup

- Enable [SSL Inspection](/SSL_Inspection) because major search engines use HTTPS.
- Confirm the default SafeSearch-related rules are present in the existing SafeSquid policy set.

## Setup instructions

### Enable HTTPS visibility first

SafeSearch enforcement on encrypted search traffic depends on HTTPS inspection. If SafeSquid cannot inspect the search request, it cannot override the user preference safely.

### Enable the SafeSearch policies

SafeSquid includes default rules to enforce SafeSearch for:

- Google
- Yahoo
- Bing

Enable the relevant SafeSearch policies in the policy and profile sections if they are currently disabled.

### Use proxy enforcement instead of browser trust

Do not rely on browser-side settings alone. Users can disable SafeSearch in the search engine or browser interface, but proxy-enforced rules keep the safer setting active regardless of local preference.

### Understand the Google behavior

Google SafeSearch enforcement works by ensuring the safe-search parameter remains active in the request path. The existing SafeSquid rules handle that centrally, which is why HTTPS inspection and correct policy application both matter.

## Verification and validation

### Positive tests

For each supported search engine:

1. perform a test query that would normally surface explicit results
2. confirm the search engine returns filtered results
3. try disabling SafeSearch in the user interface and repeat the test

Expected result:

- filtered mode remains enforced
- user-side changes do not override the proxy decision

### Negative tests

Use a normal business or educational search query.

Expected result:

- ordinary search remains usable
- enforcement does not break general search functionality

## Troubleshooting guide

### Users can still disable SafeSearch

Likely causes:

- HTTPS inspection is not enabled
- the SafeSearch policy exists but is disabled
- the traffic is bypassing the expected inspection path

Isolation steps:

- confirm the search session is decrypted
- confirm the SafeSearch policy is enabled
- verify the request passes through the intended SafeSquid policy path

Remediation:

- enable or restore HTTPS inspection
- enable the SafeSearch rules
- retest with the same search engine

### Search works, but filtered results do not appear consistently

Likely causes:

- only part of the search traffic is being inspected
- a bypass rule or exception path affects the search engine traffic

Isolation steps:

- test from the same client repeatedly
- compare working and non-working requests in logs
- review request profiles or bypass conditions that may affect search domains

Remediation:

- remove or narrow the conflicting bypass
- ensure the search engine traffic follows one consistent policy path

## Related controls / next steps

- Use [SSL Inspection](/SSL_Inspection) for the HTTPS visibility required by this control.
- Use [Web Categorization](/Web_Categorization) and [Access Restriction](/Access_Restriction) when search-result filtering must sit alongside broader destination controls.