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
