---
title: Profiling Engine
slug: /Profiling_Engine
description: Stop guessing who's doing what — profile every HTTP request by identity, application, content, and time for Zero Trust web security.
keywords:
  - SafeSquid profiling engine
  - web traffic profiling
  - identity-based access control
  - application signature detection
  - web categorization SafeSquid
  - content fingerprinting
  - zero trust web security
---


# Stop Guessing Who's Doing What — Profile Every Request

Your proxy sees thousands of requests per second: `https://cdn47.cloudprovider.com/a8f3d2e1`. Is that:
- Your CEO downloading an M&A contract? (Allow)
- A contractor uploading customer data to personal Dropbox? (Block + alert)
- Malware calling home, disguised as a CDN request? (Quarantine)

**Without profiling, every request is a mystery box.** You're forced to choose: block everything (users revolt) or allow everything (breaches happen).

**SafeSquid Profiling Engine solves this.** Every request is classified by:
- **Who:** User identity (LDAP, AD, SAML) + group membership
- **What:** Application signature (Zoom vs Tor vs ransomware C2)
- **When:** Time of day, day of week (lunch hour vs 2 AM)
- **Content:** MIME type, file extension, payload patterns (`.exe` pretending to be `.pdf`)

**Outcome:** Policies that match reality, not guesswork.



## Why Identity-Based Profiling Matters

**The anonymous insider problem:** When your proxy sees only IP addresses, a stolen laptop becomes indistinguishable from the CEO. A contractor on the guest network can exfiltrate the same data as a trusted admin. Without user identity, every security policy is a blunt instrument—block everyone or trust everyone.

**The encrypted application problem:** 90% of web traffic is HTTPS. TeamViewer, Tor Browser, Dropbox, and ransomware C2 servers all look the same to a firewall: encrypted TCP connections to cloud IPs. URL filtering fails because apps use CDN domains that rotate hourly.

**The timing problem:** Legitimate business use during work hours becomes data theft at 2 AM. Social media during lunch is acceptable; during client meetings, it's a distraction. Time-agnostic policies create false positives (blocking legitimate use) or false negatives (missing after-hours exfiltration).

**SafeSquid Profiling Engine solves all three:** Tie every HTTP request to a user and group. Detect applications by traffic fingerprints (TLS SNI, headers, payload patterns). Apply policies by time window. Inspect content for MIME type spoofing and payload threats.

**Result:** Granular Zero Trust policies like:
- **Finance team:** Full access to banking sites, block file upload to personal cloud storage
- **Contractors:** Block remote desktop apps (TeamViewer, AnyDesk), allow business SaaS
- **After-hours access:** Block all uploads >10MB, require manager approval for exceptions
- **Executives:** Bypass inspection for encrypted M&A discussions (specific domains only)



## What You Can Do with Profiling

✅ **Enforce Zero Trust policies:** Contractors can't access finance systems, even on the corporate network  
✅ **Block shadow IT:** Detect Dropbox, Telegram, Tor — even over HTTPS  
✅ **Stop data leaks:** SSN, credit cards, PHI detected in uploads → blocked before leaving the network  
✅ **Time-based access:** Social media allowed during lunch, blocked during work hours  
✅ **Detect disguised threats:** Files claiming to be PDFs but actually executables → quarantined  
✅ **Application control:** Allow Zoom for meetings, block Discord for unapproved chat



## How to Configure Profiling

### 1. [User Identities](/docs/Profiling_Engine/User_Identities/main/) — Connect LDAP/AD, Create Groups

**Your goal:** Tie every HTTP request to a user and group (Finance, IT, Contractors) so policies apply by identity, not just IP address.

**What you'll configure:**
- LDAP or Active Directory connection for user authentication
- User groups (e.g., Finance, IT, Contractors, Executives)
- Group membership rules (manual or LDAP attribute-based)

**When to use:** Required for any identity-based policy. If you only use IP-based rules, you can't distinguish between a CEO and a stolen laptop.

**⚠️ Common pitfall:** Don't rely on IP addresses for identity. Laptops roam, NAT pools rotate, VPNs mask IPs. Use user authentication (LDAP/SAML) or accept that your policies will break constantly.

→ [Configure User Identities](/docs/Profiling_Engine/User_Identities/main/)

---

