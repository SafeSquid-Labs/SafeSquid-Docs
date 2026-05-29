---
title: Blank Report Page
description: Diagnose and resolve SafeSquid blank report page incidents with causes, recovery actions, and audit evidence.
keywords:
  - troubleshooting
  - SafeSquid
  - blank report page
---

# Blank Report Page

Blank Report Page can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## ISSUE

Custom group name is taking time to update on Dashboard.

The dashboard information is obtained from SafeSquid databases. Some records on dashboard is obtained from Master table, whereas some other records are obtained from non-Master table.

Records that are coming from Master table are displayed quickly, whereas records from non-Master table waits for 1000 transactions.

## Capture useful evidence

Collect evidence before restarting services or changing policy. Keep screenshots, command output, and relevant SafeSquid logs with the incident ticket.

```sh
tail -100 /var/log/safesquid/safesquid.log
tail -100 /var/log/syslog
```

Record the affected user, source IP address, requested URL, timestamp, browser error, SafeSquid policy section changed, and verification result.

## Next steps

- Use [Find a complete connection log](/troubleshooting/how_to_use_find_client_id_sh_for_getting_complete_connection_log) to trace a specific client transaction.
- Use [Troubleshooting](/troubleshooting/troubleshooting) for the broader diagnostic checklist.
