---
title: Block Personal Gmail, Allow Google Corporate Accounts
description: Block personal Gmail and allow only Google Workspace accounts in SafeSquid for productivity and data security.
keywords:
  - block personal gmail SafeSquid
  - allow google corporate accounts SafeSquid
  - block personal gmail accounts
  - corporate email restriction SafeSquid
  - safe web gateway gmail restriction
---


# Block Personal Gmail, Allow Google Corporate Accounts



## Problem: Personal webmail increases data and productivity risk

Organizations that use Google Workspace need to allow corporate Google accounts while blocking personal Gmail. Personal email on the office network consumes productive time and can create a path for leakage of confidential information. Many organizations use Google Corporate domains for mail; Gmail cannot be blocked entirely. SafeSquid SWG allows only configured corporate domains for Google sign-in and blocks personal Gmail.



## Key benefits

Corporate Google accounts continue to work for mail and Google services. Personal Gmail sign-in is blocked so users cannot use non-corporate accounts. Policy is enforced via header manipulation so only allowed domains are accepted by Google. Administrators list allowed domains (e.g. `corp.example.com`) in one place.



## Prerequisites

- [HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) enabled so SafeSquid can inspect and modify HTTPS traffic to Google.
- Access to SafeSquid Configuration Portal (Configure page).
- List of allowed Google Workspace domains (e.g. `corp.example.com`). Multiple domains are separated by comma with no space.



## Call to action

### Enable policy from Policies and Profiles section

Match requests to the Google Application policy first.

1. From SafeSquid Dashboard open **Configure** (top right).
2. Open **Policies and profiles** section.
3. Search for the default profile named **GOOGLE APPLICATION**.

![Search for the default policy GOOGLE APPLICATION](/img/How_To/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/image1.webp)

4. Edit and enable this policy.

![Edit and enable this policy](/img/How_To/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/image2.webp)

:::note
Administrators can add User Groups to restrict the policy to specific groups.
:::

### Enable policy from Header Filter section

Insert a header so only allowed domains are accepted by Google.

1. Open **Restriction Policies** (left panel).
2. Open **Privacy Control** submenu.
3. Open [Header Filter](/docs/Header_Obfuscation/main/) section. Ensure **Global** is **Enabled** **True**.

![Header filter under Restriction Policies](/img/How_To/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/image3.webp)

4. Open **Insert** tab.
5. Search for default profile **GOOGLE APPLICATION** (first rule).

![Insert tab and GOOGLE APPLICATION default profile](/img/How_To/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/image4.webp)

6. Edit and enable this rule. Add allowed domains in the value field (comma-separated, no space). Save the policy.

![Edit and enable rule; add allowed domains in value field and save](/img/How_To/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/image5.webp)

:::note
Multiple domains: separate each with a comma, no space.
:::



## Verification and Evidence

- **Block test:** Sign in to Google (e.g. mail.google.com) with a **personal** Gmail account through the proxy. Google returns an error template or message listing the allowed domains; sign-in is blocked.
- **Allow test:** Sign in with a **corporate** Google Workspace account (allowed domain). Sign-in succeeds and mail works.
- **Interface:** **Configure** → **Restriction Policies** → **Privacy Control** → **Header Filter** shows the GOOGLE APPLICATION Insert rule with the correct domain list. **Policies and profiles** shows GOOGLE APPLICATION enabled.
- **Audit:** Access logs and restriction logs show traffic to Google; export from the [Reporting Module](/docs/Audit_Forensics/Reporting_Module/) for evidence of policy enforcement.



## Troubleshooting

| Symptom | Likely cause | Resolution | Verification |
|--------|---------------|------------|--------------|
| Personal Gmail still works | HTTPS inspection off or Header Filter rule disabled/wrong | Enable HTTPS Inspection; enable Header Filter Insert rule; set value to allowed domains only (comma, no space) | Retry personal sign-in; confirm block |
| Corporate account blocked | Domain missing or typo in rule value | Add corporate domain to Insert rule value; check TLD and spelling | Sign in with corporate account |
| Google shows generic error | Expected when personal is blocked | None; message may list allowed domains | Confirm rule and profile applied to traffic |



## Next steps

- [Header Re-Write](/docs/Header_Obfuscation/main/) for header filtering and privacy controls.
- [Access Restriction](/docs/Access_Restriction/main/) for URL and category-based policies.
- [SSL Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) for HTTPS visibility and bypass rules.

