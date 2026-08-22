---
title: "Enterprise Deployment"
description: "Centralized proxy configuration deployment for SafeSquid SWG using Group Policy Objects, Active Directory, and configuration management tools"
keywords:
  - SafeSquid enterprise deployment
  - GPO proxy configuration
  - Active Directory proxy
  - enterprise proxy management
  - centralized proxy deployment
  - configuration management
---

# Enterprise Deployment

**Enterprise deployment** pushes proxy settings to hundreds or thousands of endpoints using centralized management tools—Group Policy (Windows), MDM (macOS/mobile), or config management (Puppet, Ansible, SCCM).

**Use this method for:**
- Production deployments (100+ endpoints)
- Organization-wide rollouts
- Centralized control and enforcement
- Automated updates without touching each machine

**Time to deploy:** Initial setup 1-2 hours, then automatic for all endpoints

:::tip Start Small

Test on a pilot group (5-10 users) before rolling out to the entire organization. This catches configuration issues before they affect everyone.

:::

## Prerequisites

:::info Before You Start

**For Windows (GPO):**
- Active Directory environment
- Group Policy Management Console access
- Domain-joined Windows clients
- PAC file hosted on internal web server (or explicit proxy settings decided)

**For macOS (MDM):**
- MDM solution (Jamf, Intune, Workspace ONE)
- Enrolled macOS devices
- Administrator access to MDM console

**For Linux (Config Management):**
- Puppet, Ansible, Chef, or SaltStack
- Managed Linux nodes
- SSH access to management server

:::

## Which Method Should I Use?

| **Environment** | **Recommended Tool** | **Why** |
|-----------------|----------------------|---------|
| 100% Windows, domain-joined | **Group Policy (GPO)** | Built into Active Directory, no extra software |
| Mixed Windows/Mac, Azure AD | **Microsoft Intune** | Unified management for Windows + macOS |
| macOS only | **Jamf Pro** or **Intune** | MDM designed for Apple devices |
| Linux servers/workstations | **Ansible** or **Puppet** | Industry-standard config management |
| Mixed Windows/Linux, no AD | **Ansible** | Agentless, works over SSH |
| Existing SCCM deployment | **SCCM** | Reuse existing infrastructure |

## Windows: Group Policy (GPO)

### Create the GPO

1. **Open Group Policy Management Console** (gpmc.msc)
2. **Right-click** your domain or OU → **Create a GPO in this domain**
3. **Name it:** "SafeSquid Proxy Configuration"
4. **Right-click the new GPO** → **Edit**

---

### Configure Proxy Settings

**Option A: PAC File (Recommended)**

1. Navigate to:
   ```
   Computer Configuration → Policies → Administrative Templates → 
   Windows Components → Internet Explorer
   ```

2. **Double-click:** "Use automatic configuration script"
3. **Enable** it
4. **Enter PAC URL:** `http://pac-server.company.com/proxy.pac`
5. Click **OK**

6. **Double-click:** "Disable changing proxy settings"
7. **Enable** (prevents users from changing proxy)
8. Click **OK**

---

**Option B: Explicit Proxy (if not using PAC)**

1. Navigate to:
   ```
   Computer Configuration → Preferences → Windows Settings → Registry
   ```

2. **Right-click** → **New** → **Registry Item**

3. **Create these entries:**

| **Registry Value** | **Type** | **Data** |
|--------------------|----------|----------|
| **ProxyEnable** | REG_DWORD | `1` |
| **ProxyServer** | REG_SZ | `192.168.1.100:8080` |
| **ProxyOverride** | REG_SZ | `*.local;*.company.com;localhost;127.0.0.1` |

**Path for all three:**
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
```

**Action:** Update (not Create, to avoid errors on reapply)

---

### Link and Apply GPO

1. **Close the Group Policy Editor**
2. **Right-click the GPO** → **Link an Existing GPO**
3. **Select:** The OU containing your target computers
4. **Wait 15-90 minutes** for automatic Group Policy refresh, or force:
   ```powershell
   # On a client machine:
   gpupdate /force
   ```

---

### Verify GPO Deployment

**On a client machine:**

```powershell
# Check which GPOs applied:
gpresult /r

