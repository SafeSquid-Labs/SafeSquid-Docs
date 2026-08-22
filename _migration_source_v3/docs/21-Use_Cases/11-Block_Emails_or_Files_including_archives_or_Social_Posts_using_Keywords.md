---
title: Block Emails or Files including Archives or Social Posts using Keywords
description: Block emails, files, archives, and social posts by keyword in SafeSquid for data leakage protection.
keywords:
  - block emails using keywords SafeSquid
  - block archives using keywords SafeSquid
  - content filtering SafeSquid
  - data leakage protection SafeSquid
  - block social media posts SafeSquid
---



## Problem and benefit
When an employee or user on the network leaks confidential information intentionally or unintentionally, the organization can suffer large losses. Data leakage can occur through many channels. Users may upload important documents to the internet; even when content filtering blocks Microsoft Word and Excel uploads, users can create archives and attempt to upload them. Many organizations do not block archive files because administrators use them to transfer large log files. Organizations may protect data from external intruders but not from theft or accidental disclosure by employees and partners, who may copy content from Word or Excel and email it to third parties.

In modern era, these kind of data leaks are become a challenge for organizations. Organizations are in a quest for content filtering software's which can deeply inspect archive files and able to identify whether the archive or emails contains any confidential details of organization. Most of such archive files and emails have important keywords that should be matched while tracing the Data Leakage.

This challenge is also big for security experts because when there is an upload the post data formation is different for Gmail / Google Drive/ Media fire/ Drobox etc. The wide range of formations of post data made it difficult for security experts to derive concrete solution to these challenges.

SafeSquid **Advanced DLP** in **SafeSquid SWG** analyzes post data, inspects archives via file decomposition, and identifies archive files, emails, or social posts containing keyword matches. Administrators can then block uploads by user (e.g. XYZ) or block data transfer to specific destinations (e.g. abcd.com). The Advanced DLP solution is managed from the SafeSquid Self-Service Portal, where administrators create keyword expression matches. SafeSquid SWG downloads those expressions and loads them into memory. When a user uploads an archive or writes an email, SafeSquid SWG analyzes the post data and sends it to the ClamAV daemon for signature verification. When the keyword expression matches the email or file content, ClamAV responds and SafeSquid applies the policy configured for that keyword match.



## [Manage Keyword Signatures using Self Service portal](/docs/Profiling_Engine/Application_Signatures/)



## Configure SafeSquid SWG for using Custom Signatures

On configure page of SafeSquid interface open the Real time content security side menu. Click on Clam antivirus section to configure the policy.

![Select Configure section to Block Emails or Files including archives or Social Posts using Keywords](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image1.webp)

Click on Global part of ClamAV Section and make Enabled as True.

![Select Global part of ClamAV Section and make Enabled as True to Block Emails or Files including archives or Social Posts using Keywords](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image2.webp)

Now click on clamav subsection to configure the policy.

![Select clamav subsection to configure the policy](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image3.webp)

Enable the default policy in the subsection for virus signature detection.

![Enable the default policy in the subsection for virus signature detection](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image4.webp)

The policy appears in the list with the configured name, conditions, and BLOCK action (see screenshot below).

![The default policy in the subsection for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image5.webp)

Click on bottom left Icon to save the configuration.

![Save default policy in the subsection for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image6.webp)

:::note
After configuring the policy as above, go to the Support page and click Refresh to refresh subscription details.
:::



## Testing signature detection
HTTPS Inspection must be enabled in SafeSquid. If not, see [How to enable HTTPS Inspection](/docs/SSL_Inspection/main/).

### Test using office documents
Set proxy in the client browser and open Gmail. Confirm HTTPS traffic is inspected by SafeSquid; otherwise SafeSquid cannot block mail containing the configured keyword(s).

![Testing Signature detection that Block Emails or Files including archives or Social Posts using Keywords](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image7.webp)

Create a dummy Microsoft file containing the configured keywords. Prepare a separate archive file for testing.

![Create a dummy Microsoft file with configured keywords for testing](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image8.webp)

Attach the sample Microsoft file to a mail. SafeSquid blocks the attachment per policy.

![SafeSquid block attachment by default policy for virus signature detection. ](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image9.webp)

That's it. Your created signatures are in the action and your data is safe.

### Test using archive files
Attach the archive file to a mail; SafeSquid blocks the archive per policy.

![Testing using archive files by default policy for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image10.webp)

### Test using emails
Create an email draft using the keywords for which signatures were configured.

Before sending the mail SafeSquid will identify the keywords and will block the mail. You can see that **Save Failed** in gmail compose box.

![Test using emails by default policy for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image11.webp)

In the browser, after clicking Send the mail remains in a sending state and is blocked.

![Test using emails by default policy for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image12.webp)

### Test using social media posts
Open www.facebook.com and log in with test credentials.

Now try to post a status update using your keywords. When you click on submit button, you will not see your post on Facebook page.

![Test using social media posts by default policy for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image13.webp)

Posting the same status from the timeline is also blocked when it contains the configured keywords.

![Test using social media posts by default policy for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image14.webp)

Now try to post the comment, you will not be able to post any comments with those specified keywords.

![Not able to post any comments with those specified keyword due to default policy for virus signature detection.](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image15.webp)

The same test can be run on other sites by posting data containing the configured keywords. SafeSquid blocks posts that contain those keywords.



## Troubleshooting
### Check SafeSquid logs
You can check SafeSquid logs for troubleshooting, if things are not working as explained above.

![If default policy for virus signature detection is not working then refer SafeSquid logs for troubleshooting, ](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image16.webp)

### Check ClamAV daemon status
You can check whether ClamAV daemon is running or not using following command.
```bash
netstat -lnp | grep clamd
```

![Check ClamAV daemon Status in proxy sever command line](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image17.webp)

If you found that ClamAV daemon is not running then restart using following command.
```bash
/etc/init.d/clamav-daemon restart
```
### Check signatures file

If ClamAV service is running then check whether you have signatures database file on disk or not using locate command.
```
   updatedb && locate safesquid.ldb
   /var/lib/clamav/safesquid.ldb
   /var/lib/safesquid/content_signatures/safesquid.ldb
```
### Check ANTIVIRUS profiles applicability

![Check ANTIVIRUS profiles applicability](/img/How_To/Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords/image18.webp)

If you still got any problem, you can send us mail at support@safesquid.net

