---
title: Access Mobile Applications Through SafeSquid
description: Control mobile app internet access through SafeSquid SWG with proxy enforcement and firewall-aware policies.
keywords:
  - mobile proxy settings SafeSquid
  - block mobile apps proxy
  - allow mobile apps through SafeSquid
  - SafeSquid mobile application access
  - proxy configuration for mobile devices
---


# Route mobile app traffic through SafeSquid proxy

When internet access is allowed only via a proxy, mobile applications must use proxy settings. Set the relevant environment variables or device proxy configuration so traffic goes through SafeSquid.



## Prerequisites
Most of mobile applications will not work without direct Internet connection (Means you have blocked the access to the IP address of the mobile on your firewall/router) to the mobile.

**What is direct INTERNET connection:**
If you are using firewall, then there is an option to block the Internet access to the specific IP addresses.
If you block the Internet connection to the specific IP addresses (which is client IP / Mobile IP addresses), on your firewall then you are unable to access the Internet without setting proxy settings in that client machine(or) mobile device.
By default all devices are allowed to access the Internet



## Working of Mobile Applications with Proxy
If there is no direct Internet access to the mobiles, and you configured proxy in the mobile, then some of the applications will work through proxy, as they designed such that to use proxy settings. And some of the applications will not work.

**why?**

Example:

IP of my mobile: 192.168.27.60

**Case 1: Direct Internet Connection Allowed for 192.168.27.60 on my firewall**

In this case it is not possible to block applications through proxy, even though you configured the mobile to use proxy settings and entries were created to block those applications.
Because the applications will not use the proxy settings, they use the direct access to send or receive messages.

**Case 2: Direct Internet Connection Blocked for 192.168.27.60 on my firewall**

In this case it is not possible to allow some of the applications to work with proxy, even though if you configure the proxy settings in the mobile. Because the applications not using proxy and looking for Internet access directly.       

:::note
Note: The same scenario is applicable in transparent mode also.
:::

