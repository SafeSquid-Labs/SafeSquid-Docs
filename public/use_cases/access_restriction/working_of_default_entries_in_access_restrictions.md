---
title: "Working of Default Entries in Access Restrictions"
description: "Understand how default SafeSquid access-restriction entries behave so you can modify baseline policy safely without creating hidden enforcement gaps."
keywords: ["SafeSquid default policies", "access restriction defaults", "default web access rules", "proxy policy configuration", "SafeSquid access control"]
---

# Understand baseline rules before changing them

## Problem statement

Default restriction entries are easy to overlook because they seem familiar. In practice, they shape the baseline enforcement path for every later policy decision. Editing them casually can create hidden allow paths, unexpected denials, or troubleshooting confusion that only appears in production.

## Client scenario

Use this page when you need to:

- understand what the shipped default entries are doing
- decide whether to modify or leave a default rule in place
- troubleshoot policy behavior that seems to happen before custom rules
- prepare a safer rollout plan for access-policy changes

## Key benefits

A clear understanding of the default entries reduces accidental policy drift. It also helps new administrators understand whether a behavior comes from their custom logic or from the product baseline.

## Prerequisites

### Client-side preparations

- Reproduce the user workflow that is affected.
- Gather the username, destination, and time window for testing.

### SafeSquid-side setup

- Review the current ordered access restriction list before modifying defaults.
- Identify any custom exceptions that depend on the current baseline behavior.

## Setup instructions

### Inspect default entries before editing

Read the existing default entries in their current order.

Do not assume they are harmless placeholders. In many environments they participate in the first effective allow or deny path.

### Compare default logic with your custom policy

Before editing a default entry, ask:

- does this default rule still support the intended baseline?
- does a custom rule depend on this rule being present or absent?
- would it be safer to add a new specific rule instead of mutating the baseline?

### Prefer narrow overrides over casual baseline edits

If the requirement is specific, add a targeted exception or new rule first. Avoid changing defaults just to solve a narrow one-off workflow.

That keeps the baseline understandable and reduces surprise for future operators.

## Verification and validation

### Positive test

Identify a transaction that should follow the default path and verify it still behaves as intended after your review or edit.

Expected result:

- the baseline rule path is understood
- the final action matches the intended default behavior

### Negative test

Test a custom workflow that should bypass or override the default behavior.

Expected result:

- the custom rule still wins where intended
- the default rule does not unexpectedly reassert control

## Troubleshooting guide

### Custom policy changes seem ineffective

Likely causes:

- a default entry matches first
- administrators assumed the defaults were inactive

Isolation steps:

- inspect rule order
- identify which entry actually triggered in logs

Remediation:

- move the specific custom rule above the default if appropriate
- narrow the default entry if it is too broad

### Unexpected access is still allowed

Likely causes:

- a baseline allow remains in place
- a deny rule was added below a broader default allow

Isolation steps:

- compare the triggered rule against the full ordered list
- retest with the same user and destination

Remediation:

- move or narrow the relevant entries
- validate again with positive and negative tests

## Related controls / next steps

- Use [Access Restriction](/Access_Restriction) for the full policy model.
- Use [Security Logs](/Security_Logs) to identify which entry actually decided the request.