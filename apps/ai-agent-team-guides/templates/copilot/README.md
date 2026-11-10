# GitHub Copilot agent team files

These files define lead, developer, qa-tester and devops roles.
Read the matching HTML guide before copying them to a project.

1. Copy hidden folders too. Merge existing files; do not replace customizations.
2. Edit .agent-team/project.md for your actual commands and folder ownership.
3. Open a terminal at the project root and run: copilot --agent lead
4. Give the lead a normal feature, fix, test or build request.
5. Inspect actual specialist tasks and results.

The bundled configuration explicitly selects GPT-6.1 Sol with medium reasoning for the lead and specialists.
Check account/client availability before starting. Choose an available model
when necessary, and keep the displayed guide and local files consistent.
Recovery limits live only in .agent-team/recovery.md; these are behavioral
instructions, not guaranteed client-enforced runtime retries.

For a new C# practice project, run the companion setup-practice script instead.

The CLI agent files use model, reasoningEffort and modelPolicy: preferred.
Auto sessions inherit their resolved session model; explicit per-agent models
are not guaranteed under Auto. Inspect actual specialist models in your client.
