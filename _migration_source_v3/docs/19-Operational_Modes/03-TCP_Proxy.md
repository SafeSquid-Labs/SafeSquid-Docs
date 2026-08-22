---
title: TCP Proxy
description: Configure SafeSquid TCP Proxy mode to handle non-HTTP TCP connections, enabling secure proxying of various TCP-based protocols and applications.
keywords:
  - SafeSquid TCP proxy
  - TCP tunnel proxy
  - non-HTTP proxy SafeSquid
  - TCP protocol proxy
  - SafeSquid connect method
---


# TCP proxy handles non-HTTP protocols



## When to use TCP proxy

HTTP/HTTPS traffic is handled by SafeSquid's HTTP proxy. Applications using other TCP-based protocols (e.g. custom ports, non-web services) need a way to route through the proxy. TCP Proxy mode enables SafeSquid to accept and forward non-HTTP TCP connections so all TCP traffic can be funneled through the gateway. Clients still configure the proxy (e.g. browser or system proxy); SafeSquid forwards the TCP stream to the destination.



## Configure TCP proxy in browser

### Chrome (System Settings)

1. Open Chrome browser settings from the toolbar.

   ![Chrome menu](/img/How_To/How_To_configure_Proxy_In_a_Browser/image1.webp)

   ![Settings option](/img/How_To/How_To_configure_Proxy_In_a_Browser/image2.webp)

2. Click the **System** tab or search for "proxy".

   ![System tab](/img/How_To/How_To_configure_Proxy_In_a_Browser/image3.webp)

   ![Search proxy](/img/How_To/How_To_configure_Proxy_In_a_Browser/image4.webp)

3. Click **Open your computer's proxy settings**.

   ![Proxy settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image5.webp)

4. Enable **Use a proxy server**.

   ![Enable proxy](/img/How_To/How_To_configure_Proxy_In_a_Browser/image6.webp)

   ![Proxy toggle](/img/How_To/How_To_configure_Proxy_In_a_Browser/image7.webp)

5. Enter the proxy server IP address and port **8080**.

   ![Proxy address](/img/How_To/How_To_configure_Proxy_In_a_Browser/image8.webp)

6. (Optional) Enter bypass addresses.

   ![Bypass list](/img/How_To/How_To_configure_Proxy_In_a_Browser/image9.webp)

7. Click **Save**.

   ![Save settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image10.webp)

### Firefox

1. Open Firefox menu and click **Settings**.

   ![Firefox menu](/img/How_To/How_To_configure_Proxy_In_a_Browser/image11.webp)

   ![Firefox settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image12.webp)

2. Navigate to **Network Settings** in General section.

   ![Network Settings](/img/How_To/How_To_configure_Proxy_In_a_Browser/image13.webp)

3. Click **Settings**.

   ![Settings button](/img/How_To/How_To_configure_Proxy_In_a_Browser/image14.webp)

4. Select **Manual proxy configuration** and enter proxy details.

   ![Manual proxy](/img/How_To/How_To_configure_Proxy_In_a_Browser/image15.webp)

5. Click **OK** to save.

   ![Save](/img/How_To/How_To_configure_Proxy_In_a_Browser/image17.webp)



## Next steps

- [Forward Proxy](/docs/Operational_Modes/Forward_Proxy/) for HTTP/HTTPS explicit proxy.
- [Transparent Proxy](/docs/Operational_Modes/Transparent_Proxy/) for interception without client config.
- [Proxy Chain](/docs/Operational_Modes/Proxy_Chain/) for forwarding to a parent proxy.

