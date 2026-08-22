---
title: Cookie Filter Configuration and Reference
description: "Configure and reference SafeSquid cookie filter: Global, Allow, and Deny rules, expiry and profile options, and solution verification."
keywords:
  - cookie filter configuration SafeSquid
  - cookie allow deny rules
  - cookie filter reference
  - Restriction Profiles Cookie Filter
---


# Cookie Filter Configuration and Reference



## [Access SafeSquid interface](/docs/SafeSquid_SWG/Configuration_Portal/)



## Go to configure page
![Configure page with Cookie Filter in sidebar](/img/Configure/Restriction_Profiles/Cookie_Filter/image1.webp)



## Global
### Enabled
Enable or Disable the cookie filtering section.

-   **TRUE:** Enable cookie filtering section
-   **FALSE:** Disable the cookie filtering section

![Cookie Filter Global section with Enabled and Policy options](/img/Configure/Restriction_Profiles/Cookie_Filter/image2.webp)

### Policy
Select the default action to take, when no matching entry for a requested cookie is found.

-   **ALLOW:** When Policy is set to Allow, a requested cookie is allowed, when no matching entry is found
-   **DENY:** When Policy is set to Deny, a requested cookie is denied, if no matching entry is found



## Allow
![Cookie Filter Allow sub-section](/img/Configure/Restriction_Profiles/Cookie_Filter/image3.webp)

When the Policy is Deny, rules defined under this sub-section, are exclusively allowed access.

Add a new allow entry to explicitly permit cookie transfer for all or a specific set of conditions. This defines cookie transfer whitelists.

### Enabled
Enable or Disable this entry

**TRUE:** Enable this entry.

**FALSE:** Disable this entry.

### Comment
For documentation and future references, explain the relevance of this entry to the deployment policies.

### Profiles
Specify the Profiles applicable for this entry.

This entry will be applicable only if the connection has any one of the specified profiles.

Leave it Blank, to apply for all connections irrespective of any applied profile.

To avoid application to a connection that has a profile, use a negated profile (! profile).

### Expiry year range
Mention the cookie expiry year range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** 2016-2017, here cookie will expire after the year 2017.

### Expiry month range
Select the cookie expiry month range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** January -- March, here cookie expires after March.

### Expiry day range
The cookie expiry day range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** 1-20, here cookie will expire after the 20th day.

### Expiry weekday range
The cookie expiry weekday ranges this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** Monday -- Friday, here cookie will expire after Friday.

### Expiry hour range
The cookie expiry hour ranges this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** 1-10, Here cookie will expire after 10 AM.

### Expiry minute range
The cookie expiry minute range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** 15-30, Here cookie will expire after 10:30 AM.

In the above example, Hours are included in the Hour range.

### Domain
Here you can mention the domain (website) names by separating with pipe (|) which you want to allow or deny. You can use regular expressions to match the domains.

**Example:** safesquid.com|google.com.

### Path
A regular expression matching the cookie's path attribute.

### Direction
The direction of the cookie this entry applies to; can be either in (Set-cookie sent by website), out (Cookie sent by browser), or both.

-   **IN:** For Inbound Connections only. That is only for the cookies sent by the hosts(websites).
-   **OUT:** For Outbound Connections only. That is only for the cookies sent by the browser.
-   **BOTH:** For Both Inbound and Outbound connections. For cookies sent by the websites as well as cookies sent by the browser.

### Time match mode
Select the appropriate mode to match the multiple time ranges.

**ABSOLUTETIME:**

When the absolute time match mode is used, any time between the starting and ending time will be matched.

Example: The weekday range specified is Monday to Friday and the Hour Range is 9 to 17.

The Absolute match mode will match any time starting Monday, 9 AM and ending Friday, 17 PM.

So, it will be active from Monday 9 AM to Friday 5 PM.

**ALLRANGES:**

With all ranges time match mode, however, a time within all of the ranges will match.

Example: The weekday range specified is Monday to Friday and the Hour Range is 9 to 17.

All ranges will match any time between 9 AM to 17 PM, on all weekdays from Monday to Friday.

So, it will be active every day from Monday to Friday between 9 AM to 5 PM.

### Example
#### Rule#1
I want to allow cookie filtering for connections with the profile "COOKIE ALLOW". Users who require access to log-in webpages and personal accounts need cookie access. We can use the cookie -> Allow subsection to allow Cookies.

![Allow rule for COOKIE ALLOW profile](/img/Configure/Restriction_Profiles/Cookie_Filter/image4.webp)

#### Rule#2
I want to allow cookies for domain safesquid.com Despite the deny rule, connections to domain safesquid.com will not drop cookies This can be used in a situation where login is required for mission-critical applications.

