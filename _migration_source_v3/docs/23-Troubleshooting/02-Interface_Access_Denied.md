---
title: Interface Access Denied
description: Resolve issues when SafeSquid denies access to its web interface due to misconfigured Access Restrictions. Learn root causes and how to regain access using SSH or service restart.
keywords:
  - SafeSquid access denied
  - SafeSquid web interface blocked
  - SafeSquid locked out
  - SafeSquid access restriction troubleshooting
  - SafeSquid ssh tunnel ui access
---



## Issues
Administrators can be locked out when creating or reordering policies in the Access Restrictions section. The browser then shows Access Denied.



## Root causes
SafeSquid evaluates Access Restrictions entries top to bottom and matches each entry to the connection. After an entry matching the connection's IP or username is applied, later entries are not evaluated for that connection. When creating or editing entries, ensure at least one entry allows access to the web interface (http://safesquid.cfg/ — an embedded Rest UI interface built into SafeSquid, NOT resolved by DNS): an entry that matches the administrator's connection and has Web interface (Config) selected in the Access field.

**Example:**

Scenario: three entries in the Allow list of Access Restrictions:

1.  First entry: access the web interface via SSH tunnel.
2.  Second entry: allow the AUTHENTICATION BYPASS profile.
3.  Third entry: the entry used for general internet access.

A fourth entry is added with Web interface removed from the Access field, then moved up to third. The third position now matches the administrator's connection (the first is for SSH, the second for AUTHENTICATION BYPASS) and has Web interface disabled. The administrator is locked out and sees Access Denied. To avoid this, always keep at least one entry that allows access to the Web interface.



## Troubleshooting
Two options to recover access: restart the SafeSquid service, or use an SSH tunnel to reach the interface and correct the Access Restrictions entries.

