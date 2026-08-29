---
title: Cloud Image or Cloud-Init
description: Choose between the prebuilt SafeSquid cloud image and a cloud-init build, and provision either one without embedding secrets in instance metadata.
keywords:
  - SafeSquid cloud image
  - safesquid-swg.img
  - cloud-init provisioning
  - custom image import
  - cloud instance build
---

# Choose the Provisioning Path

Two provisioning paths reach the same running instance. The prebuilt image is faster and carries a known baseline; cloud-init is repeatable and fits an existing automation pipeline. The wrong choice is not slow — it is unowned, producing instances nobody can rebuild identically.

Both paths share one rule: no secret goes into instance metadata.

## Compare the two paths

| | Prebuilt cloud image | cloud-init build |
|---|---|---|
| Speed to first boot | Fastest | Slower, builds on launch |
| Baseline | Fixed by the published image | Defined by your configuration |
| Fits existing automation | Requires an image import step | Yes, native user data |
| Rebuild reproducibility | Depends on the image being retained | Reproducible from the configuration file |
| Main risk | Image source and update path unapproved | A silent cloud-init failure leaves a reachable instance with no proxy |

Use the prebuilt image only when the image source, release, checksum or publisher identity, and update path are approved.

## Provision the instance

The two paths diverge from here — prebuilt image for the fastest known-good baseline, cloud-init for a reproducible, automation-driven build. Follow whichever one the comparison above pointed to.

<Tabs>
  <Tab title="Prebuilt cloud image">
    {/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Cloud-IMG (Recommended) */}

    The prebuilt image is published at:

    ```text
    http://downloads.safesquid.com/appliance/cloud-img/safesquid-swg.img
    ```

    Import it through the provider's custom-image path, then launch an instance from the imported image:

    | Provider | Import path |
    |---|---|
    | AWS | Import as an AMI using VM Import/Export |
    | Azure | Upload as a managed disk, then create an image from it |
    | GCP | Create a custom image from the disk |
    | DigitalOcean | Use the Custom Images feature |

    <Warning>
    The image ships with the account `administrator` and the password `safesquid`. Change it with `passwd` at first login, before the instance is reachable from any client network. A default credential on a reachable proxy is an immediate exposure, not a setup detail.
    </Warning>

    Record the image ID, region, launch date, SafeSquid version, disk mapping, and initial security group rules.
  </Tab>
  <Tab title="cloud-init build">
    {/* source: _migration_source_v3/docs/01-Getting_Started/03-Install_SafeSquid/02-Cloud_Deployment.md §Cloud-Init */}

    Retrieve the published cloud-init configuration:

    ```bash
    curl -O https://raw.githubusercontent.com/SafeSquid-Github/safesquid_cloud-init/main/safesquid_cloud-init.yaml
    ```

    Review and adjust the network settings, hostname, and disk layout before use, then pass it as user data at launch:

    | Provider | User-data field |
    |---|---|
    | AWS | User data, during EC2 launch |
    | Azure | Custom data, during VM creation |
    | GCP | Metadata, key `user-data` |
    | DigitalOcean | User data section |

    Keep cloud-init focused on baseline OS configuration, package source selection, network settings, log-forwarder bootstrap, and management hardening.

    <Warning>
    Do not embed activation keys, administrator passwords, or certificate private keys in cloud-init text. Instance metadata is readable from inside the instance and is frequently captured in provider logs and snapshots. Upload the `activation_key` through the approved activation workflow after the instance is reachable.
    </Warning>

    Follow provisioning from the instance:

    ```bash
    tail -f /var/log/cloud-init-output.log
    ```

    Expected result: the log reaches completion without error.

    A cloud-init failure often leaves a reachable instance running no proxy at all, so check this before assuming the launch succeeded. An instance that answers SSH is not an instance that is proxying.
  </Tab>
</Tabs>

## Verify after first boot

Whichever path was used, confirm before routing clients:

- Service and listener state — see [Service Health](/deployment/service_health).
- DNS resolution from the instance.
- Activation endpoint reachability — see [Ports and Firewall Rules](/deployment/ports_and_firewall_rules).
- Access-log creation under `/var/log/safesquid/access/`.
- The default administrator password has been changed.

## Capture provisioning evidence

Store these artifacts with the deployment record:

- Image ID and region, or the cloud-init file and its version.
- SafeSquid version at first boot.
- Disk mapping and initial security group rules.
- Confirmation that the default password was changed, and by whom.
- `cloud-init-output.log` completion, where cloud-init was used.

## Troubleshoot provisioning

| Symptom | Likely cause | Fix |
|---|---|---|
| Instance is reachable but nothing proxies | cloud-init failed partway | Read `/var/log/cloud-init-output.log` from the start, not the tail |
| Image import fails | Provider-specific format requirement | Check the provider's import constraints; AWS and Azure differ in disk format and size limits |
| Activation fails on a fresh instance | Egress to the activation endpoints is blocked by the security group | Allow outbound `443` to `key.safesquid.com` and `api.safesquid.net` |
| Instance is compromised soon after launch | Default credential left in place on a reachable host | Rebuild, then change the password before exposing the instance |
| Rebuilt instance behaves differently | Image was replaced upstream, or cloud-init file drifted | Pin the image ID or the configuration file version in the deployment record |

## Next steps

- [Cloud Deployment](/getting_started/install_safesquid/cloud_deployment) - secure the surrounding cloud network.
- [Activate Your License](/getting_started/activate) - apply the key once the instance is reachable.
- [Service Health](/deployment/service_health) - confirm the instance is actually serving.
