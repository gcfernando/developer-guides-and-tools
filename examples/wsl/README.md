---
title: "WSL2 Configuration Example"
description: "A sample WSL2 configuration for CPU, memory, swap and networking."
permalink: /examples/wsl/
---

# WSL2 configuration

Review [.wslconfig.example](.wslconfig.example), then merge the settings you want into %UserProfile%\.wslconfig.

The imported sample sets an 8 GB memory limit, eight logical processors and 4 GB swap. Choose values appropriate to your machine. Setting support depends on the Windows/WSL version.

After saving work in WSL, run wsl --shutdown to stop distributions and apply changes on their next start. This interrupts running WSL workloads.