### 2. [Web Categorization](/docs/Profiling_Engine/Web_Categorization/) — Assign Sites to Categories

**Your goal:** Block or allow websites by category (Social Media, Productivity, Malware, Adult Content) rather than maintaining endless URL lists.

**What you'll configure:**
- Built-in category database (YouTube = "Streaming Media", Facebook = "Social Networking")
- Custom categories for your organization (e.g., "Approved SaaS", "Competitor Sites")
- Category overrides (add specific domains to categories)

**When to use:** 
- ✅ Block broad categories (Social Media, Gaming, Adult Content) during work hours
- ✅ Allow only approved categories (Business, Productivity, Cloud Storage)
- ✅ Custom rules (allow LinkedIn for Sales team, block for everyone else)

**⚠️ Common pitfall:** Don't block "Cloud Storage" category without whitelisting your approved services (SharePoint, OneDrive). You'll break business workflows.

→ [Configure Web Categorization](/docs/Profiling_Engine/Web_Categorization/)

---

### 3. [Application Signatures](/docs/Profiling_Engine/Application_Signatures/) — Detect Apps by Traffic Fingerprints

**Your goal:** Block (or allow) specific apps even when they use HTTPS or non-standard ports: TeamViewer, Tor Browser, Dropbox, Discord, Zoom.

**What you'll configure:**
- Keyword signatures (TLS SNI, HTTP headers, payload patterns)
- Application detection rules (match app by traffic fingerprint)
- Per-app policies (block TeamViewer for contractors, allow for IT)

**When to use:**
- ✅ Block remote access tools (TeamViewer, AnyDesk) to prevent shadow IT
- ✅ Detect anonymization tools (Tor, Psiphon) to prevent policy bypass
- ✅ Allow Zoom/Teams, block Discord/Telegram (unapproved chat)

**Examples:**
- Block **TeamViewer** and **AnyDesk** for contractors, allow for IT staff
- Detect **Tor Browser** (anonymization) to prevent policy circumvention
- Allow **Zoom** and **Teams** but block **Discord** and **Telegram** (unapproved chat apps)

→ [Configure Application Signatures](/docs/Profiling_Engine/Application_Signatures/)

---

### 4. [Content Analyser](/docs/Profiling_Engine/Content_Analyser/main/) — Inspect Files, Text, Images

**Your goal:** Detect malware, data leaks, and inappropriate content by inspecting actual file content, not just the extension or URL.

**What you'll configure:**
- **True MIME Fingerprinting:** Detect `.exe` files renamed to `.pdf`
- **Text Analyser:** Scan uploads/emails for SSN, credit cards, keywords ("confidential")
- **Image Analyser (AI):** Detect inappropriate images, OCR text extraction from screenshots

**When to use:**
- ✅ Block executable downloads (`.exe`, `.msi`) except from approved software repos
- ✅ Detect MIME type spoofing (file named `report.pdf` but actually `application/x-executable`)
- ✅ DLP: Scan uploads for sensitive data (SSN, credit cards) before leaving network
- ✅ Block inappropriate images (NSFW content in file uploads)

**⚠️ Common pitfall:** Content analysis requires SSL inspection to be enabled. If you're not decrypting HTTPS, the Content Analyser can't inspect encrypted uploads.

→ [Configure Content Analyser](/docs/Profiling_Engine/Content_Analyser/main/)

---

### 5. [Request Profiles](/docs/Profiling_Engine/Request_Profiles/) — Control by HTTP Method, Protocol, User-Agent

**Your goal:** Enforce SafeSearch, block POST requests to unapproved sites, or restrict HTTP methods (DELETE, PUT) for read-only access.

**What you'll configure:**
- HTTP method filtering (GET, POST, PUT, DELETE)
- Protocol restrictions (HTTP vs HTTPS)
- User-agent detection (block automated scrapers, allow legitimate browsers)
- SafeSearch enforcement (rewrite Google/Bing queries to enable SafeSearch)

**When to use:**
- ✅ Enforce SafeSearch on Google, Bing, YouTube (prevent adult content in search results)
- ✅ Read-only mode for social media (allow GET, block POST to prevent comments/posts)
- ✅ Block non-browser user agents (scrapers, bots, automated tools)

→ [Configure Request Profiles](/docs/Profiling_Engine/Request_Profiles/)

---

