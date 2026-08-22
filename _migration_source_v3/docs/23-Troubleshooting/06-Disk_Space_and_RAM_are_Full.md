---
title: Disk Space and RAM Full on SafeSquid Server
description: Detailed steps for identifying, cleaning, and managing disk and memory usage on a SafeSquid proxy server to prevent performance issues.
keywords:
  - SafeSquid disk full
  - SafeSquid server storage cleanup
  - SafeSquid logs delete
  - SafeSquid RAM usage high
  - free space SafeSquid server
---


# Free disk and RAM to restore proxy operation

When SafeSquid partitions or RAM are full, the proxy can fail or behave unpredictably. Use the steps below to identify full partitions, clean logs and cache safely, and prevent recurrence.



## Prerequisites
Give the enough size to backup store.

Example: If you want to take a backup of files of size 5GB then consider the store up to 5.5 GB

Don't delete the original log files (.log extension) and database files.



## Check disk space
Run the below command to check the available disk space on each partition.

```bash
df -kh
```
You will see the Used and Available sizes on each partition.

  -------------------------------------------------------------------------------------------------------------
  Filesystem                                 Size       Used       Avail      Use%       Mounted on
  ------------------------------------------ ---------- ---------- ---------- ---------- ----------------------
  udev                                       735M       4.0K       735M       1%         /dev

  tmpfs                                      150M       428K       149M       1%         /run

  /dev/dm-2                                  4.9G       4.2G       424M       91%        /

  none                                       4.0K       0          4.0K       0%         /sys/fs/cgroup

  none                                       5.0M       0          5.0M       0%         /run/lock

  none                                       746M       0          746M       0%         /run/shm

  none                                       100M       0          100M       0%         /run/user

  /dev/sda1                                  232M       37M        179M       17%        /boot

  /dev/mapper/dev--vg-var+cache+safesquid   1.8G       2.8M       1.7G       1%         /var/cache/safesquid

  /dev/mapper/dev--vg-usr+local+safesquid   1.8G       44M        1.7G       3%         /usr/local/safesquid

  /dev/mapper/dev--vg-var+db+safesquid      15G        193M       14G        2%         /var/db/safesquid

  /dev/mapper/dev--vg-var+log+safesquid     15G        171M       14G        2%         /var/log/safesquid

  /dev/ram1                                  62M        1.3M       58M        3%         /tmp/safesquid
  -------------------------------------------------------------------------------------------------------------

If any of the above partitions are observed to be used over 80%, then you may take a backup of the following files and delete files as per your requirement.



## Partitions
When the "/ " partition is full remove the files from the below paths:

### /opt/safesquid/bin
change the directory to /opt/safesquid/bin by using the command below:

```bash
cd /opt/safesquid/bin
```
![listing all the contents from /opt/safesquid/bin](/img/Troubleshooting/Disk_space_and_RAM_is_full_on_SafeSquid_server/image1.webp)

The default files and folders are:

sections

modules

safesquid -> safesquid-2017.0518.2110.3-swg-concept*

You should not delete the tar file which is soft-linked to the SafeSquid file. In the above image, it is: safesquid-2017.0518.2110.3-swg-concept*

### /var/log
You can also take the backup of system logs and delete the files with the .gz extension. This folder contains the logs related to a system, so don't delete or modify the original files (i.e. with the .log extension).

**Example: dmesg.1.gz**

### /var/cache/safesquid
Delete all files from this folder by using the command mentioned below. No need to take a backup of any file from this folder.

```bash
rm -rf *
```
### /var/db/safesquid

Delete all files except these three files from the directory: **/var/db/safesquid/report/**

safesquid2.db

safesquid2.db-wal

safesquid2.db-shm

These files will be used to store the data required for reports generation

you can take a backup or directly delete these files.

:::note
If you delete or move the above files to another destination then restart the SafeSquid server, in order to create the deleted or moved files.
:::

### /var/log/safesquid

Change the directory to **:/var/log/safesquid/native/** by using the below command

```bash
cd /var/log/safesquid/native/
```
Native logs are used to store the data related to requests and responses. You can delete all files in this folder, no backup is required.

**Example file name to be deleted: 20161223132118-safesquid.log.gz**

Change the directory to: **/var/log/safesquid/extended/** by using the below command

```bash
cd /var/log/safesquid/extended/
```
Extended logs are used to store the data related to users' information for each connection. Take a backup of these files if required.

**Example file name to be deleted: 20161223132118-extended.log.gz**

Change the directory to: **/var/log/safesquid/performance/** by using the below command

```bash
cd /var/log/safesquid/performance/
```
Performance logs are used to store the data related to safesquid performance statistics. You can take a backup if required and delete it.

**Example file name to be deleted: 20161223132118-performance.log.gz**

Change the directory to **:/var/log/safesquid/config/** by using the below command

```bash
cd /var/log/safesquid/config/
```
config logs used to store the data related to safesquid interface requests and responses. No need to take a backup of these files.

**Example file name to be deleted: 20161223132118-config.log.gz**

### /tmp/safesquid
Delete all files and folders present in this directory. By using this command

```bash
rm -rf *
```
This memory will be used only in upgradation time.

