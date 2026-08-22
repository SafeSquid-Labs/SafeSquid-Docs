---
title: Server Geo-Location
description: Configure SafeSquid SWG server geo-location profiles to enforce location-aware policies for access control, compliance, and routing optimization.
keywords:
  - SafeSquid SWG
  - server geolocation
  - geoip
  - country-based policy
  - geo-based access control
  - compliance
  - profiling engine
  - location-aware routing
  - ip intelligence
  - zero trust
---


# Server Geo-Location

Classify destination servers by country, region, and ASN (Autonomous System Number) to enforce location-aware access policies, meet data residency requirements, and block high-risk regions.

## Why use Server Geo-Location?

Without destination geography visibility, organizations cannot enforce regional restrictions or identify threat patterns by location. Server Geo-Location enables:

- **Data residency compliance:** Block traffic to non-compliant regions (GDPR, data sovereignty laws)
- **Threat mitigation:** Block high-risk countries or ASNs known for malicious activity
- **Audit evidence:** Logs show `server_country`, `server_region`, and `server_asn` for every connection
- **Usage analytics:** Report bandwidth consumption by destination geography

| Use Geo-Location When | Use Application Signatures Instead |
|------------------------|-------------------------------------|
| Enforcing regional data flow policies | Blocking specific apps (Facebook, TikTok) |
| Blocking high-risk countries (SOC directive) | Categorizing traffic by application type |
| Meeting compliance requirements (GDPR, export control) | Enforcing SaaS vs on-prem routing |
| Generating geo-based usage reports | Identifying zero-day apps by behavior |



## Prerequisites

- SafeSquid installed and operational (see [Getting Started](/docs/Getting_Started/main/))
- Profiling Engine enabled (see [Profiling Engine](/docs/Profiling_Engine/main/))
- Up-to-date GeoIP database (SafeSquid includes MaxMind GeoLite2 by default)
- Admin access to [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/)
- Consistent DNS resolution (see [Supporting Services: BIND](/docs/SafeSquid_SWG/Supporting_Services/Bind/))



## Configuration Steps

1. **Verify GeoIP database**  
   Navigate to **Profiling Engine** → **Server Geo-Location**  
   - Check that database status shows a recent update date
   - If outdated, update the database (see GeoIP database update instructions)

2. **Create geo-location profile**  
   Click **Add New** to create a profile:
   - **Name:** Descriptive identifier (e.g., `Block-High-Risk-Countries`, `EU-Only-Access`)
   - **Criteria:** Select countries, regions, or ASNs to match
   - **Action:** Specify whether to allow or block

3. **Save and verify**  
   Save the profile and confirm it appears in the profile list.  
   If multiple profiles overlap, check rule precedence (first-match-wins).

4. **Apply to policies**  
   Reference the geo-location profile in:
   - **Access Control:** Block/allow by destination country (see [Access Restriction](/docs/Access_Restriction/main/))
   - **Bandwidth Management:** Prioritize local regions (see [Manage Bandwidth](/docs/Performance_Accelerators/Manage_Bandwidth/))
   - **Reporting:** Build dashboards by destination geography (see [Reporting Module](/docs/Audit_Forensics/Reporting_Module/))

5. **Test with regional destinations**  
   Validate by accessing known sites hosted in target countries.



## Verification

- **Interface**: Profile visible, enabled, and referenced in policies.
- **Logs**: Confirm `server_country`, `server_region`, and `server_asn` in [Security Logs](/docs/Audit_Forensics/Security_Logs/).
- **Demonstrate control to auditor**: Export logs or run a report filtered by `server_country`; show policy configuration that denies or allows by geography; provide a country-based dashboard from the [Reporting Module](/docs/Audit_Forensics/Reporting_Module/) as evidence of active enforcement.
- **Curl test**:

```bash
# Test access to a site hosted in a specific country
curl -I https://example-regional-site.tld --proxy http://your-safesquid-proxy:8080
```

- Expected indicators in logs:

```text
timestamp=2025-11-10 action=deny module=access_restriction
server_ip=203.0.113.45 server_country=RU server_region=EU server_asn=AS12345
profile=Block-High-Risk-Countries rule=deny-non-compliant-regions user=jdoe
```

- Create a country-based dashboard and filter by `server_country` to validate reporting.



## Troubleshooting
- GeoIP database outdated
  - Symptom: `server_country` missing or incorrect
  - Fix: update GeoIP database; restart profiling service if required
- CDN or anycast endpoints
  - Symptom: destination resolves to global POP; country differs from brand site location.
  - Fix: allow-list CDNs by ASN where appropriate; use [Application Signatures](/docs/Profiling_Engine/Application_Signatures/).
- Private or RFC1918 destinations
  - Symptom: no geo data for non-routable IPs
  - Fix: add explicit policy exceptions; rely on identity or application profiles. See [User Identities](/docs/Profiling_Engine/User_Identities/main/).
- DNS-based variance
  - Symptom: different resolver returns regionally distinct IPs.
  - Fix: standardize resolvers; verify [Integrated DNS Security](/docs/SafeSquid_SWG/Integrated_DNS_Security/).
- IPv6 classification gaps
  - Symptom: missing geo for v6-only hosts
  - Fix: ensure IPv6 ranges in GeoIP; confirm dual-stack handling
- HTTPS SNI/IP mismatch
  - Symptom: SNI points to geo X, IP maps to geo Y
  - Fix: prefer IP-based geo for enforcement; validate SNI with server verification. See [SSL Inspection](/docs/SSL_Inspection/main/).
- Performance impact from complex geo sets
  - Symptom: latency on policy evaluation
  - Fix: consolidate countries into regions; push heavy rules higher in precedence; cache outcomes

External references:
- MaxMind GeoIP2 database: `https://dev.maxmind.com/geoip`
- Regional compliance baselines (example): `https://www.iso.org/standard/77312.html`

