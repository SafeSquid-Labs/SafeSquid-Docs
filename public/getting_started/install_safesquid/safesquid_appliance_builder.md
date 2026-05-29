---
title: SafeSquid Appliance Builder
description: Deploy SafeSquid SWG with the standard Debian-based appliance path for new bare metal or virtual machine deployments.
keywords:
  - SafeSquid Appliance Builder
  - SAB ISO
  - SafeSquid appliance
  - Debian SafeSquid deployment
---

# Build the Standard Appliance

SafeSquid Appliance Builder (SAB) is the standard path for new SafeSquid deployments on bare metal or virtual machines. It provides a repeatable appliance build with SafeSquid and supporting services. Completion time depends on hardware, storage, network, and package mirror reachability; do not treat setup-time claims as guarantees.

## Use this method when

Use SAB when:

- You are building a new dedicated SafeSquid appliance.
- The deployment can boot from an ISO.
- The organization wants a repeatable baseline instead of adapting an existing server.
- You need a clean VM or hardware appliance for production, pilot, or DR testing.

Do not use SAB when the host must preserve an existing OS, application stack, or custom hardening image.

## Know what SAB installs

SAB builds a Debian-based SafeSquid appliance and prepares the supporting services needed for a repeatable proxy deployment.

<Steps>
  <Step title="Review the operating system baseline">
    <Card title="Operating system baseline" icon="box">
      Installs the appliance operating system, partitions the selected disk, and prepares the bootloader for the target host.
    </Card>

    Confirm the selected disk can be partitioned for the appliance baseline.

    If the disk contains retained data, stop and choose a different install path.
  </Step>
  <Step title="Review SafeSquid SWG installation">
    <Card title="SafeSquid SWG" icon="shield-check">
      Installs SafeSquid and the proxy service dependencies needed for first boot, activation, and policy configuration.
    </Card>

    Confirm SafeSquid service and dependencies are expected on first boot.

    If service state is unclear after install, inspect service logs before activation.
  </Step>
  <Step title="Review supporting services">
    <Card title="Supporting services" icon="activity">
      Prepares supporting components such as Monit for process monitoring and BIND9 for local DNS service where appliance behavior requires them.
    </Card>

    Confirm monitoring and DNS service expectations are included in operations handoff.

    If supporting services are unhealthy, resolve them before routing clients.
  </Step>
  <Step title="Review operational layout">
    <Card title="Operational layout" icon="database">
      Creates a layout intended for logs, cache, database, and appliance operations. Verify disk allocation against the production retention plan.
    </Card>

    Confirm disk allocation supports cache, logs, database, and retention requirements.

    If retention cannot be met, resize storage or adjust retention before production.
  </Step>
</Steps>

## Validate prerequisites

Before booting the ISO, confirm:

- CPU, RAM, disk, and NIC allocation match the sizing plan.
- The VM or hardware can boot from the SAB ISO.
- Static IP, gateway, DNS, and NTP values are approved.
- Internet access is available for packages, updates, activation, and subscription checks.
- Activation key is available for post-install activation.
- A rollback or rebuild plan exists for the VM or hardware.

## Install the appliance

