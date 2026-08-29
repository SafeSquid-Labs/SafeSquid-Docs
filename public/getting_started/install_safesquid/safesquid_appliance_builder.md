---
title: SafeSquid Appliance Builder
description: Build a security-hardened Debian appliance with SafeSquid, Monit, and BIND9 preinstalled, using the SAB ISO on new bare metal or a virtual machine.
keywords:
  - SafeSquid Appliance Builder
  - SAB ISO
  - Debian appliance install
  - preseed appliance build
  - SafeSquid installation
---

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/01-SafeSquid_Appliance_Builder.md (whole page) and _old_getting_started_backup/03-Installation Guide/01-SafeSquid Appliance Builder.md §Preparation, §Installation Steps (Debian), §Post-Installation Checklist */}
{/* NEEDS-SME-REVIEW: the two sources give opposite BIOS boot orders — the current guide says removable media first, the older backup says hard disk first. Confirm before an operator follows either. */}
{/* NEEDS-SME-REVIEW: minimum RAM and disk are stated four different ways — 8 GB/100 GB in the SAB source, 4 GB/160 GB in quickstart.mdx, no disk figure in the sizing matrix, and a 32 GB disk in the installer screenshots. Confirm the authoritative baseline for the shipping release. */}
{/* NEEDS-SME-REVIEW: the boot menu reads "debian 13" but the first-login banner reads "built using Linux #236-Ubuntu SMP". Both sources describe SAB as a Debian ISO. Confirm the shipping base OS. */}
{/* NEEDS-SME-REVIEW: both sources give the portal as https://safesquid.cfg/ while 43 other pages in public/ use http://. This page uses http:// for internal consistency — confirm which is correct. */}
{/* NEEDS-SME-REVIEW: the /usr/local/safesquid/ row in the component table appears in neither source. Confirm the path before an operator relies on it. */}

# Build the Standard Appliance

Installing SafeSquid by hand means hardening the OS, partitioning disks correctly, resolving dependency libraries, configuring networking, and standing up Monit and BIND9. One mistake in partitioning or networking costs hours — and it costs them again on the next node, because nothing about the build is repeatable.

SafeSquid Appliance Builder (SAB) is a security-hardened Debian ISO that does all of it from one boot. You answer a short sequence of prompts; a preseed script does the rest and reboots into a working appliance.

## Use this method when

Use SAB when:

- You are building a new dedicated SafeSquid appliance.
- The deployment can boot from an ISO.
- The organisation wants a repeatable baseline instead of adapting an existing server.
- You need a clean VM or hardware appliance for production, pilot, or DR testing.

Do not use SAB when the host must preserve an existing OS, application stack, or custom hardening image — the install erases the target disk. Use [Install on a Managed Linux Host](/getting_started/install_safesquid/linux_server) instead.

## Know what SAB automates

| SAB does | So you do not have to |
|---|---|
| Installs a security-hardened Debian base | Harden the OS by hand |
| Partitions the disk with separate volumes for `/`, `/var/log/safesquid`, and `/var/lib/safesquid` | Design a layout that keeps log writes off the root volume |
| Installs SafeSquid and every dependency | Resolve library versions per distribution |
| Pre-configures Monit for process supervision and BIND9 for local DNS | Stand up supporting services separately |
| Disables unnecessary services and configures the host firewall | Apply a hardening baseline manually |
| Sets SafeSquid to start on boot | Remember to enable the unit |

The separate log and cache volumes matter more than they look. A shared root volume that fills stops the appliance and truncates the audit trail at the same time.

## Validate prerequisites

Before booting the ISO, confirm:

- CPU, RAM, disk, and NIC allocation match the sizing plan in [Sizing](/deployment/sizing).
- The CPU exposes AES-NI. SSL inspection performance depends on it.
- The VM or hardware can boot from the SAB ISO.
- Static IP, gateway, DNS, and NTP values are approved and unique within the subnet.
- Outbound access is available for packages, updates, activation, and subscription checks. See [Ports and Firewall Rules](/deployment/ports_and_firewall_rules).
- The activation key is available for post-install activation. Obtain it from [Register Your Key](/getting_started/register).
- A rollback or rebuild plan exists for the VM or hardware.

Obtain the ISO from the SafeSquid appliance download path:

