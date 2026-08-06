---
title: "Speed Limits"
description: "Configure connection speed limits in SafeSquid to control per-user or per-group bandwidth consumption."
keywords: ["speed limits", "SafeSquid bandwidth control", "per-user bandwidth", "connection speed limits", "SafeSquid SWG"]
---

# Plan and verify speed limits

Speed limits can keep one user, group, or traffic class from consuming disproportionate capacity. They are not a substitute for link sizing, congestion management, or application-aware quality of service.

<Warning>
  The exact configuration fields, measurement interval, unit interpretation, matching scope, and behavior for concurrent transfers require verification against the target SafeSquid build.
</Warning>

## Outcome

You will have a bounded test that distinguishes SafeSquid policy enforcement from endpoint, server, or network bottlenecks.

| Item | Value |
| --- | --- |
| Intended reader | Network technician, SafeSquid administrator, capacity engineer |
| When to use | Before introducing or changing a traffic speed policy |
| Estimated time | 30-45 minutes for a controlled test |
| Change impact | A low or broad limit can degrade many users and business applications |
| Maintenance requirement | Recheck after policy, topology, capacity, or release changes |

## Before you start

- Confirm the client reaches the intended SafeSquid node.
- Record the available link capacity and known upstream constraints.
- Select a controlled test client and a permitted large test object.
- Ensure no other shaping policy, VPN, endpoint agent, browser extension, or test-server limit obscures the result.
- Export or record the current configuration and policy order.
- Define an approved rollback condition.

## Input worksheet

| Input | Where to obtain it | Valid form | Safe example | Sensitive? |
| --- | --- | --- | --- | --- |
| Test client | Lab inventory | Controlled endpoint and IP | 192.0.2.25 | No |
| Identity or group | Identity test matrix | Synthetic identity | test.bandwidth | Yes |
| Traffic class | Approved policy design | URL, category, MIME type, or other supported match | Approved test download | No |
| Proposed limit | Capacity plan | Explicit value and unit | 5 Mbit/s | No |
| Baseline throughput | Repeated control test | Median observed rate | 40 Mbit/s | No |
| Concurrency | Test plan | Number of simultaneous transfers | 1, then 2 | No |
| Test duration | Test plan | Long enough to avoid startup effects | 60 seconds | No |
| Rollback trigger | Change record | Observable impact threshold | Business app latency exceeds SLO | No |

Use documentation-only addresses and synthetic identities in published examples. Do not upload production captures or credentials.

## Establish a baseline

1. Run the approved transfer without the new limit.
   **Checkpoint:** record at least three observations and use the median. The result is stable enough to distinguish a policy cap from ordinary variation.
2. Correlate the transfer with SafeSquid access and policy events.
   **Checkpoint:** the event identifies the expected client or user, destination, policy path, and proxy node.
3. Confirm the test path has capacity above the proposed limit.
   **Checkpoint:** the baseline is materially higher than the cap. If it is not, this test cannot prove enforcement.

## Apply the test policy

Configure the smallest possible scope using the fields supported by the target build. Limit only the synthetic identity or controlled client and the approved test traffic.

Before activation, independently check:

- Numeric value and unit.
- Upload, download, or combined direction.
- Per-connection, per-user, per-group, or shared scope.
- Policy order and fallback.
- Schedule and time zone.
- Exclusions.
- Expected behavior when identity is unavailable.

<Warning>
  Do not infer whether a limit is shared or applied separately to each connection. Prove it with the concurrency test.
</Warning>

## Verification matrix

| Test | Expected observation | What it discriminates |
| --- | --- | --- |
| One matching transfer | Sustained rate approaches the configured bound after startup | Basic enforcement |
| Two matching transfers from one identity | Aggregate and per-transfer rates reveal sharing behavior | Per-connection versus per-identity scope |
| Non-matching identity | Baseline behavior remains unchanged | Identity and policy scope |
| Non-matching destination | Baseline behavior remains unchanged | Traffic match |
| Policy disabled or rolled back | Original median behavior returns | Causality |
| Business application smoke test | No material regression outside intended scope | Blast radius |

Capture enough samples to show sustained behavior. A browser’s instantaneous speed display is not sufficient evidence by itself.

## Diagnose unexpected results

| Observation | Check first | Possible cause |
| --- | --- | --- |
| Rate is below both baseline and limit | Repeat the baseline and inspect path utilization | Upstream congestion or server limit |
| Rate is unchanged | Confirm node, identity, match, policy order, and activation state | Policy did not apply |
| Each download receives the full limit | Compare one and two concurrent transfers | Per-connection enforcement |
| Unrelated users slow down | Inspect group scope and shared identifiers | Policy scope is too broad |
| Short transfers appear uncapped | Use a larger safe object and longer interval | Startup burst or measurement window |
| Upload and download differ | Verify direction and test each independently | Direction-specific configuration |
| Result varies by proxy node | Compare configuration and build evidence per node | Cluster inconsistency |

Stop and roll back when the observed scope is broader than approved or when a critical application is affected.

## End-to-end evidence

Retain:

- Exact build and node identity.
- Before-and-after configuration record.
- Policy match criteria and order.
- Baseline and limited observations with timestamps.
- One-transfer and concurrent-transfer results.
- Correlated SafeSquid events.
- Non-matching control tests.
- Rollback result.
- Known measurement uncertainty.

## Rollback

1. Disable or restore the changed speed-limit policy using the approved configuration record.
2. Start a fresh client session.
3. Repeat the baseline and non-matching control tests.
4. Confirm business application health.
5. Record the rollback time, operator, observed result, and any residual effect.

Related guidance:

- [Bandwidth management](/admin_guide/performance_acceleration/manage_bandwidth)
- [Performance plot](/admin_guide/performance_acceleration/performance_plot)
- [Troubleshooting method](/troubleshooting/troubleshooting)