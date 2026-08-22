---
title: Bandwidth Management
description: Control download speed, max download size, and upload size per user with SafeSquid Limits for bandwidth and data-handling policies.
keywords:
  - SafeSquid download speed limit
  - SafeSquid upload size restriction
  - Bandwidth control SafeSquid
  - Set file transfer limits SafeSquid
  - SafeSquid HTTPS download control
---


# Control download speed and size per user with Limits

Use SafeSquid Limits to set download speed and maximum download or upload size per user. Configure limits in the Limits (or speed limits) section and attach to profiles.

### Prerequisites
When downloading files from HTTPS websites, ensure that [HTTPS Inspection](/docs/SSL_Inspection/main/) in SafeSquid is enabled

### Setup Download Rate
![clicking on edit policies and editing the first entry in speed limits section ](/img/How_To/Setup_Download_Speed_At_Which_the_files_need_to_download/image1.webp)

![selecting true from the drop down menu](/img/How_To/Setup_Download_Speed_At_Which_the_files_need_to_download/image2.webp)

![setting the download rate as 10kb as an example in download rate field](/img/How_To/Setup_Download_Speed_At_Which_the_files_need_to_download/image3.webp)

### Testing Download Rate
![testing the download rate by downloading a file](/img/How_To/Setup_Download_Speed_At_Which_the_files_need_to_download/image4.webp)



## Setup Maximum limit on the Download size
This can be achieved using SafeSquid limits feature, the interface provides an option to set up the limit on the Download size for users.

### Prerequisites
When downloading files from HTTPS websites, ensure that [HTTPS Inspection](/docs/SSL_Inspection/main/) in SafeSquid is enabled

### Setup Maximum Download Size
![Edit second entry in policy under Configuration Section to Setup Maximum limit on the Download size](/img/How_To/Setup_Maximum_limit_on_the_Download_size/image1.webp)

![Enabled second entry as True in policy under Configuration Section to Setup Maximum limit on the Download size](/img/How_To/Setup_Maximum_limit_on_the_Download_size/image2.webp)

![Save policy under Configuration Section to Setup Maximum limit on the Download size](/img/How_To/Setup_Maximum_limit_on_the_Download_size/image3.webp)

### Testing Maximum Download Limit
![Testing of policy that set maximum limit on Download size](/img/How_To/Setup_Maximum_limit_on_the_Download_size/image4.webp)

# Setup Maximum limit on the Upload size
This can be achieved using SafeSquid limits feature, the interface provides an option to set up the limit on the Download size for users.

### Prerequisites
When downloading files from HTTPS websites, ensure that [HTTPS Inspection](/docs/SSL_Inspection/main/) in SafeSquid is enabled

### Setup Maximum Upload Size
![Setup Maximum limit on the Upload size in Speed Limits section](/img/How_To/Setup_Maximum_limit_on_the_Upload_size/image1.webp)

### Testing Upload Limit
Here I am selecting the file to Upload

![Select the file to Upload to check Maximum limit on the Upload size](/img/How_To/Setup_Maximum_limit_on_the_Upload_size/image2.webp)

![Select the file to Upload to check Maximum limit on the Upload size](/img/How_To/Setup_Maximum_limit_on_the_Upload_size/image3.webp)

When I click on upload, I will get the below error, Because I am uploading 4MB file, but I have maximum upload limit of 2MB

![Error template of Maximum limit on the Upload size](/img/How_To/Setup_Maximum_limit_on_the_Upload_size/image4.webp)

