---
title: Integrated DNS Security
description: Integrated DNS Security in SafeSquid — DNSBL, homograph detection, query accounting, GeoIP-aware controls, and DNS tunnelling risk reduction.
keywords:
  - Secure Web Gateway Components
  - Integrated DNS Security
  - DNSBL Service
  - DNS threat protection
  - DNS tunneling
  - homograph detection
  - GeoIP
---

# Integrated DNS Security

## Problem statement

DNS is often the first successful step in phishing, malware delivery, command-and-control, and covert exfiltration. If malicious or deceptive resolution succeeds, the organisation pays for the connection attempt even when a later HTTP policy might still block the session. In tunnelling scenarios, DNS itself becomes the covert channel.

## Client scenario

Use Integrated DNS Security when the organisation needs more than simple name resolution:

- early blocking of known-malicious destinations
- protection against DNS tunnelling behavior
- controls for homograph and look-alike domain risk
- DNS visibility that supports investigation and policy design
- geographic restrictions on resolution targets where required

## Key benefits

- Stops some malicious activity before full web sessions begin
- Reduces wasted TCP and TLS setup for destinations that should never be reached
- Adds DNS-specific context to Layer 7 policy rather than replacing it
- Improves evidence for investigations involving tunnelling, phishing domains, or suspicious resolution patterns

## Prerequisites

Before you rely on DNS controls, define:

- whether SafeSquid is in the active DNS resolution path
- which upstream DNS dependencies are allowed
- whether DNSBL and related lookups are reachable from the deployment
- which internal domains and applications must never be disrupted by DNS policy

## Setup instructions

Integrated DNS Security combines several DNS-aware controls:

### DNSBL service

SafeSquid can query DNSBL services before allowing resolution of suspicious names or destinations. If the queried target is flagged as blacklisted, SafeSquid blocks access before the web session proceeds.

### Homograph detection

Homograph detection is relevant when attackers use look-alike domains that visually resemble trusted brands or business applications.

### DNS query accounting

Query accounting matters for investigations because it helps teams identify unusual volumes, suspicious patterns, and tunnelling-like behavior.

### GeoIP detection

GeoIP-aware DNS controls help when policy requires different treatment based on the destination country or region.

### DNS tunnelling protection

SafeSquid's documented threat model includes DNS tunnelling through CNAME or TXT query abuse for ransomware, remote-access tooling, and data exfiltration. DNS security is important because HTTP-layer controls do not see this path.

## Verification and validation

After configuration, test all of the following:

- a known-malicious or test-blacklisted destination is blocked
- a sanctioned business destination still resolves normally
- homograph or suspicious-resolution rules trigger where expected
- query-accounting logs show the events needed for investigation

Useful evidence includes:

- DNS-related event logs
- query records for the blocked test destination
- comparison of successful and blocked lookups
- proof that internal business domains are unaffected

## Troubleshooting guide

**Symptom:** Legitimate domains stop resolving.  
**Likely cause:** Overbroad DNSBL or policy scope, or upstream DNS dependency failure.  
**Isolation:** Compare blocked domains against the policy intent and verify upstream resolver health.  
**Remediation:** Narrow the rule or restore the upstream DNS path.  
**Retest:** Resolve a sanctioned destination and confirm success.

**Symptom:** Malicious test domains still resolve.  
**Likely cause:** SafeSquid is not in the effective DNS path, or the DNSBL dependency is unreachable.  
**Isolation:** Verify the actual resolver path and test DNSBL reachability.  
**Remediation:** Correct the DNS flow or allowlist the required external dependency.  
**Retest:** Repeat the same blocked-domain test and confirm prevention.

**Symptom:** DNS tunnelling indicators are not visible in logs.  
**Likely cause:** Query accounting or the relevant DNS logging path is not enabled or retained.  
**Isolation:** Review DNS logging configuration and retention behavior.  
**Remediation:** Enable the required DNS evidence path.  
**Retest:** Run a controlled test and confirm the event appears.

## Related controls / next steps

- [DNS Security](/DNS_Security) for the configuration guide
- [Access Restriction](/Access_Restriction) for Layer 7 policy aligned to DNS decisions
- [SafeSquid SWG Overview](/safesquid_swg/architecture/safesquid_swg) for the architecture context
- [Deployment Planning](/Deployment_Planning) for DNS dependency and allowlist planning
