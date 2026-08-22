---
title: Register and Get Your Key
description: Create a SafeSquid account and download your activation key from the Self-Service Portal.
keywords:
  - SafeSquid registration
  - SafeSquid activation key
  - SafeSquid account
---

# Register and Get Your Key

**Goal:** Obtain an activation key so you can license SafeSquid after installation. Registration is free and takes about two minutes.

:::tip Already registered?
[Sign in to the Self-Service Portal](https://key.safesquid.com) to download your existing key.
:::

:::info Prerequisites

- A browser with internet access
- A valid email address (for account activation and key delivery)
- Network access to `https://key.safesquid.com` (no proxy required for registration)

:::

:::tip Use Your Business Email

Using a corporate email domain (not Gmail, Yahoo, Outlook personal) unlocks enterprise account benefits:
- Priority support during POC
- Team member invitations
- Extended trial options

:::

## Registration Process

1. **Sign up** at [https://key.safesquid.com](https://key.safesquid.com). Enter your email, name, and captcha, then click **Register**.

   ![Sign up form](/img/License_Activation/image2.webp)
   *Registration form — enter your business email, name, and complete captcha*

2. **Check your inbox** for the activation email and click **Click here to activate your account**.

   ![Email confirmation](/img/License_Activation/image3.webp)
   *Activation email — click the "Click here to activate your account" link*

3. **Set a password** and click **Activate**.

   ![Activate account](/img/License_Activation/image6.webp)
   *Password setup — choose a strong password and click Activate*

4. **Sign in**, complete your profile, then click **Download Key**.

   ![Download key](/img/License_Activation/image12.webp)
   *Portal dashboard — click Download Key to save the activation_key file*

The downloaded file is named `activation_key` (no extension), typically 1-5 KB in size.

## About Your Activation Key

- **Validity:** The key does not expire. You can use it to activate SafeSquid instances at any time.
- **Reusability:** One key can activate multiple SafeSquid nodes in your deployment (use the same key for HA clusters).
- **Re-download:** Sign in to the [Self-Service Portal](https://key.safesquid.com) anytime to download your key again if lost.
- **File integrity:** Do not rename or modify the `activation_key` file — SafeSquid will reject tampered keys.

## Troubleshooting

Most registration issues resolve by checking spam filters or trying a different browser. If problems persist, contact support with your registered email address.

**Common issues:**

- **Activation email not received?** — Check spam/junk folder. Wait 5 minutes, then try registering again with the same email (duplicate attempts are safe). Still missing? [Contact SafeSquid support](https://www.safesquid.com/contact-us).
- **Key download fails?** — Ensure you are signed in to the [Self-Service Portal](https://key.safesquid.com). Try a different browser or clear your cache. If the issue persists, [contact us](https://www.safesquid.com/contact-us).
- **Forgot your password?** — Use the password reset link on the [Self-Service Portal](https://key.safesquid.com) login page.
- **Account locked or other issues?** — [Contact SafeSquid support](https://www.safesquid.com/contact-us) with your registered email address.

## Next steps

1. [Install SafeSquid](/docs/Getting_Started/Install_SafeSquid/main/) on your server or VM.
2. After installation, [Activate Your License](/docs/Getting_Started/Activate/) by uploading this key in the SafeSquid interface.
