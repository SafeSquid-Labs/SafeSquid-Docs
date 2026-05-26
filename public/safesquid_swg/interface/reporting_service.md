---
title: Reporting & Forensics
description: Reporting and forensics in SafeSquid — centralized visibility, SIEM-ready logging, audit evidence, and operational investigation workflows for proxy deployments.
keywords:
  - Secure Web Gateway Components
  - Reporting
  - SafeSquid logging
  - proxy forensics
---


# Reporting & Forensics

Reporting is not optional in an enterprise SWG. If SafeSquid enforces policy but the team cannot prove what happened, who accessed what, which policy fired, or how an override occurred, the control cannot support investigations, audits, or serious operations.

## Problem statement

Distributed proxy nodes, encrypted traffic, identity-aware policy, and exception handling all create evidence that must be retained and searched. When reporting is weak, incident response slows down, audit narratives break, and teams lose confidence in enforcement.

## Client scenario

Use this page when you need to understand how SafeSquid supports:

- centralized visibility across one or more proxy nodes
- forwarding to SIEM or reporting stacks
- forensic use of access, configuration, bypass, privacy, and security logs
- audit evidence for policy enforcement and privileged changes

## Key benefits

- Centralized evidence for multi-node deployments
- Better incident investigation because logs include user, destination, action, and policy context
- Stronger auditability through configuration, bypass, interface, and security records
- Operational flexibility because logs can stay local, feed the Reporting Service, or stream to external SIEM tooling

## What SafeSquid provides

### Centralized reporting and analytics

The Reporting Service is the centralized visibility layer for SafeSquid traffic and policy outcomes. It supports dashboards, reporting workflows, and evidence collection for security operations and audit review.

### SIEM-ready log forwarding

Internal product knowledge confirms that SafeSquid generates detailed access logs consumable by SIEM tools that accept UDP log input. Confirmed compatible destinations include:

- Splunk
- IBM QRadar
- ArcSight
- ELG-based reporting stacks

This matters because many enterprises already standardize on a SIEM. SafeSquid should fit the existing investigation workflow rather than forcing the SOC to use only the proxy-local interface.

### Forensic log classes

SafeSquid documents several log classes that are directly relevant to investigations:

- `extended.log` for detailed request-level activity
- `config.log` for configuration changes and interface actions
- `performance.log` for system behavior and capacity troubleshooting
- `bypass.log` for policy override and bypass-related events
- `privacy.log` for privacy-related records
- native logs for functional and debugging detail

The security posture knowledge base also confirms these evidence-relevant record types:

- UI Access Logs
- Privileged Access Logs
- Bypass Logs
- Deep Content Security Logs
- Content Security Policy Violation Logs

### Evidence value

Use reporting and logging to answer questions such as:

- Which user or group accessed the destination?
- Was the request allowed, blocked, bypassed, or modified?
- Which policy or profile influenced the outcome?
- Did a privileged administrator change configuration before the incident?
- Did SSL inspection, DLP, or malware-related controls trigger?

## Deployment patterns

### Local reporting on a single node

Use this for small or temporary deployments where reporting scale and retention needs are limited.

### Dedicated reporting path

Use a dedicated reporting service or SIEM path when:

- the deployment has multiple proxy nodes
- retention requirements exceed local storage comfort
- the SOC expects centralized search and alerting
- auditors require durable, exportable evidence

### External SIEM integration

Use external SIEM when the organization already has an established investigation platform and wants SafeSquid evidence to appear in the same operational workflow.

## Verification and validation

After deployment, validate all of the following:

- the expected logs are being generated
- forwarded logs arrive in the reporting destination or SIEM
- clustered nodes all contribute events
- user identity appears where authentication is expected
- configuration changes and bypass events are traceable

Useful evidence includes:

- searches for a known test request in `extended.log`
- a visible configuration change in `config.log`
- a known bypass event in `bypass.log`
- confirmation that the external reporting destination receives UDP log traffic

## Troubleshooting guide

**Symptom:** Traffic works, but no events appear in the SIEM.  
**Likely cause:** Log forwarding path, destination listener, or network allowlist is wrong.  
**Isolation:** Confirm local log generation first, then trace the forwarding path to the SIEM collector.  
**Remediation:** Correct forwarding configuration or network access.  
**Retest:** Trigger a fresh test request and confirm it appears in the destination.

**Symptom:** Logs exist, but user attribution is missing.  
**Likely cause:** Authentication is not active for the tested flow, or the request used a bypass path.  
**Isolation:** Compare the request path against authentication policy and identity logs.  
**Remediation:** Correct authentication scope or remove unintended bypass.  
**Retest:** Repeat the same request with an authenticated user and confirm attribution.

**Symptom:** Audit trails do not show who changed policy.  
**Likely cause:** Configuration logging or interface access review is incomplete.  
**Isolation:** Check `config.log`, UI access logs, and privileged-access records.  
**Remediation:** Enable or retain the required evidence path.  
**Retest:** Make a controlled change and confirm it is recorded.

## Related controls / next steps

- [Audit & Forensics](/Audit_Forensics) for the broader logging and evidence model
- [Security Logs](/Security_Logs) for detailed log classes and locations
- [Proxy Clustering](/Proxy_Clustering) for multi-node evidence planning
- [Authentication](/Authentication) for identity-rich reporting
