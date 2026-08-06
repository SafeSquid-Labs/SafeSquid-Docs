---
title: "Whitelisted Websites Blocked"
description: "Diagnose and resolve SafeSquid whitelisted websites blocked incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "whitelisted website blocked"]
---

# Whitelisted Websites Blocked

Whitelisted Websites Blocked can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Whitelisted sites still blocked

Company policy blocks the social network category for all employees, but a few social networking sites must be whitelisted. Those sites are added to the whitelist category yet still show a block template. Similarly, after whitelisting the corporate website, employees may still be unable to access it.

| Symptom | Likely cause | Resolution | Verification |
| --- | --- | --- | --- |
| Whitelisted site still shows block template | Site not in whitelist category; policy order wrong; policy disabled | Add site to whitelist in Categorize Web-sites ; enable default whitelist policy and place above GLOBAL BLOCK | Open site from client; page loads without block |
| Corporate site blocked after whitelist | sscore/categorization not loaded or category not applied | Enable sscore ; add site to whitelist category; ensure policy enabled and above block | Check Categorize Web-sites for site category; retest access |

Note: Whitelist category is the category to allow. Blacklist category is the category to block.

## Enable sscore and add site to whitelist category

Ensure the **sscore** section is enabled and the categorization engine is loaded. Verify from the SafeSquid Statistics page in the interface. See [the Reporting Module](/use_cases/audit_and_forensics/reporting_module). Add the corporate website to the whitelist category from Custom Settings -\> Categorize Web-sites in the SafeSquid UI.

## Procedure

1. [Access the SafeSquid interface](/safesquid_swg/interface/configuration_portal)
2. Go to configure page

![click on configure in SafeSquid Interface](/images/troubleshooting/whitelisted_website_blocked_01_click_on_configure_in_safesquid_interface.webp)

1. Go to the **Categorize Web-sites section under Custom Settings** and search website/domain from the **search for category** option.
2. Modify that website with a whitelist category. (A whitelist is a custom category that is made to allow blocked websites)

![Go to categorize web-sites under custom settings section](/images/troubleshooting/whitelisted_website_blocked_02_go_to_categorize_web_sites_under_custom_settings.webp)

![enter the website to be whitelisted and click search](/images/troubleshooting/whitelisted_website_blocked_03_enter_the_website_to_be_whitelisted_and_click_se.webp)

![Whitelisted website blocked troubleshooting step or policy edit](/images/troubleshooting/whitelisted_website_blocked_04_whitelisted_website_blocked_troubleshooting_step.webp)

![Modify that website with whitelist category](/images/troubleshooting/whitelisted_website_blocked_05_modify_that_website_with_whitelist_category.webp)

![click on Modify](/images/troubleshooting/whitelisted_website_blocked_06_click_on_modify.webp)

![success message of adding category to the category server](/images/troubleshooting/whitelisted_website_blocked_07_success_message_of_adding_category_to_the_catego.webp)

1. Go to Access profiles for default policy and verify whether the policy is enabled or not. (Make it enabled)

![Showing the category "whitelist"](/images/troubleshooting/whitelisted_website_blocked_08_showing_the_category_whitelist.webp)

![Showing the unique name given to the default policy](/images/troubleshooting/whitelisted_website_blocked_09_showing_the_unique_name_given_to_the_default_pol.webp)

![Making sure this policy is above GLOBAL BLOCK policy and saving it](/images/troubleshooting/whitelisted_website_blocked_10_making_sure_this_policy_is_above_global_block_po.webp)

Use Categorize websites to Create and add websites to the "whitelist category".

## Verification and Evidence

- **Interface Checks**: In [Configuration Portal](/safesquid_swg/interface/configuration_portal), Custom Settings -\> Categorize Web-sites: site shows whitelist category. Restriction Policies -\> Access profiles: default whitelist policy is enabled and above GLOBAL BLOCK.
- **Log Analysis**: Access logs show allowed response for the whitelisted URL; no block template or category block for that domain.
- **Performance Validation**: From a client, open the whitelisted site; page loads without block template.

**Related**: [Web Categorization](/use_cases/access_restriction/web_categorization), [Access Restriction](/use_cases/access_restriction/access_restriction), [Reporting](/use_cases/audit_and_forensics/reporting_module), [Troubleshooting](/troubleshooting/main)

## Capture useful evidence

Collect evidence before restarting services or changing policy. Keep screenshots, command output, and relevant SafeSquid logs with the incident ticket.

```sh
tail -100 /var/log/safesquid/safesquid.log
tail -100 /var/log/syslog
```

Record the affected user, source IP address, requested URL, timestamp, browser error, SafeSquid policy section changed, and verification result.

## Next steps

- Use [Find a complete connection log](/troubleshooting/how_to_use_find_client_id_sh_for_getting_complete_connection_log) to trace a specific client transaction.
- Use [Troubleshooting](/troubleshooting/troubleshooting) for the broader diagnostic checklist.