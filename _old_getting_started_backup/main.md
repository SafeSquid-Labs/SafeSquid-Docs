---
title: Getting Started
description: "Get started with SafeSquid SWG: registration, deployment planning, installation, and client configuration for application-layer web security."
keywords:
  - SafeSquid
  - Secure Web Gateway
  - HTTP Proxy Server
  - Application Layer Security
  - Zero-Trust Web Security
---

## Welcome to SafeSquid!

SafeSquid is the world's most advanced HTTP Proxy Server, specifically designed for Application Layer Security. The purpose-oriented architecture promises scalable performance while ensuring comprehensive mitigation of Layer 7 threats. SafeSquid-based Secure Web Gateway (SWG) shields enterprises from advanced cyber‑threats by delivering robust perimeter-level application layer security.

Learn more [about SafeSquid SWG!](/docs/SafeSquid%20SWG/main)

## In this section

1. **[Registration](/docs/Getting%20Started/Registration)** — Create an account and obtain your activation key.
2. **[Deployment Planning](/docs/Getting%20Started/Deployment%20Planning)** (includes Hardware Provisioning) — Size infrastructure, plan network and storage, and prepare the environment.
3. **[Installation Guide](/docs/Getting%20Started/Installation%20Guide/main)** — Install SafeSquid via Appliance Builder, Private Cloud, or Linux Server.
4. **[Client Configuration](/docs/Getting%20Started/Client%20Configuration/main)** — Configure browsers and clients to use SafeSquid (explicit proxy, PAC, system-wide, enterprise).
5. **[License Activation](/docs/Getting%20Started/License%20Activation)** — Activate your SafeSquid instance with your activation key.

## Typical High-Level Solution Architecture

![Solution Architecture](/img/Getting-Started/Getting_Started_with_SafeSquid_Secure_Web_Gateway/image1.webp)

In a typical organization setting, the amalgamation of [SafeSquid Application Eco-system](/docs/SafeSquid%20SWG/Application%20Ecosystem) constitutes the complete SWG solution.

## Get activation key

The product activation key is the unique secret required to activate and validate the authenticity of your SafeSquid.

To generate the product activation key, create an account on the SafeSquid Self-Service portal. Registration is free and quick and does not require credit card details. Using a business email unlocks enterprise account benefits, like team onboarding and POC support. After registration, download the activation key.

## Installation

You can set up your secure web gateway using different installation mechanisms based on your deployment plan.

### [SafeSquid Appliance Builder (Recommended)](/docs/Getting%20Started/Installation%20Guide/SafeSquid%20Appliance%20Builder)

[SafeSquid Appliance Builder(SAB)](https://downloads.safesquid.com/appliance/safesquid.iso) is a security-enhanced ISO of the latest minimal Ubuntu LTS. On booting from the SAB ISO, Ubuntu is automatically installed, and SafeSquid SWG is downloaded and deployed with all necessary dependency libraries, and services. Using the SAB ISO, you may [create a virtual appliance on any virtualization infrastructure or create a hardware appliance on standard Intel Server hardware.](/docs/Getting%20Started/Installation%20Guide/Linux%20Server)

### SafeSquid On Cloud

To setup SafeSquid SWG on your preferred Cloud PaaS platform or your private cloud infrastructure, use our [cloud-init script](https://raw.githubusercontent.com/SafeSquid-Github/safesquid_cloud-init/main/safesquid_cloud-init.yaml).

### Building from source

If you want to setup SafeSquid on already existing infrastructure or if you want to use another Operating System in the Linux family other than Ubuntu, you can use the [TAR package](https://downloads.safesquid.com/appliance/binary/safesquid-2024.0715.1656.3-swg-concept.tar.gz). You will need to make some additional configurations, like [Monit](/docs/SafeSquid%20SWG/Supporting%20Services/Monit) and [BIND9](/docs/SafeSquid%20SWG/Supporting%20Services/Bind) services used by SafeSquid.

## Activate your SafeSquid

After successful installation, you must [activate your SafeSquid instance](/docs/Getting%20Started/License%20Activation).

Configure your browser to use SafeSquid as the HTTP(S) proxy, access SafeSquid Interface [http://safesquid.cfg/](http://safesquid.cfg/), and upload the activation key.

You can validate the activation under the license details section under the Support tab on the Interface.

:::note

The same key must be uploaded on every SafeSquid instance in the proxy cluster to ensure seamless synchronization between them.

:::

## SSL Inspection

Since most of the web traffic is now encrypted, [enable HTTPS Inspection](/docs/SSL%20Inspection/main) to safeguard from hidden threats.

On the [Self-Service Portal](/docs/SafeSquid%20SWG/Self-Service%20Portal), configure your Enterprise CA (Certificate Authority) as the Root SSL certificate. If you do not have an Enterprise CA, generate SafeSquid 's Self-Signed Certificate. Import the Root SSL certificate into client browsers' trusted authorities.

## User Authentication

SafeSquid SWG has a robust user and group identity management system, with multiple authentication options.

You can set up user authentication based on [device-specific network identifiers](/docs/Authentication/Network%20Signature), or your preferred credential verification system. Integrate with enterprise-grade directory services like [Microsoft® Windows Active Directory](/docs/Authentication/Directory%20Services/Active%20Directory/main),and [OpenLDAP](/docs/Authentication/Directory%20Services/OpenLDAP/main).

Furthermore, configure user verification via [basic authentication](/docs/Authentication/Directory%20Services/OpenLDAP/Simple%20Authentication) or [Kerberos (SSO)](/docs/Authentication/Directory%20Services/OpenLDAP/SSO%20Authentication) for seamless domain network access.

## [Custom Categories](/docs/Profiling%20Engine/Web%20Categorization)

Manually classify websites into custom categories on the SafeSquid Self-Service Portal or SafeSquid interface as per the business use case.

## Security Policies

Achieve Zero-Trust Web Security strategy by enforcing the organization's web usage policies using SafeSquid's Polymath Profiling Engine, and Advanced Traffic Flow Management.

## [Reporting](/docs/Audit%20&%20Forensics/Reporting%20Module)

SafeSquid offers in-depth reporting for process audit, system performance, and traffic forensic analysis. The reporting suite includes detailed web usage reports, threat prevention reports, system reports, and performance reports. An interactive real-time dashboard, also, offers customization, export, and distribution options to suit the organization's needs.

## Integrate with other security systems

Integrate with existing security infrastructure, such as firewalls, endpoint protection platforms, third-party malware detection systems, and SIEM systems, for a cohesive security posture.

## Customization

SafeSquid provides extensive options for customization to meet specific organizational demands and user experiences.

You may alter the dashboard, reporting interfaces, and analytics to suit user preferences and requirements. You can also [customize blocking templates](/docs/Customisation/Custom%20Templates) to conform to organizational branding and communication styles. For specialized tasks and automation, administrators can use our comprehensive customization library or create their custom bash scripts.

## [Troubleshooting](/docs/Troubleshooting/main)

Troubleshooting is a cakewalk for any average Linux technician using the comprehensive SafeSquid Logs.

You will find all the logs under **/var/log/safesquid/** directory. Tweak the LOGLEVEL to control the depth of logging required. In addition to this, you will find prompt assistance from the SafeSquid Community at any time.
