---
title: "Proxy Server Refusing Connections Error"
description: "Diagnose and resolve SafeSquid proxy server refusing connections error incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "proxy server refusing connection error"]
---

# Proxy Server Refusing Connections Error

Proxy Server Refusing Connections Error can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

## Issues

1. I am trying to access the web through the proxy server and suddenly getting the error "Proxy server refusing connections".
2. When I go to Restart the SafeSquid service from the SafeSquid interface, it displays the error "Proxy server refusing connections".

## Root Causes

1. SafeSquid Process is not running.
2. SafeSquid is not listening on the specific IP (or) port, where you configured in the client browsers.
3. Monit service is not running on SafeSquid Server. (When you restart SafeSquid from the Interface, the monit service will start the SafeSquid service. If the Monit is not running, then SafeSquid is not going to start, till you start the Monit service manually).
4. Check the status of the monit service whether it is up or down.

```text
pidof monit
```

If the ouput of the command is empty then run the following command to start the service.

```text
/etc/init.d/monit start
```

1. Check the status of SafeSquid Service whether it is up or down.

```text
pidof safesquid
```

If the monit service is started already, then you will get the SafeSquid process I

1. Check the listening IP and port of SafeSquid by using the below command

```text
netstat
 
-tlnp
 
|
 
grep
 
-iE
 
"safesquid"
```

_tcp6 0 0 :::8080 ::: LISTEN 2741/safesquid_\*

_tcp6 0 0 :::8081 ::: LISTEN 2741/safesquid_\*

_tcp6 0 0 :::8443 ::: LISTEN 2741/safesquid_\*

1. Check the IP configured and Port in your browser and compare it with the above output.

In the above command, SafeSquid listens on all Interfaces present on the server with ports 8080, 8081, and 8443.

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