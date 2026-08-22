---
title: Security Logs
description: A comprehensive guide to understanding and analyzing SafeSquid proxy logs, including native logs, extended logs, performance metrics, and system integration logs.
keywords:
  - SafeSquid logs
  - SafeSquid troubleshooting
  - SafeSquid native logs
  - SafeSquid extended logs
  - SafeSquid performance log analysis
---



## Logs support troubleshooting and analysis

Logs provide a timeline of events for the OS and applications and are a primary troubleshooting tool. When an issue occurs, the system administrator analyzes log files first. Most logs are plain text under /var/log. With SafeSquid installed, two log types matter: SafeSquid application logs and SafeSquid activity logs (in system logs). To view a log file, use one of:
```bash
less /var/log/logfilename
```
```bash
more -f /var/log/logfilename
```
```bash
 /var/log/logfilename
```
```bash
tail -f /var/log/logfilename
```
```bash
grep -i error /var/log/logfilename
```



## SafeSquid Application Logs

SafeSquid application produces these logs. Logs contain all kinds of error messages, warnings or other events written by the SafeSquid. These messages provide logical, high-level information for specific use cases. Each log message helps administrators understand SafeSquid behavior.
SafeSquid application generates six different log formats.
These logs are named safesquid.log (Native logs), extended.log (NCSA/Extended logs), config.log (Config logs), and performance.log (Performance logs).
Two more log formats were added subsequently as bypass.log and privacy.log.
The path to these log files are as follows:

  -----------------------------------------------------------------------
  **Log File**             **Path**
  ------------------------ ----------------------------------------------
  **safesquid.log**        **/var/log/safesquid/native/**

  **extended.log**         **/var/log/safesquid/extended/**

  **config.log**           **/var/log/safesquid/config/**

  **performance.log**      **/var/log/safesquid/performance/**

  **bypass.log**           **/var/log/safesquid/bypass/**

  **privacy.log**          **/var/log/safesquid/privacy/**
  -----------------------------------------------------------------------

View Native Log and Config Log details from the **SafeSquid Interface**.

### Native logs

It records various functional aspects like REQUESTS, SECURITY, REDIRECT etc. that are affected by the various features and their configuration.

Control the verbosity of the Native log by specifying LOGLEVEL, as shown in the table below.
The LOGLEVEL parameter affects only the SafeSquid's Native log.

  -------------------------------------------------------------------------
  **Value**    **Process logged**      **Value**    **Process logged**
  ------------ ----------------------- ------------ -----------------------
  1            Requests                16384        Forwarding

  2            Network                 32768        Sync

  4            LDAP                    65536        Antivirus

  8            Header filtering        131072       External parser

  16           Interface Request       262144       ICAP

  32           Cookie filtering        524288       SSL

  64           Redirect                1048576      Category

  128          Template                2097152      URL command

  256          Text Analyzer           4194304      Modules

  512          Rewriting               8388608      Security

  1024         Limits                  16777216     Warning

  2048         Caching                 33554432     Error

  4096         Prefetching             67108864     Profiles

  8192         ICP                     134217728    Debug
  -------------------------------------------------------------------------

To record only requests set LOGLEVEL to 1; to record only caching set LOGLEVEL to 2048. To record rewriting, limits, and forwarding set LOGLEVEL to 512 + 1024 + 16384 (17920). To log everything (risk: very large log file quickly) set LOGLEVEL to the sum of all values in the table, 134217727—also the default if LOGLEVEL is commented out. For debug logs only set LOGLEVEL to 134217728. For all activities plus debug set LOGLEVEL to 268435455.

:::note
Adjusting this value requires a restart of SafeSquid service.
:::
This file stored all data related **to every request and response** processed by the SafeSquid. These logs will be useful for debugging purpose.

[Access the SafeSquid  User Interface ](/docs/SafeSquid_SWG/Configuration_Portal/)

On top right of Safesquid Interface view **Reports >> Dashboard**

Click on "**Native logs**" to see the run time native logs.

**Each request and response** processed through SafeSquid is visible. Use the search bar to find a particular string. The **Resume** button stops real-time streaming of logs.

  -----------------------------------------------------------------------------------------------------------------------------------------------
  ![Access Reports to view Dashboard on safesquid user interface ](/img/How_To/Analyze_The_SafeSquid_Logs/image1.webp)
  -----------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------



### Extended logs
The extended.log (NCSA / Extended log format) records maximum details of each request handled by the proxy application. Extended logs will be helpful for generation of reports to analyze the user activities.

**FORMAT / LEGEND:**

"record_id"     "client_id"     "request_id"    "date_time"     "elapsed_time"  "status"        "size"  "upload"  "download"      "bypassed"      "client_ip"     "username"      "method"        "url"   "http_referer"    "useragent"     "mime"  "filter_name"   "filtering_reason"      "interface"     "cachecode"     "peercode"        "peer"  "request_host"  "request_tld"   "referer_host"  "referer_tld"   "range" "time_profiles"   "user_groups"   "request_profiles"      "application_signatures"        "categories"    "response_profiles"       "upload_content_types"  "download_content_types"        "profiles"

**Example Log Line1:
"1531492103912WfkgX"    "91"    "2"    "13/Jul/2018:19:58:26"    "3663"    "200"    "626"    "0"    "626"    "FALSE"    "192.168.0.24"    "anonymous@192.168.0.24"    "GET"    ""    "https://accounts.google.com/"    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"    "image/png"    "-"    "-"    "192.168.24.74:8080"    "TCP_MISS"    "DIRECT"    "ssl.gstatic.com"    "ssl.gstatic.com"    "gstatic.com"    "accounts.google.com"    "google.com"    "100-1K"    ""    "ADMINS"    ""    "Unidentified Web2.0,Firefox,Internet Browser"    "Search Engines & Portals"    "POTENTIAL MALWARE THREATS,SMALL DOWNLOADS"    "-"    "image/png"    "READ ONLY,ANTIVIRUS"**

**Example Log Line2:**
```
**"153157359815951WfkgX"    "1595"    "1"    "14/Jul/2018:18:36:38"    "106"    "403"    "1517132"    "1517132"    "0"    "FALSE"    "192.168.0.24"    "anonymous@192.168.0.24"    "POST"    [http://www.csm-testcenter.org:80/test](http://www.csm-testcenter.org/test)    "-"    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"    "text/html"    "DLP"    "application/vnd.ms-excel"    "192.168.24.74:8080"    "TCP_DENIED"    "DIRECT"    "safesquid"    "www.csm-testcenter.org"    "csm-testcenter.org"    www.csm-testcenter.org    "csm-testcenter.org"    "1M-10M"    ""    "ADMINS"    "MEDIUM UPLOADS"    "Unidentified Web2.0,All Posts,All Uploads,Uploads,Firefox,Internet Browser"    "Unknown"    ""    "application/vnd.ms-excel,text/plain"    "-"    "READ ONLY,ANTIVIRUS,BLOCK UPLOADS"**
```

The details of the fields in extended.log are as follows:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Field**                **Explanation**
  ------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  record_id                A unique record identifier, to prevent duplication of records when imported into SQL databases. Example1> 1531492103912WfkgX

  client_id                The internal SafeSquid ID associated with the present/ongoing connection. Example1> 91

  request_id               A unique ID for every request created in the present/ongoing connection to the web-server. Example1> 2

  date_time                The date and time when the HTTP request was sent. The fields in the date/time field are [DD/MMM/YYYY:hh:mm:ss], where the fields are defined as  follows:
                           DD is the day of the month, MMM is the month, YYYY is the year, hh is the hour, mm is the minute, ss is the seconds. Example1> 13/Jul/2018:19:58:26

  elapsed_time             Length of time in milliseconds that current HTTP request used to complete the transaction. Example1> 3663

  status                   Numeric code indicating the success or failure of the HTTP request. This code is a server response to a browser's request. Example1> 200

  size                     Numeric field indicating the data transferred in number of bytes as part of the HTTP request, not including the HTTP header. Example1> 626

  upload                   Numeric field indicating the data transferred from webserver to client. Example2> 1517132

  download                 Numeric field indicating the data transferred from client to webserver. Example1> 626

  bypassed                 Boolean (TRUE/FALSE) value which indicates whether the current request was bypassed or not after blocked by SafeSquid filter. Example1> FALSE

  client_ip                The IP address of the requesting client. Example1> 192.168.0.24

  username                 The username@client_ip, (or user ID) used by the client for authentication. If no value is present, "anonymous" is substituted. Example1> anonymous@192.168.0.24

  method                   A method is part of HTTP request sent by client to the server. Example1> GET

  url                      An HTTP url is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it. Example1>

  http_referer             An HTTP header field that identifies the address of the age that linked to the resource being requested. "-" is substituted when there is no referrer in HTTP header field. Example1> https://accounts.google.com/

  useragent                User agent is the client which initiates a request. Useraagent are often browsers, editors, spiders (web-traversing robots), or other end user tools. Example1> Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0

  mime                     Mime-type (media type) are used to identify the format of a file and format contents transmitted on the Internet. Example1> image/png

  filter_name              Filter name due to which the request was blocked. "-" is substituted when request is allowed. Example2> DLP

  filtering_reason         If the request gets blocked, then predefined reason for blocked request will be set. "-" is substituted for unknown reasons and allowed requests. Example2> application/vnd.ms-excel

  interface                Interface IP:PORT that received the request. This field is important when SafeSquid is listening on multiple IPs or Ports. Example1> 192.168.24.74:8080

  cachecode                Cachecodes are access error code set by SafeSquid during connection with TCP/UDP request. Example2> TCP_DENIED

  peercode                 Peercode entry represents a code that explains how the request was handled, for example, by forwarding it to a peer, or returning the request to the source. Example1> DIRECT

  peer                     Peer represents the name of the host from which the object was requested. This host may be the origin site, a parent, or any other peer. Example1> ssl.gstatic.com

  request_host             Fully qualified domain name(FQDN) of the requested web-server. Example1> ssl.gstatic.com

  request_tld              Top-level domain name of the requested web-server. Example1> gstatic.com

  referer_host             The referrer is the URL of the HTTP resource that referred the user to the resource requested. "-" is substituted when there are no referrers. Example1> accounts.google.com

  referer_tld              Top-level domain name of the referrer URL that referred the user to the resource requested. "-" is substituted when there are no referrers. Example1> google.com

  range                    Data transferred in number of bytes as part of the HTTP request which comes under SafeSquid predefined range. Example2> 1M-10M

  time_profiles            Comma separated list of Time profiles that categorize, websites based on the time ranges. "" is substituted when no profiles are applied.

  user_groups              Comma separated list of User Group(s) to which this entry is applicable. Example1> ADMINS

  request_profiles         Comma separated list of Request profiles that were applied to the request. "" is substituted when no request profiles are applied. Example2> MEDIUM UPLOADS

  application_signatures   Comma separated list of application signatures that were applied to the request. Example2> Unidentified Web2.0,All Posts,All Uploads,Uploads,Firefox,Internet Browser

  categories               Comma separated list of categories that were applied to the request. "" is substituted when no profiles are applied. Example2> Search Engines & Portals

  response_profiles        Comma separated list of Response profiles that were applied to the request. "" is substituted when no response profiles are applied. Example2> POTENTIAL MALWARE THREATS,SMALL DOWNLOADS

  upload_content_types     Comma separated list of Upload Content Type. "-" is substituted when no profiles are applied or content types are unknown. Example2> application/vnd.ms-excel,text/plain

  download_content_types   Comma separated list of Download Content Type. "-" is substituted when no profiles are applied or content types are unknown. Example1> image/png

  profiles                 Comma separated list of profiles that were applied to the request. "" is substituted when no profiles are applied. Example2> READ ONLY,ANTIVIRUS,BLOCK UPLOADS
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

On top right of Safesquid Interface view **Reports >> Dashboard  **

Click on "**Detailed logs**" to see the run time extended logs.

Run time detailed logs displayed are Time, Username, Client ID, Method, URL, Status, Size, Referer, Useragent, Mime, Filter Name, Filter Reason, Profiles, Request profiles, Response profiles, Categories, Applications, Upload content type, Download content type from Extended Logs.

You can use **search option** to find information related to specific user or specific response code...etc. It's a common search option for filtering.

**Show/Hide Column** button is for** hiding** any option from above list.

You can also **search individually** from above list.

  -------------------------------------------------------------------------------------------------------------
  ![Detailed logs of safesquid ](/img/How_To/Analyze_The_SafeSquid_Logs/image2.webp)
  -------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------

### Config logs

Config logs contain the details related to the **SafeSquid user interface activities **like **configuration change**. You can find the users information who made the configuration changes and when.

**FORMAT / LEGEND**:

"ACCESS_TIME"    "SAFESQUID_INTERFACE"    "USERNAME@IP"    "PAGE"    "SECTION"    "ACTION"    "HTTP_METHOD"    "URL"    "REFERER"    "ARGUMENTS"    "CONFIG_FILE"    "REASON"

**Example Log Line1**:
**"01/Aug/2018:01:30:19"    "192.168.24.74:8080"    "anonymous@192.168.0.27"    ""    "dlp"    "edit"    "POST"    "[http://safesquid.cfg:80/](http://safesquid.cfg/)"    "http://safesquid.cfg/"    "F0=TRUE&F1=Block the uploading of PDF and Microsoft Word Documents. &F2=BLOCK-ALL-UPLOADS&F3=application/octet-stream,application/x-msdownload|application/x-dosexec&F4=.bat$|.exe$,.exe$&F5=MIME_OR_FILE&F6=DO_NOT_BYPASS&handler=configuration&section=dlp&subsection=DLP&id=3&action=edit"    ""    ""**

**Example Log Line2**:
**"01/Aug/2018:18:29:38"    "192.168.24.74:8080"    "anonymous@192.168.0.27"    ""    ""    ""    "POST"    "[http://safesquid.cfg:80/](http://safesquid.cfg/)"    "http://safesquid.cfg/"    "handler=save&filename=config.xml" "/usr/local/safesquid/security/policies/config_anonymous@192.168.0.27_2018-08-27-18-29-38.xml"    ""**

The details of the fields in config.log are as follows:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Field**             **Explanation**
  --------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ACCESS_TIME           The date and time when the request for modification in SafeSquid configuration was sent. The fields in the date/time field are [DD/MMM/YYYY:hh:mm:ss], where the fields are defined as follows:
                        DD is the day of the month, MMM is the month, YYYY is the year, hh is the hour, mm is the minute, ss is the seconds.
                        Example1> 01/Aug/2018:01:30:19

  SAFESQUID_INTERFACE   Interface IP:PORT that received the request for modification in SafeSquid configuration. This field is important when SafeSquid is listening on multiple IPs or Ports. Example1> 192.168.24.74:8080

  USERNAME@IP           The USERNAME@IP, (or user ID) of the client who modified the SafeSquid configuration. If username is unknown then, "anonymous" is substituted. Example1> anonymous@192.168.0.24

  PAGE

  SECTION               SafeSquid section where rule is either created or modified or deleted. Example1> DLP

  ACTION                Action taken on any SafeSquid section to add a new policy or edit/ clone/ delete an existing policy. Example1> edit

  HTTP_METHOD           HTTP method to request sent by client to the server. Example1> POST

  URL                   SafeSquid interface URL is a reference to open WebGUI to View/change configuration. Example> [http://safesquid.cfg:80/](http://safesquid.cfg/)

  REFERER               Referer address of the SafeSquid interface URL. Example1> http://safesquid.cfg/

  ARGUMENTS             This field displays the SafeSquid policy details which was modified.
                        Where F## shows the field values of the all fields. section=## displays section name. id=## determines the policy number from top. action=## shows the action performed on that policy.
                        Example1> F0=TRUE&F1=Block the uploading of PDF and Microsoft Word Documents. &F2=BLOCK UPLOADS&F3=application/octet-stream, application/x-msdownload|application/x-dosexec&F4=.bat$|.exe$,.exe$&F5=MIME_OR_FILE&F6=DO_NOT_BYPASS&handler=configuration&section=dlp&subsection=DLP&id=3&action=edit

  CONFIG_FILE           A backup config.xml file along with the path which can be restored at any time by the administrator.
                        Example2>/usr/local/safesquid/security/policies/config_anonymous@192.168.0.27_2018-08-27-18-29-38.xml

  REASON
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

On top right of Safesquid Interface view **Reports >> Dashboard**

Click on **"Config logs"**

You can use **search option** to find information related to specific Time, Interface, Username, Section, Action, Arguments, Config File.

  ------------------------------------------------------------------------------------------------------------------
  ![Configuration logs of safesquid ](/img/How_To/Analyze_The_SafeSquid_Logs/image3.webp)
  ------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------



### Performance logs
Performance logs will be helpful to analyze the performance of SafeSquid.
SafeSquid Performance logs provide performance metrics to identify any outage due to resource shortfall, or failure in Internet Connectivity, or surge in web-traffic, etc.
SafeSquid performance log has been extended to make it easier for analysis with third-party software such as GNU Plot that analyzes records on a progressive per line basis.

**FORMAT / LEGEND**:

Time Stamp (YYYYMMDDhhmmss),Elapsed Time,Client Connections Handled,Client Connections Closed,Client Transactions Handled,Client Connections in Pool,Spare Client Threads,Client Threads in Use,Client Threads in Waiting,Threads Starting up,Threads Reserved for Prefetching,Threading Errors,Outbound Connections created,Outbound Connections Failed,Outbound Connection Pool Reused,Outbound Connections in Pool,Bytes in (KBytes),Bytes Out (KBytes),Caching Objects Created in Memory,Caching Objects Removed from Memory,DNS Queries Reused,New DNS Queries,DNS Query failures,Total System Memory (KBytes),Free System Memory (KBytes),SafeSquid Virtual Memory (KBytes),SafeSquid Resident Memory (KBytes),SafeSquid Shared Memory (KBytes),SafeSquid Code Memory (KBytes),SafeSquid Data Memory (KBytes),SafeSquid Library Memory (KBytes),Connections Handled Delta,Connections Closed Delta,Transactions Handled Delta,Client Pool Delta,Spare Threads Delta,Active Threads Delta,Threads Waiting Delta,Threads Starting up Delta,Threads Prefetching Delta,Threading Errors Delta,Outbound Connections created Delta,Outbound Connections Failed Delta,Outbound Connection Pool Reused Delta,Outbound Connections in Pool Delta,Bytes in (KBytes) Delta,Bytes Out (KBytes) Delta,Caching Objects Created in Memory Delta,Caching Objects Removed from Memory Delta,DNS Queries Reused Delta,New DNS Queries Delta,DNS Query failures Delta,load avg.(1 min),load avg.(5 min),load avg.(15 min),Running Processes,Waiting Processes,User Time,System Time,Total (user + system) Time,User Time Delta,System Time Delta,Total Time Delta

**Example Log Line1**:
**20180905172137,1603,21151,20941,44316,119,8016,91,68,17,0,0,13640,975,20650,139,1853191,2012552,0,0,11317,3185,41,5976008,2389076,596224,98868,4204,2472,0,
472172,13,32,52,11,0,-30,30,0,0,0,5,3,27,0,1698,884,0,0,5,2,0,0.25,0.21,0.49,1,562,60.000000,56.000000,116.000000,0.000000,0.000000,0.000000**

**Example Log Line2**:
**20180905172139,1605,21170,20972,44346,132,8016,66,93,17,0,0,13654,976,20660,139,1854126,2014492,0,0,11328,3186,41,5976008,2387184,596224,98888,4204,2472,0,
472172,19,31,30,13,0,-25,25,0,0,0,14,1,10,0,935,1940,0,0,11,1,0,0.23,0.21,0.49,1,562,60.000000,56.000000,116.000000,0.000000,0.000000,0.000000**

The details of the fields in performance.log are as follows:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Field**                                   **Explanation**
  ------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Time Stamp (YYYYMMDDhhmmss)                 Time when SafeSquid generated this record and stored in performance log. SafeSquid begins printing of each record on a new line with the first column as the TimeStamp in YYYYMMDDhhmmss format.
                                              Example> Log line1 was loged at 2018 September, 5th at 17:21:37 hence it displays 20180905172137 in YYYYMMDDhhmmss format.

  Elapsed Time                                Time in seconds since the SafeSquid process started. This is the time in seconds since the process started.
                                              Example> Log line1 reports that SafeSquid process running from last 1603 seconds.

  Client Connections Handled                  Total Client Connections handled by SafeSquid since the start of process.
                                              Example> Log line1 reports that since SafeSquid process running (from 1603 seconds), process handled 21151 incoming connections.

  Client Connections Closed                   Total Client Connections closed by SafeSquid since the start of process.
                                              Example> Log line1 reports that since the start of the process, SafeSquid had closed 20941 incoming connections.
                                              Thus we can interpret that at 2018-05-09 17:21:37 there were 21151 - 20941 = 210 concurrent incoming client connections. So while the 3rd counter and 4th counter are not very significant by themselves, their differential value is very important as it gives a an idea about concurrent connections being handled at any point.

  Client Transactions Handled                 Total Number of transactions handled between clients and SafeSquid since the start of the process. Within each connection a client may send multiple requests, to service these requests SafeSquid may have to transact multiple HTTP transactions.
                                              Example> Log line1 reports that since start of the process, SafeSquid had handled 44316 transactions.

  Client Connections in Pool                  Connections in local pool of SafeSquid. After request handling each connection is been kept in client connection pool for persistence.
                                              SafeSquid may not forcibly close a client connection after performing a transaction within, and even wait for sometime allowing the client to reuse a connection after a few seconds. Such connections are maintained in a "Client Pool".
                                              Example> Log line1 reports that there were 119 client connections that were idling in the client pool. Thus out of the 210 concurrent connections (derived above), 119 were in the client pool and the remaining 91 were either actively transacting, or maybe in the various stages of closure.

  Spare Client Threads                        Additional number of Threads that SafeSquid may produce to service client requests when SafeSquid printed this record.
                                              Example> Log line1 reports that SafeSquid can still produce 8016 client requests.

  Client Threads in Use                       Concurrent Requests being serviced by SafeSquid when SafeSquid printed this record.
                                              Example> Log line1 reports that SafeSquid had used 91 threads to fulfill client requests.

  Client Threads in Waiting                   Threads just released by client requests and available for instantly servicing a client request when SafeSquid printed this record.
                                              Example> Log line1 reports that at present 68 client threads are in waiting state.

  Threads Starting up                         Some Threads already assigned for some sections when SafeSquid starts, these are special threads of SafeSquid.
                                              Example> Log line1 reports that at present 17 threads are used by SafeSquid for internal processes.

  Threads Reserved for Prefetching            Threads reserved by SafeSquid, to service pre-fetching demands. Example> Log line1 reports that at present 0 thread is used for pre-fetching.

  Threading Errors                            Total number of events when SafeSquid could not produce a thread due to system failure or MAXTHREADS limitation.
                                              Example> Log line1 reports that since start of the process 0 threading errors occurred.

  Outbound Connections created                Total New connections created by SafeSquid to various remote webservers to service a client request.
                                              Example> Log line1 shows total 13640 new connections created by SafeSquid.

  Outbound Connections Failed                 Total Number of Events since the start of the process, when SafeSquid failed to create a connection to various remote webservers to service a client request. Example> Log line1 shows total 975 failed outbound connections.

  Outbound Connection Pool Reused             After handling request from client, connections are kept/stored in connection pool in waiting state. These connections are been reused so that additional burden on server of creating too many connections on server be lower down. Total reused connection till current time.
                                              Example> Log line1 shows 20650 outbound connections are been reused from connection pool from last 1603 seconds.

  Outbound Connections in Pool                Total number of Outbound connections idling in Connection Pool. Example> Log line1 shows 139 outbound connections idling in pool.

  Bytes in (KBytes)                           Total number of KiloBytes received by SafeSquid since the start of the process.
                                              Example> Log line1 shows 1853191 Kilobytes has been received from server since the start of the process.

  Bytes Out (KBytes)                          Total number of KiloBytes sent by SafeSquid since the start of the process.
                                              Example> Log line1 shows 2012552 Kilobytes has been sent by SafeSquid since start of the process.

  Caching Objects Created in Memory           Total number of Cached Objects created by SafeSquid in memory since the start of the process.
                                              Example> Log line1 shows 0 caching objects created in memory.

  Caching Objects Removed from Memory         Total number of Cached Objects removed by SafeSquid from memory since the start of the process.
                                              Example> Log line1 shows 0 caching objects removed from memory.

  DNS Queries Reused                          Total number of DNS queries to fulfill client request that are previously used and saved in DNS cache.
                                              Example> Log line1 shows 11317 DNS queries are reused from DNS cache since start of the process.

  New DNS Queries                             Total number of successful DNS queries to fulfill client requests.
                                              Example> Log line1 shows 3185 DNS queries are reused from DNS cache since start of the process.

  DNS Query failures                          Total number of events when SafeSquid successfully failed to do a DNS lookup since the start of the process.
                                              Example> Log line1 shows 41 DNS query fails since start of the process.

  Total System Memory (KBytes)                Total system memory of server where SafeSquid is installed. Example> Log line1 indicates server has 5976008 KB(i.e. 6 GB) of RAM.

  Free System Memory (KBytes)                 Current Free system memory of server where SafeSquid is installed. Example> Log line1 indicates free system memory when log captured was 2389076 KB(i.e. 2.38 GB).

  SafeSquid Virtual Memory (KBytes)           Current Virtual memory of server where SafeSquid is installed. Example> Log line1 shows server has 596224 KB virtual memory.

  SafeSquid Resident Memory (KBytes)          Current Resident memory of server where SafeSquid is installed. Or The size of the SafeSquid process resident in physical memory.
                                              Example> Log line1 shows server has 98868 KB resident memory.

  SafeSquid Shared Memory (KBytes)            Current shared memory of server where SafeSquid is installed. The memory shared with other processes other than SafeSquid i.e. memory mapped both by SafeSquid process and other process (such as shared libraries or other helping executables and libraries).
                                              Example> Log line1 indicates 4204 KB shared memory.

  SafeSquid Code Memory (KBytes)              Total SafeSquid Code Memory in the text format. Example> Log line1 indicates 2472 KB of code is written in SafeSquid.

  SafeSquid Data Memory (KBytes)              Memory that is been used by SafeSquid in the server. The size of the SafeSquid process i.e. the size of loaded executable code of SafeSquid.
                                              Example> Log line1 shows 0 bytes of data memory used.

  SafeSquid Library Memory (KBytes)           Total memory used by SafeSquid helping Libraries. Example> Log line1 shows 472172 Kbytes of memory used by SafeSquid libraries.

  Connections Handled Delta                   Difference between two consecutive connection handled entries i.e. [present number of connection handled  - previous entry connection handled].
                                              Example> Log line2 shows Connections Handled Delta  =  21170 - 21151  => 19

  Connections Closed Delta                    Difference between two consecutive connection closed entries i.e. [Number of connection closed - previous entry connection closed].
                                              Example> Log line2 shows Connections Closed Delta  =  20972 - 20941   => 31

  Transactions Handled Delta                  Difference between two consecutive total transactions handled this can be determined by client ID i.e. [current entry transaction handled - previous entry transaction handled]. Example> Log line2 shows Transactions Handled Delta  =  44346 - 44316  => 30

  Client Pool Delta                           Difference between two consecutive client pool entries i.e. [present connections in pool waiting state - previous entry pool having connection waiting]. Example> Log line2 shows Client Pool Delta  = 132 - 119  => 13

  Spare Threads Delta                         Difference between two consecutive unused threads entry i.e. [current unused threads  - previous entry unused threads].
                                              Example> Log line2 shows Spare Threads Delta  = 8016 - 8016  => 0

  Active Threads Delta                        Difference between two consecutive entries active threads i.e. [current active threads  - previous entry active threads].
                                              Example> Log line2 shows Active Threads Delta  = 66 - 91  => -25

  Threads Waiting Delta                       Difference between two consecutive entries waiting threads i.e. [current waiting threads  - previous entry waiting threads].
                                              Example> Log line2 shows Threads Waiting Delta  = 93 - 68  => 25

  Threads Starting up Delta                   Difference between two consecutive entries startup/special threads i.e. [current special threads running - previous entry special threads running].
                                              Example> Log line2 shows Threads Starting up Delta  = 17 - 17  => 0

  Threads Prefetching Delta                   Difference between two consecutive entries prefetching threads running i.e. [present number of threads used for prefetching - previous entry prefetch threads used]. Example> Log line2 shows Threads Prefetching Delta  => 0

  Threading Errors Delta                      Difference between two consecutive entries count of threads having error i.e. [total threads having error reported - previous entry error reported thread]. Example> Log line2 shows Threading Errors Delta  => 0

  Outbound Connections created Delta          Difference between two consecutive entries where new connections are been created i.e. [count of new connections created  - previous entry having count of new connections created].
                                              Example> Log line2 shows Outbound Connections created Delta  = 13654 - 13650  => 14

  Outbound Connections Failed Delta           Difference between two consecutive entries where connections failed to complete the request i.e. [Failed connections count - failed connections count]. Example> Log line2 shows Outbound Connections Failed Delta  = 976 - 975  => 1

  Outbound Connection Pool Reused Delta       Difference between two consecutive entries where pooled connections are been reused i.e. [connections reused from pool now  - connections reused from pool 2 seconds before].
                                              Example> Log line2 shows Outbound Connection Pool Reused Delta  = 20660 - 20650  => 10

  Outbound Connections in Pool Delta          Difference between two consecutive entries total number of pooled connections i.e. [connections in pool waiting at present - connections in pool before 2 seconds waiting].
                                              Example> Log line2 shows Outbound Connections in Pool Delta  = 139 - 139  => 0

  Bytes in (KBytes) Delta                     Difference between two consecutive entries total data received in Kilobytes from server i.e. [Data[KB] received from server - Data[KB] received from server 2 seconds before]. Example> Log line2 shows Bytes in Delta  = 1854126 - 1853191  => 935 KBytes

  Bytes Out (KBytes) Delta                    Difference between two consecutive entries total data send in Kilobytes from client i.e. [Data[KB] send to server - Data[KB] send to server 2 seconds before]. Example> Log line2 shows Bytes Out Delta  = 2014492 - 2012552  => 1940

  Caching Objects Created in Memory Delta     Difference between two consecutive entries total caching objects created in memory i.e. [total caching objects created - total caching objects created 2 seconds before]. Example> Log line2 shows Caching Objects Created in Memory Delta  => 0

  Caching Objects Removed from Memory Delta   Difference between two consecutive entries total caching objects removed from memory i.e. [total caching objects removed at present - total caching objects removed 2 seconds before]. Example> Log line2 shows Caching Objects Removed from Memory Delta  => 0

  DNS Queries Reused Delta                    Difference between two consecutive entries total DNS queries used from DNS cache i.e. [total DNS queries used from cache at present - total DNS queries used from cache 2 seconds before]. Example> Log line2 shows DNS Queries Reused Delta  = 11328 - 11317  => 11

  New DNS Queries Delta                       Difference between two consecutive entries new DNS queries fired by SafeSquid i.e. [new DNS queries fired at present - new DNS queries 2 seconds before]. Example> Log line2 shows New DNS Queries Delta  = 3186 - 3185  => 1

  DNS Query failures Delta                    Difference between two consecutive entries of the DNS failure count i.e. [DNS queries failure count at present - DNS queries failure count 2 seconds before]. Example> Log line2 shows DNS Query failures Delta  => 0

  load avg.(1 min)                            1 Minute System load average when SafeSquid printed this record. Example> Log line2 shows 0.23 of 1 minute load average

  load avg.(5 min)                            5 Minute System load average when SafeSquid printed this record. Example> Log line2 shows 0.21 of 5 minute load average

  load avg.(15 min)                           15 Minute System load average when SafeSquid printed this record. Example> Log line2 shows 0.49 of 15 minute load average

  Running Processes                           Total of all SafeSquid Running Processes using CPU time when SafeSquid printed this record. Example> Log line2 shows only 1 running process

  Waiting Processes                           Total of all SafeSquid Waiting Processes waiting for CPU time when SafeSquid printed this record. Example> Log line2 shows 562 Waiting Processes

  User Time                                   User time is the amount of CPU time spent in user-mode code (outside the kernel) within the process. i.e. actual CPU time consumed by SafeSquid processes. Example> Log line2 shows Cumulated CPU time consumed by SafeSquid processes is 60.000000

  System Time                                 System time is the amount of CPU time spent in the kernel within the process. This means executing CPU time spent in system calls within the kernel, as opposed to library code, which is still running in user-space. Like 'user', this is only CPU time used by the process.
                                              Example> Log line2 shows system time consumed by SafeSquid processes is 56.000000

  Total (user + system) Time                  User + System will tell you how much actual CPU time your process used. Note that this is across all CPUs, so if the process has multiple threads it could potentially exceed the wall clock time reported by Real. Note that in the output these figures include the User and System time of all child processes as well, although the underlying system calls return the statistics for the process and its children separately.
                                              Example> Log line2 shows Cumulated Total of CPU Time consumed due to SafeSquid processes is 116.000000

  User Time Delta                             Difference between two consecutive entries of total user time i.e. [CPU time used by SafeSquid at present - CPU time used by SafeSquid before 2 seconds]. Example> Log line2 shows User Time Delta = 0.000000

  System Time Delta                           Difference between two consecutive entries of total system time i.e. [CPU time used by SafeSquid at present  - CPU time used by SafeSquid before 2 seconds]. Example> Log line2 shows System Time Delta = 0.000000

  Total Time Delta                            Difference between two consecutive entries of total (system + user) time i.e. [Present (user+system) time used by SafeSquid - (user+system) time used by SafeSquid before 2 seconds]. Example> Log line2 shows Total Time Delta = 0.000000
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Performance Plot**

From the interface go to the Support page; open the **Performance Plot** tab, select two time intervals to generate the performance plot for that range.

See More about [How to generate the Performance Plot ](/docs/Audit_Forensics/Performance_Plot/)

### Bypass logs

Bypass logs contain the details related to the execution of bypass privilege granted to any user. When users with bypass privilege, execute their privilege to access a web-site that is not explicitly allowed, it is recorded in the bypass logs. It also records the users' opinions about the site, and the URLs that were additionally bypassed, to present a seamless experience.

**FORMAT / LEGEND**:

"TimeStamp"    "Action"    "User    "Referrer.Domain"    "Requested.Domain"    "From/Referral/URL"    "Method"    "Requested/URL"    "Categories,Applied"    "Suggested,Categories"

**Example Log Line1**:
**"2018.09.12:21:07:11"    "NOT BYPASSED"    "anonymous@192.168.0.24"    "microsoft.com"    "optimizely.com"    "https://powerbi.microsoft.com/"    "POST"    "[https://logx.optimizely.com:443/v1/events](https://logx.optimizely.com/v1/events)"    "business,computersandsoftware"    "-"**

**Example Log Line2**:
**"2018.09.12:21:07:51"    "HOST ADDED"    "anonymous@192.168.0.24"    "microsoft.com"    "optimizely.com"    "https://powerbi.microsoft.com/"    "POST"    "[https://logx.optimizely.com:443/v1/events](https://logx.optimizely.com/v1/events)"    "business,computersandsoftware"    "test"**

The details of the fields in bypass.log are as follows:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Field**              **Explanation**
  ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  TimeStamp              The date and time when the user with bypass privilege accessed a web-site that is not explicitly allowed. The fields in the date/time field are [YYYY.MM.DD:hh:mm:ss], where the fields are defined as  follows:
                         DD is the day of the month, MMM is the month, YYYY is the year, hh is the hour, mm is the minute, ss is the seconds.
                         Example> 2018.09.12:21:07:11

  Action                 Action taken by User to either block or bypass the cookie for current URL (either host or referer). User can also re-categorize the current URL into predefined categories. Example> NOT BYPASSED

  User                   The User is annotating as username@clientip used by the client for authentication. If no value is present, "anonymous" is substituted.
                         Example> anonymous@192.168.0.24

  Referrer.Domain        Domain name of the referrer URL that referred the user to the resource requested. "-" is substituted when there are no referrers.
                         Example> microsoft.com

  Requested.Domain       Domain name of the requested web-server. Example> optimizely.com

  From/Referral/URL      From/Referrer/URL is the URL of the HTTP resource that referred the user to the resource requested. "-" is substituted when there are no referrer URL.
                         Example> https://powerbi.microsoft.com/

  Method                 A method is part of HTTP request sent by client to the server. Example> POST

  Requested/URL          Requested/URL is reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.
                         Example> [https://logx.optimizely.com:443/v1/events](https://logx.optimizely.com/v1/events)

  Categories,Applied     Comma separated list of categories that were applied to the request. "_" is substituted when no categories are applied.
                         Example> business,computersandsoftware

  Suggested,Categories   Comma-separated list of categories suggested for the request to access. "_" is substituted when no categories are suggested. Log line2 is printed after the requested URL is given access with suggestion of re-categorization.
                         Example> test
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Privacy logs

Privacy Logs are used to record incidences of cookies, and queries going to third-party web sites.
Privacy log captures incidences of third-party web-sites when a user accesses a web-site, and action taken by elevated privacy.

**FORMAT / LEGEND**:

YYYY/mm/DD:HH:MM:SS    ClientID    username@IP    HTTP-REFERRER    METHOD    URL    [USER_AGENT]    action

The details of the fields in privacy.log are as follows:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Field**               **Explanation**
  ----------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  YYYY/mm/DD: HH:MM: SS   Time when SafeSquid generated this record and stored in privacy log. SafeSquid begins printing of each record on a new line with the first column as the TimeStamp in YYYY/mm/DD: HH:MM: SS format.

  ClientID            The internal SafeSquid ID associated with the present/ongoing connection.

  username@IP             The username@IP(or user ID) used by the client for authentication. If no value is present, "anonymous" is substituted.

  HTTP-REFERRER           An HTTP header field that identifies the address of the age that linked to the resource being requested. "-" is substituted when there is no referrer in HTTP header field.

  METHOD                  A method is part of HTTP request sent by client to the server.

  URL                     An HTTP url is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.

   [USER_AGENT]         User agent is the client which initiates a request. Useraagent are often browsers, editors, spiders(web-traversing robots), or other end user tools.

  action                  Action is the privacy level applied to the request.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



## SafeSquid activity log written in system logs

The path to these log files is as follows:

  -----------------------------------------------------------------------
  Log File                    Path
  --------------------------- -------------------------------------------
  **Monit Log**               **/var/log/monit.log**

  **Syslog**                  **/var/log/syslog**
  -----------------------------------------------------------------------

