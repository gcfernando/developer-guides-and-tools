---
title: "PowerShell Developer Utilities and Usage Guides"
description: "Choose documented PowerShell utilities for line-ending conversion and Windows maintenance. Read prerequisites, file effects and verification limits first."
permalink: /utilities/
---

[Developer guides and tools](../README.md)

<a id="developer-utilities"></a>

# PowerShell Developer Utilities and Usage Guides

Choose a documented PowerShell utility, understand its effects and run it deliberately. The guides describe prerequisites and verification limits alongside each script.

> **In this guide:** [Get started](#guide-choose-a-utility) · [Prepare and verify](#guide-prepare-and-verify) · [Explore related examples](#guide-explore-related-examples)

<a id="guide-choose-a-utility"></a>

## Choose a utility

| Task | Utility guide | Effect to review first |
| --- | --- | --- |
| Convert LF and CRLF endings | [Line-ending converter](powershell/convert-line-endings/README.md) | Modifies selected supported text files |
| Review a Windows repair and cleanup sequence | [Windows system maintenance](powershell/system-maintenance/README.md) | Immediately starts a fixed sequence of system operations |

<a id="guide-prepare-and-verify"></a>

## Prepare and verify

Read the companion guide before execution, use an appropriate disposable or backed-up environment and inspect the resulting output or diff. The maintenance script has no dry-run mode; its full sequence begins when it is launched.

<a id="guide-explore-related-examples"></a>

## Explore related examples

For local containers, WSL settings and client configuration, use the separate [configuration and environment examples](../examples/README.md).
