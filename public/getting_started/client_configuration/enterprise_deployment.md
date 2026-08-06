---
title: "Enterprise Deployment"
description: "Roll out SafeSquid proxy settings through central endpoint management with staged validation, rollback, and audit evidence."
keywords: ["SafeSquid enterprise deployment", "proxy GPO", "proxy MDM", "managed endpoint proxy", "SafeSquid rollout"]
---

# Roll Out Proxy Settings Safely

Enterprise proxy deployment turns a working pilot into enforceable web security. The risk is blast radius: a bad GPO, MDM profile, PAC URL, or configuration-management task can break web access across an entire business unit. Deploy in stages, prove traffic evidence, and keep rollback ready before expanding scope.

## Use this method when

Use enterprise deployment when:

- Explicit proxy or PAC pilot has passed.
- Endpoint management can enforce settings.
- The organization needs consistent routing and bypass control.
- Rollback can be applied quickly to the same scope.

Do not deploy to all users before testing a small representative pilot group.

## Validate prerequisites

Confirm:

- Proxy method and settings are approved.
- PAC URL or proxy IP/port is stable.
- Internal bypass list is reviewed.
- Pilot group, expansion rings, and rollback owner are named.
- Helpdesk and operations teams know expected symptoms and rollback steps.

## Choose the rollout method

<Steps>
  <Step title="Choose Windows GPO">
    <Card title="Windows GPO" href="#deploy-with-gpo">
      Use for domain-joined Windows endpoints. Evidence is linked GPO scope, resultant settings, and pilot access logs.
    </Card>

    Confirm GPO scope and resultant settings match the pilot ring.

    If settings do not apply, inspect OU link, security filtering, and replication.
  </Step>
  <Step title="Choose MDM profiles">
    <Card title="MDM Profiles" href="#deploy-with-mdm">
      Use for macOS, Windows, and mobile fleets. Evidence is profile assignment, compliance state, and test traffic.
    </Card>

    Confirm profile assignment and compliance state match the approved device group.

    If devices miss the profile, verify enrollment, assignment filters, and sync state.
  </Step>
  <Step title="Choose configuration management">
    <Card title="Configuration Management" href="#deploy-with-configuration-management">
      Use for Linux and mixed fleets. Evidence is job output, managed file state, and SafeSquid log entries.
    </Card>

    Confirm job output shows the managed proxy file or setting was applied.

    If drift remains, rerun the job and inspect local configuration precedence.
  </Step>
  <Step title="Choose browser policy">
    <Card title="Browser Policy">
      Use when only managed browsers need PAC or proxy enforcement. Evidence is policy result pages and controlled tests.
    </Card>

    Confirm browser policy pages show the approved proxy or PAC setting.

    If browser policy is ignored, check local overrides and policy precedence.
  </Step>
</Steps>

## Stage the deployment

1. Deploy to IT pilot users.
2. Validate access logs, internal bypasses, and business apps.
3. Expand to one department or site.
4. Monitor helpdesk issues and SafeSquid logs.
5. Expand by rings only after evidence is clean.
6. Keep rollback active until the rollout is stable.

## Deploy with GPO

Use Group Policy to set proxy or PAC settings for a scoped pilot group.

<Steps>
  <Step title="Create the GPO">
    Create a dedicated GPO for the pilot scope. Name it with the proxy method, site or group, and change record ID.

    Confirm the GPO name and scope match the approved pilot ring.

    If ownership is unclear, pause rollout until the change owner approves the scope.
  </Step>
  <Step title="Configure proxy settings">
    Configure the explicit proxy address or PAC URL. Keep internal bypasses reviewed and exact.

    Confirm the proxy address, PAC URL, and bypass list match the deployment record.

    If users receive wrong settings, check policy precedence and inherited browser settings.
  </Step>
  <Step title="Link and apply">
    Link the GPO only to the pilot organizational unit or security-filtered group.

    Confirm only pilot endpoints receive the setting.

    If scope is too broad, unlink the GPO or tighten security filtering before retrying.
  </Step>
  <Step title="Verify on a pilot endpoint">
    Run the checks below and confirm the pilot user appears in SafeSquid logs.

    ```powershell
    gpresult /r
    netsh winhttp show proxy
    ```

    Confirm the intended GPO applies and the proxy settings match approved values.

    If the endpoint does not apply the GPO, refresh policy and inspect OU link, security filtering, and replication.
  </Step>