```text
https://downloads.safesquid.com/appliance/safesquid.iso
```

Record the download date and, where the organisation's process requires it, a checksum of the retrieved image in the change record.

<Accordion title="Prepare physical hardware">

1. Write the ISO to USB or DVD. Rufus, Etcher, and `dd` all work for USB; ImgBurn for CD or DVD. Use whichever is approved for the administrator workstation.
2. Set the BIOS or UEFI boot order so the removable media is tried **before** the internal disk, and disable Secure Boot if the installer will not start.
3. Confirm the CPU exposes AES-NI before committing the hardware:

   ```bash
   lscpu | grep aes
   ```

   Expected result: `aes` appears in the CPU flags. If it does not, HTTPS inspection will be substantially slower on this host — see the AES-NI requirement in [Sizing](/deployment/sizing).

</Accordion>

<Accordion title="Prepare a virtual machine">

SAB runs on both Type 1 and Type 2 hypervisors. On a Type 2 hypervisor such as VirtualBox or VMware Workstation, host-to-VM connectivity has to be established deliberately.

1. Create the VM on VMware, Hyper-V, KVM, or VirtualBox.
2. Attach the ISO as a virtual CD or DVD drive.
3. Choose the network mode:

   | Mode | Behaviour | Use when |
   |---|---|---|
   | **Bridged adapter** | The VM gets its own address on the network, bypassing the host | Production and any deployment clients must reach |
   | **NAT** | The VM sits behind the host, routing through the host's address | Isolated lab only |

   Bridged is the recommended choice. NAT complicates client routing and certificate testing later.
4. Allocate CPU, RAM, and disk according to the approved sizing plan, and confirm the hypervisor actually reserves them rather than overcommitting.

</Accordion>

<Warning>
  **Destructive disk operation:** SAB erases and repartitions the selected disk. Back up any existing data first. Do not continue unless the VM or hardware is dedicated to SafeSquid and rollback means a rebuild, not data recovery.
</Warning>

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/01-SafeSquid_Appliance_Builder.md §Before You Begin */}

Obtain the ISO from the SafeSquid appliance download path:

```text
https://downloads.safesquid.com/appliance/safesquid.iso
```

Record the download date and, where the organization's process requires it, a checksum of the retrieved image in the change record.

<Accordion title="Prepare physical hardware">

1. Write the ISO to USB or DVD. Rufus, Etcher, and `dd` all work; use whichever is approved for the administrator workstation.
2. Set the BIOS or UEFI boot order so removable media is tried before the internal disk.
3. Confirm the CPU exposes AES-NI before committing the hardware. SSL inspection performance depends on it:

   ```bash
   lscpu | grep aes
   ```

   Expected result: `aes` appears in the CPU flags. If it does not, HTTPS inspection will be substantially slower on this host.

</Accordion>

<Accordion title="Prepare a virtual machine">

1. Create the VM on VMware, Hyper-V, KVM, or VirtualBox.
2. Attach the ISO as a virtual CD or DVD drive.
3. Configure networking as **bridged** so the appliance holds a routable address on the client network. NAT works for an isolated lab but complicates client routing and certificate testing later.
4. Allocate CPU, RAM, and disk according to the approved sizing plan, and confirm the hypervisor actually reserves them rather than overcommitting.

</Accordion>

<Warning>
  **Default credentials:** the appliance ships with the account `administrator` and the password `safesquid`. Change the password at first login, before the host is reachable from any client network:

  ```bash
  passwd
  ```

  Record that the change was made in the deployment evidence. Leaving the shipped password in place on a proxy that sees all corporate web traffic is a direct compromise path.
</Warning>

## Install the appliance

