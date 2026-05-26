---
title: SafeSquid SWG Directories
description: "SafeSquid directory layout: installation, configuration, modules, logs, and performance tuning on Linux."

keywords:
  - SafeSquid directory structure
  - SafeSquid configuration files
  - SafeSquid log management
  - SafeSquid modules and plugins
  - SafeSquid performance tuning
  - SafeSquid SSL and DLP directories
---


# SafeSquid SWG Directories

SafeSquid installation and operational directories adhere to the Linux Filesystem Hierarchy Standard (FHS) and house core components for Layer 7 security, system management, and performance optimization. Key directories and their purposes are outlined below:



## SafeSquid Installation Directory

```bash npm2yarn
/usr/local/safesquid
```

The diretory contains all core SafeSquid Web Gateway components. The executables and libraries enable Layer 7 security, threat mitigation, throughput acceleration, and system management capabilities.



## SafeSquid service init scripts

```bash npm2yarn
/etc/init.d/safesquid
```

Contains scripts for managing SafeSquid services, including initialization, termination, and status checks. The SafeSquid script supports commands such as **\{start|stop|restart|status|foreground}** for service control. The service is configured to start automatically on system boot, ensuring all necessary dependencies and environmental variables are set during initialization. This script is frequently used to manage the SafeSquid service operations.



## TCP Tuning Script

```bash npm2yarn
/etc/init.d/tcp_tune.sh
```

SafeSquid stores **tcp\_tune.sh** script in the directory **/etc/init.d/** for TCP tuning. This script will optimize/set some of the values of the TCP parameters like

- maximum number of packets to put in the queue before delivery to the upper layer
- the default and maximum write (receiving) and read (sending) buffer size allocated to any connection
- the maximum number of pending requests to put in the queue before processing one connection
- The port ranges are available for a new connection
- whether to reset new connections if the system is currently overflowed with new connection attempts that the daemon(s) cannot handle
- how long to keep sockets in a wait state after connections are closed
- Keep-alive parameters for overall stability and system resource utilization
- maximum number of remembered connection requests, that have not received an acknowledgment from the connecting client
- TCP receives memory and transmits buffer size
- whether to allow to reuse of TIME-WAIT sockets for new connections

SafeSquid stores the modified TCP parameters into **/tmp/sysctl\_.conf** file for debugging purposes.



## SafeSquid Log Management Script

```bash npm2yarn
/etc/logrotate.d/safesquid
```

The SafeSquid log management script automates the rotation and archiving of log files exceeding 1GB in size using the **logrotate** utility. Logs are compressed into GZIP format to optimize disk space usage. By default, **logrotate** runs daily via a cron scheduler, ensuring systematic log management to prevent disk space exhaustion.



## Monit configuration file for SafeSquid

```bash npm2yarn
/etc/monit/conf.d/safesquid.monit
```

Enables the **Monit** to monitor the SafeSquid service. If the service stops or fails, **Monit** automatically restarts it without user intervention. The file is placed in the **conf.d** directory to preserve the original configuration and provide seamless service management and monitoring.



## PAM Configuration File for SafeSquid

```bash npm2yarn
/etc/pam.d/safesquid
```

Defines PAM (Pluggable Authentication Modules) settings for SafeSquid. PAM provides a modular framework for authentication, leveraging **libpam** and dynamically linked modules (**.so** files). SafeSquid utilizes the pam\_unix.so module for Unix-based authentication (using **/etc/shadow** and **/etc/passwd**) and the pam\_permit.so module for universal access permissions. PAM ensures secure user authentication and resource allocation.

SafeSquid uses **pam\_unix.so** and **pam\_permit.so** files.

- pam\_unix: This is the standard Unix authentication module. It performs authentication against hashed passwords stored in **/etc/shadow** file and **/etc/passwd** file.
- pam\_permit: This module always permits access and returns success. It does nothing else.



## System Tuning Configuration File

```bash npm2yarn
/etc/sysctl.conf
```

