---
title: "WSL2 Configuration — Memory, CPU and Swap Settings"
description: "Review a WSL2 configuration example for memory, CPU, swap and networking. Choose machine-appropriate values and apply changes after saving your work."
permalink: /examples/wsl/
---

[Developer guides and tools](../../README.md)

<a id="wsl2-configuration"></a>

# WSL2 Configuration — Memory, CPU and Swap Settings

Use the [WSL2 configuration example](.wslconfig.example) as a starting point for memory, processor, swap and networking preferences on your own machine.

> **In this guide:** [Get started](#guide-apply-the-settings) · [Review the example values](#guide-review-the-example-values)

<a id="guide-review-the-example-values"></a>

## Review the example values

| Setting | Imported example | Before applying |
| --- | --- | --- |
| Memory limit | 8 GB | Leave enough memory for Windows and other workloads |
| Logical processors | 8 | Choose a value appropriate to your CPU |
| Swap | 4 GB | Consider available disk space and workload needs |
| Networking options | See the example file | Check support in your Windows and WSL versions |

<a id="guide-apply-the-settings"></a>

## Apply the settings

Merge the settings you want into `%UserProfile%\.wslconfig`. Save work in running WSL distributions before applying changes.

~~~powershell
wsl --shutdown
~~~

The settings take effect when distributions next start. Shutdown interrupts running WSL workloads; the sample is not a universal machine configuration.
