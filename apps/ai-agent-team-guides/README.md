---
title: "AI Agent Team Guides"
description: "Create lead, developer, QA tester and DevOps teams in Claude Code, OpenAI Codex and GitHub Copilot."
permalink: /ai-agent-team-guides/
---

[Developer guides and tools](../../README.md) · [Interactive tools](../README.md)

# AI agent team guides

Start one lead, give it a normal request, and let it coordinate a developer,
QA tester and DevOps agent. Each guide shows complete files, model choices,
skills, parallel tasks and failure recovery.

| Product | Browser guide | Complete team files |
| --- | --- | --- |
| Claude Code | [Open guide](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/claude-code-guide.html) | [Download ZIP](downloads/claude-team.zip) |
| OpenAI Codex | [Open guide](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/openai-codex-guide.html) | [Download ZIP](downloads/codex-team.zip) |
| GitHub Copilot | [Open guide](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/github-copilot-guide.html) | [Download ZIP](downloads/copilot-team.zip) |

## Use a guide

1. Open your chosen HTML file locally or on the published site.
2. Follow the numbered steps to create or merge the shared Markdown files.
3. Register the four roles (Codex uses its main session as lead).
4. Create the four skills; check the explicit model and reasoning settings.
5. Start the lead and give it a normal request.
6. Inspect actual specialist tasks, check results and any gaps.

The matching files are also present under templates/claude, templates/codex
and templates/copilot, including hidden configuration folders. ZIP downloads
preserve those folders for copying. Merge existing configuration instead of
overwriting it.

## Optional C# starter

The six scripts under scripts/ create agent-team-practice in the current folder.
They add a small C# project, its two initial console checks and the matching
team files. They initialize a local Git repository but make no commits, contact
no remote and deploy nothing. They refuse to overwrite an existing folder.

Use Git 2.28+ and .NET 10 SDK for this starter. No extra packages or Node.js are
needed. The signed-in AI workflow needs the relevant client, account access and
an internet connection; account use may cost money.

## Reading and verification

Keep this folder together for offline reading, cross-guide links, scripts and
ZIP downloads. External documentation and AI sessions need internet access.
The HTML files are maintained directly.

[The change and test log](revision-test-log.md) separates local file/script/C#
checks from authenticated delegation, permission behavior and live recovery.
The latter remain documented but unverified in this environment.
