---
title: "SSO Authentication Fail"
description: "Diagnose and resolve SafeSquid sso authentication fail incidents with causes, recovery actions, and audit evidence."
keywords: ["troubleshooting", "SafeSquid", "sso authentication fail"]
---

# SSO Authentication Fail

SSO Authentication Fail can interrupt web access, policy enforcement, or evidence collection. Use this runbook to restore service, preserve logs, and prove the corrective action during security review.

If your configuration is exactly like **How to** and still your SSO authentication failed. Check out the following:

1. Make sure the **User Name**: is [administrator@safesquid.test](mailto:administrator@safesquid.test) (**User name should be any user from AD having administrative permissions**)
2. Monit service must be Up. Verify it using the command:

```text
pidof monit
```

root@sabproxy:~# pidof monit 19940

1. As soon as you Save policy by selecting NEGOTIATE\_LDAP\_AUTH **kerberos.sh**\* script will automatically run from path **/usr/local/safesquid/ui\_root/cgi-bin**

a. Verify below files at path\*\*:/usr/local/safesquid/security\*\*

**HTTP.keytab**

**krb5.conf**

**krb.tkt**

b. SafeSquid will create the stub zone for DNS resolution of your Active Directory server.

The file with stub zone will be created with the name: **safesquid.dns.conf**

At path\*\*:/usr/local/safesquid/security/dns\*\*

Run command:

```text
cat
 safesquid.dns.conf
```

```text
  -----------------------------------------------------------------------
  zone safesquid.test {
  type stub;
  masters {192.168.221.1;};
  };
  -----------------------------------------------------------------------
```

Also, it will automatically copy at given path\*\*:/etc/bind/\*\* Run command:

```text
cat
 safesquid.dns.conf
```

```text
  -----------------------------------------------------------------------
  zone safesquid.test {
  type stub;
  masters {192.168.221.1;};
  };
  -----------------------------------------------------------------------
```

Note: Monit service must be up

If any one of the above entries missing you have to repeat all the steps.

First, remove all the given files from the above-given path.

Start monit service and repeat all the steps and capture logs

Command:

```text
tail
 
-F
 /var/log/safesquid/native/safesquid.log
```

1. Go to Access Restriction \> GLOBAL \>\> SSO: TRUE
2. ALLOW List: Policy with PAM: TRUE
3. **Testing SSO Auth** a. Go to the Windows machine which joins in the domain of AD e.g windows7.safesquid.test b. Go to the browser and set PROXY as FQDN of the proxy server (sabproxy.safesquid.test) c. Access any website (Authentication prompt should not come) d. Open extended logs

```text
tail
 
-F
 /var/log/safesquid/extended/extended.log
```

find [username@SAFESQUID.TEST](mailto:username@SAFESQUID.TEST)@ 192.168.221.212 (IP address of Windows machine which is in the domain)

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