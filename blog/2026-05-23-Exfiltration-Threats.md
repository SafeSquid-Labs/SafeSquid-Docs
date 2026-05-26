---
slug: exfiltration-threats
title: 'Exfiltration uses trusted HTTPS sessions'
description: 'Insider data theft, shadow AI data submission, and cyberslacking require content-level inspection of uploads and POST bodies.'
---

# Exfiltration uses trusted HTTPS sessions

Data leaves the network and acceptable-use policy erodes through the same HTTPS sessions used for legitimate work — uploads to sanctioned cloud services, POST bodies to AI endpoints, and unrestricted personal browsing.

## Insider data theft

An employee with access to customer data, intellectual property, or financial records uploads files to OneDrive, Google Drive, or Dropbox. The upload is HTTPS. The destination is a sanctioned cloud storage service that the URL-category engine classifies as "Business/Cloud Storage" — allowed. Nothing about the transaction looks suspicious at the network or DNS layer.

Without content inspection of the upload payload, the upload event is invisible. The distinction between a developer backing up project files and a finance employee exfiltrating a customer database does not exist at the envelope level — the distinction exists only in the content.

Insider threats account for 20% of data breaches ([Verizon DBIR 2024](https://www.verizon.com/business/resources/reports/dbir/)) and carry the highest per-incident cost because such incidents typically involve the most sensitive data and the longest dwell time before discovery. GDPR Article 32, HIPAA § 164.312, and SOC 2 CC6 all require controls that can detect and prevent this class of event.

## Shadow AI data submission

Employees submit confidential data — proprietary source code, customer PII, financial records, internal meeting notes — to public generative AI services (ChatGPT, Google Gemini, Claude.ai, Perplexity) via HTTPS, believing the interaction is a productivity tool rather than a data transfer to a third-party processor operating under separate, non-enterprise terms of service. The data leaves the corporate perimeter in an HTTP POST request body, inside a TLS session that a URL-category engine classifies as "Productivity/AI Tools" — allowed.

The Samsung 2023 incident established the category risk: engineers submitted proprietary source code and internal meeting notes to ChatGPT in at least three separate events within weeks of the tool being made available inside the organisation. The data entered OpenAI's training and processing pipeline before Samsung implemented an AI access policy. CybSafe and the National Cybersecurity Alliance ([2025](https://webflow.cybsafe.com/press-releases/study-almost-40-of-workers-share-sensitive-information-with-ai-tools-without-employers-knowledge)) report that 38% of employees share confidential data with AI tools without organisational approval.

The legal exposure is categorically different from general data exfiltration. GDPR Articles 5(1)(f) and 28 require a Data Processing Agreement (DPA) with any third-party processor handling personal data — ChatGPT and equivalent consumer AI services carry no standard enterprise DPA, meaning submission of personal data may itself constitute a GDPR violation independent of any breach. HIPAA § 164.308(b) requires a Business Associate Agreement (BAA) before Protected Health Information (PHI) can be processed by a third party — OpenAI carries no BAA, making submission of PHI to ChatGPT a per se HIPAA violation. NIST SP 800-53r5 AC-4 (Information Flow Enforcement) and AC-20 (Use of External Information Systems), ISO 27001:2022 A.5.10 and A.8.23, and SOC 2 CC6.7 all address controls on data flowing to external services.

The SWG control is precise and does not require blanket AI service denial: identify HTTPS traffic to AI service domains by URL category or application signature; inspect the HTTP POST request body for PII patterns, intellectual property markers, or DLP policy triggers; enforce allow/block/monitor policy per authenticated user identity or group. The result is an "allow read, block data submission" posture — employees can use AI services for research while the organisation prevents sensitive data from transiting to third-party processors without a DPA or BAA. Shadow AI is predominantly inadvertent; the SWG surfaces the behaviour for policy enforcement and audit evidence rather than assuming malicious intent.

## Cyberslacking

Non-work web browsing, personal streaming, social media access, and shadow-IT application use degrade business performance and create direct compliance exposure. Bandwidth consumed by personal streaming degrades business application performance and violates network usage policy. Shadow-IT applications introduced without security review carry unknown security posture and create uncontrolled data pathways. Policy violations compound regulatory risk: an employee streaming pirated content on a corporate network creates copyright liability; personal cloud storage use creates data governance gaps; personal email access routes communication outside DLP controls on corporate mail.

URL-category engines can block broad categories but lack time-of-day distinctions, per-user exceptions, and detection of policy violations embedded in otherwise-allowed services. Acceptable-use enforcement requires policy evaluation at the session and content level — identifying the authenticated user, the requested application, the time of access, and the content flowing through the session.

The SWG evaluates every web request against the authenticated user's identity, group membership, time-of-day schedule, and content category — enforcing acceptable-use policy with per-user precision rather than organisation-wide blocks. Every enforcement action is logged with user identity, application identifier, destination URL, timestamp, and matched policy rule, producing an audit record that supports HR review, legal discovery, and compliance reporting under SOC 2 CC6.7 and ISO 27001:2022 A.5.10.

## Related topics

- [Command and control threats](/blog/command-and-control-threats) — APT C2, infostealers, session hijacking, DNS tunneling
- [Zero-Trust principles](/blog/zero-trust-principles) — least privilege, identity-aware policy, assume breach
- [Adoption criteria](/blog/adoption-criteria) — when Layer-7 Zero-Trust enforcement applies
