---
title: Header Filter Configuration and Reference
description: "Configure SafeSquid header filter: Global, Allow, Deny, Insert rules, and solution verification."
keywords:
  - header filter configuration SafeSquid
  - header allow deny insert
  - Restriction Profiles Header Filter
---


# Header Filter Configuration and Reference



## Global

The Global section controls how SafeSquid edits HTTP header messages between the browser and the Internet. Use it to increase privacy, control client requests and server responses, and add, delete, or modify request and response headers. The Insert sub-section adds new headers or modifies existing ones in addition to Allow/Deny.

The following subsections cover:

1. Request header patterns that are passed from browsers to webservers.
2. Response header patterns that are coming from webservers to clients.

![Header Filter section in Restriction Profiles](/img/Configure/Restriction_Profiles/Header_Filter/image1.webp)

### Enabled
Enable or Disable the header filter section.

**TRUE:** Enable header filter section.

**FALSE:** Disable header filter section.

### Policy
Select the default action to take, when no matching entry for a requested header is found.

**ALLOW:** Allow everything Except rules defined under Deny subsection.

**DENY:** Deny everything Except rules defined under Allow subsection.



## Allow
When the Policy is Deny, rules defined under this sub-section, are exclusively allowed access.

Add a new allow entry to explicitly permit the header for all connections or a specific set of conditions.

![Header Filter Allow sub-section](/img/Configure/Restriction_Profiles/Header_Filter/image2.webp)

### Enabled
Enable or Disable this entry.

**TRUE:** Enable this entry.

**FALSE:** Disable this entry.

### Comment
For documentation and future references, explain the relevance of this entry with your policies.

### Profiles
Specify the Profiles applicable for this entry.

This entry will be applicable only if the connection has any one of the specified profiles.

Leave it Blank, to apply for all connections irrespective of any applied profile.

To avoid application to a connection that has a profile, use a negated profile (! profile).

### Type
A regular expression matching the header type to which this entry applies.

Headers are in the form of type and value.

Leave blank to Match everything.

Example: X-GoogApps-Allowed-Domains.

### Value
A regular expression matching the header values.

Leave blank to Match everything.

**Example:** text/html.

### Applies to
This option is to select whether this entry applies to the server header, client header, or both.

**CLIENT:** This entry will be applied only for request headers, sent by the client.

**SERVER:** This entry will be applied only for response headers, sent by the server.

### Example
#### Rule#1
Allow WebSockets for connections with profile "ALLOW WEBSOCKET". Use this when all users' WebSocket connections are denied by default. The Allow rule permits WebSocket connections for a defined application or service and user group.

![Allow WebSocket rule for ALLOW WEBSOCKET profile](/img/Configure/Restriction_Profiles/Header_Filter/image3.webp)



## Deny
When the Policy is Allow, rules defined under this sub-section, are denied access exclusively.

Add a deny entry to explicitly block the header for all connections or a specific set of conditions.

![Header Filter Deny sub-section](/img/Configure/Restriction_Profiles/Header_Filter/image4.webp)

### Enabled
Enable or Disable this entry.

**TRUE:** Enable this entry.

**FALSE:** Disable this entry.

### Comment
For documentation and future references, explain the relevance of this entry with your policies.

### Profiles
Specify the Profiles applicable for this entry.

This entry will be applicable only if the connection has any one of the specified profiles.

Leave it Blank, to apply for all connections irrespective of any applied profile.

To avoid application to a connection that has a profile, use a negated profile (! profile).

### Type
A regular expression matching the header type to which this entry applies.

Headers are in the form of type and value.

Leave blank to Match everything.

Example: X-GoogApps-Allowed-Domains.

### Value
A regular expression matching the header value.

Leave blank to Match everything.

Example: text/html.

### Applies to
This option is to select whether this entry applies to the server header, client header, or both.

**CLIENT:** This entry will be applied only for request headers, sent by the client.

**SERVER:** This entry will be applied only for response headers, sent by the server.

### Example
#### Rule#1
Deny all WebSocket connections by matching request headers containing "WebSocket"

For connections with the profile "REMOVE WEBSOCKETS" "websocket: upgrade" header will be removed from request headers, which will result in a WebSocket connection never being established.

![Deny WebSocket rule REMOVE WEBSOCKETS](/img/Configure/Restriction_Profiles/Header_Filter/image5.webp)

### Insert
In this sub-section add rules to modify request and response headers. Insert additional information into the headers sent by the client browser.

![Header Filter Insert sub-section](/img/Configure/Restriction_Profiles/Header_Filter/image6.webp)

### Enabled
Enable or Disable this entry.

**TRUE:** Enable this entry.

**FALSE:** Disable this entry.

### Comment
For documentation and future references, explain the relevance of this entry with your policies.

### Profiles
Specify the Profiles applicable for this entry.

This entry will be applicable only if the connection has any one of the specified profiles.

Leave it Blank, to apply for all connections irrespective of any applied profile.

To avoid application to a connection that has a profile, use a negated profile (! profile).

### Type
A regular expression matching the header type to which this entry applies.

Headers are in the form of type and value.

Leave blank to Match everything.

Example: X-GoogApps-Allowed-Domains.

### Value
A regular expression matching the header value.

Leave blank to Match everything.

Example: text/html.

### Applies to
This option is to select whether this entry applies to the server header, client header, or both.

**CLIENT:** This entry will be applied only for request headers, sent by the client.

**SERVER:** This entry will be applied only for response headers, sent by the server.

### Example
#### Rule#1
Restrict access to the corporate Google account only. When users try to log in with a personal Google account, login is blocked. Use the custom request header X-GoogApps-Allowed-Domains to specify allowed domains. Include the domain registered with Google Workspace in the list.

![X-GoogApps-Allowed-Domains header insert for corporate Google](/img/Configure/Restriction_Profiles/Header_Filter/image7.webp)

#### Rule#2
Allow YouTube during lunch hours while blocking inappropriate content. Enforce YouTube strict mode for all users. Use header insert to add the custom header YouTube-Restrict for strict restricted access. Per Google, YouTube strict mode does not filter 100% of inappropriate content.

![YouTube-Restrict header insert for strict mode](/img/Configure/Restriction_Profiles/Header_Filter/image8.webp)



## View headers
In this sub-section, you can find the example headers with type and values.

![View headers sub-section with example headers](/img/Configure/Restriction_Profiles/Header_Filter/image9.webp)



## Verification and Evidence

- **Interface Checks**: In [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), Restriction Profiles → Header Filter: Global enabled, Allow/Deny/Insert rules match intent; Type, Value, and Applies to are set correctly.
- **Log Analysis**: Requests and responses show modified or stripped headers per policy; WebSocket or target-site behavior matches expected allow/deny/insert.
- **Performance Validation**: Test with profile (e.g. ALLOW WEBSOCKET, REMOVE WEBSOCKETS, X-GoogApps-Allowed-Domains); expected sites work and restricted behavior is enforced.

**Related**: [Cookie Inspection](/docs/Cookie_Inspection/main/), [Access Restriction](/docs/Access_Restriction/main/), [URL Redirection SafeSearch](/docs/URL_Redirection/SafeSearch/), [Troubleshooting](/docs/Troubleshooting/main/)

