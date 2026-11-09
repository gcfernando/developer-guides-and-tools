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
