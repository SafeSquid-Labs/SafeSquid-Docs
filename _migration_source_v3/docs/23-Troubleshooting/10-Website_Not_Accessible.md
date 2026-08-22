---
title: Website Not Accessible
description: "Troubleshoot website connection failures through SafeSquid: DNS resolution, port connectivity, and internal DNS checks."
keywords:
  - SafeSquid connection failed
  - website not loading through proxy
  - SafeSquid DNS troubleshooting
  - telnet SafeSquid port check
  - SafeSquid unable to connect to website
  - proxy website connection failure
  - SafeSquid no route to host
  - nslookup proxy connection issue
  - bind9 DNS configuration SafeSquid
  - conditional DNS forwarding
---



## Connection failed to proxy or origin
When the user accesses the website, the browser displays "**Connection to 192.168.27.30:80 failed**". When the user accesses https://abc.safesquid.com/ via proxy and logs in with a corporate email ID, the browser may show "**Connection to abc.safesquid.com:443 failed**".

![Error showing "Connection to abc.safesquid.com:443 failed"](/img/Troubleshooting/Connection_failure_to_websites/image1.webp)



## Possible causes
The destination website may be down, or the user may be unable to reach the site because of internet slowness.



## Troubleshooting
### Website or origin unreachable

Check whether the website is opening without proxy configuration inside the browser (No proxy in the middle).

If the website is not opening without a proxy, then it is not the problem with SafeSquid.

If it is opening without a proxy, then run the below command to verify whether the website is resolving or not.

```jsx title="Command"
nslookup 192.168.27.30
```
**To check SafeSquid server is connecting to** 192.168.27.30 on port 80

```jsx title="Command"
telnet WEBSITE PORT_TO_CONNECTON
```
When the website cannot be reached, example output:

telnet 192.168.27.30 80

Trying 192.168.27.30...

telnet: Unable to connect to remote host: No route to host

When the website is reachable, the output is:

> telnet WEBSITE PORT_TO_CONNECTON

When the website cannot be reached:

```jsx title="Command"
telnet 192.168.27.30 80
```
When the website can be reached:

root@dev:~# telnet 192.168.27.30 80

Trying 192.168.27.30...

Connected to 192.168.27.30.

Escape character is '^]'.

### On-premises with directory services (conditional DNS)

When the server is in an on-premises environment with directory services, the directory DNS server performs DNS resolution.

To check the configuration on the local internal network and its address record pointed on an active directory (AD) or local DNS server.

Run the below commands on the command prompt for **abc.safesquid.com**

```jsx title="Command"
nslookup abc.safesquid.com
```
If the website is resolving to the local internal network **e.g.** (10.10.11.78,10.10.128.106)

Configure conditional forwarding to the SafeSquid local caching DNS server.

Go to the path: **/etc/bind/**

and create a file.

```jsx title="Command"
vim named.conf
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

```jsx title="Command"
cd /etc/bind/
```
And create a file

```jsx title="Command"
vim abc.safesquid.co
```
Add below lines

```
zone "abc.safesquid.com" {
type forward;
forwarders {10.10.124.101;};
};
```

Command to restart bind9 service:

```jsx title="Command"
/etc/init.d/bind9 restart
```
Verify whether the website is resolving to the local IP successfully or not.