Contains the system tuning parameters, to increase the performance. SafeSquid modifies and saves this file for setting system variables. This file is a preload /configuration file that is used to modify kernel parameters at runtime. These parameters are listed under the**/proc/sys** directory.

SafeSquid optimizes various Linux networking and system settings such as:

- Improves memory-intensive workloads
- Limits the number of discrete mapped memory areas
- Maximum number of packets to put in the queue before delivery to the upper layer
- Increase the maximum connections
- Define the port range available for a new connection
- The maximum amount of option memory buffers
- The default and maximum amount for the receive and send socket memory
- Minimum, average, and maximum size of the TCP read and send buffers



## Main SafeSquid Configuration File

```bash npm2yarn
/opt/safesquid/bin/safesquid
```

The SafeSquid total configuration file that is soft-linked with the running version of SafeSquid. If you delete this file SafeSquid will not work.



## Customization Library of Add-on Modules

```bash npm2yarn
/opt/safesquid/bin/modules
```

SafeSquid has a library of add-on modules that can be easily added or removed, to enhance or modify existing features. SafeSquid modules are independently developed and compiled units from a source file. Each module encapsulates shared object(.so) and XML files to implement a particular functionality. SafeSquid loads all add-on modules from the directory **/opt/safesquid/bin/modules** when the process is started.



## SafeSquid DLP Feature

```bash npm2yarn
/opt/safesquid/bin/modules/dlp
```

SafeSquid has a DLP feature as an add-on module. This folder contains a shared object (.so) and XML files of the DLP module. The data loss prevention (DLP) feature detects potential data breaches/data ex-filtration transmissions and prevents end-users from sending sensitive or critical information outside the corporate network. For example, if an employee tries to upload a corporate file via email, then the file will not be uploaded, and the template will be displayed.



## SafeSquid Elevated Privacy Module

```bash npm2yarn
/opt/safesquid/bin/modules/elevated
```

Contains shared object (.so) and XML files of the Elevated Privacy module. You can use Elevated Privacy to protect privacy activity across different websites. Otherwise, third-party cookies will be tracking your activities. Example: When you are surfing the internet by logging into any of your accounts like Hotmail, Yahoo, Gmail, Online Banking... etc. Your activities will be tracked by third-party and referral domains. Set 'Privacy Level' as per your requirement to block Third-Party Cookies, and hide the HTTP & HTTPS referer and User Agents.



## SafeSquid ICAP Module

```bash npm2yarn
/opt/safesquid/bin/modules/icap
```

Contains shared object **(.so)** and XML files for the ICAP (Internet Content Adaptation Protocol) module. The ICAP module enables the proxy server to interface with an ICAP server to modify, satisfy, or redirect HTTP/FTP requests and responses.

- **HTTP Caching Systems**: Transactions are routed through the ICAP server, allowing modification or redirection of web requests and responses
- **FTP Systems**: Transactions pass through the ICAP server for integration with virus scanners or content-filtering tools, enabling advanced content inspection and security



## SafeSquid Image Analyzer Module

```bash npm2yarn
/opt/safesquid/bin/modules/imgfilter
```

Has a shared object (**.so**) and XML files for the Image Analyzer (Imgfilter) module. The module enables real-time analysis of graphical content in images to identify and block pornographic or suspicious content. Blocked images are replaced with blank or checkered placeholders. The detection accuracy is configurable and ranges between 80%-90%, making it an effective deterrent.



## Content Modifier Module

```bash npm2yarn
/opt/safesquid/bin/modules/rewrite
```

Contains a shared object (.so) and XML files for the Content Modifier (Content Re-Write) module. The module uses regular expressions to modify web page content, files, client headers, and server headers in real time. It is designed to remove potentially harmful elements like ActiveX, JavaScript, or cookies from untrusted websites before delivering the content to users. This feature requires cautious implementation due to its powerful capabilities.



## Ssqore Web Categorization

