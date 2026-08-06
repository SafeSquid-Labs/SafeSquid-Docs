---
title: "Content Moderation"
slug: "/Profiling_Engine/Content_Analyser"
description: "Combine SafeSquid categorization, text analysis, and image analysis to control inappropriate or risky web content with validation-ready policy design."
keywords: ["SafeSquid content moderation", "image filtering proxy", "text content analysis", "inappropriate content blocking", "content categorization", "web content filtering"]
---

# Combine category and content controls

## Problem statement

Category filtering alone misses pages that are uncategorized, newly created, user generated, or mixed in purpose. Enterprises that need safer browsing, acceptable-use enforcement, or sensitive-content control must inspect both where traffic goes and what the content actually contains.

## Client scenario

Use this approach when you need to:

- block inappropriate or risky content across allowed and unknown sites
- combine category rules with text and image inspection
- tune policies differently for students, staff, contractors, or privileged users
- reduce reliance on a single detection method

## Key benefits

SafeSquid content moderation combines three useful control paths:

- categorization for fast domain and site-level decisions
- Text Analyzer for body-content scoring
- Image Analyzer for direct visual-content inspection

Together, these controls improve coverage across known bad sites, uncategorized pages, and allowed platforms that still contain policy-violating material.

## Prerequisites

### Client-side preparations

- Route client web traffic through SafeSquid.
- Deploy the Root CA and enable HTTPS inspection if you need to inspect encrypted sites.

### SafeSquid-side setup

- Confirm categorization, Text Analyzer, and Image Analyzer are available in the configuration portal.
- Decide which profiles need strict enforcement and which need monitored exceptions.
- Plan a tuning period before enabling broad blocking in production.

## Setup instructions

### Start with categorization

Use categorization to block clearly unwanted websites and reduce the amount of content that needs deeper inspection.

If you already know the domains that should never be accessed, category and custom categorization policies are the fastest first layer.

### Add image inspection for visual risk

Use [Image Analyzer](/Image_Analyser_AI) where visual content matters, especially on social, media-rich, and user-generated platforms.

This closes a gap that text-only filtering cannot see.

### Add text inspection for page and payload content

Use [Text Analyzer](/Text_Analyser) to score risky keywords, sensitive terms, or policy markers in HTML and other text-based content.

This helps with uncategorized pages, regulated data patterns, and sites that contain mixed content.

### Scope by profile instead of weakening the baseline

If some teams legitimately need broader access, use profiles and targeted exceptions. Do not lower the global protection level for everyone just to solve one workflow.

## Verification and validation

### Positive tests

Test each layer separately and then together:

- access a blocked category site
- access a page with risky text that should trigger Text Analyzer
- access a page with images that should trigger Image Analyzer

Expected result:

- category rules block known-bad destinations
- text and image controls catch content that category rules alone would miss
- logs show which layer triggered the final action

### Negative tests

Use legitimate business pages with neutral text and images.

Expected result:

- permitted sites remain usable
- legitimate business images are not blocked unnecessarily
- text scoring does not trigger on harmless content

## Troubleshooting guide

### Harmful content still appears on allowed sites

Likely causes:

- HTTPS inspection is missing
- text or image analyzers are disabled
- the content does not match current rules

Isolation steps:

- confirm the site is decrypted
- confirm both analyzer sections and rules are enabled
- inspect which profiles applied to the session

Remediation:

- enable the missing inspection path
- add or refine analyzer rules
- retest with controlled samples

### Legitimate content is blocked too often

Likely causes:

- analyzer thresholds are too aggressive
- global rules are being used where profile-scoped rules are needed

Isolation steps:

- review the exact trigger path
- compare affected users against intended policy scope

Remediation:

- tune thresholds
- narrow the rule scope
- introduce explicit exceptions for approved workflows

## Related controls / next steps

- Use [Text Analyzer](/Text_Analyser) for keyword and pattern scoring.
- Use [Image Analyzer](/Image_Analyser_AI) for visual-content control.
- Use [Content Fingerprints](/True-Mime_Fingerprints) when file-type spoofing and upload control also matter.