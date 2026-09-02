---
slug: command-and-control-threats
title: 'Command and control blends into HTTPS'
description: 'APT C2, infostealer callbacks, session hijacking, and DNS tunneling evade envelope-only perimeter controls.'
mode: "center"
---

# Command and control blends into HTTPS

C2 channels blend into normal HTTPS traffic — periodic beacons disguised as analytics calls, outbound POSTs that match browser telemetry, and DNS query strings encoding covert channels.

## APT C2 and domain fronting

Traffic characteristic of nation-state and sophisticated criminal actors does not announce itself. Such traffic blends with normal browsing: periodic small requests to domains that resemble analytics services, content delivery networks, or software update endpoints. Exfiltration happens over weeks or months, in increments small enough to avoid volumetric anomaly detection. The APT campaign goal is not disruption — the goal is dwell time. The longer the attacker remains undetected, the more data the attacker extracts and the deeper lateral movement penetrates.

Perimeter controls that evaluate each request in isolation cannot detect APTs. APT detection requires behavioural correlation across sessions, users, and time: a specific endpoint has been making unusual requests to a specific domain for three weeks; a specific user's access pattern deviates from the established baseline; a specific combination of request attributes matches known C2 communication patterns. No individual request is suspicious. The pattern is.

APTs are responsible for the most damaging breaches in recent history — state-sponsored campaigns targeting critical infrastructure, defence contractors, and financial institutions. Domain fronting ([MITRE ATT&CK T1090](https://attack.mitre.org/techniques/T1090/)) routes C2 traffic through trusted CDN infrastructure so that the TLS SNI field names a legitimate domain while the HTTP `Host` header directs the request to attacker-controlled infrastructure — a technique that defeats SNI-only filtering. Application-layer protocol abuse ([T1071 — Application Layer Protocol](https://attack.mitre.org/techniques/T1071/); [T1071.001 — Web Protocols](https://attack.mitre.org/techniques/T1071/001/)) embeds C2 channels in normal-looking HTTP requests, and [T1102 — Web Service](https://attack.mitre.org/techniques/T1102/) routes C2 through trusted cloud platforms such as GitHub, Pastebin, or OneDrive. NIST SP 800-53r5 SI-4 (System Monitoring) and ISO 27001:2022 A.8.15 (Logging) address APT detection requirements, but only if the monitoring system has the context to correlate across sessions and can read decrypted HTTP payloads.

## Infostealer C2 callbacks

After an endpoint is compromised by an infostealer — LummaC2, Rhadamanthys, or StrelaStealer ([IBM X-Force Threat Intelligence Index 2025](https://www.ibm.com/thought-leadership/institute-business-value/report/2025-threat-intelligence-index)) — the malware exfiltrates harvested credentials, browser-stored session tokens, saved passwords, and autofill data to attacker-controlled infrastructure over HTTPS ([MITRE ATT&CK T1071.001 — Web Protocols](https://attack.mitre.org/techniques/T1071/001/)). The callback traffic is a standard HTTPS POST on port 443, structurally indistinguishable from normal browser telemetry or form submission at the envelope level.

IBM X-Force reported an 84% increase in emails delivering infostealers in 2024; credential harvesting ranked as the top objective in 28% of incident response cases. The compromised endpoint user is unaware — the infostealer operates silently, the endpoint security agent may not detect the C2 callback because the malware blends with normal HTTPS browser traffic, and the exfiltrated data leaves the network before any account-takeover attempt triggers an identity alert.

The SWG intercepts outbound HTTPS traffic, decrypts the TLS session, inspects the HTTP POST payload for credential patterns, session token structures, and DLP-defined sensitive data patterns (NIST SP 800-53r5 AC-4 — Information Flow Enforcement; SI-3 — Malware Protection), and evaluates the destination domain against threat intelligence feeds — blocking the C2 callback before credentials and tokens leave the network perimeter. ISO 27001:2022 A.8.7 (Protection against malware) and PCI-DSS v4.0 Requirement 5 require controls that address post-compromise exfiltration, not only initial infection prevention.

## Session hijacking

Session hijacking occurs when an attacker steals or replays authentication tokens — session cookies, OAuth tokens, JWT Bearer tokens — to impersonate an authenticated user without knowing that user's credentials ([MITRE ATT&CK T1550.004 — Use Alternate Authentication Material: Web Session Cookie](https://attack.mitre.org/techniques/T1550/004/)). Over HTTPS, session-hijacking traffic is indistinguishable from a legitimate session to any control that cannot inspect the decrypted payload. The attacker reuses the stolen token, the server treats the request as authenticated, and the access logs record the legitimate user's identity.

Without inline TLS inspection and session-level anomaly detection — detecting that a session token is being used from an unexpected IP range, on an unexpected device fingerprint, or at an unusual time — session hijacking goes undetected until the damage is visible in application logs, often days later.

The SWG intercepts outbound HTTPS sessions and inspects bearer token and cookie headers in real time — flagging reuse of session tokens across unexpected IP ranges, device fingerprints, or time windows, and terminating sessions that deviate from the authenticated user's established pattern. Every session termination event is logged with token identifier, source IP, user identity, and timestamp, producing the per-session audit trail required by NIST SP 800-53r5 AC-4 (Information Flow Enforcement) and SI-4 (System Monitoring), ISO 27001:2022 A.8.16 (Monitoring Activities), and PCI-DSS v4.0 Requirement 10.7 (automated detection of audit log anomalies).

## DNS tunneling

DNS is a control-plane protocol that most organisations allow unconditionally — blocking DNS breaks everything. Attackers exploit DNS by encoding C2 commands and exfiltrated data in DNS query strings. A sequence of queries to `a1b2c3d4.malicious-domain.com`, `e5f6g7h8.malicious-domain.com` carries a covert channel invisible to any control that treats DNS as infrastructure rather than an inspection surface.

DNS tunneling bypasses HTTP-only proxies entirely — the covert channel never touches port 80 or 443. The technique is used by sophisticated attackers for persistent C2 in air-gapped or heavily filtered environments, and by malware families including DNSMessenger, Iodine, and OzymanDNS. Detection requires inspecting the DNS query payload — query length, entropy, subdomain structure — not just resolving the domain name.

The SWG enforces DNS inspection at the query payload level — evaluating query string length, subdomain label count, character entropy, and per-domain request frequency against established baselines. Queries that match tunnel signatures are blocked and logged with the full query string, resolving identity, and timestamp, producing an audit record aligned with NIST SP 800-53r5 SI-4 (System Monitoring) and SC-20 (Secure Name/Address Resolution Service), and ISO 27001:2022 A.8.16 (Monitoring Activities).

## Related posts

- [Execution hides inside encrypted sessions](/blog/2026-05-23-Execution-Threats) - last-mile malware reassembly and XSS/CSRF.
- [Exfiltration uses trusted HTTPS sessions](/blog/2026-05-23-Exfiltration-Threats) - insider theft, shadow AI, cyberslacking.
- [Trust is assessed dynamically](/blog/2026-05-23-Trust-Algorithm) - behavioural correlation and shared inspection context.
