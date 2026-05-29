---
title: Custom Categorization Not Working
description: Diagnose and resolve SafeSquid custom categorization not working incidents with causes, recovery actions, and audit evidence.
keywords:
  - troubleshooting
  - SafeSquid
  - custom categorisation not working
---

# Custom Categorization Not Working

Custom Categorization Not Working can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issues

- I am trying to add new websites to the whitelist or blacklist category, but it is not updating

- Uploaded a new file with some websites and added them to specific categories, but I did not find the websites in the respective category

- SafeSquid interface has hung when I try to add custom websites to any category

## Root Causes

- Verify the status of **the** Categorization Engine from **the** Statistic page of SafeSquid Interface

- **The** SafeSquid server is unable to contact **the** SafeSquid category server

- The file(websites) was not uploaded correctly

### Check for a connection to the category server from your SafeSquid server

Run the below command and see below output

telnet category.safesquid.net 443

Trying 139.59.16.202...

Connected to category.safesquid.net.

Escape character is '^]'.

If the server is not reachable, you have to run the below commands and try telnet again

```text
rndc flush
```

```text
/etc/init.d/bind9 restart
```

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
