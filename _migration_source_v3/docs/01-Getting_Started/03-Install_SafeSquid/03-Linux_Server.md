---
title: Linux Server (TAR)
description: Install SafeSquid SWG from a TAR package on any Linux distribution — Red Hat, CentOS, SUSE, Debian, Ubuntu, and others.
keywords:
  - SafeSquid TAR install
  - SafeSquid Linux installation
  - manual SafeSquid installation
---

# Install from TAR Package

Install SafeSquid on an existing Linux server without replacing the OS or using a full appliance image. Works on any distribution — Debian, Ubuntu, Red Hat, CentOS, SUSE, Rocky Linux, and others.

**Use this method when:**
- You already have a configured Linux server and want to add SafeSquid only
- You need custom OS hardening or disk layouts
- You want full control over dependencies and supporting services

**Trade-off:** You must manually configure Monit, BIND9, and other dependencies. For automated setup, use [Appliance Builder](/docs/Getting_Started/Install_SafeSquid/SafeSquid_Appliance_Builder/) instead.

## Supported Distributions

| **Distribution** | **Tested Versions** | **Package Manager** |
|------------------|---------------------|---------------------|
| Debian | 10 (Buster), 11 (Bullseye), 12 (Bookworm) | apt |
| Ubuntu | 20.04 LTS, 22.04 LTS, 24.04 LTS | apt |
| Red Hat Enterprise Linux | 7, 8, 9 | yum / dnf |
| CentOS / Rocky Linux | 7, 8, 9 | yum / dnf |
| SUSE / openSUSE | SLES 15, Leap 15 | zypper |

Other distributions may work but are untested. Minimum kernel version: 3.10+

## Prerequisites

:::info System Requirements

