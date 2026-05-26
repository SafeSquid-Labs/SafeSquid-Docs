---
title: Blank Report Page
description: Troubleshoot blank or empty report pages in SafeSquid reporting module caused by database sync delays, service issues, or configuration problems.
keywords:
  - SafeSquid blank report page
  - reporting module troubleshooting
  - dashboard display issues
  - report page not loading
  - SafeSquid database sync
---


## Problem
Service interruptions and policy failures increase operational risk when root cause is unclear.

## Benefits
You can diagnose faster with repeatable checks, reduce downtime, and restore expected protection.

## Advantages
You get symptom-first guidance that supports incident response and produces evidence for audit and postmortem review.

## Call to action
Follow the checks in order, capture the observed output, and apply the fix that matches your failure pattern.

## ISSUE
Custom group name is taking time to update on Dashboard.



## Troubleshooting
The dashboard information is obtained from SafeSquid databases. Some records on dashboard is obtained from Master table, whereas some other records are obtained from non-Master table.

Records that are coming from Master table are displayed quickly, whereas records from non-Master table waits for 1000 transactions.

