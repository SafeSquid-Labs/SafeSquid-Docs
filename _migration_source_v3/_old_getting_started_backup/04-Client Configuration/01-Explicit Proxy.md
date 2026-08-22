---
title: "Explicit Proxy Configuration"
description: Manual proxy configuration for SafeSquid SWG on Windows, Linux, and macOS browsers and systems.
keywords:
  - SafeSquid explicit proxy
  - manual proxy configuration
  - browser proxy setup
  - Windows proxy settings
  - Linux proxy configuration
  - macOS proxy settings
  - Chrome proxy setup
  - Firefox proxy configuration
---

# Explicit Proxy Configuration

## Problem Statement

Organizations require manual proxy configuration for controlled environments where users must configure browsers to route traffic through SafeSquid for policy enforcement and threat protection. Manual configuration provides granular control over proxy usage while enabling comprehensive security monitoring and policy enforcement across diverse browser environments. This explicit configuration approach ensures precise control over proxy behavior while supporting user-specific preferences and organizational security requirements.

## Key Benefits

**Precise Control**: Manual proxy configuration provides exact control over proxy settings, enabling organizations to specify precise proxy servers, ports, and bypass lists for optimal security enforcement. This granular control ensures consistent policy application while allowing customization for specific organizational requirements.

**Comprehensive Coverage**: Explicit proxy configuration supports all major browsers and operating systems, ensuring comprehensive security coverage across diverse endpoint environments. This universal support enables organizations to maintain consistent security policies regardless of user preferences or platform choices.

**Troubleshooting Capability**: Manual configuration provides clear visibility into proxy settings, enabling rapid troubleshooting and verification of proxy connectivity. This transparency facilitates rapid issue resolution while maintaining security enforcement capabilities.

## Prerequisites

**Client-Side Preparations**: Ensure SafeSquid SWG is deployed and accessible from client networks with proper network connectivity and firewall rules configured to allow proxy traffic on required ports. Verify SafeSquid is running and accepting connections on configured proxy ports.

**SafeSquid-Side Setup**: Configure SafeSquid proxy services on appropriate ports (typically 8080 for HTTP, 8443 for HTTPS) with proper authentication and policy configuration. Ensure SSL inspection is enabled if HTTPS traffic requires inspection and monitoring.

**System Requirements**: Client systems must have appropriate browsers installed with administrative privileges for system-wide proxy configuration. Network connectivity must be established between client systems and SafeSquid proxy servers.

## Call to Action

### Windows Browser Configuration

#### Chrome and Edge (System-Wide Configuration)

**Access Windows Proxy Settings**:
1. Open Windows Settings (Windows key + I)
2. Navigate to Network & Internet → Proxy
3. Enable "Use a proxy server" toggle
4. Enter SafeSquid proxy IP address and port (e.g., 192.168.1.100:8080)
5. Configure bypass list for internal domains (e.g., *.local, *.company.com)
6. Click Save to apply settings

**Alternative Method via Internet Options**:
1. Open Control Panel → Internet Options
2. Navigate to Connections tab → LAN Settings
3. Enable "Use a proxy server for your LAN"
4. Enter proxy address and port
5. Configure Advanced settings for different protocols
6. Click OK to apply changes

#### Firefox Browser-Specific Configuration

**Configure Firefox Proxy Settings**:
1. Open Firefox and click menu (three horizontal lines)
2. Navigate to Settings → General
3. Scroll to Network Settings section
4. Click Settings button
5. Select "Manual proxy configuration"
6. Enter HTTP Proxy: SafeSquid IP and port
7. Enable "Use this proxy server for all protocols"
8. Configure No Proxy for internal domains
9. Click OK to save settings

**Verification**: Access http://safesquid.cfg/ to verify SafeSquid interface connectivity.

### Linux Browser Configuration

#### Chrome/Chromium (System-Wide Configuration)

