# Disposition of the 40 review findings

Reviewed and revised: 2026-11-27. Entries 1–39 are implemented in the standalone
reader and its maintained local sources. Item 40 is integrated with the parent
generator and root tests. The original handoff patch remains as historical evidence.
Integration instructions are documentation-based; no add-on account was connected
or package installed on the user's behalf.

| Finding | Applied change / evidence |
|---|---|
| 1 | My AI Usage is a canvas-host entry with Node 22.13+; CLI installation is distinguished from UI support. |
| 2 | PR Review requires its real canvas and grouped/expandable diffs; ordinary CLI/VS Code chat is not claimed as equivalent. |
| 3 | Five explicit compatibility statuses per card; unknown paths are labeled and excluded by default. |
| 4 | Environment filter uses documented compatibility metadata, not only section headings. |
| 5 | Common warnings, prerequisites and cleanup are outside client sections and remain visible. |
| 6 | Navigation and comparison links target each article's own stable `card-*` ID; legacy fragments are resolved by the reader. |
| 7 | Verification-notes ID belongs to the actual closing section. |
| 8 | Every documented path requires specific skill/tool/hook activity, output or a matching artifact. |
| 9 | CodeRabbit CLI, Git repository, agent authentication and scope checks precede review. |
| 10 | Ponytail Codex setup includes `/hooks`, lifecycle-hook review/trust and a fresh thread. |
| 11 | Security Guidance lists host/Python/auth prerequisites and automatic pattern/diff/commit review behavior. |
| 12 | SonarQube has complete Claude/Codex container commands, Copilot form arguments and VS Code secret-input JSON, plus Cloud/Server variants. |
| 13 | Onboarding covers assistant installation, sign-in, entitlement, version and a baseline task. |
| 14 | Per-card version/OS qualifications and a blank execution matrix distinguish documented support from tests actually run. |
| 15 | Current VS Code Customizations workflow, Copilot harness and source installation replace blanket Extensions searches. |
| 16 | Marketplace listing/registration/recovery steps accompany community plugin installation. |
| 17 | User, workspace/project and runtime scope are explained, with config destinations and commit guidance. |
| 18 | Runtime installation and separate per-client/per-environment registration are distinguished. |
| 19 | Browser entries document Node and Chrome/browser requirements and use noninteractive stdio launch arguments. |
| 20 | Chrome DevTools statistics/CrUX behavior is disclosed; examples include opt-out flags. |
| 21 | Claude-Mem documents local storage, optional cloud sync, observer destination, telemetry and retention/deletion. |
| 22 | Memory test uses a unique value, fresh thread and observation/retrieval traces, with confounders called out. |
| 23 | GitHub credentials belong to the intended identity; permissions, expiry, SSO and environment inheritance are explained. |
| 24 | Read-only prompt intent is distinguished from token/tool enforcement; GitHub examples use the read-only endpoint. |
| 25 | Figma requires a permitted file/node URL, matching account, available connected tools and retrieved design evidence. |
| 26 | Named workflows/skills/agents and specific artifacts replace generic verification prompts, including Semgrep setup and Claude Security reports. |
| 27 | Java/.NET SDK, wrapper, framework and baseline-test guidance plus a TypeScript LSP worked example are included. |
| 28 | Troubleshooting covers PATH, runtime mismatch, npx confirmation, Docker daemon, auth, MCP startup, tools, hooks and project resolution. |
| 29 | Every card has cleanup plus shared plugin/MCP disable, removal, restore and credential-revocation instructions. |
| 30 | Overlap among planning frameworks, memory, browsers, compression and routing is explained. |
| 31 | Decision table and 39-entry comparison matrix cover purpose, hosts, difficulty, setup estimates, data, accounts and cost. |
| 32 | Token reduction, correctness, retries/cache, latency and actual billing are separated. |
| 33 | Labeled fenced commands/configuration render real copy controls with a manual selection fallback. |
| 34 | Card, sidebar and comparison-row visibility stay synchronized. |
| 35 | Search excludes hidden clients' setup text and compatibility metadata. |
| 36 | Empty state, clear controls, direct-link reveal, legacy fragments and malformed-hash handling are implemented. |
| 37 | Keyboard skip link, focus visibility, reduced motion, persistent theme and contrast checks are implemented; mobile overflow fixed. |
| 38 | Duplicate full index removed; client sections, compatibility, cleanup and matrix are collapsible; unknown paths are not repeated as setup sections. |
| 39 | Each card has publisher evidence, review date, version/OS qualifications and an explicit not-executed integration status. |
| 40 | Local deterministic source/build added. The parent generator delegates to `build.cjs`, root tests include the reader checks, and original Markdown fragments remain. `repository-build-integration.patch` is retained as the historical handoff, not an instruction to reapply it. |

## Verification

- `node build.cjs --check`: output agrees with maintained sources.
- `npm test`: six structural/content/build checks.
- `npm run test:browser`: 19 checks across loopback HTTP, offline file loading and
  blocked storage, using isolated Microsoft Edge with a mocked clipboard.
- Browser checks include per-environment filtering, shared warnings, result and
  navigation counts, hidden-client search, direct/legacy/malformed fragments,
  copy success/fallback, theme persistence, sampled text contrast, keyboard
  navigation, reduced motion and 390-pixel mobile overflow.
- No live add-on authentication, account entitlement, provider traffic or
  macOS/Linux/WSL integration test is claimed.

The complete root `npm test` also passed in an isolated tracked-file copy after
applying the prepared CI integration: all generator checks, Atlas checks,
40 root/reader Node tests, five external-link Python tests, migration verification,
and the local-link audit passed. The parent browser-check selectors were updated
in the patch; the full parent browser suite was not executed in that copy.

The parent repository now delegates to the maintained generator. Use the current
root and scoped commands in [the reader build instructions](README.md); the handoff
patch is not needed for this integrated checkout.
