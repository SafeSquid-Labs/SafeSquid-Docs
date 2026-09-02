---
slug: trust-algorithm
title: 'Trust is assessed dynamically'
description: 'The Zero-Trust Trust Algorithm evaluates five dimensions per request and requires shared inspection context across the proxy pipeline.'
mode: "center"
---

# Trust is assessed dynamically

Zero-Trust web architecture rejects static-rule-only access decisions; the architecture runs a Trust Algorithm (TA) — a real-time, multi-dimensional evaluation of the current request context. The TA produces a weighted trust score that drives access decisions. A high score permits access. A low score restricts, challenges, or blocks. The score changes with every request as context changes.

Five dimensions feed the Trust Algorithm.

**Environmental Context** evaluates time of access, geographic location, network origin, and access pattern against established baselines. A request at 2 AM from an unfamiliar network location elevates environmental risk, even if the user credentials are valid.

**Device Metrics** assess hardware security state, software integrity indicators, and device health signals. A managed corporate device with up-to-date software is a different trust signal from an unmanaged personal device or a device with disabled endpoint security.

**User Behaviour Analytics (UBA)** compare the current request against the requesting user's established behavioural baseline: typical authentication times, typical access patterns, typical data volumes, typical application set. A user who typically accesses ten internal applications suddenly accessing forty external domains is a behavioural anomaly — even if each individual request appears legitimate.

**Resource Risk** evaluates the target resource: content sensitivity classification, SSL certificate validity and issuance history, domain registration age, compliance status of the destination. A newly registered domain with a 24-hour-old certificate carries higher resource risk than an established enterprise SaaS endpoint.

**Transaction Risk** examines the request and response at the payload level: request anomalies, response content characteristics, volume deviations, business process alignment. A download that exceeds the requesting user's typical volume profile, from a resource category inconsistent with the user's role, with content that matches DLP patterns, scores high on transaction risk regardless of what the URL category says.

The TA evaluates these five dimensions together, assigns a weight to each, and produces a single access decision. The TA is the difference between a static allow/deny rule and a Zero-Trust trust assessment: a static rule evaluates one attribute; the TA evaluates the full context. A contextual TA is especially effective for insider threats and compromised accounts — deviations from the established behavioural baseline reveal threats that no static policy rule can catch.

## Shared inspection context is required

A Trust Algorithm that evaluates five dimensions simultaneously in real time requires the inspection pipeline to share structured contextual state across all inspection stages for every request, without inter-stage latency. The gap introduced by isolated inspection stages is a correctness gap — not a performance gap.

A policy that must fire when "the authenticated user is a contractor AND the content matches a DLP pattern AND the destination is a personal cloud storage service" cannot be enforced if authentication context, content inspection result, and destination classification are produced in separate processes that cannot share state at evaluation time. Passing rich context between isolated inspection stages via inter-process communication (pipes, sockets, or OS-managed shared memory) requires serialisation and deserialisation that degrades both evaluation speed and context fidelity.

Shared-context inspection — where authentication, URL categorisation, content inspection, and UBA evaluation operate against a common request context — is the architectural requirement for granular Zero-Trust enforcement.

## Related posts

- [Zero-Trust requires Layer-7 inspection](/blog/2026-05-23-Zero-Trust-Principles) - five principles for the web perimeter.
- [Command and control blends into HTTPS](/blog/2026-05-23-Command-and-Control-Threats) - behavioural correlation for APT detection.
- [What is SafeSquid SWG](/safesquid_swg/what_is_safesquid_swg) - product implementation of the inspection pipeline.
