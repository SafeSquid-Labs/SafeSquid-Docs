---
title: Allow Specific YouTube Channel and its Playlist
description: Block general YouTube but allow specific channels and playlists in SafeSquid for education.
keywords:
  - allow specific youtube channel SafeSquid
  - SafeSquid youtube playlist access
  - block youtube except channels SafeSquid
  - youtube channel policy SafeSquid
  - SafeSquid content filtering youtube
---



## Client Scenario
Ganpat University provides graduate programs to various colleges. Ganpat University distributes the internet to its students. Ganpat University wants to block entire www.youtube.com for their students, but wants some of the YouTube channels allowed which are helpful for students.

Ganpat University's challenges are:

All Students should not be allowed to access www.youtube.com. If any student tries to access YouTube, the student receives a blocked template.

Only a few of the specified YouTube channels and their playlists should be allowed. This YouTube channel contains educational and knowledge-sharing videos.



## Solution
You can achieve this by creating a policy in the Request Profiles Section and binding it with policies in the Access Profiles Section.



## Prerequisites
HTTPS Inspection should be enabled in SafeSquid. If not enabled, refer to the document - [How to enable HTTPS Inspection](/docs/SSL_Inspection/main/).

You need the YouTube **Channel-ID** and **List-ID** of the playlist you want to allow. You have to extract the Channel-ID and List-ID of the playlist from the YouTube URL before creating rules in SafeSquid.



## Channel-ID and List-ID Extraction
### Extract Channel-ID from YouTube channel

1. Open the YouTube channel to allow. This example uses the CBT Nuggets channel. The **Channel-ID** appears in the referrer URL as the portion after **'channel/'**. Save it for reference.

CBT Nuggets Channel URL: https://www.youtube.com/channel/UClIFqsmxnwVNNlsvjH1D1Aw

**Channel-ID: UClIFqsmxnwVNNlsvjH1D1Aw**

Select any playlist of the channel and click **PLAY ALL**. This example uses the **CBT Nuggets Webinars** playlist.

![Extract Channel-ID from YouTube Channel to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image1.webp)

2. You can extract List-ID from the selected playlist.

**List-ID** is the preceding portion of the URL after the **'&list='** part. Save this part on a notepad for reference.

In our case we have taken playlist **CBT Nuggets Webinars** and its URL is https://www.youtube.com/watch?v=PcB0j6uBJCA&list=PLQVJk9oC5JKo_bMWae3xsavpPMKAzIeGb

Extracted **List-ID: PLQVJk9oC5JKo_bMWae3xsavpPMKAzIeGb**

![Extract List-ID from YouTube Channel to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image2.webp)

Every video in the playlist URL contains the same List-ID.

URL for next video in CBT Nuggets Webinars playlist: https://www.youtube.com/watch?v=q802E2jsByI&list=PLQVJk9oC5JKo_bMWae3xsavpPMKAzIeGb&index=2

**List-ID: PLQVJk9oC5JKo_bMWae3xsavpPMKAzIeGb**

![Verify List-ID from YouTube Channel to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image3.webp)



## Policy Creation
### Create policy in Request Types section

3. After extracting Channel-ID and List-ID, create policies in SafeSquid.

Go to SafeSquid Web-GUI and click on Configure to create Policies.

![Click on Configure to create policy that will allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image4.webp)

4. Click on Custom Settings to open the Request Types Section.
![Click on Custom Settings to open Request Types Section to allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image5.webp)

5. Click on the Request Types Section to create the policy.
![Click on Request Types Section to create the policy to allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image6.webp)

6. Make sure the Global of Request Types Section is Enabled to True.
![Select Global of Request Types Section is Enabled to True to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image7.webp)

7. Click on the Request Types tab to create a new policy.
![Click on Request Types tab to create new policy to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image8.webp)

8. Insert appropriate comments for future use.
![Insert appropriate comment for future use that describe policy of Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image9.webp)

9. Select **YouTube** Channels in the Request Types field.
![Select YouTube Channels in Request Types field to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image10.webp)

10. Add Channel-ID and List-ID in the File field and save the policy. Use the values saved earlier. For the CBT Nuggets channel example, use **(UClIFqsmxnwVNNlsvjH1D1Aw|PLQVJk9oC5JKo_bMWae3xsavpPMKAzIeGb)** in the File field.

![add Channel-ID and List-Id in File Field and Save the policy to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image11.webp)

11. Create new Request Types as **NUGGET CHANNEL** in the Added Request Types Field.
![Create new Request Types as NUGGET CHANNEL in Added Request Types Field to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image12.webp)

12. Save the Policy Created in the Request Types Section.
![Save the Policy Created in Request Types Section to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image13.webp)

### Create policy in Access Profiles section
13. Go to the Access Profiles section to bind with Profiles.

![Select Access Profiles section to bind with Profiles to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image14.webp)

14. Edit these two default policies with the profile name **BLOCK YOUTUBE CHANNEL** as shown below.

:::note
Create two new policies instead of modifying the default policies if preferred.
:::

![Edit these two default policies with profiles name BLOCK YOUTUBE CHANNEL to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image15.webp)

15. Edit the 1st, Policy. Set Enabled to TRUE and Save the Policy.

![Edit one out of two default policy as True with profiles name BLOCK YOUTUBE CHANNEL to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image16.webp)

16. Edit the 2nd, Policy. Set this policy Enabled to TRUE.

![Edit second one out of two default policy as True with profiles name BLOCK YOUTUBE CHANNEL to Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image17.webp)

17. Insert appropriate comments for future use.

![Insert appropriate comment for future use in policy which made to allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image18.webp)

18. Select **NUGGET CHANNEL** in the Request Types field (created in Step 10). Save the policy.

![Select NUGGET CHANNEL in Request Types field in policy that allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image19.webp)

19. After saving, verify the modified policies to confirm they were created correctly.

![saving to confirm whether its created properly or not policy that allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image20.webp)



## Test the Scenario
Now try to open videos other than the CBT Nuggets Webinars playlist of the YouTube Channel CBT Nuggets.

All the other videos will be blocked and the below template will be shown.

![Test policy that Allow Specific YouTube Channel and its Playlist](/img/How_To/Allow_Specific_YouTube_Channel_and_its_Playlist/image21.webp)

You can check the videos from the CBT Nuggets Webinars playlist of the CBT Nuggets channel. Only these videos will be allowed.

:::note
This configuration will work only for videos sourced from the channel page and not from the feeds links or YouTube Videos embedded in website.

To allow all the videos of any specific YouTube Channel you have to insert List-ID's (of every playlist in that channel) and file part (of each individual unlisted video) of the URL in the File field of the Request Types Section.
:::

