---
title: "Text analyzer"
---

<Note>
  CLI man page: `safesquid-keywords-filtering(5)`
</Note>

<Frame caption="Cumulative scoring flow">
  <img src="/images/admin_guide/text_analyzer_flowchart.svg" alt="Cumulative scoring flow" />
</Frame>

## Overview

The `Keywords-filtering` section (`safesquid-keywords-filtering(5)`) scans the textual content of HTTP payloads for specific patterns and assigns scores to determine if the content should be blocked.

## Core Mechanics (C++ Source Validation)

Cumulative scoring, early exit at threshold.

- **Cumulative Scoring Engine**: Unlike standard first-match modules, the keyword filter evaluates *all* enabled rules matching the connection profile. When a Regex keyword is matched, its defined `Score` is added to a cumulative tally for that connection.
- **Early Exit**: If the cumulative score breaches the Global Threshold (`if (x >= threshold)`), scanning immediately stops to save CPU.
- **MIME Filtering**: SafeSquid will only scan payloads whose `Content-Type` matches the specified `Mime type` regular expression.
- **Enforcement**: Once the threshold is breached, the connection action becomes **DO NOT BYPASS**, serving the specified block template and populating the `_SCORE_` and `_REASON_` template variables.

## Schema Fields

### Global Fields

- **Enabled (enabled)**: Turn Text analyzer on or off for all connections (unless bypassed).
- **Threshold (threshold)**: Minimum total score from matching rows to block. Block when total ≥ this value (strictly below = allow).
- **Template (templ)**: Block page template when score ≥ Threshold. Blank uses blocked . Template receives *SCORE* and *THRESHOLD* variables.

### Rule-Based Fields (Per Connection Tuning)

- **Enabled (enabled)**: Skip this row when disabled. Rows with Score 0 or blank Keyword are never applied.
- **Comment (comment)**: Notes for operators. Logged on match when non-empty.
- **Profiles (profiles)**: Apply only when the connection has one of these profiles. Blank = all connections. Prefix ! to skip connections that have a profile.
- **Mime type (mime)**: Regex on response Content-Type . Blank defaults to matching text (same as built-in text/css/javascript/xml/json family).
- **Keyword(s) (keyword)** — Regex searched in the response body. Required; blank Keyword skips the row. Example: `\b(gambling|casino)\b`. One match adds Score once per scan pass for this row.
- **Score (score)**: Points added when this row’s keyword regex matches the body. Use 0 to disable the row. Negative values reduce the running total.

## How SafeSquid processes the list

1. During response processing, if any enabled row matches the response `Content-Type`, SafeSquid buffers the body.
2. After the body is available, rows are walked top to bottom.
3. Mime type regex must match `Content-Type`. Blank mime defaults to matching `text` (same family as text/css/javascript/xml/json).
4. Keyword regex is searched in the buffered body; each match adds that row's Score (negative scores reduce the total).
5. Rows with Score 0 or blank Keyword are never applied.
6. At or above Threshold: HTTP 451 block page, bypass disallowed, cache code `TCP_DENIED`.

## Important entry fields

- **Profiles** — Apply only when the connection has one of these profiles. Blank = all connections. Prefix `!` to skip connections that have a profile.
- **Mime type** — Regex on response `Content-Type`. Blank defaults to matching `text`.
- **Keyword(s)** — Regex searched in the response body. Required; blank Keyword skips the row.
- **Score** — Points added when the keyword regex matches. Use 0 to disable the row. Negative values reduce the running total.

## Examples

<Tip>

### 1 — Block pages with multiple mild terms

- Threshold: **100**
- Row A: Keyword `gambling`, Score **40**
- Row B: Keyword `casino`, Score **70**

**Result:** a page containing both terms scores 110, meets Threshold, and is blocked with HTTP 451 and the configured template. A page with only `gambling` scores 40 and is allowed.
</Tip>

<Tip>

### 2 — Single high-weight term

- Threshold: **50**
- Row: Keyword `\bweapon\b`, Score **100**, Mime blank (text family)

**Result:** any text/html body matching the regex is blocked on first row match; scan stops once total ≥ Threshold.
</Tip>

<Tip>

### 3 — Limit to students profile

- Row: Profiles `Students`, Keyword `weapon`, Score **80**
- Threshold: **50**

**Result:** staff without the Students profile skip the row entirely; student connections with `weapon` in the body are blocked.
</Tip>

<Tip>

### 4 — Non-text response skipped

- Row: Mime `text`, Keyword `badword`, Score **100**

**Result:** an `image/png` response does not match the mime regex, is not buffered for keyword scan, and passes through even if binary data accidentally contained the string.
</Tip>

## How to verify

1. Fetch a test page through the proxy and confirm block vs allow against known body content.
2. Check debug response header `X-Text-Analyzer` (shows score vs threshold, or `Buffering Requested` when mime matched).
3. Enable TEXT\_ANALYZER in `LOG_LEVEL` for native `match:` and `blocked` / `allowed` lines.
4. Open **Reports → Detailed logs**; blocked responses show `filter_name` for text analyzer and the score reason.
