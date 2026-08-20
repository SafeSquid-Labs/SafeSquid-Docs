---
title: SafeSquid Ubuntu OS Upgrade from 20.04 to 24.04 Guide
slug: /Upgrade_SafeSquid/OS_Upgrade
description: "Non-interactive upgrade of SafeSquid SWG from Ubuntu 20.04 LTS to 24.04 LTS: prerequisites, OS upgrade, DNS, Netplan, and verification."

keywords:
  - SafeSquid upgrade guide
  - Upgrade Ubuntu for SafeSquid
  - SafeSquid 2025 installation
  - SafeSquid SWG OS compatibility
  - Non-interactive SafeSquid upgrade
  - SafeSquid service continuity
  - SafeSquid system prerequisites
  - SafeSquid DNS and Netplan setup
---


# Upgrade Ubuntu 20.04 to 24.04 for SafeSquid compatibility



## OS upgrade scope and procedure

Use this step-by-step, non-interactive procedure to upgrade the SafeSquid Secure Web Gateway system from Ubuntu 20.04 LTS to Ubuntu 24.04 LTS, then to SafeSquid version 2025.1001.1232.3.

The steps ensure **compatibility**, **security**, and **service continuity** for SafeSquid deployments running in production environments.

---



## Why This Upgrade Is Required

### **1. SafeSquid Compatibility Requirements for** The latest release:

**SafeSquid Secure Web Gateway 2025.1001.1232.3**

introduces the following **minimum system requirements**:

- **Linux Kernel:** 6.8 or higher
- **glibc:** 2.39 or higher

Ubuntu **20.04 LTS** includes:

- Kernel up to **5.15**
- glibc **2.31**

These versions are **too old** for SafeSquid verion 2025.1001.1232.3, which requires newer kernel APIs and library functions available only in **Ubuntu 24.04 LTS**.
Attempting to install the new version on 20.04 will cause dependency and runtime failures.

---

### **2. Ubuntu 20.04 End of Life (EoL)**

Ubuntu **20.04 LTS** reaches **End of Standard Support in April 2025**.
After this date:

- No further security patches or OS updates will be provided
- Package repositories may become unavailable
- Vulnerabilities and compatibility issues will accumulate

Upgrading to **Ubuntu 24.04 LTS (Noble Numbat)** ensures long-term security and system support until **2034** under extended maintenance.

---



## Important Pre-Requisite

1. Login as root

You **must be logged in as the root user** (or have full administrative privileges using `sudo`) to execute all commands in this procedure.

Upgrading the operating system and SafeSquid involves modifying system-level files, packages, and services that require **root-level access**.

To switch to the root user, run:

```bash
sudo -i
```

Verify root access by checking the prompt changes to:

```bash
root@hostname:~#
```

If you see this, you can proceed safely with the upgrade process

---

1. **Free Storage in `/root`:**

    The `/root` partition must have **more than 15 GB of free space** to accommodate upgrade files, temporary packages, and extracted data.

    Check available space:


```bash
df -h
```

**Expected output for sufficient free space:**

```
Filesystem                                     Size  Used Avail Use% Mounted on
/dev/mapper/vgsab--ubantu-root                  20G  4.0G  16G  20% /
tmpfs                                          392M  900K  391M   1% /run
tmpfs                                          2.0G     0  2.0G   0% /dev/shm
tmpfs                                          5.0M     0  5.0M   0% /run/lock
/dev/mapper/vgsab--ubantu-home                  24G   48K   23G   1% /home
/dev/mapper/vgsab--ubantu-var+cache+safesquid  7.0G   24K  6.7G   1% /var/cache/safesquid
/dev/mapper/vgsab--ubantu-opt+safesquid        3.7G   48M  3.5G   2% /opt/safesquid
/dev/mapper/vgsab--ubantu-var+lib+safesquid    7.5G  4.3G  2.8G  61% /var/lib/safesquid
/dev/mapper/vgsab--ubantu-var+www+safesquid     14G   24K   14G   1% /var/www/safesquid
/dev/sda1                                      1.9G  193M  1.6G  11% /boot
/dev/mapper/vgsab--ubantu-usr+local+safesquid  3.7G   9.2M  3.5G   1% /usr/local/safesquid
/dev/mapper/vgsab--ubantu-var+log+safesquid     96G  885M   90G   1% /var/log/safesquid
/dev/mapper/vgsab--ubantu-var+db+safesquid      73G  1.1M   69G   1% /var/db/safesquid
/dev/ram1                                       60M  3.0M   54M   6% /tmp/safesquid
tmpfs                                          392M  8.0K  392M   1% /run/user/0
```

> Note: If free space is below 15 GB, clean up unnecessary files or resize the /root partition before proceeding.
>

---

1. Check Current OS Version

**Purpose:**
This step confirms the current OS version before proceeding, ensuring the system is actually running **Ubuntu 20.04**. The upgrade procedure must be followed sequentially, so the version check prevents applying incorrect upgrade steps.

**Command:**

```bash
lsb_release -a
```

**Expected Output:**

```
description:    Ubuntu 20.04 LTS
```

If the version shows **18.04**, perform an upgrade to **20.04** first before continuing.

---



## Step 1: Upgrade Ubuntu from 20.04 → 24.04 (Two-Step Process)

Ubuntu LTS upgrades must be done **sequentially** (20.04 → 22.04 → 24.04).
This ensures all intermediate packages, kernel modules, and libraries are properly migrated.

---

### **Phase 1 – Upgrade from 20.04 to 22.04**

**Why:**

