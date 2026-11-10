---
name: team-plan
description: Coordinate developer, QA and DevOps work for a feature, fix, test or build request.
argument-hint: "[task description]"
user-invocable: true
disable-model-invocation: false
model: opus
effort: medium
allowed-tools: Read, Grep, Glob
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

## Claude Code settings

The metadata selects Opus and medium effort for the skill's active turn.
It allows manual invocation and automatic selection, including preloading by
the lead definition. Read, Grep and Glob are pre-approved while active.
Other tool requests retain the client's approval controls and agent tool limits.
Run in the lead's current context; context: fork and agent are intentionally
omitted because this skill coordinates specialists from the main session.
Shell, editing, MCP, hooks and persistent memory are not enabled by this skill.
