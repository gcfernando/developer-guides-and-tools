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

## Task and verification settings

The lead supplies a task ID, goal, acceptance criteria, allowed files,
dependencies and verification command with every assignment.
Keep existing user changes and agree shared interfaces before parallel edits.
Report actual command results; an unexecuted check remains unverified.

## Shared behavior and client settings

Read AGENTS.md for team boundaries and .agent-team/recovery.md for all retry,
fallback and request-wide fix/recheck limits. Do not duplicate those values here.
Read the current recovery file before assigning budgets or handling failures.
Model, reasoning, tools and approvals use the product configuration in this ZIP.
The guide's configuration section shows every selected value and exact path.
Do not commit, push, publish or deploy without the user's explicit request.