- Ubuntu cannot skip LTS versions directly
- This step ensures that kernel, libc, and dependent packages are incrementally upgraded to versions compatible with 22.04

**Commands:**

```bash
apt autoclean -y && apt autoremove -y
apt-get clean
apt update && apt upgrade -y
do-release-upgrade -f DistUpgradeViewNonInteractive
```

- `apt autoclean` removes obsolete package files
- `apt autoremove` clears unused dependencies to prevent clutter
- `apt-get clean`: Removes cached packages to free space and avoid conflicts
- `apt update && apt upgrade -y`: Ensures the system is fully patched before upgrading
- `do-release-upgrade -f DistUpgradeViewNonInteractive`: Initiates the upgrade to Ubuntu 22.04 in non-interactive mode,
This upgrades Ubuntu to the next LTS version **without stopping to ask questions**, ensuring a fully automated process suitable for remote servers or critical systems.

**After completion:**

```bash
reboot
```

Reboot is required to boot into the new kernel and load updated system libraries.

---

### **Phase 2 – Upgrade from 22.04 to 24.04**

**Why:**
This phase upgrades the system to the final target OS, **Ubuntu 24.04 LTS**, which provides:

- Kernel **6.8**
- glibc **2.39**
- Modern dependencies required by SafeSquid 2025.1001.1232.3

**Commands:**

```bash
apt autoclean -y && apt autoremove -y
apt-get clean
apt update && apt upgrade -y
do-release-upgrade -f DistUpgradeViewNonInteractive
```

- `apt autoclean` removes obsolete package files
- `apt autoremove` clears unused dependencies to prevent clutter
- **`apt-get clean`:** Removes all cached package files from `/var/cache/apt/archives` to free up space and prevent conflicts
- **`apt update && apt upgrade -y`:** Updates the package index and upgrades all installed packages to the latest available versions automatically
- **`do-release-upgrade -f DistUpgradeViewNonInteractive`:** Initiates the Ubuntu OS upgrade to the next release in a fully automated, non-interactive mode

---

After the upgrade completes:

```bash
apt autoclean -y && apt autoremove -y
reboot
```

- `apt autoclean` removes obsolete package files
- `apt autoremove` clears unused dependencies to prevent clutter
- Reboot ensures the system loads the new kernel and environment

---



## Step 2: Update BIND Configuration

**Why:**

SafeSquid, during its operation, creates or modifies `/etc/bind/named.conf.appliance.options`, which automatically add options `dnssec-validation` and TTL limits.

These options cause conflicts when starting bind9 service.

The reason SafeSquid does this is to **ensure Active Directory (AD) integration works smoothly**, as these options control DNS validation and caching behavior, which are critical for resolving AD domain controllers and Kerberos services.

**Commands:**

```bash
vim /etc/bind/named.conf.options
```

Comment the following lines:

```bash
// dnssec-validation auto;

// max-cache-ttl 300;
// max-ncache-ttl 300;
```

**Save and restart BIND:**

```bash
systemctl restart bind9
```

This restarts the DNS service with updated configuration.

---



## Step 3: Rename `msktutil` Binary

**Why:**`msktutil` is a tool used for managing machine accounts in Active Directory.

SafeSquid or system processes may attempt to use the existing `msktutil` binary, which was built for Ubuntu 20.04.

On Ubuntu 24.04, this older binary can have **dependency issues** with newer Kerberos libraries.

**Command:**

```bash
mv /usr/local/bin/msktutil /usr/local/bin/msktutil_
```

---



## Step 4: Update Netplan Configuration

**Why:**
During OS upgrades, network settings may change or revert.
Updating Netplan ensures the system uses the **local DNS resolver (127.0.0.1)**, allowing proper DNS resolution through your AD-integrated BIND server.

**Commands:**

```bash
vim /etc/netplan/00-installer-config.yaml
```

Add or modify the nameserver section:

```yaml
nameservers:
  addresses: [127.0.0.1]
```

**Apply the configuration:**

```bash
netplan apply
```

This ensures DNS resolution functions correctly with BIND post-upgrade.

---



## Step 5: Upgrade SafeSquid Application

**Why:**
Once the OS environment is compatible (kernel 6.8, glibc 2.39), install the new SafeSquid version.
The latest release provides updated filtering features, enhanced TLS handling, and improved performance.

**Commands:**

```bash
wget -P /usr/local/src https://downloads.safesquid.com/appliance/unstable/safesquid-2025.1001.1232.3-swg-standard.tar.gz
tar -xzf /usr/local/src/safesquid-2025.1001.1232.3-swg-standard.tar.gz -C /usr/local/src
/usr/local/src/_mkappliance/installation/setup.sh
```

**Check status:**

```bash
systemctl status safesquid.service
```

**Enable at boot:**

```bash
systemctl enable safesquid
```

This ensures SafeSquid starts automatically after system reboots.

---



## Step 6: Post-Upgrade Cleanup and Verification

**Why:**
Cleaning residual packages prevents storage bloat and ensures a consistent, stable environment.
Verification confirms that both OS and SafeSquid versions are upgraded successfully.

**Commands:**

```bash
apt autoclean -y && apt autoremove -y
reboot
```

After reboot, verify OS versions:

```bash
lsb_release -a
```

**Expected:**

```
description:    Ubuntu 24.04 LTS
```

---

Verify Installed SafeSquid Version.

```bash
ls -rlt /opt/safesquid/bin/safesquid
```

**Expected:**

```bash
lrwxrwxrwx 1 ssquid root 39 Oct 13 22:22 /opt/safesquid/bin/safesquid -> safesquid-2025.1001.1232.3-swg-standard
```