</Steps>

## Deploy with MDM

Use MDM to deliver proxy or PAC profiles. Apply to a scoped pilot device group before broad assignment.

<Tabs>
  <Tab title="Microsoft Intune">
    Create or update a device configuration profile that sets the approved proxy or PAC URL. Assign it to a pilot group, then verify device compliance and browser traffic.
  </Tab>
  <Tab title="Jamf Pro">
    Deliver a configuration profile for the approved network service or browser policy. Scope it to pilot Macs before production devices.
  </Tab>
</Tabs>

Verify on a managed macOS endpoint:

```bash
profiles status -type enrollment
```

Expected result: the device is managed and the assigned profile is present.

## Deploy with configuration management

Use configuration management for Linux or mixed fleets. Keep settings explicit:

<Tabs>
  <Tab title="Ansible">
    ```yaml
    proxy:
      http: "http://SAFESQUID-IP:8080"
      https: "http://SAFESQUID-IP:8080"
      bypass:
        - "localhost"
        - ".internal.example.com"
    ```

    Capture the playbook run ID and managed host list.
  </Tab>
  <Tab title="Puppet">
    ```puppet
    file { '/etc/profile.d/proxy.sh':
      ensure  => file,
      content => "export http_proxy=http://SAFESQUID-IP:8080\nexport https_proxy=http://SAFESQUID-IP:8080\n",
    }
    ```

    Capture the catalog report and changed resources.
  </Tab>
</Tabs>

For any tool, verify with a managed job output or local state check:

```bash
env | grep -i proxy
```

Expected result: the endpoint receives the intended proxy values and generates SafeSquid access-log entries.

{/* Keep this generic schema as a compact reference for teams that use a different configuration-management platform. */}

```yaml
proxy:
  http: "http://SAFESQUID-IP:8080"
  https: "http://SAFESQUID-IP:8080"
  bypass:
    - "localhost"
    - ".internal.example.com"
```

## Verify rollout evidence

On SafeSquid:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: pilot users generate logs from intended source networks, and internal bypasses behave as designed.

## Roll back safely

Rollback must remove the same setting mechanism used for rollout:

- Disable or unlink the GPO.
- Remove the MDM profile.
- Revert the configuration-management state.
- Restore the previous PAC file version.
- Confirm clients stop receiving the failed setting.

## Monitor the rollout

Track SafeSquid access logs, helpdesk tickets, endpoint policy compliance, and business-app failures during every rollout ring. Pause expansion when logs show direct bypass, repeated authentication failures, or policy matches that block required business workflows.

<Tip>
  Keep the PAC file URL stable and version the file contents. This lets endpoint policies stay unchanged while rollback restores a known-good PAC body.
</Tip>

## Troubleshoot rollout failures

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Users lose all web access | Proxy host, port, or PAC URL is wrong | Roll back the policy scope and fix the setting |
| Some users bypass SafeSquid | Scope or policy inheritance is incomplete | Check endpoint policy result and group assignment |
| Business app breaks | Missing PAC bypass or proxy incompatibility | Add a reviewed bypass or application-specific exception |
| Logs lack user context | Authentication is not configured or not matching | Verify authentication before expanding rollout |

## Next steps

- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - handle tools that ignore managed proxy settings.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - enforce controls after routing is stable.
- [Reporting Service](/safesquid_swg/interface/reporting_service) - preserve rollout and access evidence.