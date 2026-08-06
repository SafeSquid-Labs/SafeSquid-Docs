---
title: "User Groups"
description: "Configure user groups in SafeSquid for group-based web access policies, enabling differentiated security controls for departments, roles, and teams."
keywords: ["SafeSquid user groups", "group-based access policies", "user group configuration", "department web policies", "role-based proxy access"]
---

# Design and verify user groups

User groups turn authenticated identity into manageable policy scope. Use them to express business roles such as workforce, contractors, privileged administrators, or restricted devices without creating one policy for every person.

<Warning>
  The exact group-source fields, matching behavior, and policy ordering still require release-lab verification. Confirm them against your target build before a production change.
</Warning>

## Outcome

You will have:

- A documented source of group membership.
- A deterministic mapping from identities to SafeSquid policy groups.
- Test identities for positive, negative, and ambiguous cases.
- Evidence that the intended group, rather than a fallback identity, selected the policy.
- A rollback path that restores the previous mapping.

| Item | Value |
| --- | --- |
| Intended reader | Identity administrator, security technician, policy engineer |
| When to use | Before group-based policy is introduced or changed |
| Estimated planning time | 30-60 minutes, excluding directory changes |
| Change impact | Incorrect mappings can over-permit or block many users |
| Maintenance requirement | Recheck after directory, authentication, policy, or release changes |

## Prerequisites

- [Authentication design](/use_cases/authentication/authentication) is agreed and tested.
- SafeSquid receives an attributable identity for the controlled client.
- The identity source has stable group identifiers and a named owner.
- A test user exists for each expected outcome.
- The current identity and policy configuration has been exported or recorded.
- Emergency administrative access does not depend on the group mapping being changed.

## Input worksheet

| Input | Where to obtain it | Valid form | Safe example | Sensitive? |
| --- | --- | --- | --- | --- |
| Identity source | Identity architecture record | Supported directory or authentication source | Corporate directory | No |
| Group identifier | Directory administrator | Exact stable identifier used by the integration | Web-Restricted | Usually no |
| Membership model | Directory design | Direct, nested, or calculated membership as supported | Direct | No |
| Test identity | Synthetic test account inventory | Non-production account | test.contractor | Yes |
| Intended policy | Approved policy matrix | Existing policy name or change record | Contractor Baseline | No |
| Fallback outcome | Security decision record | Deny, restricted baseline, or approved alternative | Restricted baseline | No |
| Evidence location | Change or test record | Restricted case or repository path | CHG-2026-0042 | Yes |

Do not paste passwords, directory bind secrets, access tokens, or unredacted directory exports into this worksheet.

## Build the mapping model

1. List the business roles that genuinely need different web controls.
   **Checkpoint:** each role has a policy difference that can be stated and approved. Remove groups that exist only because the directory contains them.
2. Select a stable identity-source group for each role.
   **Checkpoint:** the directory owner confirms the identifier, membership owner, and whether nested membership is expected.
3. Define precedence for users who belong to more than one relevant group.
   **Checkpoint:** the policy matrix contains one expected outcome for every overlap case. No row says “whichever matches first” without proving the product order.
4. Define the unmatched and identity-failure outcome.
   **Checkpoint:** the fallback is explicit, least-privileged, and testable.
5. Prepare synthetic test identities.
   **Checkpoint:** include one member, one non-member, one multi-group user, and one identity that should exercise the fallback.

## Policy test matrix

| Test identity | Source membership | Expected SafeSquid group | Expected policy result | Evidence |
| --- | --- | --- | --- | --- |
| test.employee | Employee only | Employee baseline | Approved employee test URL follows baseline | Identity and policy event |
| test.contractor | Contractor only | Contractor restricted | Restricted category is blocked | Block event with selected policy |
| test.multigroup | Employee and privileged test group | Approved precedence result | Privileged test action follows the agreed rule | Identity and policy event |
| test.unmatched | No mapped group | Fallback | Restricted baseline or deny result | Fallback event |
| Unauthenticated test | No usable identity | Authentication failure outcome | Challenge, deny, or approved fallback | Authentication event |

Replace these examples with synthetic identities and safe destinations from your test environment.

## Verification

For every matrix row:

1. Start a fresh authenticated session so cached identity does not hide the change.
2. Generate one allowed request and one deliberately restricted request.
3. Confirm the observed username or identity is the synthetic test account.
4. Confirm the resolved group matches the matrix.
5. Confirm the named policy action matches the expected outcome.
6. Record timestamps and correlate the identity, policy, and access events.
7. Repeat from a client that should not inherit the group.

**Complete only when:** all positive, negative, overlap, and fallback cases behave as approved, and the evidence identifies the user, group decision, policy, action, release, and test time.

## Failure patterns

| Observation | Discriminating check | Likely area |
| --- | --- | --- |
| Every user receives the same policy | Compare observed identity and fallback behavior | Authentication or default policy |
| Direct members work but nested members do not | Compare direct and nested synthetic users | Directory membership semantics |
| Membership changes appear late | Start a fresh session and check identity or directory caches | Cache or synchronization |
| Multi-group users receive an unexpected policy | Compare the approved matrix with observed policy order | Precedence or policy ordering |
| Group name looks correct but never matches | Compare exact identifiers, case, and source attributes | Identifier normalization |
| Logs show identity but not the intended group | Verify that the policy consumes the mapped attribute | Mapping or policy scope |

Stop broad policy changes when the observed identity or group cannot be proven. Collect evidence and isolate identity, mapping, and policy evaluation as separate stages.

## Rollback

1. Restore the recorded identity and group mapping.
2. Restore the previous policy scope or disable the new group-specific rule according to change control.
3. Start a fresh test session.
4. Confirm the previous allowed and blocked outcomes.
5. Record the rollback result and any identities that remained cached.

## Evidence to retain

- Approved group-to-policy matrix.
- Sanitized group identifiers and synthetic memberships.
- Applicable release and exact build.
- Before-and-after configuration record.
- Identity, group-resolution, policy, and access events for every matrix row.
- Rollback transcript.
- Limitations found during testing.

Related guidance:

- [Authentication](/use_cases/authentication/authentication)
- [Access restriction](/use_cases/access_restriction/access_restriction)
- [Documentation trust](/reference/documentation-trust)