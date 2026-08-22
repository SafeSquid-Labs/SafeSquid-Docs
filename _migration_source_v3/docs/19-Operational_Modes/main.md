---
title: Operational Modes
slug: /Operational_Modes
description: "Comprehensive proxy deployment configurations including forward, transparent, TCP, reverse proxy, and proxy chaining for enterprise network architectures"
keywords:
  - SafeSquid operational modes
  - forward proxy configuration
  - transparent proxy deployment
  - reverse proxy SafeSquid
  - proxy chaining
  - TCP proxy mode
  - enterprise proxy deployment
  - network architecture proxy
---


# Proxy deployment modes for enterprise networks

SafeSquid supports forward, transparent, TCP, reverse proxy, and proxy chaining so deployment fits network architecture and security requirements. The documents below describe each mode and how to configure it.



## Configure forward, transparent, TCP, reverse, or chained proxy

### [Forward Proxy](/docs/Operational_Modes/Forward_Proxy/)
Organizations require explicit proxy configuration for controlled environments where users can configure browsers to route traffic through security gateways for policy enforcement and threat protection. Forward Proxy enables SafeSquid to operate as a traditional proxy server requiring explicit client configuration through browser settings, PAC files, or system-level proxy configuration. This deployment mode provides granular control over proxy usage while enabling comprehensive policy enforcement and security monitoring. Configure forward proxy settings in SafeSquid's network configuration to enable explicit proxy deployment with client-side configuration requirements.


### [Transparent Proxy](/docs/Operational_Modes/Transparent_Proxy/)
Organizations need proxy deployment without client configuration without requiring client configuration changes to ensure rapid adoption and comprehensive traffic coverage across all devices and applications. Transparent Proxy enables SafeSquid to intercept web traffic automatically through network-level redirection, providing seamless security enforcement without client-side configuration or user awareness. This transparent deployment ensures comprehensive traffic coverage while maintaining user experience and eliminating configuration complexity. Configure transparent proxy deployment in SafeSquid's network settings to enable automatic traffic interception and seamless security enforcement.


### [TCP Proxy](/docs/Operational_Modes/TCP_Proxy/)
Organizations require proxy functionality for non-HTTP protocols and applications that need TCP-level inspection and control for security coverage across all network protocols. TCP Proxy enables SafeSquid to operate at the TCP layer, providing protocol-agnostic proxy functionality for applications requiring TCP-level inspection, control, and security enforcement. This TCP-level capability ensures comprehensive protocol coverage while maintaining security policies and threat protection across diverse application types. Configure TCP proxy mode in SafeSquid's network settings to enable protocol-agnostic proxy functionality and security coverage.


### [Reverse Proxy](/docs/Operational_Modes/Reverse_Proxy/)
Organizations need to protect internal web servers and applications from direct internet access while providing secure external access through authentication, SSL termination, and load balancing capabilities. Reverse Proxy enables SafeSquid to operate as a server-side proxy, protecting internal resources while providing secure external access through SSL termination, authentication, and traffic management. This reverse proxy deployment ensures internal server protection while enabling secure external access and comprehensive security enforcement. Configure reverse proxy settings in SafeSquid's network configuration to enable server-side protection and secure external access.


### [Proxy Chain](/docs/Operational_Modes/Proxy_Chain/)
Enterprise environments require multi-tier proxy architectures for hierarchical security enforcement, load distribution, and specialized processing across different network segments and security zones. Proxy Chain enables SafeSquid to operate as part of multi-tier proxy architectures, providing hierarchical security enforcement, load distribution, and specialized processing capabilities through intelligent traffic routing and policy coordination. This chaining capability ensures security coverage while supporting complex enterprise architectures and specialized security requirements. Configure proxy chaining in SafeSquid's network settings to enable multi-tier proxy deployment and hierarchical security enforcement.

## Next steps

For client configuration see [Connect Your Client](/docs/Getting_Started/Connect_Your_Client/main/); for transparent redirection see [WCCP](/docs/Performance_Accelerators/WCCP/).
