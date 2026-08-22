---
title: "Enterprise Deployment"
description: Roll out SafeSquid proxy settings through central endpoint management with staged validation, rollback, and audit evidence.
keywords:
  - SafeSquid enterprise deployment
  - proxy GPO
  - proxy MDM
  - managed endpoint proxy
  - SafeSquid rollout
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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/04-Enterprise_Deployment.md §Which Method Should I Use? */}

<Accordion title="Match the tool to the estate">

| Estate | Tool | Why |
|---|---|---|
| All Windows, domain-joined | Group Policy | Built into Active Directory; nothing extra to deploy |
| Mixed Windows and macOS, Entra ID | Microsoft Intune | One console for both platforms |
| macOS only | Jamf Pro or Intune | MDM designed for Apple devices |
| Linux servers and workstations | Ansible or Puppet | Standard configuration management |
| Mixed Windows and Linux, no directory | Ansible | Agentless, works over SSH |
| Existing SCCM deployment | SCCM | Reuse the infrastructure already in place |

</Accordion>

## Stage the deployment

1. Deploy to IT pilot users.
2. Validate access logs, internal bypasses, and business apps.
3. Expand to one department or site.
4. Monitor helpdesk issues and SafeSquid logs.
5. Expand by rings only after evidence is clean.
6. Keep rollback active until the rollout is stable.

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/04-Enterprise_Deployment.md §Best Practices */}

<Accordion title="Ring sizes and dwell time">

Rings only surface problems if each one runs long enough for users to hit their real workload — a ring that advances in a day catches outages but not the weekly finance app.

| Ring | Size | Dwell |
|---|---|---|
| Pilot | 5–10 users, IT and volunteers | 1 week |
| Early adopters | 50–100 users | 1 week |
| Department by department | One business unit at a time | 2–4 weeks total |
| Full deployment | Remainder | — |

Review SafeSquid logs and helpdesk tickets at each boundary before advancing.

**PAC hosting.** Host on redundant web servers rather than one host, address it through internal DNS so the endpoint policy never has to change, keep the file body in version control, and stage changes before production.

**Monitoring.** Use Group Policy Modeling in the Group Policy Management Console to predict which machines a change will affect before you link it. Run configuration-compliance reports on a schedule, alert on proxy configuration drift, and confirm through SafeSquid logs that managed endpoints are actually routing.

</Accordion>

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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/04-Enterprise_Deployment.md §Windows: Group Policy (GPO) */}

<Accordion title="GPO console paths and values">

**Create the object** — open the Group Policy Management Console (`gpmc.msc`), right-click the target domain or OU, select **Create a GPO in this domain, and Link it here**, name it for the proxy method and change record, then right-click it and select **Edit**.

**Option A — deliver a PAC URL (preferred)**

Navigate to:

```
Computer Configuration → Policies → Administrative Templates →
Windows Components → Internet Explorer
```

1. Open **Use automatic configuration script**, enable it, and enter the PAC URL.
2. Open **Disable changing proxy settings** and enable it, so users cannot remove the configuration.

**Option B — set an explicit proxy**

Navigate to **Computer Configuration → Preferences → Windows Settings → Registry**, then create three registry items under `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings`:

| Value | Type | Data |
|---|---|---|
| `ProxyEnable` | `REG_DWORD` | `1` |
| `ProxyServer` | `REG_SZ` | `SAFESQUID-IP:8080` |
| `ProxyOverride` | `REG_SZ` | `*.local;*.internal.example.com;localhost;127.0.0.1` |

Set the action to **Update**, not **Create**. Create fails on reapply once the value exists, which produces confusing intermittent results across the fleet.

**Apply and verify**

Group Policy refreshes on its own within roughly 15 to 90 minutes. To test immediately on one endpoint:

```powershell
gpupdate /force
gpresult /r
gpresult /h C:\gp-report.html
```

```powershell
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
```

Expected result: the SafeSquid GPO appears in the applied list, and `ProxyEnable` and `ProxyServer` hold the approved values.

**Roll back**

Delete the **link**, not the GPO itself. Removing the link stops enforcement while preserving the object and its settings for a corrected retry:

1. In the Group Policy Management Console, right-click the link and select **Delete link**.
2. Run `gpupdate /force` on affected endpoints, or wait for the normal refresh window.

</Accordion>

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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/04-Enterprise_Deployment.md §macOS: MDM (Intune / Jamf) */}

<Accordion title="MDM console paths">

**Microsoft Intune**

1. Intune admin center **→ Devices → Configuration profiles**.
2. **Create profile**, platform **macOS**, profile type **Settings catalog**.
3. Search for **Proxy** and select **Network → Proxy → Web Proxy**.
4. Set the web proxy server and port, and the bypass list for hosts and domains.
5. Assign to the pilot macOS device group and create the profile.

Devices apply it at their next check-in, typically within about fifteen minutes.

**Jamf Pro**

1. **Computers → Configuration Profiles → New**.
2. Select **Network** and configure.
3. On the **Proxies** tab, enable **Web Proxy (HTTP)**, set the server and port, and set the bypass list.
4. Scope to the pilot computer group and save.

Devices apply the profile on their next check-in.

</Accordion>

Verify on a managed macOS endpoint:

```bash
profiles status -type enrollment
scutil --proxy
```

Expected result: the device is managed and the assigned profile is present.

Expected result for `scutil --proxy`: the reported proxy matches the approved SafeSquid listener.

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

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/04-Enterprise_Deployment.md §Linux: Ansible */}

<Accordion title="Ansible playbook and rollback">

