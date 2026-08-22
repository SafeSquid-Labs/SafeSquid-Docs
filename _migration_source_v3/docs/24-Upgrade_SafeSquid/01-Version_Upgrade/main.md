---
title: Upgrade SafeSquid to a Newer Version
slug: /Upgrade_SafeSquid/Version_Upgrade
description: "Upgrade SafeSquid SWG via Web GUI: prerequisites, cleanup, and applying the new tarball package."

keywords:
  - Upgrade SafeSquid SWG
  - SafeSquid tarball update
  - Update SafeSquid from GUI
  - SafeSquid version upgrade
  - SafeSquid Monit service
---


# Upgrade SafeSquid application via Web GUI



## Version upgrade scope and procedure

SafeSquid SWG upgrade is a newer version of the SafeSquid that offers a significant change or major improvement over your current version. Upgrade your SafeSquid to the latest version which may consists of bugfixes and enhancements. When you upload latest tarball of SafeSquid SWG from WebGUI monit service will automatically restart the SafeSquid service.



## Prerequisites
Monit service should be running and started on your SafeSquid server, you can check it by using below command from your SafeSquid server

```bash
pidof monit
```
If you did not find pid of monit, run below command to Start the Monit service

```bash
/etc/init.d/monit start
```

The partition size of /tmp/safesquid used must be less than 4%, you can check it by using below command

```bash
df -kh
```
After executing the command last line of the output will be similar as shown below

```bash
/dev/ram1 62M 1.3M 58M 3% /tmp/safesquid
```
Check the highlighted number which shows the actual usage, if it is greater than 4%, then remove the files from the folder /tmp/safesquid

You can remove files from /tmp/safesquid by going to that folder location using the command:
```bash
cd /tmp/safesquid
```
Further delete all the files from the folder by using the command:

```bash
rm -rf *
```



## Steps
### [Access the SafeSquid User Interface](/docs/SafeSquid_SWG/Configuration_Portal/)

![your current version of safesquid will be shown in the right hand bottom corner in the safesquid interface](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image1.webp)

### Go to Support Page
![clicking on support](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image2.webp)

### Go to upgradation
:::note
Download the latest SafeSquid SWG tarball from here and save into your machine.
:::

![clicking on upgradation](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image3.webp)

### Select new tarball
Select the latest SafeSquid tarball downloaded and saved in your machine before.

![uploading a new tarball file](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image4.webp)

![selecting the tarball file from the pc](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image5.webp)

![you can see the browsed tarball beside browse button](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image6.webp)

![Tarball file selected and ready to upload](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image6.webp)

Click on upload button to upload new tar file.

![clicking on upload button to upload](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image7.webp)



## Testing Upgradation
You can see upgraded version number of SafeSquid SWG at the bottom right corner of interface.

![test if the newer version of the safesquid is showing in the bottom right hand corner](/img/How_To/Upgrade_SafeSquid_To_A_Newer_Version/image8.webp)



## Where should I get the latest version of SafeSquid to upgrade?

You can download **SafeSquid SWG for Windows** package from - http://downloads.safesquid.net/SWG/windows/setup_safesquid_swg_latest.exe

You can download **SafeSquid SWG for Linux** package from - http://downloads.safesquid.net/appliance/binary/safesquid_latest.tar.gz