### 6. [Response Profiles](/docs/Profiling_Engine/Response_Profiles/) — Filter by MIME Type, File Size

**Your goal:** Block executable downloads, enforce file size limits, or quarantine archives for malware scanning.

**What you'll configure:**
- MIME type filtering (block `application/x-executable`, allow `application/pdf`)
- File extension filtering (block `.exe`, `.msi`, `.bat`)
- File size limits (block downloads >100MB during business hours)
- Archive handling (quarantine `.zip`, `.rar` for ClamAV scanning)

**When to use:**
- ✅ Block executable downloads (`.exe`, `.msi`) except from approved software repos
- ✅ Enforce file size limits (block downloads >100MB during business hours)
- ✅ Quarantine archives for malware scanning (`.zip`, `.rar` → ClamAV before delivery)

**⚠️ When NOT to use:** Response Profiles fire after the download starts. For pre-emptive blocking (before bandwidth is consumed), use Request Profiles + URL filtering instead.

→ [Configure Response Profiles](/docs/Profiling_Engine/Response_Profiles/)

---

### 7. [Time Profiles](/docs/Profiling_Engine/Time_Profiles/) — Enforce Policies by Time Window

**Your goal:** Allow social media during lunch, block large downloads during business hours, or require manager approval for after-hours access.

**What you'll configure:**
- Time ranges (8:00-17:00 Mon-Fri, 12:00-13:00 daily)
- Time-based rules (block Social Media except lunch hours)
- Shift-based policies (different rules for day shift vs night shift)

**When to use:**
- ✅ Allow social media only during lunch (12:00-13:00)
- ✅ Block large downloads during business hours (to preserve bandwidth)
- ✅ Flag after-hours uploads as suspicious (potential data exfiltration)

**Example:** Allow Facebook/Twitter only during lunch hour (12:00-13:00), block rest of the day.

→ [Configure Time Profiles](/docs/Profiling_Engine/Time_Profiles/)



## ⚠️ Common Pitfalls

**1. Relying on IP addresses for identity**  
**What breaks:** Laptops switch networks, VPNs mask IPs, NAT pools rotate. Your "Finance team = 192.168.10.0/24" rule breaks when someone works from home.  
**Solution:** Use LDAP or SAML authentication. Configure [User Identities](/docs/Profiling_Engine/User_Identities/) before building IP-based rules.

**2. Blocking "Cloud Storage" without whitelisting approved services**  
**What breaks:** Your categorization rule blocks "Cloud Storage" — but that includes SharePoint, OneDrive, and Box (approved). Users can't access business files.  
**Solution:** Create custom categories: "Approved Cloud Storage" (SharePoint, OneDrive) and "Personal Cloud Storage" (Dropbox, Google Drive). Block the latter.

**3. Enabling Content Analyser without SSL Inspection**  
**What breaks:** 90% of uploads are over HTTPS. If SSL inspection is disabled, Content Analyser can't see the payload — it's encrypted.  
**Solution:** Enable [SSL Inspection](/docs/SSL_Inspection/) before relying on Content Analyser for DLP or malware detection.

**4. Over-blocking with application signatures**  
**What breaks:** You block "Remote Access" signatures, which includes TeamViewer, AnyDesk, Chrome Remote Desktop — but also your approved VPN client. IT can't work remotely.  
**Solution:** Use fine-grained application rules: block TeamViewer for contractors, allow for IT group. Test with a pilot group before rolling out.

**5. Time-based policies without testing time zones**  
**What breaks:** Your "lunch hour" rule is 12:00-13:00 in IST, but your US office is in PST. US users get social media blocked during their work hours.  
**Solution:** Use UTC for time profiles and calculate offsets for each office, or create separate time profiles per region.



## Related Topics

**Prerequisites:**
- [Authentication Setup](/docs/Authentication/main/) — User identities require LDAP, AD, or SAML authentication

**Next Steps:**
- [Access Restrictions](/docs/Access_Restriction/) — Use profiles to build allow/block policies
- [Data Leakage Prevention](/docs/Data_Leakage_Prevention/) — Combine Content Analyser with DLP templates

**Troubleshooting:**
- [User Not Identified](/docs/Troubleshooting/) — LDAP bind failures, group membership issues
- [Application Not Detected](/docs/Troubleshooting/) — Signature tuning, false positives

