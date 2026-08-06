---
title: "Pre-Fetching"
description: "Configure SafeSquid prefetching to accelerate web access by preloading and caching embedded resources like images, improving response time and reducing redundant network requests."
keywords: ["SafeSquid prefetch embedded images", "SafeSquid internet accelerator", "Prefetch HTML content SafeSquid", "SafeSquid caching optimization", "Prefetching configuration SafeSquid"]
---

# Pre-fetch and cache resources referenced in HTML

Prefetching fetches and caches files referenced in HTML before the user requests them, improving load time and reducing origin requests. It applies to a wider set of resources than caching alone.

## Configure prefetching

1. Access the [SafeSquid User Interface](/Configuration_Portal) and click **Configure**. <img src="/images/How_To/Prefetch_embedded_images/image1.webp" alt="Configure page" />
2. Navigate to **Prefetching** under Application Setup. <img src="/images/How_To/Prefetch_embedded_images/image2.webp" alt="Prefetching section" />
3. Ensure **Global** section has **Enabled** set to **True**. <img src="/images/How_To/Prefetch_embedded_images/image3.webp" alt="Global enabled" />
4. Click the **Prefetch** tab. <img src="/images/How_To/Prefetch_embedded_images/image4.webp" alt="Prefetch tab" />
5. Click **Add New** to create a new policy. <img src="/images/How_To/Prefetch_embedded_images/image5.webp" alt="Add new policy" />
6. Enter an appropriate comment for future reference. <img src="/images/How_To/Prefetch_embedded_images/image6.webp" alt="Policy comment" />
7. Specify the HTML tag to analyze for prefetchable URLs. <img src="/images/How_To/Prefetch_embedded_images/image7.webp" alt="HTML tag specification" />
8. Specify the attribute of the HTML tag holding the URL to prefetch. <img src="/images/How_To/Prefetch_embedded_images/image8.webp" alt="Tag attribute" />
9. Specify the regular expression to evaluate discovered URLs in the tag attribute. <img src="/images/How_To/Prefetch_embedded_images/image9.webp" alt="URL regex" />
10. Click **Save Policy**. <img src="/images/How_To/Prefetch_embedded_images/image10.webp" alt="Save policy" />
11. Click **Save Config** to apply the configuration. <img src="/images/How_To/Prefetch_embedded_images/image11.webp" alt="Save config" /> <img src="/images/How_To/Prefetch_embedded_images/image12.webp" alt="Configuration saved" />