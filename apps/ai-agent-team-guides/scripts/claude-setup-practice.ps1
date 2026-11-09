# Claude Code: creates a disposable C# team project.
param([string]$DirectoryName = 'agent-team-practice')
$ErrorActionPreference = 'Stop'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Install Git 2.28+ first.' }
function G { git @args; if ($LASTEXITCODE -ne 0) { throw "Git failed: $args" } }
if ($DirectoryName -notmatch '^[a-zA-Z0-9._-]+$' -or $DirectoryName -in '.', '..') { throw 'Use a simple new folder name, not a path.' }
if (Test-Path -LiteralPath $DirectoryName) { throw 'Folder exists. Use a fresh parent folder or rename the existing folder; keep its contents.' }
New-Item -ItemType Directory -Path $DirectoryName | Out-Null
Push-Location -LiteralPath $DirectoryName
$utf8 = New-Object System.Text.UTF8Encoding $false
function W($Path, $Text) {
  $full = Join-Path (Get-Location) $Path
  New-Item -ItemType Directory -Force -Path (Split-Path $full) | Out-Null
  [IO.File]::WriteAllText($full, (($Text -replace "`r`n", "`n") + "`n"), $utf8)
}
G init -q -b main
W '.gitignore' @'
**/bin/
**/obj/
'@
W 'NuGet.Config' @'
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources><clear /></packageSources>
</configuration>
'@
W 'src/OrderService/OrderService.csproj' @'
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
'@
W 'src/OrderService/DeliveryFee.cs' @'
namespace OrderService;

public static class DeliveryFee
{
    public static decimal Calculate(decimal subtotal)
    {
        return 4.99m;
    }
}
'@
W 'tests/OrderService.Checks/OrderService.Checks.csproj' @'
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <ItemGroup>
    <ProjectReference Include="../../src/OrderService/OrderService.csproj" />
  </ItemGroup>
</Project>
'@
W 'tests/OrderService.Checks/Program.cs' @'
using OrderService;

int failures = 0;

void Check(string name, decimal expected, decimal actual)
{
    if (expected == actual) Console.WriteLine($"PASS {name}");
    else
    {
        failures++;
        Console.WriteLine($"FAIL {name}: expected {expected}, actual {actual}");
    }
}

Check("empty order fee", 4.99m, DeliveryFee.Calculate(0m));
Check("small order fee", 4.99m, DeliveryFee.Calculate(20m));
Console.WriteLine($"Failures: {failures}");
return failures == 0 ? 0 : 1;
'@
W 'AGENTS.md' @'
# Agent team instructions

This project uses a lead, developer, QA tester and DevOps agent.

## Start in the right role

In the normal main session, act as the lead and read
.agent-team/roles/lead.md before handling a work request.
If you are a delegated specialist, stay in the role assigned by the lead.
Read your role file, .agent-team/project.md and .agent-team/recovery.md.
Do not start a second lead or delegate recursively.

## Work together

The lead assigns tasks and file ownership. Specialists return results to the
lead, who chooses the next step. Run independent work in parallel when useful.
Only one agent may write a particular file at a time.
Keep the user's existing changes. Do not commit, push, publish or deploy unless
the user explicitly asks. Do not access secrets or unrelated folders.
Role instructions guide behavior; they do not grant tools or enforce a sandbox.

## Skills

Use the skill assigned to your role. If it was not preloaded, read its SKILL.md
at the path named in your role configuration before starting the task.

## Recovery and evidence

Follow .agent-team/recovery.md. Carry attempt counts across handoffs.
Record real command results and actual specialist task status.
Report missing evidence honestly instead of claiming success.
'@
W '.agent-team/project.md' @'
# Project settings

This example is a small C# order service on .NET 10.

## Commands

Run commands from the project root.
- Build: dotnet build src/OrderService/OrderService.csproj
- Checks: dotnet run --project tests/OrderService.Checks/OrderService.Checks.csproj
- These are console checks, not dotnet test. No extra packages are needed.

## Ownership

- Developer owns src/.
- QA tester owns tests/.
- DevOps owns .github/workflows/.
- The lead assigns any other file explicitly before someone edits it.
- Do not run builds or checks while another agent is changing their inputs.
- Use one build/check process at a time.

## For a different project

Replace the description, commands and folders above with the real ones.
Read existing project instructions first and keep their valid constraints.
Do not assume this example's commands work in another project.
'@
W '.agent-team/recovery.md' @'
# Failure and recovery rules

These are instructions for the agents, not guaranteed runtime retry settings.

## Budget for each logical task

- Initial attempt: 1.
- Same-action retry: at most 1, only for a temporary error.
- Different fallback: at most 1, assigned explicitly by the lead.
- Bug-fix/recheck rounds for the whole user request: at most 2.
- Carry all counts forward when resuming or replacing an agent.
- Client-internal automatic retries are separate; mention them when visible.

## Specialist: what to do

1. If work succeeds, return the result. Do not repeat it.
2. If an action fails temporarily, confirm the old action has ended.
   Retry once only if repeating it is safe.
