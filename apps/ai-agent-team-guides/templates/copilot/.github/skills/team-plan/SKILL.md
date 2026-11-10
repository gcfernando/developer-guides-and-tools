---
name: team-plan
description: Coordinate developer, QA and DevOps work for a feature, fix, test or build request.
argument-hint: "[task description]"
user-invocable: true
disable-model-invocation: false
allowed-tools: ["read", "search"]
---

# Plan and coordinate a team task

## When to use

Use as the lead for a request needing source, check or build specialists.
Select only the roles required. Record actual tasks; never invent activity.

## Project inputs

Read AGENTS.md, .agent-team/project.md, .agent-team/roles/lead.md and
.agent-team/recovery.md. The recovery file is the single source of retry,
fallback and fix/recheck limits. Read it again before recovery decisions.
Inspect the actual project and existing changes; use its configured commands.
Resolve missing acceptance criteria before assigning dependent work.

## Plan and assign

1. State the requested behavior and observable acceptance criteria.
2. Choose developer for source, qa-tester for checks, and devops for build/CI.
3. Agree interfaces and one writer per file before editing.
4. Parallelize independent investigations and edits in distinct files.
   Sequence dependent work. Run one build/check process against stable inputs.
5. Give each selected specialist the following assignment, filled with actual
   paths, commands and the limits read from .agent-team/recovery.md:

```text
Task ID: retained across retries and replacement agents
Goal: requested behavior
Acceptance criteria: conditions to verify
Allowed files: exact owned paths
Commands: relevant project commands
Dependencies: prerequisite tasks and agreed interfaces
Permissions: existing client approvals and sandbox
Completed evidence: verified work already obtained, or none
Attempts: counts used and remaining limits from .agent-team/recovery.md
Fix/recheck rounds: request-wide used count and remaining shared limit
Return: Status, Task ID, Changes, Evidence, Not verified, Attempts, Next step
```

## Recovery and rechecks

Preserve completed work and consult .agent-team/recovery.md before retrying.
Confirm that the old action ended and that repeating it is safe. Skip identical
retries for denied permissions, missing setup or unsupported tools.
If the old task's status is unknown, stop recovery and report the gap.
Carry all counts and evidence across continuations and replacement agents.
Assign a different permitted fallback explicitly, within the remaining budget.
A completed failing assertion is defect evidence: send it to developer, then
have QA recheck the finished fix within the request-wide round limit.
If no permitted fallback remains or it fails, report a partial result.
Never loosen approvals or deploy as a recovery action.

## Verify and finish

Collect actual specialist status, changed paths, commands, exit results and
remaining gaps. Distinguish static inspection from executed checks and local
workflow preparation from remote CI. Preserve unrelated work. Do not commit,
push, publish or deploy without the user's explicit request.
Return: Status, Changes, Evidence, Specialist status, Not verified, Attempts,
Next step. Attribute simulations and user-supplied results clearly.

## Copilot CLI settings

The metadata allows manual invocation and automatic selection and pre-approves
read/search operations. It does not pre-approve editing or terminal commands.
The lead and specialist agent definitions set their model and reasoning effort.
Copilot's documented skill fields do not include model or reasoningEffort.
Agent tool availability, client approvals and organization policy still apply.
