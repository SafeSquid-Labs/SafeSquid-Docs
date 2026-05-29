---
title: Policy, Security, and UI Files
description: SafeSquid SWG activation, policy, SSL, SQLite, user interface, CGI, template, CSS, JavaScript, image, and font path reference.
keywords:
  - SafeSquid policy files
  - SafeSquid SSL files
  - SafeSquid activation files
  - SafeSquid UI files
---

# Policy, Security, and UI Files

Policy, security, and interface files define who can use SafeSquid, which controls apply, how SSL material is stored, and how the management interface renders. Treat these paths as sensitive. Unreviewed edits can stop the service, expose certificates, break policy rollback, or make support evidence unreliable.

## Product-owned root

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/usr/local/safesquid` | Contains `security`, `ui_root`, `sqlite`, and `bin` subdirectories for activation, user interface rendering, SQLite database configuration, SSL certificates, and scripts. | Building a server inventory, preparing support evidence, or confirming product-owned paths. | Shows the local SafeSquid application data root. Apply least privilege and backup controls. |
| `/usr/local/safesquid/bin` | Stores scripts that can run through the External Applications section. User-created scripts belong here when execution is required. | External application integrations fail or script execution needs review. | Shows executable extension points. Treat scripts as privileged automation and review them before deployment. |

## Security and policy paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/usr/local/safesquid/security` | Contains `policies`, `ssl`, and `dns` subdirectories plus activation files such as `activation_key`, `activation_key.updates`, and `activation_key.updates.backup`. | Activation fails, service stops unexpectedly, or license state needs evidence. | Activation files are service-critical. The wiki warns they should never be deleted because SafeSquid can stop. |
| `/usr/local/safesquid/security/policies` | Stores policy XML. The wiki identifies `default.config.xml`, current `config.xml`, and timestamped backup files named like `config_XXXX@YYYY_ZZZZ.xml`. | Policy rollback, audit review, change dispute, or configuration recovery. | `config.xml` is the latest saved configuration. Backup files preserve prior saves by username, IP address, and modification time. Treat all policy XML as sensitive. |
| `/usr/local/safesquid/security/ssl/` | Stores SSL root certificates, trusted bundle files, and `subca` material used in OpenVPN configuration. | HTTPS inspection issues, certificate trust review, or incident evidence collection. | Contains certificate material. Restrict access, back up securely, and avoid casual copying. |
| `/usr/local/safesquid/sqlite` | Stores SQLite configuration files: `users.db.conf`, `reporting_db.conf`, and `bypass_db.conf`. | Reporting, user database, or bypass database behavior needs investigation. | Shows database configuration. Incorrect edits can affect user, reporting, or bypass behavior. |

## Interface and template paths

| Path | Purpose | Inspect when | Evidence and risk |
| --- | --- | --- | --- |
| `/usr/local/safesquid/ui_root/` | Root for files used to render the SafeSquid web user interface. | Interface rendering breaks or support asks for UI file evidence. | Product-owned interface surface. Customization can affect supportability. |
| `/usr/local/safesquid/ui_root/cgi-bin` | Stores scripts for defined functions such as support tarball generation, performance plot generation, and Kerberos setup. | Support bundle generation fails, performance plots fail, or Kerberos setup scripts need review. | Contains executable UI-backed functionality. Review changes as privileged code. |
| `/usr/local/safesquid/ui_root/css` | Stores CSS files that define interface display. | Interface layout breaks after change or upgrade. | Unsupported edits can disrupt the management interface. Use change control for any customization. |
| `/usr/local/safesquid/ui_root/fonts` | Stores web font files, including `glyphicons-halflings-regular.*`, `fontawesome-webfont.*`, and `hinted-SegoeUI.*`. | Icons or fonts fail to render in the interface. | Evidence for UI rendering dependencies. Avoid edits unless support directs them. |
| `/usr/local/safesquid/ui_root/img` | Stores image files shown in the SafeSquid interface, including PNG and GIF assets. | Interface images fail to load or branding changes need review. | Custom image changes can require related CSS or JavaScript changes. Treat as support-sensitive. |
| `/usr/local/safesquid/ui_root/js` | Stores JavaScript files used by the SafeSquid interface. | Interface actions fail or browser errors appear. | JavaScript changes can break administration workflows. Avoid manual edits without review. |
| `/usr/local/safesquid/ui_root/templates` | Stores templates and scripts such as `upgrade.sh`, `success.html`, `landing.html`, and `block_bypass.html`. | Block pages, captive portal pages, login success pages, or upgrades fail. | Templates affect user-facing security decisions and upgrade behavior. Test and review all changes. |

## Rollback guidance

Before changing policy, SSL, activation, UI, or script paths, preserve the original files and record owner, timestamp, reason, and rollback path. For policy rollback, use timestamped `config_XXXX@YYYY_ZZZZ.xml` files only after confirming the correct user, source IP, and modification time.

## Next steps

- Use [Logs and Audit Evidence](/safesquid_swg/files_and_folders/logs_and_audit_evidence) to correlate policy changes with `config.log`.
- Use [Configure](/safesquid_swg/policy_management_console/configure) for normal policy administration.
