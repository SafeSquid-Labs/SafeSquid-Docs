---
title: Custom Categorization Not Working
description: Resolve issues related to updating whitelist or blacklist categories in SafeSquid by troubleshooting categorization engine connectivity and configuration.
keywords:
  - SafeSquid category update failed
  - SafeSquid categorization engine issue
  - SafeSquid category server connection
  - whitelist not updating SafeSquid
  - blacklist update issue SafeSquid
---



## Issues
-   I am trying to add new websites to the whitelist or blacklist category, but it is not updating
-   Uploaded a new file with some websites and added them to specific categories, but I did not find the websites in the respective category
-   SafeSquid interface has hung when I try to add custom websites to any category



## Root Causes
-   Verify the status of **the** Categorization Engine from **the** Statistic page of SafeSquid Interface
-   **The** SafeSquid server is unable to contact **the** SafeSquid category server
-   The file(websites) was not uploaded correctly



## Troubleshooting
### Check for a connection to the category server from your SafeSquid server

Run the below command and see below output

telnet category.safesquid.net 443

Trying 139.59.16.202...

Connected to category.safesquid.net.

Escape character is '^]'.

If the server is not reachable, you have to run the below commands and try telnet again

```bash
rndc flush
```
```bash
/etc/init.d/bind9 restart
```

