---
title: Configuration Sync
description: Discover how to enable configuration synchronization across a SafeSquid proxy cluster to ensure consistent policy deployment, reduce administrative overhead, and improve system reliability and security.
keywords:
  - SafeSquid configuration sync
  - Proxy cluster synchronization
  - SafeSquid master-slave sync
  - Sync proxy configuration SafeSquid
  - SafeSquid centralized policy update
---


# Keep all proxy nodes in sync with master configuration

Without configuration synchronization, each proxy node must be updated manually. Inconsistencies cause policy gaps, vulnerabilities, and extra maintenance. SafeSquid configuration sync propagates policy and settings from the master to slave nodes so all nodes stay uniform and administrative overhead is reduced.

## What gets synced

**Synchronized from master to slaves:**
- Access policies (Access restrictions, Content Security, etc.)
- User groups and identity rules
- SSL Inspection settings
- Application signatures and web categories
- Extended policies (DLP, Anti-Virus, etc.)

**NOT synchronized (local to each node):**
- Network interface settings (IP, ports)
- System logs (each node logs independently)
- Performance counters
- Startup parameters (including master IP/port on slave)

## How sync works

- **Trigger**: Sync occurs automatically when you make configuration changes on the master and apply them
- **Frequency**: Near real-time (within ~1-5 minutes after applying changes on master)
- **Mechanism**: Slaves poll master at regular intervals for configuration updates
- **Restart required**: Some changes (e.g., startup params, network settings) require slave restart to apply



## Prerequisites

- Master and slave instances already connected (see [Master-Slave setup](/Master_Slave))
- If authentication is enabled on master, slave IP must be in Access restrictions → Allow list

**Important**: If proxy authentication is required for all network traffic, create an allow-list policy on the master for the slave proxy IP. Otherwise the slave cannot reach the master Configuration Portal to sync policies.

Below is an example of creating a user group for the slave proxy instance:

![A screenshot of a computer](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image1.webp)

## Configure sync on slave server

Perform these steps on each slave server to enable configuration sync from the master.



## Access the web interface and go to Support
![accessing safesquid web interface and going to support ](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image2.webp)



## Select Startup params
![selecting startup params option](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image3.webp)



## Click on the edit button.
![clicking on edit button](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image4.webp)



## Add the master proxy server IP address
![Adding the master proxy server IP address](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image5.webp)



## Add the master proxy server port number
![Adding the master proxy server port number](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image6.webp)



## Now click on the correct icon to save the configuration.
![clicking on the correct icon to save the configuration](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image7.webp)



## Now click on restart for applying changes.
![clicking on restart for applying changes](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image8.webp)

Click **Yes** to back up SafeSquid configuration to the cloud, or **No** to skip cloud backup.

Click **Submit** after selecting the appropriate option.

![clicking on submit after selecting yes or no for backup configuration](/images/How_to_Setup_Configuration_Sync_in_a_SafeSquid_Proxy_Cluster/image9.webp)

After restart, the slave begins syncing configuration from the master. Policy changes made on the master will propagate to this slave automatically.

## Verify sync is working

1. Make a test policy change on the master (e.g., add a test user group)
2. Apply the change: Configuration Portal → Support → Restart SafeSquid (on master)
3. Wait 1-5 minutes
4. Open Configuration Portal on the slave
5. Verify the test policy appears on the slave

**Expected result**: Changes made on master appear on slave within a few minutes without manual intervention.

## Troubleshooting

**Policies not syncing to slave:**
{/* source: live UI verification, Support → Startup params, and use_cases/scaling_and_high_availability/master_slave.md's own screenshot evidence (image3, image5, image6, image15) */}
{/* NEEDS-SME-REVIEW: this section previously named port 8888 for the telnet check. No UI section or product log on the verified live instance names 8888; the MASTER_PORT field in the linked page's own screenshots is 8080, matching the master's configured LISTEN_PORT, and its raw sync log records the actual sync connection as `192.168.221.222:8080`. Confirm whether 8888 is ever used on some builds — this is the same open question flagged on use_cases/customisation/configure_cloud_restore.md's ":8888" claim and use_cases/scaling_and_high_availability/proxy_clustering.md. */}
- Verify slave Startup params show correct master IP and port: Configuration Portal → Support → Startup params
- Check network connectivity from slave to master's configured LISTEN_PORT (8080 in verified screenshots; confirm the actual value on the master): `telnet <master-ip> <master-port>`
- If authentication enabled, verify slave IP in master Access restrictions → Allow list
- Restart slave: Configuration Portal → Support → Restart SafeSquid

**Sync is slow (>10 minutes):**
- Check network latency between master and slave: `ping <master-ip>`
- Verify master is not overloaded (CPU/memory usage)
- Check slave logs for sync errors: `tail -f /var/log/safesquid/extended.log`

**Changes sync but don't apply:**
- Restart slave to apply configuration changes: Configuration Portal → Support → Restart SafeSquid
- Some changes (network settings, startup params) require manual restart

**Related**: [Master-Slave setup](/Master_Slave), [Configuration Portal](/Configuration_Portal), [Troubleshooting](/Troubleshooting)

