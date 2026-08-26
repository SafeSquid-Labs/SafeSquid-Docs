---
title: Service Health
description: Prove the SafeSquid process, proxy listener, and local DNS resolver are running and healthy before routing user traffic through the node.
keywords:
  - SafeSquid service status
  - proxy listener check
  - safesquid systemctl
  - BIND9 resolver health
  - deployment validation
---

# Prove the Node Is Actually Serving

A node that answers `systemctl status` is not necessarily serving traffic. The process can be running while the listener never bound, or the listener can be up while local DNS resolution is dead — and in both cases users see failures that look like network problems, so the proxy is the last thing anyone checks.

Run these checks first. Everything else in validation assumes the service is genuinely up.

## Validate prerequisites

Confirm:

- SafeSquid is installed on the host under test.
- You have shell access to the SafeSquid server.
- The approved proxy listener port is known and recorded in the change record.

## Prove the listener bound

Run the listener check on the SafeSquid server:

```bash
ss -lntp | grep ':8080'
```

Expected result: SafeSquid listens on the approved proxy port.

An empty result with a healthy service means the process started but failed to bind — usually a port already in use, or a listener address that does not exist on this host. Check the service log before changing configuration.

## Prove the process is alive

```bash
pidof safesquid
```

Expected result: one or more process IDs.

On systemd systems, confirm service state:

```bash
systemctl status safesquid --no-pager
```

Expected result: `Active: active (running)` and no recent startup errors.

Read the startup lines even when the state is `active`. A service that restarted minutes ago is reporting health for a process that has not yet been under load.

## Prove local DNS resolution

SafeSquid cannot categorise or reach a destination it cannot resolve. Where [integrated DNS security](/use_cases/dns_security/dns_security) is deployed, BIND9 is part of the service, not a separate concern.

```bash
nslookup example.com 127.0.0.1
```

Expected result: DNS returns a valid IP address for `example.com`.

If resolution fails:

- Check BIND9 service state with `systemctl status bind9 --no-pager`.
- Check `/etc/bind/named.conf` for syntax or forwarder errors.
- Use [BIND](/safesquid_swg/interface/bind) to repair local DNS service configuration.

## Capture service evidence

Store these artifacts with the deployment record:

- `ss -lntp` output showing the bound proxy listener.
- `systemctl status safesquid` output, including the startup lines.
- `nslookup` output from the SafeSquid host.
- The date of the check and the named owner of the node.

## Troubleshoot service failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Port `8080` is not listening | SafeSquid service is stopped or failed to bind | Start SafeSquid, then read the service log for a bind error before changing the port |
| Service is `active` but no PID | Process exited immediately after start | Inspect `journalctl -u safesquid` for a configuration parse failure |
| Service restarts repeatedly | Configuration error or a supervisor restart loop | Check Monit state and the SafeSquid startup log; fix the underlying error rather than disabling the supervisor |
| DNS resolution fails from the host | BIND9 is stopped or the forwarder is unreachable | Restart BIND9 and correct resolver settings before routing clients |
| Listener is bound to the wrong interface | Listener address does not match the client-facing NIC | Correct the listener address, restart, and re-run the `ss` check |

## Next steps

- [Proxy Connectivity](/deployment/proxy_connectivity) - prove a client can actually reach the listener.
- [Production-Readiness Checklist](/getting_started/verify_your_setup) - work through the full validation sequence.
- [Monit](/safesquid_swg/interface/supporting_services_monit) - keep the service supervised after validation passes.