```bash npm2yarn
/opt/safesquid/bin/modules/ssqore
```

Contains a shared object (.so) and XML files of the Ssqore module. Ssqore allows you to categorize the websites, depending on the potential nature of the content served by the website. Ssqore queries SafeSquid's Content Categorization Service (CCS), to determine if a website belongs to one or more categories.



## SqScan Anti-Malware

```bash npm2yarn
/opt/safesquid/bin/modules/sqscan
```

Contains a shared object (.so) and XML files of the SqScan module. SqScan is a high-speed in-memory virus scanner built into a module that protects users against malware. SqScan uses an anti-malware signature database which is constantly updated to ensure the application of the latest anti-malware definitions. SqScan uses proactive protection, such as generic detection routines, a heuristic engine, and a behavior-based engine to proactively prevent unknown or previously unseen malware.



## SafeSquid WCCP Module

```bash npm2yarn
/opt/safesquid/bin/modules/wccp
```

Contains a shared object (.so) and XML files of the WCCP module.

Web Cache Communication Protocol (WCCP) is a Cisco-developed content-routing protocol that provides a mechanism to redirect traffic flows in real-time. It has built-in load balancing, scaling, fault tolerance, and service-assurance (failsafe) mechanisms. SafeSquid WCCP module is configured to interact with WCCP-enabled routers. WCCP-enabled routers are used as gateways for End users. All the client's traffic will be transparently redirected to the SafeSquid proxy by a router.



## UI Layout directory

```bash npm2yarn
/opt/safesquid/bin/sections
```

Contains the necessary XMLs of SafeSquid. You can find XML of every feature in this folder except add-on modules. These XMLs are used for rendering the SafeSquid User Interface.



## Setup and Startup Configuration Folder

```bash npm2yarn
/opt/safesquid/default
```

Contains default **startup.ini** and **setup.ini** files. These **files should not be altered**.

SafeSquid loads default configuration/startup parameters from the **startup.ini** file. You can modify the startup parameter values from the SafeSquid User interface. Modified values of startup parameters are stored in **/opt/safesquid/startup.ini** file.

SafeSquid loads default setup parameters from the setup.ini file. To modify setup parameters, you should take a copy of the setup.ini file and store it as **/opt/safesquid/setup.ini** before editing it manually.



## SafeSquid Temporary Folder

```bash npm2yarn
/tmp/safesquid
```

Contains the temporary files created by SafeSquid while the process is running or upgrading to the latest version.



## SafeSquid Core Directory

```bash npm2yarn
/usr/local/safesquid
```

The directory contains security, ui\_root, SQLite, and bin sub-directories. These sub-directories contain the various files related to

- activation of the product
- User Interface rendering
- SQLite Database
- SSL certificates etc.



## Custom Scripts Folder

```bash npm2yarn
/usr/local/safesquid/bin
```

Contains the scripts that can be executed/run with the external applications section. User-created scripts should be stored in /usr/local/safesquid/bin directory for execution.



## Security Component Folder

```bash npm2yarn
/usr/local/safesquid/security
```

The directory has policies, SSL, and DNS sub-directories. This directory contains activation\_key.updates.backup, activation\_key.updates, and activation\_key files which are product activation-related files. These files should never be deleted otherwise SafeSquid service will be stopped.



## Configuration Policy Folder

```bash npm2yarn
/usr/local/safesquid/security/policies
```

Contains the default SafeSquid configuration file (**default.config.xml**). Configuration sections and policies can be modified through the SafeSquid interface. Upon the first modification and save, two files are generated:

- **config.xml**: The updated active configuration file
- **config\_XXXX@YYYY\_ZZZZ.xml**: A backup file representing the last saved configuration, where:
- **XXXX** is the username of the individual who modified it
- **YYYY** is the IP address from which the modification was made
- **ZZZZ** is the timestamp of the modification

Subsequent modifications create additional timestamped backup files, allowing restoration of the last known stable configuration when necessary.



