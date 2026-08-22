---
title: "PAC File Configuration"
description: "Client-side Proxy Auto-Configuration (PAC) file setup and deployment for automated SafeSquid proxy selection across browsers and operating systems"
keywords:
  - SafeSquid PAC file
  - proxy auto-configuration
  - automatic proxy selection
  - PAC file deployment
  - WPAD configuration
  - browser PAC setup
---

# PAC File Configuration

## Problem Statement

Organizations require automated proxy configuration to reduce deployment complexity and enable dynamic traffic routing without manual browser configuration for each endpoint. Manual proxy configuration becomes impractical in large-scale deployments where hundreds or thousands of endpoints need consistent proxy settings with intelligent routing capabilities. PAC files provide automated proxy selection through JavaScript-based configuration, enabling sophisticated routing logic, load balancing, and failover capabilities across proxy clusters.

## Key Benefits

**Automated Deployment**: PAC files eliminate manual browser configuration requirements, enabling rapid deployment across large-scale environments with minimal administrative overhead. This automation reduces deployment time and configuration errors while ensuring consistent proxy settings across all endpoints.

**Intelligent Routing**: PAC files enable sophisticated routing logic based on destination URLs, user groups, time-based policies, and network conditions. This intelligence allows organizations to implement complex routing strategies including load balancing, failover, and conditional proxy selection.

**Centralized Management**: PAC files enable centralized configuration management with automatic updates and rollback capabilities. Changes to proxy configuration can be deployed instantly across all endpoints without individual browser reconfiguration.

## Prerequisites

**Client-Side Preparations**: Ensure browsers support PAC file functionality and have appropriate network connectivity to access PAC file hosting location. Verify DNS resolution for PAC file server and test HTTP access to PAC file URL.

**SafeSquid-Side Setup**: Configure SafeSquid proxy servers with appropriate load balancing and failover capabilities. Ensure PAC file hosting server is accessible and PAC file content is properly formatted JavaScript.

**System Requirements**: Client systems must have browsers that support PAC file functionality (Chrome, Firefox, Safari, Edge). Network connectivity must allow access to PAC file hosting server and SafeSquid proxy servers.

## Call to Action

### PAC File Overview

**What is a PAC File**: Proxy Auto-Configuration (PAC) files are JavaScript-based configuration files that browsers use to automatically determine which proxy server to use for specific URLs. PAC files contain JavaScript functions that evaluate destination URLs and return appropriate proxy server information.

**PAC File Benefits**: PAC files provide automated proxy selection, load balancing across multiple proxy servers, failover capabilities, and conditional routing based on URL patterns, user groups, or network conditions.

### PAC File Configuration Methods

#### HTTP Server Hosting (Recommended)

**Deploy PAC File on Web Server**:
1. Create PAC file with JavaScript proxy configuration
2. Host PAC file on internal web server (e.g., IIS, Apache, Nginx)
3. Ensure PAC file is accessible via HTTP/HTTPS
4. Configure browsers to use PAC file URL
5. Test PAC file functionality and proxy selection

**Example PAC File Content**:
```javascript
function FindProxyForURL(url, host) {
    // Direct connection for internal domains
    if (isInNet(host, "192.168.0.0", "255.255.0.0") ||
        isInNet(host, "10.0.0.0", "255.0.0.0") ||
        host == "localhost") {
        return "DIRECT";
    }

    // Use SafeSquid proxy for external traffic
    return "PROXY 192.168.1.100:8080; PROXY 192.168.1.101:8080";
}
```

#### File Protocol Hosting

**Local PAC File Deployment**:
1. Create PAC file with proxy configuration
2. Place PAC file in accessible local directory
3. Configure browsers to use file:// protocol path
4. Ensure file permissions allow browser access
5. Test PAC file functionality

**File Path Example**: `file:///C:/PAC/proxy.pac`

### Browser-Specific PAC Configuration

#### Windows Configuration

**Chrome PAC Configuration**:
1. Open Chrome Settings → Advanced → System
2. Click "Open proxy settings"
3. Enable "Use automatic proxy configuration"
4. Enter PAC file URL: `http://pac-server.company.com/proxy.pac`
5. Click OK to apply settings

