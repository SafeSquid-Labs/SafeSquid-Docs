---
title: Unable to Generate Support Tar-ball
description: Troubleshoot and manually generate the SafeSquid support tarball when scripts or permissions cause failures.
keywords:
  - SafeSquid support tarball issue
  - SafeSquid generate logs tar.gz
  - SafeSquid support_tarball.sh not working
  - SafeSquid support diagnostics archive
  - troubleshoot SafeSquid technical support logs
---



## ISSUE
Unable to generate support tarball from SafeSquid Interface: **Support Page > Support Tarball**



## Troubleshooting
If you cannot generate support tarball from the SafeSquid interface, automatically follow the steps below.

**Go to this path (location of support_tarball.sh script)**

  -----------------------------------------------------------------------
  root@sabproxy:~# cd /usr/local/safesquid/ui_root/cgi-bin/
  -----------------------------------------------------------------------
  root@sabproxy:/usr/local/safesquid/ui_root/cgi-bin# ll

  total 80

  drwxrwxr-- 2 ssquid root 4096 Mar 14 11:57 ./

  drwxrwxr-- 8 ssquid root 4096 Mar 14 11:57 ../

  -rwxrwxr-- 1 ssquid root 1602 Mar 19 16:54 app_template.sh*

  -rwxrwxr-- 1 ssquid root 683 Mar 19 16:54 cronentry.sh*

  -rwxrwxr-- 1 ssquid root 2542 Mar 19 16:54 kerberos.sh*

  -rwxrwxr-- 1 ssquid root 17255 Mar 19 16:54 modify_plot.sh*

  -rwxrwxr-- 1 ssquid root 2608 Mar 19 16:54 moniter.sh*

  -rwxrwxr-- 1 ssquid root 16869 Mar 19 16:54 plot.sh*

  -rwxrwxr-- 1 ssquid root 0 Mar 19 16:54 restart.sh*

  -rwxrwxr-- 1 ssquid root 619 Mar 19 16:54 service.sh*

  -rwxrwxr-- 1 ssquid root 6193 Mar 19 16:54 support_tarball.sh*

  -rwxrwxr-- 1 ssquid root 518 Mar 19 16:54 update.sh*
  -----------------------------------------------------------------------

Here you can see that the **support_tarball.sh** script is available with appropriate permissions.

Once you confirm the availability of **support_tarball.sh**, move to your requirements.

**To generate support tarball manually as below :**

```bash
Command: ./support_tarball.sh
```
Go to the below path and run above command

root@swg:/usr/local/safesquid/ui_root/cgi-bin# ./support_tarball.sh

2018-06-18::18:06:24.437971402 Creating folder: safesquid-2018-06-18-18-06-24 to contain relevant files and information for support

2018-06-18::18:06:24.445054777 Copying last 5000 lines of /var/log/safesquid/native/safesquid.log to safesquid-2018-06-18-18-06-24/safesquid_logs/safesquid.log

2018-06-18::18:06:24.868917174 Copying last 5000 lines of /var/log/safesquid/extended/extended.log to safesquid-2018-06-18-18-06-24/safesquid_logs/extended.log

2018-06-18::18:06:24.884119250 Copying last 5000 lines of /var/log/safesquid/performance/performance.log to safesquid-2018-06-18-18-06-24/safesquid_logs/performance.log

2018-06-18::18:06:24.935809437 Copying last 5000 lines of /var/log/monit.log to safesquid-2018-06-18-18-06-24/system_logs/monit.log

2018-06-18::18:06:24.969476836 Getting sysctl information into safesquid-2018-06-18-18-06-24/sysctl.txt

2018-06-18::18:06:25.142134567 Getting the Information about Network Interfaces into safesquid-2018-06-18-18-06-24/network.txt

2018-06-18::18:06:25.159857810 Getting the Information about Network Routing Table into safesquid-2018-06-18-18-06-24/network.txt

2018-06-18::18:06:25.174699658 Getting the Network Statistics into safesquid-2018-06-18-18-06-24/network.txt

2018-06-18::18:06:25.193097377 Getting iptables NAT Configuration into safesquid-2018-06-18-18-06-24/iptables.txt

2018-06-18::18:06:25.535699750 Getting iptables MANGLE Configuration into safesquid-2018-06-18-18-06-24/iptables.txt

2018-06-18::18:06:25.542781878 Getting iptables FILTER Configuration into safesquid-2018-06-18-18-06-24/iptables.txt

2018-06-18::18:06:25.549963671 Getting Disk Partitions Information into safesquid-2018-06-18-18-06-24/filesystem.txt

Disk /dev/mapper/swg--vg-root doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-swap_1 doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-opt+safesquid doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-var+lib+safesquid doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-usr+local+safesquid doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-var+lib doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-var+log doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-var+cache+safesquid doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-var+log+safesquid doesn't contain a valid partition table

Disk /dev/mapper/swg--vg-var+db+safesquid doesn't contain a valid partition table

2018-06-18::18:06:25.597927995 Getting Disk Usage Information into safesquid-2018-06-18-18-06-24/filesystem.txt

2018-06-18::18:06:25.612231349 Getting Disk inode Usage Information into safesquid-2018-06-18-18-06-24/filesystem.txt

2018-06-18::18:06:25.616382197 Getting File System Mount Information into safesquid-2018-06-18-18-06-24/filesystem.txt

2018-06-18::18:06:25.756065687 Getting Kernel Information into safesquid-2018-06-18-18-06-24/systeminfo.txt

2018-06-18::18:06:25.760061018 Getting CPU information into safesquid-2018-06-18-18-06-24/systeminfo.txt

2018-06-18::18:06:25.774230478 Getting Memory Information into safesquid-2018-06-18-18-06-24/systeminfo.txt

2018-06-18::18:06:25.777545658 Getting ram memory into safesquid-2018-06-18-18-06-24/systeminfo.txt

2018-06-18::18:06:25.788885128 Creating the tar-ball for sending to SafeSquid Technical Support

2018-06-18::18:06:26.008801780 Extracted contents of the support tar-ball may be confirmed from safesquid-2018-06-18-18-06-24

**The support tarball will generate at below path**

root@swg:/var/log/safesquid/support# ll

total 636

drwxrwxr-- 2 ssquid root 4096 Jun 18 18:06 ./

drwxrwxr-- 9 ssquid root 4096 Jun 11 16:29 ../

-rw-r--r-- 1 ssquid root 642727 Jun 18 18:06 **safesquid-2018-06-18-18-06-24.tar.gz**

