---
title: Backup Strategy
description: Decide what SafeSquid backs up, what it does not, and what the disaster-recovery plan must cover separately before the deployment depends on Cloud Restore.
keywords:
  - SafeSquid backup strategy
  - SafeSquid cloud restore
  - disaster recovery planning
  - configuration backup scope
  - RTO RPO
---

# Know What the Backup Does Not Cover

Cloud Restore recovers SafeSquid policy state tied to the activation key. It does not rebuild the host, restore networking, or recover third-party integration secrets — and a DR plan that assumes otherwise discovers the gap during the rebuild, with the outage clock running.

Plan the backup around what it actually covers, and cover the rest separately.

## Understand the backup scope

**Included in cloud backup**

- All policy configuration (`config.xml`).
- SSL root certificate and private key.
- User groups, identity rules, access policies.
- Extended policies such as DLP and anti-virus.

**Not included — plan these separately**

- System logs.
- Network interface settings, including IP and hostname.
- Operating system configuration.
- Third-party integration secrets, such as LDAP credentials and external database connections.

**Missing:** RPO and RTO figures for Cloud Restore are not stated here — escalate to the CTO for SLA-style claims.

The broader SafeSquid architecture treats backup and restore as a cloud-backed ecosystem service. Restricted or sovereignty-sensitive deployments should account for that cloud dependency explicitly during DR planning.

## Match the scenario to the recovery

| Scenario | Recovery | Result |
|---|---|---|
| Hardware failure destroys the proxy server | Restore from cloud to a new appliance | Operations resume without policy recreation |
| Accidental policy deletion or misconfiguration | Restore the previous version from cloud | Rollback to the last known-good state |
| Deploying clustered proxies | Restore master config to new slaves | Policy replicated across nodes |
| Migrating the proxy to new hardware | Restore to a new appliance with the same key | Zero policy recreation effort |

## Set the backup cadence

- **Automatic backup** — triggered when you select **Restart SafeSquid** after making configuration changes.
- **Manual backup** — **Support → Restart SafeSquid**, selecting **Yes** for cloud backup.
- **Retention** — the latest backup overwrites the previous one. A single version is stored per activation key.

Single-version retention is the constraint most DR plans miss. There is no point-in-time history to roll back through, so a bad configuration that gets backed up replaces the good one. Take a manual backup before a major change, and keep an exported copy outside the cloud store where the change is significant.

<Accordion title="Disaster recovery checks">
  Before declaring production readiness, confirm:

  - Activation key storage is recoverable without exposing the key contents.
  - Configuration backup and restore are tested.
  - Root CA material, if used, is backed up according to certificate-handling policy.
  - Rebuild steps exist for appliance, cloud, or Linux deployment.
  - DNS, PAC, GPO, MDM, firewall, and route rollback owners are named.
  - A second node or restore target can use the same activation context when cluster or DR behavior requires it.
</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Disaster recovery */}

<Accordion title="Disaster recovery site design">
  A DR stack keeps web security enforced during a regional outage. Without one, a site failure removes the control rather than degrading it, and users either lose internet access or get it unfiltered.

  **Site requirements**

  - **Geography** — a different city, data centre, and power grid than primary. Co-locating the DR stack with production negates continuity.
  - **Capacity** — mirror production sizing across CPU, RAM, NICs, and disk. The DR site carries full load during failover, not a fraction of it.
  - **Configuration** — replicate policy through [Configuration Sync](/use_cases/customisation/configuration_sync) or a documented manual procedure.

  **Recovery objectives**

  - **RTO (Recovery Time Objective)** — how long it may take to redirect traffic to the DR site.
  - **RPO (Recovery Point Objective)** — how much policy and configuration lag is acceptable. Real-time sync approaches zero; manual replication does not.

  **Failover methods**

  | Method | How it works |
  |---|---|
  | DNS-based | Repoint A records at the DR address; recovery time is bounded by record TTL |
  | BGP Anycast | Advertise the same address from the DR site |
  | Load-balancer health check | Balancer withdraws the failed site and redirects automatically |

  Set the RTO and RPO targets with the business, then test failover on a schedule and keep the result as audit evidence. Quarterly is a common cadence.

  **Missing:** recovery-time figures per failover method are not stated here — the legacy source gives numbers, but they are undated and unverified. Escalate to the CTO for SLA-style claims.
</Accordion>

## Validate DR readiness

Validate on a non-production restore target, not on the production appliance:

- The same activation key finds the expected backup.
- Policy state matches the intended version.
- SSL material restores correctly.
- Host-specific settings are re-applied where needed.
- Client traffic passes through the rebuilt system.

## Capture backup evidence

Store these artifacts with the deployment record:

- The date of the last tested restore, and the named owner of the next test.
- The activation key storage location and its access control.
- The list of items covered separately because the cloud backup excludes them.
- The agreed RTO and RPO, and who set them with the business.

## Troubleshoot backup gaps

| Symptom | Likely cause | Fix |
|---|---|---|
| Restore succeeds but the host is unreachable | Network settings are outside the backup scope | Re-apply interface, hostname, and routing from the build record |
| Directory authentication fails after restore | LDAP credentials are not backed up | Restore integration secrets from their own approved store |
| A bad configuration cannot be rolled back | Single-version retention overwrote the good backup | Take a manual backup before major changes and keep an exported copy |
| Restore finds no backup | Different activation key on the restore target | Use the same activation key; the backup is bound to it |
| DR plan cannot be signed off | RTO and RPO were never agreed with the business | Set both targets before relying on the DR stack |

## Next steps

- [Configure Cloud Restore](/use_cases/customisation/configure_cloud_restore) - set up the backup this page plans around.
- [Configuration Sync](/use_cases/customisation/configuration_sync) - keep DR-site policy aligned with production.
- [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) - add failover before relying on restore alone.
