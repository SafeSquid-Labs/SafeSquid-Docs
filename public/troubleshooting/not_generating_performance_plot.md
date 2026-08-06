---
title: "Unable to Generate Performance Plot"
description: "Diagnose and resolve SafeSquid unable to generate performance plot incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "not generating performance plot"]
---

# Unable to Generate Performance Plot

Unable to Generate Performance Plot can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## ISSUE

Unable to generate performance plot from SafeSquid Interface: **Support Page \> Performance Plot**

When you install SafeSquid Appliance Builder (SAB) to setup your secure web gateway, the required packages are also installed automatically.

The necessary package required to generate performance plot from the SafeSquid interface is gnuplot(Command-line driven interactive plotting program)

If you can not generate a performance plot from the SafeSquid interface automatically follow the below steps.

1. **Verify whether the package (gnuplot) is properly installed while installation or not**

root@sabproxy:~# aptitude search gnuplot

i gnuplot - Command-line driven interactive plotting program

If it is not installed, properly install it manually (Internet is required for installation)

root@sabproxy:~# **aptitude install gnuplot**

1. **Go to this path (location of plot.sh script)**

root@sabproxy:~# cd /usr/local/safesquid/ui\_root/cgi-bin/

root@sabproxy:/usr/local/safesquid/ui\_root/cgi-bin# ll

total 80

drwxrwxr-- 2 ssquid root 4096 Mar 14 11:57 ./

drwxrwxr-- 8 ssquid root 4096 Mar 14 11:57 ../

-rwxrwxr-- 1 ssquid root 1602 Mar 19 16:54 app\_template.sh\*

-rwxrwxr-- 1 ssquid root 683 Mar 19 16:54 cronentry.sh\*

-rwxrwxr-- 1 ssquid root 2542 Mar 19 16:54 kerberos.sh\*

-rwxrwxr-- 1 ssquid root 17255 Mar 19 16:54 modify\_plot.sh\*

-rwxrwxr-- 1 ssquid root 2608 Mar 19 16:54 moniter.sh\*

**-rwxrwxr-- 1 ssquid root 16869 Mar 19 16:54 plot.sh**\*

-rwxrwxr-- 1 ssquid root 0 Mar 19 16:54 restart.sh\*

-rwxrwxr-- 1 ssquid root 619 Mar 19 16:54 service.sh\*

-rwxrwxr-- 1 ssquid root 6193 Mar 19 16:54 support\_tarball.sh\*

-rwxrwxr-- 1 ssquid root 518 Mar 19 16:54 update.sh\*

Here you can see the **plot.sh** script is available with appropriate permissions.

Once you confirm the availability of the **plot.sh** script, move for your requirements.

1. **For a specific time range you can generate the plot as below:**

./plot.sh YYYYMMDDHHMMSS YYYYMMDDHHMMSS

**Example1:**

root@sabproxy:/usr/local/safesquid/ui\_root/cgi-bin#./plot.sh 20180305000000 20180305235959

1. **For whole day i.e. march 5th 2018**

This will give the performance plot for the whole day i.e. March 5th, 2018

**Example2:**

root@sabproxy:/usr/local/safesquid/ui\_root/cgi-bin#./plot.sh 20180305000000 20180305235959

1. **Go to below path /var/log/safesquid/performance/ \>\> location of generated performance plot**

root@sabproxy:~# cd /var/log/safesquid/performance/

root@sabproxy:/var/log/safesquid/performance# ll

total 84968

drwxrwxr-- 2 ssquid root 4096 Mar 21 16:05 ./

drwxrwxr-- 9 ssquid root 4096 Mar 14 12:05 ../

-rw-rw-r-- 1 ssquid root 86732546 Mar 21 16:46 performance.log

**-rw-rw-r-- 1 ssquid root 259706 Mar 21 16:46 performance.png**

## Capture useful evidence

Collect evidence before restarting services or changing policy. Keep screenshots, command output, and relevant SafeSquid logs with the incident ticket.

```sh
tail -100 /var/log/safesquid/safesquid.log
tail -100 /var/log/syslog
```

Record the affected user, source IP address, requested URL, timestamp, browser error, SafeSquid policy section changed, and verification result.

## Next steps

- Use [Find a complete connection log](/troubleshooting/how_to_use_find_client_id_sh_for_getting_complete_connection_log) to trace a specific client transaction.
- Use [Troubleshooting](/troubleshooting/troubleshooting) for the broader diagnostic checklist.