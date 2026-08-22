---
title: Enforce SafeSearch
description: Enforce SafeSearch on Google, Yahoo, and Bing via SafeSquid to block explicit content in search results.
keywords:
  - enforce safesearch SafeSquid
  - google safesearch SafeSquid
  - yahoo safesearch SafeSquid
  - bing safesearch SafeSquid
  - filter explicit content SafeSquid
---



## SafeSearch filters explicit content in search results

SafeSearch is an automated filter for pornography and potentially offensive content.

SafeSquid SWG SafeSearch aims to: give parents and teachers control over what content children see online; offer tips for staying safe online; and align with charities, industry, and government efforts to protect young people. Organizations and businesses also use these filters to prevent inappropriate results in search engines.

Google SafeSearch screens sexually explicit content and removes it from search results. No filter is 100% accurate, but SafeSearch reduces exposure to unwanted content.

SafeSearch can be disabled in the search engine with a few clicks. To enforce it, the proxy must override user preference. Configure the proxy server to append SafeSearch parameters to queries so users cannot disable it. Google appends **&safe=active** for SafeSearch URLs.

Google uses HTTPS, so the proxy must support SSL inspection. SafeSquid SWG supports SSL inspection and provides a WebGUI to create policies and control user access.

SafeSquid SWG includes default rules that enforce SafeSearch for Google, Yahoo, and Bing. Enable the SafeSearch policies in Policies and Profiles (if disabled).



## Required setup

HTTPS Inspection must be enabled in SafeSquid. See [How to enable HTTPS Inspection](/docs/SSL_Inspection/main/) if not yet enabled.



## Google SafeSearch

SafeSquid filters explicit search results (e.g. pornographic images, videos, and websites) on Google. Disabling Google SafeSearch in the browser has no effect; SafeSquid enforces it.



## Yahoo SafeSearch

SafeSquid filters explicit search results on Yahoo. Disabling Yahoo SafeSearch in the browser has no effect; SafeSquid enforces it.



## Bing SafeSearch

SafeSquid filters explicit search results on Bing. Disabling Bing SafeSearch in the browser has no effect; SafeSquid enforces it.

