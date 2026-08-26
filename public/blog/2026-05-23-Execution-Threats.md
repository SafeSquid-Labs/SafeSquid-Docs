---
slug: execution-threats
title: 'Execution hides inside encrypted sessions'
description: 'Last-mile malware reassembly and XSS/CSRF injection require inline response inspection at the proxy layer.'
mode: "center"
---

# Execution hides inside encrypted sessions

After access is established, the payload executes inside encrypted sessions — reassembled from individually benign fragments or injected into legitimate HTTP responses.

## Last-mile malware reassembly

Modern malware delivery does not send an executable file over HTTPS. The delivery mechanism sends fragments: a benign-looking image, a JavaScript library, a compressed archive, a PDF. Each fragment passes individually through signature-based scanners — no fragment triggers an alert. The endpoint browser or a script reassembles and detonates the payload. By the time the endpoint security agent detects anomalous process behaviour, the ransomware has already begun encrypting.

Last-mile reassembly is specifically designed to defeat controls that inspect individual objects in isolation. Defeating last-mile reassembly requires inline content reconstruction: reassemble the full payload before delivery, then scan the reconstructed object. Controls that cannot reconstruct content at the proxy layer cannot stop this class of attack.

Ransomware attacks cost enterprises an average of $1.53 million in recovery costs ([Sophos State of Ransomware 2025](https://www.sophos.com/en-us/content/state-of-ransomware), down from $2.73 million in 2024), excluding regulatory penalties and reputational impact. PCI-DSS Requirement 5 and NIST SP 800-53r5 SI-3 require malicious code protection that addresses this delivery pattern.

## XSS and CSRF injection

Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) exploit the trust relationship between a user's browser and a legitimate web application. XSS injects malicious scripts into HTTP responses from a trusted site — the browser executes the malicious payload with full trust because the injected code originates from a domain the user is authenticated to. CSRF tricks the browser into sending authenticated requests to a third-party site using the user's active session.

XSS and CSRF attacks arrive in HTTP responses, not requests. Controls that only inspect outbound requests miss XSS and CSRF attacks entirely. Inline response inspection — examining what the server sends back to the client — is required to detect injected payloads before they reach the browser. This capability is architecturally impossible for controls that operate at the DNS or URL-category layer.

The primary control point for XSS and CSRF is the application server — Content Security Policy headers, SameSite cookie attributes, and input validation. A SWG contributes a secondary control: response-body inspection for injected script patterns, and HTTP response header stripping before the payload reaches the browser. CISA's September 2024 Secure by Design Alert on XSS (AA24-263A) addresses software developers as the primary responsible party, not network gateways. Deploy both controls; do not treat SWG response inspection as a substitute for application-layer hardening.

## Related topics

- [Initial access threats](/blog/2026-05-23-Initial-Access-Threats) — zero-hour phishing and malvertising
- [Command and control threats](/blog/2026-05-23-Command-and-Control-Threats) — APT C2, infostealers, session hijacking, DNS tunneling
- [Zero-Trust Web Security](/blog/2026-05-23-Zero-Trust-Web-Security) — hub and reading path
