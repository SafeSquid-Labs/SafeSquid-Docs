---
title: Customisation
slug: /Customisation
description: "Customize SafeSquid's behavior through custom templates for error pages and branding, and startup parameters for performance tuning and operational configuration."
keywords:
  - SafeSquid customization
  - custom templates
  - startup parameters
  - proxy configuration
  - SafeSquid tuning
---


# Customize SafeSquid templates and startup parameters

SafeSquid customization covers custom templates (error pages, branding) and startup parameters (performance and operational configuration). The documents below describe each.



## Custom templates and startup configuration guides

### [Custom Templates](/docs/Customisation/Custom_Templates/)
Organizations face user confusion when blocked content displays generic error messages without branding or escalation procedures. Custom templates enable branded error pages in any language with company logos, help desk contacts, and policy explanations. User awareness and corporate identity improve while support tickets decrease. Use the document to configure custom templates for blocking scenarios.

### [Startup Parameters](/docs/Customisation/Startup_Parameters/)
Default SafeSquid configurations may not match enterprise requirements for threading, memory, logging, cluster sync, or socket tuning. Startup parameters control listening interfaces, thread management, buffer sizes, and master-slave configurations. Organizations optimize proxy performance and enable clustering or remote logging. Use the document to configure startup.ini and tune the proxy.

## Next steps

After tuning, verify with [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/) and [Performance Plot](/docs/Audit_Forensics/Performance_Plot/); for clustering see [Proxy Clustering](/docs/Proxy_Clustering/main/).
