---
title: Linux Server
description: Install SafeSquid SWG from TAR on Red Hat, CentOS, SUSE, and other Linux distributions.
keywords:
  - Install SafeSquid using TAR file
  - SafeSquid on CentOS/RedHat/SuSe
  - Manual SafeSquid installation Linux
  - SafeSquid TAR package setup
  - Configure SafeSquid with Monit and BIND
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

SafeSquid is a versatile web filtering software that can be installed on various Linux operating systems, including but not limited to Red-Hat, SuSe, and CentOS. This flexibility allows users to deploy SafeSquid on their existing infrastructure or select a Linux distribution that best fits their organizational needs and preferences. The installation process on Linux distributions other than Ubuntu involves a few additional steps and configurations to ensure optimal performance and stability.

## Key Considerations

**System Compatibility**: Before proceeding with the installation, verify that your chosen Linux distribution is compatible with SafeSquid and meets the necessary system requirements, such as CPU, memory, and storage.

**Dependency Management**: Different Linux distributions might require specific dependencies or libraries for SafeSquid. Ensure that all necessary software prerequisites are installed and updated.

**Installation Process**: The installation steps may vary slightly depending on the Linux distribution. It typically involves downloading the SafeSquid package tailored for the specific version of Linux and using the distribution's package manager for installation.

**Configuring Monit and BIND Services**: SafeSquid utilizes Monit for management and monitoring of system processes and BIND for DNS services. Proper configuration of these services is crucial for the effective functioning of SafeSquid.

**Security and Firewall Settings**: Configure your system's firewall to allow traffic through the ports used by SafeSquid. Also, ensure that your system is secured against potential threats.

**Performance Optimization**: Depending on your Linux distribution, there might be unique performance tuning options that can enhance the efficiency of SafeSquid.

**Regular Maintenance and Updates**: Keep SafeSquid and its dependencies updated to ensure security, stability, and access to the latest features.

**Documentation and Support**: Utilize the official SafeSquid documentation for detailed installation and configuration instructions. Seek support from the SafeSquid community or professional support services if needed.

**Backup and Recovery Planning**: Implement a strategy for backing up your SafeSquid configuration and system settings to facilitate quick recovery in case of system failure.

This document aims to provide a step-by-step guide to installing SafeSquid on a variety of Linux distributions, highlighting important considerations and best practices to ensure a successful deployment.

## Overview

SafeSquid can also be installed on any other Linux operating system like Red-Hat, SuSe, CentOS, etc. Choose this method of installation only if you want to setup SafeSquid on already existing infrastructure or if you want to use other Operating System in Linux family other than Ubuntu. It requires some additional configurations which are Monit and bind services used by SafeSquid.

## Prerequisites

For SafeSquid to work smoothly, configure [Monit](/docs/SafeSquid%20SWG/Supporting%20Services/Monit) for service monitoring and [bind](/docs/SafeSquid%20SWG/Supporting%20Services/Bind) for internalized DNS.

## Download Latest Version in Linux Server

Go to the linux server and change the directory to "/usr/local/src" by using below command

```bash npm2yarn
cd /usr/local/src
```

Use the "wget" command to download the latest SafeSquid package on the Linux machine on which you want to install SafeSquid. The command will download the tarball file.

```bash npm2yarn
wget http://downloads.safesquid.net/appliance/binary/safesquid_latest.tar.gz
```

![going in /usr/local/src directory](/img/Installing_SafeSquid_on_Various_Linux_Distributions_Using_SafeSquid%27s_tar_file_%281%29/image1.webp)

## Extract the tarball.

Extract the files from tar by using the command below.

```bash npm2yarn
tar -zxvf safesquid_latest.tar.gz
```

The output of the above command is shown below.

![extracting the tar.gz file in the directory](/img/Installing_SafeSquid_on_Various_Linux_Distributions_Using_SafeSquid%27s_tar_file_%281%29/image2.webp)

All the files will be extracted in the directory having name "\_mkappliance".

You must execute/run the setup.sh script to install SafeSquid.

```bash npm2yarn
_mkappliance/installation/setup.sh
```

Output after script execution is shown below.

![listing the files with command ls -lrt in the src directory](/img/Installing_SafeSquid_on_Various_Linux_Distributions_Using_SafeSquid%27s_tar_file_%281%29/image3.webp)

Installation completes if you did not get any error.

## Dependency Check

You can check if any of the dependencies missing for SafeSquid by using the "ldd" command as shown below.

```bash npm2yarn
ldd /opt/safesquid/bin/safesquid
```

Output for the above command is shown below.

