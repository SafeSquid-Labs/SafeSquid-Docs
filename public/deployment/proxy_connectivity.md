---
title: Proxy Connectivity
description: Prove a client reaches the SafeSquid listener and that its requests appear in the access log, using client-side checks the server cannot perform on itself.
keywords:
  - SafeSquid proxy test
  - curl proxy verification
  - extended.log access log
  - client proxy connectivity
  - deployment validation
---

# Prove Traffic Reaches the Proxy

A healthy proxy that clients cannot reach passes every check run on the server. The failure only appears from the client side — and by then users are already escalating, and the fastest workaround an impatient administrator reaches for is removing the proxy setting entirely.

Run this check from a pilot client, not from the SafeSquid host.

## Validate prerequisites

Confirm:

- [Service Health](/deployment/service_health) passes on the SafeSquid node.
- At least one pilot client is configured to use SafeSquid as its proxy. Use [Connect Your Client](/getting_started/client_configuration/connect_your_client) for the routing path.
- You have shell access to the SafeSquid server to read the access log.
- The test window is approved in the change record.

## Request an HTTP site through the proxy

From the pilot client:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

Expected result: the request returns an HTTP response such as `200`, `301`, or `302`.

## Confirm the request was logged

The client response alone does not prove the request went through SafeSquid — a bypassed client reaches the site just as successfully. The access log is the proof.

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the log records the pilot client IP address, destination host, timestamp, and action.

If the request succeeded but no entry appears, the client is bypassing SafeSquid or the wrong proxy address is configured. Treat that as a failed test, not a logging problem.

{/* source: _migration_source_v3/docs/01-Getting_Started/06-Verify_Your_Setup.md §Post-Installation Client Checklist */}

<Accordion title="Client-side checklist">

Run this from a client workstation, not from the SafeSquid host. It catches the failures that server-side checks cannot see — a healthy proxy that clients cannot reach still passes every check on the server.

**Network connectivity**

- [ ] `ping <PROXY-IP>` succeeds from the client.
- [ ] The proxy port accepts connections. On Windows, PuTTY in raw mode serves the same purpose as `telnet`:

  ```bash
  telnet <PROXY-IP> 8080
  ```

**Client configuration**

- [ ] Browser proxy points at `<PROXY-IP>:8080`.
- [ ] OS-level proxy is configured, where all applications must be covered.

**Licence and interface access**

- [ ] `http://safesquid.cfg/` loads when the proxy is configured.
- [ ] The activation key has been uploaded through the interface.
- [ ] **Support → License Details** shows an active state.

**Remote management, where used**

- [ ] An SSH client is available on the administrator workstation.
- [ ] Public keys are installed on the SafeSquid host if key-based authentication is required.
- [ ] `ssh <admin-user>@<PROXY-IP>` succeeds from the approved management network.

</Accordion>

## Capture connectivity evidence

Store these artifacts with the deployment record:

- The `curl` command and its response headers.
- The matching access-log line from `/var/log/safesquid/access/extended.log`, showing source, destination, timestamp, and action.
- The pilot client's proxy configuration.
- The completed client-side checklist, with the tester named.

## Troubleshoot client routing

| Symptom | Likely cause | Fix |
|---|---|---|
| `curl` fails to connect | Firewall blocks the client network, or the listener is bound elsewhere | Confirm the inbound rule for the client CIDR, then re-run [Service Health](/deployment/service_health) |
| Request succeeds but no log entry | Client bypasses the proxy, or the wrong log path was checked | Confirm proxy settings on the client and inspect `/var/log/safesquid/access/extended.log` |
| Only some clients are logged | Bypass rule or PAC exception is matching more broadly than intended | Review PAC logic and bypass lists; narrow to named destinations |
| `safesquid.cfg` does not load | Pilot browser is not using SafeSquid | Configure explicit proxy and retry before investigating the portal |
| Connections work then drop under load | NIC saturation, or bonding configured on the host but not the switch | Compare against the sizing plan in [Hardware Sizing](/deployment/hardware_sizing) |

## Next steps

- [HTTPS Inspection Validation](/deployment/https_inspection_validation) - prove encrypted traffic is inspected, not tunnelled.
- [Logging and Reporting](/deployment/logging_and_reporting) - confirm evidence is retained and reportable.
- [Explicit Browser Proxy](/getting_started/client_configuration/explicit_proxy) - re-check the client routing method.
