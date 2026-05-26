---
title: Response Profiles
description: Use SafeSquid Response Profiles to classify downloads and server responses by MIME type, file extension, size, and headers before applying controls.
keywords:
  - SafeSquid response profiles
  - SafeSquid MIME filtering
  - SafeSquid file extension block
  - SafeSquid content length rules
  - SafeSquid response header filtering
  - configure SafeSquid response profiles
---

# Classify downloads by what they return

## Problem statement

Many important web-control decisions depend on the response, not the request. A harmless-looking URL can return a macro-enabled document, a large archive, a WebSocket upgrade, or a suspicious MIME type. If SafeSquid does not classify the response correctly, downstream controls miss the real risk.

## Client scenario

Use Response Profiles when you need to:

- classify files by MIME type or extension
- detect high-risk downloads such as macro-enabled documents or archives
- separate WebSocket or special header-driven traffic
- trigger downstream blocking, logging, or handling based on returned content

## Key benefits

Response Profiles let you turn content-return characteristics into reusable enforcement signals. That improves file-control precision and makes download governance easier to tune than repeating MIME logic inside many separate rules.

## Prerequisites

### Client-side preparations

- Ensure the relevant download traffic reaches SafeSquid.
- If the response is encrypted, enable HTTPS inspection so SafeSquid can see the returned content.

### SafeSquid-side setup

- Decide which response conditions matter most first: MIME type, file extension, size, header patterns, or streaming behavior.
- Align response-profile names with the enforcement policy they support.

## Setup instructions

### Enable the Response Profiles section

In **Configure → Custom Settings → Response Types**, set **Enabled** to `TRUE`.

If the section is disabled, no response classification occurs.

### Order entries from precise to broad

Response profile logic is evaluated top-down. Put precise high-risk matches above generic content-type rules.

This reduces accidental over-classification.

### Match the right response attributes

Use the fields that best reflect the risk you care about:

- **Content type** for MIME-aware controls
- **File Extension** when the returned file name is meaningful
- **Minimum Content Size** and **Maximum Content Size** for large-download governance
- **Response Header Pattern** for protocol upgrades or specialized handling

### Use added and removed profiles carefully

Use **Added Response Types** to label the response for later enforcement. Use **Removed Response Types** only when a later rule must override an earlier broad classification.

## Verification and validation

### Positive tests

Use controlled downloads that should match the rule, such as:

- a macro-enabled Office document
- an `.epub` or `.azw` file
- a response with `Upgrade: websocket`

Expected result:

- the intended response profile is added
- downstream access or security policy acts on that profile
- logs show the response attributes you expected

### Negative tests

Download a nearby but benign file that should stay outside the rule.

Expected result:

- SafeSquid does not misclassify ordinary business traffic
- downstream controls do not over-block

## Troubleshooting guide

### The response profile does not appear

Likely causes:

- the section is disabled
- the content type or header does not match the real response
- HTTPS inspection is missing

Isolation steps:

- confirm the section is enabled
- inspect the actual MIME type and headers in logs
- confirm decryption for HTTPS traffic

Remediation:

- correct the matching criteria
- enable the required visibility path
- retest with a known sample

### Legitimate downloads are blocked too often

Likely causes:

- a generic MIME pattern is too broad
- file extension matching is catching approved formats
- a broad response profile is being consumed by an aggressive access rule

Isolation steps:

- identify the exact response profile applied
- compare the affected files against intended scope

Remediation:

- narrow the pattern
- add approved exceptions
- tune the downstream enforcement policy

### WebSocket or special response traffic is missed

Likely causes:

- the response header pattern is incorrect
- the relevant header never reaches the expected inspection point

Isolation steps:

- inspect the actual returned headers
- verify the rule pattern against the live header value

Remediation:

- correct the header regex
- retest using a known WebSocket-enabled destination

## Related controls / next steps

- Use [Access Restriction](/Access_Restriction) to block or allow content based on response classification.
- Use [Content Fingerprints](/True-Mime_Fingerprints) when true MIME validation must support the final decision.
- Use [Security Logs](/Security_Logs) to confirm MIME, headers, and final profile application.