**Firefox PAC Configuration**:
1. Open Firefox → Settings → General
2. Scroll to Network Settings → Settings
3. Select "Automatic proxy configuration URL"
4. Enter PAC file URL
5. Click OK to save settings

**Internet Explorer/Edge Legacy**:
1. Open Internet Options → Connections tab
2. Click LAN Settings
3. Enable "Use automatic configuration script"
4. Enter PAC file URL
5. Click OK to apply settings

#### Linux Configuration

**Chrome PAC Configuration**:
1. Open Chrome Settings → Advanced → System
2. Click "Open proxy settings"
3. Configure automatic proxy configuration URL
4. Enter PAC file URL
5. Apply settings and restart browser

**Firefox PAC Configuration**:
1. Open Firefox → Preferences → General
2. Navigate to Network Settings
3. Select "Automatic proxy configuration URL"
4. Enter PAC file URL
5. Click OK to save settings

**System-Wide PAC Configuration**:
```bash
# Set PAC file URL via environment variable
export PAC_URL="http://pac-server.company.com/proxy.pac"

# Configure via Network Manager
nmcli connection modify "connection-name" proxy.pac-url "$PAC_URL"
```

#### macOS Configuration

**Safari PAC Configuration**:
1. Open System Preferences → Network
2. Select network connection → Advanced
3. Navigate to Proxies tab
4. Enable "Automatic Proxy Configuration"
5. Enter PAC file URL
6. Click OK and Apply

**Chrome PAC Configuration**:
1. Open Chrome → Preferences → Advanced
2. Navigate to System section
3. Click "Open proxy settings"
4. Configure automatic proxy configuration
5. Enter PAC file URL

**Firefox PAC Configuration**:
1. Open Firefox → Preferences → General
2. Navigate to Network Settings
3. Select "Automatic proxy configuration URL"
4. Enter PAC file URL
5. Click OK to save settings

### WPAD (Web Proxy Auto-Discovery)

**WPAD Configuration Overview**: Web Proxy Auto-Discovery enables automatic PAC file discovery without manual URL configuration. WPAD uses DNS and DHCP to automatically locate PAC files on the network.

**WPAD Requirements**:
1. Configure DNS server with WPAD record
2. Host PAC file as `wpad.dat` on web server
3. Ensure DHCP provides WPAD configuration
4. Configure browsers to use automatic proxy discovery

**WPAD DNS Configuration**:
```
# Add DNS record for WPAD
wpad.company.com. IN A 192.168.1.10
```

## Solution Verification

**PAC File Loading Verification**: Check browser developer tools or proxy settings to confirm PAC file is loading correctly and proxy selection is working as expected.

**Traffic Routing Verification**: Monitor SafeSquid logs to verify traffic is being routed according to PAC file logic with appropriate load balancing and failover behavior.

**Bypass List Testing**: Confirm internal domains bypass proxy configuration while external traffic routes through SafeSquid according to PAC file rules.

**Load Balancing Verification**: Test multiple proxy servers to ensure PAC file load balancing is functioning correctly with proper failover capabilities.

## Troubleshooting Guide

**PAC File Not Loading**: Verify PAC file URL is accessible and returns valid JavaScript content. Check browser console for JavaScript errors in PAC file execution.

**Proxy Selection Errors**: Review PAC file JavaScript syntax and logic. Test PAC file functions using browser developer tools or PAC file testing utilities.

**Network Connectivity Issues**: Ensure PAC file server is accessible and SafeSquid proxy servers are reachable from client networks.

**Browser Compatibility**: Verify browser supports PAC file functionality and JavaScript execution. Test with different browsers to identify compatibility issues.

**DNS Resolution Problems**: Check DNS resolution for PAC file server and proxy servers. Verify internal DNS configuration and external DNS resolution.

**Performance Issues**: Monitor PAC file execution time and optimize JavaScript logic for faster proxy selection. Consider caching PAC file content for improved performance.