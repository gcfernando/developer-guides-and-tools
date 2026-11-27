## Troubleshoot the failed layer

| Symptom | Check | Next step |
|---|---|---|
| Command not found | Runtime executable, PATH, native Windows versus WSL | Reopen the terminal; use the runtime's official install and shell-update instructions. Check inside the environment running the assistant. |
| MCP server stays “starting” | Launch command, arguments, required Node/Python version and server log | Run a harmless `--help` check, then inspect the host's MCP output. Increase a timeout only after diagnosing a slow legitimate startup. |
| `npx` waits or exits on startup | First-run package confirmation or network failure | Run the package's `--help` once interactively. MCP launch examples use `-y` to avoid an invisible install prompt; review the named package first. |
| Docker installed but connection fails | `docker version` server section, image pull, container log | Start the approved daemon, validate its context, then retry. Do not add `-t` to a stdio MCP container. |
| Connected but no useful tools | Tool chooser, disabled tools, selected harness and account | Enable the specific required read tool, restart/new session and inspect the actual tool call. |
| Plugin installed but no skill loaded | Installed component names and command completion | Invoke the documented namespaced command or select the installed skill explicitly. A generic answer is not proof. |
| Authentication denied or expired | Account, token expiry, repository access, SSO, credential environment | Reauthorize through the supported browser flow or refresh your own scoped credential. Verify the assistant inherits its environment. |
| Browser missing | Supported Chrome/Playwright browser and server launch log | Install the browser requested by that server, use a clean test profile, and retry the printed local app URL. |
| Global MCP server sees wrong project | Working directory and project activation | Reopen the assistant from the intended root; verify the server's active project before asking questions. |
| Marketplace/plugin missing | Registered source, selected harness, edition and organization policy | Refresh or add the documented source. An absent host feature needs a compatible release/account; do not substitute another client's files. |
| Port already in use | Owning process and configured callback/proxy port | Stop only a process you own or choose a publisher-supported alternative port. |

## Disable, remove and restore

Before installation, record the files/settings changed and save their previous values outside any directory the tool replaces. When removing an integration: disable it first, stop its background process, remove its registration, restore only the settings it changed, and revoke account connections or tokens no longer used. Do not erase unrelated client configuration.

For Claude use `/plugin` to disable/uninstall plugins; for MCP use the registered name and correct scope:

```terminal
claude mcp remove example-server --scope project
```

For Codex, use its manager or the following examples, replacing identifiers with those shown in your installed list:

```terminal
codex plugin remove example-plugin
codex mcp remove example-server
```

For Copilot CLI:

```terminal
copilot plugin disable example-plugin
copilot plugin uninstall example-plugin
```

Use `/mcp` to remove its MCP entry. For VS Code use Customizations → Plugins → Disable/Uninstall, or **MCP: List Servers** to stop the server and remove that entry from the appropriate MCP configuration. Remove a marketplace only after removing dependent plugins. For project skills/hooks, inspect the recorded diff and restore only those changes. Stored memory, exported reports and browser profiles need a separate retention/deletion decision.

## Documentation and verification notes

This edition distinguishes a **documented integration** from a **locally executed setup**. Each card links its publisher evidence, states version/OS qualifications, and records the review date. Sources on moving branches may change; record a release or commit when adopting a tool. “Unverified” is not a compatibility guarantee or a claim that support is impossible.

**Review date: 2026-11-27.** The HTML reader is built and checked locally. Add-on installation, paid accounts, authorization, provider calls and integration smoke tests have not been executed as part of this edit. No macOS/Linux/WSL integration test result is claimed. Package minimums are listed where the inspected publisher documents them; a missing minimum is explicitly identified rather than guessed.

Use this template for each environment you actually test. The guide does not prefill passes:

```text
Add-on and exact package version:
Publisher release/commit or documentation URL:
Date:
OS and version (native / WSL / container / SSH):
Assistant and exact version:
Installation scope and changed files:
Account / entitlement (no credentials):
Integration method (plugin / skill / MCP / hook / proxy):
Install listed: PASS / FAIL / NOT RUN
Component active: PASS / FAIL / NOT RUN
Smoke test and observed tool/hook/report evidence:
Result: PASS / FAIL / NOT RUN
Data destination and measured cost, if relevant:
Disable / restore result:
```

A UI exploration is not automatically a reproducible E2E test. Commit an appropriate test and run it with the project's actual test command when that is the goal. An AI review or clean scanner result is limited to the selected scope, rules, dependencies and execution conditions; it is not proof that the repository has no defects.

### Maintain this edition

The standalone folder now contains its own sources: `guide.json` (39 structured cards and compatibility), `intro.md`, `closing.md`, `styles.css`, `app.js`, and `build.cjs`. From **apps/ai-coding-addons**, install locked dependencies and rebuild:

```terminal
npm ci --ignore-scripts
npm run build
npm run check:generated
npm test
npm run test:browser
```

On Windows use `npm.cmd` when the PowerShell npm wrapper is blocked. Browser checks use an isolated headless browser profile; see the local README for prerequisites and executable selection.

**Repository build integration remains a separate maintenance step:** the older repository-level `scripts/build-ai-addons.cjs` still reads `docs/ai/coding-addons.md`. Those files were outside this edit session's writable directory. Running the old root `npm run build:addons` can overwrite this edition. Until a maintainer redirects that root script to this folder's `build.cjs`, rebuild here after a root build and run `check:generated` here. See the local README for the exact proposed root change. The standalone sources preserve these fixes without requiring edits to generated HTML.

[Original Markdown source in the repository](https://github.com/gcfernando/developer-guides-and-tools/blob/main/docs/ai/coding-addons.md) · [Original generator](https://github.com/gcfernando/developer-guides-and-tools/blob/main/scripts/build-ai-addons.cjs) · [Repository documentation](https://gcfernando.github.io/developer-guides-and-tools/documentation/)