<Steps>
  <Step title="Attach and boot the ISO">
    Attach the SAB ISO to the VM or physical server and boot the target host from the ISO.

    Confirm the SafeSquid Appliance Builder boot menu appears.

    If the host does not boot from ISO, reattach the ISO and set it as the first boot device.

    ![SafeSquid Appliance Builder boot menu](/images/getting_started/safesquid_appliance_builder_01_sab_boot_menu.webp)
  </Step>
  <Step title="Confirm the target disk">
    Select the target disk only after confirming it is dedicated to SafeSquid and safe to overwrite.

    Confirm the selected disk matches the VM or hardware allocation approved for SafeSquid.

    If the disk cannot be confirmed, stop the install and verify hypervisor or hardware storage mapping.

    ![SafeSquid Appliance Builder disk selection prompt](/images/getting_started/safesquid_appliance_builder_14_disk_selection.webp)
  </Step>
  <Step title="Enter approved network details">
    Provide approved static IP, gateway, DNS, hostname, domain, and package mirror details when prompted.

    Confirm DHCP, static IP, gateway, DNS, hostname, domain, mirror, and HTTP proxy prompts match the approved network plan.

    If mirrors or updates fail, verify DNS, gateway, outbound firewall policy, and any required upstream HTTP proxy.

    ![SafeSquid Appliance Builder DHCP prompt](/images/getting_started/safesquid_appliance_builder_02_dhcp_prompt.webp)

    ![SafeSquid Appliance Builder static IP prompt](/images/getting_started/safesquid_appliance_builder_06_static_ip.webp)

    ![SafeSquid Appliance Builder gateway prompt](/images/getting_started/safesquid_appliance_builder_07_gateway.webp)

    ![SafeSquid Appliance Builder DNS prompt](/images/getting_started/safesquid_appliance_builder_08_dns.webp)

    ![SafeSquid Appliance Builder hostname prompt](/images/getting_started/safesquid_appliance_builder_09_hostname.webp)

    ![SafeSquid Appliance Builder domain prompt](/images/getting_started/safesquid_appliance_builder_10_domain.webp)

    ![SafeSquid Appliance Builder package mirror prompt](/images/getting_started/safesquid_appliance_builder_11_mirror.webp)

    ![SafeSquid Appliance Builder HTTP proxy prompt](/images/getting_started/safesquid_appliance_builder_12_http_proxy.webp)
  </Step>
  <Step title="Monitor installation progress">
    Allow the appliance build to install the operating system, supporting services, and SafeSquid components. Keep console access open until the installer reaches the finishing screen.

    Confirm language, location, keyboard, SSH notice, GRUB, and finishing screens complete without installer errors.

    If installation stops, capture the console error, correct package or network reachability, and rebuild from a clean boot.

    ![SafeSquid Appliance Builder language selection](/images/getting_started/safesquid_appliance_builder_03_language.webp)

    ![SafeSquid Appliance Builder location selection](/images/getting_started/safesquid_appliance_builder_04_location.webp)

    ![SafeSquid Appliance Builder keyboard selection](/images/getting_started/safesquid_appliance_builder_05_keyboard.webp)

    ![SafeSquid Appliance Builder SSH notice](/images/getting_started/safesquid_appliance_builder_13_ssh_notice.webp)

    ![SafeSquid Appliance Builder GRUB installation prompt](/images/getting_started/safesquid_appliance_builder_15_grub.webp)

    ![SafeSquid Appliance Builder finishing installation screen](/images/getting_started/safesquid_appliance_builder_16_finishing_installation.webp)
  </Step>
  <Step title="Remove media and reboot">
    Remove the ISO when installation completes, then reboot into the installed appliance.

    Confirm the appliance reaches the login prompt after reboot.

    If the host returns to the installer, remove the ISO from virtual media and check boot order.

    ![SafeSquid Appliance Builder login prompt after reboot](/images/getting_started/safesquid_appliance_builder_17_login_prompt.webp)
  </Step>
</Steps>

The installation overwrites the selected target disk. Confirm the host is dedicated to SafeSquid before continuing.

<Warning>
  **Destructive disk operation:** SAB erases and repartitions the selected disk. Do not continue unless the VM or hardware is dedicated to SafeSquid and rollback is a rebuild, not data recovery.
</Warning>

## Verify installation

After reboot, run these checks before activation.

<Steps>
  <Step title="Confirm service state">
    Verify SafeSquid service health from the appliance console.

    ```bash
    systemctl status safesquid --no-pager
    ```

    Confirm SafeSquid is running or reports a clear service state ready for activation.

    If service state is failed or unclear, inspect service logs and rebuild if the appliance baseline is incomplete.
  </Step>
  <Step title="Confirm proxy listener">
    Verify the approved proxy listener is present.

    ```bash
    ss -lntp | grep ':8080'
    ```

    Confirm the approved proxy listener is present.

    If the listener is missing, check service state and startup logs before routing clients.
  </Step>
  <Step title="Confirm interface reachability">
    Open the Configuration Portal from a proxied pilot browser.

    ```text
    http://safesquid.cfg/
    ```

    Confirm the Configuration Portal loads through the SafeSquid proxy path.

    If the interface does not load, configure explicit proxy on the pilot browser and retry `http://safesquid.cfg/`.
  </Step>
</Steps>

## Capture appliance evidence

Store:

- Appliance hostname and IP address.
- VM or hardware asset identifier.
- ISO source and install date.
- Disk and NIC allocation.
- Service status output.
- Proxy listener check.
- First Configuration Portal access test.
- Activation key storage reference.

## Troubleshoot installation

| Symptom | Likely cause | Fix |
|---|---|---|
| Host does not boot from ISO | Boot order or hypervisor media setting is wrong | Reattach ISO and set it as first boot device |
| Installer cannot reach mirrors | DNS, gateway, or outbound firewall is blocked | Fix network settings and retry installation |
| Service is not running after reboot | Installation did not complete cleanly | Check service logs and rebuild if the appliance baseline is incomplete |
| Interface does not load | Pilot browser is not proxied through SafeSquid | Configure explicit proxy and retry `http://safesquid.cfg/` |

## Next steps

- [Access the Interface](/getting_started/access_the_interface) - open the Configuration Portal safely.
- [Activate Your License](/getting_started/activate) - apply the activation key.
- [Connect Your Client](/getting_started/client_configuration/connect_your_client) - prove pilot traffic flow.
