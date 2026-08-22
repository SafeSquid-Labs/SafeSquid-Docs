---
title: Data Leakage Prevention
slug: /Data_Leakage_Prevention
description: Catch data leaks before they become breaches — detect SSN, credit cards, PHI in uploads and block them in real time.
keywords:
  - data leakage prevention
  - SafeSquid DLP
  - compliance templates
  - sensitive data detection
  - PCI DSS HIPAA GDPR compliance
  - data exfiltration prevention
---


# Catch Data Leaks Before They Become Breaches

**The scenario:** A sales rep emails a spreadsheet to their personal Gmail. Inside: 10,000 customer credit card numbers. By the time you find out, it's been forwarded three times and posted to Pastebin.

**The cost:** $4.45M average breach (IBM, 2024). GDPR fine: up to €20M or 4% of revenue. PCI-DSS non-compliance: lose ability to process cards. Board wants answers.

**The problem:** Your users handle sensitive data daily — SSN, PHI, credit cards, trade secrets. Email, file uploads, social media posts — every channel is a potential leak. You can't inspect laptops after-the-fact; you need to **stop data at the exit point**, in real time.

**SafeSquid DLP sits at your network perimeter**, inspecting every byte before it leaves:
- **Text Analyser** scans uploads, emails, social posts for credit cards, SSN, PHI, keywords
- **Image Analyser** extracts text from screenshots (OCR), detects PII in photos
- **Compliance Templates** provide pre-built rules for PCI-DSS, HIPAA, GDPR
- **Real-time enforcement:** Block, log + alert, or quarantine for manager approval

**Outcome:** Data exfiltration attempts are caught before they become breaches. Compliance auditors get proof you're monitoring egress.



## Before/After SafeSquid DLP

| Scenario | Without DLP | With SafeSquid DLP |
|----------|-------------|---------------------|
| Rep emails customer list to personal Gmail | ❌ No visibility, discovered in audit 6 months later | ✅ **Blocked** — SSN pattern detected in attachment, manager notified, SIEM alert fired |
| Contractor uploads pricing spreadsheet to personal Dropbox | ❌ Data exfiltrated, posted to competitor website | ✅ **Quarantined** — "confidential" keyword detected, manager approval required before release |
| Engineer posts AWS credentials to public GitHub gist | ❌ Credentials harvested in minutes, crypto miner deployed on EC2 | ✅ **Blocked** — API key pattern detected in POST body, SIEM alert, security review triggered |
| Finance team shares SSN spreadsheet on Slack (external workspace) | ❌ Legal discovers it 8 months later during e-discovery | ✅ **Blocked** — 9-digit SSN pattern detected, upload fails with "Policy Violation: PII Detected" message |



## How SafeSquid DLP Works

SafeSquid sits between your users and the internet, inspecting **every byte** before it leaves:

### 1. Text Analyzer Scans for Patterns

Scans uploads, emails, social posts, form submissions for:
- **Credit card numbers:** Visa, Mastercard, Amex (PCI-DSS compliance)
- **Social Security Numbers:** 9-digit SSN format (HIPAA, GDPR)
- **Protected Health Information:** Patient IDs, diagnosis codes, medical record numbers
- **Keywords:** "confidential," "internal only," "DO NOT SHARE," "proprietary"
- **Custom patterns:** Your proprietary data formats (internal employee IDs, product codes)

**How it works:** Regular expression (regex) matching against content. When a match is found, the configured action triggers (block, log, quarantine).

→ [Configure Text Analyser](/docs/Profiling_Engine/Content_Analyser/Text_Analyser/)

### 2. Image Analyzer Detects Visual Content

Inspects images in uploads and attachments:
- **OCR text extraction:** Finds SSN or credit cards in scanned documents, screenshots
- **Facial recognition:** Detects PII in employee photos (optional, requires AI model)
- **Explicit content detection:** Blocks NSFW uploads to corporate Slack, SharePoint

**Use case:** Employee screenshots customer data from internal CRM, uploads to personal cloud storage. Image Analyzer extracts text via OCR, detects SSN, blocks upload.

→ [Configure Image Analyser](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/)

### 3. Compliance Templates Provide Pre-Built Rules