<Steps>
  <Step title="Boot the ISO and choose an installation mode">
    Attach the SAB ISO and boot the target host from it. The menu offers **Standard Installation**, **Expert Installation**, **Serial Console Installation (Standard)**, and **Serial Console Installation (Expert)**.

    Confirm **Standard Installation** is selected. It is the recommended path and the one this page documents.

    If the host is reachable only over a serial console, use the matching serial variant — the prompt sequence is the same.

    ![SafeSquid Appliance Builder boot menu showing Standard, Expert, and two Serial Console installation modes](/images/getting_started/safesquid_appliance_builder_01_sab_boot_menu.webp)
  </Step>
  <Step title="Choose DHCP or static addressing">
    Select **Yes** to configure networking automatically by DHCP, or **No** to assign a static address manually.

    Confirm the choice matches the approved network plan. Production appliances use a static address.

    If DHCP is selected for a production host, restart the installer — a proxy whose address moves breaks every client that points at it.

    ![Network autoconfiguration prompt asking whether to use DHCP](/images/getting_started/safesquid_appliance_builder_02_dhcp_prompt.webp)
  </Step>
  <Step title="Select language, location, and keyboard">
    The language applies to both the installer and the installed system. The location sets the appliance **time zone**. The keyboard layout follows the keyboard's country of origin.

    Confirm the time zone matches the one your log timestamps must correlate against, and the keyboard layout matches the hardware.

    If the time zone is wrong, log entries will not line up with other systems during an incident. A mismatched keyboard layout causes input errors on non-standard keyboards, which is easy to misdiagnose while typing a password.

    ![Installer language selection screen](/images/getting_started/safesquid_appliance_builder_03_language.webp)

    ![Installer location selection screen, which sets the appliance time zone](/images/getting_started/safesquid_appliance_builder_04_location.webp)

    ![Installer keyboard layout configuration screen](/images/getting_started/safesquid_appliance_builder_05_keyboard.webp)
  </Step>
  <Step title="Assign the static IP address">
    Skip this step if DHCP was selected. Otherwise enter the address with its CIDR prefix appended, in the form `IP/subnet` — for example `192.168.1.50/24`.

    Confirm the address falls inside the subnet range the network team defined, and is unique on that network.

    If the address collides with an existing host, the conflict surfaces intermittently after rollout rather than at install time. Check the allocation record before continuing.

    ![Installer prompt for the static IP address with CIDR netmask](/images/getting_started/safesquid_appliance_builder_06_static_ip.webp)
  </Step>
  <Step title="Specify the gateway">
    Enter the default gateway address. Where a router forwards traffic from the local network to other networks, that router's address is the gateway.

    Confirm the gateway is reachable **from the address you just assigned**, not merely that it is correct in general.

    If the gateway is unreachable, the installer fails later at mirror selection rather than here, so the real cause surfaces several screens away.

    ![Installer prompt for the default gateway address](/images/getting_started/safesquid_appliance_builder_07_gateway.webp)
  </Step>
  <Step title="Set the name servers">
    Enter the DNS servers, space-separated. Provide a primary and a secondary for redundancy.

    Confirm both resolve names correctly from the appliance network.

    If only one resolver is given and it fails, categorization and update paths fail with it — SafeSquid cannot categorise a destination it cannot resolve.

    ![Installer prompt for name server addresses](/images/getting_started/safesquid_appliance_builder_08_dns.webp)
  </Step>
  <Step title="Assign hostname and domain">
    Set a hostname that fits your naming convention, then the domain name.

    Confirm the resulting fully qualified domain name is the one you intend, and that both forward and reverse DNS entries exist for it.

    If the FQDN is wrong, directory integration is the first thing to break — Active Directory integration depends on it. Changing the hostname later means revisiting certificate and logging references, so settle it now.

    ![Installer prompt for the appliance hostname](/images/getting_started/safesquid_appliance_builder_09_hostname.webp)

    ![Installer prompt for the domain name](/images/getting_started/safesquid_appliance_builder_10_domain.webp)
  </Step>
  <Step title="Select the package mirror">
    Choose the Debian archive mirror geographically closest to the server, preferring one known for bandwidth and uptime. Leave the HTTP proxy field blank unless your network requires an upstream proxy; the expected form is `http://[[user][:pass]@]host[:port]/`.

    Confirm the installer reaches the mirror and begins retrieving packages.

    If mirror selection hangs, outbound HTTP and HTTPS are blocked or an upstream proxy is required. Fix reachability before retrying.

    ![Installer prompt to choose a Debian archive mirror by country](/images/getting_started/safesquid_appliance_builder_11_mirror.webp)

    ![Installer prompt for HTTP proxy information, blank for none](/images/getting_started/safesquid_appliance_builder_12_http_proxy.webp)
  </Step>
  <Step title="Confirm the disk and the GRUB target">
    SAB auto-partitions the selected disk. Select the target drive — typically `/dev/sda` or `/dev/nvme0n1` — for partitioning, then the same drive again for the GRUB bootloader.

    Confirm the selected disk matches the allocation approved for SafeSquid, and that the GRUB target is the same internal disk.

    If you are installing from a USB stick, unselect the USB drive at the partitioning prompt so it cannot be chosen by mistake.

    ![Disk partitioning prompt listing available disks](/images/getting_started/safesquid_appliance_builder_14_disk_selection.webp)

    ![GRUB bootloader installation prompt listing available disks](/images/getting_started/safesquid_appliance_builder_15_grub.webp)
  </Step>
  <Step title="Wait for the automated build">
    The preseed script partitions the disk, installs the Debian base with security updates, installs SafeSquid with Monit and BIND9, applies hardening, and sets SafeSquid to start on boot. The host reboots by itself when it finishes.

    Confirm the progress screen advances and the host reboots without installer errors.

    If installation stops, capture the console error, correct package or network reachability, and rebuild from a clean boot.

    ![Installer progress screen showing base system installation](/images/getting_started/safesquid_appliance_builder_16_finishing_installation.webp)
  </Step>
  <Step title="Log in and reset the password">
    Remove the ISO, let the appliance boot, and log in at the console with the default credentials `administrator` / `safesquid`. The appliance requires a password reset on first login: re-enter the current password, then set and confirm a new one.

    Confirm the reset completes and the new password is stored under approved credential handling.

    If the host returns to the installer, remove the ISO from virtual media and check the boot order.

    ![Console login prompt showing the default credentials and first-login password reset notice](/images/getting_started/safesquid_appliance_builder_17_login_prompt.webp)
  </Step>
