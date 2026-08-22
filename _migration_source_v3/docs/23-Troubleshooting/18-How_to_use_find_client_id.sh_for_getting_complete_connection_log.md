---
title: Using find_client_id.sh for Connection Logs
description: Use the find_client_id.sh script to extract complete connection details from SafeSquid logs for troubleshooting and forensic analysis.
keywords:
  - SafeSquid connection logs
  - find_client_id.sh script
  - SafeSquid log analysis
  - proxy troubleshooting tools
  - connection forensics
  - SafeSquid debugging
---


# Get complete connection log with find_client_id.sh

Native logs are written in real time by response; entries for one connection can be scattered. To analyze a single connection from start to finish (profiles, categories, headers, errors), use the client id to pull all log lines for that connection. find_client_id.sh extracts complete connection details for a given client id. Below: how to obtain the client id and run the script.

To use find\_client\_id.sh you are first required to get your connection's client id.

Client id can be extracted from the response headers section in browsers network tab.

(Note: we are assuming that you know how to open developer tools in a browser)

![find_client_id script output or connection log example](/img/picture1.jpg)

Also, client id can be extracted from SafeSquid's native logs

