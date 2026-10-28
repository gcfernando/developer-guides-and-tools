---
title: "AI Client Configuration Examples and Setup Notes"
description: "Review opt-in Codex and Claude configuration snapshots and Copilot guidance. Keep client preferences separate from credentials and instruction templates."
permalink: /examples/ai-clients/
---

[Developer guides and tools](../../README.md)

<a id="ai-client-configuration-examples"></a>

# AI Client Configuration Examples and Setup Notes

Review the configuration examples for your client, then copy only the settings you intend to use. Instruction templates and account state are separate concerns.

> **In this guide:** [Get started](#guide-choose-a-client) · [Understand the details](#guide-review-compatibility-and-permissions) · [Add instructions deliberately](#guide-add-instructions-deliberately)

<a id="guide-choose-a-client"></a>

## Choose a client

| Client | Example or guide | Purpose |
| --- | --- | --- |
| Codex | [config.example.toml](codex/config.example.toml) | An imported, opt-in preference snapshot |
| Claude | [settings.example.json](claude/settings.example.json) | An imported, opt-in settings snapshot |
| Copilot | [Configuration and instruction guidance](copilot/README.md) | Supported preferences and a reusable instruction template |

<a id="guide-review-compatibility-and-permissions"></a>

## Review compatibility and permissions

These files are imported personal preference snapshots, not a compatibility guarantee for a current release. Inspect the model, permissions, sandbox and experimental options. Validate against the installed client's official schema before copying settings.

<a id="guide-add-instructions-deliberately"></a>

## Add instructions deliberately

Use the separate [AI instruction templates](../../templates/ai-instructions/README.md) when you want reusable guidance. Instruction text does not grant permissions or enforce a sandbox. Keep credentials and personal application state out of shared configuration.