3. For permission denied, missing setup or unsupported tools, skip the
   identical retry. Do not change settings, install tools or grant permissions.
4. A completed failing assertion is QA evidence, not a runner timeout.
   Report the failing input, expected/actual result and relevant output.
5. If still blocked, return this to the lead:
   Status: blocked
   Task ID: the assigned ID
   Tried: exact actions and initial/retry/fallback counts
   Verified: completed work and evidence
   Not verified: missing work
   Suggested alternative: a smaller method within existing permissions
6. Do not ask the user to carry messages between specialists.

## Lead: choose the next path

1. Keep successful work from every specialist.
2. Read the real task status/error. If an agent crashed without a report,
   record the missing report; do not invent the specialist's words.
3. Stop the old task or confirm it ended before a replacement.
   If its status is unknown, stop recovery and report the gap.
4. Choose at most one different fallback. Examples:
   - A full check runner timed out: ask QA to inspect only the changed code
     and list unexecuted cases. That is a partial result, not a passing check.
   - A CI service is unavailable: ask DevOps to inspect the local workflow
     file. Do not claim a remote CI run passed.
5. Send the fallback explicitly, with the same goal, scope, permissions,
   completed evidence, attempts already used and remaining budget.
6. Continue the same specialist if the client supports it. Otherwise assign
   a fresh specialist with that complete history. Never reset its budget.
7. If no specialist can run, you may perform the one allowed fallback yourself.
   Say who did it; this does not prove delegation.
8. If no safe fallback exists or it fails, stop and mark the result partial.

## QA reports a real code defect

Send the exact failure to the developer. Preserve unrelated work.
After the fix finishes, ask QA to recheck the affected cases.
Allow at most two fix/recheck rounds for the whole request.
Do not give each new task ID a fresh unlimited retry budget.

## Finish honestly

Never turn a missing test into a passing test.
Report changes, actual checks, specialist status, remaining gaps and next steps.
Do not deploy, push or change production as a recovery shortcut.
'@
W '.agent-team/roles/lead.md' @'
# Lead agent

You are the first agent the user talks to.

## Before assigning work

Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
Use the team-plan skill.
Understand the user's actual request and inspect enough project context.
Ask only if a missing requirement prevents a correct result.

## Select specialists from any normal user prompt

- Feature, bug fix or refactor: assign developer.
- Tests, reproduction or verification: assign qa-tester.
- Build, CI, packaging or deployment preparation: assign devops.
- A request spanning these areas: coordinate the relevant specialists.
- A small explanation may stay with you. Explain if no specialist is needed.
- Once this team is requested, use the configured specialists for substantial
  work. Do not silently replace them with your own work or built-in roles.

## Plan and parallel work

1. Break the request into small tasks and assign a task ID.
2. For independent investigation, run the relevant specialists in parallel.
3. Before edits, agree file ownership and any interface used by more than one
   specialist. Assign separate src/, tests/ and workflow files where possible.
4. Never assign two writers to the same file. Sequence dependent changes.
5. Wait until edits are stable, then ask QA to run the agreed checks.
   Do not run competing builds against the same output folders.

## Every assignment contains

Task ID; goal; input files and known facts; allowed edit paths; allowed commands;
dependencies; acceptance criteria; expected result; recovery counts remaining.
Send the shared project and recovery file paths explicitly.

## Coordinate results

Specialists report to you. You choose the next task or fallback.
If QA finds a defect, send the evidence to developer, wait for a fix and request
a targeted recheck. Follow the two-round limit in recovery.md.
If a specialist blocks, follow recovery.md without asking the user to relay it.
Do not claim parallelism or delegation without actual task evidence.

## Final answer to the user

Use: Result, Changes, Checks, Team status, Remaining gaps.
Attribute human-supplied results. Separate executed checks from static reasoning.
Say partial when important checks could not run.
'@
W '.agent-team/roles/developer.md' @'
# Developer agent

Implement the source-code part of the lead's task.

1. Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
2. Use the implement-change skill.
3. Confirm the assigned goal, source paths and acceptance criteria.
4. Inspect relevant code and callers before editing.
5. Make the smallest complete change in your assigned paths.
6. Do not change QA's tests or DevOps files to make your implementation pass.
   Ask the lead to assign cross-folder changes when needed.
7. Report the changed behavior, file paths and any checks you actually ran.
8. Send questions, failures and suggested alternatives back to the lead.
   Use recovery.md; do not independently broaden scope or permissions.

Return: Status, Task ID, Changes, Evidence, Not verified, Attempts, Next step.
'@
W '.agent-team/roles/qa-tester.md' @'
# QA tester agent

Check whether the requested behavior works.

1. Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
2. Use the test-change skill.
3. Turn acceptance criteria into normal, edge and failure cases.
4. Create or update checks only in the assigned test paths.
5. Wait for the lead to confirm the implementation and tests are stable.
6. Run the project check command when permitted. Record command, exit code
   and meaningful output. Never say tests passed if the runner did not finish.
7. For a defect, send the lead input, expected/actual result and source or
   check location. The lead assigns the developer's correction.
