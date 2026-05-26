---
slug: legacy-enforcement-gap
title: 'Legacy controls leave a structural enforcement gap'
description: 'Why network firewalls, endpoint security, and DNS-only or URL-category-only controls cannot enforce Layer-7 web policy.'
---

# Legacy controls leave a structural enforcement gap

Three structural gaps explain why legacy solutions fail at the web perimeter.

**Network Layer Firewalls (L3/L4)** operate on IP headers and TCP/UDP ports. Port 443 traffic — which accounts for over 90% of enterprise web traffic — is entirely opaque to network layer firewalls. A state-of-the-art next-generation firewall that cannot perform inline TLS inspection is, for practical purposes, a sophisticated gatekeeper that waves through everything marked "HTTPS." Encrypted malware, encrypted C2 beaconing, encrypted data exfiltration, and legitimate web browsing are indistinguishable at the L3/L4 layer.

**Endpoint Security** operates at the device level — catching known malware signatures, monitoring process behaviour, and enforcing device-local policy. Cross-session patterns are invisible to individual endpoint agents: a single agent has no view of what other endpoints in the environment are doing. Policy sprawl across thousands of managed devices creates inconsistency. Computational overhead competes with workload performance. Critically, threats that never execute code on the endpoint generate no alert: a user manually uploading sensitive files to a personal cloud account bypasses endpoint detection entirely because the browser is functioning exactly as designed.

**DNS-only and URL-category-only controls** are coarse-grained by design — blocking known-bad domains and categorising URLs against a reputation database. Payload inspection is architecturally absent from both control types. Known-bad domain lists and reputation databases fail against newly registered domains with no signal, against legitimate domains repurposed for malicious activity (a compromised CDN, a sanctioned cloud service used for exfiltration), and against DNS tunneling — where the DNS query string itself encodes the covert channel. URL category databases lag threat actors by hours to days; zero-hour attacks specifically exploit this window.

None of these controls is worthless. Each control addresses part of the threat landscape. The problem is treating any single control as sufficient for web security. Zero-Trust Web Security requires inspection at the layer where the threats live.

## Related topics

- [Zero-Trust Web Security](/blog/zero-trust-web-security) — hub and reading path
- [Initial access threats](/blog/initial-access-threats) — zero-hour phishing and malvertising
- [Zero-Trust principles](/blog/zero-trust-principles) — architectural requirements for Layer-7 enforcement
