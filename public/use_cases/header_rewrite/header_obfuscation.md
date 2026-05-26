---
title: Header Re-Write
slug: /Header_Obfuscation
description: Configure SafeSquid header filter to allow, deny, or insert HTTP headers for client-server communication control.
keywords:
  - header filter SafeSquid
  - modify headers SafeSquid
  - http header filtering SafeSquid
  - header policy SafeSquid
  - request response header SafeSquid
---


# Header Re-Write

## Problem

HTTP headers carry authentication tokens, tracking identifiers, and client fingerprints. Uncontrolled headers break login flows, leak internal paths, or weaken privacy controls. Administrators need allow, deny, and insert rules before downstream content rewriting runs.

## Benefits

SafeSquid header filter adds, deletes, or modifies request and response headers by policy. Global default (allow-all vs deny-all) plus Allow, Deny, and Insert lists give predictable ordering; Insert runs after Allow and Deny.

## Advantages

**Confirmed:** Header processing runs before the Content Re-Write header stage, so header policy applies first in the pipeline described in SafeSquid documentation.

**Draft (CTO confirmation):** Whether header rewriting depth matches a specific competing SWG depends on vendor feature matrices—do not claim parity without a source register entry.

## Call to action

Open the [Configuration Portal](/Configuration_Portal) → Real-time content security → Header filter. Set Global policy, then tune Allow, Deny, and Insert. Follow [Header Filter Configuration and Reference](/Header_Filter_Configuration) for field-level steps and verification.



## Header filter behavior and scope

SafeSquid modifies HTTP header messages exchanged between clients (e.g. web browsers) and the requested web service. Administrators can add, delete, or modify header directives.

The request and response headers are processed by this section before they are processed by the facility to rewrite headers in the Content Re-Write section.

Header filter has 4 sub-sections: Global, Allow, Deny, and Insert.

The processing of a request or a response, by this section is bypassed if the Global sub-section is set to False, and the policies in Allow / Deny / Insert thus become muted.

The policies in the Insert section are processed after the policies in the Allow / Deny lists.

Setting the Default Policy to Allow in the Global Sub-Section, permits all HTTP headers to be exchanged unless there is a policy directive in the Deny List to prevent a header from being exchanged.

Similarly setting the Default policy to Deny shall block all non-mandatory HTTP headers from being exchanged, unless a policy in the Allow list, explicitly permits.



## Header filter configuration guides

### [Header Filter Configuration and Reference](/Header_Filter_Configuration)
Header allow/deny/insert behavior requires correct Global policy and rule configuration. The document covers the Global section, Allow and Deny rule parameters (Type, Value, Applies to, Profiles), and Insert rules for adding or modifying headers. Solution verification confirms policies apply as intended. Use the document to configure and validate header filtering.

## Next steps

Combine header filter with [Access Restriction](/Access_Restriction) and [Cookie Inspection](/Cookie_Inspection) for full request/response control.