</Steps>

<Warning>
  **Do not defer the password reset.** The appliance ships with `administrator` / `safesquid`, and those credentials are printed on the login screen. Complete the reset before the host is reachable from any client network, and record that it was done in the deployment evidence. Leaving the shipped password in place on a proxy that sees all corporate web traffic is a direct compromise path.
</Warning>

<Warning>
  **Confirm the GRUB target disk.** The bootloader prompt is separate from the partitioning prompt, and it is easy to accept an external USB device instead of the internal disk. Installing GRUB to the wrong drive leaves the appliance unbootable once the media is removed.
</Warning>

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/01-SafeSquid_Appliance_Builder.md §Installation Steps step 6 SSH tip */}

<Accordion title="Continue the install over SSH">

Once network configuration completes, the installer offers to continue remotely. It displays the appliance address and a host-key fingerprint, and accepts a session as the user `installer`:

```bash
ssh installer@SAFESQUID-SERVER-IP
```

Expected result: the installer resumes in the SSH session at the prompt the console had reached.

Compare the displayed SHA256 fingerprint before accepting the host key. This is useful for a headless server or a remote data centre — treat it as a management-network action and connect from an approved administrator workstation, not from a general user network.

![Installer notice offering to continue the installation remotely over SSH](/images/getting_started/safesquid_appliance_builder_13_ssh_notice.webp)

</Accordion>

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/01-SafeSquid_Appliance_Builder.md §Monitoring Installation Progress */}

<Accordion title="Watch installation progress from another console">

The installer runs on a virtual console. Switch between consoles to see what it is actually doing, which matters when the main screen appears stuck.

| Keys | Console |
|---|---|
| **ALT + F1** | Main installation interface, the default view |
| **ALT + F2** | Live installation log, real-time progress and errors |
| **ALT + F3** | Shell prompt for troubleshooting |
| **ALT + F4** | System messages |

Switch to the live log (**ALT + F2**) when installation appears stuck, network configuration fails, or partitioning errors appear — it distinguishes a slow step from a failed one.

From the shell (**ALT + F3**):

```bash
tail -f /var/log/syslog
ping -c 3 8.8.8.8
lsblk
```

Expected result: the log advances, outbound connectivity succeeds, and the intended target disk is present and the size you expect.

</Accordion>

## Verify installation

After reboot, run these checks from the appliance console or over SSH.

Confirm the service is running:

```bash
systemctl status safesquid --no-pager
```

Expected result: `Active: active (running)` with no recent startup errors.

Confirm the proxy listener is bound:

```bash
ss -lntp | grep ':8080'
```

