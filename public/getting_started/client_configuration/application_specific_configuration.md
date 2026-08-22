---
title: "Application-Specific Configuration"
description: Configure proxy settings for tools that do not inherit browser or operating system proxy settings.
keywords:
  - SafeSquid application proxy
  - Git proxy
  - Docker proxy
  - npm proxy
  - pip proxy
  - command-line proxy
---

# Handle Applications That Bypass OS Proxy

Some applications ignore browser, PAC, or operating system proxy settings. Developer tools, package managers, containers, email clients, and command-line utilities can create unlogged egress unless they are configured directly or blocked from direct internet access.

## Use this method when

Use application-specific configuration when:

- A tool does not appear in SafeSquid access logs.
- Developers or administrators use package managers.
- Command-line tools need controlled internet access.
- Business applications require explicit proxy fields.

Do not use application exceptions to bypass security review. Every exception should have an owner, scope, and expiry or review date.

## Validate prerequisites

Confirm:

- Host or browser proxy routing has already been tested.
- Proxy host, port, and authentication requirements are known.
- Direct internet egress is restricted where possible.
- Tool-specific credentials are not stored in plain text unless the risk is accepted.
- Application owner can test normal business workflow after the change.

## Configure common tools

Use the tabs for frequently approved developer and operations tools. Replace `SAFESQUID-IP` with the approved proxy address and add authentication only through the organization's approved secret-handling method.

<Tabs>
  <Tab title="Git">

```bash
git config --global http.proxy http://SAFESQUID-IP:8080
git config --global https.proxy http://SAFESQUID-IP:8080
git config --global --get http.proxy
```

Expected result: Git reports the configured proxy and repository requests appear in SafeSquid access logs.

Exempt internal Git hosts so they are not routed outward:

```bash
git config --global http.noProxy "*.internal.example.com"
```

To remove the configuration during rollback:

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

  </Tab>
  <Tab title="npm">

```bash
npm config set proxy http://SAFESQUID-IP:8080
npm config set https-proxy http://SAFESQUID-IP:8080
npm config get proxy
```

Expected result: npm package requests route through SafeSquid and match package-management policy.

Set the registry explicitly where an internal mirror is in use, so package resolution is not left to whatever the client defaults to:

```bash
npm config set registry https://registry.npmjs.org/
```

To remove the configuration during rollback:

```bash
npm config delete proxy
npm config delete https-proxy
```

  </Tab>
  <Tab title="pip">

Use a per-user or managed configuration file where approved:

```ini
[global]
proxy = http://SAFESQUID-IP:8080
```

The file location differs by platform: `~/.pip/pip.conf` on Linux and macOS, `%APPDATA%\pip\pip.ini` on Windows.

For a single command without changing configuration:

```bash
pip install --proxy http://SAFESQUID-IP:8080 <package>
```

Verify:

```bash
python -m pip config list
```

  </Tab>
  <Tab title="APT">

Configure Debian or Ubuntu package traffic through an approved APT proxy file:

```text
Acquire::http::Proxy "http://SAFESQUID-IP:8080";
Acquire::https::Proxy "http://SAFESQUID-IP:8080";
```

Store the file through configuration management, then test with a controlled package metadata refresh.

  </Tab>
  <Tab title="YUM/DNF">

Configure RHEL, CentOS, or Fedora package traffic in the approved package-manager configuration:

```ini
proxy=http://SAFESQUID-IP:8080
```

Verify with a metadata refresh and confirm the source IP appears in SafeSquid logs.

  </Tab>
</Tabs>

<Accordion title="Command-line tools: curl and wget">

Use direct proxy flags for one-off tests or scripted jobs:

```bash
curl -I --proxy http://SAFESQUID-IP:8080 http://example.com
wget -e use_proxy=yes -e http_proxy=http://SAFESQUID-IP:8080 http://example.com
```

Expected result: the request succeeds and appears in SafeSquid access logs.

For persistent per-user configuration, both tools read a dotfile:

```
# ~/.curlrc
proxy = "http://SAFESQUID-IP:8080"
```

```
# ~/.wgetrc
http_proxy = http://SAFESQUID-IP:8080
https_proxy = http://SAFESQUID-IP:8080
use_proxy = on
```

</Accordion>

<Accordion title="Docker and container runtimes">

Configure Docker proxy settings through the organization's approved daemon or systemd method. Use placeholders for authentication material and store credentials in the approved secret store.

```bash
HTTP_PROXY=http://SAFESQUID-IP:8080
HTTPS_PROXY=http://SAFESQUID-IP:8080
NO_PROXY=localhost,127.0.0.1,.internal.example.com
```

Restart the container runtime only in an approved change window. Confirm image pulls and registry metadata requests appear in SafeSquid logs.

The daemon also reads a `proxies` block from `/etc/docker/daemon.json`, which survives service restarts without depending on the unit environment:

