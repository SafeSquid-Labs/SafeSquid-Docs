---
title: Allow Outlook to Work Through SafeSquid
description: Configure SafeSquid and firewall rules so Microsoft Outlook works with proxy authentication and SSL inspection enabled.
keywords:
  - allow outlook through proxy
  - SafeSquid outlook configuration
  - iptables rules for outlook
  - outlook with SSL inspection
  - SafeSquid authentication settings
---



## Problem: Outlook fails when proxy authentication or SSL inspection is enabled

MS Outlook often fails when SafeSquid has authentication (Negotiate or Basic) and/or SSL inspection enabled. SafeSquid is typically deployed behind a firewall that allows only ports 80 and 443; other traffic is blocked. Outlook uses not only HTTP/HTTPS but also SMTP(S), IMAP(S), POP(S), DNS (UDP), and LDAP (389, 636). Blocking those ports or failing to allow them through the firewall breaks Outlook.

Outlook supports proxy authentication (Negotiate and Basic) and SSL negotiation with a certificate deployed in Internet Explorer. The fix is to allow the necessary Outlook-related traffic (mail, DNS, LDAP, etc.) in the firewall or on the SafeSquid server and block the rest.



## Key benefits

Outlook works through SafeSquid with authentication and SSL inspection enabled. Mail flow continues without weakening proxy policy. Administrators can use iptables on the SafeSquid server or configure the organization firewall to allow the required ports.



## Prerequisites

- SafeSquid with authentication and/or SSL inspection enabled.
- Root or sufficient privilege to configure iptables on the SafeSquid server, or access to the organization firewall to allow the ports listed below.



## Call to action

The findings in allowing the Outlook traffic using the iptables rules are shown below:

This rule is to allow the established incoming connections to the server
```bash
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```
This rule is to allow the loopback connections to the server
```bash
iptables -A INPUT -i lo -m comment --comment "Allow loopback connections" -j ACCEPT
```
This rule is to allow the incoming ping requests to the server
```bash
iptables -A INPUT -p icmp -m comment --comment "Allow Ping to work as expected" -j ACCEPT
```
This rule is to allow the incoming connections on the following ports to the server, 22(SSH), **25(SMTP), 53(DNS), 110(POP), 389(LDAP), 587(SMTPS), 636(LDAPS), 953(RNDC), 993(IMAPS), 995(POP3S)
```bash
iptables -A INPUT -p tcp -m multiport --dports 22,25,53,110,389,465,587,636,953,993,995 -j ACCEPT
```
This rule is to allow the incoming connections on the following ports to the server, 1023(Reserved), **3268(MSGC), 3269(MSGCS), 5222(XMPP client connections), 5269(XMPP server-to-server), 5280(XMPP over synchronous HTTP), 8080(SafeSquid port)
```bash
iptables -A INPUT -p tcp -m multiport --dports 1023,3268,3269,5222,5269,5280,8080 -j ACCEPT
```
:::note
Note that both the above rules are one and the same excepting the ports. iptables will not allow us to add all the above-mentioned ports at one go, which is the reason to separate them into two rules
:::
This rule is to allow the incoming UDP connections to the server on the following ports, 53(DNS), 953(RNDC)
```bash
iptables -A INPUT -p udp -m multiport --dports 53,953 -j ACCEPT
```
This rule is to allow the established outbound connections from the server
```bash
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
```
This rule is to allow the loopback connections from the server
```bash
iptables -A FORWARD -i lo -m comment --comment "Allow loopback connections" -j ACCEPT
```
This rule is to allow the ping outside from the server
```bash
iptables -A FORWARD -p icmp -m comment --comment "Allow Ping to work as expected" -j ACCEPT
```
This rule is to allow the connections on the following ports from the server, 22(SSH), 25(SMTP), **53(DNS), 110(POP), 389(LDAP), 587(SMTPS), 636(LDAPS), 953(RNDC), 993(IMAPS), 995(POP3S)
iptables -A FORWARD -p tcp -m multiport --dports 22,25,53,110,389,465,587,636,953,993,995 -j ACCEPT**

This rule is to allow the connections on the following ports from the server, 1023(Reserved), 3268(MSGC), 3269(MSGCS), 5222(XMPP client connections), 5269(XMPP server-to-server), 5280(XMPP over synchronous HTTP), 8080(SafeSquid port)**
iptables -A FORWARD -p tcp -m multiport --dports 1023,3268,3269,5222,5269,5280,8080 -j ACCEPT**

This rule is to allow the UDP connections from the server on the following ports 53(DNS), 953(RNDC)
```bash
iptables -A FORWARD -p udp -m multiport --dports 53,953 -j ACCEPT
```
This rule is to DROP the remaining input traffic to the server
```bash
iptables -P INPUT DROP
```
This rule is to drop the forward output traffic from the server
```bash
iptables -P FORWARD DROP
```
The above iptables rules are enough for Outlook to work in an environment where authentication and/or SSL inspection in SafeSquid are enabled.

