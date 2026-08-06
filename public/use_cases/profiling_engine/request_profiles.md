---
title: "Request Profiles"
description: "Use SafeSquid Request Profiles to classify traffic by method, protocol, host, headers, user agent, and request behavior before applying enforcement policies."
keywords: ["SafeSquid request profiles", "configure request profiles SafeSquid", "user agent filtering", "hostname based profiling SafeSquid", "SafeSquid safe search", "SafeSquid request classification"]
---

# Classify traffic before you enforce it

## Problem statement

Many web controls fail because enforcement is attempted before traffic is classified correctly. If SafeSquid cannot distinguish uploads from downloads, browser traffic from desktop apps, or sanctioned SaaS use from general browsing, access rules become brittle and hard to tune.

## Client scenario

Use Request Profiles when you need to:

- identify requests by host, method, protocol, referrer, user agent, or header patterns
- separate upload paths from read-only browsing paths
- detect application-specific traffic such as desktop clients or SaaS services
- build precise exceptions for SSL bypass, authentication behavior, or access restriction

## Key benefits

Request Profiles create reusable classification signals. Instead of repeating complex matching logic in multiple policies, you define the request behavior once and then consume that profile throughout SafeSquid.

## Prerequisites

### Client-side preparations

- Ensure the target traffic reaches SafeSquid.
- Gather representative request samples before writing production rules.

### SafeSquid-side setup

- Decide which business behaviors you want to classify first, such as uploads, webmail, Teams desktop traffic, or read-only social-media use.
- Plan naming carefully so profiles remain understandable months later.

## Setup instructions

### Enable the Request Profiles section

In **Configure → Custom Settings → Request Types**, set the global **Enabled** field to `TRUE`.

If the section is disabled, none of the profile entries will classify traffic.

### Build rules from specific to broad

Request profile entries are tested in top-down order. Put highly specific application or workflow matches above general host or protocol matches.

This matters because the first matching logic can influence which profiles are added or removed.

### Use tracing when validating

Enable **Trace Entry** during testing for the rule you are tuning.

That gives you a way to verify whether the entry actually matched instead of guessing based on user outcome alone.

### Match only the attributes that matter

Use the minimum set of fields needed for reliable classification:

- **Method** for read, upload, or tunnel behavior
- **Protocol** for HTTP, HTTPS, or FTP context
- **Host Name** and **Smart TLD** for service targeting
- **User Agent** for application-specific traffic
- **Referrer** or header patterns when workflow context matters

Avoid overloading one rule with many weak conditions if one strong condition identifies the traffic more reliably.

### Add and remove profiles intentionally

Use **Added Request profiles** to tag traffic for later enforcement. Use **Removed Request profiles** only when you need to override or clean up an earlier broad match.

## Verification and validation

### Positive tests

Test realistic traffic that should match the rule, such as:

- a desktop app with a known user agent
- a SaaS upload using `POST` or `PUT`
- a specific host that should receive a special profile

Expected result:

- the intended request profile is added
- downstream access or inspection policy consumes that profile correctly
- logs show the expected request classification path

### Negative tests

Test nearby traffic that should not match, such as:

- a different app with a similar host
- normal browsing traffic on the same domain
- GET requests when the profile is intended only for uploads

Expected result:

- SafeSquid does not over-classify unrelated traffic
- exception profiles stay narrow

## Troubleshooting guide

### The expected request profile is never applied

Likely causes:

- the global section is disabled
- a higher rule matches first
- the selected fields do not reflect the actual traffic

Isolation steps:

- confirm the section is enabled
- enable **Trace Entry**
- compare live request headers against the rule conditions

Remediation:

- fix rule order
- refine the matching fields
- retest with captured request samples

### Too many requests receive the same profile

Likely causes:

- the hostname regex is too broad
- Smart TLD is enabled when a strict FQDN match is needed
- a generic user-agent pattern matches many clients

Isolation steps:

- inspect actual matched requests
- compare intended scope with the regex used

Remediation:

- narrow the regex
- disable Smart TLD where precise matching matters
- add another distinguishing field

### Downstream policy still does not behave correctly

Likely causes:

- the request profile is added correctly but never consumed
- another policy removes or overrides the profile later

Isolation steps:

- confirm the profile appears in logs
- inspect later profile-removal logic and downstream access rules

Remediation:

- attach the correct enforcement policy to the profile
- remove the unintended override

## Related controls / next steps

- Use [Access Restriction](/Access_Restriction) to enforce decisions based on these profiles.
- Use [Response Profiles](/Response_Profiles) when the decision depends on server response content rather than request intent.
- Use [Security Logs](/Security_Logs) to verify trace behavior and final profile assignment.