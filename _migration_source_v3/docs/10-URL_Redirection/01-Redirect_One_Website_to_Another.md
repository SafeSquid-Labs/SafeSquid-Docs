---
title: Redirect One Website to Another
description: Configure SafeSquid to redirect one URL to another using Real Time Content Security Redirect policies.
keywords:
  - URL redirection SafeSquid
  - redirect website to another
  - redirection policies
  - Real Time Content Security Redirect
---


# Redirect One Website to Another

### [Access the SafeSquid User Interface ](/docs/SafeSquid_SWG/Configuration_Portal/)
SafeSquid includes sample policies to support policy creation. The sample policy "Enable interface access through authentication" is already present. Enable those policies to make them applicable.

Click on 'Configure' which is at top right of the SafeSquid Interface.

On the left side bar of SafeSquid Interface click on** Real Time Content Security   >> Redirect**

Make the Global Section Enabled to TRUE.

![Global Section Enabled to TRUE to access the SafeSquid User Interface ](/img/How_To/Redirect_One_Website_To_Another_Website/image1.webp)

Click Redirection Policies to see default policies, then add a new policy.

![Default policies in Redirection Policies section](/img/How_To/Redirect_One_Website_To_Another_Website/image2.webp)

Create a policy in **Configure** → **Access Profiles** (or **Templates**) with source/destination and redirect action as in the following example:

![Policy to Redirect One Website To Another Website](/img/How_To/Redirect_One_Website_To_Another_Website/image3.webp)

Click on save (Save button is placed at right bottom)

### Verify redirect
In this the URL value 'rediff.com' is redirect to 'SafeSquid.com' and the port to redirect to 80.

In a browser, open https://www.rediff.com/, it must redirect to SafeSquid.com; verify in SafeSquid under Native logs on SafeSquid interface Reports >> Native logs as like below.

![Verify Redirect One Website To Another Website in Native logs on](/img/How_To/Redirect_One_Website_To_Another_Website/image4.webp)

