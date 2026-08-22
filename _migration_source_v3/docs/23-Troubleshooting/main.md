---
title: "Troubleshooting"
slug: /Troubleshooting
description: "Comprehensive diagnostic procedures and resolution guides for common SafeSquid proxy issues, connection failures, and configuration problems"
keywords:
  - SafeSquid troubleshooting guide
  - proxy connection issues
  - SafeSquid diagnostic procedures
  - proxy error resolution
  - SafeSquid logs analysis
  - network connectivity issues
  - proxy configuration problems
  - SafeSquid support procedures
---


# Diagnose and resolve SafeSquid proxy issues

When the UI doesn't load, activation fails, or clients can't reach the proxy, use the documents below to diagnose and fix. Each document covers a symptom area: installation, interface access, SSL, authentication, DNS, connectivity, policy, reporting, and advanced diagnostics. Pick the document that matches your symptom.



## Common Configuration Issues

### [Installation issues](/docs/Troubleshooting/Installation_Issues/)
Organizations encounter installation problems during SafeSquid deployment: dependency conflicts, permission issues, and configuration errors prevent successful startup. Installation Issues provides resolution procedures for dependency resolution, permission configuration, and system compatibility. Use this document to resolve common deployment and installation problems.

### [Interface access denied](/docs/Troubleshooting/Interface_Access_Denied/)
Administrators cannot reach SafeSquid's web interface due to authentication failures, network configuration, or permission restrictions. Interface Access Denied provides diagnostic steps for authentication, network connectivity, and permission issues. Follow this document to diagnose and resolve web interface access problems.

### [SSL inspection issues](/docs/Troubleshooting/SSL_Inspection_Issues/)
Organizations encounter SSL inspection problems including certificate errors, handshake failures, and inspection bypass issues that prevent proper SSL traffic analysis and control. SSL Inspection Issues provides diagnostic procedures for SSL-related problems including certificate validation, handshake troubleshooting, and inspection configuration issues. Reference this document to resolve SSL inspection and certificate-related problems.



## Authentication and Directory Service Issues

### [SSO authentication fail](/docs/Troubleshooting/SSO_Authentication_Fail/)
Organizations experience single sign-on authentication failures due to directory service connectivity problems, certificate issues, or configuration errors that prevent user authentication. SSO Authentication Fail provides diagnostic procedures and resolution steps for SSO-related problems including directory service connectivity, certificate validation, and authentication configuration. Follow this document to diagnose and resolve single sign-on authentication issues.

### [Failed to fetch LDAP entries](/docs/Troubleshooting/Failed_To_Fetch_LDAP_Entries/)
Administrators encounter LDAP connectivity problems that prevent user authentication and group membership resolution due to network issues, configuration errors, or directory service problems. Failed To Fetch LDAP Entries provides diagnostic procedures for LDAP-related problems including connectivity troubleshooting, configuration validation, and directory service integration. Reference this document to resolve LDAP connectivity and configuration issues.



## Performance and Resource Issues

### [Disk space and RAM are full](/docs/Troubleshooting/Disk_Space_and_RAM_are_Full/)
Organizations experience performance degradation and system failures due to insufficient disk space or memory resources that prevent proper SafeSquid operation and log generation. Disk Space and RAM are Full provides diagnostic procedures and resolution steps for resource-related problems including disk space management, memory optimization, and log cleanup. Follow this document to diagnose and resolve system resource problems.

### [Not generating performance plot](/docs/Troubleshooting/Not_Generating_Performance_Plot/)
Administrators encounter issues with performance monitoring and reporting when SafeSquid fails to generate performance plots due to configuration problems, resource constraints, or service failures. Not Generating Performance Plot provides diagnostic procedures and resolution steps for performance monitoring issues including configuration validation, service troubleshooting, and resource optimization. Reference this document to resolve performance monitoring and reporting issues.



## Network and Connectivity Issues

### [DNS failure](/docs/Troubleshooting/DNS_Failure/)
Organizations experience DNS resolution problems that prevent web access and proxy functionality due to DNS server issues, network configuration problems, or firewall restrictions. DNS Failure provides diagnostic procedures for DNS-related problems including resolution troubleshooting, server configuration validation, and network connectivity. Follow this document to diagnose and resolve DNS resolution and connectivity issues.

### [Connection failure on websites](/docs/Troubleshooting/Connection_Failure_on_Websites/)
Users encounter website access problems due to proxy configuration issues, network connectivity problems, or policy enforcement that prevents legitimate website access. Connection Failure on Websites provides diagnostic procedures and resolution steps for website access problems including proxy configuration validation, network troubleshooting, and policy review. Reference this document to resolve website access and connectivity problems.

