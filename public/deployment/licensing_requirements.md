---
title: Licensing Requirements
description: Understand what SafeSquid activation unlocks, how the free and commercial tiers differ, and what licensing state the deployment plan has to assume.
keywords:
  - SafeSquid licensing tiers
  - free versus commercial licence
  - activation key
  - subscription capability
  - licence audit evidence
---

# Know What the Licence Buys

An unactivated instance runs with limited capability regardless of which tier you hold. Planning a deployment around threat intelligence or categorization that the licence does not include produces a control that passes the pilot and fails the first real policy decision.

Settle the tier before sizing and before policy design — both depend on which feeds are available.

## Compare the tiers

SafeSquid offers two licensing tiers.

| Capability | Free | Commercial |
|---|:--:|:--:|
| Core proxy and filtering | Yes | Yes |
| SSL inspection | Yes | Yes |
| Custom policies and profiles | Yes | Yes |
| Real-time threat intelligence | No | Yes |
| URL categorization database | No | Yes |
| Disaster-recovery backup, 365 days | No | Yes |
| Email support | No | Yes |

The free licence has no time limit. Upgrade to commercial at any point through the [Self-Service Portal](https://key.safesquid.com); the deployment steps are the same for both tiers.

## Plan around what the tier excludes

The two exclusions that most often surprise a deployment:

- **[URL categorization](/use_cases/access_restriction/web_categorization).** Category-based access policy is central to most acceptable-use designs. On the free tier those rules have no categorization database behind them, so the policy exists but does not classify.
- **Disaster-recovery backup.** [Configure Cloud Restore](/use_cases/customisation/configure_cloud_restore) depends on the commercial tier. A DR plan built on it needs the licence to match.

Confirm which tier the deployment assumes, and record it, before policy design begins.

## Treat licence state as audit evidence

Activation also matters for audit: licensed state is visible in the [Configuration Portal](/safesquid_swg/interface/configuration_portal) and serves as evidence that the gateway is correctly licensed. The activation key itself is not the audit artifact — store the key securely and capture licence-state evidence from the interface instead.

## Capture licensing evidence

Store these artifacts with the deployment record:

- The tier the deployment assumes, and who approved it.
- The activation key storage location and its access control.
- A record of licensed state from the Configuration Portal.
- The subscription renewal owner, for commercial deployments.

## Troubleshoot licensing assumptions

| Symptom | Likely cause | Fix |
|---|---|---|
| Category rules match nothing | Free tier has no categorization database | Confirm the tier against the policy design; upgrade or redesign the rules |
| Threat intelligence feeds are absent | Free tier excludes real-time intelligence | Plan detection around the feeds the tier includes |
| Cloud Restore is unavailable | DR plan assumes a commercial capability | Confirm the tier before relying on Cloud Restore for recovery |
| Capability disappears after a period | Commercial subscription expired | See [Manage Subscription State](/deployment/manage_subscription_state) |
| Licence state cannot be evidenced | Only the key was stored, not the portal record | Capture licensed state from the Configuration Portal for the deployment record |

## Next steps

- [Register and Get Your Key](/getting_started/register) - obtain the activation key.
- [Activate Your License](/getting_started/activate) - apply it to the instance.
- [Manage Subscription State](/deployment/manage_subscription_state) - handle renewal and expiry.
