---
title: Proxy Server Refusing Connections Error
description: "Troubleshoot \"Proxy server refusing connections\" in SafeSquid: service verification, IP/port checks, and browser configuration."
keywords:
  - Proxy server refusing connection
  - SafeSquid not responding
  - SafeSquid monit service
  - troubleshoot proxy errors
  - SafeSquid not listening on port
---



## Issues

1.  I am trying to access the web through the proxy server and suddenly getting the error "Proxy server refusing connections".
1.  When I go to Restart the SafeSquid service from the SafeSquid interface, it displays the error "Proxy server refusing connections".



## Root Causes
1.  SafeSquid Process is not running.
1.  SafeSquid is not listening on the specific IP (or) port, where you configured in the client browsers.
1.  Monit service is not running on SafeSquid Server. (When you restart SafeSquid from the Interface, the monit service will start the SafeSquid service. If the Monit is not running, then SafeSquid is not going to start, till you start the Monit service manually).



## Troubleshooting

1.  Check the status of the monit service whether it is up or down.

```bash
pidof monit
```
If the ouput of the command is empty then run the following command to start the service.

```bash
/etc/init.d/monit start
```
2.  Check the status of SafeSquid Service whether it is up or down.

```bash
pidof safesquid
```
If the monit service is started already, then you will get the SafeSquid process I

3.  Check the listening IP and port of SafeSquid by using the below command

```bash
netstat -tlnp | grep -iE "safesquid"
```
**tcp6 0 0 :::8080 :::* LISTEN 2741/safesquid**

**tcp6 0 0 :::8081 :::* LISTEN 2741/safesquid**

**tcp6 0 0 :::8443 :::* LISTEN 2741/safesquid**

4.  Check the IP configured and Port in your browser and compare it with the above output.

In the above command, SafeSquid listens on all Interfaces present on the server with ports 8080, 8081, and 8443.

