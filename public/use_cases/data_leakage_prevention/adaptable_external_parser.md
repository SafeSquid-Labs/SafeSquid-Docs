---
title: External Parser
description: Use SafeSquid External Parser to send request or response content to a custom program for specialized inspection, transformation, or policy decisions.
keywords:
  - SafeSquid external parser
  - custom content inspection
  - SafeSquid executable filter
  - request response parser
  - custom DLP integration
---

# Invoke custom inspection logic safely

## Problem statement

Some enterprises need content checks that go beyond built-in controls. They may need a custom parser, a proprietary classifier, or an integration with internal inspection tooling. Without a controlled way to extend inspection, teams either miss required controls or build unsafe side paths around the proxy.

## Client scenario

Use External Parser when you need to:

- send content to a custom executable or script
- inspect request bodies, response bodies, or both
- integrate specialized internal logic into the web-control path
- test advanced content decisions without replacing SafeSquid

This is a powerful feature. Treat it as an extension point that can affect performance, reliability, and content-handling safety.

## Key benefits

External Parser lets SafeSquid call a custom program during transaction processing. That can support specialized DLP logic, proprietary content checks, and workflow-specific enforcement that built-in controls do not cover directly.

## Prerequisites

### Client-side preparations

- Ensure the relevant traffic passes through SafeSquid.
- For HTTPS traffic, enable HTTPS inspection if the parser must see decrypted content.

### SafeSquid-side setup

- Prepare the executable or script and confirm it handles input safely.
- Decide whether content should be passed by `Pipe` or `File`.
- Test the parser on representative payloads before applying it broadly.
- Ensure the host has enough capacity because external processing adds latency and failure risk.

## Setup instructions

### Enable the global section

In **Configure → Custom Settings → External Applications**, set **Enabled** to `TRUE`.

This activates the section that allows SafeSquid to invoke external programs.

### Create an application policy

Under **Application Policies**, add a policy entry and define:

- **Enabled**
- **Comment**
- **Profiles**
- **Executable**
- **Type**
- **Applies to**
- **Run once per session**
- **Send header**

### Set the executable path carefully

Use **Executable** to define the program and arguments. If you do not use an absolute path, SafeSquid relies on the host `PATH`, which is harder to audit and troubleshoot.

### Choose how content is passed

Set **Type** based on parser behavior:

- `Pipe` sends content to standard input
- `File` writes content to a temporary file and passes the file path as the last argument

Choose the method your parser is designed to handle. A mismatch here causes silent-looking failures.

### Limit scope before broad rollout

Use **Profiles** so the parser applies only to high-risk traffic or a controlled pilot group first.

This reduces latency surprises and makes troubleshooting much easier.

## Verification and validation

### Positive test

Send a controlled request or response that should trigger the parser.

Expected result:

- the parser runs
- the transaction reflects the expected modified or inspected outcome
- logs show the request path and resulting policy behavior

### Negative test

Send traffic outside the intended profile or content scope.

Expected result:

- the parser does not run unnecessarily
- unaffected traffic follows normal SafeSquid processing

### Operational checks

Verify:

- parser exit status behavior
- transaction latency before and after enabling the parser
- what happens when the parser returns a non-zero status code

## Troubleshooting guide

### The parser never seems to run

Likely causes:

- the global section is disabled
- the policy is disabled
- the request does not match the configured profile or direction

Isolation steps:

- confirm **Enabled** is `TRUE` globally and in the entry
- confirm **Applies to** matches request, response, or both
- confirm the traffic matches the intended profile

Remediation:

- enable the correct objects
- correct the scope
- retest with a controlled request

### The parser runs but has no visible effect

Likely causes:

- the executable exits with a non-zero status
- the parser output is not in the expected format
- the wrong headers are being sent

Isolation steps:

- test the executable outside SafeSquid
- confirm the output format is valid
- confirm whether request headers, response headers, or both are being sent

Remediation:

- fix the executable behavior
- correct the output format
- retest with a known-good sample

### Performance degrades after enabling the parser

Likely causes:

- the parser runs on too much traffic
- file-based processing adds overhead
- the executable is slow or unstable

Isolation steps:

- compare latency before and after deployment
- check whether the parser applies globally instead of to a pilot profile
- measure execution time on representative payloads

Remediation:

- narrow scope with profiles
- optimize the parser
- switch passing mode if appropriate
- retest under load

## Related controls / next steps

- Use [Content Fingerprints](/True-Mime_Fingerprints) when file-type validation is the main need.
- Use [Text Analyzer](/Text_Analyser) and [Image Analyzer](/Image_Analyser_AI) before building custom logic for problems SafeSquid already solves natively.
- Use [Security Logs](/Security_Logs) to investigate parser-side effects and request outcomes.
