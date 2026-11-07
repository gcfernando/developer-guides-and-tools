---
title: "Interactive Developer Tools and Offline References"
description: "Choose a searchable Linux command reference, an AI learning atlas or an AI coding add-ons reader, with browser links and offline-use guidance."
permalink: /interactive-tools/
---

[Developer guides and tools](../README.md)

<a id="interactive-tools"></a>

# Interactive Developer Tools and Offline References

Use these browser tools to find Linux commands, plan AI study or compare coding add-ons. Choose a tool below; its companion guide covers setup, offline use and maintenance.

<a id="guide-choose-a-tool"></a>

## Choose a tool

| Your goal | Browser tool | Companion guide |
| --- | --- | --- |
| Find Linux commands and examples | [Linux command reference](https://gcfernando.github.io/developer-guides-and-tools/apps/linux-command-reference/index.html) | [Search, offline use and maintenance](linux-command-reference/README.md) |
| Follow an AI study path and track progress | [AI Learning Atlas](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-learning-atlas/index.html) | [Learning paths and progress backups](ai-learning-atlas/README.md) |
| Understand AI coding add-ons | [AI coding add-ons reader](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-coding-addons/index.html) | [Source guide and setup notes](../docs/ai/coding-addons.md) |
| Build an AI agent review team | [Claude Code](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/claude-code-guide.html), [OpenAI Codex](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/openai-codex-guide.html), [GitHub Copilot](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/github-copilot-guide.html) | [Offline use and practice scripts](ai-agent-team-guides/README.md) |

<a id="guide-read-offline"></a>

## Read offline

Download the complete Linux reference folder for offline search. The Atlas and AI add-ons readers are standalone HTML files. External publisher and reference links require an internet connection.

<a id="guide-keep-generated-pages-in-sync"></a>

## Keep generated pages in sync

The add-ons browser page is generated from the Markdown guide, the Linux command table from its data source, and the Atlas reader from its authoring sources and exercises. Run `npm run build` from the repository root to rebuild all of them, or use `build:addons`, `build:linux` and `build:atlas` individually. Follow the [contribution guide](../CONTRIBUTING.md) before changing generated content.
