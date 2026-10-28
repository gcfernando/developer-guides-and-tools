---
title: "Copilot Configuration and Instruction Guidance"
description: "Separate reusable Copilot instructions from personal account state. Find the instruction template and guidance for configuring your own client."
permalink: /examples/ai-clients/copilot/
---

[Developer guides and tools](../../../README.md)

<a id="copilot-configuration-guidance"></a>

# Copilot Configuration and Instruction Guidance

Use your installed client's supported settings interface for preferences and a reusable instruction file for project guidance. Keep personal account state out of both.

> **In this guide:** [Start with the instruction template](#guide-start-with-the-instruction-template) · [Configure your own client](#guide-configure-your-own-client) · [Why the imported state is excluded](#guide-why-the-imported-state-is-excluded)

<a id="guide-start-with-the-instruction-template"></a>

## Start with the instruction template

The [Copilot instruction template](../../../templates/ai-instructions/copilot/copilot-instructions.md) is maintained separately from client preferences. Inspect its guidance and install it deliberately for your workflow.

<a id="guide-configure-your-own-client"></a>

## Configure your own client

Consult the official documentation for your installed client version. Do not copy another user's login, first-launch information or application-state file.

<a id="guide-why-the-imported-state-is-excluded"></a>

## Why the imported state is excluded

The original `copilot-config.json` was automatically managed state containing account identifiers and UI flags. It is not distributed as a reusable configuration example. The [source map](../../../maintenance/migration/source-map.csv) records its checksum and exclusion without reproducing account data.
