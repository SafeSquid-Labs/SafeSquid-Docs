---
title: "Monit"
description: "Install and verify Monit so SafeSquid restarts automatically after local service failure and operators can detect monitoring gaps early."
keywords: ["monit SafeSquid setup", "SafeSquid monit service", "monit auto restart SafeSquid", "SafeSquid monitoring daemon", "SafeSquid service recovery"]
---

# Keep SafeSquid under service watch

## Problem statement

If the SafeSquid service stops and no local watchdog restarts it, web access can fail until an operator notices the outage. In branch sites and lean operations teams, that gap can turn a recoverable process failure into a visible business incident.

## Client scenario

Use Monit when you need the host to:

- detect a stopped SafeSquid service quickly
- restart SafeSquid automatically after local process failure
- confirm the watchdog itself is running after reboot

Monit helps with local process recovery. It does not replace clustering, upstream load balancing, or disaster recovery planning.

## Key benefits

Monit shortens recovery time for simple service failures and gives administrators a clear local health mechanism. It is most useful for single-node deployments, pilot environments, and branch appliances that need basic self-healing.

## Prerequisites

### Client-side preparations

- Ensure you have shell access with administrative privileges on the SafeSquid host.
- Confirm you can restart SafeSquid safely during a maintenance window if this is a production system.

### SafeSquid-side setup

- If you used the SafeSquid Appliance Builder, Monit may already be installed.
- Confirm the SafeSquid init/service commands used on the host are valid before building rules around them.

## Setup instructions

### Confirm whether Monit already exists

Run:

```bash
/etc/init.d/monit status
```

If the service is present and running, review the current configuration before changing anything.

### Install Monit when it is missing

Run:

```bash
apt-get install monit
```

This installs the local monitoring daemon that will watch SafeSquid and restart it when the process stops.

### Update the Monit configuration

Open the Monit configuration directory and edit `monitrc`.

Set a polling interval, enable the local web status page if your operational model allows it, and include the directory used for service-specific policies.

Example baseline:

```conf
set daemon 3

set httpd port 2812 and
    use address localhost
    allow localhost
    allow admin:monit
    allow @monit

include /etc/monit/conf.d/
```

The three-second polling interval determines how quickly Monit notices a stopped process. The include directive matters because service checks are typically stored under `/etc/monit/conf.d/`.

### Restart Monit after changes

Run:

```bash
/etc/init.d/monit restart
```

This reloads the configuration and applies the updated monitoring rules.

### Confirm SafeSquid is under Monit control

Run:

```bash
monit status
```

Verify that SafeSquid appears in the monitored service list. If it does not, Monit is running but not yet supervising the proxy service.

### Start Monit automatically at boot

Run:

```bash
update-rc.d monit enable
```

This reduces the risk of rebooting into an unmonitored state.

## Verification and validation

### Positive test

Stop SafeSquid intentionally:

```bash
/etc/init.d/safesquid stop
```

Then check whether the process returns:

```bash
pidof safesquid
```

Expected result:

- the SafeSquid process disappears briefly
- Monit detects the stop condition
- SafeSquid starts again without manual intervention

### Negative test

Stop Monit and then stop SafeSquid in a controlled test window. SafeSquid should remain down until you restart it manually. This proves the automatic recovery path depends on Monit actually running.

### Evidence to retain

- output of `monit status`
- service status before and after the stop test
- time taken between stop event and service recovery

## Troubleshooting guide

### SafeSquid does not restart after a stop test

Likely causes:

- Monit is not running
- SafeSquid is not defined as a monitored service
- the Monit rule points to the wrong service name or PID file

Isolation steps:

- run `/etc/init.d/monit status`
- run `monit status`
- confirm SafeSquid appears as a monitored object

Remediation:

- start or restart Monit
- correct the SafeSquid service check definition
- rerun the stop test

### Monit runs but reports no SafeSquid service

Likely causes:

- the include path is missing or wrong
- the service policy file was never created

Isolation steps:

- inspect `monitrc`
- verify `include /etc/monit/conf.d/` exists
- verify a SafeSquid-specific rule exists in the included directory

Remediation:

- restore the include line
- add or correct the SafeSquid monitoring rule
- restart Monit and confirm with `monit status`

### Monitoring breaks after reboot

Likely causes:

- Monit is not enabled at startup
- boot sequencing starts SafeSquid before its monitoring rule is available

Isolation steps:

- check whether Monit starts automatically after reboot
- confirm both Monit and SafeSquid show expected service state

Remediation:

- run `update-rc.d monit enable`
- reboot in a maintenance window and validate again

## Related controls / next steps

- Use [Disaster Recovery](/Disaster_Recovery) for recovery planning beyond single-host service restarts.
- Use [Proxy Clustering](/Proxy_Clustering) when you need resilient scale-out instead of local process recovery alone.
- Use [Security Logs](/Security_Logs) to confirm outage timing and recovery evidence during investigations.