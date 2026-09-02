---
title: Manage Subscription State
description: Handle SafeSquid commercial subscription expiry — what degrades, what keeps running, and how to renew or extend the conservation period.
keywords:
  - SafeSquid subscription expiry
  - renew subscription
  - conservation period
  - licence renewal
  - degraded feed schedule
---

# Handle Expiry Before It Degrades Enforcement

Expiry degrades the deployment; it does not stop it. Core proxy and filtering keep running, so nothing obvious breaks — and that is the risk. Threat feeds quietly drop to a weekly schedule while the deployment reports itself healthy, and the gap only becomes visible when something current gets through.

Knowing which half still works prevents an unnecessary emergency, and knowing which half does not prevents a false sense of coverage.

{/* source: _migration_source_v3/docs/01-Getting_Started/04-Activate.md §Troubleshooting case4 License Expired */}

## Know what expiry changes

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

## Choose the recovery option

{/* NEEDS-SME-REVIEW: "Manage Account" confirmed still absent from the local safesquid.cfg admin interface as of 2026-09-02 — it is not the local Support page (verified live this session: License Details panel plus Support Tarball, Download/Upload Config, Upgradation, Performance Plot, URL Commands, Restart SafeSquid, Cloud Restore, Startup params, Live Support — no "Manage Account" among them, see admin_guide/infrastructure_and_access/support.mdx). So this workflow is external-portal-only, narrowing but not yet closing the original question — still need a logged-in screenshot of key.safesquid.com to confirm "Manage Account" / "Renew Subscription" / "Extend Conservation Period" are still the current labels there. The "each extension adds three days" figure is also still unverified. */}

**Option 1 — renew.** Sign in to [key.safesquid.com](https://key.safesquid.com), go to **Manage Account** and then **Renew Subscription**. After payment, download the updated activation key and upload it under [Subscription](/admin_guide/infrastructure_and_access/subscription) using the same steps as the initial activation.

**Option 2 — extend the conservation period.** From **Manage Account**, select **Extend Conservation Period**. Each extension adds three days and clears the expiry banner for that window. It can be applied more than once, but it is a bridge to renewal, not a substitute for it — treat repeated extensions as a signal that subscription ownership needs attention.

Restart SafeSquid from the interface after either action — see
[Support](/admin_guide/infrastructure_and_access/support) — so the new state takes effect.

<Steps>
  <Step title="Confirm subscription ownership">
    Identify who owns the subscription account before taking either action.

    Confirm the account owner approves the renewal or conservation-period path.

    If subscription ownership is unclear, pause and resolve it — an extension applied without an owner defers the problem without assigning it.
  </Step>
  <Step title="Apply the renewal or extension">
    Use the Self-Service Portal workflow for the approved option.

    Confirm the action completes and the updated key is downloaded, where renewing.

    ![Extend conservation period option in the activation workflow](/images/getting_started/activate_06_extend_conservation_period.webp)
  </Step>
  <Step title="Restart and verify">
    Restart SafeSquid from the interface, then confirm subscription state in the [Configuration Portal](/safesquid_swg/interface/configuration_portal).

    Confirm the expiry banner is cleared and feed schedules have returned to the commercial cadence.

    If the state has not changed, re-check that the updated key was uploaded, not just downloaded.
  </Step>
</Steps>

## Capture subscription evidence

Store these artifacts with the deployment record:

- Which option was used, renewal or conservation period, and who approved it.
- The date of the action and the new expiry date.
- A record of subscription state from the Configuration Portal after the restart.
- The named owner of the subscription and the renewal review date.

## Troubleshoot subscription state

| Symptom | Likely cause | Fix |
|---|---|---|
| Expiry banner persists after renewal | Updated key was downloaded but not uploaded | Upload the new `activation_key` through the interface and restart |
| Feeds stay on the weekly schedule | SafeSquid was not restarted after the key upload | Restart from the interface and re-check subscription state |
| Conservation period cannot be extended | Extension already applied for the current window | Renew the subscription; extensions bridge to renewal, they do not replace it |
| Renewal succeeds, threat intelligence stays off | Outbound update endpoints are blocked | Confirm the update paths in [Ports and Firewall Rules](/deployment/ports_and_firewall_rules) |
| Nobody knows who owns renewal | Subscription ownership was never recorded | Assign an owner and a review date before the next expiry |

## Next steps

- [Licensing Requirements](/deployment/licensing_requirements) - confirm what the tier includes.
- [Activate Your License](/getting_started/activate) - re-apply an updated activation key.
- [Ports and Firewall Rules](/deployment/ports_and_firewall_rules) - confirm the update paths are reachable.
