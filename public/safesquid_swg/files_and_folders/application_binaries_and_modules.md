---
title: "Application Binaries and Modules"
description: "SafeSquid SWG binary, module, feature library, section XML, and default startup file path reference."
keywords: ["SafeSquid modules", "SafeSquid binaries", "SafeSquid startup.ini", "SafeSquid setup.ini"]
---

# Application Binaries and Modules

SafeSquid binaries and modules load the enforcement engine and optional feature capabilities. Treat these paths as product-owned. Removing, replacing, or manually modifying files can disable controls, break the interface, or create unsupported runtime behavior.

## Core binary paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/opt/safesquid/bin/safesquid` | SafeSquid executable link for the running SafeSquid version. | Service fails to start, upgrade verification, or binary integrity review. | Proves which runtime binary the service uses. The wiki warns that deleting this file stops SafeSquid from working. |
| `/opt/safesquid/bin/sections` | Stores SafeSquid feature XML files, except add-on module XMLs. SafeSquid uses these XML files to render the user interface. | Interface sections are missing, feature pages fail to render, or support asks for UI structure evidence. | Shows product section definitions. Manual edits can break management interface rendering. |
| `/opt/safesquid/default` | Stores default `startup.ini` and `setup.ini`. | Startup parameter review, setup parameter recovery, or upgrade comparison. | Keep default files unchanged. Modified startup parameters belong in `/opt/safesquid/startup.ini`; manual setup changes require a copied `/opt/safesquid/setup.ini`. |

## Module root

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/opt/safesquid/bin/modules` | Stores add-on modules loaded when SafeSquid starts. Modules include shared objects and XML files. | Feature fails to load, startup errors mention modules, or support asks for module inventory. | Confirms which add-on capability files exist. Mismatched files can disable features or prevent clean startup. |

## Feature module paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/opt/safesquid/bin/modules/dlp` | Stores DLP module shared objects and XML. DLP detects and blocks potential data exfiltration. | Upload control fails, DLP policies do not apply, or module inventory is required. | Supports evidence that the DLP module is present. Missing files can remove data-loss controls. |
| `/opt/safesquid/bin/modules/elevated` | Stores Elevated Privacy module files. This feature can block third-party cookies and hide referer and user-agent details according to privacy level. | Privacy controls fail or policy behavior differs from expectation. | Shows whether Elevated Privacy module files are installed. Changes can affect privacy enforcement. |
| `/opt/safesquid/bin/modules/icap` | Stores ICAP module files. ICAP enables request or response modification through an ICAP server. | ICAP integration fails, external content filtering breaks, or request modification is not applied. | Confirms ICAP module presence. Incorrect changes can disrupt external scanning or transformation workflows. |
| `/opt/safesquid/bin/modules/imgfilter` | Stores Image Analyzer module files. The wiki states it can block suspicious images and is typically `80%-90%` accurate, depending on configuration. | Image filtering does not trigger or support asks for module state. | Shows installed image analysis files. Treat accuracy as configurable, not absolute. |
| `/opt/safesquid/bin/modules/imgfilter/imgfilter` | Stores Image Analyzer dependency libraries such as `libIAImageReaderShared.so.*`, `libIAEngineShared.so.*`, and `imgfilter.tune`. | Image Analyzer loads but scoring or dependencies fail. | Contains engine, reader, and threshold tuning files. Changes can alter image block behavior. |
| `/opt/safesquid/bin/modules/rewrite` | Stores Content Re-Write module files. The feature uses regular expressions to modify pages, files, client headers, or server headers in real time. | Rewrite policy behaves unexpectedly or high-risk content modification is under review. | High-risk control surface. Use change control because incorrect expressions can alter trusted content before delivery. |
| `/opt/safesquid/bin/modules/sscore` | Stores SScore module files. SScore queries SafeSquid Content Categorisation Service to classify websites. | Category decisions fail or classification evidence is needed. | Confirms website categorization module files. Missing files can reduce category-based enforcement. |
| `/opt/safesquid/bin/modules/svscan` | Stores SvScan module files. SvScan is a high-speed in-memory malware scanner with signature database support. | Malware scanning fails or signature-dependent behavior needs proof. | Confirms anti-malware module files. Missing files can weaken malware protection. |
| `/opt/safesquid/bin/modules/wccp` | Stores WCCP module files. WCCP redirects traffic from WCCP-enabled routers to SafeSquid for transparent proxying. | Transparent redirection fails, router integration changes, or failover is reviewed. | Confirms WCCP support files. Misconfiguration can bypass proxy enforcement or affect routing. |

## Change-control guidance

Do not manually replace module files during normal administration. Use supported package, upgrade, or support-directed procedures. Capture directory listings before and after upgrades so reviewers can explain changed capabilities.

## Next steps

- Use [Runtime Data and Signatures](/safesquid_swg/files_and_folders/runtime_data_and_signatures) to review downloaded signature and library stores.
- Use [Proxy Service](/safesquid_swg/application_ecosystem/proxy_service) to understand how service startup affects enforcement.