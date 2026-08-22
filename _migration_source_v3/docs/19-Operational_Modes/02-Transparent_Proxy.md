---
title: Transparent Proxy
description: Deploy SafeSquid in transparent proxy mode to intercept HTTP/HTTPS without client config for policy enforcement and SSL inspection.
keywords:
  - SafeSquid transparent proxy
  - Configure SafeSquid inline proxy
  - HTTP/HTTPS interception SafeSquid
  - Transparent SSL proxy SafeSquid
  - SafeSquid proxy redirection setup
---


# Transparent proxy intercepts traffic without client configuration



## Why transparent proxy is used

Uncontrolled direct internet access increases malware, data loss, and compliance risk. A secure web gateway (SWG) intercepts and examines web traffic so the organization can enforce policy and block threats. Explicit proxy requires every browser or application to be configured; transparent proxy uses network-level redirection so traffic is sent to the proxy without endpoint configuration. Applications believe they connect directly to the destination; in reality, a router or firewall redirects traffic to SafeSquid, which then forwards it. This reduces deployment effort and ensures all HTTP/HTTPS traffic from the segment is inspected.



## Client scenario
Stark Tech has 200 employees. Stark Tech wants to provide internet services to the employees through WIFI. When the employees open their web browser, they're connected to a proxy server that manages all the network's communication.

Since this is a new employee, the proxy displays a web page in the browser asking the employee to agree to certain terms and conditions. If the employee accepts, then the proxy routes its traffic to the actual destination using a transparent proxy.



## Transparent proxy intercepts without application awareness

A transparent proxy (inline, intercepting, or forced proxy) sits between the client and the internet and redirects requests and responses. The application is not configured to use a proxy; the user is unaware. SafeSquid supports HTTP and HTTPS in transparent mode (HTTPS is SSL transparent mode). Servers see traffic as coming from the proxy.



## How SafeSquid transparent proxy works
![Diagram how SafeSquid proxy works](/img/Troubleshooting/Transparent_proxy/image1.webp)

Bob is using a laptop in Stark Tech and wants to access internet services via Stark Tech's WIFI network.

Bob enable WIFI on his laptop.

Identified Stark tech WIFI network and tried to connect to Stark tech WIFI.

Now admin of the Stark tech receives an IP address of Bob (say 192.168.24.20) to check filtering policies, and serve traffic.

The traffic will come to the router and the router will send traffic to SafeSquid Secure web gateway with ports 80 and 443 respectively.

The **redirection rules on the SafeSquid Secure web gateway** will redirect traffic to SafeSquid Proxy with port 8080 and 8443 (SSL transparent) respectively (By enabling IP forwarding).

When Bob sets SafeSquid Proxy IP address 192.168.221.222 as a gateway, Bob will get access to the WIFI network and he can access all HTTP as well as HTTPS websites transparently.

SafeSquid transparent proxies are extremely versatile.

The following list contains the usefulness of SafeSquid transparent proxy to Bob.

1. **Proxy caches** create copies of the data stored on a server and serve the cached content to Bob. This reduces the strain on the web service by having the proxy provide the content instead of the service itself.
1. **Filtering proxies** prevents access to certain websites or web services. These are commonly implemented by organizations to prevent users from accessing resources that are unrelated or disruptive to the organization.
1. **Gateway proxies modify or block network traffic** based on certain policies. Locations that offer public Wifi often implement gateways that require users to register or accept an agreement before they can use the service.



## Prerequisites
1. Deploy SafeSquid Secure web gateway (SAB).
1. Enable SafeSquid SSL transparent facility on two ports, one is port 8081 for HTTP traffic and the other one is port 8433 for HTTPS traffic. Also, Enable SSL Inspection to control SSL traffic. If not enabled, refer to the document - How to Enable HTTPS Inspection
1. Redirect traffic from ports 80 and 443 to 8081 and 8443 respectively. The redirection can take place on the router if the router supports redirection.
1. Make sure the IP tables-persistent package is installed (to save IP table rules)
1. If your router only supports traffic forwarding then you should redirect traffic on the SafeSquid server using IP tables.
1. Configure Transparent proxy



## Benefits

1. Transparent proxies are an **unobtrusive way** to add features and functionality to a user's browsing experience.
1. **Enterprises experience greater control** over how their customers interact with their services by routing and modifying requests as they come in.
1. **Users interact with web services more easily** since their connections are seamlessly and invisibly passed through the proxy, leaving configuration to the service providers.



## Next steps

- [Forward Proxy](/docs/Operational_Modes/Forward_Proxy/) for explicit browser configuration.
- [TCP Proxy](/docs/Operational_Modes/TCP_Proxy/) for non-HTTP protocols.
- [Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) for SSL transparent mode.