## SSL Certificate Store

```bash npm2yarn
/usr/local/safesquid/security/ssl/
```

The folder has the SSL ROOT certificates and trusted bundle files. It also contains the SubCA used in the OpenVPN configuration.



## Database Configuration

```bash npm2yarn
/usr/local/safesquid/sqlite
```

Contains the users.db.conf, reporting\_db.conf, and bypass\_db.conf files. These are configuration files for the SQLite database in SafeSquid.



## Web Interface Root

```bash npm2yarn
/usr/local/safesquid/ui_root/
```

Contains further sub-directories that contain files used for rendering SafeSquid Web User Interface.



## CGI Scripts

```bash npm2yarn
/usr/local/safesquid/ui_root/cgi-bin
```

Contains the additional scripts that are used for the execution of the well-defined functionality of SafeSquid. Some of the functionalities are generation of support tarball, generation of performance plot, Kerberos setup, etc.



## Style Sheets

```bash npm2yarn
/usr/local/safesquid/ui_root/css
```

Has all the CSS (Cascading Style Sheets) files. These files help to describe how HTML elements of SafeSquid are displayed on the screen. Modification in these files without proper knowledge may disarrange the SafeSquid interface display.



## Web Fonts

```bash npm2yarn
/usr/local/safesquid/ui_root/fonts
```

Have the web font files used in SafeSquid. You will get glyphicons-halflings-regular.*, font awesome-web font.*, and hinted-SegoeUI.\* files. Font Awesome is a font and icon toolkit based on CSS and LESS. Segoe is a typeface or family of fonts, that is best known for its use by Microsoft. Glyphis used for a variety of designs of a certain character. You can add more web font files as per your needs.



## Interface Images

```bash npm2yarn
/usr/local/safesquid/ui_root/img
```

Contains the image files that are shown on the SafeSquid interface. Some of these files are in PNG and GIF formats used to show simple animations or small icons on the interface. You can add your preferred image files to this folder to modify the interface display. Modify CSS/JavaScript files and edit your preferred image file names to modify the SafeSquid interface display.



## JavaScript Resources

```bash npm2yarn
/usr/local/safesquid/ui_root/js
```

This directory contains all the JavaScript files used in SafeSquid to perform various functionality.



## HTML Templates

```bash npm2yarn
/usr/local/safesquid/ui_root/templates
```

This directory contains files for SafeSquid's web interface, including:

- **upgrade.sh**: Script for checking and upgrading SafeSquid to the latest version
- **success.html**: Template for successful login messages
- **landing.html**: Captive portal template for user redirection
- **block\_bypass.html**: Template displayed when access is denied or bypassed

Custom HTML templates can be added to this directory and configured in the templates section to customize browser displays.



## SafeSquid's Caching directory

```bash npm2yarn
/var/cache/safesquid
```

This is the default directory to store all caching objects. You can configure SafeSquid''s cache and its storage area, for optimum performance. SafeSquid will create a cache store for all cacheable objects if the cache section is enabled.



## Web analytics databases

```bash npm2yarn
/var/db/safesquid/report
```

This directory contains SQLite database files used by SafeSquid to retrieve user information for the reports tab. The key files include:

- **main.db** and **safesquid2.db**: Primary database files
- **main.db-shm** and **safesquid2.db-shm**: Shared memory storage files for database operations
- **main.db-wal** and **safesquid2.db-wal**: Write-ahead log files storing modifications before they are committed

Additionally, a time-stamped file (**YYYYMMDDhhmmss-main.db**) is created after every 1000 transactions for audit and recovery purposes. These files collectively ensure efficient and reliable database operations.



## SSL certificate storage

```bash npm2yarn
/var/db/safesquid/ssl
```

Contains the temporary SSL certificates created by safesquid for webservers, while doing https inspection.



## User-to-IP mapping database

```bash npm2yarn
/var/db/safesquid/users_ip_db
```

SQLITE\_DB file containing usernames assigned to IP addresses.



