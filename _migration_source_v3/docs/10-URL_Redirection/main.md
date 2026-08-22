---
title: URL Redirection
slug: /URL_Redirection
description: Configure URL redirection policies in SafeSquid to redirect websites, enforce safe search, and implement content steering for security and compliance.
keywords:
  - SafeSquid URL redirection
  - proxy URL rewriting
  - safe search enforcement
  - website redirection policies
  - content steering proxy
  - URL filtering SafeSquid
---


# URL Redirection

URL redirection lets SafeSquid send users to a different URL than the one requested. Use it to enforce safe search, steer traffic for compliance, or redirect specific sites to an alternative destination.

## Redirection Modes

SafeSquid supports two redirection modes controlled by the **302 Redirect** toggle:

### HTTP Redirection (302 Redirect Enabled)
When enabled, SafeSquid sends an HTTP 302 redirect response to the client browser. The browser sees the redirect and follows it to the new destination. This mode:
- Shows the redirect in browser history
- Allows the client to see both original and target URLs
- Uses standard HTTP redirect mechanisms

### Internal Redirection (302 Redirect Disabled)
When disabled, SafeSquid performs the redirection internally without informing the client. The proxy fetches content from the target URL and serves it transparently. This mode:
- Hides the redirect from the end user
- Maintains the original URL in the browser address bar
- Performs the redirection at the proxy level

Choose the mode based on whether users should see the redirect happening (HTTP) or experience seamless content steering (internal).

## URL redirection and SafeSearch guides

### [Enforce SafeSearch](/docs/URL_Redirection/SafeSearch/)
Search engines return explicit content when SafeSearch is not enforced. SafeSquid appends SafeSearch parameters to Google, Yahoo, and Bing queries so users cannot disable filtering. Consistent content filtering across search traffic reduces exposure and supports policy compliance. Enable SafeSearch policies using this document.

### [Redirect One Website to Another](/docs/URL_Redirection/Redirect_One_Website_to_Another/)
Organizations need to send traffic from one URL to another for branding, blocking, or compliance. The document covers enabling the Redirect section and creating redirection policies in Real Time Content Security. Verification in Native logs confirms redirects work as intended. Use this document to configure and validate URL-to-URL redirection.

## Next steps

Combine with [Access Restriction](/docs/Access_Restriction/main/) for allow/deny by URL; use [Profiling Engine](/docs/Profiling_Engine/main/) for category-based policy.