No need to write regex from scratch. SafeSquid includes templates for:
- **PCI-DSS:** Credit card data (Visa, Mastercard, Amex, Discover)
- **HIPAA:** PHI (patient IDs, medical record numbers)
- **GDPR:** PII (names + addresses + SSN/passport combos)
- **Custom:** Your organization's proprietary data patterns

**How to use:** Load template → Test with dummy data → Enable blocking.

→ [Load Compliance Templates](/docs/Data_Leakage_Prevention/Compliance_Templates/)

### 4. Real-Time Enforcement

When SafeSquid detects sensitive data, you choose the action:

**Block (recommended for high-risk data):**
- Upload fails immediately
- User sees: "Policy Violation: PCI Data Detected. Contact IT Security."
- SIEM alert fired
- Manager notified

**Log + Alert (for low-risk or testing):**
- Upload proceeds, but logged
- SIEM gets alert for security review
- Useful during tuning phase (identify false positives)

**Quarantine (for ambiguous cases):**
- File held in quarantine
- Manager receives approval request with file preview
- Manager can release or permanently block
- Audit trail maintained



## When to Use DLP

✅ **Your industry requires it:**  
Healthcare (HIPAA), finance (PCI-DSS, SOX), government (ITAR, FedRAMP), retail (PCI-DSS)

✅ **You handle customer PII:**  
Names, addresses, SSN, payment info, medical records, passport numbers

✅ **You have trade secrets:**  
Source code, formulas, M&A documents, pricing strategies, customer lists

✅ **Compliance audit coming:**  
Auditors want proof you're monitoring data egress. DLP logs export to SIEM for evidence.

✅ **Recent breach or close call:**  
Board mandates "we need to prevent the next incident." DLP provides technical controls + audit trail.



## When NOT to Use DLP (Alone)

⚠️ **DLP is not endpoint protection:**  
If data is already on a USB drive, laptop, or personal phone, network DLP won't catch it. Combine with endpoint DLP (Microsoft Purview, Symantec DLP, Forcepoint).

⚠️ **DLP is not encryption:**  
Data in transit to approved services (SharePoint, OneDrive, Salesforce) should still be encrypted. DLP blocks *unapproved* channels, not all channels.

⚠️ **DLP creates false positives:**  
Credit card regex matches test data (`4111111111111111` is a test Visa number). Don't enable hard blocking on day one. Start with **log-only mode** for 2 weeks, tune patterns, then enable blocking.

⚠️ **DLP needs SSL inspection:**  
90% of uploads are over HTTPS. If SSL inspection is disabled, DLP can't see the payload — it's encrypted. Enable SSL inspection first.



## How to Configure DLP

### Step 1: Enable SSL Inspection (Required)

DLP can't inspect encrypted uploads without SSL inspection. 90% of web traffic is HTTPS.

**Action:** [Enable SSL Inspection](/docs/SSL_Inspection/) and deploy the Root CA to client devices.

