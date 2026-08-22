---
title: PAM Authentication
description: Configure PAM (Pluggable Authentication Modules) integration with SafeSquid for system-level authentication.
keywords:
  - PAM authentication
  - SafeSquid PAM
  - Pluggable Authentication Modules
  - system authentication proxy
---

# PAM Authentication

PAM integration validates proxy users against the system's Pluggable Authentication Modules (PAM) stack. This allows you to use a single set of credentials for both OS-level access (SSH, Login) and proxy access.

## When to use PAM Authentication

| Use PAM Authentication When | Use Directory Services Instead |
|-----------------------------|--------------------------------|
| SafeSquid is running on Linux/Unix | Primary identity is in Active Directory |
| You want to use local OS users | You need Single Sign-On (SSO) |
| System already uses PAM for LDAP/Radius | Best user experience for domain PCs |

:::info Prerequisites
- SafeSquid running on a PAM-capable operating system (typically Linux).
- OS users and passwords already configured.
- Admin access to the SafeSquid [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/).
:::

## Enable PAM in Access Rules

1. **Access Configuration:** Open the [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/) and click **Configure**.
2. **Navigate to Allow List:** **Application Setup** → **Access Restrictions** → **Allow List**.
3. **Configure Rule:**
   - Edit the entry that matches your client segment.
   - **PAM Authentication:** Set to **TRUE**.
   - **Username/Password:** Leave these empty (we are using OS PAM, not local SafeSquid credentials).
4. **Save and Apply:** Click the checkmark to save.

:::tip Note on Local Users
If you create a user via `useradd` on the Linux host, SafeSquid will be able to authenticate them once PAM is set to TRUE.
:::

## Verification

| Action | Method | Expected Result |
|--------|--------|-----------------|
| **Test Login** | Access a website from a client. | A browser login prompt appears; enter Linux OS credentials. |
| **Check Logs** | `tail -f /var/log/safesquid/identity.log` | Shows the OS username for each authenticated request. |
| **Verify Rule** | Check **Access Restrictions** → **Allow List**. | The rule shows **PAM Authentication** is **TRUE**. |

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Authentication prompt does not appear | Rule mismatch | Ensure the rule matches the client IP and is placed high enough in the Allow List. |
| OS credentials rejected | PAM stack mismatch | Verify the system PAM configuration (e.g., `/etc/pam.d/safesquid`) if it exists, or ensure the global PAM service is working. |
| Login prompt repeats | Incorrect credentials | Verify the user exists on the Linux host and the password is correct. |

## Next steps

- [Local Credential Store (BASIC)](/docs/Authentication/BASIC/) for SafeSquid-only users.
- [Directory Services](/docs/Authentication/Directory_Services/main/) for enterprise identity integration.
- [Bypass Authentication](/docs/Authentication/Bypass_Authentication/) for services that cannot authenticate.
