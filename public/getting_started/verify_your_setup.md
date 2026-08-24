---
title: Production-Readiness Checklist
description: Work through the full SafeSquid validation sequence and confirm every control is enforcing, not merely enabled, before routing production traffic.
keywords:
  - SafeSquid production readiness
  - deployment validation checklist
  - proxy go-live checklist
  - integration validation
  - audit evidence
---

# Confirm the Deployment Is Ready

SafeSquid is not production-ready until service state, proxy routing, license status, inspection, policy, and log evidence all agree. This page is the sequence that ties those checks together and the record you keep when they pass.

Each step links to the detailed check. Work them in order — a failure early on makes every later result unreliable.

## Validate prerequisites

Before running the sequence, confirm:

- SafeSquid is installed and activated. Use [Activate Your License](/getting_started/activate) if the license is not active.
- At least one pilot client uses SafeSquid as its proxy. Use [Connect Your Client](/getting_started/client_configuration/connect_your_client) for the routing path.
- You have shell access to the SafeSquid server.
- The test window is approved in the change record.
- Rollback exists for proxy settings, firewall rules, and client routing.

## Run the validation sequence

<Steps>
  <Step title="Prove service and listener state">
    Confirm the proxy listener, process ID, service state, and local DNS resolution in [Service Health](/deployment/service_health).

    Confirm the listener, process, and resolver checks all show SafeSquid is running.

    If any check fails, inspect service logs before routing more users.
  </Step>
  <Step title="Open the interface safely">
    Load the [Configuration Portal](/safesquid_swg/interface/configuration_portal) from an approved management path, following [Access the Management Interface](/getting_started/access_the_interface).

    Confirm the portal loads and the management path used is recorded.

    If the portal does not load, verify browser proxy settings, listener state, and network ACLs.
  </Step>
  <Step title="Confirm activation">
    Check product type, subscription state, and expiry, following [Activate Your License](/getting_started/activate).

    Confirm product, subscription, and expiry details are populated.

    If activation details are missing, re-upload the activation key and test subscription reachability.
  </Step>
  <Step title="Prove client traffic reaches the proxy">
    Run the client-side checks in [Proxy Connectivity](/deployment/proxy_connectivity).

    Confirm the request returns a response and a matching access-log entry appears.

    If the request succeeds with no log entry, the client is bypassing SafeSquid. Treat that as a failure.
  </Step>
  <Step title="Prove HTTPS is inspected">
    Read the certificate issuer as described in [HTTPS Inspection Validation](/deployment/https_inspection_validation).

    Confirm the issuer is the SafeSquid CA for inspected destinations, and the original CA for excluded ones.

    If HTTPS fails with trust warnings, finish Root CA deployment before production inspection.
  </Step>
  <Step title="Prove the audit trail">
    Confirm logs, retention, forwarding, and reports in [Logging and Reporting](/deployment/logging_and_reporting).

    Confirm the evidence path works end to end, not just that the log file exists.

    If reports are empty while access logs are healthy, the reporting integration is the fault.
  </Step>
</Steps>

## Validate production controls

Before routing broad user traffic, confirm these controls are planned or already complete:

- SSL inspection is configured and the SafeSquid Root CA is deployed to managed endpoints.
- Authentication integrates with the approved identity source.
- Baseline access policies block malware, high-risk categories, and unauthorized applications.
- Reporting or log export captures access evidence for incident response.
- High availability is planned with [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) when uptime requirements demand it.
- Support and rollback owners are documented.

{/* source: _migration_source_v3/docs/01-Getting_Started/06-Verify_Your_Setup.md §SafeSquid Integration Validation */}

<Accordion title="Integration validation before production">

Use this once controls are configured, to confirm each one is actually enforcing rather than merely enabled.

**Authentication and identity**

- [ ] Users authenticate with domain credentials through the configured AD or LDAP integration.
- [ ] Usernames, not just IP addresses, appear in `/var/log/safesquid/access/extended.log`.
- [ ] Where group policies are configured, different groups receive demonstrably different policy.

**Policy enforcement**

- [ ] A blocked category is genuinely blocked from a client.
- [ ] Sites are categorized as expected.
- [ ] Time-based policies activate and deactivate on schedule, where configured.
- [ ] HTTPS sites present the SafeSquid certificate once the CA is deployed.

**Security and content filtering**

- [ ] An EICAR test file download is blocked, confirming antivirus scanning is live.
- [ ] Keyword-based content blocking triggers, where enabled.
- [ ] Restricted file types are blocked on upload and download.

**Testing and documentation**

- [ ] Multiple client devices browse successfully through SafeSquid.
- [ ] A documented test case exists for each policy rule.
- [ ] Configuration is backed up, including `/usr/local/safesquid/config/`.
- [ ] A failover and restore procedure is written down and has been tested.

<Note>
  Use the EICAR test file rather than live malware. It is an industry-standard, inert string designed for exactly this check and is safe to transmit on a production network.
</Note>

</Accordion>

Operations and monitoring checks — current logs, update reachability, forwarding, and reports — are covered in [Logging and Reporting](/deployment/logging_and_reporting).

## Capture readiness evidence

Store these artifacts with the deployment record:

- Service, listener, and resolver output from [Service Health](/deployment/service_health).
- Screenshot or record showing active license state.
- HTTP and HTTPS access-log entries from `/var/log/safesquid/access/extended.log`.
- Certificate issuer evidence for an inspected and an excluded destination.
- Pilot client proxy configuration.
- The completed integration checklist above, with the tester named.
- Change record with rollback owner.

This evidence supports SOC 2 change management, ISO 27001 operational control review, and NIST SP 800-53 audit traceability for first deployment.

## Troubleshoot failed checks

| Symptom | Likely cause | Fix | Verify |
|---|---|---|---|
| A step fails before the sequence completes | An earlier control is not yet stable | Stop and fix in order; later results are unreliable until earlier steps pass | The failed step's own page reports a pass |
| License is inactive | Key was not uploaded or subscription path is blocked | Re-upload `activation_key`; allow HTTPS to `api.safesquid.net` | Activation details show active state |
| Controls are enabled but nothing is blocked | Policy scope does not match the pilot group | Confirm user attribution in the access log before changing policy | A blocked category returns the expected block page |
| Different clients get different results | Bypass or PAC exception matches inconsistently | Review bypass lists and PAC logic against the documented scope | All pilot clients produce matching log entries |
| Checklist passes but an auditor query cannot be answered | Evidence was not captured at the time of the test | Re-run the affected check and attach the output to the deployment record | The record contains the artifact for every step |

Escalate to the operations owner if service restart, DNS repair, or activation upload changes production traffic behavior.

## Verification is complete

The setup is ready for policy rollout when service state, interface access, activation status, client routing, HTTPS inspection, and log evidence all pass, and every artifact above is attached to the deployment record.

## Next steps

- [Policy Enforcement](/getting_started/configure_web_security_policies) - enforce the baseline controls in order.
- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - enable HTTPS decryption after CA rollout.
- [Access Restriction](/use_cases/access_restriction/access_restriction) - enforce category and time-based policies.
