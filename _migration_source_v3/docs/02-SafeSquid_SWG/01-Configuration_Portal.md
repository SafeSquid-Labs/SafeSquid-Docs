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

## Access Methods

Access the interface from a browser configured to use SafeSquid as proxy:

- **Via proxy:** `http://safesquid.cfg/` (embedded Rest UI interface built into SafeSquid; accessible only when your client uses the proxy, but NOT resolved by SafeSquid's DNS resolver)
- **Direct access:** `https://SERVER-IP:8443/` (before proxy configuration or for troubleshooting)

**First-time setup:** See [Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/) to configure your browser to use SafeSquid.

:::tip Login Credentials

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

**Details:** [Access Restriction](/docs/Access_Restriction/main/)

---

### 2. Real-Time Content Security

Configure deep content inspection: DLP, malware scanning, image analysis, and content modification.

**Location:** Sidebar → **Real Time Content Security**

**Use for:**
- Data leakage prevention (DLP)
- Malware scanning with ClamAV/ICAP
- Rewrite HTTP headers
- Block specific MIME types

**Details:** [Data Leakage Prevention](/docs/Data_Leakage_Prevention/main/), [Malware Scanners](/docs/Malware_Scanners/main/)

---

### 3. Authentication

Integrate with Active Directory, LDAP, or configure local users for identity-based policies.

**Location:** Sidebar → **Authentication**

**Use for:**
- User-aware access control
- SSO with Active Directory
- PAM authentication

**Details:** [Authentication](/docs/Authentication/main/)

---

### 4. SSL Inspection

Enable HTTPS decryption to inspect encrypted traffic for threats and policy violations.

**Location:** Sidebar → **SSL Inspection**

**Use for:**
- Inspect HTTPS traffic
- Deploy enterprise Root CA
- Selective decryption by category/user

**Details:** [SSL Inspection](/docs/SSL_Inspection/main/)

---

### 5. Reports & Logs

Access real-time logs, historical reports, and traffic analytics.

**Location:** Top menu → **Reports**

**Use for:**
- Audit trails and compliance
- User activity investigation
- Traffic pattern analysis

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

---

## Next Steps

1. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Enable HTTPS decryption
2. **[Authentication](/docs/Authentication/main/)** — Configure user authentication
3. **[Access Restriction](/docs/Access_Restriction/main/)** — Set up URL filtering and content policies
4. **[Troubleshooting](/docs/Troubleshooting/main/)** — Reference for common issues

