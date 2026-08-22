---
title: LDAP Entries Not Fetched
description: Troubleshooting guide for resolving LDAP integration issues with Active Directory in SafeSquid, including LDAP configuration and AD connectivity.
keywords:
  - SafeSquid ldap integration
  - ldap entries not showing
  - ldap can't contact server
  - SafeSquid ad integration issues
  - troubleshoot SafeSquid ldap
---



## Issues
I configured LDAP with Active Directory, but LDAP entries are still not fetched.



## Root Cause

1.  **Case 1:** You should not have properly configured LDAP with Active Directory.
1.  **Case 2:** You are not able to contact AD (Active Directory).

Verify it from SafeSquid Logs.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  POST http://safesquid.cfg/ HTTP/1.1
  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  Host: safesquid.cfg

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0

  Accept: application/xml, text/xml, */*; q=0.01

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer: http://safesquid.cfg/

  Content-Type: application/x-www-form-urlencoded; charset=UTF-8

  X-Requested-With: XMLHttpRequest

  Content-Length: 25

  Connection: keep-alive

  2019 04 08 12:23:55.725 [10281] debug: network: net_filebuf_read: speed: 192.168.0.10 uploaded to safesquid.cfg 25 bytes in 20.0000 us [ 1.2500 MBps ]

  2019 04 08 12:23:55.725 [10281] debug: request: buffered 25 bytes of POSTDATA

  2019 04 08 12:23:55.725 [10281] debug: interface: [IP:192.168.0.10] [1]

  2019 04 08 12:23:55.725 [10281] debug: interface: invoke_handler:89 [ldap]

  **2019 04 08 12:23:55.732 [0] debug: ldap: cache_update:1937 manual/configuration update**

  2019 04 08 12:23:55.732 [0] debug: network: writing 0 bytes to /usr/local/safesquid/security/dns/safesquid.dns.conf file

  2019 04 08 12:23:55.732 [0] debug: ldap: init_routine_unlocked:239 connection not exists in pool for domain safesquid.local

  2019 04 08 12:23:55.732 [0] debug: ldap: get_ld:1174 192.168.221.1:389 max query limit:[0], 0 means no limit

  2019 04 08 12:23:58.731 [0] error: ldap: s_bind:2253 authentication failed for user:administrator@safesquid.local [-1:Can't contact LDAP server]

  2019 04 08 12:23:58.733 [10281] debug: header: to 192.168.0.10:

  HTTP/1.1 200 OK

  X-Powered-By: safesquid-2019.0401.1624.3-swg-standard

  Date: Mon, 08 Apr 2019 12:23:55 GMT

  Content-Type: text/xml

  Content-Length: 40

  Cache-Control: no-cache

  Proxy-Connection: keep-alive

  X-SafeSquid-Client-ID: 10281.1

  X-SafeSquid-User-Groups: ADMINS
  ------------------------------------------------------------------------------------------------------------------------------------------------------------



## Troubleshooting
### Case 1: Check for configuration of LDAP with AD (Active Directory).
Run command on the console:

```bash
ldapsearch -x -h 192.168.221.1 -b "dc=safesquid,dc=test" -D adusername@domain -w password
```
root@sabproxy:~# ldapsearch -x -h 192.168.221.1 -b "dc=safesquid,dc=test" -D administrator@safesquid.test -w sarva@1234

The above command gives you the result of all the fetch entries of users from AD only if the configuration of LDAP integration is correct.

Follow the [Link](https://help.safesquid.com/portal/en/kb/articles/integrate-ad-or-openldap-with-safesquid) for How to integrate AD or Open LDAP with SafeSquid.

### Case2: Check the connection to Active Directory
  -----------------------------------------------------------------------
  root@sabproxy:~# ping 192.168.221.1
  -----------------------------------------------------------------------
  PING 192.168.221.1 (192.168.221.1) 56(84) bytes of data.

  64 bytes from 192.168.221.1: icmp_seq=1 ttl=128 time=0.396 ms

  64 bytes from 192.168.221.1: icmp_seq=2 ttl=128 time=0.446 ms

  64 bytes from 192.168.221.1: icmp_seq=3 ttl=128 time=0.361 ms

  --- 192.168.221.1 ping statistics ---

  3 packets transmitted, 3 received, 0% packet loss, time 2000ms

  rtt min/avg/max/mdev = 0.361/0.401/0.446/0.034 ms

  root@sabproxy:~# ping ad.safesquid.test

  PING ad.safesquid.test (192.168.221.1) 56(84) bytes of data.

  64 bytes from 192.168.221.1: icmp_seq=1 ttl=128 time=0.262 ms

  64 bytes from 192.168.221.1: icmp_seq=2 ttl=128 time=0.358 ms

  64 bytes from 192.168.221.1: icmp_seq=3 ttl=128 time=0.442 ms

  ^C

  --- ad.safesquid.test ping statistics ---

  3 packets transmitted, 3 received, 0% packet loss, time 2000ms

  rtt min/avg/max/mdev = 0.262/0.354/0.442/0.073 ms
  -----------------------------------------------------------------------

:::note
ad.safesquid.test (192.168.221.1) >> Active Directory FQDN and IP Address
:::

**If you are unable to contact Active Directory you should face an error as shown below " Destination Host Unreachable"**

  -------------------------------------------------------------------------------
  root@sabproxy:~# ping 192.168.221.1
  -------------------------------------------------------------------------------
  PING 192.168.221.1 (192.168.221.1) 56(84) bytes of data.

  From 192.168.221.222 icmp_seq=31 Destination Host Unreachable

  From 192.168.221.222 icmp_seq=32 Destination Host Unreachable

  --- 192.168.221.1 ping statistics ---

  37 packets transmitted, 0 received, +6 errors, 100% packet loss, time 36269ms
  -------------------------------------------------------------------------------

