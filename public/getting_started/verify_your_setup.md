---
title: Verify Your Setup
description: Verify SafeSquid installation, activation, proxy connectivity, policy enforcement, and log evidence before production rollout.
keywords:
  - verify your setup
  - SafeSquid
  - get_started
---

# Verify Your Setup

SafeSquid is not production-ready until service state, proxy routing, license status, DNS resolution, and log evidence all agree. Use this checklist before enabling broad user traffic or claiming audit readiness.

## Validate prerequisites

Before running these tests, confirm:

- SafeSquid is installed and activated. Use [Activate Your License](/getting_started/activate) if the license is not active.
- At least one pilot client uses SafeSquid as its proxy. Use [Connect Your Client](/getting_started/client_configuration/connect_your_client) for the routing path.
- You have shell access to the SafeSquid server.
- The test window is approved in the change record.
- Rollback exists for proxy settings, firewall rules, and client routing.

## Run the verification path

<Steps>
  <Step title="Prove service and listener state">
    Confirm the proxy listener, process ID, and service state from the SafeSquid server.

    Confirm the listener, process, and service checks all show SafeSquid is running.

    If any check fails, inspect service logs before routing more users.
  </Step>
  <Step title="Open the interface safely">
    Load `http://safesquid.cfg/` through the proxy path, or use direct management access only from an approved administrator network.

    Confirm the Configuration Portal loads from an approved management path.

    If the portal does not load, verify browser proxy settings, listener state, and network ACLs.
  </Step>
  <Step title="Confirm activation">
    Check product type, subscription state, and expiry in the SafeSquid interface.

    Confirm product, subscription, and expiry details are populated.

    If activation details are missing, re-upload the activation key and test subscription reachability.
  </Step>
  <Step title="Prove HTTP and HTTPS proxy flow">
    Run explicit `curl --proxy` tests and confirm corresponding access-log records.

    Confirm HTTP and HTTPS tests produce matching access-log entries.

    If HTTPS fails with trust warnings, finish Root CA deployment before production inspection.
  </Step>
  <Step title="Prove DNS resolution">
    Test DNS resolution from the SafeSquid server and repair BIND9 before production rollout if resolution fails.

    Confirm DNS returns expected answers from the SafeSquid server path.

    If resolution fails, repair DNS forwarding, gateway, or BIND9 state before rollout.
  </Step>
  <Step title="Capture evidence">
    Save service, listener, license, DNS, access-log, and pilot-client records with the change.

    Confirm the deployment record contains all required readiness artifacts.

    If evidence is incomplete, rerun the failed check and attach the corrected output.
  </Step>
</Steps>

## Prove the service runs

Run the listener check on the SafeSquid server:

```bash
ss -lntp | grep ':8080'
```

Expected result: SafeSquid listens on the approved proxy port.

Confirm the process is active:

```bash
pidof safesquid
```

Expected result: one or more process IDs.

On systemd systems, confirm service state:

```bash
systemctl status safesquid --no-pager
```

Expected result: `Active: active (running)` and no recent startup errors.

## Open the interface safely

From a browser configured to proxy through SafeSquid, open:

```text
http://safesquid.cfg/
```

Expected result: the Configuration Portal loads through the SafeSquid proxy path.

If the pilot browser is not proxied yet, use direct management access only from an approved administrator network:

```text
https://SAFESQUID-SERVER-IP:8443/
```

Document which management path was used. Direct access changes the trust boundary and must not become the default user path.

## Confirm activation state

In the SafeSquid interface, open the **Support** menu and check the activation or subscription details shown for the instance.

Expected result:

- **Product Type** shows the licensed tier.
- **Status** or subscription state is active.
- **Expiry** is valid for the intended deployment window.

If the status is inactive, re-upload the `activation_key` from the approved storage location and confirm outbound HTTPS access to `api.safesquid.net`.

## Prove HTTP proxy flow

From the pilot client, request an HTTP site through SafeSquid:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

Expected result: the request returns an HTTP response such as `200`, `301`, or `302`.

On the SafeSquid server, inspect the access log:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the log records the pilot client IP address, destination host, timestamp, and action.

If no entry appears, the client is bypassing SafeSquid or the wrong proxy address is configured.

## Prove HTTPS proxy flow

