---
slug: adoption-criteria
title: 'When Zero-Trust web security applies'
description: 'Criteria for adopting Layer-7 Zero-Trust web enforcement and next steps toward SafeSquid deployment.'
mode: "center"
---

# When Zero-Trust web security applies

✅ **Zero-Trust Web Security applies when:**

- The organisation processes sensitive data and has compliance obligations under GDPR, HIPAA, PCI-DSS, ISO 27001, or SOC 2 that require demonstrable web access controls and audit evidence
- HTTPS traffic is currently opaque to perimeter controls — the controls cannot see what is inside encrypted sessions
- Identity-aware policy is required: different access for different users, groups, roles, or device states
- Detection and prevention of insider data theft via sanctioned cloud services is required
- The threat model includes APTs, zero-hour phishing, or malware delivered over HTTPS
- A complete, per-user, per-request audit trail suitable for incident investigation and regulatory reporting is required
- Policy enforcement on DNS as a potential covert channel — not just as name resolution infrastructure — is required

❌ **Layer-7 enforcement remains absent when:**

- The organisation relies on DNS filtering alone for web security — DNS inspection does not cover HTTP(S) payload and leaves the Layer-7 surface uncontrolled
- URL category engines are the primary enforcement mechanism — URL category engines cannot inspect content, cannot enforce identity-aware policy, and cannot detect zero-hour domains
- The perimeter firewall performs stateful inspection but not inline TLS decryption — encrypted traffic is opaque regardless of firewall capability below the TLS layer
- Endpoint security is assumed to cover the web perimeter — endpoint agents cannot enforce web policy for unmanaged devices, cannot correlate cross-session behaviour, and cannot inspect network-layer content

## Next steps

- [What is SafeSquid SWG](/safesquid_swg/what_is_safesquid_swg) — how SafeSquid implements Zero-Trust web controls: the inspection pipeline, control model, and compliance evidence SafeSquid produces
- [Prerequisites](/getting_started/install_safesquid/prerequisites) — validate system, network, and identity requirements before deployment
- [Getting Started](/getting_started/welcome) — production onboarding path for deploy, activate, and harden

## Related topics

- [Zero-Trust Web Security](/blog/2026-05-23-Zero-Trust-Web-Security) — hub and reading path
- [Zero-Trust principles](/blog/2026-05-23-Zero-Trust-Principles) — five architectural principles
- [Trust algorithm](/blog/2026-05-23-Trust-Algorithm) — dynamic trust scoring
