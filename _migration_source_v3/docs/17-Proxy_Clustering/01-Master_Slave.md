---
title: Master-Slave
description: Configure SafeSquid master-slave architecture for centralized policy sync and reporting across slave instances.
keywords:
  - SafeSquid master-slave configuration
  - Configure SafeSquid slave server
  - Centralized policy management SafeSquid
  - SafeSquid multi-instance setup
  - SafeSquid synchronization
---



## How master-slave works

In a master-slave configuration, one SafeSquid instance (the master) manages policy and reporting for multiple slave instances. Slaves enforce policy and process traffic; master provides centralized control.

**Data flow:**
- **Master → Slaves**: Policies, configuration, tasks
- **Slaves → Master**: Reporting data, logs, statistics

Control and policy flow from master to slaves; reporting data flows from slaves to master:

```mermaid
flowchart TB
    Master[Master SafeSquid]
    Slave1[Slave 1]
    Slave2[Slave 2]
    Master -->|policies and tasks| Slave1
    Master -->|policies and tasks| Slave2
    Slave1 -->|reporting data| Master
    Slave2 -->|reporting data| Master
```

**Slave behavior:**
- Processes client traffic and enforces policy synced from master
- Forwards reporting data to master for centralized analysis
- Operates independently if master is temporarily unavailable (uses last synced policy)

**Master behavior:**
- Does not process client traffic directly
- Aggregates reporting data from all slaves into unified reports
- Pushes policy updates to slaves automatically

## Prerequisites

- SafeSquid installed on all nodes (master and slaves)
- Same activation key on all nodes
- Network access from slaves to master Configuration Portal (port 8888 by default)
- If authentication is enabled on master, slaves must be allowed in Access Restriction → Allow list



## Configure master-slave relationship

Follow these steps to connect a slave instance to a master. Perform slave configuration first, then (if authentication is enabled) configure the master to allow the slave.

## Step 1: Configure slave server

### [Access the SafeSquid User Interface](/docs/SafeSquid_SWG/Configuration_Portal/) on the slave server



## Go to Support
![clicking on support in safesquid interface in top right corner ](/img/How_To/Master_Slave_configuration/image1.webp)



## Go to Startup params
![clicking on start up params](/img/How_To/Master_Slave_configuration/image2.webp)

![clicking on edit button](/img/How_To/Master_Slave_configuration/image3.webp)

![entering the master IP address](/img/How_To/Master_Slave_configuration/image4.webp)

![entering the port of master server](/img/How_To/Master_Slave_configuration/image5.webp)

![clicking on submit button](/img/How_To/Master_Slave_configuration/image6.webp)

![clicking on restart button](/img/How_To/Master_Slave_configuration/image7.webp)

![clicking on yes for backup current configuration to cloud](/img/How_To/Master_Slave_configuration/image8.webp)



## Step 2: Configure master server (if authentication is enabled)

If your master requires authentication, add the slave IP to the Allow list so the slave can access the Configuration Portal and sync policies.

### Go to Access Restriction under Application Setup

![Going to Access Restriction under Application Setup](/img/How_To/Master_Slave_configuration/image9.webp)



## Go to Allow list
![going to allow list tab in access restrictions](/img/How_To/Master_Slave_configuration/image10.webp)

![enabling the policy as true](/img/How_To/Master_Slave_configuration/image11.webp)

![enabling the policy as true for giving access to slave server](/img/How_To/Master_Slave_configuration/image12.webp)

![clicking on save to save the policy](/img/How_To/Master_Slave_configuration/image13.webp)

![policy saved](/img/How_To/Master_Slave_configuration/image14.webp)



## Step 3: Verify synchronization

### Check slave configuration sync

![Verifying the synchronization of defined sections on Slave server](/img/How_To/Master_Slave_configuration/image15.webp)

On the slave Configuration Portal, confirm that sections synced from the master appear with the same settings. Make a test policy change on the master and verify it appears on the slave within a few minutes.

### Verify reporting flow

On the master, open [Reporting Service](/docs/SafeSquid_SWG/Reporting_Service/) and confirm logs from slave nodes appear in unified reports. Slave traffic should be visible on the master.

## Verification checklist

- [ ] Slave Configuration Portal → Support → Startup params shows correct master IP and port
- [ ] Master Configuration Portal → Access Restriction → Allow list includes slave IP (if authentication enabled)
- [ ] Test policy change on master propagates to slave within 5 minutes
- [ ] Slave traffic appears in master Reporting Service
- [ ] Slave logs show successful sync events (check `/var/log/safesquid/extended.log`)

## Troubleshooting

**Slave not syncing policies:**
- Verify network connectivity from slave to master port 8888: `telnet <master-ip> 8888`
- Check master firewall allows incoming connections on port 8888
- If authentication enabled, verify slave IP in master Access Restriction → Allow list
- Check slave logs: `tail -f /var/log/safesquid/extended.log` (look for sync errors)

**Slave traffic not appearing in master reports:**
- Verify reporting data path is not blocked by firewall
- Check slave Configuration Portal → Support → Startup params has correct master IP
- Restart slave: Configuration Portal → Support → Restart SafeSquid

**Policies syncing but not applying:**
- After policy changes on master, restart slave to apply: Configuration Portal → Support → Restart SafeSquid
- Verify slave activation key matches master (same license)

**Related**: [Configuration Sync](/docs/Proxy_Clustering/Configuration_Sync/), [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), [Reporting Service](/docs/SafeSquid_SWG/Reporting_Service/), [Troubleshooting](/docs/Troubleshooting/main/)

