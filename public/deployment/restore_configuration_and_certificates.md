---
title: Restore Configuration and Certificates
description: Restore SafeSquid policy and SSL material onto a rebuilt or new appliance, and verify what the restore did not bring back.
keywords:
  - SafeSquid restore
  - cloud restore procedure
  - config.xml restore
  - SSL root certificate recovery
  - appliance rebuild
---

# Restore Policy, Then Rebuild the Rest

Cloud Restore brings back policy and SSL material bound to the activation key. It does not bring back the host — networking, OS configuration, and integration secrets stay missing, and a restore declared complete before those are checked leaves a proxy that looks configured and cannot pass traffic.

Restore in two halves: what the backup covers, then what it does not.

## Validate prerequisites

Confirm:

- SafeSquid is installed on the new or rebuilt appliance.
- The **same** activation key used for the backup is available. The backup is bound to it.
- The build record for the original host is at hand, for the settings the backup excludes.
- Cloud Restore was configured on the original appliance. See [Configure Cloud Restore](/use_cases/customisation/configure_cloud_restore).

## Restore the backed-up material

<Steps>
  <Step title="Activate with the original key">
    Activate the rebuilt appliance using the same activation key that produced the backup.

    Confirm activation succeeds and the licensed state is visible in the [Configuration Portal](/safesquid_swg/interface/configuration_portal).

    If activation fails, resolve it before attempting restore — the restore prompt only appears for an activated instance.
  </Step>
  <Step title="Trigger Cloud Restore">
    Select **Cloud Restore** in the Configuration Portal.

    Confirm the restore prompt appears. It is shown only when SafeSquid finds a cloud backup matching the activation key.

    If no prompt appears, the key does not match the backup. Check the key before assuming the backup is gone.
  </Step>
  <Step title="Restart to apply">
    Restart SafeSquid so the restored configuration takes effect.

    Confirm the service returns to a running state after the restart.

    If the service fails to start, inspect the service log before re-running the restore.
  </Step>
</Steps>

These files are restored:

| Path | Holds |
|---|---|
| `/usr/local/safesquid/security/policies/config.xml` | All policies and settings |
| `/usr/local/safesquid/security/ssl/ROOT_X509File.cer` | SSL root certificate |
| `/usr/local/safesquid/security/ssl/ROOT_PrivateKeyFile.pem` | SSL private key |

Restoring the original Root CA is what keeps already-deployed client trust valid. A rebuilt appliance with a newly generated CA forces a fresh trust rollout to every endpoint — which is usually discovered when users start seeing certificate warnings.

## Verify what was restored

1. Open the Configuration Portal.
2. Navigate to **Configure → Access Restriction**, or any configured section.
3. Confirm policies match the state from the original appliance.
4. Check the SSL certificate under **SSL Inspection**, and confirm the certificate details match the original CA.
5. Test a client connection through the rebuilt appliance.

Expected result: policies, user groups, and SSL certificates match the backed-up configuration, and a pilot client's request appears in the access log.

## Restore what the backup excluded

These are not in the cloud backup. Re-apply each from the build record:

- Interface IP address, hostname, and routing.
- DNS and NTP configuration.
- Directory integration secrets and external connector settings.
- Operating system configuration and hardening.
- Log forwarding destinations and credentials.

Verify traffic flows end to end through the rebuilt appliance before returning it to production. See [Production-Readiness Checklist](/getting_started/verify_your_setup).

## Capture restore evidence

Store these artifacts with the incident or change record:

- The date of the restore and the backup version it recovered.
- Confirmation that the restored Root CA matches the original, with issuer detail.
- The list of excluded items re-applied, and by whom.
- Client-side proof that traffic passes through the rebuilt appliance.
- Any policy difference found between the restore and the expected state.

## Troubleshoot restore failures

| Symptom | Likely cause | Fix |
|---|---|---|
| No restore prompt appears | Activation key differs from the one that made the backup | Activate with the original key; the backup is bound to it |
| Policies restore, clients still fail | Network settings were not re-applied | Restore interface, routing, and DNS from the build record |
| Clients see certificate warnings after restore | A new Root CA was generated instead of restoring the original | Confirm the restored `ROOT_X509File.cer` matches the deployed CA; re-run the restore if it does not |
| Directory authentication fails | Integration secrets are outside the backup scope | Restore LDAP credentials from their own approved store |
| Restore recovers an unwanted configuration | Single-version retention overwrote the good backup | See the retention constraint in [Backup Strategy](/use_cases/scaling_and_high_availability/disaster_recovery) |

## Next steps

- [Configure Cloud Restore](/use_cases/customisation/configure_cloud_restore) - set up or repair the backup path.
- [Backup Strategy](/use_cases/scaling_and_high_availability/disaster_recovery) - understand what the backup covers.
- [Production-Readiness Checklist](/getting_started/verify_your_setup) - re-validate before returning to production.
