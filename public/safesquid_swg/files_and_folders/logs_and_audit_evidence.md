---
title: "Logs and Audit Evidence"
description: "SafeSquid SWG config, extended, native, performance, privacy, and process evidence path reference."
keywords: ["SafeSquid logs", "SafeSquid audit evidence", "SafeSquid extended log", "SafeSquid performance log"]
---

# Logs and Audit Evidence

SafeSquid logs prove who changed policy, what users accessed, which controls matched, and whether the proxy had enough capacity. Preserve these files before remediation. Reboots, rotation, compression, or emergency cleanup can remove the only evidence that explains a security incident.

## Configuration audit logs

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/log/safesquid/config` | Stores `config.log`, which records SafeSquid configuration changes made through the interface. Rotated files are named like `XXXX-config.log`. | Policy dispute, rollback, unauthorized change review, or audit evidence collection. | Shows who changed configuration, from which source, on which page or section, and why. Missing logs weaken change accountability. |

`config.log` records this legend:

```text
"ACCESS_TIME" "SAFESQUID_INTERFACE" "USERNAME@IP" "PAGE" "SECTION" "ACTION" "HTTP_METHOD" "URL" "REFERER" "ARGUMENTS" "CONFIG_FILE" "REASON"
```

## Traffic and policy logs

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/log/safesquid/extended` | Stores `extended.log`, which details users, applications, security breaches, and each request or response processed by SafeSquid. Rotated files are named like `XXXX-extended.log`. | Incident investigation, user activity review, SIEM comparison, or policy verification. | Contains user, destination, policy, profile, category, application, and content-type evidence. Treat as sensitive personal and security data. |

`extended.log` records this legend:

```text
"record_id" "client_id" "request_id" "date_time" "elapsed_time" "status" "size" "upload" "download" "bypassed" "client_ip" "username" "method" "url" "http_referer" "useragent" "mime" "filter_name" "filtering_reason" "interface" "cachecode" "peercode" "peer" "request_host" "request_tld" "referer_host" "referer_tld" "range" "time_profiles" "user_groups" "request_profiles" "application_signatures" "categories" "response_profiles" "upload_content_types" "download_content_types" "profiles"
```

## Native troubleshooting logs

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/log/safesquid/native` | Stores `native.log`, which records functional details for requests, security, redirects, and feature behavior. Rotated files are named like `XXXX-native.log`. | Feature behavior is unclear, request handling needs debugging, or support requests native evidence. | Supports deep troubleshooting. High verbosity can grow quickly and expose detailed traffic context. |

Native log verbosity is controlled by `LOG_LEVEL`:

| Value | Meaning |
| --- | --- |
| `16777216` | Warnings only |
| `33554432` | Errors only |
| `67108864` | Profiles only |
| `134217728` | Debug only |
| `268435455` | All activities and debug information |
| `33554435` | Default: errors, requests, and network |

## Performance evidence

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/log/safesquid/performance` | Stores `performance.log`, which records performance metrics for outages, resource shortfall, internet connectivity failure, and traffic surge analysis. Rotated files are named like `XXXX-performance.log`. | Slow browsing, connection exhaustion, memory pressure, DNS failures, or capacity review. | Provides progressive line-based metrics that can be analyzed with third-party tools such as GNU Plot. Missing data weakens capacity root-cause analysis. |

`performance.log` includes metrics for timestamps, elapsed time, client connections, transactions, thread pools, outbound connection pools, bytes in and out, cache object counts, DNS query reuse and failures, memory, connection deltas, load averages, process counts, and CPU time.

## Privacy and process paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/log/safesquid/privacy` | Privacy log path listed in the wiki source. | Privacy-related logging is enabled or support asks for the path. | The wiki does not describe contents. Verify live product behavior before making definitive claims. |
| `/var/run/safesquid` | Stores `safesquid.pid`, the current SafeSquid process ID. The file changes on every restart. | Service status differs between tools, process restart is disputed, or incident timeline needs confirmation. | Confirms runtime process state. Stale PID data can mislead operations during outage response. |

## Log rotation

SafeSquid log rotation controls large log files. The wiki states SafeSquid rotates logs when they exceed `1GB` and compresses rotated logs with gzip. Before troubleshooting old events, check both active and rotated files.

## Next steps

- Use [Service and Startup Files](/safesquid_swg/files_and_folders/service_and_startup_files) to verify logrotate and startup controls.
- Use [Reports](/safesquid_swg/policy_management_console/reports) to compare log evidence with report views.