```json
{
  "proxies": {
    "http-proxy": "http://SAFESQUID-IP:8080",
    "https-proxy": "http://SAFESQUID-IP:8080",
    "no-proxy": "localhost,127.0.0.1,.internal.example.com"
  }
}
```

Reload the daemon in an approved window, then confirm it took effect:

```bash
docker info | grep -i proxy
```

Expected result: the proxy values appear in the daemon configuration. Note that this configures the daemon, which pulls images — containers themselves receive proxy settings separately, through their own environment.

</Accordion>

<Accordion title="Email clients: Outlook and Thunderbird">

Outlook and Thunderbird can use operating-system proxy settings, but some profiles, add-ins, or mail transports bypass them. Configure proxy settings through the approved desktop-management path and test mailbox sign-in, attachment download, and autodiscover traffic.

Record the mail domains, identity method, and whether SSL inspection is bypassed because of certificate pinning or application behavior.

**Outlook on Windows** inherits the Windows proxy for Exchange and Microsoft 365 accounts, so no separate configuration is usually needed. Where it is:

1. **File → Account Settings → Account Settings**.
2. Select the account, then **Change → More Settings**.
3. On the **Connection** tab, select **Connect using Internet Explorer or a 3rd party dialer**, which routes Outlook through the Windows system proxy.

If Outlook will not connect after the change, temporarily disabling Cached Exchange Mode isolates whether the failure is in the connection or the local cache.

**Thunderbird** keeps its own settings and ignores the OS configuration:

1. Menu (☰) **→ Settings → General**.
2. Scroll to **Network & Disk Space** and select **Connection Settings**.
3. Choose **Manual proxy configuration**, set the HTTP proxy and port `8080`, and enable **Use this proxy server for all protocols**.
4. Set **No Proxy for** to the approved internal entries, then select **OK**.

</Accordion>

<Accordion title="Applications not listed here">

For anything else, work through these in order:

1. Check the application's own documentation for a proxy setting.
2. Try the standard environment variables — many tools honour them:

   ```bash
   export http_proxy=http://SAFESQUID-IP:8080
   export https_proxy=http://SAFESQUID-IP:8080
   ```

3. Look for a configuration file: `~/.config/<app>/` or `~/.<app>/` on Linux and macOS, `%APPDATA%\<App>\` on Windows.
4. Check for a command-line flag such as `--proxy`, `-x`, or `--http-proxy`.

Common runtime patterns:

| Runtime | Setting |
|---|---|
| Java | `-Dhttp.proxyHost=SAFESQUID-IP -Dhttp.proxyPort=8080` |
| Ruby gems | `gem install --http-proxy http://SAFESQUID-IP:8080 <package>` |
| Go modules | `export GOPROXY=http://SAFESQUID-IP:8080` |

Any tool that cannot be routed needs a recorded exception with an owner and a review date, not a silent direct path to the internet.

</Accordion>

<Note>
  Do not store proxy passwords in plain text application config files unless the risk is documented and accepted.
</Note>

## Verify application evidence

After configuring the tool:

1. Run one safe external request.
2. Run one internal request that should bypass SafeSquid, if applicable.
3. Inspect SafeSquid access logs.

```bash
tail -20 /var/log/safesquid/access/extended.log
```

Expected result: external tool traffic appears with source, destination, timestamp, and action.

## Capture exception evidence

Store:

- Application name and owner.
- Hostname or managed group.
- Proxy setting applied.
- Bypass entries.
- Access-log sample.
- Credential-storage decision, if authentication is used.
- Review or expiry date for the exception.

## Troubleshoot application failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Tool still bypasses SafeSquid | Tool ignores OS settings and lacks direct proxy config | Apply the tool-specific proxy setting |
| Authentication fails | Tool cannot use the configured credential method | Use an approved credential mechanism or scoped service account |
| Internal repository fails | Missing bypass for internal destination | Add an exact internal bypass entry |
| Traffic appears without user context | Tool runs as service or system account | Document service identity and add authentication mapping if required |
| Package manager works outside SafeSquid | Direct egress is still open | Restrict direct internet routes and retest through SafeSquid |
| `SSL certificate verify failed` | SSL inspection is active and the tool does not trust the SafeSquid root CA | Install the root CA into the trust store the tool uses; language runtimes often keep their own, separate from the OS |
| `docker pull` fails while other traffic works | Registry host is not in the no-proxy list, or is being proxied when it should not be | Add the registry to `no-proxy`, or confirm the proxy path allows registry traffic |
| `git clone` is unusually slow | Large repository plus proxy overhead | Use SSH rather than HTTPS for large clones, or bypass the proxy for internal Git hosts |

## Next steps

- [Enterprise Deployment](/getting_started/client_configuration/enterprise_deployment) - enforce settings centrally.
- [Configure Web Security Policies](/getting_started/configure_web_security_policies) - apply controls to routed application traffic.
- [Troubleshooting](/troubleshooting/troubleshooting) - diagnose client and policy failures.
