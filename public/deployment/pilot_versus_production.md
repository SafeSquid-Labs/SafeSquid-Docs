---
title: Pilot Versus Production
description: Decide what the first SafeSquid deployment has to prove, and which controls must be owned before a pilot can widen into production traffic.
keywords:
  - SafeSquid pilot deployment
  - proxy rollout stages
  - controlled pilot
  - production cutover
  - deployment change control
---

# Prove the Control Before You Widen It

A pilot that skips inspection, authentication, and logging proves only that packets can traverse the proxy. Production then surfaces every deferred decision at once — certificate warnings, unattributed logs, business apps breaking — and the fastest workaround anyone reaches for is disabling the control.

Treat the first deployment as a measured pilot with a defined exit condition, not a smaller version of production.

## Decide what the pilot has to prove

| Stage | What it must demonstrate | Exit condition |
|---|---|---|
| Pilot | Traffic flows, activation holds, logs record attributable requests, certificate trust works on a managed endpoint | Every check in [Production-Readiness Checklist](/getting_started/verify_your_setup) passes for the pilot group |
| Limited production | Policy behaves for a real business group under real load | No unexplained bypasses; exceptions have named business owners |
| Full production | Capacity holds at peak, evidence is retained and reportable | Sizing confirmed against measured peak; retention and forwarding proven |

Run the pilot with the production control set enabled. A pilot without HTTPS inspection or authentication measures a different system from the one you intend to ship.

## Confirm ownership before the pilot starts

Before onboarding users, confirm:

- A deployment owner and change record are defined.
- The `activation_key` storage location is approved and access-controlled.
- Topology, sizing, firewall, DNS, NTP, and rollback decisions are documented.
- A Root CA rollout path exists for managed endpoints.
- Log retention and reporting ownership are assigned.

Any item without a named owner is the item that stalls the widening. Assign it before the pilot rather than during the escalation.

## Keep the pilot reversible

The pilot's value depends on being able to undo it quickly and visibly:

- Prefer explicit proxy configuration for pilot clients even when transparent interception is the production target — it makes the affected endpoint obvious and the rollback a single setting.
- Keep the pilot group small enough that a rollback is a message, not an incident.
- Record which client, which setting, and which owner for each change, so the rollback does not depend on memory.

Fail closed rather than open where the choice exists. A pilot client that loses web access reports itself immediately; a pilot client that silently browses unfiltered does not.

## Capture pilot evidence

Store these artifacts with the deployment record:

- The pilot group definition, and the business owner who approved it.
- Completed readiness checks for the pilot window.
- Measured peak concurrent connections during the pilot, for [Sizing](/deployment/sizing).
- Any exception granted during the pilot, with its business justification and owner.
- The rollback method used or rehearsed, and its owner.

## Troubleshoot pilot-to-production gaps

| Symptom | Likely cause | Fix |
|---|---|---|
| Pilot passes, production drops sessions | Pilot ran without inspection, or below peak concurrency | Re-measure with the production control set at the peak window |
| Users bypass the proxy during the pilot | Rollback was easier than reporting a problem | Shorten the feedback path and make bypass visible in the access log |
| Widening stalls repeatedly | An unowned prerequisite surfaces each time | Reconcile the ownership list above before the next stage, not during it |
| Exceptions accumulate without review | No business owner recorded at the time of the grant | Attach an owner and a review date to every exception before production |

## Next steps

- [Deployment Checklist](/getting_started/install_safesquid/prerequisites) - confirm readiness before the pilot installs.
- [Production-Readiness Checklist](/getting_started/verify_your_setup) - the pilot's exit condition.
- [Resource Planning](/deployment/resource_planning) - record what the pilot measures.
