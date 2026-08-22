---
title: Text Analyzer
description: Configure SafeSquid Text Analyzer to restrict access by keyword-based scoring for inappropriate or unclassified content.
keywords:
  - SafeSquid text analyzer
  - block inappropriate web content
  - content-based filtering
  - keyword scoring filter
  - real-time text analysis SafeSquid
  - web page keyword filtering
  - safe web browsing policies
  - mime type content blocking
  - block unclassified websites
  - SafeSquid content filter policy
---



## Text Analyzer restricts access by keyword score

The Text Analyzer detects and restricts access to websites that may contain inappropriate or pornographic content using a keyword scoring system.

Text analyzer is particularly useful in detecting unclassified websites that could serve inappropriate content.

This feature can be effectively used to block websites belonging to specific categories, without having to depend on any database.

When a keyword from the list of words specified in an entry is found, the page is given the score specified in that entry. The total score of the page is equal to the sum of the scores of all the rules that match.

When the total score is equal to or greater than the threshold, then the page is blocked.



## Global
![Text-global.jpg](/img/Configure/Real_Time_Content_Activity/Text_analyzer/image1.webp)

### Enabled
Enable or Disable text analyzer section.

**TRUE**: Enable text analyzer section.

**FALSE**: Disable text analyzer section.

### Threshold
The number of the total score must equal or exceed until the page is blocked.

### Template
Templates are used throughout Safesquid as a replacement for pages that can't be displayed due to filtering, error, or other conditions.

Specify the template name to display when this entry matches. Select the name from the template section.

Leave this rule blank, to use the default template.



## Filtering policies
Add new policies here to block websites based on content type.

You can give the score to each policy and the keywords to block inappropriate content.

![Text-policy.jpg](/img/Configure/Real_Time_Content_Activity/Text_analyzer/image2.webp)

### Enabled
Enable or Disable this Policy.

**TRUE**: Enable this entry.

**FALSE**: Disable this entry.

### Comment
For documentation, and future references, explain the relevance of this entry to the deployment policies.

That is, by reading the policies, a future user can understand the purpose of that entry.

### Profiles
Specify the Profiles applicable for this entry.

This entry will be applicable only if the connection has any one of the specified profiles.

Leave it Blank, to apply for all connections irrespective of any applied profile.

To avoid application to a connection that has a profile, use negated profile (!profile).

### Mime type
It's a way of identifying files on the Internet according to their nature and format.

Set this to a specific MIME type when possible; otherwise all files are checked.

A regular expression matching the mime-types this entry policy applies to.

**Example**: text/html, ^image/,^application/, application/x-shockwave-flash.

### Keyword(s)
A regular expression matching anything in the body of the document considered inappropriate, leave blank to match everything.

We can add more than one keyword in a single policy.

**Example: (sex|sexy|porn|pornography).**

### Score
This entry adds to the total score when it matches, this may be a positive or negative integer.

If you mention a keyword as adult, then every time this word is found in the document the score mentioned will be added.

**Example:** If you mentioned the score as 20, then if the word adult is found once in the requested document, 20 will be added, for two times it will be 40, three times it will be 60.



## Example
### Rule#1
**Example:** Block web pages based on defined keywords.

For connections with the profile "TEXT ANALYZER FOR SAFESQUID' will search for the keywords SafeSquid, proxy, swg, web proxy, squid, Perimeter security solution and secure web gateway.

For any keywords matched, the webpage is being scored and if the score reaches equal to or above the thread hold which is 100 web pages will be blocked.

**For example: if the webpage consists of the words SafeSquid then the text analyzer will score as 60, on the next successful match of the defined keyword it will now be 120.**

120 is above the threshold, so the page is blocked and SafeSquid displays the blocked_bypass template.

Text analyzer can be used in situations where uncategorized websites serve inappropriate content.

**Example: Articles, news etc.**

![Slide1-txtAnlyz.webp](/img/Configure/Real_Time_Content_Activity/Text_analyzer/image3.webp)

