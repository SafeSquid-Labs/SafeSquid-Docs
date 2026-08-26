---
title: Verify Failover
description: Test SafeSquid high-availability failover deliberately, confirm the VIP moves, and keep the evidence that proves the control survived a node loss.
keywords:
  - SafeSquid failover test
  - Keepalived VRRP failover
  - VIP handover verification
  - HA evidence
  - failover testing cadence
---

# Untested Failover Is Not High Availability

A configured cluster proves nothing until a node has actually been taken away from it. Split-brain, a truncated `auth_pass`, a health check that never drops priority — every one of these looks correct in the configuration file and fails only under the condition the cluster exists for.

Test it deliberately, on a schedule, and keep the output.

## Validate prerequisites

Confirm:

- An active-passive pair is configured. See [Monit and Keepalived](/use_cases/scaling_and_high_availability/ha_monit_keepalived).
- Both nodes are healthy and the VIP is currently held by the Master.
- The test window is approved, and clients affected by a brief handover are known.
- You have shell access to both nodes.

## Confirm the starting state

On the Master, confirm Keepalived owns the VIP and the health check passes:

```bash
sudo systemctl status keepalived
sudo journalctl -u keepalived -n 30 --no-pager
```

Expected output on the Master includes:

```
(SAFESQUID_VIP) Entering MASTER STATE
VRRP_Script(check_safesquid) succeeded
```

Confirm the address is Keepalived-owned, not statically assigned:

```bash
ip a show INTERFACE | grep VIP-ADDRESS
```

Expected output on the Master only:

```
inet VIP-ADDRESS/32 scope global proto keepalived INTERFACE
```

The `proto keepalived` tag confirms Keepalived owns the address and will withdraw it automatically on failover. An address without that tag was assigned statically and will not move.

## Trigger the failover

Open two terminals. Watch the log on the Backup while you stop SafeSquid on the Master.

```bash
# Backup node: follow the Keepalived log
sudo journalctl -u keepalived -f
```

```bash
# Master node: trigger the failure
sudo systemctl stop safesquid
```

Within 10–15 seconds the log shows the handover:

```
(SAFESQUID_VIP) Changing effective priority from 101 to 0
(SAFESQUID_VIP) Master received advert from BACKUP-IP with higher priority 100
(SAFESQUID_VIP) Entering BACKUP STATE
(SAFESQUID_VIP) Transition to MASTER STATE
Sending gratuitous ARP on INTERFACE for VIP-ADDRESS
```

Confirm the VIP moved:

```bash
ip a show INTERFACE | grep VIP-ADDRESS
```

Expected result: the address now appears on the Backup and is gone from the Master.

Prove it from a client, not only from the nodes. Browse through the VIP and confirm the request appears in the surviving node's access log — a VIP that moved but carries no traffic is a half-successful failover.

## Restore the Master

```bash
sudo systemctl start safesquid
```

<Note>
`nopreempt` keeps the VIP on the Backup after the Master recovers. This avoids a second interruption during business hours. To move the VIP back deliberately, restart Keepalived on the Master: `sudo systemctl restart keepalived`.
</Note>

## Capture failover evidence

Store these artifacts with the change record:

- `journalctl -u keepalived` extract covering the tested failover, showing the state transition and gratuitous ARP.
- `ip a` output before and after failover, showing VIP ownership on each node.
- `/var/log/keepalived_check.log` and `/var/log/monit.log` for the test window.
- Client-side proof that browsing resumed through the VIP, plus the access-log entries from the surviving node.
- The date of the last tested failover and the named owner of the next test.

<Warning>
Schedule a failover test on the same cadence as your disaster-recovery restore test. A cluster that has not failed over in a year is a configuration file, not a control.
</Warning>

## Troubleshoot failover tests

| Symptom | Likely cause | Fix |
|---|---|---|
| Both nodes report MASTER | `virtual_router_id` or `auth_pass` mismatch | Set an identical `virtual_router_id` and `auth_pass` on both nodes; `auth_pass` must be 8 characters or fewer |
| VIP does not move on failure | `weight` does not drop priority below the Backup | Use `weight -101` so the effective priority reaches 0 |
| VIP moves but clients still fail | Clients point at a node address, not the VIP | Repoint PAC, GPO, or MDM at the VIP; a profile naming the Master will not fail over |
| VIP present but tagged differently | Address was assigned statically | Remove the static assignment; only a `proto keepalived` address will move |
| Handover works, logs are empty on the survivor | Traffic is not reaching the surviving node | Confirm firewall rules permit the client network to both nodes, not just the Master |

## Next steps

- [Monit and Keepalived](/use_cases/scaling_and_high_availability/ha_monit_keepalived) - review or correct the cluster configuration.
- [Backup Strategy](/use_cases/scaling_and_high_availability/disaster_recovery) - pair failover testing with a restore test.
- [Configuration Sync](/use_cases/customisation/configuration_sync) - keep policy identical on both nodes.