### [Website not accessible](/docs/Troubleshooting/Website_Not_Accessible/)
Organizations experience website accessibility issues due to proxy blocking, network problems, or configuration errors that prevent legitimate website access. Website Not Accessible provides diagnostic procedures for website accessibility problems including proxy policy review, network troubleshooting, and configuration validation. Follow this document to diagnose and resolve website accessibility issues.



## Policy and Configuration Issues

### [Whitelisted website blocked](/docs/Troubleshooting/Whitelisted_Website_Blocked/)
Administrators encounter issues where whitelisted websites remain blocked despite policy configuration, indicating policy enforcement problems or configuration conflicts. Whitelisted Website Blocked provides diagnostic procedures and resolution steps for policy enforcement issues including whitelist configuration validation, policy conflict resolution, and enforcement troubleshooting. Reference this document to resolve whitelist policy enforcement issues.

### [Custom categorization not working](/docs/Troubleshooting/Custom_Categorisation_Not_Working/)
Organizations experience problems with custom website categorization when SafeSquid fails to apply custom category assignments due to configuration issues or policy conflicts. Custom Categorization Not Working provides diagnostic procedures for categorization problems including custom category configuration validation, policy enforcement troubleshooting, and categorization conflict resolution. Follow this document to diagnose and resolve custom categorization issues.

### [SafeSearch not working](/docs/Troubleshooting/SafeSearch_Not_Working/)
Organizations encounter SafeSearch enforcement problems when search engines fail to apply safe search settings due to configuration issues or policy enforcement problems. SafeSearch Not Working provides diagnostic procedures and resolution steps for SafeSearch enforcement issues including configuration validation, policy troubleshooting, and enforcement procedure review. Reference this document to resolve SafeSearch enforcement and configuration issues.

### [Unable to login specific website](/docs/Troubleshooting/Unable_To_Login_Specific_Website/)
Users cannot log in to a specific website through the proxy due to cookie filter, header filter, elevated privacy, or SSL inspection settings. Unable to Login Specific Website provides resolution steps for login failures on sites such as Facebook and Google when access works but authentication fails. Follow this document to diagnose and resolve login failures on specific sites.



## Reporting and Interface Issues

### [Blank report page](/docs/Troubleshooting/Blank_Report_Page/)
Administrators experience reporting interface problems when SafeSquid's reporting module displays blank pages due to configuration issues, service failures, or database problems. Blank Report Page provides diagnostic procedures for reporting interface problems including configuration validation, service troubleshooting, and database connectivity. Follow this document to diagnose and resolve reporting interface and functionality issues.

### [Proxy server refusing connection error](/docs/Troubleshooting/Proxy_Server_Refusing_Connection_Error/)
Users encounter proxy connection refusal errors due to service failures, configuration problems, or resource constraints that prevent proxy functionality. Proxy Server Refusing Connection Error provides diagnostic procedures and resolution steps for connection refusal problems including service troubleshooting, configuration validation, and resource optimization. Reference this document to resolve proxy connection and service availability issues.

### [No tar-ball support](/docs/Troubleshooting/No_Tar-Ball_Support/)
Administrators cannot generate the support tarball from the SafeSquid interface due to script or permission failures. No Tar-Ball Support provides steps to manually run the support tarball script and resolve permission or path issues so diagnostic archives can be produced for support. Follow this document to generate the support tarball when the interface option fails.



## Advanced Diagnostic Tools

### [How to use find_client_id.sh for getting complete connection log](/docs/Troubleshooting/How_to_use_find_client_id.sh_for_getting_complete_connection_log/)
Administrators need advanced diagnostic tools to analyze specific connection issues and obtain detailed logs for troubleshooting complex proxy problems. find_client_id.sh provides connection analysis including detailed log extraction, connection tracing, and diagnostic information for specific client connections. Use this document to obtain detailed connection logs and perform connection analysis for complex troubleshooting.

### [Product failure](/docs/Troubleshooting/Product_Failure/)
Organizations experience complete SafeSquid service failures due to system crashes, configuration corruption, or critical errors that prevent proxy functionality. Product Failure provides emergency diagnostic procedures and recovery steps for complete service failures including system recovery, configuration restoration, and emergency troubleshooting. Follow this document to diagnose and resolve complete SafeSquid service failures and system crashes.

## Next steps

After resolving the issue, verify with [Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/); for configuration changes see [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/).

