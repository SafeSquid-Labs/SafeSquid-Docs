---
title: DNS Failure
description: Resolve DNS lookup failures in SafeSquid when accessing web resources via proxy.
keywords:
  - SafeSquid dns failure
  - dns lookup failed via proxy
  - dns resolution error SafeSquid
  - troubleshoot dns proxy error
  - SafeSquid nslookup fails
---



## Issue
Via proxy sometimes occur an error "DNS Lookup for safesqddns.com failed".

![Proxy error showing "DNS Lookup for safesqddns.com failed"](/img/Troubleshooting/DNS_failure/image1.webp)



## Root Causes

1.  The FQDN of the website is incorrect.
1.  The local DNS server service is not running.
1.  The forwarder DNS server is not able to resolve the query.
1.  The network service is down.



## Solution
If the FQDN of the website is incorrect you will face a DNS failure issue to that website while accessing via proxy. So, you have to enter the correct FQDN of that particular website.

If the FQDN of a particular website is correct but the local DNS server service is not running still you can face a DNS failure issue. So, you make sure that the local DNS server service is running.

Run the below commands to verify DNS server service

**nslookup (FQDN of the site)**

example:

**nslookup www.safesquiddns.com**

Server: 127.0.0.1

Address: 127.0.0.1#53

Non-authoritative answer:

www.safesquiddns.com canonical name = safesquiddns.com.

Name: safesquiddns.com

Address: 164.177.149.146

If the website is not able to resolve

root@dev:~# nslookup www.safesquiddns.com

Server: 127.0.0.1

Address: 127.0.0.1#53

server can't find test.safesquiddns.com: NXDOMAIN

