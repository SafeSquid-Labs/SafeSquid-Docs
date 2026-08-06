---
title: "Files and Folders"
description: "SafeSquid SWG server path reference for service control, policy storage, runtime data, logs, audit evidence, backup, and rollback."
keywords: ["SafeSquid files and folders", "SafeSquid server paths", "SafeSquid audit evidence", "SafeSquid configuration files"]
---

# Files and Folders

SafeSquid server paths are part of the enforcement boundary. They hold service control scripts, module binaries, policy XML, activation material, SSL data, reporting databases, signature stores, runtime files, and logs. Uncontrolled edits can break proxy availability, weaken inspection, erase rollback evidence, or create audit gaps.

Use this section when you need to prove what changed, locate operational evidence, or decide which files need change control before an upgrade or incident response.

## Control the file surface

Treat these paths as production controls, not ordinary local files:

| Path group | Control value | Primary risk |
| --- | --- | --- |
| Service and startup files | Prove how SafeSquid starts, restarts, and tunes the host | Unapproved runtime changes or service outage |
| Binaries and modules | Load SafeSquid features and interface section definitions | Missing modules, mismatched libraries, or unsupported edits |
| Policy and security files | Store activation, policy, SSL, SQLite, and UI assets | Policy drift, certificate exposure, or support risk |
| Runtime data and signatures | Store cache, temporary files, databases, and downloaded signatures | Stale data, failed updates, or lost reporting history |
| Logs and PID state | Preserve audit, forensic, performance, and runtime evidence | Missing incident evidence or incorrect process state |

## Protect sensitive evidence

Activation files, SSL folders, policy XML, reporting databases, and SafeSquid logs contain security-sensitive data. Logs can include user identifiers, source IP addresses, destinations, policy outcomes, browser metadata, and investigation context.

Before exporting or sharing evidence, redact personal data unless an approved audit or incident investigation requires it. Retain copied files according to your organization's evidence-handling policy.

## Use change control

Do not edit SafeSquid-controlled files directly unless a documented procedure requires it. Record the path, owner, reason, backup location, reviewer, and rollback step before changing service scripts, startup parameters, policy XML, SSL material, modules, templates, or log settings.

For policy work, prefer the SafeSquid interface. File-level edits should be reserved for recovery, support-directed remediation, or documented administrative tasks.

## Locate the right path

| Need | Start here |
| --- | --- |
| Verify service controls, startup behavior, TCP tuning, log rotation, Monit, PAM, or kernel tuning | [Service and Startup Files](/safesquid_swg/files_and_folders/service_and_startup_files) |
| Understand binaries, modules, section XMLs, and default startup or setup files | [Application Binaries and Modules](/safesquid_swg/files_and_folders/application_binaries_and_modules) |
| Locate activation, policy, SSL, SQLite, UI, CGI, template, CSS, JS, image, or font files | [Policy, Security, and UI Files](/safesquid_swg/files_and_folders/policy_security_and_ui_files) |
| Review temporary data, cache, report databases, SSL certificate cache, user data, and signature stores | [Runtime Data and Signatures](/safesquid_swg/files_and_folders/runtime_data_and_signatures) |
| Collect config, extended, native, performance, privacy, and process evidence | [Logs and Audit Evidence](/safesquid_swg/files_and_folders/logs_and_audit_evidence) |

## Minimum incident set

For an operational incident, preserve:

1. affected user, source IP, destination, and timestamp
2. matching report entry or SIEM event
3. relevant `extended.log`, `native.log`, `performance.log`, or `config.log` lines
4. recent configuration backup files
5. service state and startup parameters
6. Monit, BIND, and NTP health status
7. SafeSquid process ID from `/var/run/safesquid`

## Next steps

- Use [Logs and Audit Evidence](/safesquid_swg/files_and_folders/logs_and_audit_evidence) to collect proof for investigation and audit.
- Use [Support](/safesquid_swg/policy_management_console/support) to prepare escalation evidence.