- Linux server meeting [hardware requirements](/docs/Getting_Started/Deployment_Planning/#hardware-sizing) (minimum 4 CPU cores, 8 GB RAM, 100 GB disk)
- Root or sudo access
- Internet connectivity for downloads
- Kernel version 3.10 or newer

:::

**Required dependencies:**

SafeSquid requires the following libraries. Install before running the installer:

**For Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install -y wget tar libssl-dev libpcre3 libpcre3-dev zlib1g-dev \
  build-essential libc6 libgcc-s1 libstdc++6
```

**For Red Hat/CentOS/Rocky:**
```bash
sudo yum install -y wget tar openssl-devel pcre-devel zlib-devel \
  gcc gcc-c++ make glibc libgcc libstdc++
```

**For SUSE/openSUSE:**
```bash
sudo zypper install -y wget tar libopenssl-devel pcre-devel zlib-devel \
  gcc gcc-c++ make glibc libgcc_s1 libstdc++6
```

## System Preparation

Before installing SafeSquid, prepare the target system:

1. **Create dedicated disk partitions** (recommended for production):
   ```bash
   # Example: Create separate directories for logs and cache
   sudo mkdir -p /var/log/safesquid
   sudo mkdir -p /var/lib/safesquid
   sudo mkdir -p /var/db/safesquid
   ```

2. **Configure firewall** to allow proxy traffic:
   ```bash
   # For firewalld (RHEL/CentOS):
   sudo firewall-cmd --permanent --add-port=8080/tcp
   sudo firewall-cmd --permanent --add-port=8443/tcp
   sudo firewall-cmd --reload

   # For ufw (Ubuntu/Debian):
   sudo ufw allow 8080/tcp
   sudo ufw allow 8443/tcp
   sudo ufw reload

   # For iptables:
   sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
   sudo iptables -A INPUT -p tcp --dport 8443 -j ACCEPT
   sudo iptables-save
   ```

3. **Disable SELinux or configure permissive mode** (RHEL/CentOS only):
   ```bash
   sudo setenforce 0
   sudo sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
   ```

4. **Verify time synchronization** (required for SSL certificate validation):
   ```bash
   timedatectl status
   # If NTP is not active, install and enable:
   sudo systemctl enable --now systemd-timesyncd
   ```

## Installation Steps

1. **Verify prerequisites**

   Before installing, confirm you have:
   - Root or sudo access (run `sudo -v` to verify)
   - Internet connectivity (run `ping -c 3 google.com` to test)
   - At least 10 GB free disk space (run `df -h /` to check)

2. **Download and extract** the SafeSquid package:

   ```bash
   cd /usr/local/src
   wget http://downloads.safesquid.net/appliance/binary/safesquid_latest.tar.gz
   tar -zxvf safesquid_latest.tar.gz
   ```

   **Expected output:** Directory `_mkappliance` extracted with installation scripts.

3. **Run the installer:**

   From the directory where you extracted the TAR:

   ```bash
   sudo _mkappliance/installation/setup.sh
   ```

   **What the installer does:**
   - Checks for required dependencies
   - Creates `safesquid` system user and group
   - Installs binaries to `/opt/safesquid/`
   - Creates init scripts and systemd service files
   - Sets up default configuration in `/etc/safesquid/`

   **If installation fails:** Check the terminal output for missing dependencies. Common issues:
   - Missing libraries → Install dependencies (see Prerequisites above)
   - Permission denied → Ensure you're running with `sudo` or as root
   - Disk full → Check available space with `df -h`

4. **Check for missing dependencies:**

   ```bash
   ldd /opt/safesquid/bin/safesquid
   ```

   If any library shows `not found`, install the missing package using your distribution's package manager (`apt`, `yum`, `zypper`, etc.).

5. **Start SafeSquid:**

   ```bash
   sudo systemctl start safesquid
   # Or for init.d-based systems:
   sudo /etc/init.d/safesquid start
   ```

## Verify Installation

**1. Check service status:**

```bash
# For systemd-based systems:
sudo systemctl status safesquid

# For init.d-based systems:
sudo /etc/init.d/safesquid status
```

**Expected output:** Active (running)

**2. Verify port 8080 is listening:**

```bash
netstat -tulnp | grep 8080
```

**Expected output:** `safesquid` process listening on `0.0.0.0:8080`

**3. Check logs for errors:**

```bash
tail -50 /var/log/safesquid/safesquid.log
```

**Expected:** No critical errors. Info and startup messages are normal.

**4. Access admin interface:**

- **Direct access:** `https://SERVER-IP:8443/`
- **Via proxy:** Configure a browser to use `SERVER-IP:8080`, then navigate to `https://safesquid.cfg/` (embedded Rest UI interface built into SafeSquid; NOT resolved by SafeSquid's DNS resolver)

If the interface loads, installation succeeded.

## Post-Install Hardening

**For production deployments:**

1. **Change default admin password:**
   - Log in to `https://SERVER-IP:8443/`
   - Navigate to System → User Management
   - Change the `administrator` account password

2. **Restrict admin interface access:**
   - Configure firewall to allow port 8443 only from admin IPs
   - Use SSH tunneling for remote admin access

3. **Enable automatic updates:**
   ```bash
   # Add SafeSquid repository and configure auto-updates
   # (See SafeSquid documentation for repository setup)
   ```

4. **Configure log rotation:**
   ```bash
   sudo nano /etc/logrotate.d/safesquid
   ```
   Add:
   ```
   /var/log/safesquid/*.log {
       daily
       rotate 30
       compress
       delaycompress
       missingok
       notifempty
       sharedscripts
       postrotate
           /etc/init.d/safesquid reload > /dev/null
       endscript
   }
   ```

5. **Set up Monit monitoring** (see [Configure Supporting Services](#configure-supporting-services))

## Troubleshooting

| Symptom | Likely cause | Fix |
| ------- | ------------ | --- |
| `ldd` shows "not found" for a library | Missing system dependency | Install the required package (e.g., `libssl`, `libpcre`) using your distro's package manager (see Prerequisites) |
| SafeSquid fails to start | Permissions, port in use, or config error | Check `/var/log/safesquid/safesquid.log`; ensure port 8080 is free: `netstat -lntp \| grep 8080`; run with sudo |
| Installer script fails | Insufficient disk, no root/sudo, or network | Ensure ≥10 GB free, run with sudo/root, verify outbound connectivity to `downloads.safesquid.net` |
| "Permission denied" errors in logs | SELinux blocking SafeSquid | Set SELinux to permissive mode: `sudo setenforce 0` (RHEL/CentOS only) |
| Cannot access admin interface at :8443 | Firewall blocking port | Configure firewall to allow port 8443 (see System Preparation) |
| Service starts but stops immediately | Missing configuration or dependency | Run `sudo journalctl -u safesquid -n 50` to check for errors; verify all dependencies: `ldd /opt/safesquid/bin/safesquid` |

## Configure Supporting Services

SAB handles these automatically, but TAR installations require manual setup:

### Monit (Process Monitoring)

**Why it matters:** Monit automatically restarts SafeSquid if it crashes, ensuring high availability.

**Quick setup:**

1. Install Monit:
   ```bash
   # Debian/Ubuntu:
   sudo apt install monit

   # RHEL/CentOS:
   sudo yum install monit
   ```

2. Configure Monit for SafeSquid:
   ```bash
   sudo nano /etc/monit/conf.d/safesquid
   ```
   Add:
   ```
   check process safesquid with pidfile /var/run/safesquid.pid
       start program = "/etc/init.d/safesquid start"
       stop program = "/etc/init.d/safesquid stop"
       if failed port 8080 then restart
       if 5 restarts within 5 cycles then timeout
   ```

3. Enable and start Monit:
   ```bash
   sudo systemctl enable --now monit
   ```

**Full guide:** [Monit Configuration](/docs/SafeSquid_SWG/Supporting_Services/Monit/)

---

### BIND9 (Local DNS)

SafeSquid uses a local DNS resolver for performance and policy-aware resolution.

**Quick setup:**

1. Install BIND9:
   ```bash
   # Debian/Ubuntu:
   sudo apt install bind9

   # RHEL/CentOS:
   sudo yum install bind
   ```

2. Configure SafeSquid to use local BIND9 (done via SafeSquid admin interface after activation)

**Full guide:** [BIND9 Configuration](/docs/SafeSquid_SWG/Supporting_Services/Bind/)

:::tip Before Production

Configure both Monit and BIND9 before moving to production. Without Monit, a crashed SafeSquid process will not restart automatically.

:::

## Next Steps

1. **[Configure Supporting Services](#configure-supporting-services)** — Set up Monit and BIND9 before production
2. **[Activate Your License](/docs/Getting_Started/Activate/)** — Upload your activation key to make SafeSquid fully operational
3. **[Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/)** — Configure a browser to use the proxy
4. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Confirm traffic flows through SafeSquid
5. **[Enable SSL Inspection](/docs/SSL_Inspection/main/)** — Decrypt and inspect HTTPS traffic
