---
title: FAQs
slug: /FAQs
description: Frequently asked questions about SafeSquid Secure Web Gateway covering installation, configuration, licensing, and troubleshooting common issues.
keywords:
  - SafeSquid FAQ
  - SafeSquid questions
  - SafeSquid help
  - SafeSquid troubleshooting
  - SafeSquid support
  - SafeSquid SWG FAQ
---


# FAQs

Common questions about SafeSquid SWG: installation, activation, licensing, proxy modes, reporting, transparent proxy, WCCP, DLP, SafeSearch, and troubleshooting. Use the list below to jump to a topic.



## FAQ index

- [What is SafeSquid for Windows?](#what-is-safesquid-for-windows)
- [Where to get a product activation key](#where-to-get-a-product-activation-key)
- [What is SafeSquid Self Service portal?](#what-is-safesquid-self-service-portal)
- [Who has access to the SafeSquid Web GUI](#who-has-access-to-the-safesquid-web-gui)
- [How to confirm SafeSquid is activated](#how-to-confirm-safesquid-is-activated)
- [Where to get license details](#where-to-get-license-details)
- [Why does "Proxy Access Denied" appear?](#why-does-proxy-access-denied-appear)
- [Does SafeSquid supports transparent proxy?](#does-safesquid-supports-transparent-proxy)
- [When to enable WCCP](#when-to-enable-wccp)
- [How does SafeSquid licensing work?](#how-does-safesquid-licensing-work)
- [How to purchase SafeSquid SWG](#how-to-purchase-safesquid-swg)



## What is SafeSquid for Windows?
SafeSquid for Windows is content filtering proxy server. SafeSquid for Linux has been natively ported for use on Microsoft Windows platform, and distributed as SafeSquid for Windows. It provides total access control, Total Content Control & Total Internet Security. SafeSquid for Windows can be installed on any desktop/server having Microsoft Windows based 64-bit Operating Systems.



## Where to get a product activation key
Obtain a product activation key **on SafeSquid self-service portal** - https://key.safesquid.com/

Register to create an account on **SafeSquid self-service portal** and **download the product activation key**



## What is SafeSquid Self Service portal?
The SafeSquid Self-Service Portal is the cloud-based management console for SafeSquid.

The SafeSquid Self-Service Portal manages the activities like, SafeSquid cloud-backed features, Custom Web Categorization, Web Security Clients for Roaming users (VPN), Confidential Data Signatures, Subscription management, etc.

Read more: [Self-Service Portal](/docs/SafeSquid_SWG/Self-Service_Portal/).



## Who has access to the SafeSquid Web GUI
SafeSquid has an intrinsic Web GUI, that enables administrators to manage the installation, setup required policies, and monitor the secure web gateway.

Configure SafeSquid policies to allow access of the Web GUI to only security administrators.



## How to confirm SafeSquid is activated
If all websites are accessible through the browser, the product is activated.



## Where to get license details
After successful activation, license details appear on the Support page of the SafeSquid Web GUI.

For more details see the [Support page](/docs/Audit_Forensics/main/) (license details after activation) or [Activate](/docs/Getting_Started/Activate/).



## Why does "Proxy Access Denied" appear?
"Proxy Access Denied" appears when access restriction policies are misconfigured or the administrator has not granted SafeSquid Interface access.



## Can I use SafeSquid Captive portal to monitor internet usage traffic?
Yes. SafeSquid captive portal can monitor internet usage traffic.



## What is SafeSquid Captive portal?
SafeSquid captive portal is works as same as general captive portal.

Used to enhance security of WIFI network by authenticating users before granting internet access.

Users receive the SafeSquid Captive Portal landing page when accessing the internet via the WIFI network and enter credentials there.

SafeSquid captive portal validates user credentials using various authentication mechanisms and maintains database of authenticated source IP addresses and usernames for lookup.

If a user from a source IP address authenticated through captive portal, then SafeSquid will pick the username from the database and attach to the traffic coming from the same source IP address

This way SafeSquid captive portal secures WIFI network by only granting access to valid users

Combining SafeSquid Captive Portal with SafeSquid secure web gateway allows monitoring of internet usage, filtering of traffic, and other security enhancements to enhance security levels.



## Does SafeSquid supports transparent proxy?
Yes, SafeSquid supports transparent proxy.

SafeSquid support both HTTP and HTTPS websites in transparent mode. The HTTPS websites in transparent mode called as SSL transparent proxy

The traffic will come to router and router will send traffic to SafeSquid Secure web gate way with port 80 and 443 respectively.

The **redirection rules on SafeSquid Secure web gateway** will redirect traffic to SafeSquid Proxy with port 8080 and 8443 (SSL transparent) respectively (By enabling IP forwarding).



## When to enable WCCP
For transparent redirection of traffic, Load balance traffic & scaling up or Service assurance & high availability, enable WCCP in SafeSquid. Enable WCCP support on routers that support WCCP.

Ex: CISCO ASA routers.

Web Cache Communication Protocol (WCCP) is a Cisco-developed content-routing protocol that provides a mechanism to redirect traffic flows in real-time. It has built-in load balancing, scaling, fault tolerance, and service-assurance (failsafe) mechanisms.

Making SafeSquid go direct for some sites

Preventing access to porn sites



## Preventing access to social networking sites
Yes. SafeSquid can prevent users from accessing social networking sites. When configured, SafeSquid blocks all social networking sites by default. Administrators can allow those sites for specific times (e.g. lunch hour).

Allow social networking sites in lunch hours: [Allow Social Networking Sites During Lunch Hours](/docs/Use_Cases/Allow_Social_Networking_Sites_during_Lunch_Hours/).

Facebook is a social networking website that allows users to interact with other users in a multimedia environment on the Web. Facebook users can install and use applications to enhance their experience. Many organizations want to allow Facebook access to maintain morale, increase retention, and boost hiring, but they also want to control access to it.

SafeSquid allows full Facebook access for a social media group, partial access to a customer service group, and read-only access to other groups. Access to Facebook can also be assigned by time of day. For more details: [Facebook Read-Only Mode](/docs/Use_Cases/Facebook_Read_Only_Mode/), [Allow Specific Page on Facebook](/docs/Use_Cases/Allowing_Specific_Page_on_Facebook/).



## Preventing users from uploading confidential data
Yes. SafeSquid can prevent users from uploading confidential data. When an organization has confidential information and an internal user leaks it intentionally or unintentionally, productivity loss can be large.

Data leakage can occur through many channels. Users may upload important documents to the internet; even when content filtering blocks Microsoft Word and Excel files, users can create archives of those files and attempt to upload them. Blocking all archives is not practical because staff use archives to transfer large log files.

There are other users who simply take information out of Microsoft Word and Microsoft XL and simply send an Email to third party.

In modern era, these kind of data leaks become a challenge for organizations. Organizations are in a quest for content filtering software's which can deeply inspect archive files and able to identify whether the archive or emails which contains certain keyword matches.

This challenge is also big for security experts because when there is an upload the post data formation is different for Gmail / Google Drive/ Media fire/ Drobox etc. The wide range of formations of post data made it difficult for security experts to derive concrete solution to these challenges.

But SafeSquid come up with **Advanced DLP** solution embedded into **SafeSquid SWG**, which analyzes post data, deeply inspect archives using file decomposition methods and able to identify whether archive or emails or social media posts contains certain keyword matches. Based on the match, the administrator can block uploads by user or by destination website. The Advanced DLP solution is managed from the SafeSquid Self-Service Portal, where administrators create keyword expression matches. SafeSquid SWG will download those keyword expressions and loads into memory. When an archive uploads or an email write, SafeSquid SWG analyses Post data and transmit it to the Clam AV daemon for Signatures verification. If the keyword expression matches Clam AV daemon responds with match. SafeSquid will take respective action based on match.



## Preventing upload of specific file extensions
Yes. SafeSquid can prevent users from uploading specific file extensions.

SafeSquid DLP section is nothing but **Data Loss Prevention module**, used to protect from sending sensitive or critical information outside the corporate network.

It is possible by blocking the specific file types or file extensions based on Content type and extension of file types.



## Can I prevent users to use anonymous proxy?
Yes. SafeSquid can prevent users from using anonymous proxy.

An anonymous proxy will allow users to surf the web anonymously, since it tunnels traffic through servers that spread out across the globe and involve other IP addresses.

Anonymous Proxy service can enhance security and lets users access some restricted websites online.


For more detail: [Access Restriction](/docs/Access_Restriction/main/) and [Use Cases](/docs/Use_Cases/main/) for blocking anonymous proxies and application control.



## Should third-party cookies be blocked?
SafeSquid can block cookies for third-party domains. This controls tracking across sites and hides the referrer for third-party domains; SafeSquid can set referrer to match hostname. Administrators can also hide user agents for third-party domains; SafeSquid can use a default user agent (e.g. Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)).



## Where to get SafeSquid default policies
SafeSquid default policies and how-to guides are in the "How To" section of http://docs.safesquid.com



## Where to get the performance plot
The performance plot is available on the Support page of the SafeSquid Web GUI. Administrators can generate a performance plot by range: last hour, last 7 days, last month, today, or a custom time.



## Where to get the support tarball
The support tarball is on the Support page of the SafeSquid Web GUI. Administrators can generate a new support tarball or search existing tarballs by year, month, day, or time.



## When to download the config file
The config file can be downloaded at any time. SafeSquid allows download by year, month, day, or time, and allows download of the default config for revert scenarios.



## Is SafeSquid provide dashboard for reporting?
SafeSquid provide dashboard which contain details of last 1000 transactions.

SafeSquid dashboard provides Ip address, Users, User groups, websites domains, profiles, application signature, categories, upload content, download content,

Administrators can edit the total number of transactions for the report. Reports support date-range selection.

Administrators can select any number of filtering options.



## How to get reports in PDF format
SafeSquid reporting supports export to PDF and Excel. Open the SafeSquid interface, go to Reports > Dashboard; the PDF button is at the bottom right, just above the SafeSquid version.



## Can reports be generated for specific dates?
Yes. SafeSquid has a reporting module that reduces processing time and provides detailed reports, hour-wise reports, filtering options, deeper data analysis, an automated data mining engine, and export to PDF and Excel.



## Why does SafeSquid become slow after running for some time?
Slowness after sustained operation is often due to resource exhaustion (disk, memory, or connection state). Check disk space and RAM (see [Disk space and RAM are full](/docs/Troubleshooting/Disk_Space_and_RAM_are_Full/)), clear or rotate logs, and review the [Performance Plot](/docs/Audit_Forensics/Performance_Plot/) and [Support](/docs/Audit_Forensics/main/) page for resource usage. Restart the proxy after freeing resources if needed.



## How does SafeSquid licensing work?
SafeSquid SWG is available with annual subscription.

**Base Subscription Plans**

Choose one of the following base subscription plans:

1. Named Users
2. Concurrent Connections
3. CPU Hours

Named Users and Concurrent Connection subscriptions are annual. Multi-year consecutive purchase is available.

**Premium Features Subscription**

1. Data Leakage Prevention
2. Support for Roaming (Windows Laptop) users
3. Log Aggregator
4. WCCP



## How to purchase SafeSquid SWG
Opt for a SafeSquid SWG subscription by paying online via PayPal or by wire or bank transfer.



## What happens if the subscription is not renewed?
SafeSquid SWG is an annual subscription; if the subscription is not renewed, the product stops working.

