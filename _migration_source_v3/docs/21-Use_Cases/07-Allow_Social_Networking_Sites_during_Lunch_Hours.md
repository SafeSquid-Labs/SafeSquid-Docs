---
title: Allow Social Networking Sites During Lunch Hours
description: Allow social networking access during lunch hours via SafeSquid time profiles while keeping productivity controls.
keywords:
  - allow social media lunch hours SafeSquid
  - SafeSquid time profile
  - lunch time policy SafeSquid
  - social networking site access SafeSquid
  - safe social media access SafeSquid
---



## Problem: Social networking access must be bounded by time

Unrestricted social networking during work hours can reduce productivity and create policy risk. Many organizations block social networking on network computers. Some organizations allow access during lunch or defined windows to balance productivity and morale. SafeSquid time profiles allow social networking sites only during configured hours (e.g. lunch); outside that window access is blocked.



## Key benefits

Social networking is allowed only during the configured time window. Outside that window users receive a block template. Administrators set the LUNCH (or custom) time profile once; policy applies consistently. Productivity controls remain while offering limited access.



## Prerequisites

- [HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) enabled in SafeSquid.

- SScore section enabled as TRUE (Application setup → Score).
- Access to [SafeSquid Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/).



## Call to action
![Select Configure section to allow social networking sites in lunch hours](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image1.webp)

Open the Search icon (bottom right of SafeSquid Web GUI) to search by keyword or profile name.

![View default policies under policies and profiles](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image2.webp)



## Search default policy: LUNCH.
Enter **LUNCH** in the value field of the search dialog and click Search.

![Search for default policy Lunch](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image3.webp)

The default policy for the **LUNCH** profile appears in the Time Profile section.



## Go to Time Profiler
Open the default policy from the Time Profiler section having a **LUNCH** profile.

![Open the default policy from Time Profiler section having LUNCH profile](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image4.webp)

### Edit LUNCH policy
Set the lunch time (Hour Range and Minute Range) and save the policy.

![Modify lunch time (Hour Range and Minute Range) and save the policy](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image5.webp)

Also, ensure the Global part of the Time Profiler Section is Enabled with TRUE.

![Global part of Time Profiler Section is Enabled with TRUE to allow social networking sites in lunch hours](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image6.webp)

By default, Global Part of Time Profiler is FALSE.

![Save the policy after making Global part of Time Profiler as TRUE.](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image7.webp)

Save the policy after making Global part of Time Profiler as TRUE.

![Save the policy after making Global part of Time Profiler as TRUE.](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image7.webp)



## Go to Access Profiles
Open Access Profiles from the Restriction Policies side menu.

![Open Access Profiles from Restriction Policies side menu to allow social networking sites in lunch hours](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image8.webp)

### Create new policy
Create a new policy under the Access Profiles section for incorporation of the default **LUNCH** profile from the Time Profiler section.

![Create new policy under Access Profiles section for incorporation of default LUNCH profile from Time Profiler section.](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image9.webp)

Select the default Category **Socialnetworks** from the Categories Field.

![Select the default Category Socialnetworks from Categories Field.](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image10.webp)

Select **ALLOW** in the Action field to allow **Social Networking sites** during lunch hours.

![Select ALLOW in Action field to allow Social Networking sites in lunch hours.](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image11.webp)

Specify a unique profile name in the Added Profiles field (e.g. **SOCIAL NETWORKING SITE**).

Click on the top right Icon to save the policy.

![Specify unique profile name inside Added Profiles field and click on top right Icon to save the policy.](/img/How_To/Allow_Social_Networking_Sites_during_Lunch_Hours/image12.webp)



## Verification and Evidence

- During the configured lunch window: access a social networking site; access is allowed.
- Outside the lunch window: access a social networking site; the **BLOCK** template appears.
- **Interface:** Time Profiler shows LUNCH with the correct hour/minute range; Access Profiles shows the policy with Category Socialnetworks, Action ALLOW, and the added profile. Global for Time Profiler is TRUE.



## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Social sites always blocked | Ensure Global (Time Profiler) is TRUE. Confirm the LUNCH hour/minute range includes the current time. Confirm Access Profile has Action ALLOW and Category Socialnetworks. |
| Social sites always allowed | Check policy order; a later ALLOW may override. Confirm the time profile is applied to the Access Profile and the range is correct. |

