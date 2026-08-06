---
title: "Restrict AnyDesk"
description: "Restrict AnyDesk access via SafeSquid policies and proxy configuration for secure network access control."
keywords: ["restrict anydesk SafeSquid", "SafeSquid block anydesk", "configure anydesk restriction SafeSquid", "SafeSquid remote desktop control", "block remote access anydesk SafeSquid"]
---

## Problem

Security teams need predictable control over app and web usage to reduce policy bypass and data-risk exposure.

## Benefits

You can enforce policy decisions consistently with SafeSquid while preserving legitimate business workflows.

## Advantages

You keep actionable policy control close to operations, with verifiable outcomes in logs and policy behavior.

## Call to action

Use the steps in this guide to implement the control, then validate behavior with a real user-flow test.

## [Access the SafeSquid User Interface](/Configuration_Portal)

## Go to configure page

![Go to configure page to Restict anydesk](/images/How_To/Restrict_any_desk/image1.webp)

## Go to Real time content security

![Select HTTPS Inspection option in Real time content security section to Restrict anydesk](/images/How_To/Restrict_any_desk/image2.webp)

![Enabled Global section as true to restrict anydesk and to edit Inspection policy](/images/How_To/Restrict_any_desk/image3.webp)

![Enabled Global section as true to restrict anydesk and to edit Inspection policy](/images/How_To/Restrict_any_desk/image4.webp)

![Select Access profiles in Restriction policies to access default policies to restrict any desk](/images/How_To/Restrict_any_desk/image5.webp)

![Default Restrict remote desktop application policies present in policies and profiles section](/images/How_To/Restrict_any_desk/image6.webp)

![Edit one of clone policy in policies and profile section to restrict anydesk](/images/How_To/Restrict_any_desk/image7.webp)

![Edit and entry comment and request type in policy to restrict anydesk](/images/How_To/Restrict_any_desk/image8.webp)

![Save Restrict anydesk policy](/images/How_To/Restrict_any_desk/image9.webp)

![Save configuration of policy to restrict anydesk](/images/How_To/Restrict_any_desk/image10.webp)

## Configuration on anydesk

Set proxy on anydesk application

If authentication is enabled you have to specify Username and Password on any desk application.

Anydesk should not take auto proxy settings: If you set proxy in IE browser or chrome browser and you select "Try to detect the proxy server" option on anydesk, it should not take proxy automatically. You must have to configure proxy on anydesk application.