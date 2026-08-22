---
title: "System-Wide Proxy Settings"
description: "Operating system-level proxy configuration for SafeSquid SWG affecting all applications across Windows, Linux, and macOS environments"
keywords:
  - SafeSquid system proxy
  - OS-level proxy configuration
  - Windows proxy settings
  - Linux proxy environment
  - macOS proxy configuration
  - universal proxy settings
---

# System-Wide Proxy Settings

## Problem Statement

Organizations require operating system-level proxy configuration to ensure all applications route traffic through SafeSquid without individual application configuration for comprehensive security coverage. Many applications do not respect browser-specific proxy settings, requiring system-wide configuration to ensure complete traffic interception and security enforcement. System-wide proxy settings provide universal application coverage while eliminating the need for application-specific configuration across diverse software environments.

## Key Benefits

**Universal Application Coverage**: System-wide proxy configuration ensures all network applications route traffic through SafeSquid, providing comprehensive security coverage without individual application configuration requirements. This universal approach eliminates security gaps caused by applications that bypass browser-specific proxy settings.

**Simplified Management**: OS-level proxy configuration reduces administrative overhead by eliminating the need to configure proxy settings for each individual application. This centralized approach enables consistent security policy enforcement across all network applications.

**Consistent Security Enforcement**: System-wide proxy settings ensure uniform security policy application across all applications, preventing security bypasses and ensuring comprehensive threat protection and policy enforcement.

## Prerequisites

**Client-Side Preparations**: Ensure administrative privileges are available for system-wide proxy configuration changes. Verify network connectivity between client systems and SafeSquid proxy servers with appropriate firewall rules configured.

**SafeSquid-Side Setup**: Configure SafeSquid proxy services on standard ports with proper authentication and policy configuration. Ensure SSL inspection is enabled if HTTPS traffic requires inspection and monitoring.

**System Requirements**: Client systems must have appropriate operating system versions that support system-wide proxy configuration. Network connectivity must be established between client systems and SafeSquid proxy servers.

## Call to Action

### Windows System-Wide Configuration

#### Internet Options Control Panel

**Configure System Proxy via Internet Options**:
1. Open Control Panel → Internet Options
2. Navigate to Connections tab
3. Click LAN Settings button
4. Enable "Use a proxy server for your LAN"
5. Enter SafeSquid proxy IP and port (e.g., 192.168.1.100:8080)
6. Click Advanced to configure different protocols
7. Configure bypass list for internal domains
8. Click OK to apply settings

**Advanced Proxy Configuration**:
1. In Advanced settings, configure separate proxies for:
   - HTTP: 192.168.1.100:8080
   - HTTPS: 192.168.1.100:8443
   - FTP: 192.168.1.100:8080
   - SOCKS: 192.168.1.100:1080
2. Configure bypass list: *.local; *.company.com; 127.0.0.1

#### Windows Settings (Modern UI)

**Configure Proxy via Windows Settings**:
1. Open Windows Settings (Windows key + I)
2. Navigate to Network & Internet → Proxy
3. Enable "Use a proxy server" toggle
4. Enter proxy address and port
5. Configure bypass list for internal domains
6. Enable "Use proxy server for all protocols"
7. Click Save to apply settings

#### Registry-Based Configuration

**Configure Proxy via Registry**:
1. Open Registry Editor (regedit)
2. Navigate to: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
3. Set ProxyEnable to 1
4. Set ProxyServer to "192.168.1.100:8080"
5. Configure ProxyOverride for bypass list
6. Restart applications to apply changes

**Registry Script Example**:
```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings]
"ProxyEnable"=dword:00000001
"ProxyServer"="192.168.1.100:8080"
"ProxyOverride"="*.local;*.company.com;127.0.0.1"
```

### Linux System-Wide Configuration

#### Network Manager GUI

**Configure Proxy via Network Manager**:
1. Open System Settings → Network
2. Select network connection → Configure
3. Navigate to Proxy tab
4. Select "Manual" proxy configuration
5. Enter HTTP proxy: SafeSquid IP:8080
6. Enter HTTPS proxy: SafeSquid IP:8443
7. Configure bypass list for internal domains
8. Apply settings and restart applications

