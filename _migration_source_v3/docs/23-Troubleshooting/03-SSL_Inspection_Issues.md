---
title: SSL Certification Errors
description: "Identify and fix SSL certificate errors in SafeSquid: connection failures, zero-byte certificates, DNS mismatches, and HTTPS inspection issues."
keywords:
  - SSL certificate error
  - HTTPS inspection issue
  - SafeSquid certificate troubleshooting
  - secured connection fail
  - domain mismatch SSL
---



## SSL certificate and inspection issues

| Symptom | Likely cause | Resolution | Verification |
|--------|---------------|------------|--------------|
| Browser shows "Your connection is not private" after certificate import | HTTPS Inspection policies not configured correctly | Configure Enforce SSL scanning and Bypass rules in **Configure** → **Real-time content security** → **HTTPS Inspection** | Reload HTTPS site; confirm no certificate warning |
| youtube.com (or one site) fails; other HTTPS sites work | Global subsection not set to Enabled TRUE | Set **HTTPS Inspection** → **Global** → **Enabled** to TRUE | Access the previously failing site |
| "Secured connection fail" after certificate installed in browser | Passphrase mismatch or password encryption failed | Re-enter correct passphrase; ensure password encryption step completed | Retry HTTPS; confirm connection succeeds |
| Certificate file downloaded with 0 bytes | Certificate downloaded without password encryption | Download certificate with encryption enabled in Self-Service Portal | Check file size; re-import in browser |
| ERROR S_X509_DNS_MISMATCH or "SSL Certificate has DNS errors" | Stale or wrong cert in SafeSquid SSL cache | Remove affected site from **SSL Certs/Cache** or clear `/var/db/safesquid/ssl/certs` for that host | Retry connection; check logs for ssl_ctx:NULL or failed reading key |
| Some HTTPS sites work, others do not | Mixed cert or cache state after key/cert change | Clear SSL cache; remove old activation key data; ensure new cert deployed to clients | Test previously failing and working sites |

**Details (numbered items):**

1.  When the SSL certificate is imported into the Chrome browser and the browser still shows **Your connection is not private** (or similar) for HTTPS sites.

->Policies in the HTTPS Inspection subsection may not be configured correctly.

2.  While the **successful configuration of HTTPS Inspection**, accessing youtube.com shows an error while all other HTTPS sites work fine.

->In the HTTPS inspection section, if the Global subsection is not set to Enabled as TRUE then this problem may arise.

3.  While the SafeSquid certificate is installed inside the browser however HTTPS sites show the error **Secured connection fail**.

->Either passphrases were not matched or Password encryption failed due to inappropriate input being given.

4.  SSL certificate downloaded with size 0 bytes.

->When the certificate is downloaded without encryption of the password then the certificate will be downloaded with 0 bytes.

5.  Displaying ERROR "SSL Connection to webmail.safesquid.net:2096 denied S_X509_DNS_MISMATCH: SSL Certificate has DNS errors."

->Remove HTTPS websites from SSL Certs/Cache when **Secured connection fails** appears on HTTPS websites.

6.  Or some of the **HTTPS websites are working without error** but some of the **HTTPS websites are not working**.



