---
title: Pre-Fetching
description: Configure SafeSquid prefetching to accelerate web access by preloading and caching embedded resources like images, improving response time and reducing redundant network requests.
keywords:
  - SafeSquid prefetch embedded images
  - SafeSquid internet accelerator
  - Prefetch HTML content SafeSquid
  - SafeSquid caching optimization
  - Prefetching configuration SafeSquid
---


# Pre-fetch and cache resources referenced in HTML

Prefetching fetches and caches files referenced in HTML before the user requests them, improving load time and reducing origin requests. It applies to a wider set of resources than caching alone.



## Configure prefetching

1. Access the [SafeSquid User Interface](/docs/SafeSquid_SWG/Configuration_Portal/) and click **Configure**.

   ![Configure page](/img/How_To/Prefetch_embedded_images/image1.webp)

2. Navigate to **Prefetching** under Application Setup.

   ![Prefetching section](/img/How_To/Prefetch_embedded_images/image2.webp)

3. Ensure **Global** section has **Enabled** set to **True**.

   ![Global enabled](/img/How_To/Prefetch_embedded_images/image3.webp)

4. Click the **Prefetch** tab.

   ![Prefetch tab](/img/How_To/Prefetch_embedded_images/image4.webp)

5. Click **Add New** to create a new policy.

   ![Add new policy](/img/How_To/Prefetch_embedded_images/image5.webp)

6. Enter an appropriate comment for future reference.

   ![Policy comment](/img/How_To/Prefetch_embedded_images/image6.webp)

7. Specify the HTML tag to analyze for prefetchable URLs.

   ![HTML tag specification](/img/How_To/Prefetch_embedded_images/image7.webp)

8. Specify the attribute of the HTML tag holding the URL to prefetch.

   ![Tag attribute](/img/How_To/Prefetch_embedded_images/image8.webp)

9. Specify the regular expression to evaluate discovered URLs in the tag attribute.

   ![URL regex](/img/How_To/Prefetch_embedded_images/image9.webp)

10. Click **Save Policy**.

    ![Save policy](/img/How_To/Prefetch_embedded_images/image10.webp)

11. Click **Save Config** to apply the configuration.

    ![Save config](/img/How_To/Prefetch_embedded_images/image11.webp)

    ![Configuration saved](/img/How_To/Prefetch_embedded_images/image12.webp)

