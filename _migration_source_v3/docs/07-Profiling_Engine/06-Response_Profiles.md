---
title: Response Profiles
description: Profile web server responses in SafeSquid using MIME types, file extensions, content size, and headers for traffic and content control.
keywords:
  - SafeSquid response types
  - SafeSquid response profiler
  - SafeSquid MIME filtering
  - SafeSquid file extension block
  - SafeSquid content length rules
  - SafeSquid response header filtering
  - SafeSquid websocket profiling
  - SafeSquid block downloads by type
  - configure SafeSquid response profiles
---



## Response profiles manage rules by server response

Use Response profiles to manage profiling based on responses from the web server. Profiling can use these parameters from the response:

1. Mime
2. File
3. Content-Length
4. Response header pattern, etc.,



## [Access SafeSquid interface](/docs/SafeSquid_SWG/Configuration_Portal/)



## Go to configure page

![clicking on configure in safesquid interface](/img/Configure/Custom_Settings/Response_Types/image1.webp)



## Go to custom settings.

![clicking on custom settings in the sidebar](/img/Configure/Custom_Settings/Response_Types/image2.webp)

![clicking on Response Types in custom settings](/img/Configure/Custom_Settings/Response_Types/image3.webp)



## Global

### Enabled

Enable or Disable the response types section.

TRUE: Enable response types section.

FALSE: Disable response types of section.

![showing global section of response types](/img/Configure/Custom_Settings/Response_Types/image4.webp)

![adding a new policy by clicking on add new button](/img/Configure/Custom_Settings/Response_Types/image5.webp)



## Response Types

The following rules are tested for each connection.

The testing is done in top-down order.

The first entry that matches the Response Profile of a connection, will be applied to it.

![showing response Type tab in Response type section](/img/Configure/Custom_Settings/Response_Types/image6.webp)

### Enabled

Enable or Disable this entry.

1. TRUE: Enable this entry.
2. FALSE: Disable this entry.

### Comment

For documentation and future references, explain the relevance of this entry to the deployment policies.

### Trace Entry

Enable or Disable Tracing of this entry

Select "Yes" to debug the application of entry using SafeSquid logs.

Enable entry tracing to validate that the entry is applied.

TRUE: Select this option to enable profile tracing.

FALSE: Select this option to disable profile tracing.

### Response Types

Specify the list of Response Profile(s)for which this entry should be applicable.

Leave it Blank, to ignore this applicability test.

If one or more Response Profiles are specified, this entry will be applicable only after, a response has been received from the web server.

To avoid application to a connection for specific Response Profile(s), use negation (! Response Profile).

### Content type

Specify the MIME type for which this entry should be applicable.

MIME-type is a way of identifying files on the Internet according to their nature and format.

Here, MIME-type indicates the response body received from the server.

This entry applies to the regular expression matching the MIME type.

**Example**: text/html, ^image/, ^application/, application/x-shockwave-flash.

If this entry should be applied to all responses, irrespective of MIME type, leave it blank.

### File Extension

Specify the file extensions for which this entry should be applicable.

This entry applies to the regular expression matching the extension of the file(s) obtained in the response body.

Leave it blank to apply all the requests, irrespective of file extension.

### Transfer Encoding Chunk

This option is to control how the transfer encoding chunk header should be handled.

**Example**: Transfer-Encoding: chunked

1. **ANY:** Select this if the transfer encoding chunked does not matter in the response header.
2. **NO:** Select this to skip applying the profile when transfer-encoding chunked is present in the response header.
3. **YES:** Select this if you want to apply a profile if the transfer encoding chunked is present in the response header.

### multipart\_byterange

This option is to control how the multi-part/ byte ranges header should be handled.

**Example**: Content-type: multipart/x-byteranges; boundary=THIS\_STRING\_SEPARATES --THIS\_STRING\_SEPARATES

Content-type: application/x-pdf Content-range: bytes 500-999/8000 ...the first range... --THIS\_STRING\_SEPARATES

Content-type: application/x-pdf Content-range: bytes 7000-7999/8000 ...the second range... --THIS\_STRING\_SEPARATES--

1. **ANY**: Select this if multipart/ byterange does not matter in the response header.
2. **NO:** Select this to skip applying the profile when multipart/byteranges are present in the response header.
3. **YES:** Select this to apply the profile when multipart/byteranges are present in the response header.

### Minimum Content Size

Specify the minimum content size of the response body for which this entry is applicable.

### Maximum Content Size

Specify the maximum content size of the response body for which this entry is applicable.

### Response Header Pattern

Specify the regular expression matching the response header pattern for which this entry is applicable.

If left blank, applies to all response patterns.

### Added Response Types

Specify the list of Response Profiles, to append to the connection's existing Response Profiles, if all the applicability test rules match.

Subsequent applicable Entries may further modify the connection's Response Profiles.

Define a new Response Profile(s), or select previously defined Response Profile(s)from the drop-down menu to apply to the connection, if it matches this entry.

When defining a new Response Profile, use terms that uniquely represent your needs.

### Removed Response Types

Specify the list of Response Profile(s), to remove the connection's existing Profiles, if all the applicability test rules match.

Subsequent applicable Entries may further modify the connection's Response Profiles.

Select previously defined Response Profile(s)from the drop-down menu to apply to the connection, if it matches this entry.



## Example

### Rule#1

All files with content type macro enabled office documents to be added to a profile "ALL MACRO ENABLED DOCUMENT".

This response type blocks downloads of macro-enabled documents.

Response type is used to profile connections based on the response received from the web server.

![showing rule which will block micro enabled documents](/img/Configure/Custom_Settings/Response_Types/image7.webp)

### Rule#2

To block all e-book files: match file extensions .azw and .epub, add the matching response type "EBOOK's", then create Access policies that block files with those extensions.

![showing rule which will block response type of electronic books](/img/Configure/Custom_Settings/Response_Types/image8.webp)

### Rule#3

For connections with response header Upgrade: websocket, add the response type as WebSocket All websocket connections will now be profiled as "Websocket".

![showing rule which will add the response type of websocket](/img/Configure/Custom_Settings/Response_Types/image9.webp)

