---
title: Allow Remote Applications to Particular Users
description: Allow specific users to access remote applications via SafeSquid policies, including without application signatures.
keywords:
  - remote application access SafeSquid
  - SafeSquid user access control
  - SafeSquid policy creation
  - network access policy SafeSquid
---


# Allow specific users to access remote applications

When traffic is blocked by default, some users may need access to remote applications. SafeSquid can allow specific users or groups to access remote applications while keeping the default block for others.



## How it works
When a user tries to access remote application software, First SafeSquid checks for that user and decides whether this user is allowed to access the remote application or not, if yes then SafeSquid gives access to that user, and before giving the access it will check for user-agent or website which you added in Custom Settings > Request types section. If access is allowed to both users and the application, then only the user can able to access that application. If the user **Samidha wants access** to the **XYZ** application but is trying to access the **ABC** application, SafeSquid will block the user Samidha.



## How to Allow Remote Applications?
Follow the Link: [Allow anydesk](/docs/Use_Cases/Allow_anydesk/)



## How to create policy without Application Signature
1.  Remote applications are already categorized in the SafeSquid Application Signatures. First, you need to check whether the Application is categorized or not.
2.  If the application is not categorized under default Application Signatures, find the User-agent using SafeSquid's extended logs or any other traffic-capturing tool.
3.  Add that User-agent or website into Request Types.
4.  Bind that created user group and Request Type in Access Profiles and decide whether to block or allow

