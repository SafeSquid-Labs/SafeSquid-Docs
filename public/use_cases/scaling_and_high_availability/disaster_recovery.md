---
title: Disaster Recovery
slug: /Disaster_Recovery
description: Restore SafeSquid configuration and SSL certificates after failure or in clusters using Cloud Restore and the same activation key.

keywords:
  - SafeSquid disaster recovery
  - SafeSquid cloud restore
  - Restore SafeSquid configuration
  - SafeSquid backup and recovery
  - SafeSquid SSL recovery
---


# Disaster Recovery

## Problem

Hardware failure, disk corruption, or accidental misconfiguration destroys or invalidates SafeSquid policies and SSL material. Rebuilding rules by hand extends outages and risks inconsistency across cluster nodes.

## Benefits

SafeSquid Cloud Restore backs up configuration and certificates to the cloud. The same activation key restores to a rebuilt appliance or a new appliance. Administrators recover policy state quickly and keep cluster members aligned when restore procedures are followed.

## Operational scope

Cloud Restore is one part of disaster recovery, not the whole DR plan. It restores SafeSquid policy state tied to the activation key, but it does not rebuild the host, restore networking, or recover third-party integration secrets.

## Advantages

**Confirmed:** Cloud Restore covers policy configuration (`config.xml`), SSL root certificate and private key, identity and access policy data, and extended policies (DLP, Anti-Virus, etc.) as listed in SafeSquid documentation.

**Confirmed limitation:** System logs, network interface settings, OS configuration, and third-party integration secrets (e.g. LDAP credentials) are outside the backup scope—plan separately.

**Missing:** RPO/RTO numbers for Cloud Restore are not stated here—escalate to CTO for SLA-style claims.

The broader SafeSquid architecture also treats backup and restore as a cloud-backed ecosystem service. Restricted or sovereignty-sensitive deployments should account for that cloud dependency explicitly during DR planning.

## Call to action

Configure Cloud Restore and Monit per [Configure Cloud Restore](/Configure_Cloud_Restore). After changes, use Support → Restart SafeSquid with cloud backup when prompted. Store the activation key in secure recovery runbooks. Test a restore on a non-production appliance before production reliance.



## When to use Cloud Restore

| Scenario | Solution | Benefit |
|---|---|---|
| Hardware failure destroys proxy server | Restore from cloud to new appliance | Resume operations within minutes |
| Accidental policy deletion or misconfiguration | Restore previous version from cloud | Rollback to last known-good state |
| Deploying clustered proxies | Restore master config to new slaves | Replicate policies across nodes |
| Migrating proxy to new hardware | Restore to new appliance with same key | Zero policy recreation effort |

## What gets backed up

**Included in cloud backup:**
- All policy configuration (`config.xml`)
- SSL root certificate and private key
- User groups, identity rules, access policies
- Extended policies (DLP, Anti-Virus, etc.)

**NOT included:**
- System logs
- Network interface settings (IP, hostname)
- Operating system configuration
- Third-party integrations (LDAP credentials, external DB connections)

## Verification and validation

Validate DR readiness on a non-production restore target:

- the same activation key finds the expected backup
- policy state matches the intended version
- SSL material restores correctly
- host-specific settings are re-applied where needed
- client traffic can pass through the rebuilt system

## Backup frequency

- **Automatic backup**: Triggered when you click **Restart SafeSquid** after making configuration changes
- **Manual backup**: Support → Restart SafeSquid (select "Yes" for cloud backup)
- **Retention**: Latest backup overwrites previous (single version stored per activation key)

The document below covers Cloud Restore configuration and usage.



## Disaster recovery configuration guides

### [Configure Cloud Restore](/Configure_Cloud_Restore)
Recovery requires Cloud Restore to be configured and the same activation key. The document covers how Cloud Restore works, required setup (Monit), and step-by-step configuration in the SafeSquid interface. Restoring configuration and SSL certificates from the cloud reduces downtime and rework. Use this document to implement and run disaster recovery.

## Next steps

After configuring Cloud Restore, verify with Verify your setup; for HA see [Proxy Clustering](/Proxy_Clustering).
