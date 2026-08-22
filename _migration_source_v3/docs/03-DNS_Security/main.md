---
title: DNS Security
slug: /DNS_Security
description: SafeSquid's DNS-level security features including DNSBL, GeoIP filtering, and homograph attack detection.
keywords:
  - SafeSquid DNS security
  - DNSBL
  - GeoIP
  - homograph detection
---


# DNS Security

SafeSquid provides DNS-level security at the domain resolution layer. Features include DNS-based blacklisting, geographic IP filtering, and detection of internationalized domain name (IDN) homograph attacks. For how DNS security fits into the SafeSquid SWG architecture, see [Integrated DNS Security](/docs/SafeSquid_SWG/Integrated_DNS_Security/).

```mermaid
flowchart LR
    Client[Client Request] --> SafeSquid[SafeSquid Proxy]
    SafeSquid --> DNS[DNS Resolution]
    DNS --> DNSBL[DNSBL Check]
    DNSBL --> GeoIP[GeoIP Check]
    GeoIP --> Homograph[Homograph Check]
    Homograph --> Allow[Allow]
    Homograph --> Block[Block]
```

**Why DNS-level security matters:** Blocking threats at DNS resolution (before connection) is faster and more efficient than content inspection. DNS security provides early threat mitigation, reduces bandwidth waste, and creates audit evidence before users reach malicious sites.



## DNS security controls and configuration

### [DNS Blacklisting](/docs/DNS_Security/DNSBL/)
Unrestricted DNS resolution allows access to known-malicious domains and increases malware, phishing, and compliance risk. DNSBL blocks dangerous sites before connection by querying DNS-based blacklist services. Blocking at resolution reduces exposure and supports audit evidence in logs and reports. Configure DNSBL in Real-time content security and verify blocks in Security Logs.

### [Server Geo-Location](/docs/DNS_Security/GeoIP/)
Organizations face regional compliance gaps and threat exposure when destination geography is unknown. Server Geo-Location classifies destinations by country and ASN for location-aware policies. Country-based access control and reporting support data residency and geo-restriction requirements. Enable geo profiles in Profiling Engine and reference them in Access Restriction and Reporting.

### [Homograph Detection](/docs/DNS_Security/Homograph_Detection/)
IDN homograph attacks use visually similar characters to impersonate legitimate domains and enable phishing. Homograph detection identifies and blocks these impersonation attempts at DNS resolution. The control reduces lookalike-domain risk and supports evidence in DNS security logs. Configure allowed or blocked IDN patterns in DNS Security when the feature is available.

## Next steps

Use DNS security together with [Access Restriction](/docs/Access_Restriction/main/) and [Profiling Engine](/docs/Profiling_Engine/main/) for URL and application policy; see [Integrated DNS Security](/docs/SafeSquid_SWG/Integrated_DNS_Security/) for architecture context.
