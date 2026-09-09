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

### [Custom Templates](/use_cases/customisation/custom_templates)
Organizations face user confusion when blocked content displays generic error messages without branding or escalation procedures. Custom templates enable branded error pages in any language with company logos, help desk contacts, and policy explanations. User awareness and corporate identity improve while support tickets decrease. Use the document to configure custom templates for blocking scenarios.

### [Startup Parameters](/use_cases/customisation/startup_parameters)
Default SafeSquid configurations may not match enterprise requirements for threading, memory, logging, cluster sync, or socket tuning. Startup parameters control listening interfaces, thread management, buffer sizes, and master-slave configurations. Organizations optimize proxy performance and enable clustering or remote logging. Use the document to configure startup.ini and tune the proxy.

## Next steps

After tuning, verify with Verify your setup and [Performance Plot](/use_cases/performance_acceleration/performance_plot); for clustering see [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering).
