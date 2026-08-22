---
title: Reporting Module
description: Use SafeSquid real-time dashboard reporting to filter data and drill down into transactions for network analysis.
keywords:
  - SafeSquid dashboard
  - SafeSquid reporting
  - realtime proxy reports
  - SafeSquid analytics
  - proxy traffic monitoring
---



## Reporting module provides real-time visibility

SafeSquid provides visibility into activity with detailed real-time reporting. The SafeSquid Dashboard shows real-time traffic (Internet usage), bandwidth utilization, and request counts. Dashboard data comes from SafeSquid databases; direct database access is available for querying and analytics. Reports default to the last **1000 transactions**; **date range** and **last transaction** are configurable.

The dashboard displays the following activities based on the last 1000 transactions:

1. IP Address
2. Upload Content
3. User Name
4. Download Content
5. User Group
6. Block Websites
7. Websites
8. Security Breaches
9. Domains
10. Connection Failed
11. IP Address
12. DNS Failed
13. User Name
14. Bypass Websites
15. User Group
16. Profiles
17. Application Signature
18. Categories

![Detailed real-time reporting SafeSquid Dashboard](/img/How_To/Reporting_Dashboard/image1.webp)



## Drilling method
Click any entry to apply that filter. In the example below the drill-down uses **User Name: "anounymous@192.168.0.14"**.

![Filtering section in SafeSquid Dashboard](/img/How_To/Reporting_Dashboard/image2.webp)

### Transactions
SafeSquid reports on the last 1000 transactions by default and supports custom report ranges. Edit the number of transactions as needed for drilling.

![Report based on last 1000 transactions by default.](/img/How_To/Reporting_Dashboard/image3.webp)

![Edit report based on number of transactions by default.](/img/How_To/Reporting_Dashboard/image4.webp)

![Apply filter to view safesquid report](/img/How_To/Reporting_Dashboard/image5.webp)

![Choose no of filtering option to view safesquid report](/img/How_To/Reporting_Dashboard/image6.webp)

![Close filter menu safesquid report](/img/How_To/Reporting_Dashboard/image7.webp)

### Date range
SafeSquid supports reports by date range. Filter the report by selecting start and end date (and time) as needed. Example: for 20 February 2018 between 1 PM and 2 PM, set Start date 20, time 1 PM, year 2018; set End date 20, time 2 PM, year 2018. The dashboard shows the filtered report. Click the close button to analyze the drilled report.

![Safesquid report based on date range.](/img/How_To/Reporting_Dashboard/image8.webp)

![Safesquid filtered report.](/img/How_To/Reporting_Dashboard/image9.webp)

![Flush button to reset filters of safesquid report](/img/How_To/Reporting_Dashboard/image10.webp)



## Verification and Evidence

- **Interface:** Reports > Dashboard shows the last 1000 transactions (or configured range); drill-down and date range filters apply. PDF/Excel export is available.
- **Audit evidence:** Use date range and filters to produce reports for a given period; export to PDF or Excel for compliance or audit. Logs and reports demonstrate control operation for SOC 2, PCI-DSS 10.x, or similar.

**Related**: [Security Logs](/docs/Audit_Forensics/Security_Logs/), [Performance Plot](/docs/Audit_Forensics/Performance_Plot/)

