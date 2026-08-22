---
title: "Application-Specific Configuration"
description: "Proxy configuration procedures for non-browser applications including email clients, development tools, and command-line utilities with SafeSquid SWG"
keywords:
  - SafeSquid application proxy
  - email client proxy
  - development tools proxy
  - command line proxy
  - Outlook proxy configuration
  - Git proxy settings
---

# Application-Specific Configuration

## Problem Statement

Organizations require specialized proxy configuration for non-browser applications including email clients, development tools, and command-line utilities to ensure comprehensive security coverage across all network applications. Many applications do not respect system-wide proxy settings or browser-specific configurations, requiring individual application configuration to ensure complete traffic interception and security enforcement. Application-specific configuration provides detailed setup procedures for diverse application types while maintaining functionality and performance.

## Key Benefits

**Comprehensive Application Coverage**: Application-specific configuration ensures all network applications route traffic through SafeSquid, providing complete security coverage without relying on system-wide or browser-specific proxy settings. This comprehensive approach eliminates security gaps caused by applications that bypass standard proxy configurations.

**Maintained Application Functionality**: Specialized configuration procedures maintain application functionality while enabling proxy connectivity, ensuring applications continue to operate normally with security enforcement. This approach balances security requirements with application performance and user experience.

**Detailed Implementation Guidance**: Application-specific configuration provides detailed, step-by-step procedures for diverse application types, enabling administrators to configure complex applications with confidence and ensuring consistent security enforcement.

## Prerequisites

**Client-Side Preparations**: Ensure applications are installed and configured with appropriate permissions for proxy configuration changes. Verify network connectivity between applications and SafeSquid proxy servers.

**SafeSquid-Side Setup**: Configure SafeSquid proxy services with appropriate authentication and policy configuration for non-HTTP protocols. Ensure SSL inspection is enabled if HTTPS traffic requires inspection.

**System Requirements**: Client systems must have applications installed with appropriate configuration access. Network connectivity must be established between applications and SafeSquid proxy servers.

## Call to Action

### Email Client Configuration

#### Microsoft Outlook

**Configure Outlook Proxy Settings**:
1. Open Outlook → File → Account Settings
2. Select email account → Change
3. Click More Settings → Connection tab
4. Configure proxy settings:
   - HTTP Proxy: 192.168.1.100:8080
   - HTTPS Proxy: 192.168.1.100:8443
5. Enable "Use proxy authentication"
6. Enter proxy credentials if required
7. Click OK to save settings

**Outlook Advanced Configuration**:
1. Configure separate proxies for different protocols
2. Set bypass list for internal mail servers
3. Configure SSL/TLS settings for secure connections
4. Test email connectivity and proxy functionality

#### Mozilla Thunderbird

**Configure Thunderbird Proxy**:
1. Open Thunderbird → Preferences → General
2. Navigate to Network & Disk Space
3. Click Connection Settings
4. Select "Manual proxy configuration"
5. Configure proxy settings:
   - HTTP Proxy: 192.168.1.100:8080
   - SSL Proxy: 192.168.1.100:8443
6. Configure No Proxy for internal domains
7. Click OK to save settings

#### Evolution (Linux)

**Configure Evolution Proxy**:
1. Open Evolution → Preferences → Mail Accounts
2. Select account → Edit
3. Navigate to Receiving Email → Advanced
4. Configure proxy settings:
   - Proxy Type: HTTP
   - Host: 192.168.1.100
   - Port: 8080
5. Configure authentication if required
6. Test email connectivity

### Development Tools Configuration

#### Git Proxy Configuration

**Configure Git HTTP Proxy**:
```bash
# Configure HTTP proxy for Git
git config --global http.proxy http://192.168.1.100:8080
git config --global https.proxy http://192.168.1.100:8443

# Configure proxy authentication
git config --global http.proxyAuthMethod basic

# Configure bypass for internal repositories
git config --global http.proxy http://192.168.1.100:8080
git config --global http.noProxy "*.local,*.company.com"
```

**Configure Git SSH Proxy**:
```bash
# Configure SSH proxy via ProxyCommand
git config --global core.gitProxy "ssh -o ProxyCommand='nc -X connect -x 192.168.1.100:8080 %h %p'"
```

#### npm/yarn Proxy Configuration

**Configure npm Proxy**:
```bash
# Configure npm proxy settings
npm config set proxy http://192.168.1.100:8080
npm config set https-proxy http://192.168.1.100:8443
npm config set registry https://registry.npmjs.org/

# Configure authentication
npm config set proxy-auth "username:password"
```