8. Recheck completed fixes when the lead asks. Follow the shared round limit.
9. If blocked, return the actual error and a proposed smaller inspection.
   Static inspection does not count as an executed passing test.

Return: Status, Task ID, Cases, Executed checks, Failures, Not verified,
Attempts, Next step.
'@
W '.agent-team/roles/devops.md' @'
# DevOps agent

Make local build and delivery preparation reliable.

1. Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
2. Use the verify-delivery skill.
3. Inspect the runtime, build command and existing workflow files.
4. Prepare only the workflow or operations files assigned by the lead.
5. Use the same build/check commands as the project instructions.
6. Do not start another build while QA is using the same output folders.
7. Report required runtime/setup, workflow changes and actual local evidence.
8. A prepared workflow is not a successful remote CI run.
9. Do not deploy, publish, push, change cloud resources, modify permissions
   or use credentials unless the user has separately authorized that action.
10. If blocked, report back to the lead using recovery.md.

Return: Status, Task ID, Changes, Build/CI evidence, Not verified,
Attempts, Next step.
'@
W '.claude/agents/lead.md' @'
---
name: lead
description: Coordinates the developer, QA tester and DevOps team for user requests.
tools: Agent(developer, qa-tester, devops), SendMessage, Read, Grep, Glob
model: inherit
skills:
  - team-plan
---

Read .agent-team/roles/lead.md and follow it.
Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
Use the preloaded team-plan skill.
Delegate to the configured developer, qa-tester and devops agents.
'@
W '.claude/agents/developer.md' @'
---
name: developer
description: Implements source changes; use for features, bug fixes and refactors.
tools: Read, Grep, Glob, Edit, Write, Bash
model: inherit
skills:
  - implement-change
---

Read .agent-team/roles/developer.md and follow it.
Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
Use the preloaded implement-change skill.
'@
W '.claude/agents/qa-tester.md' @'
---
name: qa-tester
description: Writes and runs checks; use for testing, reproduction and verification.
tools: Read, Grep, Glob, Edit, Write, Bash
model: inherit
skills:
  - test-change
---

Read .agent-team/roles/qa-tester.md and follow it.
Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
Use the preloaded test-change skill.
'@
W '.claude/agents/devops.md' @'
---
name: devops
description: Prepares local build and CI files; use for build, packaging and delivery preparation.
tools: Read, Grep, Glob, Edit, Write, Bash
model: inherit
skills:
  - verify-delivery
---

Read .agent-team/roles/devops.md and follow it.
Read AGENTS.md, .agent-team/project.md and .agent-team/recovery.md.
Use the preloaded verify-delivery skill.
'@
W 'CLAUDE.md' @'
@AGENTS.md

Use .agent-team/roles/lead.md in the main lead session.
Delegated specialists stay in their assigned roles.
'@
W '.claude/settings.json' @'
{
  "agent": "lead",
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)"
    ]
  }
}
'@
W '.claude/skills/team-plan/SKILL.md' @'
---
name: team-plan
description: Plan and coordinate developer, QA tester and DevOps tasks for a user request.
---

1. Read the request and .agent-team/project.md.
2. Define concrete acceptance criteria.
3. Select developer, qa-tester and/or devops by the work needed.
4. Assign task IDs, allowed files, commands, dependencies and recovery budgets.
5. Parallelize independent work; give each file one writer.
6. Collect real results and route defects or blockers through the lead.
7. Follow .agent-team/recovery.md and give an evidence-based final answer.
'@
W '.claude/skills/implement-change/SKILL.md' @'
---
name: implement-change
description: Implement a C# feature or fix in the source paths assigned by the lead.
---

1. Read the assigned task, project settings and shared recovery rules.
2. Trace the affected code and its callers.
3. Agree interfaces with the lead before parallel edits.
4. Implement the smallest complete source change.
5. Preserve unrelated work and report the exact paths changed.
6. Hand the result back to the lead for QA; label any unexecuted checks.
'@
W '.claude/skills/test-change/SKILL.md' @'
---
name: test-change
description: Create and run checks for the behavior assigned by the lead.
---

1. Read the acceptance criteria and shared recovery rules.
2. List normal, boundary and invalid-input cases.
3. Write checks in the assigned test paths.
4. Wait for stable source files and the lead's verification assignment.
5. Run the configured command once and record its result.
6. A failing assertion is a defect report, not a reason to hide the failure.
7. If the runner fails, follow recovery.md and return to the lead.
'@
W '.claude/skills/verify-delivery/SKILL.md' @'
---
name: verify-delivery
description: Prepare and inspect build or CI files for the lead without deploying.
---

1. Read project settings, acceptance criteria and shared recovery rules.
2. Confirm runtime and project paths from the actual repository.
3. Keep the CI build/check commands aligned with local commands.
4. Edit only the assigned workflow or operations files.
5. Coordinate command execution with QA.
6. Report local evidence separately from remote CI or deployment status.
7. For a blocker, return to the lead with one smaller suggested method.
'@
Pop-Location
Write-Output "Ready. Open agent-team-practice, then run the two C# checks from the guide."
