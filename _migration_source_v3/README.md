# Docusaurus Setup Guide

This guide provides step-by-step instructions to set up and deploy a Docusaurus-based documentation site.

## Prerequisites
Ensure you have the following installed:
```sh
# Install Node.js and npm from NodeSource
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt update && sudo apt install -y nodejs

# Install Git
sudo apt install -y git

# Install rsync for deployment
sudo apt install -y rsync
```
A web server (e.g., Apache, Nginx) is also required for hosting the documentation. You can install Apache using:
```sh
sudo apt update && sudo apt install -y apache2
```

## Setup Steps

### 1. Clone the Documentation Repository
```sh
mv docs/ test_docs  # Backup existing docs folder

git clone https://github.com/SafeSquid-Github/docs.git  # Clone the repository
ls -rlt  # Verify the contents
cd docs/  # Navigate to the docs directory
```

### 2. Prepare the Documentation Directory
```sh
mv docs docs_  # Rename existing docs folder
mkdir docs  # Create a new docs folder
```

### 3. Install Dependencies and Build the Site
```sh
npm install  # Install required dependencies
npm run build  # Build the static site
```

### 4. Serve the Documentation Locally
```sh
npm run serve  # Start the local server
```
By default, the local server listens on `http://localhost:3000`. You can access it by opening a browser and navigating to this address.

### 5. Deploy the Documentation (Requires a Web Server)
If you have installed a web server such as Apache, you can deploy the documentation by following these steps:
To deploy the documentation to a web server:
```sh
cd /var/www/html/  # Navigate to the web server root directory
rsync -av --delete /opt/docs/build/ /var/www/html/  # Sync the built documentation to the server
```

### 6. Verify Deployment
```sh
ip a  # Get the server's IP address
```
Open a web browser and navigate to `http://<server-ip>` to verify the documentation site is live.

## Additional Commands
- **Rebuild and deploy**
  ```sh
  npm run build && rsync -av --delete /opt/docs/build/ /var/www/html/
  ```
- **Check Git status**
  ```sh
  git status  # View repository changes
  ```
- **View system performance**
  ```sh
  top  # Monitor resource usage
  ```

## Troubleshooting
- If `npm run serve` fails, try reinstalling dependencies:
  ```sh
  rm -rf node_modules package-lock.json
  npm install
  npm run build
  npm run serve
  ```
- If the site doesn't update after deployment, check file permissions and ensure the web server has read access to `/var/www/html/`.


## Future Documentation Hierarchy
- **01-About SafeSquid SWG**
  - About_SafeSquid_Secure_Web_Gateway.md

- **02-Getting Started**
  - Getting_Started_with_SafeSquid_Secure_Web_Gateway.md

- **03-Installation**
  - main.md
  - **01-On Cloud**
    - Install SafeSquid SWG on AWS.md
    - Installation on Cloud.md
    - main.md
  - **02-On-Premise**
    - Install on VIrtual Box.md
    - Install SafeSquid using SAB.md
    - main.md
  - **03-Manual**
    - main.md
    - TAR Installation.md

- **04-License Activation**
  - License Activation.md

- **05-Architecture**
  - Application_Eco-System.md
  - main.md
  - Management_of_Self-Service_Portal.md
  - SafeSquid_SWG_directorys.md

- **06-User Identification**
  - Bypass Authentication.md
  - main.md
  - PAM Integeration.md
  - Setup Authentication.md
  - **01-Browser Authentication**
    - Browser Authentication.md
    - Kerberos SSO.md
    - main.md
  - **02-Directory Services**
    - Active Directory.md
    - main.md
    - OpenLDAP.md
  - **03-Network Identifiers**
    - IP-Based Authentication.md
    - main.md
    - Network Identifiers.md

- **07-SSL Inspection**
  - Bypass SSL Inspection.md
  - main.md
  - Setup SSL Inspection.md

- **08-SafeSquid Interface**
  - Accessing the SafeSquid Interface.md
  - Isolating the Portal.md
  - main.md
  - PAC file.md
  - Report.md
  - **01-Configuration**
    - main.md
    - **Application Setup**
      - Accelerators.md
      - Access_restrictions.md
      - Caching.md
      - FTP_browsing.md
      - Integration_of_LDAP.md
      - Network_settings.md
      - Prefetching.md
      - Proxy_chain.md
      - System_configuration.md
      - WCCP.md
    - **Custom Settings**
      - Categorize_WebSites.md
      - External_Applications.md
      - Request_Types.md
      - Response_Types.md
      - Templates.md
      - Time_Profiler.md
    - **Real Time Content Security**
      - 2.0_Real_time_content_security.md
      - Clam_antivirus.md
      - Content_modifier.md
      - DLP.md
      - DNS_blacklist.md
      - HTTPS_Inspection.md
      - ICAP.md
      - Image_analyzer.md
      - Redirect.md
      - SqScan.md
      - Text_analyzer.md
    - **Restriction Profiles**
      - Access_Profiles.md
      - Cookie_Filter.md
      - Elevated_Privacy.md
      - Header_Filter.md
      - Speed_Limits.md
  - **02-Support**
    - main.md
    - Startup Parameters.md
