---
title: "Runtime Data and Signatures"
description: "SafeSquid SWG temporary files, cache, reporting databases, SSL runtime data, user data, and signature store path reference."
keywords: ["SafeSquid runtime data", "SafeSquid signatures", "SafeSquid report database", "SafeSquid cache"]
---

# Runtime Data and Signatures

Runtime data and signature stores explain what SafeSquid is processing now, what it cached, and which local data supports categorization, content inspection, image analysis, and malware scanning. These files support investigation and capacity review, but they can also contain sensitive traffic or user context.

## Temporary and cache paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/tmp/safesquid` | Stores temporary files created while SafeSquid runs or upgrades. | Upgrade fails, temporary disk use grows, or support requests runtime artifacts. | Temporary files can explain interrupted operations. Review before cleanup during an incident. |
| `/var/cache/safesquid` | Default store for cacheable objects when caching is enabled. | Disk growth, cache behavior, or performance issues. | Cache content can contain requested objects. Treat as sensitive and align cleanup with policy. |

## Database paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/db/safesquid/report` | Stores SQLite reporting database files such as `main.db`, `safesquid2.db`, `main.db-shm`, `main.db-wal`, `safesquid2.db-shm`, `safesquid2.db-wal`, and timestamped `YYYYMMDDhhmmss-main.db` files. | Reports are missing, SIEM results differ from local data, or investigation needs database evidence. | The wiki states a timestamped `YYYYMMDDhhmmss-main.db` file is created after every `1000` transactions. `DB-WAL` files hold pending write-ahead log changes; `DB-SHM` files hold shared memory state. |
| `/var/db/safesquid/ssl` | Stores temporary SSL certificates created for web servers during HTTPS inspection. | HTTPS inspection fails or certificate cache behavior needs review. | Contains generated certificate material. Restrict access and avoid exporting without approval. |
| `/var/db/safesquid/users` | Reserved user database path in the wiki source. | User database behavior needs investigation or support asks for the path. | The wiki does not describe contents. Verify live product behavior before making claims. |

## Signature and library paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/var/lib/safesquid/application_signatures` | Stores the `applications3` file in an `updates` folder. SafeSquid checks and downloads the latest application signature file from the cloud hourly. | Application detection fails or signature update state needs evidence. | Shows local application signature state. Failed hourly updates can reduce application-aware controls. |
| `/var/lib/safesquid/category` | Stores `category.db`, the local database for custom categories. | Custom categories do not match expected policy results. | Contains local category data. Back up before category recovery work. |
| `/var/lib/safesquid/content_signatures` | Stores `magic.mgc`, `libmagic.so`, and an `updates` folder containing `content4`. SafeSquid checks and downloads the latest content signature file hourly. | Content-type detection fails or content inspection results change unexpectedly. | Shows local content signature and library state. Failed updates can weaken content classification. |
| `/var/lib/safesquid/imgfilter` | Stores Image Analyzer libraries such as `libIAImageReaderShared.so`, `libIAEngineShared.so`, and `imgfilter.tune`. SafeSquid checks and downloads the latest library files hourly. | Image Analyzer fails, dependency errors appear, or threshold behavior needs review. | Contains runtime dependencies and tuning for image analysis. Changes affect block decisions. |
| `/var/lib/safesquid/sscore2` | Stores SScore libraries and signatures. SScore signatures are in `parental_sig`; the latest `libbdupdatesdk.so` is downloaded to `update` hourly. | Website categorization fails or SScore update health needs evidence. | Shows categorization support files. Failed updates can reduce classification accuracy. |
| `/var/lib/safesquid/svscan` | Stores SvScan libraries and anti-malware signatures. Anti-malware signatures are in `Plugins`; the latest `libbdupdatesdk.so` is downloaded to `update` hourly. | Malware scanning fails or signature currency needs evidence. | Shows anti-malware update state. Failed updates can weaken malware detection. |

## Evidence handling

Database, cache, SSL, and signature files can contain sensitive operational data. Copy them only for approved troubleshooting or audit work. Preserve timestamps and file ownership when evidence integrity matters.

## Next steps

- Use [Application Binaries and Modules](/safesquid_swg/files_and_folders/application_binaries_and_modules) to confirm the related feature modules exist.
- Use [Reporting Service](/safesquid_swg/interface/reporting_service) to compare local reporting data with centralized evidence.