Expected result: SafeSquid is listening on `0.0.0.0:8080`.

Confirm the management interface answers, from an approved administrator network:

```text
https://SAFESQUID-SERVER-IP:8443/
```

Expected result: the SafeSquid admin login loads. If it prompts for license activation, the installation succeeded and the appliance is ready for [Activate Your License](/getting_started/activate).

{/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/01-SafeSquid_Appliance_Builder.md §What Gets Installed */}

<Accordion title="What the appliance installs, and where">

| Component | Location or detail |
|---|---|
| SafeSquid proxy | `/opt/safesquid/` — listens on port `8080` |
| Security, policy, and UI material | `/usr/local/safesquid/` |
| Monit | Process monitoring and automatic restart for SafeSquid |
| BIND9 | Local DNS resolver on port `53` |
| Logs | `/var/log/safesquid/` |
| Configuration Portal | `http://safesquid.cfg/` — an embedded interface reachable only through the proxy, and deliberately not resolved by SafeSquid's own DNS resolver |
| Direct management access | `https://SAFESQUID-SERVER-IP:8443/` — before a proxy is configured, or when the proxy path is unavailable |

Use the direct `:8443` path only from an approved administrator network. It bypasses the proxy path that every other client uses, so it changes the trust boundary and should not become the routine way in.

</Accordion>

{/* source: _migration_source_v3/_old_getting_started_backup/03-Installation Guide/01-SafeSquid Appliance Builder.md §Post-Installation Checklist and Recommendations */}

## Hand off to activation

The appliance is built but not yet enforcing. Complete these before treating it as a control:

1. Configure a browser to use the appliance as its proxy — see [Explicit Browser Proxy](/getting_started/client_configuration/explicit_proxy). The Configuration Portal is only reachable through the proxy path.
2. Activate the instance from the portal — see [Activate Your License](/getting_started/activate).
3. Set up HTTPS inspection and configure policy for your environment — see [SSL Inspection](/use_cases/ssl_inspection/ssl_inspection).
4. Install the SafeSquid certificate in the clients' desktop trust store — see [Import Certificate](/use_cases/ssl_inspection/import_certificate_chrome_ie).
5. Convert the appliance to SSH key-based login and disable password authentication for administrative access.

## Capture appliance evidence

Store these artifacts with the deployment record:

- Appliance hostname, FQDN, and IP address.
- VM or hardware asset identifier.
- ISO source, download date, and checksum where the process requires it.
- Disk and NIC allocation, and the disk selected for partitioning and GRUB.
- Service status and proxy listener output.
- Confirmation that the first-login password reset was completed, and by whom.
- First Configuration Portal access test.
- Activation key storage reference.

## Troubleshoot installation

| Symptom | Likely cause | Fix |
|---|---|---|
| Host does not boot from media | Boot order wrong, or Secure Boot enabled | Set removable media ahead of the internal disk and disable Secure Boot |
| Installation hangs at mirror selection | Outbound access blocked, an upstream proxy is required, or the gateway is unreachable from the assigned IP | Confirm outbound HTTP and HTTPS and gateway reachability; enter proxy details if the network requires one |
| `Failed to partition disk` | Disk in use, too small, or the wrong drive was selected | Confirm the target disk against the approved allocation; unselect the USB installation media and detach other drives |
| Appliance unbootable after removing media | GRUB was installed to the removable device | Reinstall, selecting the internal disk for the bootloader as well as for partitioning |
| Port `8080` not listening after reboot | SafeSquid failed to start | Run `systemctl status safesquid --no-pager` and check `/var/log/safesquid/safesquid.log` |
| Management interface unreachable on `:8443` | Host or network firewall blocks the port | Check host firewall rules with `iptables -L` and permit the port from the administrator network only |
| SSH connection refused after reboot | SSH is not running, or the address changed | Confirm the address with `ip addr`, then check `systemctl status ssh` |
| Directory integration fails after install | Hostname or domain does not produce the expected FQDN, or reverse DNS is missing | Correct the FQDN and confirm both forward and reverse DNS entries resolve |
| Log timestamps do not match other systems | Time zone set incorrectly at the location prompt | Correct the time zone before correlating evidence across systems |

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - open the Configuration Portal safely.
- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - prove pilot traffic flow.
