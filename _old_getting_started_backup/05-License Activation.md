---
title: License Activation
description: Activate SafeSquid Secure Web Gateway instances using activation keys via the WebGUI for enabling subscription features and platform synchronization.
keywords:
  - SafeSquid license activation
  - SafeSquid product activation
  - SafeSquid activation key upload
  - SafeSquid self-service portal
  - SafeSquid WebGUI access
  - SafeSquid SWG license management
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Licensing Overview and Activation Purpose

SafeSquid requires valid licensing to enable full functionality and continuous availability. Two licensing options are available:
- **Free Licensing**: Always free; supports core functionality without time restriction
- **Commercial Licensing**: Includes real-time threat intelligence updates, 365-day disaster recovery and backup, and email-based support

License activation is completed after installation and is essential for activating subscription-based features and ensuring platform synchronization.

Activating multiple SafeSquid instances using the same activation key enables synchronization of SSL certificates and configuration files across nodes.

## Readiness Checklist

### Client-side preparations

- Ensure the SafeSquid server has unrestricted outbound Internet access
- Allow traffic through the firewall to the following endpoints and ports:

**Licensing and Update Services**

| Host                      | Port | Purpose                           |
| ------------------------- | ---- | --------------------------------- |
| api.safesquid.net         | 443  | License activation                |
| swgupdates2.safesquid.net | 443  | Subscription, malware definitions |
| swgupdates.safesquid.net  | 80   | Seqrite updates                   |
| sslupdates.safesquid.com  | 443  | SSL certificate updates           |
| category.safesquid.net    | 443  | Category DB updates               |
| download.quickheal.com    | 80   | Virus signature updates           |

**URL Categorization Engines**

| Host                     | Port | Path                                 |
| ------------------------ | ---- | ------------------------------------ |
| prourl.itsecure.co.in    | 8080 | /URLCategorizerService/URLCategorize |
| encurl.itsecure.co.in    | 8080 | /URLCategorizerService/URLCategorize |
| klassify.itsecure.co.in  | 8080 | /URLCategorizerService/URLCategorize |
| prourl.itonlinesecure.in | 8080 | /URLCategorizerService/URLCategorize |
| encurl.itonlinesecure.in | 8080 | /URLCategorizerService/URLCategorize |

- Validate DNS resolution and establish successful HTTPS connections to each host

### SafeSquid-side setup

- Install and configure the SafeSquid service on the target system

## Activation Procedure

### Upload the activation key 

First, configure browsers or network clients to route HTTP/HTTPS traffic through the SafeSquid proxy.

![uploading the activation key When accessing the interface for the first time, Picture](/img/License_Activation/image13.webp)

![selecting your activation key file and clicking on upload, Picture](/img/License_Activation/image14.webp)

![clicking on restart, Picture](/img/License_Activation/image15.webp)

![waiting for page refresh, Picture](/img/License_Activation/image16.webp)

## Validating Activation Success

1. Open a browser and go to: [**http://Safesquid.cfg/**](http://Safesquid.cfg/)

2. Access the **Support** section from the menu.

![clicking on support to validate product activation, Picture](/img/License_Activation/image17.webp)

1. Confirm the **Activation Details** section is populated.

![showing activation details in license details, Picture](/img/License_Activation/image18.webp)

If these fields are present and valid, the license activation is confirmed.

## Solution Verification

- **Interface Checks**: Support → Activation Details shows product type, expiry (if applicable), and subscription status. Screenshot above (image17, image18) confirms the section.
- **Log Analysis**: After activation, SafeSquid logs should show successful contact with licensing endpoints; failures appear as connection or subscription errors.
- **Performance Validation**: Threat and category updates should run; [Reporting](/docs/Audit%20&%20Forensics/Reporting%20Module) and other subscription features are available.

**Related**: [Registration](/docs/Getting%20Started/Registration), [Deployment Planning](/docs/Getting%20Started/Deployment%20Planning), [Installation Guide](/docs/Getting%20Started/Installation%20Guide/main), [Client Configuration](/docs/Getting%20Started/Client%20Configuration/main), [Troubleshooting](/docs/Troubleshooting/main)

## **Troubleshooting Activation Failures**

<Tabs>
  <TabItem value="Case 1" label="Case 1" default>
    **Case 1: Activation Key Not Detected By [http://safesquid.cfg/](http://safesquid.cfg/)**

    **Symptoms:** After uploading the activation key, the SafeSquid UI displays "Failed to set Subscription details."

    **Root Cause:** The activation key file is either missing or improperly named.

    **Resolution:**

    1. Verify the presence of the activation key file:

    ```bash
    ls -lrt /usr/local/safesquid/security/
    ```

    Ensure a file named activation\_key exists.

    2. If absent or misnamed, re-upload the correct activation key file.

    3. Restart the SafeSquid service:

    ```bash
    /etc/init.d/safesquid stop
    ```

    ```bash
    /etc/init.d/safesquid start
    ```
  </TabItem>

  <TabItem value="Case 2" label="Case 2" default>
    **Case 2: Subscription Server Unreachable**

    **Symptoms:** Post activation key upload, the browser shows "proxy server refusing connections."

    **Root Cause:** SafeSquid cannot connect to the subscription server due to network issues.

    **Resolution:**

    1. Test connectivity to the subscription server:

    ```bash
    ping swgupdates2.safesquid.net
    ```

    ```bash
    nslookup swgupdates2.safesquid.net
    ```

    Ensure the server responds and DNS resolution is successful.

    2. If connectivity fails, check firewall settings and network configurations to allow access to the required hosts and ports.

    3. After resolving network issues, restart the SafeSquid service:

    ```bash
    /etc/init.d/safesquid start
    ```
  </TabItem>

  <TabItem value="Case 3" label="Case 3" default>
    **Case 3: Improper Service Restart**

    **Symptoms:**

    - Even after uploading the activation key, subscription details remain unset

    - The browser indicates the proxy server is refusing connections

    **Root Cause:** SafeSquid service was not restarted correctly after activation key upload.

    **Resolution:**

    1. Ensure the monit service is configured properly to manage SafeSquid.

    2. If monit is not set up, manually restart the SafeSquid service:

    ```bash
    /etc/init.d/safesquid stop**
    ```

    ```bash
    /etc/init.d/safesquid start**
    ```
  </TabItem>
</Tabs>
