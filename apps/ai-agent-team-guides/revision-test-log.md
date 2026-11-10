# Four-agent team rewrite and test log

## Official configuration corrections — 10 November 2026

The complete examples now include selected configuration values directly in
their final files. The earlier review's inheritance defaults and repeated
recovery summaries have been replaced as follows:

- Codex: GPT-6.1 Sol/medium in the complete project config and all three agent
  TOMLs; workspace-write/on-request; enabled delegation; three concurrently open
  specialist threads excluding the lead; explicit specialist defaults and
  interrupt-message behavior. Global controls stay in .codex/config.toml.
- Claude: Opus/medium for the lead and planning skill, Sonnet/medium for the
  specialists, explicit default permissions, and a documented 30-turn cap in
  the representative developer definition. The lead includes TaskStop for
  recovery. Project settings select the lead and its model.
- Copilot: explicit GPT-6.1 Sol/medium in every agent, with preferred model
  policy, automatic delegation eligibility, instruction opt-in and tool lists.
  The guide explains model overrides, fallback and the Auto-session exception.
- Product-specific skill examples: Claude model/effort and invocation/read-tool
  controls; Copilot invocation/read-tool controls; Codex workflow metadata plus
  the complete agents/openai.yaml display/invocation companion.
- Recovery limits remain numeric only in recovery.md among the authoritative
  instruction files. Expanded project, developer and planning instructions read
  those current limits instead of repeating them. Walkthroughs illustrate the
  bundled defaults and are labelled accordingly.
- Added missing files to the Codex/Claude folder trees, removed Copilot-specific
  installation text from other guides, corrected the Codex approvals/security
  source link, and replaced isolated model snippets with links to complete files.
- Updated all three ZIPs, template READMEs, six starter scripts and displayed
  template blocks. The original CSS and JavaScript remain byte-for-byte equal
  to the repository versions.

Official references used for these corrections:

- [Codex agents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
  [config basics](https://learn.chatgpt.com/docs/config-file/config-basic),
  [config reference](https://learn.chatgpt.com/docs/config-file/config-reference),
  [skills](https://learn.chatgpt.com/docs/build-skills), and
  [approvals/security](https://learn.chatgpt.com/docs/agent-approvals-security).
- [Claude agents](https://code.claude.com/docs/en/sub-agents),
  [skills](https://code.claude.com/docs/en/skills),
  [settings](https://code.claude.com/docs/en/settings), and
  [model configuration](https://code.claude.com/docs/en/model-config).
- [Copilot CLI field reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference),
  [custom agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli), and
  [skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

Verification completed:

- Six regression tests in tests/test_agent_team_guides.py passed. They check
  explicit model/reasoning/global settings, product-specific skill metadata,
  recovery-source consistency, folder trees, and displayed/downloaded/embedded
  file equality. These checks run with Python's standard library.
- All six PowerShell/Bash starters executed in new isolated folders, generated
  the corrected templates (including the Codex skill companion), and refused
  reruns against existing folders while preserving a sentinel user file.
- TOML and YAML syntax, archive integrity, local links and fragment IDs passed.
- All 12 Edge combinations passed: three guides, 1440px/390px, HTTP/file URLs.
  Checked actual HTTP ZIP downloads, full skill/developer copying, Codex project
  configuration copying including the model and [agents] controls, themes,
  absence of page overflow and JavaScript errors. Clipboard checks use a stub.
- Inspected desktop/mobile screenshots; original style and script blocks match.
- Repository standards and git diff whitespace checks passed.

Validation covers documentation, local files and browser behavior. It does not
claim an authenticated agent-team run, effective account model access, live
recovery, remote CI, deployment or published-site verification.

## Guide review updates — 10 November 2026

- Removed the rewritten-date badge shown in the supplied screenshot from all
  three HTML headers. The screenshot file itself is preserved.
- Added a matching ZIP download button to each header and extraction guidance
  in the existing downloads section.
- Expanded one representative file in each file-authoring section: project.md
  for shared settings, developer.md for role instructions, the product-specific
  developer definition for registration, and team-plan/SKILL.md for skills.
  Each is labelled as a complete example and retains the existing copy control.
- The developer definition now includes its role body directly. Shared project
  settings, recovery rules and the implementation skill remain separate inputs.
  Other roles and skills retain their existing examples.
- Updated the matching templates, all three ZIPs and the embedded contents in
  all six starter scripts. Kept the existing CSS and page interactions.

Validation performed for this update:

| Check | Observed result |
| --- | --- |
| All three guides' IDs, fragment targets and relative file links | Passed; no duplicate IDs or broken local targets |
| Displayed template blocks against their actual files | Passed for every matching template block |
| ZIP integrity, file lists and bytes against template folders | Passed for all three archives, including hidden folders |
| Codex TOML and Markdown YAML metadata | Parsed successfully |
| All six PowerShell/Bash starters | Executed in isolated temporary folders; generated team files matched templates |
| Starter reruns against existing folders | All six refused to overwrite; sentinel user files were preserved |
| Headless Edge at 1440px and 390px, local HTTP and file URLs | All 12 page/transport/viewport combinations passed; no page overflow or JavaScript errors |
| Header ZIP downloads over local HTTP | Actual downloads completed with matching filenames on desktop and mobile |
| Complete team-plan file copy | Copied content matched the full displayed file in all 12 combinations; test clipboard stub used |
| Theme control and screenshots | Checked all combinations; inspected desktop/mobile header and mobile skill captures |
| Repository structure/metadata check and git diff whitespace check | Passed |

The expanded skill retains the required name/description metadata and puts the
workflow in its Markdown body, following the
[official skill documentation](https://learn.chatgpt.com/docs/build-skills).
This update does not claim authenticated agent delegation, live recovery,
remote CI, deployment, or published-site verification. Existing C# application
behavior is unchanged; this update verified starter generation, not a new C# run.

## Previous rewrite

Rewritten 9 November 2026.

This log is a static Markdown download so the same relative link works in the
published site and the offline guides. It intentionally has no Jekyll front matter.

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
