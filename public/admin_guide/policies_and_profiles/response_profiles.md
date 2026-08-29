---
title: "Response Types"
---

<Note>
  CLI man page: `safesquid-respProfiles(5)`
</Note>

The **Response Types** section (`safesquid-respProfiles(5)`) labels HTTP responses for [Access Profiles](/admin_guide/policies_and_profiles/access_profiles) and content filters. It does not block by itself.

## Core mechanics

### Two-pass evaluation

1. On response headers — response profiling runs with no body buffer.
2. On buffered body — hook runs again with detected MIME and size.

Every matching enabled row applies; no first-match stop.

<Frame caption="Response Types — row gate order">
  <img src="/images/admin_guide/response_types_flowchart.svg" alt="Response Types gate flow" />
</Frame>

### Content size

Non-zero min/max tested against body buffer size when present, and against Content-Length when CL flag set. Zero disables each test.

### MIME and extension

MIME regex tries response Content-Type header, then detected body type. Extension regex tries URL (query stripped), then attachment filename.

## Examples

<Tip>

### Text for keyword filter

**Config:** MIME `(^text/|script$)`, add `text_res`.

**Result:** HTML/JS/text responses tagged.
</Tip>

<Tip>

### Images

**Config:** MIME `^image/`, add `image_res`.

**Result:** image Content-Types tagged for image filter policies.
</Tip>

<Tip>

### Large images

**Config:** MIME `^image/`, min size 1048576, add `large-image`.

**Result:** skipped below 1 MiB; tagged at or above threshold.
</Tip>

## How to verify

1. **Trace Entry**; fetch test URL; check native logs.
2. Detailed logs — `response_profiles`, `download_content_types`.
