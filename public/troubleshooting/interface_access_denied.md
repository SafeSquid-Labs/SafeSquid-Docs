---
title: Interface Access Denied
description: Diagnose and resolve SafeSquid interface access denied incidents with causes, recovery actions, and audit evidence.
keywords:
  - troubleshooting
  - SafeSquid
  - interface access denied
---

# Interface Access Denied

Interface Access Denied can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issues

Administrators can be locked out when creating or reordering policies in the Access Restrictions section. The browser then shows Access Denied.

## Root causes

SafeSquid evaluates Access Restrictions entries top to bottom and matches each entry to the connection. After an entry matching the connection's IP or username is applied, later entries are not evaluated for that connection. When creating or editing entries, ensure at least one entry allows access to the web interface ([http://safesquid.cfg/](http://safesquid.cfg/)  -  an embedded Rest UI interface built into SafeSquid, NOT resolved by DNS): an entry that matches the administrator's connection and has Web interface (Config) selected in the Access field.

**Example:**

Scenario: three entries in the Allow list of Access Restrictions:

1. First entry: access the web interface via SSH tunnel.

2. Second entry: allow the AUTHENTICATION BYPASS profile.

3. Third entry: the entry used for general internet access.

A fourth entry is added with Web interface removed from the Access field, then moved up to third. The third position now matches the administrator's connection (the first is for SSH, the second for AUTHENTICATION BYPASS) and has Web interface disabled. The administrator is locked out and sees Access Denied. To avoid this, always keep at least one entry that allows access to the Web interface.

Two options to recover access: restart the SafeSquid service, or use an SSH tunnel to reach the interface and correct the Access Restrictions entries.

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
