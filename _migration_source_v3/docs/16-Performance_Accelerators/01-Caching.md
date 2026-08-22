---
title: Content Caching
description: Configure SafeSquid content caching to improve bandwidth efficiency, reduce latency, and accelerate web access for frequently visited content.
keywords:
  - SafeSquid website caching
  - Configure cache in SafeSquid
  - SafeSquid disk cache management
  - Bandwidth optimization SafeSquid
  - Cache specific URLs SafeSquid
---


# Serve repeated requests from local cache

Content Caching stores local copies of requested pages and files. Later requests for the same content are served from cache instead of the origin, improving bandwidth and latency. SafeSquid provides configurable content caching.



## Configure content caching

### Create Access Policy

1. Access the [SafeSquid User Interface](/docs/SafeSquid_SWG/Configuration_Portal/) and click **Configure**.

   ![Configure page](/img/How_To/Caching_Specific_websites/image1.webp)

2. Navigate to **Access Policies** under Restriction Policies.

   ![Access Policies section](/img/How_To/Caching_Specific_websites/image2.webp)

3. Click **Add New** to create a new policy.

   ![Add new policy](/img/How_To/Caching_Specific_websites/image3.webp)

4. Enter a descriptive comment for reference.

   ![Policy comment](/img/How_To/Caching_Specific_websites/image4.webp)

5. Select the desired categories from the **Categories** dropdown.

   ![Select categories](/img/How_To/Caching_Specific_websites/image5.webp)

6. Set **Action** to **Allow**.

   ![Set action](/img/How_To/Caching_Specific_websites/image6.webp)

7. Assign a unique name in **Added Profiles**.

   ![Added Profiles](/img/How_To/Caching_Specific_websites/image7.webp)

8. Click **Save Policy**.

   ![Save policy](/img/How_To/Caching_Specific_websites/image8.webp)

### Configure Caching Store

9. Navigate to **Caching** under Application Setup.

   ![Caching section](/img/How_To/Caching_Specific_websites/image9.webp)

10. Click the **Store** tab.

    ![Store tab](/img/How_To/Caching_Specific_websites/image10.webp)

11. Click **Clone** to duplicate an existing policy.

    ![Clone policy](/img/How_To/Caching_Specific_websites/image11.webp)

    ![Duplicated policy](/img/How_To/Caching_Specific_websites/image12.webp)

12. Click **Edit Policy** on the cloned entry.

    ![Edit policy](/img/How_To/Caching_Specific_websites/image13.webp)

13. Set **Enabled** to **True**.

    ![Enable policy](/img/How_To/Caching_Specific_websites/image14.webp)

14. Add an appropriate comment for future reference.

    ![Policy comment](/img/How_To/Caching_Specific_websites/image15.webp)

15. Select the profile created earlier from the **Profiles** dropdown.

    ![Select profile](/img/How_To/Caching_Specific_websites/image16.webp)

16. Click **Save Policy**.

    ![Save caching policy](/img/How_To/Caching_Specific_websites/image17.webp)

17. Click **Save** to apply the configuration globally.

    ![Global save](/img/How_To/Caching_Specific_websites/image18.webp)



## Verification and Evidence

18. Navigate to **Manage Cached Objects** in the Caching section.

    ![Manage Cached Objects](/img/How_To/Caching_Specific_websites/image19.webp)

19. Verify cached websites appear under disk cache.

    ![Disk cache contents](/img/How_To/Caching_Specific_websites/image20.webp)

