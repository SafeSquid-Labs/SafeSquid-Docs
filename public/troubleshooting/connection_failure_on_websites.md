---
title: Connection Failure to Websites
description: Diagnose and resolve SafeSquid connection failure to websites incidents with causes, recovery actions, and audit evidence.
keywords:
  - troubleshooting
  - SafeSquid
  - connection failure on websites
---

# Connection Failure to Websites

Connection Failure to Websites can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Connection failed to proxy or origin

When the user accesses the website, the browser displays "**Connection to 192.168.27.30:80 failed**". When the user accesses [https://abc.safesquid.com/](https://abc.safesquid.com/) via proxy and logs in with a corporate email ID, the browser may show "**Connection to abc.safesquid.com:443 failed**".

![Error showing "Connection to abc.safesquid.com:443 failed"](/images/troubleshooting/connection_failure_on_websites_01_error_showing_connection_to_abc_safesquid_com_44.webp)

## Root Causes

If the website which you are trying to reach is not up

If you are unable to reach the particular website because of internet slowness issues.

### Case1

Check whether the website is opening without proxy configuration inside the browser (No proxy in the middle).

If the website is not opening without a proxy, then it is not the problem with SafeSquid.

If it is opening without a proxy, then run the below command to verify whether the website is resolving or not.

Command: nslookup 192.168.27.30

**To check SafeSquid server is connecting to** 192.168.27.30 on port 80

Command: telnet WEBSITE PORT_TO_CONNECTON

When the website cannot be reached, example output:

telnet 192.168.27.30 80

Trying 192.168.27.30...

telnet: Unable to connect to remote host: No route to host

When the website is reachable, the output is

```text
telnet WEBSITE PORT_TO_CONNECTON
```

When the website cannot be reached:

Command :telnet 192.168.27.30 80

you will get this output if the website can connect

root@dev:~# telnet 192.168.27.30 80

Trying 192.168.27.30...

Connected to 192.168.27.30.

Escape character is '^]'.

### Case 2

For an on-premises server integrated with directory services, DNS resolution is done by the directory DNS server.

To check the configuration on the local internal network and its address record pointed on an active directory (AD) or local DNS server.

Run the below commands on the command prompt for **abc.safesquid.com**

```text
nslookup
 abc.safesquid.com
```

If the website is resolving to the local internal network **e.g.** (10.10.11.78,10.10.128.106)

Configure conditional forwarding to the SafeSquid local caching DNS server.

Go to the path: **/etc/bind/**

and create a file.

```text
vim
 named.conf
```

root@swg:/etc/bind# vim named.conf

// This is the primary configuration file for the BIND DNS server named.

//

// Please read /usr/share/doc/bind9/README.Debian.gz for information on the

// structure of BIND configuration files in Debian, *BEFORE* you customize

// this configuration file.

//

// If you are just adding zones, please do that in /etc/bind/named.conf.local

include "/etc/bind/named.conf.options";

include "/etc/bind/named.conf.local";

include "/etc/bind/named.conf.default-zones";

include "/etc/bind/safesquid.dns.conf";

include "/etc/bind/abc.safesquid.com";

Go to the path

```text
cd
 /etc/bind/
```

And create a file

```text
vim
 abc.safesquid.co
```

Add below lines

```text
zone "abc.safesquid.com" {
type forward;
forwarders {10.10.124.101;};
};
```

Command to restart bind9 service:

```text
/etc/init.d/bind9 restart
```

Verify whether the website is resolving to the local IP successfully or not.

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