## Application Signature Storage

```bash npm2yarn
/var/lib/safesquid/application_signatures
```

Stores the **applications3** file in the **updates** folder which is an application signature file. SafeSquid service checks and downloads the latest application signature file from the cloud on an hourly basis.



## Custom Category Storage

```bash npm2yarn
/var/lib/safesquid/category
```

Contains a category.db file which is the local database for custom categories.



## Content Signature Shared Library and Storage

```bash npm2yarn
/var/lib/safesquid/content_signatures
```

The directory contains the following components for SafeSquid's content signature functionality:

- **magic.mgc** and **libmagic.so**: Shared library files essential for content signature operations
- **updates folder**: Stores the content4 file, which serves as the content signature database

The SafeSquid service periodically checks and downloads the latest content signature updates from the cloud every hour, ensuring up-to-date content recognition capabilities.



## Image Analyzer Dependency and Finetuning Files

```bash npm2yarn
/var/lib/safesquid/imgfilter
```

The directory contains essential dependencies for the Image Analyzer module:

- **libIAImageReaderShared.so** and **libIAEngineShared.so**: The engine and Reader shared library files required for module initialization
- **imgfilter.tune**: Configuration file for fine-tuning the filter by setting the threshold score limit

The SafeSquid service periodically checks and downloads the latest versions of these library files from the cloud on an hourly basis to ensure optimal performance.



## Ssqore Dependency Files and Signature Storage

```bash npm2yarn
/var/lib/safesquid/ssqore
```

Contains essential library files for the proper execution of the **Ssqore** module. All the Ssqore signatures are stored in the **parental\_sig** subfolder. SafeSquid service checks and downloads the latest **libbdupdatesdk.so** file and stores into **an **update subfolder on an hourly basis.



## Sqscan Dependency Files and Anti-Malware Signature Storage

```bash npm2yarn
/var/lib/safesquid/sqscan
```

Contains essential library files for the proper execution of the SqScan module. All the SqScan anti-Malware signature databases are stored in the **Plugins** subfolder. SafeSquid service checks and downloads the latest **libbdupdatesdk.so** file and stores into an **update** subfolder on an hourly basis.



## SafeSquid Config Logs

```bash npm2yarn
/var/log/safesquid/config
```

Folder contains the **config.log** file which stores the details about modification in the SafeSquid configuration via SafeSquid UI. This log file will help the administrator trace any rule that is added/modified/deleted in the SafeSquid configuration. The administrator can easily roll back the faulty changes from the SafeSquid configuration.  Log rotation will change **config.log** into **XXXX-config.log** file, where XXXX is the time of log rotation.

Below is the heading/legend for the Config Log file- `"ACCESS_TIME"   "SAFESQUID_INTERFACE"   "USERNAME@IP"   "PAGE"  "SECTION"       "ACTION"        "HTTP_METHOD"   "URL"   "REFERER"       "ARGUMENTS"     "CONFIG_FILE"   "REASON"` **Log Rotation**: Log Rotation is the process in SafeSquid to control large log files. Some Log Analyzers and Text Editor cannot process bigger log files (2GB earlier). To handle this SafeSquid sets the parameter LOG\_SIZE\_LIMIT for the maximum file size in bytes for a log file. Exceeding the maximum file size SafeSquid will automatically truncate and compress the log file, further, this file will be renamed and saved on the disk.



## SafeSquid Extended Logs

```bash npm2yarn
/var/log/safesquid/extended
```

Contains the extended.log file detailing the users, applications, and security breaches. This log file will help the administrator to trace each request and response processed by the SafeSquid. Log rotation will change extended.log into **XXXX-extended.log file**, where XXXX is the time of log rotation.

Below is the heading/legend for the Extended Log file-