**Configure Yarn Proxy**:
```bash
# Configure Yarn proxy settings
yarn config set proxy http://192.168.1.100:8080
yarn config set https-proxy http://192.168.1.100:8443
```

#### Python pip Proxy Configuration

**Configure pip Proxy**:
```bash
# Configure pip proxy via command line
pip install --proxy http://192.168.1.100:8080 package_name

# Configure pip proxy via configuration file
# Create ~/.pip/pip.conf
[global]
proxy = http://192.168.1.100:8080
trusted-host = pypi.org
               files.pythonhosted.org
```

#### Docker Proxy Configuration

**Configure Docker Proxy**:
1. Create Docker daemon configuration: `/etc/docker/daemon.json`
2. Add proxy configuration:
```json
{
  "proxies": {
    "http-proxy": "http://192.168.1.100:8080",
    "https-proxy": "http://192.168.1.100:8443",
    "no-proxy": "localhost,127.0.0.1,*.local"
  }
}
```
3. Restart Docker daemon to apply changes
4. Test Docker proxy functionality

### Command-Line Tools Configuration

#### curl/wget Proxy Configuration

**Configure curl Proxy**:
```bash
# Configure curl proxy via command line
curl --proxy http://192.168.1.100:8080 https://example.com

# Configure curl proxy via environment variables
export http_proxy=http://192.168.1.100:8080
export https_proxy=http://192.168.1.100:8443
curl https://example.com
```

**Configure wget Proxy**:
```bash
# Configure wget proxy via command line
wget --proxy=on --http-proxy=192.168.1.100:8080 https://example.com

# Configure wget proxy via configuration file
# Create ~/.wgetrc
http_proxy = http://192.168.1.100:8080
https_proxy = http://192.168.1.100:8443
use_proxy = on
```

#### SSH Tunneling Through Proxy

**Configure SSH Proxy**:
```bash
# Configure SSH proxy via ProxyCommand
ssh -o ProxyCommand="nc -X connect -x 192.168.1.100:8080 %h %p" user@remote-host

# Configure SSH proxy via configuration file
# Create ~/.ssh/config
Host remote-host
    ProxyCommand nc -X connect -x 192.168.1.100:8080 %h %p
    User username
```

### Office Applications Configuration

#### Microsoft Office Suite

**Configure Office Proxy**:
1. Open Office application → File → Options
2. Navigate to Trust Center → Trust Center Settings
3. Click Privacy Options → Web Options
4. Configure proxy settings:
   - Use system proxy settings
   - Or configure manual proxy settings
5. Test Office connectivity and proxy functionality

**Office Advanced Configuration**:
1. Configure proxy settings for different Office applications
2. Set bypass list for internal Office services
3. Configure SSL/TLS settings for secure connections
4. Test Office functionality with proxy configuration

#### LibreOffice

**Configure LibreOffice Proxy**:
1. Open LibreOffice → Tools → Options
2. Navigate to Internet → Proxy
3. Configure proxy settings:
   - HTTP Proxy: 192.168.1.100:8080
   - HTTPS Proxy: 192.168.1.100:8443
4. Configure No Proxy for internal domains
5. Test LibreOffice connectivity

## Solution Verification

**Application Connectivity Testing**: Verify all configured applications can connect through SafeSquid proxy with proper functionality and performance.

**Traffic Monitoring**: Monitor SafeSquid logs to confirm all application traffic is being processed through proxy with appropriate policy enforcement.

**Functionality Verification**: Test application-specific features to ensure proxy configuration does not impact application functionality or user experience.

**Performance Validation**: Test application performance to ensure proxy configuration does not significantly impact application performance or response times.

## Troubleshooting Guide

**Application Connection Failures**: Verify application-specific proxy settings and ensure applications support proxy configuration. Check application logs for connection errors.

**Authentication Issues**: Confirm SafeSquid authentication settings match application configuration. Verify user credentials and authentication method compatibility.

**SSL/TLS Certificate Problems**: Install SafeSquid root CA certificate in application trust store when SSL inspection is enabled. Verify certificate installation and trust settings.

**Performance Issues**: Check network latency between applications and proxy server. Verify SafeSquid performance settings and consider proxy server optimization.

**Configuration Conflicts**: Ensure application-specific proxy settings do not conflict with system-wide or browser proxy configurations. Choose consistent configuration approach.

**Protocol Compatibility**: Verify SafeSquid supports protocols required by applications. Check proxy server configuration for protocol-specific settings and requirements.