![Allow cookies for domain safesquid.com rule](/img/Configure/Restriction_Profiles/Cookie_Filter/image5.webp)



## Deny
When the Policy is Allow, rules defined under this sub-section, are exclusively denied access.

Here, you can add rules under Deny that would explicitly result in blocking or denial of cookie transfer to all or a specific set of conditions.

This effectively allows you to set a variety of intelligently and creatively defined Cookie Transfer Blacklist(s).

![Cookie Filter Deny sub-section with rule list](/img/Configure/Restriction_Profiles/Cookie_Filter/image6.webp)

### Enabled
Enable or Disable this entry

-   **TRUE:** Enable this entry
-   **FALSE:** Disable this entry

### Comment
For documentation and future references, explain the relevance of this entry to the deployment policies.

### Profiles
Specify the Profiles applicable for this entry.

This entry will be applicable only if the connection has any one of the specified profiles.

Leave it Blank, to apply for all connections irrespective of any applied profile.

To avoid application to a connection that has a profile, use a negated profile (! profile).

### Expiry year range
Mention the cookie expiry year range this entry applies to

The cookie from a particular host (website), will be expired after this range.

**Example:** 2016-2017, here cookie will expire after the year 2017.

### Expiry month range
Select the cookie expiry month range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** January -- March, here cookie expires after March.

### Expiry day range
The cookie expiry day range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

Example: 1-20, here cookie will expire after the 20th day.

### Expiry weekday range
The cookie expiry weekday ranges this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** Monday -- Friday, here cookie will expire after Friday.

### Expiry hour range
The cookie expiry hour ranges this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** 1-10, Here cookie will expire after 10 AM.

### Expiry minute range
The cookie expiry minute range this entry applies to.

The cookie from a particular host (website), will be expired after this range.

**Example:** 15-30, Here cookie will expire after 10:30 AM.

In the above example, Hours are included in the Hour range.

### Domain
Here you can mention the domain(website) names by separating with pipe (|) which you want to allow or deny. You can use regular expressions to match the domains.

**Example:** safesquid.com|google.com

### Path
A regular expression matching the cookie's path attribute.

### Direction
The direction of the cookie this entry applies to; can be either in (Set-cookie sent by website), out (Cookie sent by browser), or both.

-   **IN:** For Inbound Connections only. That is only for the cookies sent by the hosts(websites).
-   **OUT:** For Outbound Connections only. That is only for the cookies sent by the browser.
-   **BOTH:** For Both Inbound and Outbound connections. For cookies sent by the websites as well as cookies sent by the browser.

### Time match mode
Select the appropriate mode to match the multiple time ranges.

**ABSOLUTETIME:**

When the absolute time match mode is used, any time between the starting and ending time will be matched.

Example: The weekday range specified is Monday to Friday and the Hour Range is 9 to 17.

The Absolute match mode will match any time starting Monday, 9 AM and ending Friday, 5 PM.

So, it will be active from Monday 9 AM to Friday 5 PM.

**ALLRANGES:**

With all ranges time match mode, however, a time within all of the ranges will match.

Example: The weekday range specified is Monday to Friday and the Hour Range is 9 to 17.

All ranges will match any time between 9 AM to 17 PM, on all weekdays from Monday to Friday.

So, it will be active every day from Monday to Friday between 9 AM to 5 PM.

### Example
#### Rule#1
The default rule for dropping cookies is used by SafeSquid.

Connections with the profile "READ ONLY" will ensure users are unable to log in.

Cookies sent in both directions are dropped.

![DROP COOKIES rule with READ ONLY profile](/img/Configure/Restriction_Profiles/Cookie_Filter/image7.webp)

#### Rule#2
Connections with the profile "DROP COOKIES FOR GOOGLE" will drop all cookies for the domain google.com.

Cookies will be dropped for both incoming and outgoing requests.

![DROP COOKIES FOR GOOGLE rule for domain google.com](/img/Configure/Restriction_Profiles/Cookie_Filter/image8.webp)



## Verification and Evidence

- **Interface Checks**: In [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), Restriction Profiles → Cookie Filter: Global and policy entries match intent (Allow/Deny, profiles). Test URLs or domains show correct category in Categorize Web-sites if used.
- **Log Analysis**: Access logs reflect cookie allow/deny per policy; blocked cookie exchange may show in response or request logs.
- **Performance Validation**: Browsing with Allow profile allows login and cookies; with Deny or Drop profile, target sites do not receive or retain cookies as configured.

**Related**: [Access Restriction](/docs/Access_Restriction/main/), [Header Obfuscation](/docs/Header_Obfuscation/main/), [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), [Troubleshooting](/docs/Troubleshooting/main/)