```
"record_id"     "client_id"     "request_id"    "date_time"     "elapsed_time"  "status"        "size"  "upload"        "download"      "bypassed"      "client_ip"     "username"      "method"        "url"   "http_referer"  "useragent"     "mime"  "filter_name"   "filtering_reason"      "interface"     "cachecode"     "peercode"      "peer"  "request_host"  "request_tld"   "referer_host"  "referer_tld"   "range" "time_profiles" "user_groups"   "request_profiles"      "application_signatures"        "categories"    "response_profiles"     "upload_content_types"  "download_content_types"        "profiles"** **
```



## SafeSquid Native Logs

```bash npm2yarn
/var/log/safesquid/native
```

Contains the **native.log** file detailing the various functional aspects like **REQUESTS, SECURITY, REDIRECT**, etc. that are affected by the various features and their configuration. This file stores all data related to every request and response processed by the SafeSquid which will be helpful to an administrator for debugging purposes. Control the verbosity of the Native Log by specifying LOGLEVEL. Log rotation will change **native.log** into **XXXX-native.log** file, where **XXXX** is the time of log rotation.

**LOG\_LEVEL**: Set to 16777216 (for only warnings) 33554432 (only errors) 67108864 (only profiles) 134217728 (only debug) 268435455 (all activities and debug information). The default is 33554435(errors requests network).



## Performance Logs

```bash npm2yarn
/var/log/safesquid/performance
```

Contains the **performance.log** file, which records metrics to identify outages caused by resource shortfalls, internet connectivity failures, or traffic surges. The log file supports third-party analysis tools like GNU Plot for progressive line-based data analysis.

Log rotation renames **performance.log** to a time-stamped file (**XXXX-performance.log**), where **XXXX** denotes the rotation timestamp, ensuring efficient log management for ongoing performance analysis.

Below is the heading/legend for the Performance Log file-

```
Time Stamp (YYYYMMDDhhmmss) , Elapsed Time , Client Connections Handled , Client Connections Closed , Client Transactions Handled , Client Connections in Pool , Spare Client Threads , Client Threads in Use , Client Threads in Waiting , Threads Starting up , Threads Reserved for Prefetching , Threading Errors , Outbound Connections created , Outbound Connections Failed , Outbound Connection Pool Reused , Outbound Connections in Pool , Bytes in (KBytes) , Bytes Out (KBytes) , Caching Objects Created in Memory , Caching Objects Removed from Memory , DNS Queries Reused , New DNS Queries , DNS Query failures , Total System Memory (KBytes) , Free System Memory (KBytes) , SafeSquid Virtual Memory (KBytes) , SafeSquid Resident Memory (KBytes) , SafeSquid Shared Memory (KBytes) , SafeSquid Code Memory (KBytes) , SafeSquid Data Memory (KBytes) , SafeSquid Library Memory (KBytes) , Connections Handled Delta , Connections Closed Delta , Transactions Handled Delta , Client Pool Delta , Spare Threads Delta , Active Threads Delta , Threads Waiting Delta , Threads Starting up Delta , Threads Prefetching Delta , Threading Errors Delta , Outbound Connections created Delta , Outbound Connections Failed Delta , Outbound Connection Pool Reused Delta , Outbound Connections in Pool Delta , Bytes in (KBytes) Delta , Bytes Out (KBytes) Delta , Caching Objects Created in Memory Delta , Caching Objects Removed from Memory Delta , DNS Queries Reused Delta , New DNS Queries Delta , DNS Query failures Delta, load avg.(1 min), load avg.(5 min), load avg.(15 min), Running Processes, Waiting Processes, User Time, System Time, Total (user + system) Time , User Time Delta , System Time Delta , Total Time Delta
```



## Privacy logs

```bash npm2yarn
/var/log/safesquid/privacy
```

Contains the privacy logs record cookies, cross-site exchange, and Safesquid Elevated Privacy policy enforcements.



## SafeSquid PID

```bash npm2yarn
/var/run/safesquid
```

Contains the **safesquid.pid** file which stores the process ID of SafeSquid. For every restart of SafeSquid, this file is modified with a new process ID.

