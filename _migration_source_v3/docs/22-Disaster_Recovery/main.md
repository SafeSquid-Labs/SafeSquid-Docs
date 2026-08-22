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

Hardware failure, disk corruption, or accidental misconfiguration can cause loss of SafeSquid policies and SSL certificates. SafeSquid Cloud Restore automatically backs up configuration and certificates to the cloud; use the same activation key to restore them to the same appliance (after rebuild) or a new appliance.

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

## Backup frequency

- **Automatic backup**: Triggered when you click **Restart SafeSquid** after making configuration changes
- **Manual backup**: Support → Restart SafeSquid (select "Yes" for cloud backup)
- **Retention**: Latest backup overwrites previous (single version stored per activation key)

The document below covers Cloud Restore configuration and usage.



## Disaster recovery configuration guides

### [Configure Cloud Restore](/docs/Disaster_Recovery/Configure_Cloud_Restore/)
Recovery requires Cloud Restore to be configured and the same activation key. The document covers how Cloud Restore works, required setup (Monit), and step-by-step configuration in the SafeSquid interface. Restoring configuration and SSL certificates from the cloud reduces downtime and rework. Use this document to implement and run disaster recovery.

## Next steps

After configuring Cloud Restore, verify with [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/); for HA see [Proxy Clustering](/docs/Proxy_Clustering/main/).
