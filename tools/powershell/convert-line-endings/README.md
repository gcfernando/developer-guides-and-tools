---
title: "Convert LF and CRLF Line Endings with PowerShell"
description: "Convert supported UTF-8 text files between LF and CRLF with a PowerShell utility, documented exclusions, usage examples and diff-based verification."
permalink: /utilities/line-endings/
---

[Developer guides and tools](../../../README.md)

<a id="line-ending-converter"></a>

# Convert LF and CRLF Line Endings with PowerShell

Normalize supported UTF-8 text files between LF and CRLF using [Convert-LineEndings.ps1](Convert-LineEndings.ps1). Pass a file or folder and the **existing** ending to convert **from**; begin with a disposable file and inspect the result.

<a id="guide-run-the-converter"></a>

## Run the converter

From the repository root:

~~~powershell
# LF to CRLF
.\tools\powershell\convert-line-endings\Convert-LineEndings.ps1 .\example.txt LF

# CRLF to LF
.\tools\powershell\convert-line-endings\Convert-LineEndings.ps1 .\example.txt CRLF

git ls-files --eol
~~~


<a id="guide-understand-the-scope"></a>

## Understand the scope

Use a disposable file or a committed working tree first. Folder mode includes hidden files, prunes `.git`, `bin`, `obj` and `node_modules`, and skips reparse points. Explicit file arguments are processed directly.

Empty files, NUL-containing files and UTF-8 BOM files are skipped. Invalid UTF-8 is reported as a failure. Converted output is UTF-8 without BOM.

<a id="guide-verify-the-result"></a>

## Verify the result

The script reports counts but does not set a failing process exit code. Inspect its output and review `git diff` rather than relying only on the command's exit status.

The utility implementation is preserved from the imported source. [Contribution guidance](../../../CONTRIBUTING.md) describes the repository's maintenance process.
