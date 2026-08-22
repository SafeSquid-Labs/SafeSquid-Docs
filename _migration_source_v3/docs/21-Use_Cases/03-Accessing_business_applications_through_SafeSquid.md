---
title: Accessing Business Applications Through SafeSquid
description: Troubleshoot and configure SafeSquid to allow business applications by identifying blocked URLs, authentication issues, and SSL inspection requirements.
keywords:
  - SafeSquid business applications
  - application proxy troubleshooting
  - URL whitelist configuration
  - enterprise application access
  - proxy application compatibility
---

There have been several instances where it has been reported that certain applications that the organizations use do not work through SafeSquid. This article describes a generalized way of identifying what is wrong with the application and solving it.

There is more than one reason because of why the application may not work through SafeSquid. They can be listed as:

1) The applications may have certain URLs that are getting blocked by SafeSquid. You need to allow those URLs by creating policies so that the application works properly. To identify whether URLs are getting blocked, you need to carefully observe the extended log of SafeSquid by verifying if the status code is '403' (which means blocked) for any of the requests sent by the application. To view the logs, you can run the following command by taking the SSH access of the SafeSquid server:

```bash
tail -F /var/log/safesquid/extended/extended.log | grep "192.168.0.17" | grep '403'
```
Where "192.168.0.17" is the IP of the machine accessing the application. You will be displayed with something like the following log line. The status code 403 describes the blocked URLs.
```
"1496477492.50.1.2386.zx5NhVkA9enUdJEC"    "50"    "1"    "03/Jun/2017:13:41:32"    "78"    "403"    "0"    "0"    "0"    "-"    "192.168.0.17"    "anonymous@192.168.0.17"    "GET"    https://www.bing.com:80/search?q=porn&qs=n&form=QBLH&sp=-1&pq=porn&sc=0-0&sk=&cvid=ADEF7442BA9A41FEB3857DD679E8124F    https://www.bing.com/  "Mozilla"
/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"    "text/html"    "Profiles"    "-"    "192.168.17.1:8080"    "TCP_DENIED"    "DIRECT"    "safesquid"    "www.bing.com"    "bing.comnp"    "www.bing.com"    "bing.com"    "0"    "LUNCH"    "ADMINS"    ""    "Firefox Browser,Browsers,Bing,Search Engine,Bing Search,Bing UnSafe Search"    "pornography,searchengines"    ""    "-"    "-"    "GLOBAL BLOCK"

```
The logline legend mentioning what each field means is shown below:

"record_id"    "client_id"    "request_id"    "date_time"    "elapsed_time"    "status"    "size"    "upload"    "download"    "bypassed"    "client_ip"    "username"    "method"    "url"    "http_referer"    "useragent"    "mime"    "filter_name"    "filtering_reason"    "interface"    "cachecode"    "peercode"    "peer"    "request_host"    "request_tld"    "referer_host"    "referer_tld"    "range"    "time_profiles"    "user_groups"    "request_profiles"    "application_signatures"    "categories"    "response_profiles"    "upload_content_types"    "download_content_types"    "profiles"

2) One of the other reasons may be, that you have authentication and/or HTTPS inspection enabled and the application may not support the authentication (Negotiate/Basic) and/or HTTPS inspection. Authentication failure can be verified by observing the logs and checking for a status code of '407' which indicates "Invalid SSO Auth" (if you have enabled Negotiate authentication)