# Detailed report (HTML):
gpresult /h c:\gp-report.html
```

Look for your "SafeSquid Proxy Configuration" GPO in the output.

**Check registry directly:**

```powershell
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
```

Should show `ProxyEnable = 1` and `ProxyServer = 192.168.1.100:8080`

---

### Rollback Procedure

**If deployment causes issues:**

1. **Unlink the GPO:**
   - Group Policy Management → Right-click the link → **Delete link**
   - This stops enforcement immediately (doesn't delete the GPO)

2. **Force client update:**
   ```powershell
   gpupdate /force
   ```

3. **Clients revert to previous settings** within 15-90 minutes (or immediately with gpupdate)

---

## macOS: MDM (Intune / Jamf)

### Microsoft Intune

1. **Intune admin center** → **Devices** → **Configuration profiles**
2. **Create profile** → Platform: **macOS**, Profile type: **Settings catalog**
3. **Add settings:**
   - Search: **Proxy**
   - Select: **Network → Proxy → Web Proxy**
   - **Web Proxy Server:** `192.168.1.100`
   - **Web Proxy Server Port:** `8080`
   - **Bypass proxy settings for these Hosts & Domains:** `*.local, localhost, 127.0.0.1`
4. **Assign** to macOS device group
5. **Create** and wait for devices to check in (~15 minutes)

---

### Jamf Pro

1. **Computers** → **Configuration Profiles** → **New**
2. **Network** → Configure
3. **Proxies tab:**
   - **Web Proxy (HTTP):** Enable
   - **Proxy Server:** `192.168.1.100:8080`
   - **Bypass Proxy:** `*.local, localhost, 127.0.0.1`
4. **Scope** to target computer group
5. **Save** — devices apply on next check-in

---

## Linux: Ansible

**Create playbook** (`safesquid-proxy.yml`):

```yaml
---
- name: Deploy SafeSquid Proxy Configuration
  hosts: all
  become: yes
  tasks:
    - name: Configure system proxy in /etc/environment
      lineinfile:
        path: /etc/environment
        line: "{{ item }}"
        create: yes
      loop:
        - 'http_proxy="http://192.168.1.100:8080"'
        - 'https_proxy="http://192.168.1.100:8080"'
        - 'ftp_proxy="http://192.168.1.100:8080"'
        - 'no_proxy="localhost,127.0.0.1,*.local,*.company.com"'

    - name: Configure APT proxy (Debian/Ubuntu)
      copy:
        dest: /etc/apt/apt.conf.d/95proxies
        content: |
          Acquire::http::Proxy "http://192.168.1.100:8080";
          Acquire::https::Proxy "http://192.168.1.100:8080";
      when: ansible_os_family == "Debian"

    - name: Configure YUM proxy (RHEL/CentOS)
      lineinfile:
        path: /etc/yum.conf
        line: "proxy=http://192.168.1.100:8080"
      when: ansible_os_family == "RedHat"

    - name: Create profile.d proxy script
      copy:
        dest: /etc/profile.d/proxy.sh
        mode: '0644'
        content: |
          export http_proxy=http://192.168.1.100:8080
          export https_proxy=http://192.168.1.100:8080
          export no_proxy=localhost,127.0.0.1,*.local
```

**Deploy:**

```bash
# Test on one host first:
ansible-playbook -i inventory safesquid-proxy.yml --limit testhost

# Deploy to all:
ansible-playbook -i inventory safesquid-proxy.yml
```

**Rollback:**

Create `remove-proxy.yml`:

```yaml
---
- name: Remove SafeSquid Proxy Configuration
  hosts: all
  become: yes
  tasks:
    - name: Remove proxy lines from /etc/environment
      lineinfile:
        path: /etc/environment
        regexp: '.*proxy.*'
        state: absent

    - name: Remove APT proxy config
      file:
        path: /etc/apt/apt.conf.d/95proxies
        state: absent

    - name: Remove YUM proxy config
      lineinfile:
        path: /etc/yum.conf
        regexp: '^proxy='
        state: absent

    - name: Remove profile.d proxy script
      file:
        path: /etc/profile.d/proxy.sh
        state: absent
