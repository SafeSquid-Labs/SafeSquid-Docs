---
title: Performance Accelerators
slug: /Performance_Accelerators
description: "Advanced performance optimization through intelligent caching, prefetching, bandwidth management, and WCCP integration for enterprise web security"
keywords:
  - SafeSquid performance optimization
  - web caching SafeSquid
  - bandwidth management proxy
  - WCCP integration SafeSquid
  - content prefetching
  - proxy performance tuning
  - web acceleration
  - cache optimization
---


# Caching, prefetch, and bandwidth control

SafeSquid Performance Accelerators improve delivery through caching, prefetching, bandwidth management, speed limits, and WCCP integration. The documents below cover configuration for each feature.



## Performance accelerator guides

### [Caching](/docs/Performance_Accelerators/Caching/)
Organizations face bandwidth constraints and latency issues when users repeatedly access the same web content, resulting in increased costs and poor user experience. Content Caching enables SafeSquid to store frequently accessed web content locally, serving cached copies instead of fetching fresh content from origin servers. This caching mechanism reduces bandwidth consumption, improves response times, and decreases server load while maintaining content freshness through intelligent cache management. Configure content caching in SafeSquid's Application Setup to enable intelligent content storage and delivery optimization.

### [Pre Fetching](/docs/Performance_Accelerators/Pre_Fetching/)
Users experience delays when accessing web content that requires multiple round trips or contains embedded resources that load sequentially, creating poor user experience and reduced productivity. Pre Fetching enables SafeSquid to anticipate user needs and proactively fetch content before explicit requests, reducing perceived latency and improving browsing experience through intelligent prediction algorithms. This prefetching capability ensures faster content delivery while optimizing bandwidth usage and server resources. Configure prefetching rules in SafeSquid's Application Setup to enable predictive content delivery and performance optimization.

### [Manage Bandwidth](/docs/Performance_Accelerators/Manage_Bandwidth/)
Organizations need granular control over bandwidth allocation to prevent congestion and ensure fair use. Bandwidth Management enables SafeSquid to control download speed, maximum download size, and upload size per user through the Limits feature. Critical applications and user groups can be prioritized. Configure bandwidth and data-handling policies in Application Setup using this document.

### [Speed Limits](/docs/Performance_Accelerators/Speed_Limits/)
Per-user or per-group bandwidth consumption must be capped to prevent abuse and ensure fair sharing. Speed Limits allow administrators to control download and upload speeds for users, groups, or content types. Connection-level rate limits enforce policy and protect network capacity. Configure speed limits in SafeSquid using this document.

### [WCCP](/docs/Performance_Accelerators/WCCP/)
Enterprise networks require seamless integration with existing routing infrastructure to enable transparent proxy deployment and load distribution across multiple proxy instances. WCCP integration enables SafeSquid to participate in Web Cache Communication Protocol for automatic traffic redirection, load balancing, and failover management through router-based traffic steering. This integration capability ensures transparent proxy operation while providing scalability and high availability through intelligent traffic distribution. Configure WCCP integration in SafeSquid's network settings to enable router integration and transparent proxy deployment.

## Next steps

For high availability see [Proxy Clustering](/docs/Proxy_Clustering/main/); for operational modes see [Transparent Proxy](/docs/Operational_Modes/Transparent_Proxy/) and [WCCP](/docs/Performance_Accelerators/WCCP/).