- **09-Profiling Engine**
  - Application Signatures.md
  - main.md
  - Request Profiles.md
  - Response Profiles.md
  - Time Profiles.md
  - True MIME Detection.md
  - Website Categorization.md

- **10-Web Access Control**
  - Basic Control.md
  - Content Filtering.md
  - Cookie Control.md
  - DNS Blacklisting.md
  - Geo Location Blocking.md
  - Header Re-Write.md
  - main.md
  - Payload Content Rewrite.md
  - Privileged Access Management.md
  - Protocol Filtering.md
  - Web Access Control.md
  - **01-URL Redirection**
    - main.md
    - SafeSearch.md
    - URL Redirection.md

- **11-Deep Content Security**
  - Data Leakage Prevention.md
  - Elevated Privacy.md
  - main.md
  - **01-Malware Detection**
    - Adaptable External Parser.md
    - ClamAV Malware Scanning.md
    - main.md
    - Malware Detection.md
    - Meta-Scan Integration.md
    - SqScan.md
  - **02-Content Moderation**
    - Image Analzer.md
    - main.md
    - Text Analyzer.md

- **12-Server Security**
  - main.md
  - SNI Aware.md
  - SSL Certificate Validation.md
  - SSL Offloading.md
  - Trusted Root CA Customization.md

- **13-System Audit**
  - main.md
  - Monitoring.md
  - Performance Plot.md
  - Real Time Statistics-Repoorting Module.md
  - Security Logs.md

- **14-Performance Optimisation**
  - Bandwidth Management.md
  - Client-side SSL Session Caching.md
  - Content Caching.md
  - main.md
  - Multi-Queue NIC Utilization.md
  - Pre-Fetching.md
  - Server-Side SSL Session Optimization.md
  - Smart In-Memory DNS Cache Manager.md
  - TCP Connection Reuse.md
  - WCCP Integeration.md
  - **01-Internalisae DNS**
    - Bind.md
    - Internalisae DNS.md
    - main.md

- **15-Scaling**
  - main.md
  - Scaling.md
  - SMP Aware.md
  - **01-Proxy Clustering**
    - main.md
    - Master-Slave.md
    - Proxy Clustering.md

- **16-Disaster Recovery**
  - Disaster Recovery.md
  - main.md

- **17-Operational Modes**
  - Forward Proxy.md
  - main.md
  - Proxy Chain.md
  - Reverse Proxy.md
  - TCP Proxy.md
  - Transparent Proxy.md

- **18-Custom Templates**
  - Custom Templates.md
  - main.md

- **19-Threat Intelligence Feeds**
  - main.md
  - TAXII Server.md

- **20-VPN Integration**
  - main.md
  - VPN Integration.md

- **21-Upgrade SafeSquid**
  - main.md
  - Upgrade SafeSquid.md

- **22-Troubleshooting**
  - Activation Failure.md
  - Basic SOP.md
  - Blank Report Page.md
  - Connection Failure on Websites.md
  - Custom Categorization Not Working.md
  - Disk Space and RAM are Full.md
  - DNS Failure.md
  - Failed To Fetch LDAP Entries.md
  - Gateway Timeout.md
  - Installation Issues.md
  - Interface Access Denied.md
  - main.md
  - Master Slave Configuration Not Working.md
  - No Tar-Ball Support.md
  - Not Generating Performance Plot.md
  - Product Failure.md
  - Proxy Server Refusing Connection Error.md
  - SafeSearch Not Working.md
  - SSL Inspection Issues.md
  - SSO Authentication Fail.md
  - Unable To Login Specific Website.md
  - Website Not Accessible.md
  - Whitelisted Website Blocked.md

- **23-Usecases**
  - Accessing_business_applications_through_SafeSquid.md
  - Access_Mobile_Applications_Through_SafeSquid.md
  - Access_Remote_Desktop_Applications_Through_SafeSquid.md
  - Allowing_Specific_Page_on_Facebook.md
  - Allow_anydesk.md
  - Allow_Outlook_To_Work_through_SafeSquid.md
  - Allow_remote_applications_to_particular_users.md
  - Allow_Social_Networking_Sites_during_Lunch_Hours.md
  - Allow_Specific_YouTube_Channel_and_its_Playlist.md
  - Block_Advertisements_And_Banners.md
  - Block_Emails_or_Files_including_archives_or_Social_Posts_using_Keywords.md
  - Block_inappropriate_images_by_using_Image_Analyzer.md
  - Block_Particular_User_Login_To_Facebook_Or_Gmail.md
  - Block_Personal_Gmail_Allow_Google_Corporate_Accounts.md
  - Block_Specific_Youtube_Channel.md
  - Facebook_Read_Only_Mode.md
  - main.md
  - Restrict_any_desk.md
  - YouTube_API_Integration_With_SafeSquid_To_Allow_Specific_YouTube_Videos.md

- **24-FAQs**
  - FAQ.md

## Conclusion
Following these steps, you should have a fully functioning Docusaurus documentation site running locally and deployed on your server. Happy documenting!

