---
title: "SafeSearch Not Working"
description: "Diagnose and resolve SafeSquid safesearch not working incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "safesearch not working"]
---

# SafeSearch Not Working

SafeSearch Not Working can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

You have enabled all the entries required for Safe Searches, but you are able to access the in appropriate content through search engines, then follow the below steps to Troubleshoot

Test your configuration once. All required entries must be enabled.

Then test your HTTPS Inspection enabled or not. If if not enabled see our document - [How to configure HTTPS inspection](/use_cases/ssl_inspection/ssl_inspection)

Then check the SSL certificate in the browser. See [Test certificate in Firefox](/use_cases/ssl_inspection/ssl_inspection).

Removes the cache and restart the browser and test it again.

You may see block template when "Text Analyzer" and default entry to block pornogrophy in policies and profiles are enabled.

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