Covers the shell environment, both package managers, and a login-shell profile script, so terminal sessions and package operations route consistently.

```yaml
---
- name: Deploy SafeSquid proxy configuration
  hosts: all
  become: yes
  tasks:
    - name: Configure system proxy in /etc/environment
      lineinfile:
        path: /etc/environment
        line: "{{ item }}"
        create: yes
      loop:
        - 'http_proxy="http://SAFESQUID-IP:8080"'
        - 'https_proxy="http://SAFESQUID-IP:8080"'
        - 'ftp_proxy="http://SAFESQUID-IP:8080"'
        - 'no_proxy="localhost,127.0.0.1,.internal.example.com"'

    - name: Configure APT proxy
      copy:
        dest: /etc/apt/apt.conf.d/95proxies
        content: |
          Acquire::http::Proxy "http://SAFESQUID-IP:8080";
          Acquire::https::Proxy "http://SAFESQUID-IP:8080";
      when: ansible_os_family == "Debian"

    - name: Configure YUM proxy
      lineinfile:
        path: /etc/yum.conf
        line: "proxy=http://SAFESQUID-IP:8080"
      when: ansible_os_family == "RedHat"

    - name: Create profile.d proxy script
      copy:
        dest: /etc/profile.d/proxy.sh
        mode: '0644'
        content: |
          export http_proxy=http://SAFESQUID-IP:8080
          export https_proxy=http://SAFESQUID-IP:8080
          export no_proxy=localhost,127.0.0.1,.internal.example.com
```

Run against one host before the fleet:

```bash
ansible-playbook -i inventory safesquid-proxy.yml --limit testhost
ansible-playbook -i inventory safesquid-proxy.yml
```

**Rollback.** Removing the playbook does not remove what it wrote. Keep a paired teardown and test it before the rollout, not during the incident:

```yaml
---
- name: Remove SafeSquid proxy configuration
  hosts: all
  become: yes
  tasks:
    - name: Remove proxy lines from /etc/environment
      lineinfile:
        path: /etc/environment
        regexp: '.*proxy.*'
        state: absent

    - name: Remove APT proxy config
      file:
        path: /etc/apt/apt.conf.d/95proxies
        state: absent

    - name: Remove YUM proxy setting
      lineinfile:
        path: /etc/yum.conf
        regexp: '^proxy='
        state: absent

    - name: Remove profile.d proxy script
      file:
        path: /etc/profile.d/proxy.sh
        state: absent
```

Capture the playbook run ID and the managed host list with the change record.

</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/05-Connect_Your_Client/04-Enterprise_Deployment.md §Linux: Puppet */}

<Accordion title="Puppet class">

```puppet
class safesquid_proxy (
  String $proxy_server = 'SAFESQUID-IP:8080',
  String $no_proxy     = 'localhost,127.0.0.1,.internal.example.com',
) {

  file { '/etc/profile.d/proxy.sh':
    ensure  => file,
    mode    => '0644',
    content => epp('safesquid_proxy/proxy.sh.epp', {
      'proxy_server' => $proxy_server,
      'no_proxy'     => $no_proxy,
    }),
  }

  if $facts['os']['family'] == 'Debian' {
    file { '/etc/apt/apt.conf.d/95proxies':
      ensure  => file,
      content => "Acquire::http::Proxy \"http://${proxy_server}\";\nAcquire::https::Proxy \"http://${proxy_server}\";\n",
    }
  }

  if $facts['os']['family'] == 'RedHat' {
    ini_setting { 'yum_proxy':
      path    => '/etc/yum.conf',
      section => 'main',
      setting => 'proxy',
      value   => "http://${proxy_server}",
    }
  }
}
```

Template at `modules/safesquid_proxy/templates/proxy.sh.epp`:

```bash
export http_proxy=http://<%= $proxy_server %>
export https_proxy=http://<%= $proxy_server %>
export no_proxy=<%= $no_proxy %>
```

Apply to scoped nodes in `site.pp`, keeping the match narrow enough to stay inside the current rollout ring:

```puppet
node /^workstation.*\.example\.com$/ {
  include safesquid_proxy
}
```

Capture the catalog report and the list of changed resources with the change record.

</Accordion>

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
|---|---|---|
| Users lose all web access | Proxy host, port, or PAC URL is wrong | Roll back the policy scope and fix the setting |
| Some users bypass SafeSquid | Scope or policy inheritance is incomplete | Check endpoint policy result and group assignment |
| Business app breaks | Missing PAC bypass or proxy incompatibility | Add a reviewed bypass or application-specific exception |
| Logs lack user context | Authentication is not configured or not matching | Verify authentication before expanding rollout |
| MDM profile reports an error state | Enrollment problem or a malformed profile | Check the MDM logs for the device, correct the profile, and re-send it |
| Ansible fails on a subset of hosts | SSH reachability or sudo rights | Test with `ansible all -m ping`, then confirm keys and privilege escalation on the failing hosts |
| Puppet nodes never receive the change | Agent stopped or cannot reach the master | Check `systemctl status puppet`, then run `puppet agent -t --verbose` to see the failure |
| PAC file does not load on managed clients | DNS or firewall blocks the hosting URL from the client network | Resolve and fetch the URL from an affected client: `nslookup` the host, then `curl` the file |

## Next steps

- [Application-Specific Configuration](/getting_started/client_configuration/application_specific_configuration) - handle tools that ignore managed proxy settings.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - enforce controls after routing is stable.
- [Reporting Service](/safesquid_swg/interface/reporting_service) - preserve rollout and access evidence.
