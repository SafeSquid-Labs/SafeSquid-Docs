---
title: Upgrade SafeSquid
slug: /Upgrade_SafeSquid
description: Upgrade SafeSquid SWG via OS upgrade or version upgrade for stability, security, and new features.
keywords:
  - SafeSquid upgrade
  - OS upgrade SafeSquid
  - version upgrade SafeSquid
  - SafeSquid update
---


# Upgrade SafeSquid application or OS

Administrators can upgrade SafeSquid SWG in two ways: OS upgrade (when the underlying OS must be updated) or version upgrade (when only the SafeSquid application is updated). The documents below describe each path and when to use it.



## Upgrade guides

### [OS Upgrade](/docs/Upgrade_SafeSquid/OS_Upgrade/main/)
The base OS may reach end-of-life or lack kernel and library versions required by newer SafeSquid. OS Upgrade documents non-interactive upgrade of the host (e.g. Ubuntu 20.04 to 24.04) so SafeSquid remains supported and secure. Configuration is retained and restored after the system upgrade. Follow the OS Upgrade document when the OS must be modernized.

### [Version Upgrade](/docs/Upgrade_SafeSquid/Version_Upgrade/main/)
SafeSquid software updates deliver bug fixes, security patches, and new features. Version Upgrade describes upgrading the SafeSquid application via the Support page and tarball upload while keeping the OS unchanged. Monit restarts the service after upload. Follow the Version Upgrade document to update SafeSquid when the OS is already current.

## Next steps

After upgrade, verify with [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/) and [Troubleshooting](/docs/Troubleshooting/main/) if issues appear.
