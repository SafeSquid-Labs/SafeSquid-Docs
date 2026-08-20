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

   ![Chrome menu](/images/How_To/How_To_configure_Proxy_In_a_Browser/image1.webp)

   ![Settings option](/images/How_To/How_To_configure_Proxy_In_a_Browser/image2.webp)

2. Click the **System** tab or search for "proxy".

   ![System tab](/images/How_To/How_To_configure_Proxy_In_a_Browser/image3.webp)

   ![Search proxy](/images/How_To/How_To_configure_Proxy_In_a_Browser/image4.webp)

3. Click **Open your computer's proxy settings**.

   ![Proxy settings](/images/How_To/How_To_configure_Proxy_In_a_Browser/image5.webp)

4. Enable **Use a proxy server**.

   ![Enable proxy](/images/How_To/How_To_configure_Proxy_In_a_Browser/image6.webp)

   ![Proxy toggle](/images/How_To/How_To_configure_Proxy_In_a_Browser/image7.webp)

5. Enter the proxy server IP address and port **8080**.

   ![Proxy address](/images/How_To/How_To_configure_Proxy_In_a_Browser/image8.webp)

6. (Optional) Enter bypass addresses.

   ![Bypass list](/images/How_To/How_To_configure_Proxy_In_a_Browser/image9.webp)

7. Click **Save**.

   ![Save settings](/images/How_To/How_To_configure_Proxy_In_a_Browser/image10.webp)

### Firefox

1. Open Firefox menu and click **Settings**.

   ![Firefox menu](/images/How_To/How_To_configure_Proxy_In_a_Browser/image11.webp)

   ![Firefox settings](/images/How_To/How_To_configure_Proxy_In_a_Browser/image12.webp)

2. Navigate to **Network Settings** in General section.

   ![Network Settings](/images/How_To/How_To_configure_Proxy_In_a_Browser/image13.webp)

3. Click **Settings**.

   ![Settings button](/images/How_To/How_To_configure_Proxy_In_a_Browser/image14.webp)

4. Select **Manual proxy configuration** and enter proxy details.

   ![Manual proxy](/images/How_To/How_To_configure_Proxy_In_a_Browser/image15.webp)

5. Click **OK** to save.

   ![Save](/images/How_To/How_To_configure_Proxy_In_a_Browser/image17.webp)



## Next steps

- [Forward Proxy](/Forward_Proxy) for HTTP/HTTPS explicit proxy.
- [Transparent Proxy](/Transparent_Proxy) for interception without client config.
- [Proxy Chain](/Proxy_Chain) for forwarding to a parent proxy.

