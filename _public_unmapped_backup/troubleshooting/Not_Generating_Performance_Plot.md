---
title: Unable to Generate Performance Plot
description: Troubleshoot SafeSquid performance plot failures by checking plotting dependencies, script availability, output generation, and manual fallback workflow.
keywords:
  - SafeSquid performance plot issue
  - SafeSquid gnuplot missing
  - performance.png not generated
  - troubleshoot SafeSquid plot.sh
  - SafeSquid support performance metrics
---

# Restore performance plot generation

## Problem statement

If the performance plot cannot be generated during an incident, operators lose a quick way to visualize load and timing behavior. That slows troubleshooting and makes escalation harder because the evidence window may pass before the graph is recovered.

## Client scenario

Use this runbook when:

- the Support interface fails to generate a performance plot
- the plot file is missing
- the plotting workflow worked earlier but now fails
- you need to generate the plot manually while the UI path is broken

## Key benefits

This runbook helps you isolate whether the failure comes from missing dependencies, script-path issues, or output-generation problems. It also gives you a manual fallback path so evidence collection can continue while you repair the UI-driven workflow.

## Prerequisites

### Client-side preparations

- Ensure you have shell access with administrative privileges on the SafeSquid host.
- Note the time range you need before starting manual generation.

### SafeSquid-side setup

- Confirm the host has internet access if you may need to install missing packages.
- Confirm the plotting script path exists on the appliance.

## Troubleshooting guide

### Symptom: The UI does not produce a plot

Likely causes:

- `gnuplot` is not installed
- the plotting script is missing or not executable
- the plot output file is not being created

### Step 1: Confirm `gnuplot` is installed

Run:

```bash
aptitude search gnuplot
```

Expected result:

- the package appears as installed

If it is missing, install it:

```bash
aptitude install gnuplot
```

### Step 2: Confirm the plotting script exists

Go to the UI CGI path:

```bash
cd /usr/local/safesquid/ui_root/cgi-bin/
ls -l
```

Expected result:

- `plot.sh` exists
- the file has execute permissions

If `plot.sh` is missing or not executable, the UI will not be able to generate the plot correctly.

### Step 3: Generate the plot manually

Run the script with a start and end timestamp:

```bash
./plot.sh YYYYMMDDHHMMSS YYYYMMDDHHMMSS
```

Example:

```bash
./plot.sh 20180305000000 20180305235959
```

This lets you test whether the underlying plotting path works even when the UI path fails.

### Step 4: Confirm the output file exists

Check the performance output path:

```bash
cd /var/log/safesquid/performance/
ls -l
```

Expected result:

- `performance.log` exists
- `performance.png` is generated after the script runs

## Verification and validation

### Positive test

After installing dependencies or fixing the script path:

- generate a plot manually
- confirm `performance.png` appears
- retry the same time range from the UI

Expected result:

- both manual and UI generation succeed

### Negative test

Run the script for a valid but low-activity time window.

Expected result:

- the file still generates
- low activity produces a quiet graph rather than no graph at all

## Escalation boundary

Escalate after you have collected:

- package status for `gnuplot`
- confirmation of `plot.sh` presence and permissions
- the exact command used for manual generation
- whether `performance.png` was created

That evidence prevents a generic escalation and gives the next responder a concrete failure point.

## Related controls / next steps

- Use [Performance Plot](/Performance_Plot) for the normal operator workflow.
- Use [Security Logs](/Security_Logs) and [Reporting Module](/Reporting_Module) to correlate the plotted window with real request activity.
