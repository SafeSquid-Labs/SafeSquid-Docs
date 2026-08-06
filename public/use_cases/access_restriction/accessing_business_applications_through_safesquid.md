---
title: "Accessing Business Applications Through SafeSquid"
description: "Troubleshoot and configure SafeSquid to allow business applications by identifying blocked URLs, authentication issues, and SSL inspection requirements."
keywords: ["SafeSquid business applications", "application proxy troubleshooting", "URL whitelist configuration", "enterprise application access", "proxy application compatibility"]
---

## Problem

Security teams need predictable control over app and web usage to reduce policy bypass and data-risk exposure.

## Benefits

You can enforce policy decisions consistently with SafeSquid while preserving legitimate business workflows.

## Advantages

You keep actionable policy control close to operations, with verifiable outcomes in logs and policy behavior.

## Call to action

Use the steps in this guide to implement the control, then validate behavior with a real user-flow test.

There have been several instances where it has been reported that certain applications that the organizations use do not work through SafeSquid. This article describes a generalized way of identifying what is wrong with the application and solving it.

There is more than one reason because of why the application may not work through SafeSquid. They can be listed as:

1. The applications may have certain URLs that are getting blocked by SafeSquid. You need to allow those URLs by creating policies so that the application works properly. To identify whether URLs are getting blocked, you need to carefully observe the extended log of SafeSquid by verifying if the status code is '403' (which means blocked) for any of the requests sent by the application. To view the logs, you can run the following command by taking the SSH access of the SafeSquid server:

```bash
tail -F /var/log/safesquid/extended/extended.log | grep "192.168.0.17" | grep '403'
```

Where "192.168.0.17" is the IP of the machine accessing the application. You will be displayed with something like the following log line. The status code 403 describes the blocked URLs.

```text
"1496477492.50.1.2386.zx5NhVkA9enUdJEC"    "50"    "1"    "03/Jun/2017:13:41:32"    "78"    "403"    "0"    "0"    "0"    "-"    "192.168.0.17"    "anonymous@192.168.0.17"    "GET"    https://www.bing.com:80/search?q=porn&qs=n&form=QBLH&sp=-1&pq=porn&sc=0-0&sk=&cvid=ADEF7442BA9A41FEB3857DD679E8124F    https://www.bing.com/  "Mozilla"
/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"    "text/html"    "Profiles"    "-"    "192.168.17.1:8080"    "TCP_DENIED"    "DIRECT"    "safesquid"    "www.bing.com"    "bing.comnp"    "www.bing.com"    "bing.com"    "0"    "LUNCH"    "ADMINS"    ""    "Firefox Browser,Browsers,Bing,Search Engine,Bing Search,Bing UnSafe Search"    "pornography,searchengines"    ""    "-"    "-"    "GLOBAL BLOCK"
```

The logline legend mentioning what each field means is shown below:

"record\_id"    "client\_id"    "request\_id"    "date\_time"    "elapsed\_time"    "status"    "size"    "upload"    "download"    "bypassed"    "client\_ip"    "username"    "method"    "url"    "http\_referer"    "useragent"    "mime"    "filter\_name"    "filtering\_reason"    "interface"    "cachecode"    "peercode"    "peer"    "request\_host"    "request\_tld"    "referer\_host"    "referer\_tld"    "range"    "time\_profiles"    "user\_groups"    "request\_profiles"    "application\_signatures"    "categories"    "response\_profiles"    "upload\_content\_types"    "download\_content\_types"    "profiles"

2. One of the other reasons may be, that you have authentication and/or HTTPS inspection enabled and the application may not support the authentication (Negotiate/Basic) and/or HTTPS inspection. Authentication failure can be verified by observing the logs and checking for a status code of '407' which indicates "Invalid SSO Auth" (if you have enabled Negotiate authentication)