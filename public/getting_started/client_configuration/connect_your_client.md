---
title: Connect Your Client
description: Choose the right client routing method and prove that pilot traffic reaches SafeSquid before production rollout.
keywords:
  - SafeSquid client configuration
  - proxy client routing
  - SafeSquid proxy setup
  - managed proxy rollout
---

# Prove Client Traffic Reaches SafeSquid

SafeSquid cannot enforce policy on traffic that bypasses the proxy. Client onboarding must prove that web requests traverse SafeSquid, appear in logs, and can later be tied to user identity. Start with a pilot client, then move to managed rollout.

## Validate prerequisites

Confirm:

- SafeSquid is installed and activated.
- The proxy listener is reachable from the pilot network.
- The pilot client can resolve DNS and reach the proxy IP.
- The operator can inspect `/var/log/safesquid/access/extended.log`.
- Rollback steps exist for the selected client setting.

## Choose the routing method

<Steps>
  <Step title="Choose fastest pilot test">
    <Card title="Fastest pilot test" icon="monitor-cog" href="/getting_started/client_configuration/explicit_proxy">
      Use explicit proxy settings on one browser or host.
    </Card>

    Confirm one browser produces a SafeSquid access-log entry.

    If no log appears, retest with `curl --proxy`.
  </Step>
  <Step title="Choose managed browser routing">
    <Card title="Managed browser routing" icon="file-code" href="/getting_started/client_configuration/pac_file">
      Use a PAC file for controlled browser routing and bypass logic.
    </Card>

    Confirm PAC evaluation sends internet traffic to SafeSquid.

    If internal apps break, correct exact bypass logic.
  </Step>
  <Step title="Choose host-level OS proxy">
    <Card title="Host-level OS proxy" icon="settings" href="/getting_started/client_configuration/system_wide_proxy">
      Use system-wide settings when applications inherit operating-system proxy configuration.
    </Card>

    Confirm OS-aware applications inherit the proxy setting.

    If applications bypass OS settings, use application-specific configuration.
  </Step>
  <Step title="Choose organization-wide rollout">
    <Card title="Organization-wide rollout" icon="building-2" href="/getting_started/client_configuration/enterprise_deployment">
      Use GPO, MDM, Jamf, Ansible, Puppet, or other managed rollout tooling.
    </Card>

    Confirm the rollout tool applies settings only to the pilot ring.

    If scope is too broad, roll back the profile or policy.
  </Step>
  <Step title="Choose application-specific routing">
    <Card title="Applications that ignore OS settings" icon="blocks" href="/getting_started/client_configuration/application_specific_configuration">
      Configure Git, package managers, container runtimes, curl, wget, Outlook, Thunderbird, and other tools directly.
    </Card>

    Confirm each application uses SafeSquid or has an approved exception.

    If a tool still bypasses the proxy, configure its native proxy setting.
  </Step>
</Steps>

## Start with a pilot

<Steps>
  <Step title="Configure one client">
    Configure one browser or host to use SafeSquid as its proxy.

    Confirm the client has the approved SafeSquid IP, port, and bypass entries.

    If the setting does not persist, check endpoint management policy and local browser overrides.
  </Step>
  <Step title="Test external access">
    Browse to `http://example.com` and record whether the request is allowed or blocked as expected.

    Confirm the request produces the expected browser result.

    If browsing fails, confirm proxy reachability and the SafeSquid listener.
  </Step>
  <Step title="Test internal bypass">
    Browse to an internal site that should bypass the proxy, if a bypass is required.

    Confirm the internal destination follows the approved bypass behavior.

    If the internal app fails, add only an approved exact bypass entry.
  </Step>
  <Step title="Record the result">
    Record whether traffic is allowed, blocked, or bypassed as expected, then compare the result with SafeSquid access logs.

    Confirm `/var/log/safesquid/access/extended.log` records proxied traffic with source, destination, timestamp, and action.

    If no log appears, retest with `curl --proxy` and confirm the client is not bypassing SafeSquid.
  </Step>
</Steps>

## Verify traffic evidence

From a client:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
```

On the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the log records the pilot request with source, destination, timestamp, and action.

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/main.md §Testing Your Configuration */}

<Accordion title="Confirm routing from the client, without server access">

The access log is the authoritative check, but it needs shell access to the SafeSquid host. When you are walking a pilot user through the change, or verifying an endpoint you cannot log into, check the egress address from the browser instead.

Visit an address-reflection service such as `whatismyip.com` from the configured client.

Expected result: the address shown is the SafeSquid host's WAN address, not the client's own public address. If the client's own address appears, traffic is bypassing the proxy regardless of what the settings screen says.

Pair this with the internal-bypass test: an internal destination should load and should *not* appear in the SafeSquid log.

</Accordion>

<Accordion title="Rough scale guidance by method">

Method choice tracks fleet size more than anything else:

| Fleet | Method |
|---|---|
| One browser or host, first validation | Explicit proxy |
| A single user across several browsers | PAC file |
| One machine, all applications | System-wide proxy |
| Tens to thousands of endpoints | Enterprise deployment via GPO or MDM |
| Specific tools only, such as a container runtime | Application-specific configuration |

For production, the usual path is explicit proxy to prove the route, then enterprise deployment to enforce it.

</Accordion>

## Prevent bypass

After the pilot passes, restrict direct internet egress where the network design allows it. A browser proxy setting alone is not a control if endpoints can still reach the internet directly.

## Capture onboarding evidence

Store:

- Pilot client and user.
- Proxy method and settings.
- Access-log sample.
- Internal bypass test result.
- Rollback command or management profile.
- Exception owner.

## Troubleshoot client routing

| Symptom | Likely cause | Fix |
|---|---|---|
| Client cannot reach proxy | Firewall, route, or wrong proxy IP | Test network reachability and confirm proxy listener |
| No access log appears | Client bypasses SafeSquid | Recheck proxy setting and retest with `curl --proxy` |
| Internal apps fail | Missing bypass or routing exception | Add an approved exact bypass entry |
| HTTPS warning appears | Root CA trust is missing | Complete Root CA deployment before testing HTTPS inspection |

## Next steps

- [Explicit Proxy Configuration](/getting_started/client_configuration/explicit_proxy) - configure the first browser.
- [PAC File Configuration](/getting_started/client_configuration/pac_file) - move to controlled browser routing.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - scale to managed endpoints.
