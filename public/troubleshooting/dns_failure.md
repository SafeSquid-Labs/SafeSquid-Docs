---
title: "DNS Failure"
description: "Diagnose and resolve SafeSquid dns failure incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "dns failure"]
---

# DNS Failure

DNS Failure can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issue

Via proxy sometimes occur an error "DNS Lookup for safesqddns.com failed".

![Proxy error showing "DNS Lookup for safesqddns.com failed"](/images/troubleshooting/dns_failure_01_proxy_error_showing_dns_lookup_for_safesqddns_co.webp)

## Root Causes

1. The FQDN of the website is incorrect.
2. The local DNS server service is not running.
3. The forwarder DNS server is not able to resolve the query.
4. The network service is down.

## Solution

If the FQDN of the website is incorrect you will face a DNS failure issue to that website while accessing via proxy. So, you have to enter the correct FQDN of that particular website.

If the FQDN of a particular website is correct but the local DNS server service is not running still you can face a DNS failure issue. So, you make sure that the local DNS server service is running.

Run the below commands to verify DNS server service

**nslookup (FQDN of the site)**

example:

**nslookup [www.safesquiddns.com](http://www.safesquiddns.com)**

Server: 127.0.0.1

Address: 127.0.0.1#53

Non-authoritative answer:

[www.safesquiddns.com](http://www.safesquiddns.com) canonical name = safesquiddns.com.

Name: safesquiddns.com

Address: 164.177.149.146

If the website is not able to resolve

root@dev:~# nslookup [www.safesquiddns.com](http://www.safesquiddns.com)

Server: 127.0.0.1

Address: 127.0.0.1#53

server can't find test.safesquiddns.com: NXDOMAIN

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