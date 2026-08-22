---
title: Proxy Chain
description: Deploy SafeSquid behind a parent proxy with proxy chaining, HTTPS inspection, and request forwarding for enterprise integration.
keywords:
  - Deploy SafeSquid behind proxy
  - SafeSquid proxy chaining
  - Configure parent-child proxy
  - SafeSquid forwarding proxy setup
  - SafeSquid behind corporate firewall
---


# Forward client traffic through a parent proxy

Use SafeSquid as a child proxy in front of a corporate (parent) proxy. A simple configuration in SafeSquid forwards all client requests to the parent proxy. SafeSquid can still perform HTTPS inspection and policy enforcement before forwarding; the parent handles upstream connectivity and any corporate policy.

Traffic flows from the client through the child SafeSquid to the parent proxy, then to the internet:

```mermaid
flowchart LR
    Client[Client browser]
    Child[Child SafeSquid]
    Parent[Parent proxy]
    Internet[Internet]
    Client --> Child
    Child --> Parent
    Parent --> Internet
```

Example scenarios:

![Proxy chain scenario: client, child proxy, and parent proxy network layout](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image1.webp)

Here am using two proxy servers as SafeSquid only

My client (Browser)## 's network IP - 192.168.0.27

My Child Proxy## 's network IP - 192.168.27.50 (with no direct internet Access)

My Parent Proxy## 's network IP - 192.168.27.100

**Configuration on child proxy:**

1. Deploy SafeSquid proxy
2. Enabling SSL inspection in SafeSquid
3. Downloading ROOT CA certificate from SafeSquid
4. Deploy certificate in client browsers.
5. Enable forwarding to parent proxy using forwarding section

**Configuration on Parent proxy:**

Deploy SafeSquid, it is up and running, no extra configuration required in parent proxy



## Prerequisites
Enable HTTPS inspection on child proxy (optionally on parent proxy also). Check our document to configure HTTPS inspection on SafeSquid - [How to configure HTTPS inspection](/docs/SSL_Inspection/main/)

Import SafeSquid child proxy ROOT CA in client browser

Note: No configuration required on Parent Proxy server. Just deploy the parent proxy and make sure that it is up and running.



## Configure proxy chain in SafeSquid

Access the [SafeSquid Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/).

### Open Configure page

![Configure page in SafeSquid interface](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image2.webp)

### Open Application Setup → Proxy chain

![Application Setup section in sidebar](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image3.webp)

![Proxy chain section in Application Setup](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image4.webp)

### Enable Global section
![Enable Global section for proxy chain](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image5.webp)

![Global proxy chain toggle and options](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image6.webp)

![Saving Global proxy chain configuration](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image7.webp)

### Open Forwarding proxies and add an entry

![Forwarding proxies section](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image8.webp)
![Add new forwarding proxy entry](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image9.webp)

![Forwarding proxy form with comment field](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image10.webp)

![Entering parent proxy host or IP](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image11.webp)

![Forwarding proxy entry with IP 192.168.27.100](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image12.webp)

In the example: my upstream proxy ip: 192.168.27.100

![Entering parent proxy port](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image13.webp)

![Forwarding proxy port 8080 configured](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image14.webp)

In example: my upstream proxy listening on port 8080

![Submit forwarding proxy entry](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image15.webp)

![Forwarding proxy list with new entry](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image16.webp)

![Save configuration button](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image17.webp)

![Save conf confirmation](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image18.webp)

![Configuration saved successfully](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image19.webp)

### Test proxy chain connectivity

![Testing proxy chain connectivity](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image20.webp)

![Proxy chain test result or log](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image21.webp)

![Verifying traffic through parent proxy](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image22.webp)

### Save configuration

![Save configuration to apply proxy chain settings](/img/How_To/Deploy_SafeSquid_Behind_Corporate_Proxy/image23.webp)

When the administrator clicks Save config, a prompt asks for confirmation to store the configuration in the cloud.

Select Yes only in below cases:

to reuse this configuration in other SafeSquid instances.

if the total configuration in all sections is completed and validated.

Otherwise select No and click on submit.



## Verification and Evidence

- **Interface Checks**: In [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), open Application Setup → Proxy chain. Confirm Global is enabled and the forwarding proxy entry shows the correct parent IP and port.
- **Log Analysis**: Check SafeSquid access logs for requests showing the parent proxy as upstream; connection failures to the parent appear in logs with connect errors.
- **Performance Validation**: From a client behind the child proxy, browse an external site; traffic should succeed and appear in both child and parent proxy logs.



## Next steps

- [Forward Proxy](/docs/Operational_Modes/Forward_Proxy/) for explicit proxy without chaining.
- [SSL Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) for HTTPS inspection on the child proxy.
- [Troubleshooting](/docs/Troubleshooting/main/) if connectivity or parent proxy errors occur.

