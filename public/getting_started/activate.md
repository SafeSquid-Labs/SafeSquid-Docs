---
title: Activate Your License
description: Upload the SafeSquid activation key, verify licensed state, and capture evidence before configuring production policy.
keywords:
  - SafeSquid activation
  - activation key
  - SafeSquid license
  - license verification
  - deployment smoke test
---

# Activate Before Policy Rollout

SafeSquid must be activated before the deployment can be treated as ready for enforcement. Activation ties the instance to the Self-Service Portal, unlocks licensed capability, and gives operators a checkpoint before SSL inspection, authentication, URL controls, malware scanning, and DLP are enabled.

{/* source: _migration_source_v3/docs/01-Getting_Started/04-Activate.md §Key Benefits (licensing tiers) */}

## Know what activation unlocks

SafeSquid offers two licensing tiers. An unactivated instance runs with limited capability regardless of which tier you hold.

| Capability | Free | Commercial |
|---|:--:|:--:|
| Core proxy and filtering | Yes | Yes |
| SSL inspection | Yes | Yes |
| Custom policies and profiles | Yes | Yes |
| Real-time threat intelligence | No | Yes |
| URL categorization database | No | Yes |
| Disaster-recovery backup, 365 days | No | Yes |
| Email support | No | Yes |

The free licence has no time limit. Upgrade to commercial at any point through the [Self-Service Portal](https://key.safesquid.com); the deployment steps are the same for both tiers.

Activation also matters for audit: licensed state is visible in the Configuration Portal and serves as evidence that the gateway is correctly licensed.

## Validate prerequisites

Before activation, confirm:

- The `activation_key` file was downloaded from the [Self-Service Portal](/getting_started/register).
- SafeSquid service is running.
- A pilot browser can reach `http://safesquid.cfg/` through the proxy path.
- The administrator is on an approved management network.
- Outbound DNS and HTTPS access are available for license and subscription validation.
- The change record includes rollback steps for client routing and firewall changes.

## Allow subscription paths

Activation and subscription refresh require outbound reachability. Confirm the network team has reviewed the required paths for the installed release and subscription. The legacy activation guide identifies these common dependencies:

| Host | Port | Purpose |
|---|---:|---|
| `api.safesquid.net` | `443` | License activation |
| `swgupdates2.safesquid.net` | `443` | Subscription and update checks |
| `swgupdates.safesquid.net` | `80` | Update services |
| `sslupdates.safesquid.com` | `443` | SSL certificate updates |
| `category.safesquid.net` | `443` | Category database updates |
| `download.quickheal.com` | `80` | Virus signature updates |

Treat this table as a deployment checklist, not a firewall exception template. Confirm current endpoint requirements through the approved release or support channel before production allowlisting.

{/* source: _migration_source_v3/docs/01-Getting_Started/04-Activate.md §Readiness Checklist */}

<Accordion title="Which endpoints block activation, and which do not">

Only one endpoint has to be reachable for activation itself to succeed. The rest affect ongoing updates, so a blocked path there produces a licensed gateway with stale intelligence rather than a failed activation — a quieter failure, and an easier one to miss.

**Required for activation**

| Host | Port | Purpose |
|---|---:|---|
| `api.safesquid.net` | `443` | License activation |

**Required for ongoing updates**

| Host | Port | Purpose |
|---|---:|---|
| `swgupdates2.safesquid.net` | `443` | Subscription and malware definitions |
| `swgupdates.safesquid.net` | `80` | Seqrite updates |
| `sslupdates.safesquid.com` | `443` | SSL certificate updates |
| `category.safesquid.net` | `443` | Category database updates |
| `download.quickheal.com` | `80` | Virus signature updates |

**URL categorization engines, commercial licence only**

Each of these is reached on port `8080` at the path `/URLCategorizerService/URLCategorize`:

| Host |
|---|
| `prourl.itsecure.co.in` |
| `encurl.itsecure.co.in` |
| `klassify.itsecure.co.in` |
| `prourl.itonlinesecure.in` |
| `encurl.itonlinesecure.in` |

If categorization is blocked while everything else is reachable, policies that depend on category matching will fail open rather than error, so verify this group explicitly rather than inferring it from a working activation.

</Accordion>

## Upload the activation key

<Steps>
  <Step title="Open the proxied interface">
    Configure the pilot browser to use SafeSquid as proxy, open `http://safesquid.cfg/`, and sign in with the approved administrator account.

    Confirm the Configuration Portal loads through the SafeSquid proxy path.

    If `safesquid.cfg` does not load, recheck pilot browser proxy settings and SafeSquid listener reachability.

    ![Upload activation key prompt in the SafeSquid Configuration Portal](/images/getting_started/activate_01_upload_activation_key_prompt.webp)
  </Step>
  <Step title="Select the activation key">
    When the first-run activation prompt appears, click **Choose File** or the file-selector control and select the `activation_key` file from the approved secure location.

    Confirm the selected file is named exactly `activation_key`.

    If the key is missing or renamed, retrieve the original file from approved secure storage or re-download it from the Self-Service Portal.

    ![Select the activation key file and upload it](/images/getting_started/activate_02_select_and_upload_key.webp)
  </Step>
  <Step title="Upload and restart">
    Click **Upload**, then click **Restart** when the interface prompts you to apply the license.

    Confirm the interface accepts the upload and presents the restart action.

    If upload fails, verify file name, file contents, and outbound subscription reachability before retrying.

    ![Restart SafeSquid after activation key upload](/images/getting_started/activate_03_restart_safesquid.webp)
  </Step>
  <Step title="Wait for reload">
    Wait for SafeSquid to restart and reload the Configuration Portal before running evidence checks.

    Confirm the portal reloads after restart and accepts administrator sign-in.

    If the proxy refuses connections, check service state from the server console before routing users.
  </Step>
</Steps>

Do not route production users until activation has been verified and logged.

<Note>
  **License evidence:** The activation key is not the audit artifact. Store the key securely, and capture license-state evidence from the Configuration Portal plus service, listener, and access-log checks.
</Note>

## Verify activation evidence

Run these checks immediately after activation.

<Steps>
  <Step title="Confirm the service is running">
    Run the service-state check and confirm there are no recent startup errors.

    ```bash
    systemctl status safesquid --no-pager
    ```

    Confirm the service is active and no startup error appears in the recent log.

    If the service is inactive, inspect the service journal and restart SafeSquid from the server console after correcting the cause.
  </Step>
  <Step title="Confirm the key exists on disk">
    Verify that `/usr/local/safesquid/security/activation_key` exists and has not been renamed.

    ```bash
    ls -l /usr/local/safesquid/security/activation_key
    ```

    Confirm a file named exactly `activation_key` exists.

    If it is missing or renamed, re-upload the downloaded key file.
  </Step>
  <Step title="Confirm listener state">
    Confirm SafeSquid listens on the approved proxy port.

    ```bash
    ss -lntp | grep ':8080'
    ```

    Confirm SafeSquid listens on the approved proxy port.

    If no listener appears, verify service state, startup logs, and the configured proxy port.
  </Step>
  <Step title="Confirm interface license details">
    Open **Support** and inspect **Activation Details** for product and subscription state.

    ![Open the Support menu to view activation status](/images/getting_started/activate_04_support_menu.webp)

    ![Activation Details showing product and subscription state](/images/getting_started/activate_05_activation_details.webp)

    Confirm product type, subscription state, or activation details are populated.

    If details are missing, verify subscription reachability and re-upload the correct activation key.
  </Step>
  <Step title="Confirm HTTP traffic is logged">
    Send one pilot HTTP request through SafeSquid and confirm a new record appears in `/var/log/safesquid/access/extended.log`.

    ```bash
    curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
    ```

    ```bash
    tail -20 /var/log/safesquid/access/extended.log
    ```

    Confirm the access log records source, destination, timestamp, and action.

    If no log appears, confirm the client is using SafeSquid and inspect `/var/log/safesquid/access/extended.log`.
  </Step>
</Steps>

## Capture activation evidence

Store these artifacts with the deployment record:

- Activation key ownership record from the Self-Service Portal.
- Screenshot or change record showing active license state.
- SafeSquid service status output.
- Listener check for the approved proxy port.
- Access-log entry for a pilot HTTP request.
- Subscription path reachability result.
- Root CA rollout plan before HTTPS inspection.

## Troubleshoot activation

| Symptom | Likely cause | Fix |
|---|---|---|
| `safesquid.cfg` does not load | Browser is not using SafeSquid as proxy | Recheck pilot proxy settings and retry `http://safesquid.cfg/` |
| `Failed to set Subscription details` | Key file is missing, renamed, or not loaded | Verify `/usr/local/safesquid/security/activation_key` and re-upload the correct file |
| Proxy refuses connections after upload | Service restart failed | Check service state and start SafeSquid from the server console if needed |
| Subscription server is unreachable | DNS, routing, or firewall block | Test `nslookup swgupdates2.safesquid.net` and restore outbound access |
| HTTP request succeeds but no log appears | Client bypasses SafeSquid or wrong log path checked | Confirm proxy path and inspect `/var/log/safesquid/access/extended.log` |
| HTTPS warning appears | Root CA is not trusted or SSL inspection is incomplete | Deploy the Root CA through the approved trust path before retesting HTTPS |
| Commercial subscription is expiring | Renewal or conservation period was not planned | Confirm renewal status in the Self-Service Portal and record any approved conservation-period action |
| Commercial features are inert after a successful activation | A free-tier key was uploaded, or the key has expired | Open **Support** and check **Activation Details**: Product Type should read Commercial and Expiry should be in the future. If not, download the correct key from the Self-Service Portal and re-upload it |

{/* source: _migration_source_v3/docs/01-Getting_Started/04-Activate.md §Troubleshooting case4 License Expired */}

<Accordion title="What happens when a commercial subscription expires">

Expiry degrades the deployment; it does not stop it. Knowing which half still works prevents an unnecessary emergency.

**Continues working**

- Core proxy and filtering, uninterrupted.

**Reduces to the free-tier schedule**

| Feed | Update frequency after expiry |
|---|---|
| Anti-virus engine | Weekly |
| Web categorization | Weekly |
| SSL security updates | Weekly |
| Application and content signatures | Monthly |

**Becomes unavailable**

- Real-time threat intelligence, disaster-recovery backup, and email support.

Free licences do not expire, so this applies only to commercial subscriptions.

**Option 1 — renew.** Sign in to [key.safesquid.com](https://key.safesquid.com), go to **Manage Account** and then **Renew Subscription**. After payment, download the updated activation key and upload it using the same steps as the initial activation.

**Option 2 — extend the conservation period.** From **Manage Account**, select **Extend Conservation Period**. Each extension adds three days and clears the expiry banner for that window. It can be applied more than once, but it is a bridge to renewal, not a substitute for it — treat repeated extensions as a signal that subscription ownership needs attention.

Restart SafeSquid from the interface after either action so the new state takes effect, and record which option was used in the deployment evidence.

</Accordion>

<Steps>
  <Step title="Handle subscription expiry">
    Use the Self-Service Portal conservation-period workflow only when subscription ownership approves it.

    Confirm the renewal or conservation-period action is recorded in the deployment evidence.

    If subscription ownership is unclear, pause the action until the account owner approves the renewal path.

    ![Extend conservation period option in the activation workflow](/images/getting_started/activate_06_extend_conservation_period.webp)
  </Step>
</Steps>

## Move toward production

After activation, configure controls in this order:

<Steps>
  <Step title="Deploy SSL inspection safely">
    Use [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) only after the SafeSquid Root CA trust path is approved and deployed.

    Confirm the pilot endpoint trusts the SafeSquid Root CA before HTTPS inspection expands.

    If browsers show certificate warnings, stop expansion and fix the trust deployment.
  </Step>
  <Step title="Add identity attribution">
    Use [Authentication](/use_cases/authentication/authentication) to add user and group attribution.

    Confirm access logs show the expected user or group identity.

    If logs show only IP addresses, verify authentication policy and directory reachability.
  </Step>
  <Step title="Protect DNS and access">
    Use [Integrated DNS Security](/use_cases/dns_security/dns_security) and [Access Restriction](/use_cases/access_restriction/access_restriction) to enforce baseline destination controls.

    Confirm a controlled test domain produces the expected DNS or access-control action.

    If traffic bypasses controls, verify DNS path, proxy routing, and policy order.
  </Step>
  <Step title="Enable content security">
    Use [Malware Scanners](/use_cases/malware_scanning/malware_scanners) and [Data Leakage Prevention](/use_cases/data_leakage_prevention/data_leakage_prevention) to inspect risky downloads and uploads.

    Confirm test uploads or downloads match the expected malware or DLP disposition.

    If inspection does not occur, verify SSL inspection scope, file limits, and scanner status.
  </Step>
  <Step title="Preserve operational evidence">
    Use [Reporting Service](/safesquid_swg/interface/reporting_service) to preserve evidence for operations and audit.

    Confirm reports include timestamp, source, user, URL, action, and policy context.

    If reports lack audit value, verify log forwarding, retention, and identity attribution.
  </Step>
</Steps>

## Next steps

- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - apply the baseline control sequence.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - expand from pilot routing to managed rollout.
- [Troubleshooting](/troubleshooting/troubleshooting) - diagnose activation, routing, certificate, and policy failures.