```

Run: `ansible-playbook -i inventory remove-proxy.yml`

---

## Linux: Puppet

**Create module** (`/etc/puppetlabs/code/environments/production/modules/safesquid_proxy/manifests/init.pp`):

```puppet
class safesquid_proxy (
  String $proxy_server = '192.168.1.100:8080',
  String $no_proxy = 'localhost,127.0.0.1,*.local,*.company.com',
) {

  # Configure /etc/environment
  file { '/etc/environment':
    ensure  => file,
    content => template('safesquid_proxy/environment.erb'),
  }

  # Configure profile.d script
  file { '/etc/profile.d/proxy.sh':
    ensure  => file,
    mode    => '0644',
    content => epp('safesquid_proxy/proxy.sh.epp', {
      'proxy_server' => $proxy_server,
      'no_proxy'     => $no_proxy,
    }),
  }

  # APT proxy (Debian/Ubuntu)
  if $facts['os']['family'] == 'Debian' {
    file { '/etc/apt/apt.conf.d/95proxies':
      ensure  => file,
      content => "Acquire::http::Proxy \"http://${proxy_server}\";\nAcquire::https::Proxy \"http://${proxy_server}\";\n",
    }
  }

  # YUM proxy (RHEL/CentOS)
  if $facts['os']['family'] == 'RedHat' {
    ini_setting { 'yum_proxy':
      path    => '/etc/yum.conf',
      section => 'main',
      setting => 'proxy',
      value   => "http://${proxy_server}",
    }
  }
}
```

**Create template** (`modules/safesquid_proxy/templates/proxy.sh.epp`):

```bash
export http_proxy=http://<%= $proxy_server %>
export https_proxy=http://<%= $proxy_server %>
export no_proxy=<%= $no_proxy %>
```

**Apply to nodes** (`site.pp`):

```puppet
node 'workstation*.company.com' {
  include safesquid_proxy
}
```

---

## Verify Deployment

**Sample 5-10 endpoints from different groups:**

**Windows:**
```powershell
gpresult /r
netsh winhttp show proxy
```

**macOS:**
```bash
scutil --proxy
```

**Linux:**
```bash
env | grep proxy
cat /etc/environment
```

**Test connectivity on each:**

```bash
curl -I http://example.com
```

Check SafeSquid logs for requests from those IPs.

---

## Troubleshooting

| **Symptom** | **Likely Cause** | **Fix** |
|-------------|------------------|---------|
| GPO not applying to client | Wrong OU link or client not in domain | Run `gpresult /r` on client, check GPO link in GPMC |
| GPO applied but proxy not working | Registry values incorrect | Check `HKCU:\...\Internet Settings` manually |
| MDM profile shows "Error" | Enrollment issue or syntax error | Check MDM logs, re-send profile |
| Ansible fails on some hosts | SSH connectivity or sudo access | Test: `ansible all -m ping`, check SSH keys |
| Puppet agent not checking in | Puppet agent stopped or network issue | `systemctl status puppet`, `puppet agent -t` |
| PAC file not loading on clients | DNS issue or firewall blocking | Test: `nslookup pac-server.company.com`, `curl http://pac-server.company.com/proxy.pac` |

**Still not working?**

1. **Verify management tool connectivity:**
   - GPO: `gpupdate /force` then `gpresult /r`
   - Ansible: `ansible all -m ping`
   - Puppet: `puppet agent -t --verbose`

2. **Check one endpoint manually:**
   - Apply settings manually (Explicit Proxy method)
   - If manual works, issue is deployment tool
   - If manual fails, issue is SafeSquid or network

3. **Check SafeSquid accessibility from clients:**
   ```bash
   telnet safesquid-ip 8080
   ```

## Best Practices

### Staged Deployment

1. **Pilot group** (5-10 users) → 1 week
2. **Early adopters** (50-100 users) → 1 week
3. **Department by department** → 2-4 weeks
4. **Full deployment**

Monitor logs and support tickets at each stage.

---

### PAC File Hosting

- **Host on redundant web servers** (not a single point of failure)
- **Use internal DNS** (`pac.company.local`)
- **Version control** PAC file changes (Git)
- **Test changes** in staging before production

---

### Monitoring

- **Group Policy Modeling** (GPMC) to predict impact before deploying
- **Configuration compliance reports** (weekly)
- **Alert on proxy configuration drift**
- **SafeSquid log analysis** to confirm traffic from managed endpoints

---

## Next Steps

1. **[Verify Your Setup](/docs/Getting_Started/Verify_Your_Setup/)** — Sample endpoints to confirm proxy is working
2. **[SSL Inspection](/docs/SSL_Inspection/main/)** — Deploy root CA via GPO/MDM for HTTPS inspection
3. **[Configure Policies](/docs/Access_Restriction/main/)** — Now that all traffic flows through SafeSquid, set up access controls
4. **Monitor and iterate** — Review logs, support tickets, and user feedback to refine configuration
