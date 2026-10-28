---
title: "Reusable AI Instruction Templates"
description: "Opt-in instruction templates for Codex, Claude, Copilot and ChatGPT."
permalink: /templates/ai-instructions/
---

# Reusable AI instruction templates

These documents are examples to inspect and deliberately install, rather than repository-wide instructions for this library.

| Client | Template |
|---|---|
| Codex | [AGENTS.md](codex/AGENTS.md) |
| Claude | [CLAUDE.md](claude/CLAUDE.md) |
| Copilot | [copilot-instructions.md](copilot/copilot-instructions.md) |
| ChatGPT custom instructions | [custom-instructions.txt](chatgpt/custom-instructions.txt) |
| Shared policy used by the Claude example | [ENGINEERING.md](shared/ENGINEERING.md) |

The Claude template references ~/.ai/ENGINEERING.md. If you choose to use that template, install the shared file at that path or update the import to the location you deliberately select. Other clients retain their self-contained source templates.

Preserve required filenames and confirm instruction-loading behavior in the installed client. The [configuration examples](../../examples/ai-clients/README.md) are a separate concern. Instructions describe behavior; permissions and sandboxing are controlled by the actual environment.

Shared sections are similar across templates but have client-specific application notes. Review those notes before propagating a policy edit between them.
