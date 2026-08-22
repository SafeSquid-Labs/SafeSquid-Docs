---
title: Block Advertisements And Banners
description: Block ads and banners in SafeSquid to improve load time, security, and bandwidth and reduce distractions.
keywords:
  - block advertisements SafeSquid
  - block banners SafeSquid
  - secure web gateway ads blocking
  - SafeSquid ad blocking configuration
  - ads and banners blocking SafeSquid
---


# Block advertisements and banners



## Ads create security risk, waste bandwidth, and hurt user experience

Ad networks can deliver malware, tracking, and unwanted scripts; ads also increase load time and bandwidth use. Blocking ads at the gateway reduces exposure to ad-based threats, improves performance, and supports acceptable-use policy. SafeSquid BLOCK ADVERTISEMENT policy replaces ad content with a configurable template so users see cleaner pages without client-side ad blockers.



## Key benefits

Reduces malware and tracking exposure from ad networks. Lowers bandwidth and CPU use. Cleaner pages with fewer distractions. Evidence for auditors: policy is visible in **Configure** → **Access Profiles** (or **Templates**); access logs show traffic that matched the policy. **Limitation:** Some sites may break if they depend on specific ad endpoints; use bypass or allow rules for exceptions.



## Prerequisites

**SafeSquid-side:** HTTPS Inspection enabled so SafeSquid can inspect and modify HTTPS content. See [Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) if not yet enabled. Admin access to the Configuration Portal.

**Client-side:** No change required; blocking is transparent.



## Enable BLOCK ADVERTISEMENT policy

1. Access the SafeSquid interface via the [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/) — web interface for policy and system settings. In the interface header, click **Configure** to open the configuration menu.

![Configuration Portal header with Configure menu highlighted](/img/How_To/Block_Advertisements_And_Banners/image1.webp)

2. In **Access Profiles** (or **Templates**), use the search box to find the default policy; search for **BLOCK ADVERTISEMENT**.

![Search box in Access Profiles or Templates list](/img/How_To/Block_Advertisements_And_Banners/image2.webp)

![Search for BLOCK ADVERTISEMENT default policy](/img/How_To/Block_Advertisements_And_Banners/image3.webp)

3. Open the policy: click **Edit** on the BLOCK ADVERTISEMENT row to open the policy editor. Set **Enabled** to **TRUE**, then click **Save** (or the equivalent save control in the policy section) to save the policy.

![Edit button on the BLOCK ADVERTISEMENT policy row](/img/How_To/Block_Advertisements_And_Banners/image4.webp)

![Enabled toggle set to TRUE in the policy form](/img/How_To/Block_Advertisements_And_Banners/image5.webp)

![Save button to persist the policy changes](/img/How_To/Block_Advertisements_And_Banners/image6.webp)

4. Alternatively, enable from **Templates** in custom settings: open the BLOCK ADVERTISEMENT template, set **Enabled** to **TRUE**, and save.

![Enable BLOCK ADVERTISEMENT from Templates in custom settings](/img/How_To/Block_Advertisements_And_Banners/image7.webp)

![Set Enabled to True in template](/img/How_To/Block_Advertisements_And_Banners/image8.webp)

![Save the template](/img/How_To/Block_Advertisements_And_Banners/image9.webp)



## Verification and Evidence

- **Interface:** **Configure** → **Access Profiles** (or **Templates**) shows BLOCK ADVERTISEMENT with **Enabled** TRUE.
- **Traffic:** Open a site that normally shows ads (e.g. https://www.youtube.com/); ads should be replaced by the SafeSquid template.

![Blocked ad replaced by SafeSquid template on YouTube](/img/How_To/Block_Advertisements_And_Banners/image10.webp)

- **Audit:** Access logs and reports show traffic matching the policy; export reports from the [Reporting Module](/docs/Audit_Forensics/Reporting_Module/) for evidence.

:::note
Administrators can replace the default template with a custom template.
:::



## Troubleshooting

| Symptom | Likely cause | Resolution | Verification |
|--------|---------------|------------|--------------|
| Ads still visible | HTTPS Inspection not enabled or policy not applied | Enable HTTPS Inspection; ensure BLOCK ADVERTISEMENT is enabled and profile applied to the connection | Reload page; confirm template replaces ads |
| Site broken or login fails | Site depends on blocked ad domain | Add bypass or allow rule for that domain or path | Retest site after rule change |
| Policy not in list | Default policies not loaded | Restore defaults or contact support for policy set | Search again in Access Profiles |



## Next steps

- [Block inappropriate images using Image Analyzer](/docs/Use_Cases/Block_inappropriate_images_by_using_Image_Analyzer/) for visual content filtering.
- [Header Re-Write](/docs/Header_Obfuscation/main/) for header filtering and privacy.
- [Content Modifier](/docs/Content_Modifier/main/) for custom regex-based content rewriting.

