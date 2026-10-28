---
layout: default
permalink: /utilities/windows-maintenance/
title: "Windows Maintenance with PowerShell — Script Guide"
description: Review a PowerShell Windows maintenance script's repair, update, networking and cleanup sequence, its prerequisites, side effects and limitations.
---

[Developer guides and tools](../../../README.md)

<a id="-windows-system-maintenance--powershell-script-reference"></a>

# Windows Maintenance with PowerShell — Script Guide

`SystemMaintenance.ps1` runs a fixed sequence of Windows repair, update, networking and cleanup operations. This guide explains the checked-in script's behavior so an administrator can decide whether it suits a particular machine.

> **In this guide:** [Get started](#guide-prerequisites) · [Walk through the example](#guide-usage) · [Check the limits](#guide-verification-and-logs)

<!-- Preserve links to earlier section headings. -->
<a id="windows-system-maintenance-powershell-script--sfc-dism-chkdsk-windows-update-and-cleanup"></a>
<a id="what-the-script-does"></a>
<a id="requirements"></a>
<a id="usage"></a>
<a id="logs"></a>
<a id="things-to-know-before-running"></a>
<a id="related-tools"></a>
<a id="documentation-links"></a>

<a id="guide-prerequisites"></a>

## 📦 Prerequisites

- Windows with the system commands and PowerShell modules used by the script.
- An elevated PowerShell session and authority to administer the machine.
- Internet access for updates and the first installation of `PSWindowsUpdate`.
- A script execution policy permitted by your organization.
- Saved work, an appropriate backup and a maintenance window with local access.

The script does not check every prerequisite, request elevation itself, provide a dry run or accept per-task switches. Running it starts the entire sequence.

## ⚙️ Operations and side effects

| Order | Operation | Actual behavior |
|---|---|---|
| 1 | CBS log cleanup | Stops `TrustedInstaller`, tries to delete `C:\Windows\Logs\CBS\CBS.log`, then restarts the service; a failure stopping the service skips this function |
| 2 | System File Checker | Runs `sfc /scannow` and maps its process exit code to a summary string |
| 3 | Image servicing | Runs DISM `/RestoreHealth` and `/StartComponentCleanup` |
| 4 | Disk repair | Runs `chkdsk C: /f /r /x /b`; Windows may prompt to schedule a check at restart |
| 5 | Device rescan | Runs `pnputil.exe /scan-devices`; it does not select or download driver packages |
| 6 | Windows Update | Installs `PSWindowsUpdate` for all users if absent; runs `Get-WindowsUpdate -AcceptAll -Install -AutoReboot:$false`; on failure restarts `wuauserv` and retries |
| 7 | Network reset | Runs Winsock/IP resets and DHCP release/renew/flush; restarts adapters and enables disconnected adapters whose names match `*Wi-Fi*` |
| 8 | Registry export | Runs `regedit /e` to `%TEMP%\registry_backup.reg`, waits ten seconds, then deletes that file if present; no retained backup results |
| 9 | Reporting | Calls `Get-WindowsErrorReporting` and queries physical disk reliability counters; this is not a complete health assessment |
| 10 | Cleanup | Recursively deletes temporary files, runs `cleanmgr.exe /verylowdisk`, then tries to delete crash dumps |
| 11 | Summary | Prints duration, its SFC interpretation, a fixed DISM completion label and a network-reset result |

Network operations can disconnect remote access. Keep local access available. Crash dumps and the CBS log may be needed for an existing investigation; preserve them before deciding to use the script.

<a id="guide-usage"></a>

## 💡 Usage

First read [`SystemMaintenance.ps1`](SystemMaintenance.ps1). If you have decided to run the complete sequence, open an elevated PowerShell in this folder:

```powershell
.\SystemMaintenance.ps1
```

If execution is blocked, check your organization's policy and the script's provenance before changing settings. SFC, DISM, updates and disk checks can take a long time. Decide when to restart based on actual update and CHKDSK output; the script does not reboot the machine itself.

<a id="guide-verification-and-logs"></a>

## 🧪 Verification and logs

| Intended path | Content |
|---|---|
| `%TEMP%\MaintenanceLog.txt` | Timestamped step messages |
| `%TEMP%\CleanupErrors.log` | Deduplicated error messages |

Read the native command output as well as the script's logs. Many steps have `try`/`catch`, but a nonzero native exit code does not consistently trigger those handlers. Several messages report completion without validating the native result; the final DISM label is fixed text. The animated SFC progress runs after the process exits, so it is not live scan progress.

The cleanup includes `%TEMP%`, where both logs and the registry export are stored. It can delete its own earlier logs; later writes may recreate only part of the history. Preserve needed diagnostics separately. A completed script or a printed summary does not establish a healthy system or successful execution of every step.

For a documentation review, inspect the source and parse PowerShell syntax without invoking the script. Runtime verification needs an authorized disposable Windows environment because the script makes system-wide changes.

## 🛠️ Troubleshooting and limitations

- **Missing module or update errors:** inspect the actual PowerShell error and module/provider prerequisites. The script can install a third-party module from the PowerShell Gallery.
- **Network loss:** use local access and inspect adapter/IP state. Enabling an adapter does not guarantee reconnection to a Wi-Fi network.
- **Disk check not completed:** inspect the CHKDSK prompt and restart requirements. The script does not automatically confirm scheduling.
- **Unexpected health output:** [`Get-WindowsErrorReporting`](https://learn.microsoft.com/en-us/powershell/module/windowserrorreporting/get-windowserrorreporting) is a reporting-setting query, not an enumeration of crash reports. Reliability-counter output also depends on storage hardware and available properties.
- **Missing logs:** the script's own temporary-file cleanup may have removed them.

Windows versions, device configuration, policy and module availability affect behavior. No cross-version runtime compatibility is established by this guide.

## 🔗 Related documentation

- [Repository overview](../../../README.md)
- [Documentation index](../../../documentation.md)
- [FixNetwork Python example](https://github.com/gcfernando/python-projects-and-examples/blob/main/FixNetwork/readme.md)