**Verification:** Visit an HTTPS site and confirm the certificate is issued by SafeSquid-Root-CA (not the website's original cert).

---

### Step 2: Load Compliance Templates

Pre-built regex patterns for PCI-DSS, HIPAA, GDPR.

**Action:** [Load Compliance Templates](/docs/Data_Leakage_Prevention/Compliance_Templates/) in the Text Analyser configuration.

**What you'll get:**
- Credit card patterns (Visa: `^4[0-9]{12}(?:[0-9]{3})?$`, Mastercard, Amex)
- SSN pattern: `^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$`
- Custom keyword lists: "confidential," "proprietary," "internal only"

---

### Step 3: Configure Text Analyser

Enable content scanning in uploads, emails, form submissions.

**Action:** [Configure Text Analyser](/docs/Profiling_Engine/Content_Analyser/Text_Analyser/)

**Settings to configure:**
- **Scan scope:** Uploads, emails, POST bodies, social media posts
- **Pattern matching:** Enable compliance templates (PCI, HIPAA, GDPR)
- **Action on match:** Block, log + alert, or quarantine
- **Exclusions:** Whitelist approved file transfer services (e.g., SFTP to partner)

---

### Step 4: Link DLP to Access Restrictions

DLP detections must trigger enforcement actions (block, log, quarantine).

**Action:** [Configure Access Restrictions](/docs/Access_Restriction/) with DLP profile matching.

**Example rule:**
- **If:** Text Analyser detects PCI data (credit card pattern)
- **Then:** Block upload + log to SIEM + notify manager
- **Except:** Allow if destination is approved payment processor (e.g., Stripe API)

---

### Step 5: Set Up SIEM Integration

Send DLP alerts to your SIEM (Splunk, QRadar, Wazuh) for security monitoring.

**Action:** [Configure SIEM Integration](/docs/Integrations/) with syslog forwarding.

**What gets logged:**
- Timestamp, user identity, source IP
- Detected pattern (e.g., "SSN detected in upload to gmail.com")
- Action taken (blocked, logged, quarantined)
- File hash (SHA256) for forensics

---

### Step 6: Test with Dummy Data

Don't enable blocking in production without testing. False positives will break workflows.

**Action:** Create test files with fake sensitive data:
- Fake SSN: `123-45-6789` (invalid SSN, but matches pattern)
- Test Visa card: `4111111111111111` (official test number, won't process)
- Keyword test: Text file with "CONFIDENTIAL - DO NOT SHARE"

**Upload to personal Gmail, Dropbox, etc. Verify:**
- ✅ SafeSquid blocks or logs the upload
- ✅ SIEM receives alert
- ✅ User sees policy violation message

**Tune patterns to reduce false positives** (e.g., exclude test credit card numbers).

Once tuning is complete, enable blocking for real data.



## ⚠️ Common Pitfalls

**1. Enabling DLP without SSL inspection**  
**What breaks:** 90% of uploads are HTTPS. DLP can't inspect encrypted traffic.  
**Solution:** [Enable SSL Inspection](/docs/SSL_Inspection/) first, deploy Root CA to clients, then enable DLP.

**2. Blocking too aggressively on day one**  
**What breaks:** False positives block legitimate business workflows. Finance team can't email invoices (credit card-like numbers in invoice IDs).  
**Solution:** Start with **log-only mode** for 2 weeks. Review SIEM alerts, tune regex patterns, whitelist false positives. Then enable blocking.

**3. Forgetting compressed files**  
**What breaks:** User uploads `customer_data.zip` with 10,000 SSNs inside. DLP sees a ZIP file, not the contents.  
**Solution:** Enable [archive decompression](/docs/Content_Modifier/) in Content Modifier. SafeSquid will extract and scan ZIP/RAR contents before allowing upload.

**4. Not whitelisting approved data channels**  
**What breaks:** You block all credit card uploads. But your payment team needs to upload transaction files to Stripe. Legitimate business stops.  
**Solution:** Create exception rules in Access Restrictions: "Allow credit card uploads to stripe.com API endpoint only."

**5. Ignoring image-based data leaks**  
**What breaks:** User screenshots customer SSN from CRM, uploads image to personal cloud. DLP only scans text, misses image uploads.  
**Solution:** Enable [Image Analyser with OCR](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/) to extract text from images.



## Related Topics

**Prerequisites:**
- [SSL Inspection](/docs/SSL_Inspection/) — Required to inspect encrypted uploads (90% of traffic)
- [Authentication](/docs/Authentication/main/) — User identity needed for per-user DLP policies

**Next Steps:**
- [Text Analyser Configuration](/docs/Profiling_Engine/Content_Analyser/Text_Analyser/) — Fine-tune regex patterns
- [Image Analyser (AI-powered)](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/) — OCR for screenshots
- [Access Restrictions](/docs/Access_Restriction/) — Link DLP detections to block/log actions
- [SIEM Integration](/docs/Integrations/) — Forward DLP alerts to Splunk, QRadar, etc.

**Troubleshooting:**
- [DLP False Positives](/docs/Troubleshooting/) — How to tune regex patterns, whitelist test data

**Use Cases:**
- [Block Personal Gmail, Allow Corporate](/docs/Use_Cases/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/) — Prevent data leaks via personal email
- [Block Keywords in Uploads](/docs/Use_Cases/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/) — Detect "confidential" in social posts

Uncontrolled data exfiltration drives regulatory fines (e.g. GDPR up to €20M, PCI-DSS loss of card processing), breach costs (average $4.45M), and reputational damage. SafeSquid DLP detects and blocks sensitive data (PII, PHI, payment card data) in real time at the network perimeter. DLP logs export to SIEM; violation reports are auditor-ready. Every block or alert includes timestamp, user, detected pattern, action taken, and file hash. Plan 1–2 weeks for deployment and tuning; then quarterly pattern review and SIEM alert monitoring.

