---
title: Login Issues on Specific Websites
description: Diagnose and resolve SafeSquid login issues on specific websites incidents with causes, recovery actions, and audit evidence.
keywords:
  - troubleshooting
  - SafeSquid
  - unable to login specific website
---

# Login Issues on Specific Websites

Login Issues on Specific Websites can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issues

1. [https://www.facebook.com/](https://www.facebook.com/) is accessible via proxy but login fails.

2. Login to specific websites using Facebook or Google credentials fails via proxy.

3. Login works on [https://www.facebook.com/](https://www.facebook.com/) but fails on [https://accounts.google.com/](https://accounts.google.com/)

4. Login fails on both [https://accounts.google.com/](https://accounts.google.com/) and [https://www.facebook.com/](https://www.facebook.com/)

## Solution

### Case 1: Facebook accessible via proxy but login fails

When [https://www.facebook.com/](https://www.facebook.com/) is accessible via proxy with HTTPS inspection enabled, HTTPS and SSL certificate configuration in the browser are correct. If HTTPS inspection is not configured, follow [Configure HTTPS Inspection](/use_cases/ssl_inspection/ssl_inspection). Inability to log in on Facebook usually means the Cookie Filter section is enabled with Global TRUE. Set the policy under Privacy Control > Cookie filter > Deny to Enabled FALSE (search for "Strip cookies from all connections profiled as NO LOGIN") and disable it.

### Case 2: Login fails on a specific website using Facebook or Google credentials via proxy

Confirm the target website is HTTP or HTTPS. For HTTPS, configure the HTTPS Inspection section; follow [Configure HTTPS Inspection](/use_cases/ssl_inspection/ssl_inspection). If login to [https://stackoverflow.com/](https://stackoverflow.com/) via Facebook or Google fails, the Elevated Privacy section is likely enabled with Global TRUE. Set the policy under Privacy Control > Elevated Privacy > Elevated policies to Enabled FALSE (search for "Blocks the third-party cookies") and disable it.

### Case 3: Facebook login works but Google account login fails

When login works on [https://www.facebook.com/](https://www.facebook.com/) and other sites but fails only on [https://accounts.google.com/](https://accounts.google.com/), the corporate policy under Header Filter > Insert is likely enabled. Set the policy under Privacy Control > Header Filter > Insert to Enabled FALSE (search for "Enforce use of corporate Google Account, for all users who are NOT ALLOWED PERSONAL GOOGLE ACCOUNTS") and disable it.

### Case 4: Login fails on both Google and Facebook

When login fails only on [https://accounts.google.com/](https://accounts.google.com/) and [https://www.facebook.com/](https://www.facebook.com/), the "Block Particular User Login to Facebook or Gmail" policy is likely enabled. Set the policy under Real Time Content Security > Content modifier > Rewrite Policies to Enabled FALSE.

If the global section is enabled for the particular section but the policy under that particular section is disabled then that individual policy should not work.

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