From the pilot client, request an HTTPS site:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 https://www.google.com
```

Expected result: the connection succeeds or fails with a known certificate-trust condition that matches the current SSL inspection stage.

If SSL inspection is not configured, do not normalize browser certificate-warning bypasses for production users. Limit any warning bypass to an isolated pilot test, record it in the change evidence, and complete Root CA deployment before production HTTPS inspection.

<Warning>
  **TLS warning risk:** A browser certificate warning is not a successful production HTTPS inspection test. It is evidence that endpoint trust, SSL policy, or the test path still needs review.
</Warning>

Check the access log:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the log records the HTTPS destination and policy action.

{/* source: _migration_source_v3/docs/01-Getting_Started/06-Verify_Your_Setup.md §5 HTTPS Traffic Flows Through the Proxy */}

Once SSL inspection is configured and the Root CA is deployed, the positive test is the certificate itself. Load an HTTPS site in the pilot browser and inspect the certificate issuer.

Expected result: the issuer is the SafeSquid CA, and no warning appears. An issuer showing the original site's certificate authority means the connection is being tunnelled rather than inspected, even though the page loads normally.

## Prove DNS resolution

Test DNS resolution from the SafeSquid server:

```bash
nslookup example.com 127.0.0.1
```

Expected result: DNS returns a valid IP address for `example.com`.

If DNS fails:

- Check BIND9 service state with `systemctl status bind9 --no-pager`.
- Check `/etc/bind/named.conf` for syntax or forwarder errors.
- Use [BIND](/safesquid_swg/interface/bind) to repair local DNS service configuration.

## Capture readiness evidence

Store these artifacts with the deployment record:

- SafeSquid service status output.
- Proxy listener output for the approved port.
- Screenshot or record showing active license state.
- HTTP and HTTPS access-log entries from `/var/log/safesquid/access/extended.log`.
- DNS test output.
- Pilot client proxy configuration.
- Change record with rollback owner.

This evidence supports SOC 2 change management, ISO 27001 operational control review, and NIST SP 800-53 audit traceability for first deployment.

## Troubleshoot failed checks

| Symptom | Likely cause | Fix | Verify |
|---|---|---|---|
| Port `8080` is not listening | SafeSquid service is stopped or failed | Start SafeSquid and review service logs | `ss -lntp | grep ':8080'` returns a listener |
| `safesquid.cfg` does not load | Pilot browser is not using SafeSquid | Configure explicit proxy and retry | Configuration Portal loads through proxy |
| License is inactive | Key was not uploaded or subscription path is blocked | Re-upload `activation_key`; allow HTTPS to `api.safesquid.net` | Activation details show active state |
| HTTP request succeeds but no log appears | Client bypasses proxy or wrong log path checked | Confirm proxy settings and inspect `/var/log/safesquid/access/extended.log` | New request appears in access log |
| DNS resolution fails | BIND9 is stopped or forwarder is unreachable | Restart BIND9 and fix resolver settings | `nslookup example.com 127.0.0.1` succeeds |
| HTTPS sites fail unexpectedly | SSL inspection trust, firewall, or service failure | Check Root CA rollout, firewall policy, and SafeSquid service state | HTTPS request and access-log entry match policy |

Escalate to the operations owner if service restart, DNS repair, or activation upload changes production traffic behavior.

## Validate production controls

Before routing broad user traffic, confirm these controls are planned or already complete:

- SSL inspection is configured and the SafeSquid Root CA is deployed to managed endpoints.
- Authentication integrates with the approved identity source.
- Baseline access policies block malware, high-risk categories, and unauthorized applications.
- Reporting or log export captures access evidence for incident response.
- High availability is planned with [Proxy Clustering](/use_cases/scaling_and_high_availability/proxy_clustering) when uptime requirements demand it.
- Support and rollback owners are documented.

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
- [ ] **Support → Activation Details** shows an active state.

**Remote management, where used**

- [ ] An SSH client is available on the administrator workstation.
- [ ] Public keys are installed on the SafeSquid host if key-based authentication is required.
- [ ] `ssh <admin-user>@<PROXY-IP>` succeeds from the approved management network.

</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/06-Verify_Your_Setup.md §SafeSquid Integration Validation */}

<Accordion title="Integration validation before production">

Use this once controls are configured, to confirm each one is actually enforcing rather than merely enabled.

**Authentication and identity**

- [ ] Users authenticate with domain credentials through the configured AD or LDAP integration.
- [ ] Usernames, not just IP addresses, appear in `/var/log/safesquid/access/extended.log`.
- [ ] Where group policies are configured, different groups receive demonstrably different policy.

**Policy enforcement**

- [ ] A blocked category is genuinely blocked from a client.
- [ ] Sites are categorized as expected.
- [ ] Time-based policies activate and deactivate on schedule, where configured.
- [ ] HTTPS sites present the SafeSquid certificate once the CA is deployed.

**Security and content filtering**

- [ ] An EICAR test file download is blocked, confirming antivirus scanning is live.
- [ ] Keyword-based content blocking triggers, where enabled.
- [ ] Restricted file types are blocked on upload and download.

**Operations and monitoring**

- [ ] `/var/log/safesquid/` contains current access logs.
- [ ] The host reaches its update servers.
- [ ] An update schedule is defined, whether automatic or manual.
- [ ] Log forwarding to the monitoring or SIEM platform works, where configured.
- [ ] Reports load in the Configuration Portal.

**Testing and documentation**

- [ ] Multiple client devices browse successfully through SafeSquid.
- [ ] A documented test case exists for each policy rule.
- [ ] Configuration is backed up, including `/usr/local/safesquid/config/`.
- [ ] A failover and restore procedure is written down and has been tested.

<Note>
  Use the EICAR test file rather than live malware. It is an industry-standard, inert string designed for exactly this check and is safe to transmit on a production network.
</Note>

</Accordion>

## Verification is complete

The setup is ready for policy rollout when service state, interface access, activation status, HTTP routing, HTTPS routing, DNS resolution, and access logs all pass.

## Next steps

- Use [Configure Web Security Policies](/getting_started/configure_web_security_policies) to enforce initial controls.
- Use [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) to enable HTTPS decryption after CA rollout.
- Use [Access Restriction](/use_cases/access_restriction/access_restriction) to enforce category and time-based policies.
