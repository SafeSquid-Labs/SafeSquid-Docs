---
title: SSO Authentication Fail
description: "Troubleshoot SSO authentication failures in SafeSquid: verify Kerberos, DNS stub zones, and bypass auth for unsupported apps."
keywords:
  - SafeSquid SSP fail
  - SSO authentication error
  - Kerberos troubleshooting
  - proxy authentication bypass
  - application login issues
---



## Troubleshooting
If your configuration is exactly like **How to** and still your SSO authentication failed. Check out the following:

1.  Make sure the **User Name**: is administrator@safesquid.test (**User name should be any user from AD having administrative permissions**)

2.  Monit service must be Up. Verify it using the command:

```bash
pidof monit
```
root@sabproxy:~# pidof monit
19940

3.  As soon as you Save policy by selecting NEGOTIATE_LDAP_AUTH
**kerberos.sh*** script will automatically run from path **/usr/local/safesquid/ui_root/cgi-bin**

a.  Verify below files at path**:/usr/local/safesquid/security**

**HTTP.keytab**

**krb5.conf**

 **krb.tkt**

b.  SafeSquid will create the stub zone for DNS resolution of your Active Directory server.

The file with stub zone will be created with the name: **safesquid.dns.conf**

At path**:/usr/local/safesquid/security/dns**

Run command:
```bash
cat safesquid.dns.conf
```
```
  -----------------------------------------------------------------------
  zone safesquid.test {
  type stub;
  masters {192.168.221.1;};
  };
  -----------------------------------------------------------------------
```
Also, it will automatically copy at given path**:/etc/bind/**
Run command:
```bash
cat safesquid.dns.conf
```
```
  -----------------------------------------------------------------------
  zone safesquid.test {
  type stub;
  masters {192.168.221.1;};
  };
  -----------------------------------------------------------------------
```
:::note
Note: Monit service must be up
:::
If any one of the above entries missing you have to repeat all the steps.

First, remove all the given files from the above-given path.

Start monit service and repeat all the steps and capture logs

Command:
```bash
tail -F /var/log/safesquid/native/safesquid.log
```
4.  Go to Access Restriction > GLOBAL >> SSO: TRUE
5.  ALLOW List: Policy with PAM: TRUE
6.  **Testing SSO Auth**

    a.  Go to the Windows machine which joins in the domain of AD e.g windows7.safesquid.test
    b.  Go to the browser and set PROXY as FQDN of the proxy server (sabproxy.safesquid.test)
    c.  Access any website (Authentication prompt should not come)
    d.  Open extended logs

```bash
tail -F /var/log/safesquid/extended/extended.log
```
find username@SAFESQUID.TEST@ 192.168.221.212 (IP address of Windows machine which is in the domain)

