---
title: SafeSquid Use Cases
slug: /Use_Cases
description: "Use-case index for SafeSquid SWG: configurations for security, access control, and productivity."
keywords:
  - SafeSquid use cases
  - SafeSquid configurations
  - Secure Web Gateway policies
  - SafeSquid administration
---


# Use-case index for SafeSquid SWG

Find use-case configurations for SafeSquid SWG below. Each document describes how to configure SafeSquid for a specific need: blocking or allowing sites, restricting access by user or time, and enforcing security policies.



## Use case configuration guides

### [Access Mobile Applications Through SafeSquid](/docs/Use_Cases/Access_Mobile_Applications_Through_SafeSquid/)
Mobile applications must use the enterprise proxy to enforce policy and visibility. The document describes configuring mobile apps to use SafeSquid so traffic is inspected and policies apply. Organizations gain consistent control over mobile web and API traffic. Follow the document to configure mobile applications through SafeSquid.

### [Access Remote Desktop Applications Through SafeSquid](/docs/Use_Cases/Access_Remote_Desktop_Applications_Through_SafeSquid/)
Remote desktop traffic may need to be allowed or restricted by policy. The document covers managing and restricting access to remote desktop applications via SafeSquid. Administrators can allow or block specific RDP or similar traffic. Use the document to configure remote desktop access.

### [Access Business Applications Through SafeSquid](/docs/Use_Cases/Accessing_business_applications_through_SafeSquid/)
Only approved business applications should reach the internet in locked-down environments. The document explains how to allow specific business applications while blocking others. Policy applies by application signature or destination. Follow the document to restrict access to business applications only.

### [Allow AnyDesk](/docs/Use_Cases/Allow_anydesk/)
AnyDesk or similar remote support may be required for IT or vendors. The document describes allowing AnyDesk access while restricting other applications. Organizations balance support needs with access control. Use the document to allow AnyDesk through SafeSquid.

### [Allow Outlook To Work Through SafeSquid](/docs/Use_Cases/Allow_Outlook_To_Work_through_SafeSquid/)
Outlook and Exchange can fail when proxy authentication or inspection blocks traffic. The document covers allowing Outlook to operate through SafeSquid while keeping security policies. Mail flow continues without weakening overall policy. Follow the document to configure Outlook through SafeSquid.

### [Allow Remote Applications to Particular Users](/docs/Use_Cases/Allow_remote_applications_to_particular_users/)
Remote applications may be allowed for some users or groups but not others. The document explains allowing specific users to access remote applications via SafeSquid. Policy is applied by identity or group. Use the document to allow remote applications for particular users.

### [Allow Social Networking Sites During Lunch Hours](/docs/Use_Cases/Allow_Social_Networking_Sites_during_Lunch_Hours/)
Organizations may allow social networking only during specified times. The document describes time-based access so social sites are allowed only during lunch or defined windows. Productivity and policy balance is configurable. Follow the document to allow social networking sites during lunch hours.

### [Allow Specific YouTube Channel and Its Playlist](/docs/Use_Cases/Allow_Specific_YouTube_Channel_and_its_Playlist/)
Only approved YouTube channels or playlists may be allowed for training or morale. The document covers allowing specific YouTube channels or playlists while blocking others. Granular control reduces exposure to non-business content. Use the document to allow specific YouTube channels.

### [Allow Specific Page on Facebook](/docs/Use_Cases/Allowing_Specific_Page_on_Facebook/)
Organizations may allow specific Facebook pages (e.g. company page) while blocking the rest. The document explains allowing specific Facebook pages while blocking others. Facebook can be used for business without full social access. Follow the document to allow a specific page on Facebook.

### [Block Advertisements and Banners](/docs/Use_Cases/Block_Advertisements_And_Banners/)
Ads and banners consume bandwidth and can introduce tracking or malware. The document describes blocking ads and banners from websites to improve experience and reduce risk. Users see fewer distractions and less exposure to ad-based threats. Use the document to block advertisements and banners.

