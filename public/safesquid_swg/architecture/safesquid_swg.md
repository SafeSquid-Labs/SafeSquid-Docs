---
title: SafeSquid SWG Overview
slug: /SafeSquid_SWG
description: SafeSquid Secure Web Gateway overview — software-defined deployment, core architecture, enforcement components, intelligence feeds, browser security, and operational services.
keywords:
  - SafeSquid SWG
  - Secure Web Gateway
  - Web Proxy
  - Application Layer Firewall
  - Configuration Portal
  - Proxy Cluster
  - Zero-Trust Web Security
---

# SafeSquid SWG architecture and components

## Problem statement

Enterprise web traffic is now the delivery path for phishing, ransomware, shadow IT, remote administration abuse, session hijacking, and data exfiltration. If the organisation cannot inspect and govern HTTP and HTTPS at Layer 7, it cannot reliably separate legitimate business use from malicious or unsafe use.

## Client scenario

Use this overview when you need to understand what SafeSquid actually is before you deploy it, size it, or integrate it. This page is especially relevant when you are deciding:

- where to place the enforcement point
- how to onboard users and applications
- how to handle TLS inspection and identity-aware policy
- which supporting services and cloud dependencies must be available

## Key benefits

- Software-defined deployment on generic Linux-compatible x86_64 platforms rather than proprietary hardware
- Layer 7 enforcement through an HTTP(S) proxy architecture
- Scale-up through SMP-aware multi-core execution and scale-out through clustering
- Intelligence-driven decisions using cloud-delivered feeds for URL, application, malware, SSL, image, content, and threat context
- SIEM-ready logging and reporting for audit, investigation, and operational monitoring
- Agent-less browser security patterns that reduce endpoint deployment friction

## Core architecture

SafeSquid SWG is a purpose-built HTTP(S) proxy for enterprise secure web gateway deployments. It is described internally as a software-defined appliance: the product runs as software on standard server or cloud infrastructure rather than on vendor-locked hardware.

The architecture combines these main components:

1. **SafeSquid SWG Proxy** as the core inspection and enforcement engine
2. **Policy Management and Configuration Interface** for administration
3. **AD/LDAP Integration** for identity and group-aware policy
4. **SSL Inspection** for decrypt-inspect-re-encrypt workflows
5. **Reporting and Analytics** for evidence, investigation, and usage visibility
6. **Cloud Intelligence Feeds** for URL, malware, application, SSL, and other updates
7. **Cluster Management** for scale-out and policy consistency

## Deployment model

SafeSquid supports on-premise, off-premise, and hybrid deployment patterns. Cloud-init deployment paths are documented for major cloud providers, while on-premise deployments use either the SafeSquid Appliance Builder or Linux-based installation paths.

This flexibility matters because deployment location changes trust boundaries:

- on-premise keeps policy execution, TLS interception, and logs inside the enterprise-controlled boundary
- cloud-hosted deployments reduce hardware dependency but require careful network and dependency planning
- hybrid models let organisations place enforcement near different traffic sources while keeping a common control model

## Product capabilities that shape the architecture

### Intelligence-driven enforcement

SafeSquid consumes named cloud-based feeds for:

- threat intelligence
- URL classification
- application identification
- image analysis AI
- content fingerprints
- malware signatures
- geo-location
- SSL updates

These feeds matter because many web decisions cannot be made from static policy alone. Classification, malware detection, SSL trust evaluation, and application recognition depend on current intelligence.

### Browser security modes

SafeSquid documents two browser-security modes:

- **Native Browser Sandboxing** through CSP sandbox header injection
- **Remote Browser Isolation (RBI)** for isolated browsing sessions

These modes matter for high-risk browsing scenarios where policy alone is not enough and the organisation needs stronger containment of active web content.

### Logging and evidence

SafeSquid generates detailed access logs and can stream them to SIEM platforms that accept UDP log input. Confirmed integrations include Splunk, IBM QRadar, ArcSight, and ELG-based reporting stacks.

This is important because a web control that cannot produce usable evidence creates false assurance. Security teams need request-level history, privileged-access records, and policy outcomes for investigations and audits.

## Component map

### [Configuration Portal](/Configuration_Portal)

Use this interface to configure policy, SSL inspection, authentication, DLP, and operational settings.

### [Application Ecosystem](/Application_Ecosystem)

Use this page to understand how the proxy, feeds, portal, reporting, backup, DNS, and supporting services fit together.

### [SafeSquid Proxy Cluster](/SafeSquid_Proxy_Cluster)

Use this page to understand scale-out, policy replication, and resilience patterns.

### [Self-Service Portal](/safesquid_swg/interface/self_service_portal)

Use this portal for activation keys, licensing workflows, and cloud-managed operational dependencies.

### [Reporting Service](/Reporting_Service)

Use this service for operational visibility, dashboards, and audit evidence workflows.

### [Integrated DNS Security](/Integrated_DNS_Security)

Use this page to understand how SafeSquid extends protection into DNS-layer risk such as malicious resolution and tunnelling abuse.

### [Supporting Services](/safesquid_swg/interface/supporting_services_monit)

Use the supporting services pages for Monit, BIND, and NTP because those services directly affect reliability, DNS performance, authentication, and TLS validation.

## Related controls / next steps

- [What is SafeSquid SWG](/safesquid_swg/what_is_safesquid_swg) for the security problem and product role
- [Application Ecosystem](/Application_Ecosystem) for feed, portal, reporting, and supporting-service relationships
- [SafeSquid Proxy Cluster](/SafeSquid_Proxy_Cluster) for resilience and scale
- [Deployment Planning](/deployment/deployment_planning) for sizing, dependencies, and rollout preparation
