---
title: Access Remote Desktop Applications Through SafeSquid
description: Understand how remote desktop applications like AnyDesk, TeamViewer, and AmmyAdmin interact with SafeSquid in different network scenarios and how to effectively block or allow access using HTTPS inspection and access profiles.
keywords:
  - block remote desktop apps proxy
  - SafeSquid https inspection
  - allow anydesk through proxy
  - teamviewer proxy blocking
  - SafeSquid access profiles
---



## Case 1: There is no direct Internet access to the client Machine
**A)HTTPS ENABLED**

**Any desk** :  Any desk is not able to connect to the remote server through proxy.

**Team viewer** : Team viewer is not able to connect to  the remote server through proxy.

**AmmyAdmin**: AmmyAdmin is not able to connect to the remote server through proxy.


**B) HTTPS DISABLED :**

**Any desk**:  Any desk is able to connect to the remote server through proxy.

**Team viewer**: Team viewer is able to connect to remote the server through proxy.

**AmmyAdmin** : AmmyAdmin is able to connect to the remote server through proxy.

How to block in the above(B) scenario:
1. Enable the default entry in access profiles named as: BLOCK APPLICATIONS (or)
2. Enable HTTPS inspection In the SafeSquid



## **Case 2 : There is a direct Internet access to the client Machine**
    

**A)HTTPS ENABLED**

**Any desk** :  Any desk is able to connect to the remote server (It should not use proxy settings if there is a direct Internet connection).

**Team viewer** : Team viewer is able to connect to the remote  server through proxy (It should use proxy settings, but if we apply blocking rules on proxy, then it will use direct Internet connection, so it is not possible to block team viewer with proxy in direct internet connection ).

**AmmyAdmin** : AmmyAdmin is not able to connect to  the remote  server through proxy.

    
**B) HTTPS DISABLED :**

**Any desk** : Any desk is able to connect to the remote server (It is not using proxy settings if there is a direct Internet connection).

**Team viewer** : Team viewer is able to connect to remote the server through proxy.

**AmmyAdmin** : AmmyAdmin is able to connect to the remote server through proxy.

How to block in the above(B) scenario:
1. It is not possible to block Any desk and team viewer with direct Internet connection, because they don't use the proxy settings configured in settings.
2. You can block AmmyAdmin by enabling default entry in Access profiles (or) By enabling HTTPS Inspection.