### [Block Emails or Files, Including Archives or Social Posts Using Keywords](/docs/Use_Cases/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/)
Sensitive content in emails, files, archives, or social posts must be blocked by policy. The document covers blocking based on keyword matches in emails, files, archives, and social posts. DLP and content filtering apply across channels. Follow the document to configure keyword-based blocking.

### [Block Inappropriate Images Using Image Analyzer](/docs/Use_Cases/Block_inappropriate_images_by_using_Image_Analyzer/)
Inappropriate or non-compliant images in web content create policy and compliance risk. The document explains using SafeSquid Image Analyzer to block inappropriate images. Visual content is analyzed and blocked when it matches policy. Use the document to configure image analyzer blocking.

### [Block Particular User Login to Facebook or Gmail](/docs/Use_Cases/Block_Particular_User_Login_To_Facebook_Or_Gmail/)
Specific users may be blocked from logging into Facebook or Gmail while others are allowed. The document describes blocking certain users from logging into Facebook or Gmail. Policy applies by user or group. Follow the document to block particular user login to Facebook or Gmail.

### [Block Personal Gmail, Allow Google Corporate Accounts](/docs/Use_Cases/Block_Personal_Gmail_Allow_Google_Corporate_Accounts/)
Personal Gmail may be blocked while Google Workspace (corporate) accounts are allowed. The document covers header manipulation and policy so only corporate Google domains are allowed. Data and productivity stay on approved channels. Use the document to block personal Gmail and allow corporate accounts.

### [Facebook Read-Only Mode](/docs/Use_Cases/Facebook_Read_Only_Mode/)
Organizations may allow Facebook viewing but prevent commenting, liking, or posting. The document explains read-only mode so Facebook access is allowed without engagement actions. Reduced risk of misuse while preserving limited access. Follow the document to configure Facebook read-only mode.

### [Block Specific YouTube Channel](/docs/Use_Cases/Block_Specific_Youtube_Channel/)
Specific YouTube channels may be blocked while other video content is allowed. The document describes blocking specific YouTube channels while allowing other videos. Granular control supports policy and acceptable use. Use the document to block a specific YouTube channel.

### [Restrict AnyDesk](/docs/Use_Cases/Restrict_anydesk/)
AnyDesk or similar tools may be restricted by user, time, or destination. The document covers restricting AnyDesk usage based on security policies. Remote access is controlled without blocking all use. Follow the document to restrict AnyDesk.

### [YouTube API Integration With SafeSquid To Allow Specific YouTube Videos](/docs/Use_Cases/YouTube_API_Integration_With_SafeSquid_To_Allow_Specific_YouTube_Videos/)
Only specific YouTube videos may be allowed for training or approved content. The document explains YouTube API integration so SafeSquid can allow specific videos. Fine-grained control supports education or approved media. Use the document to allow specific YouTube videos via API integration.

### [Native Sandboxing](/docs/Use_Cases/Native_Sandboxing/)
Suspicious web content should be isolated and inspected before reaching users. The document describes SafeSquid native sandboxing to isolate and inspect content. Threats are contained and analyzed before delivery. Follow the document to configure native sandboxing.

### [Elevated Privacy](/docs/Use_Cases/Elevated_Privacy/)
Third-party tracking and fingerprinting should be reduced for user privacy. The document covers blocking third-party cookies, hiding referrers, and anonymizing user-agent data. Users gain privacy and tracking is reduced. Use the document to configure elevated privacy.

### [Working of Default Entries in Access Restrictions](/docs/Use_Cases/working_of_default_entries_in_access_restrictions/)
Default access restriction policies control baseline web access and must be understood. The document explains how default entries in access restrictions control access for users, groups, and applications. Administrators can tune or override defaults with clarity. Follow the document to understand default entries in access restrictions.

## Next steps

Configure [Access Restriction](/docs/Access_Restriction/main/) and [Profiling Engine](/docs/Profiling_Engine/main/) for policy; see [Troubleshooting](/docs/Troubleshooting/main/) if a use case does not behave as expected.
