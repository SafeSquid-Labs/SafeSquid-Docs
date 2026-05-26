---
slug: zero-trust-principles
title: 'Zero-Trust requires Layer-7 inspection'
description: 'Five Zero-Trust principles for the web perimeter: least privilege, never trust always verify, adaptive trust, micro-segmentation, and assume breach.'
---

# Zero-Trust requires Layer-7 inspection

Each of the eleven Layer-7 threat patterns in this tab is addressed by the same architectural answer: Layer-7 inspection governed by Zero-Trust principles. Zero-Trust is not a product category but an architectural principle: no user, device, or network connection is implicitly trusted. Every access request must be verified against explicit policy, authorised based on current context, and logged for accountability.

Applied to the web perimeter, Zero-Trust has specific architectural implications. Every DNS and HTTP(S) transaction must be inspected end-to-end — not just the envelope, but the payload. Satisfying "URL categorisation" is not the same as satisfying Zero-Trust web access control. Zero-Trust cannot be satisfied by DNS or URL-category controls alone; DNS-only and URL-category-only solutions leave a structural enforcement gap, leaving HTTP(S) payload content uninspected and the Layer-7 surface uncontrolled.

The policy engine must correlate in real-time: identity, device, client application, network context, content, runtime behaviour, and session state — for every request, every time. Static rules evaluated against envelope attributes are insufficient. The Zero-Trust model requires a dynamic trust assessment that changes as context changes.

Five Zero-Trust principles define what Zero-Trust looks like at the web perimeter.

**Least Privilege Access** — users and devices receive access only to the specific resources required for the current task. "Allow internet access" is not a policy. "Allow this authenticated user, from this managed device, during business hours, to access this category of sites, with uploads blocked" is a policy. Every grant of access is the minimum necessary, and nothing is assumed.

**Never Trust, Always Verify** — no session is trusted by virtue of a prior authenticated connection, a known IP address, or a VPN tunnel. Every request is independently authenticated and authorised against current policy. A user authenticated yesterday is not trusted today without re-verification. A request from a known IP is not trusted without identity confirmation.

**Adaptive Trust Assessment** — trust is not binary. Trust is a score derived from the current context: who is requesting, from where, using what device, at what time, for what resource, with what content. High-risk contexts require higher verification or receive lower access. A request that looks normal in isolation may look anomalous in the context of the requesting user's behavioural baseline.

**Micro-Segmentation** — access is segmented at the application and content level, not just the network level. Different users have different access to different parts of the same web service. A contractor accessing a sanctioned SaaS platform is not granted the same access as a full-time employee. Segmentation is enforced at the content layer.

**Assume Breach** — the architecture assumes that the perimeter has already been compromised. Controls are designed to detect and contain, not just to prevent. Every access is logged, anomalies are surfaced, and the system maintains a complete audit trail that enables forensic investigation after a breach is discovered.

## Related topics

- [Exfiltration threats](/blog/exfiltration-threats) — insider theft, shadow AI, cyberslacking
- [Trust algorithm](/blog/trust-algorithm) — dynamic trust scoring and shared inspection context
- [Adoption criteria](/blog/adoption-criteria) — when to apply Zero-Trust web security