#### Environment Variables Configuration

**Configure Proxy via Environment Variables**:
1. Edit system profile file: `/etc/environment`
2. Add proxy environment variables:
```bash
http_proxy=http://192.168.1.100:8080
https_proxy=http://192.168.1.100:8443
ftp_proxy=http://192.168.1.100:8080
no_proxy=localhost,127.0.0.1,*.local,*.company.com
```

**Apply Environment Variables**:
```bash
# Source environment variables
source /etc/environment

# Export variables for current session
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8443
export no_proxy=localhost,127.0.0.1,*.local
```

#### APT/YUM Proxy Configuration

**Configure Package Manager Proxy**:
1. Create APT proxy configuration: `/etc/apt/apt.conf.d/95proxies`
2. Add proxy configuration:
```
Acquire::http::Proxy "http://192.168.1.100:8080";
Acquire::https::Proxy "http://192.168.1.100:8443";
```

**YUM Proxy Configuration**:
1. Edit YUM configuration: `/etc/yum.conf`
2. Add proxy settings:
```ini
proxy=http://192.168.1.100:8080
proxy_username=username
proxy_password=password
```

#### System-Wide Profile Configuration

**Configure Proxy in Profile Scripts**:
1. Edit system profile: `/etc/profile`
2. Add proxy environment variables
3. Create proxy configuration script: `/etc/profile.d/proxy.sh`
4. Add proxy settings:
```bash
#!/bin/bash
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8443
export no_proxy=localhost,127.0.0.1,*.local
```

### macOS System-Wide Configuration

#### System Preferences Network Settings

**Configure Proxy via System Preferences**:
1. Open System Preferences → Network
2. Select active network connection
3. Click Advanced → Proxies tab
4. Enable "Web Proxy (HTTP)" and "Secure Web Proxy (HTTPS)"
5. Enter SafeSquid proxy IP address and ports
6. Configure bypass list for internal domains
7. Enable "Exclude simple hostnames"
8. Click OK and Apply to save settings

#### Network Locations Configuration

**Configure Network Locations**:
1. In Network preferences, click Location dropdown
2. Select "Edit Locations"
3. Create new location: "Corporate Proxy"
4. Configure proxy settings for location
5. Switch between locations as needed
6. Apply settings for current location

#### Terminal Proxy Configuration

**Configure Terminal Proxy Settings**:
1. Edit shell profile: `~/.bash_profile` or `~/.zshrc`
2. Add proxy environment variables:
```bash
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8443
export no_proxy=localhost,127.0.0.1,*.local
```

**Apply Terminal Settings**:
```bash
# Source profile
source ~/.bash_profile

# Test proxy connectivity
curl -I --proxy $http_proxy http://safesquid.cfg/
```

## Solution Verification

**System-Wide Application Testing**: Verify all applications (browsers, email clients, development tools) route traffic through SafeSquid proxy without individual configuration.

**Traffic Monitoring**: Monitor SafeSquid logs to confirm all application traffic is being processed through proxy with appropriate policy enforcement.

**Bypass List Verification**: Test internal domain access to ensure bypass list configuration works correctly for internal resources.

**Performance Validation**: Test application performance to ensure system-wide proxy configuration does not significantly impact functionality or user experience.

## Troubleshooting Guide

**Applications Not Using Proxy**: Verify system-wide proxy settings are properly applied and applications are restarted after configuration changes. Check application-specific proxy settings that may override system settings.

**Connection Refused Errors**: Verify SafeSquid proxy service is running and accessible on configured ports. Check firewall rules and network connectivity.

**Authentication Failures**: Confirm SafeSquid authentication settings match system configuration. Verify user credentials and authentication method compatibility.

**SSL Certificate Issues**: Install SafeSquid root CA certificate in system trust store when SSL inspection is enabled. Verify certificate installation and trust settings.

**Environment Variable Issues**: Check environment variable configuration and ensure variables are properly exported and sourced in application environments.

**Network Manager Conflicts**: Verify Network Manager proxy settings do not conflict with manual environment variable configuration. Choose one configuration method consistently.

