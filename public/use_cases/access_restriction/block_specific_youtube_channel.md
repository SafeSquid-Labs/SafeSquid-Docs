---
title: "Block Specific YouTube Channel"
description: "Block a specific YouTube channel using SafeSquid by creating policies based on Channel-ID and List-ID for targeted video restriction."
keywords: ["block specific youtube channel SafeSquid", "SafeSquid youtube video restriction", "youtube channel blocking SafeSquid", "SafeSquid block youtube content", "youtube category restriction SafeSquid"]
---

## Problem

Security teams need predictable control over app and web usage to reduce policy bypass and data-risk exposure.

## Benefits

You can enforce policy decisions consistently with SafeSquid while preserving legitimate business workflows.

## Advantages

You keep actionable policy control close to operations, with verifiable outcomes in logs and policy behavior.

## Call to action

Use the steps in this guide to implement the control, then validate behavior with a real user-flow test.

# Block one YouTube channel while allowing other content

Block access to specific YouTube channels (e.g., T-Series) while allowing other YouTube content.

:::note Blocking specific YouTube channels while allowing other videos is a common policy need. The steps below demonstrate blocking a specific channel and its playlist videos. :::

## Prerequisites

- HTTPS Inspection must be enabled in SafeSquid. See [How to enable HTTPS Inspection](/SSL_Inspection).
- Extract the YouTube **Channel-ID** and **List-ID** from the target channel URL

## Extract Channel-ID and List-ID

1. Open the YouTube channel to block (e.g., T-Series).
2. Extract the **Channel-ID** from the URL (the portion after `channel/`):
   - URL: `https://www.youtube.com/channel/UCq-Fj5jknLsUf-MWSy4_brA`
   - **Channel-ID:** `UCq-Fj5jknLsUf-MWSy4_brA` <img src="/images/How_To/Block_Specific_Youtube_Channel/image1.webp" alt="Extract Channel-ID from YouTube Channel" />
3. Click **PLAY ALL** on the channel page to access a playlist.
4. Extract the **List-ID** from the playlist URL (the portion after `&list=`):
   - URL: `https://www.youtube.com/watch?v=IgKdXLfxgQQ&list=PL9bw4S5ePsEE2KMw53rY40A00t4I-otqy`
   - **List-ID:** `PL9bw4S5ePsEE2KMw53rY40A00t4I-otqy` <img src="/images/How_To/Block_Specific_Youtube_Channel/image2.webp" alt="Extract List-ID from YouTube Channel" /> <img src="/images/How_To/Block_Specific_Youtube_Channel/image3.webp" alt="List-ID in subsequent videos" />

## Create Request Types Policy

5. Open SafeSquid WebGUI and click **Configure**. <img src="/images/How_To/Block_Specific_Youtube_Channel/image4.webp" alt="SafeSquid Configure section" />
6. Click **Custom Settings** to open the Request Types section. <img src="/images/How_To/Block_Specific_Youtube_Channel/image5.webp" alt="Custom Settings menu" />
7. Ensure the **Global** setting in Request Types is set to **True**. <img src="/images/How_To/Block_Specific_Youtube_Channel/image6.webp" alt="Enable Global Request Types" />
8. Click the **Request Types** tab to create a new policy. <img src="/images/How_To/Block_Specific_Youtube_Channel/image7.webp" alt="Request Types tab" />
9. Create a new Request Profile named **T-SERIES CHANNEL** in the Added Request Types field. <img src="/images/How_To/Block_Specific_Youtube_Channel/image8.webp" alt="Create T-SERIES CHANNEL profile" />
10. Add the Channel-ID and List-ID to the **File** field using the format:
    ```text
    (UCq-Fj5jknLsUf-MWSy4_brA|PL9bw4S5ePsEE2KMw53rY40A00t4I-otqy)
    ```
    Save the policy. <img src="/images/How_To/Block_Specific_Youtube_Channel/image9.webp" alt="Add Channel-ID and List-ID" />

## Create Access Profiles Policy

11. Navigate to the **Access Profiles** section. <img src="/images/How_To/Block_Specific_Youtube_Channel/image10.webp" alt="Access Profiles section" />
12. Edit the default policy **BLOCK YOUTUBE CHANNELS**:
    - Select **T-SERIES CHANNEL** in the Request Types field
    - Set Action to **DO\_NOT\_BYPASS** <img src="/images/How_To/Block_Specific_Youtube_Channel/image11.webp" alt="Configure Access Profile" />
13. Save the policy. <img src="/images/How_To/Block_Specific_Youtube_Channel/image12.webp" alt="Save policy" />

## Verification and Evidence

14. Access the T-Series channel URL: `https://www.youtube.com/channel/UCq-Fj5jknLsUf-MWSy4_brA` The channel displays the Access Blocked template. <img src="/images/How_To/Block_Specific_Youtube_Channel/image13.webp" alt="Channel blocked" />
15. Access any T-Series playlist video to confirm blocking. <img src="/images/How_To/Block_Specific_Youtube_Channel/image14.webp" alt="Playlist video blocked" />

:::note This configuration blocks videos accessed from the channel page only. Videos from feed links or embedded YouTube videos are not blocked.

To block all videos from a channel, add all playlist List-IDs and individual video file portions to the Request Types File field. :::

## Next steps

- [Allow Specific YouTube Channel and Its Playlist](/Allow_Specific_YouTube_Channel_and_its_Playlist) to allow only approved channels.
- [Access Restriction](/Access_Restriction) for policy and profile configuration.