## Troubleshooting
### Verify SSL certificate import in browser
Follow [Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) and [Import certificate into Firefox](/docs/SSL_Inspection/Configure_HTTPS_Inspection/#import-certificate-into-firefox) or Chrome/IE.

### Case 2: Check SSL certs/cache for these symptoms
SafeSquid certificate is imported in the browser but a secured connection still fails when accessing HTTPS websites. Some HTTPS sites work while others do not. After removing the old activation key, installing a new key, and configuring the new SSL certificate, clear SSL cache if issues persist.

Native Logs

2018 03 17 10:15:38.084 [119] network: IP:192.168.0.10 fd:20 normal client disconnected after making 1 requests

2018 03 17 10:15:38.084 [119] warn: advice: [IP:192.168.0.10] process: transfer failed

2018 03 17 10:15:38.084 [119] error: ssl: ClientEncrypt: failed encryption :anonymous@192.168.0.10 for www.irctc.co.in:443

2018 03 17 10:15:38.083 [119] error: ssl: EncryptC:987 ssl_ctx:NULL

**2018 03 17 10:15:38.083 [119] error: ssl: failed : reading key from /var/db/safesquid/ssl/certs/irctc.co.in/www.irctc.co.in**

When facing the above issues, remove all HTTPS website data from **/var/db/safesquid/ssl**

Run the below command and check for the file

```
cd /var/db/safesquid/ssl
```
root@sabproxy:/var/db/safesquid/ssl# ll

total 24

drwxrwxr-- 6 ssquid root 4096 Jul 28 17:06 ./

drwxrwxr-- 7 ssquid root 4096 Jul 28 17:06 ../

drwxrwxr-- 2 ssquid root 4096 Aug 10 13:34 badcerts/

drwxrwxr-- 29 ssquid root 4096 Sep 2 16:27 certs/

drwxrwxr-- 2 ssquid root 4096 Jul 28 17:06 goodcerts/

drwxrwxr-- 2 ssquid root 4096 Jul 28 17:06 serials/

root@sabproxy:/var/db/safesquid/ssl# cd certs/

root@sabproxy:/var/db/safesquid/ssl/certs#rm -rf *

Repeat the above step for **goodcerts**/ and **badcerts**/ **and access those websites from the browser.**

### S_X509_DNS_MISMATCH: SSL certificate has DNS errors

When the browser shows "S_X509_DNS_MISMATCH: SSL Certificate has DNS errors" via proxy despite a correct certificate in the browser, the origin website's certificate is broken. SafeSquid stores such sites under **/var/db/safesquid/ssl/badcerts/**. Locate the domain in that path.

Go to that domain name folder by command:
```
cd domain-name
```
The FQDN for that website is in that folder (e.g. webmail.safesquid.net). Open the FQDN file with **vi FQDN** (e.g. vi webmail.safesquid.net).

Here you should find mismatch domain name

root@dev:~# cd /var/db/safesquid/ssl/

root@dev:/var/db/safesquid/ssl# ll

total 52

drwxrwxr-- 2 ssquid root 4096 Jul 4 2017 serials

drwxrwxr-- 2 ssquid root 4096 Mar 9 16:30 goodcerts

**drwxrwxr-- 71 ssquid root 4096 Mar 9 16:45 badcerts**

drwxrwxr-- 1022 ssquid root 36864 Mar 12 12:16 certs

root@dev:/var/db/safesquid/ssl# cd badcerts/

root@dev:/var/db/safesquid/ssl/badcerts# ll

total 276

drwxrwxr-- 2 ssquid root 4096 Mar 8 12:07 1rx.io

drwxrwxr-- 2 ssquid root 4096 Mar 8 12:32 ravenad.com

drwxrwxr-- 2 ssquid root 4096 Mar 8 15:36 microsoft.com

drwxrwxr-- 2 ssquid root 4096 Mar 8 16:04 indiatimes.com

drwxrwxr-- 2 ssquid root 4096 Mar 8 19:08 quoracdn.net

drwxrwxr-- 2 ssquid root 4096 Mar 9 15:25 iis.net

**drwxrwxr-- 2 ssquid root 4096 Mar 9 16:27 safesquid.net**

root@dev:/var/db/safesquid/ssl/badcerts# cd safesquid.net/

root@dev:/var/db/safesquid/ssl/badcerts/safesquid.net# ll

total 8

**-rw-rw-r-- 1 ssquid root 5904 Mar 9 15:43 webmail.safesquid.net**

root@dev:/var/db/safesquid/ssl/badcerts/safesquid.net# vi webmail.safesquid.net

---

**S_X509_DNS_MISMATCH: SSL Certificate has DNS errors**.

---

Certificate:

Data:

Version: 3 (0x2)

Serial Number:

f8:bd:5e:60:3d:26:db:5d:1a:c0:6a:05:92:ee:c7:81

Signature Algorithm: sha256WithRSAEncryption

Issuer: C=US, ST=TX, L=Houston, O=cPanel, Inc., CN=cPanel, Inc. Certification Authority

Validity

Not Before: Jul 23 00:00:00 2017 GMT

Not After : Jul 23 23:59:59 2018 GMT

Subject: OU=Domain Control Validated, OU=PositiveSSL, **CN=alpha.surebrowse.net**

Subject Public Key Info:

Public Key Algorithm: rsaEncryption

Public-Key: (2048 bit)

To allow domain mismatch errors for specific HTTPS websites, create a policy:

![Creating a new policy in request types under custom settings section](/img/Troubleshooting/SSL_certification_errors/image1.webp)

![Creating a policy by adding all the required values ](/img/Troubleshooting/SSL_certification_errors/image2.webp)

![Creating a new policy in Access profiles section](/img/Troubleshooting/SSL_certification_errors/image3.webp)

![adding the required values](/img/Troubleshooting/SSL_certification_errors/image4.webp)

![Clicking on Inspection policies in HTTPS inspection under Real time content security section](/img/Troubleshooting/SSL_certification_errors/image5.webp)

![Creating a new policy ](/img/Troubleshooting/SSL_certification_errors/image6.webp)

![showing settings to configure a security policy, allowing "block domain mismatch in the website ssl certificate"](/img/Troubleshooting/SSL_certification_errors/image7.webp)

![moving up the created policy just above the last policy](/img/Troubleshooting/SSL_certification_errors/image8.webp)

![saving configuration globally](/img/Troubleshooting/SSL_certification_errors/image9.webp)



## Verification and Evidence

- **Interface Checks**: Confirm the SafeSquid Root CA is installed in the browser trust store ([Import Certificate into Chrome or IE](/docs/SSL_Inspection/Import_Certificate_Chrome_IE/)). In Configuration Portal, HTTPS Inspection policies match the intended bypass/enforce rules; SSL Certs/Cache cleared if DNS mismatch was the issue.
- **Log Analysis**: Native logs show successful client encryption for previously failing domains; no `S_X509_DNS_MISMATCH` or transfer failed errors for the fixed cases.
- **Performance Validation**: Previously failing HTTPS sites load without "connection not secured" or "secured connection fail"; YouTube and other sites work per policy.



## Next steps

- [Configure HTTPS Inspection](/docs/SSL_Inspection/Configure_HTTPS_Inspection/) for setup and bypass rules.
- [Import Certificate into Chrome or IE](/docs/SSL_Inspection/Import_Certificate_Chrome_IE/) for client certificate import.
- [Troubleshooting](/docs/Troubleshooting/main/) for other diagnostic guides.