### Monit log

SafeSquid Uses Monit service for managing and monitoring its process. Monit service is particularly useful for monitoring daemon processes, such as those started at system boot time. While Monit service is running and if SafeSquid process is terminated either manually or automatically then SafeSquid will be restarted. Also, Monit service plays a crucial role when user want to modify any startup parameter or upgrade the SafeSquid version.

**FORMAT**:

[date] priority : message

**Example Log Lines**:
**[IST Jan 20 13:08:37] info     : 'safesquid' trying to restart
[IST Jan 20 13:08:37] info     : 'safesquid' start: /etc/init.d/safesquid
[IST Jan 20 13:08:40] error    : 'safesquid.dns.conf' timestamp was changed for /usr/local/safesquid/security/dns/safesquid.dns.conf
[IST Jan 20 13:08:40] info     : 'safesquid.dns.conf' exec: /bin/bash
[IST Jan 20 13:08:40] error    : 'upgrade' timestamp was changed for /tmp/safesquid/upgrade
[IST Jan 20 13:08:40] info     : 'upgrade' exec: /bin/bash
[IST Jan 20 13:08:40] error    : 'safesquid.ldb' file doesn't exist
[IST Jan 20 13:08:40] info     : 'safesquid.ldb' trying to restart
[IST Jan 20 13:08:43] error    : 'Logs' space usage 86.9% matches resource limit [space usage>5.0%]
[IST Jan 20 13:08:43] info     : 'safesquid' process is running with pid 1815
[IST Jan 20 13:08:43] error    : 'named' process PID changed from 1170 to 1891
[IST Jan 20 13:08:43] info     : 'safesquid.dns.conf' timestamp was not changed for /usr/local/safesquid/security/dns/safesquid.dns.conf
[IST Jan 20 13:08:43] info     : 'upgrade' timestamp was not changed for /tmp/safesquid/upgrade**

