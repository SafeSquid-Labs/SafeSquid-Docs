---
title: SafeSearch Not Working
description: Troubleshoot Safe Search issues in SafeSquid when inappropriate content is accessible despite enabling all Safe Search entries. Includes HTTPS Inspection validation, SSL certificate checks, and policy verification.
keywords:
  - SafeSquid Safe Search
  - HTTPS inspection troubleshooting
  - SSL certificate check
  - block pornography policy
  - inappropriate content search
---


## Problem
Service interruptions and policy failures increase operational risk when root cause is unclear.

## Benefits
You can diagnose faster with repeatable checks, reduce downtime, and restore expected protection.

## Advantages
You get symptom-first guidance that supports incident response and produces evidence for audit and postmortem review.

## Call to action
Follow the checks in order, capture the observed output, and apply the fix that matches your failure pattern.

You have enabled all the entries required for Safe Searches, but you are able to access the in appropriate content through search engines, then follow the below steps to Troubleshoot

Test your configuration once. All required entries must be enabled.

Then test your HTTPS Inspection enabled or not. If if not enabled see our document - [How to configure HTTPS inspection](/SSL_Inspection)

Then check the SSL certificate in the browser. See [Test certificate in Firefox](/Configure_HTTPS_Inspection#import-certificate-into-firefox).

Removes the cache and restart the browser and test it again.

You may see block template when "Text Analyzer" and default entry to block pornogrophy in policies and profiles are enabled.

