---
title: Configure
description: Configure entry point for SafeSquid SWG policy, authentication, SSL inspection, DLP, DNS security, and operational settings.
keywords:
  - SafeSquid configure
  - SafeSquid policy
  - SSL inspection
  - DLP policy
---

# Configure

Use **Configure** as the controlled change path for SafeSquid policy. Changes here influence web access, inspection depth, identity enforcement, logging, and business availability.

Every production change should have a reason, an expected result, a rollback path, and evidence that proves the result. This protects the organization from silent overblocking, accidental bypass, and audit gaps.

## Common configuration domains

| Domain | Use it to control | Evidence to check |
| --- | --- | --- |
| Access restrictions | Category, application, user, group, and time-based access | Reports and `extended.log` |
| Authentication | Identity-aware policy and SSO behavior | Authentication logs and user-attributed reports |
| SSL inspection | HTTPS visibility and selective decryption | Inspection reports and certificate validation results |
| Malware and content security | File, payload, keyword, and content controls | Security events and SIEM records |
| DNS security | Resolution-time blocking and DNS risk signals | DNS events and related reports |

## Change discipline

1. Back up configuration before high-impact edits.
2. Change one policy objective at a time.
3. Test with a known user, destination, and expected outcome.
4. Review Reports before expanding the scope.
5. Retain the change ticket, report evidence, and rollback note.

## Next steps

- Use [Policy Management Console](/safesquid_swg/interface/configuration_portal) for the complete interface guide.
- Use [Reports](/safesquid_swg/policy_management_console/reports) to prove the change worked.
