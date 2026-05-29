---
title: Client Configuration
description: Client onboarding path for routing pilot, managed, and application traffic through SafeSquid SWG.
keywords:
  - client configuration
  - SafeSquid documentation
  - explicit proxy
  - PAC file
  - enterprise proxy deployment
---

# Route Clients Without Losing Control

SafeSquid enforces policy only for traffic that traverses the proxy. Client onboarding must prove traffic flow, preserve user attribution, and avoid bypass paths before production users depend on the gateway.

## Choose the routing method

<Steps>
  <Step title="Choose explicit proxy">
    <Card title="Explicit Proxy" icon="monitor-cog" href="/getting_started/client_configuration/explicit_proxy">
      Best for one pilot browser or troubleshooting session. Manual settings prove the path but are easy to bypass.
    </Card>

    Confirm one pilot request appears in the SafeSquid access log.

    If the browser bypasses SafeSquid, recheck manual proxy settings.
  </Step>
  <Step title="Choose PAC file">
    <Card title="PAC File" icon="file-code" href="/getting_started/client_configuration/pac_file">
      Best for managed browsers that need controlled exceptions. PAC errors can over-route or under-route traffic.
    </Card>

    Confirm PAC output routes internet traffic through SafeSquid and bypasses only approved internal targets.

    If routing is wrong, inspect PAC logic and browser policy precedence.
  </Step>
  <Step title="Choose system-wide proxy">
    <Card title="System-Wide Proxy" icon="settings" href="/getting_started/client_configuration/system_wide_proxy">
      Best for a managed host where OS-aware applications must inherit proxy settings. Some applications still ignore OS proxy state.
    </Card>

    Confirm OS-aware applications inherit the approved proxy state.

    If only browsers use the proxy, configure application-specific settings.
  </Step>
  <Step title="Choose enterprise deployment">
    <Card title="Enterprise Deployment" icon="building-2" href="/getting_started/client_configuration/enterprise_deployment">
      Best when GPO, MDM, Jamf, Ansible, Puppet, or another configuration system owns rollout and rollback.
    </Card>

    Confirm rollout scope and rollback are documented for the pilot ring.

    If many users lose access, roll back the management policy for that ring.
  </Step>
  <Step title="Choose application-specific settings">
    <Card title="Application-Specific Settings" icon="blocks" href="/getting_started/client_configuration/application_specific_configuration">
      Best for developer tools, package managers, container runtimes, and email clients that bypass browser or OS settings.
    </Card>

    Confirm each named application logs expected proxied traffic or has an approved bypass.

    If a tool ignores OS proxy state, configure its native proxy option.
  </Step>
</Steps>

## Rollout sequence

<Steps>
  <Step title="Prove one explicit pilot">
    Configure one browser or test client and verify a new access-log entry under `/var/log/safesquid/access/extended.log`.

    Confirm the access log records the pilot source, destination, timestamp, and action.

    If no log appears, confirm proxy settings and test with `curl --proxy`.
  </Step>
  <Step title="Add managed routing">
    Apply PAC or system-wide settings to a small pilot group. Validate internal bypasses, authentication, and business applications.

    Confirm pilot users receive the managed proxy setting and approved bypasses work.

    If internal apps fail, review PAC output, bypass entries, and endpoint policy precedence.
  </Step>
  <Step title="Scale through management tools">
    Roll out through GPO, Intune, Jamf, Ansible, Puppet, or another approved configuration system with a documented rollback.

    Confirm deployment scope, rollback, and change evidence match the approved rollout ring.

    If users lose access, roll back the management profile or policy for that ring.
  </Step>
  <Step title="Cover bypassing applications">
    Configure application-specific proxy settings for Git, npm, pip, Docker, APT, YUM/DNF, curl, wget, Outlook, Thunderbird, and other tools that bypass OS settings.

    Confirm each named application generates the expected SafeSquid log entry or approved bypass evidence.

    If an application bypasses the proxy, configure its native proxy setting and retest.
  </Step>
  <Step title="Monitor before expanding">
    Review SafeSquid logs, support tickets, authentication failures, and bypass requests before moving to the next rollout group.

    Confirm no repeated bypass, authentication, or business-app failures remain open for the pilot ring.

    If failures persist, pause expansion and assign owners for each exception.
  </Step>
</Steps>

## Evidence to capture

Store:

- Pilot client hostname and user.
- Proxy method selected.
- Proxy host, port, and bypass list.
- Positive access-log sample.
- Negative bypass test for internal destinations.
- Rollback method.
- Owner for exceptions.

## Troubleshoot routing

| Symptom | Likely cause | Fix |
|---|---|---|
| No logs appear | Client bypasses SafeSquid | Confirm proxy setting and test with `curl --proxy` |
| Internal app breaks | Missing bypass | Add a reviewed exact bypass entry |
| Only browsers use proxy | Applications ignore OS settings | Configure application-specific proxy settings |
| Many users lose access | Enterprise rollout scope is too broad | Roll back the GPO, MDM profile, or configuration task |

## Next steps

- [Explicit Proxy Configuration](/getting_started/client_configuration/explicit_proxy) - prove the first client.
- [PAC File Configuration](/getting_started/client_configuration/pac_file) - automate browser routing.
- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - roll out safely.
