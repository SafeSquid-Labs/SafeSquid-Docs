---
title: Monit
description: Install, configure, and verify Monit for SafeSquid to auto-monitor and restart the proxy service.
keywords:
  - monit SafeSquid setup
  - SafeSquid monit service
  - monit auto restart SafeSquid
  - SafeSquid monitoring daemon
  - SafeSquid high availability
  - monit startup configuration
---



## Installation and configuration of Monit Service
**Monit** will automatically get installed when you install **SafeSquid Appliance Builder (SAB)** to set up your secure web gateway.

You can check the status of the monit service using the command**:**

**/etc/init.d/monit status**

**If Monit is not installed automatically while installing SAB or while installing SafeSquid manually, you must install and configure it manually.**

**Follow the below steps to install Monit**:

Run the below command to install the monit service

```bash
apt-get install monit
```
Open **/etc/monit** folder and edit **monitrc** configuration file.

Set the parameters as shown below-
-   To check the services in a 3-second interval
set daemon 3

-   Enable the built-in web server for browsing the services you're monitoring:

set httpd port 2812 and

use address localhost

allow localhost

allow admin:monit

allow @monit

-   To include the configuration or its parts from other files or directories

```bash
include /etc/monit/conf.d/
```
-   Restart the monit service by using the command

```bash
/etc/init.d/monit restart
```
-   Check whether SafeSquid is monitored by Monit or not by using the command

```bash
monit status
```
You will see all services monitored by the monit

### Testing
To test the working of the Monit service, stop the SafeSquid service by using the command

```bash
/etc/init.d/safesquid stop
```
Now check the process ID of the SafeSquid service with the command

```bash
pidof safesquid
```
You will observe that the SafeSquid service had automatically been started by Monit without any user interaction.



## Add Monit service to startup
You can also execute the command below to start a monit service for every machine reboot.

```bash
update-rc.d monit enable
```

