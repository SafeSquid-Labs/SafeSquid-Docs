---
title: Ports and Firewall Rules
description: The single reference for SafeSquid inbound listeners and outbound endpoints, with the source scopes each rule must be restricted to.
keywords:
  - SafeSquid firewall rules
  - proxy port 8080 8443
  - SafeSquid outbound endpoints
  - activation endpoints
  - update and categorization hosts
---

# Open Only What the Proxy Needs

A proxy port open to `0.0.0.0/0` is an open relay waiting to be found. An outbound path left closed is an activation that fails at 02:00 on cutover night. Both failures come from the same gap: firewall rules agreed informally and never written down with a scope.

This page is the single reference for those rules. Agree them with the network owner before installation.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Prepare the host before install, steps 6-7 */}

## Restrict the inbound listeners

Each rule has a named source scope. None should be opened to `0.0.0.0/0`.

| Port | Protocol | Purpose | Restrict to |
|---|---|---|---|
| `8080` | TCP | HTTP proxy listener | Approved client networks |
| `8443` | TCP | Management interface | Administrator workstations only |
| `53` | TCP/UDP | DNS, when [integrated DNS security](/use_cases/dns_security/dns_security) is used | Approved client networks |

The management interface is the highest-value target on the host — it changes policy for every user behind the proxy. Restrict it to administrator workstations, not to the client network.

## Allow the outbound paths

| Port | Purpose |
|---|---|
| `80`, `443` | Web access on behalf of clients, plus update and subscription paths |
| `53` | Upstream DNS resolution |

Outbound DNS goes to the root servers `A.ROOT-SERVERS.NET` through `M.ROOT-SERVERS.NET`, or to the upstream resolvers your network team designates. SafeSquid cannot categorize or resolve destinations without it.

{/* source: _migration_source_v3/docs/01-Getting_Started/01-Deployment_Planning.md §Firewall Whitelist Requirements */}

### Endpoints that block activation

Activation fails without these. Confirm them before the cutover window, not during it.

| Endpoint | Port | Purpose |
|---|---:|---|
| `key.safesquid.com` | `443` | License management and Self-Service Portal |
| `api.safesquid.net` | `443` | License activation |

### Endpoints that block updates, not activation

The instance activates without these, then quietly stops receiving current data. Treat them as required for a production deployment even though activation succeeds.

| Endpoint | Port | Purpose |
|---|---:|---|
| `swgupdates2.safesquid.net` | `443` | Software and package updates |
| `swgupdates.safesquid.net` | `80` | Legacy update repository |
| `sslupdates.safesquid.com` | `443` | SSL inspection and security updates |
| `category.safesquid.net` | `443` | URL categorization |
| `download.quickheal.com` | `80` | Antivirus signature updates |

{/* NEEDS-SME-REVIEW: the itsecure.co.in and itonlinesecure.in categorization endpoints below are listed inconsistently across sources — activate.md includes encurl.itonlinesecure.in, deployment_planning.md does not. Confirm the authoritative set for the shipping release before an operator allowlists them. */}

### Additional categorization endpoints

| Endpoint | Port |
|---|---:|
| `prourl.itsecure.co.in` | `8080` |
| `encurl.itsecure.co.in` | `8080` |
| `klassify.itsecure.co.in` | `8080` |
| `prourl.itonlinesecure.in` | `8080` |

Treat this page as a deployment checklist, not a firewall exception template. Confirm current endpoint requirements through the approved release or support channel before production allowlisting.

## Verify reachability before installing

```bash
nslookup key.safesquid.com
ping -c 3 key.safesquid.com
```

Expected result: the host resolves and reaches the Self-Service Portal path needed for key and activation workflows.

## Capture firewall evidence

Store these artifacts with the deployment record:

- The firewall change record, with owner, source CIDRs, destination services, test window, and rollback.
- Confirmation that `8443` is scoped to administrator networks only.
- Reachability output for the activation endpoints.
- The date of the last review of the outbound allowlist, and its owner.

## Troubleshoot firewall failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Activation fails, proxy works | `key.safesquid.com` or `api.safesquid.net` is blocked | Allow outbound `443` to both, then retry activation |
| Categorization is stale, activation is fine | Update and category endpoints are blocked | Allow the update endpoints above; activation success does not imply they are reachable |
| Proxy port is exposed too broadly | Rule was written without a source scope | Restrict to the approved client CIDRs and re-record the change |
| Management interface reachable from user networks | `8443` scoped to the client network | Re-scope to administrator workstations immediately; treat as an exposure |
| Host cannot resolve portal names | Outbound `53` blocked or resolver unreachable | Fix DNS before installation; every later step depends on it |

## Next steps

- [Deployment Checklist](/getting_started/install_safesquid/prerequisites) - confirm the resolver, time source, and the rest of the readiness list.
- [Activate Your License](/getting_started/activate) - apply the key once the activation endpoints are reachable.
- [Sizing](/deployment/sizing) - size the node these rules will carry traffic for.
