---
title: "SafeSquid SWG"
description: "SafeSquid is a purpose-built inline proxy that inspects every HTTP and HTTPS transaction for threats, policy violations, and data leakage before the connection reaches the internet."
keywords:
  - SafeSquid introduction
  - getting started
  - zero trust web security
  - secure web gateway
  - HTTPS inspection
  - on-premise web security
  - RBI compliance
  - SEBI CSCRF
  - India sovereign proxy
  - squid replacement
---

# Web-Based Threats Bypass Network Perimeter Controls

Zero-hour phishing, ransomware delivery, command-and-control callbacks, credential theft, and confidential data exfiltration routinely transit approved HTTP and HTTPS sessions. Uncontrolled exposure creates financial, operational, legal, and reputational impact, including regulatory action, breach notification obligations, ransomware recovery delays, and loss of stakeholder trust.

Network Firewalls provide packet inspection capabilities to enforce Layer 3 and Layer 4 security policies. Such controls prevent unauthorized connections, but cannot fully interpret the HTTP transaction, user intent, payload semantics, browser behavior, or content risk inside approved web sessions. Layer-7 web security requires an HTTP/HTTPS proxy that can terminate sessions, inspect protocol headers and payloads, apply policy, and generate transaction-level audit evidence before traffic reaches the internet or the endpoint.

# Introducing SafeSquid SWG

SafeSquid deploys as an inline HTTP/HTTPS proxy at the network perimeter. Every web transaction from a configured client is inspected by SafeSquid before reaching the internet. 

SafeSquid enforces Zero-Trust Web Security at Layer 7 by:

* Blocking phishing pages and credential-harvesting sites before users submit credentials, using real-time URL reputation and content analysis
* Stopping ransomware delivery and severing command-and-control channels
* Preventing egress of confidential data across all HTTP and HTTPS channels
* Preventing session hijacking of authenticated web sessions
* Isolating untrusted web content in Remote Browser Isolation (RBI) — an embedded browser at the perimeter renders pages; no active content reaches the endpoint

SafeSquid's inline policy enforcement and per-transaction audit logs satisfy access control, audit retention, and incident response evidence requirements across [NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [PCI-DSS](https://www.pcisecuritystandards.org/document_library/), [HIPAA](https://www.hhs.gov/hipaa/index.html), [ISO 27001](https://www.iso.org/standard/27001), [SOC 2](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services), [RBI Master Direction on IT Governance 2023](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562), [SEBI CSCRF](https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html), and the [DPDP Act](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf).

# How SafeSquid Inspects Every Transaction

![SafeSquid inline proxy architecture: users on the left, SafeSquid proxy in the center terminating TLS, origin servers on the right](/images/ProxyArchitecture.png)

For HTTPS traffic, SafeSquid terminates the client-side TLS session, decrypts the HTTP transaction, inspects the HTTP protocol headers and the payload entities, applies policy, re-encrypts the transaction, and establishes a separate TLS session with the origin server. Specialized security processors operate on the same transaction context in an in-stream inspection pipeline. Malware scanning, DLP, image analysis, homograph detection, content modification, cookie inspection, header controls, and application signatures can evaluate the transaction before the final allow, block, modify, isolate, or log decision. Because processors operate on the same transaction context, policy enforcement avoids fragmented inspection chains and reduces the need for repeated parsing, copying, or handoff between independent tools.

# Start Intercepting Web Traffic

Follow these steps to deploy SafeSquid and begin intercepting every HTTP and HTTPS transaction from enrolled clients.

<Steps>
  <Step title="Register and obtain an activation key">
    Create an account on the [SafeSquid Self-Service Portal](/getting_started/register). The portal generates the activation key on signup.
  </Step>
  <Step title="Plan your deployment">
    [Plan your proxy deployment](/getting_started/deployment_planning) before installing. Choose a proxy topology, size the gateway for user count and throughput, and define high-availability and client rollout requirements.
  </Step>
  <Step title="Deploy the gateway">
    Choose the installation path that matches your infrastructure:

    <CardGroup cols={3}>
      <Card title="Appliance Builder ISO" href="/getting_started/install_safesquid/safesquid_appliance_builder">
        Bare metal or VM — boots and configures a dedicated SafeSquid appliance.
      </Card>
      <Card title="Cloud Deployment" href="/getting_started/install_safesquid/cloud_deployment">
        AWS, Azure, GCP, and DigitalOcean — deploy from a pre-built image or marketplace listing.
      </Card>
      <Card title="Linux Server" href="/getting_started/install_safesquid/linux_server">
        Existing Debian or Ubuntu host — installs SafeSquid alongside current services.
      </Card>
    </CardGroup>
  </Step>
  <Step title="Route client traffic through the proxy">
    [Configure clients](/getting_started/client_configuration/connect_your_client) to route HTTP and HTTPS traffic through SafeSquid. Client routing is required before the admin interface becomes accessible. Options include explicit proxy settings, a PAC file, system-wide proxy configuration, or enterprise GPO rollout.
  </Step>
  <Step title="Access the admin interface">
    [Open the SafeSquid admin interface](/getting_started/access_the_interface) from a browser on the admin network. The Configuration Portal is required to activate the license and configure all policies.
  </Step>
  <Step title="Activate the license">
    [Upload the activation key](/getting_started/activate) to unlock full policy enforcement and SSL inspection. The proxy operates in restricted mode until activation completes.
  </Step>
  <Step title="Configure web security policies">
    [Configure SSL inspection, user identity, URL categories, and DLP rules](/getting_started/configure_web_security_policies). To verify enforcement, browse a blocked URL category from a test client. Confirm the access log shows the transaction with the matched policy rule and disposition.
  </Step>
</Steps>

## Next Steps

- [Troubleshooting](/troubleshooting/troubleshooting) — diagnose proxy connectivity, certificate trust, and policy enforcement failures after deployment
- [SafeSquid SWG Architecture](/safesquid_swg/what_is_safesquid_swg) — understand proxy components, DNS security integration, and reporting modules
