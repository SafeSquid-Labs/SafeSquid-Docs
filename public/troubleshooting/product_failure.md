---
title: Product Activation Failure
description: Diagnose and resolve SafeSquid product activation failure incidents with causes, recovery actions, and audit evidence.
keywords:
  - troubleshooting
  - SafeSquid
  - product failure
---

# Product Activation Failure

Product Activation Failure can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issues

1. I uploaded my activation key, but still SafeSquid UI is showing Failed to set Subscription details.

2. After uploading the activation key, I am getting the template on the browser proxy server refusing connections.

3. Unable to see subscription details on the support page from SafeSquid User Interface.

## Root Causes

1. SafeSquid server is unable to contact the SafeSquid Subscription server.

2. The file (activation key) was not uploaded correctly.

3. The file name you uploaded is other than **activation_key.**

4. After uploading the activation key, the page shows the proxy server refusing connections.

5. SafeSquid service restart was not done properly.

### Case 1: Check for the activation_key file on the SafeSquid server

Run the below command and check for the file:

```text
ls
 
-lrt
 /usr/local/safesquid/security/
```

## root@dev:~# ls -lrt /usr/local/safesquid/security/

total 60

drwxrwxr-- 2 ssquid root 4096 Jul 10 11:55 dns

-rw-rw-r-- 1 ssquid root 724 Jul 28 11:23 krb5.conf

-rw-rw-r-- 1 ssquid root 2111 Aug 3 18:52 activation_key

drwxrwxr-- 2 ssquid root 12288 Aug 4 16:04 policies

drwxrwxr-- 5 ssquid root 4096 Aug 4 16:09 ssl

-rw-rw-r-- 1 ssquid root 15744 Aug 5 09:51 activation_key.updates.backup

## -rw-rw-r-- 1 ssquid root 15744 Aug 5 09:51 activation_key.updates

If the file was not found, then upload your activation key again and click on restart

Restart SafeSquid service from the SafeSquid Interface will work, only if the [monit service](/safesquid_swg/interface/supporting_services_monit) is configured properly on the SafeSquid server.

Otherwise, you can directly restart the SafeSquid service from LINUX box by using below commands

```text
/etc/init.d/safesquid stop
```

```text
/etc/init.d/safesquid start
```

### Case 2: Check the connection to the Subscription server, by using following commands

## root@dev:~# ping swgupdates2.safesquid.net

PING swgupdates2.safesquid.net (104.236.27.61) 56(84) bytes of data.

64 bytes from 104.236.27.61: icmp_seq=1 ttl=52 time=309 ms

64 bytes from 104.236.27.61: icmp_seq=2 ttl=52 time=228 ms

--- swgupdates2.safesquid.net ping statistics ---

2 packets transmitted, 2 received, 0% packet loss, time 1000ms

## rtt min/avg/max/mdev = 228.387/269.078/309.770/40.694 ms

```text
nslookup
 swgupdates2.safesquid.net
```

## Server: 127.0.0.1

Address: 127.0.0.1#53

Non-authoritative answer:

Name: swgupdates2.safesquid.net

## Address: 104.236.27.61

**After uploading the activation key, the page shows the proxy server refusing connections**

SafeSquid restart was not done, start the SafeSquid from the server console by using the command below:

```text
/etc/init.d/safesquid start
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
