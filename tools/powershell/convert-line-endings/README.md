---
title: "PowerShell Line-Ending Converter"
description: "Convert supported UTF-8 text files between LF and CRLF, with exclusions and verification."
permalink: /utilities/line-endings/
---

# Line-ending converter

[Convert-LineEndings.ps1](Convert-LineEndings.ps1) accepts a file or folder and the EXISTING ending to convert FROM.

From the repository root:

~~~powershell
# LF to CRLF
.\tools\powershell\convert-line-endings\Convert-LineEndings.ps1 .\example.txt LF

# CRLF to LF
.\tools\powershell\convert-line-endings\Convert-LineEndings.ps1 .\example.txt CRLF

git ls-files --eol
~~~

Use a disposable file or a committed working tree first. Folder mode includes hidden files, prunes .git, bin, obj and node_modules, and skips reparse points. Explicit file arguments are processed directly.

Empty files, NUL-containing files and UTF-8 BOM files are skipped. Invalid UTF-8 is reported as a failure. Converted output is UTF-8 without BOM. The script reports counts but does not set a failing process exit code; inspect its output and review the diff.

The script's behavior is preserved from the source collection.
