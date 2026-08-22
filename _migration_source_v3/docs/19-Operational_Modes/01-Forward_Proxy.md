---
title: Forward Proxy
description: Configure web browsers to use SafeSquid proxy server, including detailed steps for Chrome and Firefox proxy settings to access the SafeSquid WebGUI.
keywords:
  - Configure proxy in browser
  - Set proxy in Chrome for SafeSquid
  - Firefox manual proxy configuration
  - SafeSquid browser setup
  - Access SafeSquid WebGUI
---


# Forward proxy requires explicit client configuration



## Why explicit proxy is used

Uncontrolled direct internet access increases malware, data loss, and compliance risk. SafeSquid provides a browser-based WebGUI at `http://safesquid.cfg` (an embedded Rest UI interface built into SafeSquid; accessible via proxy, NOT resolved by DNS) for configuration and management. Clients must send traffic through SafeSquid by configuring the browser or system proxy. Forward (explicit) proxy gives administrators clear control over which applications use the proxy and supports per-browser or per-application rollout.



## Benefits of forward proxy mode

Explicit configuration ensures only intended traffic is inspected. Policy enforcement and logging apply to configured clients. No network-layer redirection is required; deployment fits environments where endpoint configuration is manageable. **Limitation:** Applications that do not use the configured proxy bypass SafeSquid unless system-wide or PAC-based proxy is used.



## Prerequisites

**Client-side:** Browser supporting manual proxy configuration (Chrome, Firefox, or equivalent). SafeSquid proxy IP and port (default 8080). **SafeSquid-side:** SafeSquid deployed and listening on the proxy port; WebGUI reachable via proxy at `http://safesquid.cfg` (embedded interface, NOT DNS-resolved).



## Configure proxy in Chrome (system settings)

1. Open Chrome browser settings from the toolbar.

   ![Chrome menu](/img/How_To/How_To_configure_Proxy_In_a_Browser/image1.webp)

   ![Settings option](/img/How_To/How_To_configure_Proxy_In_a_Browser/image2.webp)

2. Click the **System** tab in Settings, or search for "proxy" in the search bar.

   ![System tab](/img/How_To/How_To_configure_Proxy_In_a_Browser/image3.webp)

   ![Search proxy](/img/How_To/How_To_configure_Proxy_In_a_Browser/image4.webp)

3. Click **Open your computer's proxy settings**.

   ![Proxy settings link](/img/How_To/How_To_configure_Proxy_In_a_Browser/image5.webp)

4. Enable **Use a proxy server**.

   ![Enable proxy](/img/How_To/How_To_configure_Proxy_In_a_Browser/image6.webp)

   ![Proxy toggle](/img/How_To/How_To_configure_Proxy_In_a_Browser/image7.webp)

5. Enter the proxy server IP address and port **8080**.

   ![Proxy address and port](/img/How_To/How_To_configure_Proxy_In_a_Browser/image8.webp)

6. (Optional) Enter domains and IP addresses to bypass the proxy in the exclusion field:
   - Example: `infatica.io`, `192.158.1.38`, addresses starting with `127.`

   ![Proxy bypass list](/img/How_To/How_To_configure_Proxy_In_a_Browser/image9.webp)

7. Click **Save**.

   ![Save settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image10.webp)



## Configure Proxy in Firefox

Firefox allows browser-specific proxy configuration without affecting system-wide settings.

1. Open Firefox and click the **menu button** (three horizontal lines) in the top right corner.

   ![Firefox menu](/img/How_To/How_To_configure_Proxy_In_a_Browser/image11.webp)

2. Click **Settings**.

   ![Firefox settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image12.webp)

3. Scroll down to **Network Settings** in the General section.

   ![Network Settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image13.webp)

4. Click the **Settings** button.

   ![Settings button](/img/How_To/How_To_configure_Proxy_In_a_Browser/image14.webp)

5. Select **Manual proxy configuration**.

   ![Manual proxy option](/img/How_To/How_To_configure_Proxy_In_a_Browser/image15.webp)

6. Enter the proxy server address and port number.

   ![Proxy details](/img/How_To/How_To_configure_Proxy_In_a_Browser/image16.webp)

7. Click **OK** to save changes.

   ![Save Firefox settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image17.webp)



## Verify configuration

Open `http://safesquid.cfg` through the proxy; the SafeSquid WebGUI loads. Browse an external site; traffic appears in SafeSquid access logs from the client IP. **Interface:** Confirm proxy IP and port in browser or system proxy settings. **Logs:** Check `access.log` or Reporting for requests from the client.



## Troubleshooting

| Symptom | Likely cause | Resolution |
|--------|--------------|------------|
| WebGUI or sites do not load | Wrong proxy IP/port or proxy down | Verify SafeSquid is listening on 8080; confirm IP and port in browser. |
| Some sites work, others fail | Bypass list or policy blocking | Review bypass list and access restriction rules. |
| Firefox works, Chrome does not | Chrome using system proxy vs manual | Ensure Chrome proxy settings match intended proxy (system or manual). |

**Escalation:** If connectivity fails after correct configuration, check firewall and SafeSquid service status; contact support with access log excerpts.



## Next steps

- [Transparent Proxy](/docs/Operational_Modes/Transparent_Proxy/) for interception without client proxy configuration.
- [Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/) for PAC file, system-wide, and enterprise deployment.
- [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/) to confirm end-to-end connectivity.

