---
title: Configure Web Security Policies
description: Production sequence for turning SafeSquid proxy traffic into inspected, attributed, logged, and auditable web security controls.
keywords:
  - SafeSquid policy
  - web security configuration
  - SSL inspection
  - authentication
  - access restriction
  - DLP
  - malware scanning
  - audit evidence
---

# Turn Proxy Traffic Into Enforced Controls

Routing traffic through SafeSquid proves reachability, but it does not finish the deployment. Production value starts when SafeSquid decrypts approved HTTPS sessions, attributes requests to users, applies policy, blocks unsafe activity, and records evidence for operations, audit, and incident response.

## Validate prerequisites

Before enabling baseline controls, confirm:

- SafeSquid is installed and activated.
- A pilot client generates access-log entries.
- Root CA rollout ownership is assigned.
- Authentication source and group mapping are known.
- Log retention or forwarding is approved.
- A rollback path exists for each policy stage.

## Apply controls in order

Use this sequence to reduce outage risk and preserve evidence quality.

| Step | Control | Why it comes here |
|---|---|---|
| 1 | SSL inspection readiness | HTTPS must be visible before content controls can inspect encrypted traffic |
| 2 | Authentication | User attribution improves policy scope and audit value |
| 3 | DNS security | Name-resolution controls reduce exposure before HTTP policy decisions |
| 4 | Access restriction | Category and application rules enforce acceptable use |
| 5 | Malware scanning | Downloads and content streams are inspected before delivery |
| 6 | DLP | Uploads and posts are inspected after identity and inspection are stable |
| 7 | Reporting | Logs and reports prove control effectiveness |

## Start with inspection

Deploy Root CA trust before enabling broad HTTPS inspection. Do not ask users to bypass certificate warnings; that normalizes man-in-the-middle risk and weakens audit defensibility.

Verification:

- A pilot HTTPS site loads without browser certificate warnings.
- SafeSquid logs the HTTPS transaction.
- Excluded destinations are documented with business justification.

## Add user context

Connect authentication before writing broad user or group policies. Use directory integration where possible so logs identify the user, group, source, destination, policy, and action.

Verification:

- A test user appears in the access log.
- Group-scoped policy applies only to the intended pilot group.
- Failed authentication has a clear user-facing and operator-facing signal.

## Enforce acceptable use

Start with pilot groups and high-confidence categories. Block only what the business has approved, and keep a documented exception path for business-critical sites.

Verification:

- A blocked category produces the expected block page.
- An allowed business site remains reachable.
- The access log records the matched policy and action.

## Scan content before delivery

Enable malware scanning and content controls after routing, activation, inspection, and identity are stable. This prevents noisy troubleshooting where certificate, routing, and scanning failures overlap.

Verification:

- A safe test download is allowed and logged.
- A controlled malware-test file or approved test pattern is blocked according to policy.
- Scan failures produce actionable logs.

## Control outbound data

Enable DLP only after HTTPS inspection and user attribution are validated. DLP without decrypted traffic and identity produces weak enforcement and weak evidence.

Verification:

- A test upload containing the approved test pattern is blocked.
- The log records the source user, destination, matched control, and action.
- Business-approved uploads still work.

## Prove the baseline

Store:

- Root CA rollout evidence.
- Authentication test result.
- Allowed and blocked URL category tests.
- Malware scanning test result.
- DLP test result.
- Access-log samples from `/var/log/safesquid/access/extended.log`.
- Reporting Service or SIEM forwarding evidence.
- Rollback steps for every enabled control.

## Troubleshoot policy rollout

| Symptom | Likely cause | Fix |
|---|---|---|
| HTTPS sites show warnings | Root CA trust is missing | Deploy Root CA through GPO, MDM, or approved trust process before retesting |
| Policy does not match user | Authentication or group mapping is incomplete | Verify the user identity in access logs before changing policy |
| Block rule affects business apps | Scope is too broad or bypass is missing | Narrow the rule to target categories, users, or destinations and document exceptions |
| DLP does not trigger | HTTPS inspection is missing or test content does not match | Confirm decrypted traffic and use an approved test pattern |
| Reports are empty | Traffic bypasses SafeSquid or reporting is not connected | Verify access logs first, then reporting integration |

## Next steps

- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - deploy trusted HTTPS inspection.
- [Authentication](/use_cases/authentication/authentication) - add user and group attribution.
- [Reporting Service](/safesquid_swg/interface/reporting_service) - preserve operating and audit evidence.
