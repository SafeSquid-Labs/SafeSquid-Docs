---
slug: initial-access-threats
title: 'Initial access exploits Layer 7'
description: 'Zero-hour phishing and malvertising drive-by compromise inside HTTPS sessions that perimeter controls cannot inspect.'
---

# Initial access exploits Layer 7

Attackers use Layer-7 traffic to plant the first foothold — exploiting newly registered domains and compromised ad networks inside HTTPS sessions that perimeter controls cannot inspect.

Mapping web threats to the [MITRE ATT&CK](https://attack.mitre.org/) kill chain reveals a consistent pattern: Layer 7 is the attack surface at every phase. Controls that cannot inspect HTTP(S) payloads are blind at every stage, not just one.

## Zero-hour phishing

Phishing kits now deploy on newly registered or typosquatted domains — `paypa1-secure.com`, `microsoft-login-verify.net` — with valid TLS certificates issued minutes before the attack. DNS filters and URL-category engines have no reputation signal for newly registered domains. Signature-based detection has nothing to match against. The targeted user receives a page that is visually identical to a legitimate login form. Credentials are stolen before any threat intelligence database learns the domain exists.

The financial sector, healthcare providers, and government contractors are primary targets. A single stolen credential in a privileged account is the entry point for lateral movement, ransomware deployment, and sustained data exfiltration. NIST SP 800-63B authentication assurance levels and ISO 27001:2022 A.5.15 access controls assume that credential theft is prevented upstream — phishing at scale invalidates that assumption.

AI-generated phishing lures defeat reputation-based and grammar-based detection entirely — the lure contains no typos, no known-bad patterns, and no domain history; content analysis at the TLS-inspection layer is the only reliable detection point.

## Malvertising and drive-by download

An employee visits a legitimate news site, financial portal, or SaaS vendor page. The ad network serving content to that site has been compromised or is hosting a malicious creative. The browser executes injected code or is silently redirected to an exploit kit without any user action beyond page load ([MITRE ATT&CK T1189 — Drive-by Compromise](https://attack.mitre.org/techniques/T1189/)). No click is required. The site itself carries no malicious content. Only the ad-network payload is hostile, and the ad-network payload arrives over HTTPS on the same trusted session the browser opened to the legitimate domain.

Polyglot files — files simultaneously valid as two binary formats, such as a JPEG that is also a valid JavaScript module — bypass format-specific scanners because each scanner evaluates the file through the lens of a single format. The polyglot decoder executes inside the browser after the file passes inspection. Microsoft tracked the Storm-0408 campaign ([Microsoft Security Blog, March 2025](https://www.microsoft.com/en-us/security/blog/2025/03/06/malvertising-campaign-leads-to-info-stealers-hosted-on-github/)), which infected nearly one million devices through malvertising before detection, with distribution reaching enterprise endpoints through ad networks serving major news and entertainment properties.

The SWG control point is HTTP response inspection before the payload reaches the browser. Content Disarm and Reconstruct (CDR) strips active content from delivered files — removing JavaScript embedded in image containers, macro-enabled objects in documents, and injected script elements from HTML responses — before delivery to the requesting endpoint. NIST SP 800-53r5 SC-18 (Mobile Code) requires policy enforcement on mobile code downloaded from external sources. ISO 27001:2022 A.8.23 (Web Filtering — new in the 2022 revision) explicitly mandates protection against malicious web content delivered through browsing. PCI-DSS v4.0 Requirement 6.4.3 (payment page script integrity, mandatory from March 2025) targets injected third-party scripts specifically — a direct match for the malvertising delivery pattern.

## Related topics

- [Legacy enforcement gap](/blog/legacy-enforcement-gap) — why envelope-only controls fail
- [Execution threats](/blog/execution-threats) — last-mile malware reassembly and XSS/CSRF
- [Zero-Trust Web Security](/blog/zero-trust-web-security) — hub and reading path
