---
title: Cookie Inspection
slug: /Cookie_Inspection
description: Configure SafeSquid cookie filter to manage, allow, or block cookies for user privacy and policy enforcement.
keywords:
  - cookie filter SafeSquid
  - block cookies SafeSquid
  - cookie management SafeSquid
  - restrict cookies SafeSquid
  - cookie filtering SafeSquid
---


# Cookie Inspection



## Cookie filter controls which hosts can send and receive cookies

The Cookie Filter lets administrators choose which hosts (websites) may send and receive cookies. An HTTP cookie is a small piece of data sent from a website and stored in the user's browser while the user browses. Administrators can control cookie exchange between remote websites and users, manage user privacy (username and preferences), and prevent users from logging into personal accounts on selected sites.

**Example:** Block cookies from advertising sites such as tribalfusion.com and doubleclick.net to prevent private information from being transferred. Users can query search engines (Google, Yahoo) but cannot log into personal accounts (Gmail, shopping, trading sites).



## Cookie filter configuration guides

### [Cookie Filter Configuration and Reference](/docs/Cookie_Inspection/Cookie_Filter_Configuration/)
Cookie allow/deny behavior requires correct Global policy and Allow/Deny rules. The document covers the Configuration Portal path, Global and Policy options, and Allow/Deny rule parameters (profiles, expiry, domain, path, direction, time match). Example rules and solution verification support validation. Use the document to configure and validate cookie filtering.

## Next steps

Combine with [Header Obfuscation](/docs/Header_Obfuscation/main/) and [Access Restriction](/docs/Access_Restriction/main/) for full request/response and privacy control.
