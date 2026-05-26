---
title: Content Fingerprints
description: Use SafeSquid content fingerprinting and true MIME detection to identify disguised files, reduce spoofing risk, and improve content-control accuracy.
keywords:
  - SafeSquid content fingerprints
  - true MIME detection
  - file type spoofing prevention
  - disguised malware detection
  - SafeSquid DLP file validation
---

# Trust file content, not file names

## Problem statement

Attackers and careless users can disguise files by changing extensions, headers, or upload context. If policy decisions rely only on visible names or claimed MIME types, malware and unauthorized data transfers can slip through controls that appear correct on paper.

## Client scenario

Use content fingerprinting when you need to:

- identify the real file type instead of trusting the extension
- detect uploads or downloads that do not match their declared content type
- strengthen malware, DLP, and upload-control policies
- reduce false trust in renamed or disguised files

## Key benefits

True MIME detection improves the quality of downstream policy decisions. It helps SafeSquid distinguish between what a file claims to be and what it actually contains, which matters for malware prevention, upload governance, and sensitive-data controls.

## Prerequisites

### Client-side preparations

- Ensure the traffic path passes file uploads and downloads through SafeSquid.
- If the transfer is encrypted, enable HTTPS inspection so SafeSquid can inspect the payload.

### SafeSquid-side setup

- Identify which upload and download channels matter most, such as email, webmail, file sharing, and SaaS storage.
- Review related controls that will consume this signal, including DLP, malware, and access-restriction policies.

## Setup instructions

### Use true MIME signals in policy design

Build file-handling policies on the actual detected content type, not only on filename extensions or user-declared metadata.

This matters because extension-only controls are easy to bypass.

### Pair content fingerprinting with upload and response policies

Use true MIME awareness alongside:

- upload controls
- DLP inspection
- malware and threat-prevention controls
- request and response profiles

This turns MIME detection into an enforcement decision instead of a passive observation.

### Validate high-risk channels first

Start with traffic paths where disguised files create the most risk:

- browser uploads to SaaS platforms
- downloads from unknown or uncategorized sources
- email and webmail attachments

## Verification and validation

### Positive test

Use a controlled file whose extension or declared type does not match its real content.

Expected result:

- SafeSquid identifies the transaction based on the real content type
- the related policy decision follows the true MIME result
- logs and reports reflect the transaction in a way operators can investigate

### Negative test

Transfer a legitimate file whose extension and content type match.

Expected result:

- SafeSquid allows or handles the file according to normal policy
- no spoofing-specific control triggers by mistake

### Evidence to review

Verify:

- request and response logs for the transaction
- policy outcomes tied to upload or download handling
- whether the detected content type aligns with the actual test file

## Troubleshooting guide

### File-type controls do not trigger

Likely causes:

- HTTPS inspection is missing for encrypted transfers
- the related enforcement policy does not consume the MIME signal
- the test transaction bypassed the expected proxy path

Isolation steps:

- confirm the transfer passed through SafeSquid
- confirm decryption for HTTPS traffic
- inspect the request and response policy path

Remediation:

- enable the correct inspection path
- attach the MIME-aware signal to a blocking or logging rule
- retest with a controlled spoofed file

### Legitimate files are blocked unexpectedly

Likely causes:

- an enforcement rule is too broad
- the policy treats all uncommon file types as suspicious

Isolation steps:

- review the exact content type detected
- compare the rule scope with the business use case

Remediation:

- narrow the rule
- add approved exceptions for legitimate business formats
- retest with both approved and disguised files

## Related controls / next steps

- Use [Content Moderation](/Profiling_Engine/Content_Analyser) for broader content-risk controls.
- Use [Adaptable External Parser](/Adaptable_External_Parser) when custom downstream inspection logic is required.
- Use [Security Logs](/Security_Logs) for evidence collection during spoofing and malware investigations.
