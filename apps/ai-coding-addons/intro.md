## Start with one working assistant

Choose your environment in the sidebar. Only **documented integrations** appear by default. **Unverified** means this edition does not establish a working integration; it does not mean the tool can never work there. **Unavailable** means the required host capability is absent from that surface. No add-on integration is marked locally tested in this edition.

1. Open a small practice repository you can share with the selected providers. Make a checkpoint of existing work. Confirm its README build/test command works before adding tools.
2. Install **one** assistant using its official setup guide: [Claude Code](https://code.claude.com/docs/en/setup), [Codex](https://developers.openai.com/codex/quickstart), [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli), or [VS Code Copilot](https://code.visualstudio.com/docs/copilot/setup). Use a supported OS installation path; a WSL install is separate from native Windows.
3. Complete that assistant's sign-in, verify your account has access to the intended model/tools, and send one simple request without add-ons. For VS Code, use the Copilot harness in Chat and a supported agent mode. Availability can depend on organization policy and release channel.
4. Record the installed version. Run **only the command for your selected CLI**, or use **Help → About** for VS Code:

```terminal
claude --version
```

```terminal
codex --version
```

```terminal
copilot --version
```

5. Setup commands belong in the normal terminal. A fenced **Assistant chat** example belongs inside the named assistant. JSON/TOML examples belong in the indicated configuration file. Replace clearly named sample project values before use; never replace an environment-variable reference with a literal token in a tracked file.

### Choose by the problem you have

| Need | Start with | Check before adding more |
|---|---|---|
| Current library documentation | Context7 or OpenAI Developers for OpenAI APIs | Your assistant may already have documentation tools. Ask for a source and the project's dependency version. |
| Find callers or understand a large repository | Serena; Graphify when a persistent map helps | Built-in search, LSP and ordinary file reads may already be enough. |
| Inspect a running web app | Playwright MCP or Chrome DevTools MCP | Existing browser tools may suffice. Pick one initially. |
| Plan and implement carefully | One of Superpowers, Agent Skills, or a focused planning/testing plugin | Avoid installing several overlapping planning frameworks at once. |
| Review changes | One focused review plugin or CodeRabbit | Define the base branch, staged/uncommitted scope and whether findings stay local. |
| Reduce noisy command output | RTK | Prove a command was rewritten, then compare correctness and actual usage. |
| Resume previous work | Existing session resume first; memory only if needed | Decide what may persist, where, and how to erase it. |
| Route or compress model traffic | Headroom or OmniRoute, after basic tools work | These are advanced options requiring an understood provider and data path. |

The comparison table below includes documented environments, difficulty, estimated setup time, processing, accounts and cost model. Setup times are rough planning estimates for someone with a working assistant; they exclude account approval, downloads and troubleshooting.

### Shared prerequisites and installation scope

Install only the runtime needed by your selected card: [Node.js LTS](https://nodejs.org/en/download), [uv](https://docs.astral.sh/uv/getting-started/installation/), or [Docker](https://docs.docker.com/get-docker/). Check both the client and runtime, and reopen the terminal after changing PATH:

```terminal
node --version
npx --version
uv --version
docker version
```

`docker version` must show a responding server as well as a client. A version command showing an executable alone does not establish that a background service works. On Windows, if PowerShell blocks the npm wrapper, use `npm.cmd` or `npx.cmd`; keep the execution policy intact.

| Scope | Meaning | What to review |
|---|---|---|
| Runtime / executable | Available in this OS environment | PATH, runtime version, update channel; install separately inside WSL or a container when needed. |
| User plugin or MCP registration | Available to this assistant across repositories | Account connections and permissions; user configuration normally stays outside Git. |
| Project skill / hook / instruction | Files under the current repository | Review the diff and existing instructions before committing. Preserve unrelated rules. |
| Remote development | Processes run in SSH, WSL or a container | Install runtimes and credentials in that environment. Local installation alone is insufficient. |

For Claude MCP, the guide uses project registration through `--scope project` where practical. This writes `.mcp.json`; review it and never put a token in it. Codex CLI MCP examples register in the user's Codex configuration (normally `~/.codex/config.toml`), so check the project resolved by the server. Copilot CLI commonly stores MCP registration under `~/.copilot/mcp-config.json`; VS Code uses `.vscode/mcp.json` for workspace configuration or its user MCP configuration for user scope. Respect any custom home/profile path.

### Install, activate, then prove use

These are three separate checks: the manager lists the plugin; the host loads the relevant skill/hook/tools; a test task produces a trace or artifact from that integration. An ordinary AI answer does not prove the third check. Expand the selected card's environment instructions and capture its specified evidence.

For VS Code plugins, run **Chat: Open Customizations** in the Command Palette, choose the **Copilot harness**, open **Plugins / Browse**, review the publisher and install. If an older VS Code release exposes `@agentPlugins` in Extensions, use that release's documented workflow; do not assume it is the current UI. If a source is missing, configure a trusted marketplace or run **Chat: Install Plugin from Source**. Start a new chat using the same harness. See [official plugin discovery and source installation](https://code.visualstudio.com/docs/agent-customization/agent-plugins#_discover-and-install-plugins).

For Copilot CLI, inspect the registered marketplaces first. `awesome-copilot` is normally included. If it is missing, add the actual source, refresh/retry discovery, then install a specific plugin:

```terminal
copilot plugin marketplace list
copilot plugin marketplace browse awesome-copilot
```

Recovery only when the marketplace is missing:

```terminal
copilot plugin marketplace add github/awesome-copilot
```

For Claude's official plugins, open `/plugin` and inspect Discover. If the official marketplace is missing, add it inside Claude, then retry the exact install command in the card:

```chat
/plugin marketplace add anthropics/claude-plugins-official
```

For Codex, open `/plugins`. If a named plugin is missing, inspect configured sources with the following commands and consult its publisher's installation instructions. Installation is separate from account connection and hook trust:

```terminal
codex plugin marketplace list
codex plugin list
```

References: [Copilot marketplace commands](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing), [Claude plugins](https://code.claude.com/docs/en/plugins), [Codex plugins](https://developers.openai.com/plugins/).

### Permissions, credentials and data

Review what each integration can read, execute, store or transmit. A prompt saying “read only” is an instruction, not a permission boundary. Disable unnecessary write tools, use a test repository/account, and select read-only server modes where available. Hook execution is local code execution even when the requested task sounds harmless.

Create personal access tokens for your own authorized identity, or use an approved service identity. Ask an administrator to approve the access model rather than lend you someone else's token. Restrict repositories and scopes, set an expiry, complete organization SSO authorization where required, and revoke credentials no longer needed. Prefer browser OAuth when the client and server support it.

When a card uses an environment variable, retrieve the secret from your approved credential manager into the terminal's environment before launching the assistant. Do not echo it. A GUI launched elsewhere may not inherit that environment. Configuration files should refer to secret inputs or inherited environment variables; do not paste values into chat, shell history, screenshots, tracked JSON or TOML.

### Combining add-ons and measuring value

Start with one tool and keep a baseline. Planning frameworks can compete for task sequencing, skill names and automatic hooks. Memory tools can duplicate session-resume features. Browser servers can duplicate built-in tools. Add a second integration only for a distinct need, then inspect loaded tools and hooks for overlap.

RTK changes command output; Headroom changes model context; OmniRoute changes routing. Combining transformations makes attribution harder and can hide details needed to diagnose a failure. Compare the same task and dependency versions, with and without the integration, recording input/output tokens, cache hits, elapsed time, retries, correctness and actual charges. Reduced text does not guarantee reduced subscription fees, premium-request consumption or billed cost. Extra planning/review can increase usage.

### Small dictionary

| Term | Meaning |
|---|---|
| Plugin | A host-specific package that may bundle skills, tools, hooks and integrations. |
| Skill | Instructions and optional resources the assistant loads for a task. |
| MCP server | A process or remote service exposing tools to an assistant. |
| Hook | Code automatically triggered by a host event. |
| Token | A unit of model text; an API token/PAT is instead a secret credential. |
| Proxy / provider | An intermediary handling requests / the service running the model. |
| Canvas | A host-rendered interactive view; installing its package does not add canvas support to every client. |
