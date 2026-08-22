---
title: Content Moderation
slug: /Profiling_Engine/Content_Analyser
description: Configure SafeSquid to filter inappropriate content using custom categorization, image analyzers, and text analyzers for comprehensive content control.
keywords:
  - SafeSquid content moderation
  - image filtering proxy
  - text content analysis
  - inappropriate content blocking
  - content categorization
  - web content filtering
---


# Filter inappropriate content with categorization and analyzers



## Content analysis and inappropriate content blocking

SafeSquid prevents users from accessing inappropriate content such as pornography using categorization, image analysis, and text analysis.



## Prerequisites
HTTPS Inspection must be enabled in SafeSquid. See [How to enable HTTPS Inspection](/docs/SSL_Inspection/main/) if not yet enabled.



## Select the Filters to block
To block inappropriate content from web, SafeSquid provides different types of filters.

If know the domains then you can use **custom categorization** to block all websites.

If you want to block pornographic images, you can use image filter.

If you want to block pornographic content, you can use text analyzer.

SafeSquid provides you with some default rules in "Text analyzer" to block pornographic content from web.

And in image filter also there is one default policy exist, to block the pornographic images.



## Custom Categorization
SafeSquid includes sample policies to support policy creation.

1. In the SafeSquid UI header, click the **Configure** button (top-right corner).

2. In SafeSquid sample policies, locate the "Inappropriate content Strictly block for all users" policy. Enable the relevant policies so they apply.

3. The page shows existing policies. Use the search box to find policies containing 'GLOBAL BLOCK'.

![blocking inappropriate content for all users](/img/How_To/Content_Filtering/image1.webp)

Edit the policy and enable the policy by setting Enabled as TRUE and save (Save button is placed at right bottom)



## Image Analyzer
1. Verify the **Default** section is enabled (default: TRUE).

2. Set the **Global** section to **Enabled: TRUE**.

3. Navigate to **Filtering Policies** and set the policy's **Enabled** field to **TRUE**.

Read more about [How to block inappropriate images by using Image Analyzer](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/)



## Text Analyzer
1. Check the **Default** section (default: **Enabled: FALSE**).

2. Set the **Global** section to **Enabled: TRUE**.

3. Navigate to **Filtering Policies** and set the policy's **Enabled** field to **TRUE**.


Read more about [Image Analyzer](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/) and [Text Analyzer](/docs/Profiling_Engine/Content_Analyser/Text_Analyser/)



## Testing
Accessing pornographic content from a browser shows the SafeSquid blocked template. Pornographic images are blocked by the image analyzer.



SafeSquid’s content moderation engine analyzes and filters web content in real-time to enforce compliance, safety, and productivity policies.



## Included Modules
- [Content Fingerprints](/docs/Profiling_Engine/Content_Analyser/True-Mime_Fingerprints/): Detects true MIME types through content fingerprinting to prevent file extension spoofing and malware disguise
- [Image Analyzer](/docs/Profiling_Engine/Content_Analyser/Image_Analyser_AI/): Detects inappropriate or non-compliant visual content using AI-powered image analysis
- [Text Analyzer](/docs/Profiling_Engine/Content_Analyser/Text_Analyser/): Scans and classifies textual content for profanity, hate speech, and policy violations

Use these tools to build a safer and policy-compliant browsing environment.

