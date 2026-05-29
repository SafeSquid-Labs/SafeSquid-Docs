---
title: Remote Browser Isolation
description: Remote Browser Isolation role in the SafeSquid SWG ecosystem for separating risky browsing from trusted enterprise endpoints.
keywords:
  - Remote Browser Isolation
  - RBI
  - browser isolation
  - SafeSquid SWG
---

# Remote Browser Isolation

Remote Browser Isolation (RBI) separates high-risk web activity from the endpoint. Use it when the business must allow access to uncertain or risky sites without giving active web content direct execution access on managed devices.

RBI is part of the application ecosystem because it complements proxy policy. The proxy decides whether a request is allowed, blocked, inspected, or redirected into a safer browsing path. Isolation reduces endpoint exposure when a complete block would interrupt legitimate work.

## Risk and control fit

| Scenario | Proxy-only outcome | RBI-assisted outcome |
| --- | --- | --- |
| Unknown research site | User reaches active content on the endpoint if allowed | Site opens away from the endpoint trust boundary |
| High-risk category with business need | Teams choose between block and exception | Access can be constrained to an isolated session |
| Phishing investigation | Analysts risk endpoint exposure | Analysts review content with reduced local execution risk |

## Use RBI when

- Legal, finance, security, or research teams must inspect unknown sites.
- Executives and privileged users face targeted phishing risk.
- A temporary exception is necessary but direct endpoint rendering is too risky.
- Audit teams need proof that risky access was controlled, not silently allowed.

## Evidence to retain

Pair RBI decisions with proxy and reporting evidence:

- user identity and destination
- policy decision that sent the session to isolation
- time of access and session result
- related block, bypass, or exception record

## Next steps

- Use [Proxy Service](/safesquid_swg/application_ecosystem/proxy_service) to understand the enforcement point.
- Use [Reporting Service](/safesquid_swg/interface/reporting_service) to retain investigation evidence.
