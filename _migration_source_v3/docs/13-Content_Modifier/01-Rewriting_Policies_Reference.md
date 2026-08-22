---
title: Rewriting Policies Reference
description: Field-by-field reference for SafeSquid Content Modifier rewriting policies including pattern matching, replacement, MIME types, and applies-to targets.
keywords:
  - SafeSquid content modifier reference
  - rewriting policies configuration
  - content modifier fields
  - regex content rewriting
  - SafeSquid body modification
  - HTTP header rewriting
---


# Rewriting policies control what SafeSquid modifies

Content Modifier uses regex-based rewriting policies to modify web page body content, client request headers, server response headers, and POST data in real time. Each policy defines a match pattern, a replacement, a MIME scope, and a target (body, client header, server header, or POST data). Policies are ordered; SafeSquid evaluates them top-to-bottom and applies all matching rules to each connection.



## Global section enables or disables all rewriting

Access the Content Modifier section in the SafeSquid interface under **Configure → Real-time Content Security → Content Modifier**.

### Enabled

Enable or disable the entire Content Modifier section.

- **TRUE**: SafeSquid applies rewriting policies to matching connections.
- **FALSE**: SafeSquid skips all content modification. No policies are evaluated.



## Policy fields define match conditions and actions

Each rewriting policy contains the following fields.

### Enabled

Enable or disable this specific policy entry.

- **TRUE**: SafeSquid evaluates this policy.
- **FALSE**: SafeSquid skips this entry.

### Comment

Document the purpose of this policy entry. A future administrator reading the policies should understand the intent of each entry from the comment alone.

### Profiles

Specify the profiles applicable for this entry. SafeSquid applies the policy only if the connection has any one of the specified profiles. Leave blank to apply to all connections regardless of profile. Negate a profile with `!` (e.g. `!bypass`) to exclude connections with that profile.

### Mime type

Specify a regular expression matching the MIME types for which this entry applies. According to their nature and format, MIME type identifies files on the Internet.

Set this field to limit the scope. If left blank, SafeSquid checks all file types — a significant performance cost.

**Examples:**
- `text/html` — HTML pages only
- `^image/` — all image types
- `^application/` — all application types
- `application/x-shockwave-flash` — Flash content only

### Pattern

A regular expression matching the area of text inside the file to modify. SafeSquid uses Perl-compatible regular expressions (PCRE). The pattern may include a trailing `/` followed by flag characters (e.g. `/i` for case-insensitive). If a `/` appears anywhere else in the pattern, flags must be specified explicitly.

Use parenthesized capture groups to extract portions of the match for use in the replacement.

### Replace

Specify the replacement text to substitute in place of the matched text. The replacement may contain back-references to strings captured using parentheses in the Pattern field (e.g. `\1`, `\2`).

### Applies to

Select what the rewrite entry targets:

| Value | Target | Notes |
|---|---|---|
| **BODY** | Response body (HTML, JavaScript, CSS, etc.) | Modifies web page content before delivery to the client. |
| **CLIENT** | Client request header | Rewrites the client HTTP header before SafeSquid parses it. Take care not to remove headers required for request handling. |
| **SERVER** | Server response header | Rewrites the response header from the remote web server. Same caution as CLIENT applies. |
| **POST** | POST/PUT request body | Rewrites POST or PUT data sent when submitting a form or uploading a file. |



## Examples demonstrate common rewriting scenarios

### Mark inspected pages with a modified title tag

**Goal:** Modify the `<title>` tag of web pages to indicate SafeSquid inspected the content.

- **Applies to:** BODY
- **Mime type:** `text/html`
- **Profiles:** (blank — applies to all)
- **Pattern:** `<title>(.*?)</title>`
- **Replace:** `<title>Inspected by SafeSquid - \1</title>`

SafeSquid buffers chunked responses to ensure the complete title tag is matched and replaced.

### Request PNG/JPG images instead of AVIF/WEBP

**Goal:** Modify the `Accept` header sent from the client so the remote server returns PNG or JPG images instead of AVIF or WEBP. AVIF images bypass SafeSquid's Image Analyser.

- **Applies to:** CLIENT
- **Mime type:** (blank — header rewriting, not body)
- **Pattern:** `(Accept:.*?)image/avif,?|image/webp,?`
- **Replace:** `\1`

SafeSquid strips the AVIF and WEBP entries from the Accept header, causing the server to fall back to PNG or JPG formats that the Image Analyser can inspect.



## Verification and evidence

- **Interface Checks**: In the [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), confirm Content Modifier → Global is enabled. Verify each policy shows the correct Pattern, Replace, Mime type, and Applies to values.
- **Log Analysis**: Access logs should show connections matching the configured profiles and MIME types. Enable extended logging to confirm rewriting occurred on the expected connections.
- **Performance Validation**: Load a target page in the browser and inspect the page source (or response headers) to verify the expected modification. For body rewrites, view source to confirm substituted text. For header rewrites, use browser developer tools or SafeSquid logs.

**Next steps:** [Content Modifier overview](/docs/Content_Modifier/main/) for prerequisites, implementation actions, and troubleshooting. [Header Obfuscation](/docs/Header_Obfuscation/main/) for header-specific filtering. [Cookie Inspection](/docs/Cookie_Inspection/main/) for cookie-level policies.