<Tabs>
  <TabItem value="Success" label="Success" default>
    root\@safesquid:/opt/safesquid/bin## ldd /opt/safesquid/bin/safesquid

    linux-vdso.so.1 => (0x00007ffebebdb000)

    libldap\_r-2.4.so.2 => /usr/lib/x86\_64-linux-gnu/libldap\_r-2.4.so.2 (0x00007ff03107e000)

    libpam.so.0 => /lib/x86\_64-linux-gnu/libpam.so.0 (0x00007ff030e70000)

    liblber-2.4.so.2 => /usr/lib/x86\_64-linux-gnu/liblber-2.4.so.2 (0x00007ff030c61000)

    libgssapi.so.3 => /usr/lib/x86\_64-linux-gnu/libgssapi.so.3 (0x00007ff030a23000)

    libdl.so.2 => /lib/x86\_64-linux-gnu/libdl.so.2 (0x00007ff03081f000)

    libresolv.so.2 => /lib/x86\_64-linux-gnu/libresolv.so.2 (0x00007ff030604000)

    libstdc++.so.6 => /usr/lib/x86\_64-linux-gnu/libstdc++.so.6 (0x00007ff030300000)

    libm.so.6 => /lib/x86\_64-linux-gnu/libm.so.6 (0x00007ff02fffa000)

    libgcc\_s.so.1 => /lib/x86\_64-linux-gnu/libgcc\_s.so.1 (0x00007ff02fde4000)

    libpthread.so.0 => /lib/x86\_64-linux-gnu/libpthread.so.0 (0x00007ff02fbc6000)

    libc.so.6 => /lib/x86\_64-linux-gnu/libc.so.6 (0x00007ff02f7fd000)

    libsasl2.so.2 => /usr/lib/x86\_64-linux-gnu/libsasl2.so.2 (0x00007ff02f5e2000)
  </TabItem>

  <TabItem
    value="Dependency Missing Error"
    label="Dependency Missing Error"
    default
  >
    root\@safesquid:/opt/safesquid/bin## ldd /opt/safesquid/bin/safesquid

    linux-vdso.so.1 => (0x00007ffebebdb000)

    libldap\_r-2.4.so.2 => /usr/lib/x86\_64-linux-gnu/libldap\_r-2.4.so.2 (0x00007ff03107e000)

    libpam.so.0 => /lib/x86\_64-linux-gnu/libpam.so.0 (0x00007ff030e70000)

    liblber-2.4.so.2 => /usr/lib/x86\_64-linux-gnu/liblber-2.4.so.2 (0x00007ff030c61000)

    libgssapi.so.3 => /usr/lib/x86\_64-linux-gnu/libgssapi.so.3 (0x00007ff030a23000)

    libdl.so.2 => /lib/x86\_64-linux-gnu/libdl.so.2 (0x00007ff03081f000)

    libresolv.so.2 => /lib/x86\_64-linux-gnu/libresolv.so.2 (0x00007ff030604000)

    libstdc++.so.6 => /usr/lib/x86\_64-linux-gnu/libstdc++.so.6 (0x00007ff030300000)

    libgmp.so.3==> not found

    libm.so.6 => /lib/x86\_64-linux-gnu/libm.so.6 (0x00007ff02fffa000)

    libgcc\_s.so.1 => /lib/x86\_64-linux-gnu/libgcc\_s.so.1 (0x00007ff02fde4000)

    libpthread.so.0 => /lib/x86\_64-linux-gnu/libpthread.so.0 (0x00007ff02fbc6000)

    libc.so.6 => /lib/x86\_64-linux-gnu/libc.so.6 (0x00007ff02f7fd000)

    libsasl2.so.2 => /usr/lib/x86\_64-linux-gnu/libsasl2.so.2 (0x00007ff02f5e2000)
  </TabItem>
</Tabs>

If you notice that any of the dependencies are not present then, you should install that dependencies to make SafeSquid work.

## Start the SafeSquid

Further you need to Start the SafeSquid service by using the command below.

```bash npm2yarn
/etc/init.d/safesquid start
```

## Testing

You can check whether SafeSquid service is running or not by using these commands.

```bash npm2yarn
pidof safesquid
```

OR

```bash npm2yarn
netstat -tulnp | grep "safesquid"
```

![checking whether SafeSquid service is running or not by using these commands pidof safesquid OR netstat -tulnp | grep "safesquid"](/img/Installing_SafeSquid_on_Various_Linux_Distributions_Using_SafeSquid%27s_tar_file_%281%29/image4.webp)

By default, SafeSquid will listen on PORT 8080. If you observe SafeSquid is listening on any one of the ports shown in the image, then its confirm that SafeSquid has started.

This installation does not include the Monit and Bind configurations.

Make some additional configurations to services used by SafeSquid, for [Monit](/docs/SafeSquid%20SWG/Supporting%20Services/Monit) and [BIND9](/docs/SafeSquid%20SWG/Supporting%20Services/Bind).
