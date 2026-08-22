---
title: Integrated DNS Security
description: DNS security integration with DNSBL service to block malicious domain resolution and protect against DNS-based threats in SafeSquid.
keywords:
  - Secure Web Gateway Components
  - Integrated DNS Security
  - DNSBL Service
  - DNS threat protection
---


# Integrated DNS Security



## DNSBL service

For DNS Security, SafeSquid blocks the DNS resolution of malicious domains by integrating with the DNSBL service. When any user requests a domain or IP, SafeSquid queries the A record to the DNSBL service. DNSBL checks whether the IP or domain is associated with malicious or harmful traffic in its blacklist. If DNSBL flags the site as blacklisted, SafeSquid blocks access. For DNSBL, GeoIP, and homograph detection configuration, see [DNS Security](/docs/DNS_Security/main/).

