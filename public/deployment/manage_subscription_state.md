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

{/* NEEDS-SME-REVIEW: confirmed live 2026-09-02 (logged-in portal view) — "Manage Account" is a real, current portal tab (alongside Manage Key, Manage Categories, Manage Certificates, Manage VPN, Manage Signatures), still absent from the local safesquid.cfg Support page as expected. Its subscription panel shows Subscription ID, C-Code, Key Name, Plan, Named Users, No of Instances, Support Validity, and one action button labeled **"Conserve Subscription"** — not "Extend Conservation Period" as below; that label matches only the old screenshot referenced further down (dated 1 July 2022, Subscription ID 2263), which is now stale. No "Renew Subscription" button was visible for this account's Plan: Trial — whether it appears for a Commercial-plan account is unconfirmed, so Option 1 below is not verified as currently written. Also unresolved: the Manage Key panel's Support Validity for this key read "25-Aug-2027" while the Manage Account panel read "24-Sep-2026" for what should be the same subscription — don't treat either as authoritative without asking which one the portal actually enforces. The "each extension adds three days" figure is still unverified. */}

**Option 1 — renew.** Sign in to [key.safesquid.com](https://key.safesquid.com) and go to **Manage
Account**. **Missing:** whether a "Renew Subscription" action is available there is unconfirmed —
it wasn't visible for a Trial-plan account when last checked (2026-09-02); a Commercial plan may
show it. If you don't see it, contact SafeSquid support rather than assuming renewal isn't
possible. After renewing, download the updated activation key and upload it under
[Subscription](/admin_guide/infrastructure_and_access/subscription) using the same steps as the
initial activation.

**Option 2 — conserve the subscription.** From **Manage Account**, use **Conserve Subscription**
(this button was previously labeled "Extend Conservation Period" — confirm which label your
portal shows, since this has changed at least once). It extends the support window and clears
the expiry banner for that period. It can be applied more than once, but it is a bridge to
renewal, not a substitute for it — treat repeated use as a signal that subscription ownership
needs attention.

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

    {/* NEEDS-SME-REVIEW: this screenshot is stale — dated 1 July 2022 (Subscription ID 2263), and shows the action button labeled "Extend Conservation Period". The live portal as of 2026-09-02 labels the equivalent button "Conserve Subscription". Recapture before publishing further revisions of this page. */}
    ![Conserve Subscription option on the Manage Account tab — screenshot predates the current "Conserve Subscription" label, shown here as "Extend Conservation Period"](/images/getting_started/activate_06_extend_conservation_period.webp)
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
