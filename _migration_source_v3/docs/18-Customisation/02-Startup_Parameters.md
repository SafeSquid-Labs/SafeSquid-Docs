---
title: Startup Parameters
description: Configure SafeSquid startup parameters (LISTEN_IP, MASTER_IP, LOG_LEVEL, threading) for performance and reliability.
keywords:
  - SafeSquid configuration
  - proxy server tuning
  - SafeSquid LISTEN_IP
  - LOG_LEVEL settings
---



## Startup parameters control proxy behavior and tuning
SafeSquid loads default configuration/startup parameters from the startup.ini file. You can modify the startup parameter values from SafeSquid GUI. Modified values of startup parameters are stored in **/opt/safesquid/startup.ini** file.

SafeSquid loads default setup parameters from the setup.ini file. To modify setup parameters, you should take a copy of the setup.ini file and store it as **/opt/safesquid/setup.ini** before editing it manually.



## Startup Parameters
| **Field**                     | **Explanation** |
|--------------------------------|---------------|
| **LISTEN_IP**                  | A proxy server acts as an intermediate/bridge between the internet and the user's computer. The socket on which SafeSquid should bind, and then serve is LISTEN_IP. LISTEN_IP is the IP address that listens for incoming TCP connections. The default value for LISTEN_IP is "*" which allows SafeSquid to bind the instance to more than one IP address. |
| **LISTEN_PORT**                | LISTEN_PORT is an HTTP port that will listen for all incoming requests in the SafeSquid proxy. SafeSquid instance binds on LISTEN_IP: LISTEN_PORT and serves the request. The default value for LISTEN_PORT is 8080. |
| **MASTER_IP**                  | MASTER_IP is an IP address of a Master server in a Master-Slave settings/configuration. Master-Slave settings/configuration is generally used to ensure automatic synchronization of policies among various clustered services, or even remote proxy servers. SafeSquid can be invoked as a Slave and can be configured to synchronize and fetch configuration parameters and policies from a remote-based SafeSquid Master server. The default value for MASTER_IP is "" which is for standalone proxy service. |
| **MASTER_PORT**                | MASTER_PORT is an HTTP port that along with MASTER_IP is used for Master-Slave settings/configuration. The default value for MASTER_PORT is "". For standalone proxy service always keep MASTER_IP and MASTER_PORT blank. |
| **SEND_SOCKET_BUFFERS**        | The SafeSquid throughput can be boosted by TCP tuning of the socket buffers. Each network socket is allocated a send buffer for outbound packets and a receive socket for inbound packets. SEND_SOCKET_BUFFERS is used for tuning the outbound data buffer. The default value for SEND_SOCKET_BUFFERS is 131072. |
| **RECEIVE_SOCKET_BUFFERS**     | The SafeSquid throughput can be boosted by TCP tuning of the socket buffers. Each network socket is allocated a send buffer for outbound packets and a receive socket for inbound packets. RECEIVE_SOCKET_BUFFERS is used for tuning the inbound data buffer. The default value for RECEIVE_SOCKET_BUFFERS is 131072. |
| **TCP_KEEPIDLE_TIME**          | TCP_KEEPIDLE_TIME is the time (in seconds) to keep an idle TCP connection active. The default value for TCP_KEEPIDLE_TIME is 900. |
| **TCP_KEEPINTVL_TIME**         | TCP_KEEPINTVL_TIME is the interval between packets sent to validate the TCP connection. Default value for TCP_KEEPINTVL_TIME is 75. |
| **TCP_KEEPCNT_COUNTS**         | TCP_KEEPCNT_COUNTS is the number of keepalive probes to be sent before terminating the connection. The default value for TCP_KEEPCNT_COUNTS is 9. |
| **PASSWORD_CACHE_SIZE**        | SafeSquid provides an excellent Password Caching feature which is used to reduce the latency when authentication is desired from a remote authentication system. PASSWORD_CACHE_SIZE is the maximum number of password cache entries stored in memory. The default value for PASSWORD_CACHE_SIZE is 8111. |
| **PASSWORD_CACHE_EXPIRE_TIME** | PASSWORD_CACHE_EXPIRE_TIME is the time (in seconds) to keep the password cache entries in memory and clean the entry after the expiry time. The default value for PASSWORD_CACHE_EXPIRE_TIME is 3600 seconds. |
| **NEVER_SYNC**                 | The SafeSquid service when invoked as SLAVE fetches policies from a remote SafeSquid server. You can specify the section's name in a comma-separated format that need not be fetched from the Master instance for synchronization. The default value for NEVER_SYNC is "cache". |
| **ALWAYS_SYNC**                | The SafeSquid service when invoked as SLAVE fetches policies from a remote SafeSquid server. You can specify the section's name in a comma-separated format that should be fetched from the Master instance for synchronization. The default value for ALWAYS_SYNC is "". |
| **LOG_SIZE_LIMIT**             | LOG_SIZE_LIMIT is the size (in bytes) that specifies the maximum size of any log file, after which SafeSquid executes log rotation. The default value for LOG_SIZE_LIMIT is 524288000 in bytes. |
| **SYNCTIME**                   | SYNCTIME is the time (in seconds) after which the slave server will synchronize with the Master server by fetching policy configuration. The default value for SYNCTIME is 99 seconds. |
| **LOG_LEVEL**             | LOG_LEVEL is the numerical value that determines the details that will be logged in the log file, like REQUESTS, SECURITY, REDIRECT, etc. This parameter affects only the SafeSquid Native Log. You can control the verbosity of the Native log with this parameter. Selecting too many options could affect the size of the log file. The default value for LOG_LEVEL is 134217727. Note: For debugging set 268435455. ADVICE-0; REQUEST-1; NETWORK-2; LDAP-4; HEADER-8; INTERFACE-16; COOKIE-32; REDIRECT-64; TEMPLATE-128; TEXT_ANALYZER-256; REWRITE-512; LIMITS-1024; CACHE-2048; PREFETCH-4096; ICP-8192; FORWARD-16384; SYNC-32768; ANTIVIRUS-65536; EXTERNAL-131072; ICAP-262144; SSL-524288; CATEGORY-1048576; URLCOMMAND-2097152; MODULE-4194304; SECURITY-8388608; WARN-16777216; ERROR-33554432; PROFILES-67108864; DEBUG-134217728. |
| **PROCESS_OLD_LOGS**      | PROCESS_OLD_LOGS is the numeric value that specifies the activity to be done during Log Rotation. When the log file exceeds the LOG_SIZE_LIMIT, SafeSquid executes the Log Rotation process. If PROCESS_OLD_LOGS value is set to 0 then SafeSquid will just open a new log file and delete the earlier file. If PROCESS_OLD_LOGS value is set to 1 then SafeSquid will open a new log file and compress the earlier file with the current time-stamp. If PROCESS_OLD_LOGS value is set other than 0 and 1 then SafeSquid will open a new log file and rename the earlier file with the current time-stamp. The default value for PROCESS_OLD_LOGS is 1. |
| **STACKSIZE**             | STACKSIZE is the numeric value defined for the stack size of a thread created by SafeSquid. If STACKSIZE is specified as 20, then the SafeSquid executable will set the thread stack size to 2^20 i.e. 1024KB. For optimum use of memory, this value should be a multiple of page size. The default value for STACKSIZE is 21. |
| **MALLOC_CHECKING**       | This feature is not yet described. |
| **OVERLOAD_FACTOR**       | OVERLOAD_FACTOR is a numeric value used to dynamically control the number of connections held in the client pool. OVERLOAD_FACTOR along with MAXTHREADS strengthen SafeSquid's capability to deal with DDoS attacks or even when such conditions get developed unintentionally. The default value for OVERLOAD_FACTOR is 10. |
| **SOCKET_TIMEOUT**        | SOCKET_TIMEOUT is the minimum time (in seconds) a socket handle will be monitored by SafeSquid for a consecutive incoming request on an established connection. If the client-side application supports pipelining, the subsequent request will be handled with nearly zero latency. SafeSquid will additionally check for a socket's availability for 10 times the socket_timeout before considering it a dead socket. The default value for SOCKET_TIMEOUT is 6 seconds. |
| **THREAD_TIMEOUT**        | SafeSquid can use the same thread to handle consecutive connections. THREAD_TIMEOUT is the minimum time (in seconds) a thread is kept alive after serving a request, and can serve a new request immediately after serving the first request. Keeping a higher THREAD_TIMEOUT reserves virtual memory for a longer period but reduces the CPU overheads involved in the creation of a new thread. Keeping a lower THREAD_TIMEOUT releases virtual memory faster and may be beneficial if the environment requires a large number of concurrent threads while conserving virtual memory. The default value for THREAD_TIMEOUT is 10 seconds. |
| **HOSTNAME**              | HOSTNAME is your SafeSquid server hostname, the name by which the proxy's host or service name is referred. HOSTNAME is also used as the [realm] parameter for the authentication process. HOSTNAME can be configured even in the General Section of SafeSquid's run-time configuration. HOSTNAME can be set to the IP address if you intend to manage SafeSquid without setting it as your browser's proxy server. Note: If you intend this instance to be a part of a load-balanced clustered service, then ensure each instance participating in the cluster has a common HOSTNAME. The default value for HOSTNAME is "". |
| **DOMAIN**                | DOMAIN is the Domain Name for the SafeSquid server. A domain name represents an Internet Protocol (IP) resource, such as a personal computer used to access the Internet, a server computer hosting a website, or the website itself or any other service communicated via the Internet. The default value for DOMAIN is "". |
| **MAXTHREADS**                 | MAXTHREADS is a numeric value to define the maximum number of concurrent threads SafeSquid will open. The default value for MAXTHREADS is 8192. |
| **MAX_FDS**                    | MAX_FDS is a numeric value to define the maximum number of handles that can be used for input/output resources. The default value for MAX_FDS is 32768. |
| **EXTENDED_UDP_IP**            | EXTENDED_UDP_IP is the UDP IP to write extended logs on the UDP server. The default value for EXTENDED_UDP_IP is "". |
| **EXTENDED_UDP_PORT**          | EXTENDED_UDP_PORT is a UDP port to write extended logs on a UDP server. The default value for EXTENDED_UDP_PORT is "". |
| **NATIVE_UDP_IP**         | NATIVE_UDP_IP is the UDP IP to write native logs on the UDP server. SafeSquid will write native logs on the UDP server using UDP sockets when both NATIVE_UDP_IP and NATIVE_UDP_PORT are mentioned. The default value for NATIVE_UDP_IP is "". |
| **NATIVE_UDP_PORT**       | NATIVE_UDP_PORT is a UDP port to write native logs on the UDP server. SafeSquid will write native logs on the UDP server using UDP sockets when both NATIVE_UDP_IP and NATIVE_UDP_PORT are mentioned. The default value for NATIVE_UDP_PORT is "". |
| **CONFIG_UDP_IP**              | CONFIG_UDP_IP is the UDP IP to write config logs on the UDP server. The default value for CONFIG_UDP_IP is "". |
| **CONFIG_UDP_PORT**            | CONFIG_UDP_PORT is a UDP port to write config logs on the UDP server. The default value for CONFIG_UDP_PORT is "". |
| **REAL_TIME_DB_WRITE**         | REAL_TIME_DB_WRITE determines whether SafeSquid logs should be written in the SQLite database. If REAL_TIME_DB_WRITE is set to 1, real-time logs will be written. If set to 0, they will not be written. Default: 1. |
| **STATEMENT_COUNT**            | SafeSquid uses the STATEMENT_COUNT parameter to optimize writing into the SQLite database. STATEMENT_COUNT is the maximum number of log lines written into the database in one transaction. The default value of STATEMENT_COUNT is 100. |

:::note
You can tune up the SafeSquid for better results. You can modify Startup Parameters to obtain better performance by tweaking the overall system & application tuning. Quite a few users have experienced difficulties due to a lack of understanding of SafeSquid\'s configuration, and possibly due to insufficient documentation on the subject.
:::

