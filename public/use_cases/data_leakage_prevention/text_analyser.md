---
title: "Text Analyzer"
description: "Use SafeSquid Text Analyzer to score and control web content based on keywords, patterns, and MIME-aware inspection for DLP and content policy enforcement."
keywords: ["SafeSquid text analyzer", "content-based filtering", "keyword scoring filter", "SafeSquid DLP", "MIME-aware text inspection", "real-time text analysis SafeSquid"]
---

# Score text before it leaves control

## Problem statement

URL category decisions alone do not tell you what a page or payload actually contains. Sensitive terms, policy-violating language, and uncategorized harmful content can pass through allowed sites unless the body content is inspected directly.

## Client scenario

Use Text Analyzer when you need to:

- score page or payload content by keywords or regular expressions
- detect uncategorized inappropriate content
- identify likely data leakage indicators in web traffic
- apply different text-inspection policies to different user groups or profiles

Text Analyzer is strongest when paired with HTTPS inspection, access restriction policies, and reporting.

## Key benefits

Text Analyzer lets you inspect content instead of trusting domain reputation alone. It helps administrators build detection logic for pornography, sensitive business terms, regulatory data patterns, and custom policy markers without relying only on third-party category databases.

## Prerequisites

### Client-side preparations

- Ensure client traffic is actually passing through SafeSquid.
- If the content is encrypted, deploy the SafeSquid Root CA and enable HTTPS inspection first.

### SafeSquid-side setup

- Confirm HTTPS inspection is enabled for traffic you want to inspect.
- Identify which MIME types should be scanned. Broad scanning increases coverage but can raise false positives and processing load.
- Decide whether the first rollout should log and tune, or block immediately.

## Setup instructions

### Enable the global section

In **Configure → Real Time Content Security → Text Analyzer**, set **Enabled** to `TRUE`.

This turns on the feature globally. If the section remains disabled, none of the policy entries will take effect.

### Set the threshold deliberately

Configure **Threshold** to define when cumulative matches cause a block.

Use a lower threshold when a single match should be decisive. Use a higher threshold when you want multiple indicators before SafeSquid blocks the content.

### Choose a user-facing template

Set **Template** if you want a specific response page when the threshold is reached.

This matters in production because users and help desks need a clear signal that a policy decision, not a network fault, caused the block.

### Create filtering policies

Add policy entries under **Filtering Policies**.

For each policy:

- set **Enabled** to `TRUE`
- use **Comment** to describe the business purpose
- scope with **Profiles** when the rule should apply only to selected users or traffic classes
- restrict **Mime type** where possible, such as `text/html` or `application/json`
- define **Keyword(s)** as the regular expression or terms to match
- set **Score** to reflect how strongly one match should contribute to the block threshold

### Keep rules specific

Use targeted patterns instead of broad keywords where possible. A generic word can trigger on harmless pages and create false confidence about DLP quality.

## Verification and validation

### Positive test

Create or access a test page that contains the configured keywords often enough to exceed the threshold.

Expected result:

- SafeSquid blocks the page or payload
- the configured template appears
- the relevant log entry shows the text-analysis outcome or associated filter action

### Negative test

Access a page that contains similar but non-matching text, or a MIME type outside the rule scope.

Expected result:

- SafeSquid allows the request
- the score does not exceed threshold
- no misleading block event appears for the rule

### What to verify in logs

Verify the request shows:

- the correct user or client identity
- the expected profile set
- the correct MIME type
- the expected filter or policy outcome

## Troubleshooting guide

### Content is not being blocked

Likely causes:

- HTTPS inspection is not active for encrypted pages
- the MIME type does not match the policy
- the keyword expression does not match the actual content
- the score does not reach the threshold

Isolation steps:

- confirm the page is decrypted and visible to SafeSquid
- inspect the actual MIME type in logs
- test the expression with known matching content
- compare total score against the configured threshold

Remediation:

- enable HTTPS inspection where appropriate
- correct the MIME scope
- refine the pattern
- adjust score or threshold, then retest

### Too many false positives occur

Likely causes:

- keywords are too broad
- threshold is too low
- the rule applies to all users instead of a high-risk profile

Isolation steps:

- review blocked samples
- identify which term or pattern triggered repeatedly
- compare affected traffic against intended policy scope

Remediation:

- narrow the regex
- increase the threshold
- limit the rule with profiles or MIME types
- retest with both positive and negative examples

### Logs show requests, but not useful policy evidence

Likely causes:

- the wrong log family is being reviewed
- the request is allowed and only appears in request-level logs
- operators are checking only UI summaries and not underlying log records

Isolation steps:

- review extended and native logs together
- search by username, URL, and time window
- confirm the transaction reached the proxy path you expected

Remediation:

- use request-level logs for evidence collection
- preserve the test case details so the event can be traced again

## Related controls / next steps

- Use [Compliance Templates](/Compliance_Templates) for pattern-based detection starting points.
- Use [Content Moderation](/Profiling_Engine/Content_Analyser) to combine categorization, text, and image controls.
- Use [Security Logs](/Security_Logs) and [Reporting Module](/Reporting_Module) to validate policy outcomes and retain evidence.