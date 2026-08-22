---
title: Custom Templates
description: Create custom templates in SafeSquid for error pages, branding, and blocked-content replacement using HTML, images, or executables.

keywords:
  - SafeSquid custom templates
  - SafeSquid template configuration
  - SafeSquid error page customization
  - Create HTML template SafeSquid
  - SafeSquid UI template management
---


# Replace blocked or error pages with custom content

SafeSquid uses templates to replace pages that cannot be displayed (filtering, error, or other conditions). Custom templates support non-English messages, company logos, and contact text (e.g. "If this site was blocked in error, contact helpdesk@mycompany.com"). Templates can be HTML, images, audio, or executables. Built-in examples include tinygif, checkeredgif, and tinyswf; checkeredgif is the default replacement for images blocked by the pornographic image filter.



## Prerequisites
Create your own html file and place that file in the below paths

for windows version of SafeSquid:

**c:ProgramDatausrlocalsafesquidui_roottemplates**

The path for Linux version of SafeSquid is:

**/usr/local/safesquid/ui_root/templates/**

**Note**: If you want to use any images in the html file make sure that the image also exist in the same path.



## Example:
Here i am creating below html page:

![Create Custom Templates or template list in SafeSquid interface](/img/How_To/Create_Custom_Templates/image1.webp)

I Am saving this file with name:

**Custom_template.html**

I will use this file in the below configuration



## [Access the SafeSquid user interface](/docs/SafeSquid_SWG/Configuration_Portal/)
### Go to Configure Page
![Clicking on configure in SafeSquid interface](/img/How_To/Create_Custom_Templates/image2.webp)

### Go to Custom Settings
![Clicking to custom settings](/img/How_To/Create_Custom_Templates/image3.webp)

### Go to Templates
![Clicking on templates ](/img/How_To/Create_Custom_Templates/image4.webp)

### Clone existing entry
![Cloning the existing entry by clicking on clone](/img/How_To/Create_Custom_Templates/image5.webp)

### Edit the original entry
![Clicking on edit to edit the policies](/img/How_To/Create_Custom_Templates/image6.webp)

You must edit the original entry, because the entries in template section are processed from top to bottom

![Editing the comment as per your entry](/img/How_To/Create_Custom_Templates/image7.webp)

![In profiles, selecting the required profile in the drop down menu](/img/How_To/Create_Custom_Templates/image8.webp)

![Do not change the "name" field](/img/How_To/Create_Custom_Templates/image9.webp)

![Giving the name of your html file in file field](/img/How_To/Create_Custom_Templates/image10.webp)

![clicking on save policy to save it](/img/How_To/Create_Custom_Templates/image11.webp)

![Saved rule](/img/How_To/Create_Custom_Templates/image12.webp)



## Testing
![Testing the template](/img/How_To/Create_Custom_Templates/image13.webp)



## Saving the Configuration
![clicking on save config to save the policy](/img/How_To/Create_Custom_Templates/image14.webp)



## Verification and Evidence

- **Interface Checks**: In [Configuration Portal](/docs/SafeSquid_SWG/Configuration_Portal/), Custom Settings → Custom Templates: new template appears in the list with correct content and is assigned to the intended policy or block page.
- **Log Analysis**: When a block or redirect occurs, the custom template is served; config logs show the template change if applicable.
- **Performance Validation**: Trigger a block or use case that invokes the template; the custom message or page displays as designed.

**Related**: [Startup Parameters](/docs/Customisation/Startup_Parameters/), [Customisation](/docs/Customisation/main/), [Access Restriction](/docs/Access_Restriction/main/), [Troubleshooting](/docs/Troubleshooting/main/)