**Configure System Proxy Settings**:
1. Open System Settings → Network
2. Select network connection → Configure
3. Navigate to Proxy tab
4. Select "Manual" proxy configuration
5. Enter HTTP proxy: SafeSquid IP:8080
6. Enter HTTPS proxy: SafeSquid IP:8443
7. Configure bypass list for internal domains
8. Apply settings and restart browser

**Command Line Configuration**:
```bash
# Set environment variables
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8443
export no_proxy=localhost,127.0.0.1,*.local

# Launch Chrome with proxy settings
google-chrome --proxy-server=http://192.168.1.100:8080
```

#### Firefox Browser-Specific Configuration

**Configure Firefox Proxy Settings**:
1. Open Firefox and navigate to Preferences
2. Scroll to Network Settings section
3. Click Settings button
4. Select "Manual proxy configuration"
5. Enter HTTP Proxy: SafeSquid IP and port
6. Enable "Use this proxy server for all protocols"
7. Configure No Proxy for internal domains
8. Click OK to save settings

**Verification**: Test connectivity using curl command:
```bash
curl -I --proxy http://192.168.1.100:8080 http://safesquid.cfg/
```

### macOS Browser Configuration

#### Safari (System Preferences)

**Configure System Proxy Settings**:
1. Open System Preferences → Network
2. Select active network connection
3. Click Advanced → Proxies tab
4. Enable "Web Proxy (HTTP)" and "Secure Web Proxy (HTTPS)"
5. Enter SafeSquid IP address and ports
6. Configure bypass list for internal domains
7. Click OK and Apply to save settings

#### Chrome (System-Wide Configuration)

**Configure Chrome via System Settings**:
1. Open System Preferences → Network
2. Select network connection → Advanced
3. Navigate to Proxies tab
4. Enable HTTP and HTTPS proxy
5. Enter SafeSquid proxy details
6. Configure bypass domains
7. Apply settings and restart Chrome

#### Firefox Browser-Specific Configuration

**Configure Firefox Proxy Settings**:
1. Open Firefox → Preferences
2. Navigate to General → Network Settings
3. Click Settings button
4. Select "Manual proxy configuration"
5. Enter proxy server details
6. Configure protocol settings
7. Set bypass list for internal domains
8. Click OK to save settings

**Verification**: Access SafeSquid interface at http://safesquid.cfg/ to confirm connectivity.

## Solution Verification

**Interface Access Verification**: Successfully access SafeSquid WebGUI at http://safesquid.cfg/ through configured proxy settings, confirming proper proxy connectivity and authentication.

**Traffic Monitoring**: Verify SafeSquid logs show client traffic being processed through proxy with appropriate policy enforcement and security monitoring.

**Bypass List Testing**: Confirm internal domains bypass proxy configuration while external traffic routes through SafeSquid for security enforcement.

**Performance Validation**: Test web browsing performance to ensure proxy configuration does not significantly impact user experience or application functionality.

## Troubleshooting Guide

**Connection Refused Errors**: Verify SafeSquid proxy service is running and accessible on configured ports. Check firewall rules and network connectivity between client and proxy server.

**Authentication Failures**: Confirm SafeSquid authentication settings match client configuration. Verify user credentials and authentication method compatibility.

**SSL Certificate Issues**: Install SafeSquid root CA certificate in browser trust store when SSL inspection is enabled. Verify certificate installation and browser trust settings.

**Bypass List Not Working**: Check bypass list syntax and ensure internal domains are properly configured. Verify DNS resolution for internal domains.

**Browser Not Using Proxy**: Clear browser cache and restart browser after configuration changes. Verify system-wide proxy settings are properly applied.

**Performance Issues**: Check network latency between client and proxy server. Verify SafeSquid performance settings and consider proxy server optimization.

**Related**: [PAC File](02-PAC%20File.md), [System-Wide Proxy](03-System-Wide%20Proxy.md), [Configuration Portal](/docs/SafeSquid%20SWG/Configuration%20Portal), [SSL Inspection](/docs/SSL%20Inspection/main), [Troubleshooting](/docs/Troubleshooting/main)