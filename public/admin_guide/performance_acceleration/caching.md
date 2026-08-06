---
title: "Content Caching"
description: "Configure SafeSquid content caching to improve bandwidth efficiency, reduce latency, and accelerate web access for frequently visited content."
keywords: ["SafeSquid website caching", "Configure cache in SafeSquid", "SafeSquid disk cache management", "Bandwidth optimization SafeSquid", "Cache specific URLs SafeSquid"]
---

# Serve repeated requests from local cache

Content Caching stores local copies of requested pages and files. Later requests for the same content are served from cache instead of the origin, improving bandwidth and latency. SafeSquid provides configurable content caching.

## Configure content caching

### Create Access Policy

1. Access the [SafeSquid User Interface](/Configuration_Portal) and click **Configure**. <img src="/images/How_To/Caching_Specific_websites/image1.webp" alt="Configure page" />
2. Navigate to **Access Policies** under Restriction Policies. <img src="/images/How_To/Caching_Specific_websites/image2.webp" alt="Access Policies section" />
3. Click **Add New** to create a new policy. <img src="/images/How_To/Caching_Specific_websites/image3.webp" alt="Add new policy" />
4. Enter a descriptive comment for reference. <img src="/images/How_To/Caching_Specific_websites/image4.webp" alt="Policy comment" />
5. Select the desired categories from the **Categories** dropdown. <img src="/images/How_To/Caching_Specific_websites/image5.webp" alt="Select categories" />
6. Set **Action** to **Allow**. <img src="/images/How_To/Caching_Specific_websites/image6.webp" alt="Set action" />
7. Assign a unique name in **Added Profiles**. <img src="/images/How_To/Caching_Specific_websites/image7.webp" alt="Added Profiles" />
8. Click **Save Policy**. <img src="/images/How_To/Caching_Specific_websites/image8.webp" alt="Save policy" />

### Configure Caching Store

9. Navigate to **Caching** under Application Setup. <img src="/images/How_To/Caching_Specific_websites/image9.webp" alt="Caching section" />
10. Click the **Store** tab. <img src="/images/How_To/Caching_Specific_websites/image10.webp" alt="Store tab" />
11. Click **Clone** to duplicate an existing policy. <img src="/images/How_To/Caching_Specific_websites/image11.webp" alt="Clone policy" /> <img src="/images/How_To/Caching_Specific_websites/image12.webp" alt="Duplicated policy" />
12. Click **Edit Policy** on the cloned entry. <img src="/images/How_To/Caching_Specific_websites/image13.webp" alt="Edit policy" />
13. Set **Enabled** to **True**. <img src="/images/How_To/Caching_Specific_websites/image14.webp" alt="Enable policy" />
14. Add an appropriate comment for future reference. <img src="/images/How_To/Caching_Specific_websites/image15.webp" alt="Policy comment" />
15. Select the profile created earlier from the **Profiles** dropdown. <img src="/images/How_To/Caching_Specific_websites/image16.webp" alt="Select profile" />
16. Click **Save Policy**. <img src="/images/How_To/Caching_Specific_websites/image17.webp" alt="Save caching policy" />
17. Click **Save** to apply the configuration globally. <img src="/images/How_To/Caching_Specific_websites/image18.webp" alt="Global save" />

## Verification and Evidence

18. Navigate to **Manage Cached Objects** in the Caching section. <img src="/images/How_To/Caching_Specific_websites/image19.webp" alt="Manage Cached Objects" />
19. Verify cached websites appear under disk cache. <img src="/images/How_To/Caching_Specific_websites/image20.webp" alt="Disk cache contents" />