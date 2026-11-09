---
title: "AI Agent Team Guides Revision Test Log"
description: "Changes and local verification for the lead, developer, QA tester and DevOps guides."
---

# Four-agent team rewrite and test log

Rewritten 9 November 2026.

## What changed

All three HTML guides now teach the same requested team: lead, developer,
QA tester and DevOps.

- Complete shared Markdown instructions, project settings and recovery rules.
- Four role documents explaining ownership, reporting and coordination.
- Product-specific agent registration, tools and model configuration.
- Four skills: team-plan, implement-change, test-change and verify-delivery.
- Exact launch commands showing which agent starts first.
- Normal user prompts and the lead's selection of relevant specialists.
- Parallel investigation and separate-file editing, followed by serial verification.
- Concrete task assignments and specialist return formats.
- A blocked QA report, a lead-assigned alternate path and a partial final result.
- Separate limits for temporary retries, one fallback and two fix/recheck rounds.
- A complete C# delivery-fee example with checks and a prepared CI workflow.
- Actual template files, three ZIP downloads and six matching starter scripts.
- Mobile tables presented as labelled fields, and readable wrapped chat/output blocks.
- Existing public fragment IDs and cross-guide links preserved.

This replaces the earlier shopping-cart review-only lab. The report files at the
repository root are preserved as supplied. New team roles and the user's approved
structure take precedence over obsolete examples in those reports.

## Files provided

Each product has a templates folder containing the exact Markdown/configuration
shown in its HTML guide. ZIPs contain those same files, including hidden folders,
plus a short README.

Codex uses the main session as lead, three specialist TOML files and a parent
workspace-write/on-request configuration. Claude Code uses four Markdown agent
files, preloaded skills, a CLAUDE.md import and project settings. Copilot CLI uses
four .agent.md files with explicit skill-file reads, strict tool lists and
repository-instruction opt-in.

These are development teams allowed to change assigned files, not the previous
read-only review configuration. Markdown ownership/retry rules guide the agents;
they do not enforce an OS sandbox or deterministic workflow.

## Local checks

Environment: native Windows; Windows PowerShell 5.1; PowerShell 7.6.9;
Git Bash with Git 2.45.1; WSL2 Ubuntu 22.04; .NET SDK 10.0.403;
Python 3.12.10; Node 22.23.4 for repository/browser QA.

| Check | Observed result |
| --- | --- |
| Script matrix | All three products in PowerShell 5.1, PowerShell 7 and Git Bash: nine fresh C# projects. Exact generated files, expected main branch and no automatic commits. |
| Existing-folder guard | All nine scripts refuse a collision; file hashes confirm existing project files are preserved. |
| WSL2 | All three Bash scripts run. All 47 team configuration/Markdown files match the displayed templates. C# was not executed in WSL. |
| ZIPs | Three archives created; each configuration entry matches its template byte for byte, including hidden paths. |
| Starter C# | All three PowerShell 7 generated projects compile; both initial console checks pass. No extra NuGet packages are needed. |
| Walkthrough C# result | Displayed final source and check runner compile and pass five cases: zero, below boundary, at boundary, above boundary and negative-input exception. This tests an authored example, not AI implementation. |
| Configuration | TOML/JSON and YAML headers parse. Four roles and four skills are present. CI YAML parses, uses read-only contents permissions, a timeout and verified full action commit IDs. |
| HTML consistency | Every displayed role/configuration block matches the actual template; links resolve; all previous IDs remain; no duplicate IDs; browser JavaScript/JSON-LD parse. |
| Browser | Edge at offline file URLs and local HTTP: six runs across three guides. Desktop 1280px and mobile 390px, keyboard skip/theme/details, search, every code-copy control, and no page-wide mobile overflow. Clipboard writes mocked. |
| Accessibility | Automated axe WCAG A/AA checks pass in light/dark themes. Not a complete manual accessibility audit. |
| Repository | Aggregate tests, local links, repository standards and patch whitespace checked. |

The .NET checks are small console runners, not a test framework or dotnet test.
The starter deliberately covers only old fixed-fee behavior; the normal task asks
QA to add the new behavior checks.

The initial aggregate run passed its generated-content, example and unit checks
but caught three README reader-link conventions. Those links were corrected to
the published browser URLs and the link audit passed. The final aggregate npm test run passed after that correction.

Official setup, agent, skill and model documentation was checked during the rewrite.
Official action tags were resolved read-only: checkout v7.0.1 and setup-dotnet v6.
No GitHub Actions run, publish, push or deployment was performed.

## Not verified by an authenticated session

Installed client help was inspected for Codex 0.167.0, Copilot 1.0.108-1 and
Claude Code 2.1.319 on native Windows. Documentation can describe newer versions;
model aliases and available settings should be checked in the reader's client.

The following remain documented/unverified for each product:

- Authenticated loading of all roles and skills.
- Automatic selection from a normal prompt.
- Three real specialist executions and live parallel task activity.
- Continuation/messaging, cancellation and fresh-task handoff behavior.
- A real timeout/retry/alternate-path sequence.
- Effective permissions and per-role model access.
- Actual remote CI, deployment and real-project results.
- VS Code panel/harness parity, macOS clients and authenticated Linux sessions.

All illustrative task reports and recovery messages are labelled. Missing task
evidence must not be replaced with an invented transcript. Retry budgets in
Markdown are model instructions; built-in client retries may behave differently.

## Local-only QA

Scripts, fresh projects, screenshots and machine-readable results are stored in
.runtime/agent-team-rewrite-qa/. They are not part of the reader's starter project.
The prior revision log is saved there for historical context.
