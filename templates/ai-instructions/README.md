---
title: "Reusable AI Instruction Templates for Developers"
description: "Inspect and deliberately install reusable instruction templates for Codex, Claude, Copilot and ChatGPT. Keep instructions separate from permissions."
permalink: /templates/ai-instructions/
---

[Developer guides and tools](../../README.md)

<a id="reusable-ai-instruction-templates"></a>

# Reusable AI Instruction Templates for Developers

Choose reusable guidance for Codex, Claude, Copilot or ChatGPT, inspect it and install it deliberately for your client. These templates are example content; they do not govern this library as repository-wide instructions.

<a id="guide-choose-a-template"></a>

## Choose a template

| Client or purpose | Template |
| --- | --- |
| Codex | [AGENTS.md](codex/AGENTS.md) |
| Claude | [CLAUDE.md](claude/CLAUDE.md) |
| Copilot | [copilot-instructions.md](copilot/copilot-instructions.md) |
| ChatGPT custom instructions | [custom-instructions.txt](chatgpt/custom-instructions.txt) |
| Shared policy used by the Claude example | [ENGINEERING.md](shared/ENGINEERING.md) |

<a id="guide-install-with-the-correct-filenames"></a>

## Install with the correct filenames

Preserve each client's required filename and confirm instruction-loading behavior in the installed version. The Claude example references `~/.ai/ENGINEERING.md`: install the shared file there or update the import to the location you deliberately choose. Other templates retain their self-contained guidance.

<a id="guide-keep-settings-and-permissions-separate"></a>

## Keep settings and permissions separate

The [AI client configuration examples](../../examples/ai-clients/README.md) contain preference snapshots and separate setup notes. Instruction text guides behavior; it does not grant account access or enforce tool permissions, approval rules or a sandbox.
