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
