---
title: "Admin Guide"
description: Configure, secure, and operate the SafeSquid Secure Web Gateway from first login through steady-state administration.
keywords:
  - SafeSquid admin guide
  - SafeSquid configuration
  - secure web gateway administration
  - SafeSquid policy management
  - SafeSquid operations
---

# Configure and Operate SafeSquid

SafeSquid only enforces the policy it is actually configured with. This section takes an administrator from first login through network setup, HTTPS inspection, policy and profile configuration, content filtering, malware protection, performance tuning, and the reporting and system operations that keep the gateway running day to day.

## Quickstart path

1. **[First configuration](/admin_guide/start_here/first_configuration)** - go from a service check to a working Allow rule and your first content policy.
2. **[Architecture and request pipeline](/admin_guide/start_here/architecture)** - understand how a request moves through SafeSquid before changing anything that sits in its path.
3. **[Network settings and listeners](/admin_guide/network_and_access/network_settings_and_listeners)** - confirm the proxy is listening where clients expect it.
4. **[Access Profiles](/admin_guide/policies_and_profiles/access_profiles)** - understand how policy decisions are evaluated and applied.
5. **[HTTPS inspection](/admin_guide/https_inspection/https_inspection)** - decide whether and how encrypted traffic is inspected.
6. **[Logging and troubleshooting](/admin_guide/start_here/logging)** - confirm the evidence trail exists before you need it.

## Next steps

- [Network and access](/admin_guide/network_and_access/network_settings_and_listeners) - configure listeners, access restrictions, and upstream proxies.
- [Policies and profiles](/admin_guide/policies_and_profiles/access_profiles) - build the policy decisions SafeSquid enforces.
- [Malware and data protection](/admin_guide/malware_and_data_protection/clamav) - configure content scanning and data-loss controls.
