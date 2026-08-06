---
title: "LDAP Entries Not Fetched"
description: "Diagnose and resolve SafeSquid ldap entries not fetched incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "failed to fetch ldap entries"]
---

# LDAP Entries Not Fetched

LDAP Entries Not Fetched can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issues

I configured LDAP with Active Directory, but LDAP entries are still not fetched.

## Root Cause

1. **Case 1:** You should not have properly configured LDAP with Active Directory.
2. **Case 2:** You are not able to contact AD (Active Directory).

Verify it from SafeSquid Logs.

## POST [http://safesquid.cfg/](http://safesquid.cfg/) HTTP/1.1

Host: safesquid.cfg

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0

Accept: application/xml, text/xml, _/_; q=0.01

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: [http://safesquid.cfg/](http://safesquid.cfg/)

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

X-Requested-With: XMLHttpRequest

Content-Length: 25

Connection: keep-alive

2019 04 08 12:23:55.725 \[10281\] debug: network: net\_filebuf\_read: speed: 192.168.0.10 uploaded to safesquid.cfg 25 bytes in 20.0000 us \[ 1.2500 MBps \]

2019 04 08 12:23:55.725 \[10281\] debug: request: buffered 25 bytes of POSTDATA

2019 04 08 12:23:55.725 \[10281\] debug: interface: \[IP:192.168.0.10\] \[1\]

2019 04 08 12:23:55.725 \[10281\] debug: interface: invoke\_handler:89 \[ldap\]

**2019 04 08 12:23:55.732 \[0\] debug: ldap: cache\_update:1937 manual/configuration update**

2019 04 08 12:23:55.732 \[0\] debug: network: writing 0 bytes to /usr/local/safesquid/security/dns/safesquid.dns.conf file

2019 04 08 12:23:55.732 \[0\] debug: ldap: init\_routine\_unlocked:239 connection not exists in pool for domain safesquid.local

2019 04 08 12:23:55.732 \[0\] debug: ldap: get\_ld:1174 192.168.221.1:389 max query limit:\[0\], 0 means no limit

2019 04 08 12:23:58.731 \[0\] error: ldap: s\_bind:2253 authentication failed for user :administrator @safesquid.local \[-1 :Can 't contact LDAP server\]

2019 04 08 12:23:58.733 \[10281\] debug: header: to 192.168.0.10:

HTTP/1.1 200 OK

X-Powered-By: safesquid-2019.0401.1624.3-swg-standard

Date: Mon, 08 Apr 2019 12:23:55 GMT

Content-Type: text/xml

Content-Length: 40

Cache-Control: no-cache

Proxy-Connection: keep-alive

X-SafeSquid-Client-ID: 10281.1

## X-SafeSquid-User-Groups: ADMINS

### Case 1: Check for configuration of LDAP with AD (Active Directory).

Run command on the console:

```text
ldapsearch 
-x
 
-h
 
192.168
.221.1 
-b
 
"dc=safesquid,dc=test"
 
-D
 adusername@domain 
-w
 password
```

root@sabproxy:~# ldapsearch -x -h 192.168.221.1 -b "dc=safesquid,dc=test" -D [administrator@safesquid.test](mailto:administrator@safesquid.test) -w sarva@1234

The above command gives you the result of all the fetch entries of users from AD only if the configuration of LDAP integration is correct.

Follow the [Link](https://help.safesquid.com/portal/en/kb/articles/integrate-ad-or-openldap-with-safesquid) for How to integrate AD or Open LDAP with SafeSquid.

### Case2: Check the connection to Active Directory

## root@sabproxy:~# ping 192.168.221.1

PING 192.168.221.1 (192.168.221.1) 56(84) bytes of data.

64 bytes from 192.168.221.1: icmp\_seq=1 ttl=128 time=0.396 ms

64 bytes from 192.168.221.1: icmp\_seq=2 ttl=128 time=0.446 ms

64 bytes from 192.168.221.1: icmp\_seq=3 ttl=128 time=0.361 ms

--- 192.168.221.1 ping statistics ---

3 packets transmitted, 3 received, 0% packet loss, time 2000ms

rtt min/avg/max/mdev = 0.361/0.401/0.446/0.034 ms

root@sabproxy:~# ping ad.safesquid.test

PING ad.safesquid.test (192.168.221.1) 56(84) bytes of data.

64 bytes from 192.168.221.1: icmp\_seq=1 ttl=128 time=0.262 ms

64 bytes from 192.168.221.1: icmp\_seq=2 ttl=128 time=0.358 ms

64 bytes from 192.168.221.1: icmp\_seq=3 ttl=128 time=0.442 ms

^C

--- ad.safesquid.test ping statistics ---

3 packets transmitted, 3 received, 0% packet loss, time 2000ms

## rtt min/avg/max/mdev = 0.262/0.354/0.442/0.073 ms

ad.safesquid.test (192.168.221.1) \>\> Active Directory FQDN and IP Address

**If you are unable to contact Active Directory you should face an error as shown below " Destination Host Unreachable"**

## root@sabproxy:~# ping 192.168.221.1

PING 192.168.221.1 (192.168.221.1) 56(84) bytes of data.

From 192.168.221.222 icmp\_seq=31 Destination Host Unreachable

From 192.168.221.222 icmp\_seq=32 Destination Host Unreachable

--- 192.168.221.1 ping statistics ---

## 37 packets transmitted, 0 received, \+6 errors, 100% packet loss, time 36269ms

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