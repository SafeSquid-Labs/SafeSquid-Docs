---
title: "TCP Proxy"
description: "Configure SafeSquid TCP Proxy mode to handle non-HTTP TCP connections, enabling secure proxying of various TCP-based protocols and applications."
keywords: ["SafeSquid TCP proxy", "TCP tunnel proxy", "non-HTTP proxy SafeSquid", "TCP protocol proxy", "SafeSquid connect method"]
---

# TCP proxy handles non-HTTP protocols

## When to use TCP proxy

HTTP/HTTPS traffic is handled by SafeSquid's HTTP proxy. Applications using other TCP-based protocols (e.g. custom ports, non-web services) need a way to route through the proxy. TCP Proxy mode enables SafeSquid to accept and forward non-HTTP TCP connections so all TCP traffic can be funneled through the gateway. Clients still configure the proxy (e.g. browser or system proxy); SafeSquid forwards the TCP stream to the destination.

## Configure TCP proxy in browser

### Chrome (System Settings)

1. Open Chrome browser settings from the toolbar. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image1.webp" alt="Chrome menu" /> <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image2.webp" alt="Settings option" />
2. Click the **System** tab or search for "proxy". <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image3.webp" alt="System tab" /> <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image4.webp" alt="Search proxy" />
3. Click **Open your computer's proxy settings**. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image5.webp" alt="Proxy settings" />
4. Enable **Use a proxy server**. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image6.webp" alt="Enable proxy" /> <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image7.webp" alt="Proxy toggle" />
5. Enter the proxy server IP address and port **8080**. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image8.webp" alt="Proxy address" />
6. (Optional) Enter bypass addresses. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image9.webp" alt="Bypass list" />
7. Click **Save**. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image10.webp" alt="Save settings" />

### Firefox

1. Open Firefox menu and click **Settings**. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image11.webp" alt="Firefox menu" /> <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image12.webp" alt="Firefox settings" />
2. Navigate to **Network Settings** in General section. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image13.webp" alt="Network Settings" />
3. Click **Settings**. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image14.webp" alt="Settings button" />
4. Select **Manual proxy configuration** and enter proxy details. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image15.webp" alt="Manual proxy" />
5. Click **OK** to save. <img src="/images/How_To/How_To_configure_Proxy_In_a_Browser/image17.webp" alt="Save" />

## Next steps

- [Forward Proxy](/Forward_Proxy) for HTTP/HTTPS explicit proxy.
- [Transparent Proxy](/Transparent_Proxy) for interception without client config.
- [Proxy Chain](/Proxy_Chain) for forwarding to a parent proxy.