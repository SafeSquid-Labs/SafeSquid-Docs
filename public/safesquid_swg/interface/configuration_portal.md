---
title: Policy Management Console
description: Administrative interface for defining, simulating, and enforcing SafeSquid access control, URL filtering, SSL inspection, and DLP policies.
keywords:
  - SafeSquid policy management
  - proxy policy console
  - web security administration
  - SafeSquid WebGUI
---


# Policy Management Console

The Policy Management Console (Configuration Portal) is the SafeSquid web interface for defining, simulating, and enforcing access control, URL filtering, SSL inspection, and DLP policies. Administrators use it to configure restriction profiles, real-time content security, authentication, and operational settings.

## Problems addressed

Operators need a single **authoritative** place to define Layer 7 policy, simulate or review impact, and push consistent rules to proxy nodes. Fragmented tooling increases misconfiguration risk and weakens audit narratives.

## Outcomes operators expect

- One console for restriction profiles, real-time content security, authentication, SSL inspection, and reports (paths in **Key Sections** below).
- Repeatable UI paths suitable for change control and screenshots in runbooks.
- A place where policy changes, interface access, and administrative actions can be traced for audit and investigation.

## Advantages vs “CLI-only” or multi-vendor policy stacks

SafeSquid ships the console **with** the SWG so policy and enforcement stay product-coupled. **Comparative** ease-of-use or feature parity vs other SWG consoles: **Missing (in-repo)**—no third-party matrix in this KB.

## Acquire, deploy, use

Install SafeSquid, reach the UI via **Access Methods** below, then follow linked sections (SSL Inspection, Authentication, Access Restriction) for each control.

## Access Methods

Access the interface from a browser configured to use SafeSquid as proxy:

- **Via proxy:** `http://safesquid.cfg/` (embedded Rest UI interface built into SafeSquid; accessible only when your client uses the proxy, but NOT resolved by SafeSquid's DNS resolver)
- **Direct access:** `https://SERVER-IP:8443/` (before proxy configuration or for troubleshooting)

**First-time setup:** See [Connect Your Client](/Connect_Your_Client) to configure your browser to use SafeSquid.

:::tip
**Login Credentials**

Default credentials after SAB installation: **administrator** / **safesquid**  
Change immediately after first login for security.

:::

---

## Key Sections

### 1. Restriction Profiles

Define access control rules by URL category, application signature, user/group, and time window.

**Location:** Sidebar → **Restriction Profiles** → **Access Restrictions**

**Use for:** 
- Block malicious sites and adult content
- Enforce work-hours internet access
- Allow specific applications while blocking others

**Details:** [Access Restriction](/Access_Restriction)

---

### 2. Real-Time Content Security

Configure deep content inspection: DLP, malware scanning, image analysis, and content modification.

**Location:** Sidebar → **Real Time Content Security**

**Use for:**
- Data leakage prevention (DLP)
- Malware scanning with ClamAV/ICAP
- Rewrite HTTP headers
- Block specific MIME types

**Details:** [Data Leakage Prevention](/Data_Leakage_Prevention), [Malware Scanners](/Malware_Scanners)

---

### 3. Authentication

Integrate with Active Directory, LDAP, or configure local users for identity-based policies.

**Location:** Sidebar → **Authentication**

**Use for:**
- User-aware access control
- SSO with Active Directory
- PAM authentication

**Details:** [Authentication](/Authentication)

---

### 4. SSL Inspection

Enable HTTPS decryption to inspect encrypted traffic for threats and policy violations.

**Location:** Sidebar → **SSL Inspection**

**Use for:**
- Inspect HTTPS traffic
- Deploy enterprise Root CA
- Selective decryption by category/user

**Details:** [SSL Inspection](/SSL_Inspection)

---

### 5. Reports & Logs

Access real-time logs, historical reports, and traffic analytics.

**Location:** Top menu → **Reports**

**Use for:**
- Audit trails and compliance
- User activity investigation
- Traffic pattern analysis

## Operational significance

The configuration portal matters for more than policy editing:

- it is the operational source of truth for many SafeSquid controls
- interface actions can become audit evidence through configuration and access logs
- misconfiguration here can affect authentication, SSL inspection, DLP, categorization, and reporting at once

Teams should treat changes in this interface as change-controlled events, not casual clicks.

---

## Navigation Tips

- **Top-right menu:** System settings, support, and logout
- **Sidebar:** Policy configuration sections
- **Top menu:** Reports, diagnostics, and system status
- **Apply button:** Save and apply configuration changes (restart required for some settings)

---

## Best Practices

1. **Test policies before enforcement:** Use simulation mode when available
2. **Document changes:** Use policy description fields for change tracking
3. **Back up configuration:** Use cloud sync or manual export before major changes
4. **Review logs regularly:** Check policy effectiveness and adjust as needed

## Verification and validation

After making a change in the portal, confirm all of the following:

- the expected policy behavior actually changed
- the change is recorded in the configuration or interface evidence path
- clustered nodes reflect the intended policy state if clustering is in use
- no unrelated controls were affected by the edit

## Troubleshooting

**Symptom:** A policy change appears saved, but behavior does not change.  
**Likely cause:** The change was not fully applied, did not match the expected rule path, or did not replicate.  
**Isolation:** Compare the saved configuration, active policy scope, and if relevant the cluster state.  
**Remediation:** Reapply the intended change and verify the correct rule order.  
**Retest:** Run the same request and confirm the new policy outcome.

**Symptom:** Operators cannot prove who changed policy.  
**Likely cause:** Configuration or interface evidence is not being reviewed or retained.  
**Isolation:** Check `config.log`, UI access logs, and the reporting path.  
**Remediation:** Retain and review the administrative evidence path.  
**Retest:** Make a controlled change and confirm it is recorded.

---

## Source register

| Topic | Status | Source |
| ----- | ------ | ------ |
| Policy Management Console / sidebar structure | **Confirmed** | This page (UI paths) |
| Default credentials **administrator** / **safesquid** | **Confirmed** | This page; change after first login |
| `safesquid.cfg` / **8443** access | **Confirmed** | This page, [Getting Started](/Getting_Started) |
| Comparative UI ease vs other SWGs | **Missing** | No SSOT in this KB |

---

## Next Steps

1. **[SSL Inspection](/SSL_Inspection)** — Enable HTTPS decryption
2. **[Authentication](/Authentication)** — Configure user authentication
3. **[Access Restriction](/Access_Restriction)** — Set up URL filtering and content policies
4. **[Troubleshooting](/Troubleshooting)** — Reference for common issues
