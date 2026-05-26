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

- Proxy settings must reach many managed endpoints.
- Users must not control the production proxy configuration.
- Security teams need consistent traffic flow, user attribution, and audit evidence.
- Rollout must be tracked through change control.

Complete [Explicit Proxy](/getting_started/client_configuration/explicit_proxy) or [PAC File](/getting_started/client_configuration/pac_file) validation before enterprise rollout.

## Validate prerequisites

Before touching fleet policy, confirm:

- SafeSquid nodes are sized and reachable from target networks.
- The chosen method is owned by the endpoint team: GPO, Intune, Jamf, MDM, Ansible, Puppet, or equivalent.
- Pilot users, pilot devices, and rollback owners are named in the change record.
- SSL inspection Root CA deployment is ready before HTTPS inspection is enforced.
- Authentication and reporting owners know how to verify user attribution.
- Direct internet egress is restricted where policy requires mandatory proxy use.

## Choose the rollout method

| Managed estate | Recommended method | Evidence to capture |
|---|---|---|
| Windows domain endpoints | Group Policy Object (GPO) | GPO link, scope, `gpresult`, client proxy state |
| Windows cloud-managed endpoints | Intune device configuration | Assignment group, profile status, client proxy state |
| macOS endpoints | Jamf or MDM profile | Profile scope, installation status, proxy state |
| Linux servers or workstations | Ansible or Puppet | Inventory scope, task output, config file diff |
| Mixed browser estate | PAC URL through endpoint management | PAC URL, checksum, bypass approval, client fetch result |

## Stage the deployment

Use staged rollout for every production change:

1. **Lab group** - one administrator-owned endpoint per operating system.
2. **Pilot group** - 5 to 20 users from one business function.
3. **Department group** - one department or branch with support coverage.
4. **Production group** - broad rollout after evidence and support readiness are complete.

Do not expand stages until the previous stage shows successful traffic flow, acceptable user impact, and working rollback.

## Deploy with GPO

For Windows domain environments:

1. Create a dedicated GPO, such as **SafeSquid Proxy - Pilot**.
2. Scope it to the pilot organizational unit or security group only.
3. Configure proxy settings or PAC URL under the approved Windows policy path used by your endpoint standard.
4. Link the GPO to the pilot scope.
5. Run a policy refresh on one test endpoint.

```powershell
gpupdate /force
gpresult /h C:\Temp\safesquid_proxy_gpresult.html
netsh winhttp show proxy
```

Confirm browser proxy state and run a proxied HTTP test before adding more users.

## Deploy with MDM

For Intune, Jamf, or another MDM:

1. Create a dedicated pilot profile.
2. Set the manual proxy or PAC URL.
3. Assign the profile to the pilot device group.
4. Wait for device check-in and profile installation.
5. Verify proxy state on one endpoint before expanding assignment.

For macOS, verify locally:

```bash
scutil --proxy
```

## Deploy with configuration management

For Linux or mixed server estates, deploy a minimal proxy configuration first. Keep the inventory group small.

```yaml
- name: Configure SafeSquid proxy environment
  hosts: safesquid_proxy_pilot
  become: true
  tasks:
    - name: Write proxy environment file
      copy:
        dest: /etc/profile.d/safesquid_proxy.sh
        mode: '0644'
        content: |
          export http_proxy=http://SAFESQUID-IP:8080
          export https_proxy=http://SAFESQUID-IP:8080
          export no_proxy=localhost,127.0.0.1,.example.internal
```

Test one host before broad deployment:

```bash
ansible-playbook safesquid_proxy.yml --limit pilot-host.example.internal --check
ansible-playbook safesquid_proxy.yml --limit pilot-host.example.internal
```

## Verify rollout evidence

For each stage, prove:

- Client setting points to the approved SafeSquid proxy or PAC URL.
- A public HTTP request appears in `/var/log/safesquid/access/extended.log`.
- HTTPS works without certificate warnings after Root CA deployment.
- Authentication maps the request to the expected user or group.
- Reporting Service or SIEM receives the transaction if forwarding is enabled.
- Blocked-category test shows matched rule, action, user, URL, and timestamp.

## Roll back safely

Document rollback before rollout starts:

- GPO: unlink or disable the pilot GPO, then run `gpupdate /force`.
- Intune or Jamf: remove the assignment or deploy a replacement profile.
- PAC: restore the previous PAC URL or file version.
- Ansible or Puppet: apply the previous config and verify removal.
- Firewall: restore pre-change egress only if security leadership approves bypass risk.

Rollback is complete only after the endpoint proxy state and SafeSquid logs confirm traffic returned to the expected path.

## Troubleshoot rollout failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Some users do not receive settings | Scope, group membership, or device check-in issue | Verify policy assignment and endpoint management status |
| Settings apply but traffic bypasses SafeSquid | Direct egress remains open or app ignores proxy | Restrict direct egress and configure app-specific proxy settings |
| HTTPS fails after rollout | Root CA not installed or wrong trust store | Deploy Root CA through endpoint management and retest |
| Logs show IP but no user | Authentication not enabled or user mapping failed | Configure authentication and repeat test from known users |
| Business app breaks | Missing PAC bypass or proxy incompatibility | Add a reviewed bypass or application-specific exception |

## Next steps

- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - complete HTTPS visibility with managed Root CA deployment.
- [Authentication](/use_cases/authentication/authentication) - add user and group attribution.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - enforce baseline controls after routing is stable.

