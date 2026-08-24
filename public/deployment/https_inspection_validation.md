---
title: HTTPS Inspection Validation
description: Prove SafeSquid is decrypting and inspecting HTTPS sessions rather than tunnelling them, using the certificate issuer as the positive test.
keywords:
  - SafeSquid HTTPS inspection test
  - verify SSL inspection
  - certificate issuer check
  - proxy TLS validation
  - deployment validation
---

# Prove HTTPS Is Inspected, Not Tunnelled

An HTTPS site that loads through the proxy proves nothing about inspection. SafeSquid can tunnel the session untouched and the page still renders perfectly — so the control appears to work while [malware scanning](/use_cases/malware_scanning/malware_scanners), [DLP](/use_cases/data_leakage_prevention/data_leakage_prevention), and content policy see nothing but an opaque stream.

The certificate issuer is the only reliable positive test. Everything else is a page that loaded.

## Validate prerequisites

Confirm:

- [Proxy Connectivity](/deployment/proxy_connectivity) passes for plain HTTP.
- The SafeSquid Root CA has been deployed to the pilot client's trust store, if inspection is enabled.
- The intended inspection scope is documented, including any destinations deliberately excluded.
- A rollback path exists for the client trust store.

## Request an HTTPS site through the proxy

From the pilot client:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 https://www.google.com
```

Expected result: the connection succeeds or fails with a known certificate-trust condition that matches the current [SSL inspection](/use_cases/ssl_inspection/ssl_inspection) stage.

Check the access log on the SafeSquid server:

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: the log records the HTTPS destination and policy action.

<Warning>
  **TLS warning risk:** A browser certificate warning is not a successful production HTTPS inspection test. It is evidence that endpoint trust, SSL policy, or the test path still needs review.
</Warning>

If SSL inspection is not configured yet, do not normalise browser certificate-warning bypasses for production users. Limit any warning bypass to an isolated pilot test, record it in the change evidence, and complete Root CA deployment before production HTTPS inspection.

{/* source: _migration_source_v3/docs/01-Getting_Started/06-Verify_Your_Setup.md §5 HTTPS Traffic Flows Through the Proxy */}

## Read the certificate issuer

Once SSL inspection is configured and the Root CA is deployed, the positive test is the certificate itself. Load an HTTPS site in the pilot browser and inspect the certificate issuer.

Expected result: the issuer is the SafeSquid CA, and no warning appears.

An issuer showing the original site's certificate authority means the connection is being tunnelled rather than inspected, even though the page loads normally. That is the failure this page exists to catch.

Check an excluded destination too. A destination on the bypass list should show its original issuer — if it shows the SafeSquid CA, the exclusion is not matching, and traffic the business agreed not to decrypt is being decrypted.

## Capture inspection evidence

Store these artifacts with the deployment record:

- Certificate issuer for an inspected destination, showing the SafeSquid CA.
- Certificate issuer for an excluded destination, showing the original CA.
- The matching access-log entries for both.
- The documented inspection scope, with the business owner of each exclusion.
- Root CA rollout evidence for the pilot client.

## Troubleshoot inspection failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser shows a certificate warning | Root CA is not in the client trust store | Complete Root CA deployment through GPO, MDM, or the approved trust process before retesting |
| Page loads but issuer is the original CA | Session is tunnelled, not inspected | Confirm the destination is in the inspection scope and that SSL inspection is enabled for that policy |
| An excluded destination shows the SafeSquid CA | Exclusion rule is not matching | Correct the bypass entry and re-test; a mis-scoped exclusion decrypts traffic the business excluded |
| Some applications fail while browsers work | Certificate pinning in the application | Add the application's destinations to the documented exclusion list with a named business owner |
| HTTPS fails entirely after enabling inspection | Firewall, trust, or service failure overlap | Re-run [Service Health](/deployment/service_health) first, then re-check Root CA rollout |

## Next steps

- [Policy Enforcement](/getting_started/configure_web_security_policies) - confirm controls act on the decrypted traffic.
- [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection) - configure or adjust the inspection policy.
- [Import Certificate](/use_cases/ssl_inspection/import_certificate_chrome_ie) - deploy Root CA trust to clients.