### Syslog

Linux's syslog service provides a highly configurable logging system. Some messages triggered by SafeSquid application are been stored in syslog. Syslog is a standard log for sending and receiving notification messages--in a particular format--from various network devices. The messages include time stamps, event messages, severity, host IP addresses, diagnostics and more.
Syslog was designed to monitor network devices and systems to send out notification messages if there are any issues with functioning--it also sends out alerts for pre-notified events and monitors suspicious activity via the change log/event log of participating network devices.
You will find log lines of SafeSquid application in the syslog file.

**Example Log Lines**:
**2020 01 20 14:25:08 [-1] init: Startup Log: /var/log/syslog
2020 01 20 14:25:08 [-1] init: safesquid: start called
2020 01 20 14:25:08 [-1] init: USER: ssquid exists
2020 01 20 14:25:08 [-1] init: ssquid: checking for group membership: root
2020 01 20 14:25:08 [-1] init: ssquid: has group memberships: root
2020 01 20 14:25:08 [-1] init: ssquid: is member of group: root
2020 01 20 14:25:08 [-1] init: export MALLOC_CHECK_=2
2020 01 20 14:25:08 [-1] init: debug: invoking tcp_tune
2020 01 20 14:25:08 [-1] init: RAMDEVICE /dev/ram1 does not exist, and therefore cannot be used
2020 01 20 14:25:08 [-1] init: LIBS_DIR: /opt/safesquid/libs no preload libraries found
2020 01 20 14:25:08 [-1] init: validating: OPT_DIR:/opt/safesquid with permissions ug=rwX,o=r
2020 01 20 14:25:08 [-1] init: already exists: OPT_DIR:/opt/safesquid
2020 01 20 14:25:08 [-1] init: SET_PERMISSION: OPT_DIR:/opt/safesquid ug=rwX,o=r
2020 01 20 14:25:08 [-1] init: validating: USR_LOCAL_DIR:/usr/local/safesquid with permissions ug=rwX,o=r
2020 01 20 14:25:08 [-1] init: already exists: USR_LOCAL_DIR:/usr/local/safesquid
2020 01 20 14:25:08 [-1] init: SET_PERMISSION: USR_LOCAL_DIR:/usr/local/safesquid ug=rwX,o=r
2020 01 20 14:25:08 [-1] init: validating: TMP_DIR:/tmp/safesquid with permissions ug=rwX,o=r
2020 01 20 14:25:08 [-1] init: already exists: TMP_DIR:/tmp/safesquid
2020 01 20 14:25:08 [-1] init: SET_PERMISSION: TMP_DIR:/tmp/safesquid ug=rwX,o=r**


https://help.safesquid.com/portal/en/kb/articles/identify-the-filter-by-using-safesquid-extended-logs-or-detailed-logs
https://help.safesquid.com/portal/en/kb/articles/identify-the-filter-name-using-safesquid-detailed-logs-from-the-interface
https://help.safesquid.com/portal/en/kb/articles/forwarding-logs-to-the-siem-server-by-configuring-the-udp-port

