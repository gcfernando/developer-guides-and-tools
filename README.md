---
layout: default
title: "Developer Guides, Cheat Sheets and Practical Tools"
description: "Study Python, machine learning, C#/.NET, SQL and Azure. Find Linux, Git and container references, interactive learning tools and documented utilities."
permalink: /repository/
canonical_url: https://gcfernando.github.io/developer-guides-and-tools/
sitemap: false
---

<a id="developer-guides-cheat-sheets--tools"></a>
<a id="developer-guides-cheat-sheets-and-practical-tools"></a>

# Developer guides and tools

Practical guides, command references and examples for learning Python, machine learning, C#/.NET, SQL and Azure.

[![Repository standards](https://github.com/gcfernando/developer-guides-and-tools/actions/workflows/repository-standards.yml/badge.svg)](https://github.com/gcfernando/developer-guides-and-tools/actions/workflows/repository-standards.yml) [![Read the documentation](https://img.shields.io/badge/Read-the_documentation-2563eb?style=flat-square)](https://gcfernando.github.io/developer-guides-and-tools/)

Choose a resource below to start reading. **Open in browser** links launch the published reader; guide and setup links open readable Markdown on GitHub. Reading requires no installation. Each runnable example has its own requirements.

[Browser workbooks and tools](#open-a-workbook-or-tool-in-your-browser) · [Learning guides](#learning-guides) · [Command references](#command-and-browser-references) · [Utilities and examples](#utilities-environments-and-templates) · [Repository map](#repository-map) · [Complete catalog](documentation.md)

<a id="choose-a-learning-path"></a>
<a id="guide-choose-a-learning-path"></a>

## Start here

| Your goal | First step |
| --- | --- |
| Read the Data Science and Machine Learning workbook | **[Open the browser workbook](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/Data-Science-and-Machine-Learning.html)** or [read the Markdown edition](examples/machine-learning/ml-practical-lessons/Data-Science-and-Machine-Learning.md). |
| Learn a subject from the beginning | Choose a [learning path](docs/learning-paths/index.md), then follow its guides in order. |
| Search Linux commands or explore AI learning tools | Choose a [browser tool below](#open-a-workbook-or-tool-in-your-browser). |
| Find a specific command or concept | Use the [reference index below](#command-and-browser-references) or [complete resource catalog](documentation.md). |
| Run an example or utility | Choose a [practice environment](examples/README.md) or [PowerShell utility](tools/README.md), and read its setup and side effects first. |

New to the collection? The [getting-started guide](docs/getting-started.md) explains how to choose a resource and organize a practice session. Reading needs only a browser or Markdown viewer. There is no shared installer for all examples.

## Open a workbook or tool in your browser

Click **Open in browser** to use the resource immediately. Opening an `.html` file in GitHub's file list shows its source; these links open the published page instead.

| Resource | Open in browser | Setup, downloads or source guide |
| --- | --- | --- |
| **Data Science and Machine Learning workbook** | **[Open in browser](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/Data-Science-and-Machine-Learning.html)** | [Course and lesson downloads](examples/machine-learning/ml-practical-lessons/README.md) · [Python setup](examples/machine-learning/ml-practical-lessons/SETUP.md) · [Glossary](examples/machine-learning/ml-practical-lessons/GLOSSARY.md) |
| Linux command reference | [Open in browser](https://gcfernando.github.io/developer-guides-and-tools/apps/linux-command-reference/index.html) | [Search and offline-use guide](apps/linux-command-reference/README.md) |
| AI Learning Atlas | [Open in browser](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-learning-atlas/index.html) | [Study paths and progress backups](apps/ai-learning-atlas/README.md) |
| AI coding add-ons | [Open in browser](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-coding-addons/index.html) | [Installation and configuration guide](docs/ai/coding-addons.md) |
| Claude Code agent teams | [Open in browser](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/claude-code-guide.html) | [Team files, downloads and practice scripts](apps/ai-agent-team-guides/README.md) |
| OpenAI Codex agent teams | [Open in browser](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/openai-codex-guide.html) | [Team files, downloads and practice scripts](apps/ai-agent-team-guides/README.md) |
| GitHub Copilot agent teams | [Open in browser](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/github-copilot-guide.html) | [Team files, downloads and practice scripts](apps/ai-agent-team-guides/README.md) |

To find the ML workbook in GitHub's file list, follow **examples → machine-learning → ml-practical-lessons → Data-Science-and-Machine-Learning.html** ([view the file on GitHub](https://github.com/gcfernando/developer-guides-and-tools/blob/main/examples/machine-learning/ml-practical-lessons/Data-Science-and-Machine-Learning.html)). For offline use, download the repository and keep the workbook folder together so its diagrams and lesson downloads remain available.

<a id="programming-databases-and-cloud"></a>

## Learning guides

| Subject | Start with | Reference or practice material |
| --- | --- | --- |
| Python | [Python learning path](docs/learning-paths/python.md) | [Object-oriented programming](docs/python/oop.md) and [special methods](docs/python/special-methods.md) |
| C# and .NET | [C#/.NET learning path](docs/learning-paths/csharp-dotnet.md) | [Object-oriented design and testing](docs/csharp-dotnet/oop.md) |
| SQL | [SQL learning path](docs/learning-paths/sql.md) | [SQL Server and MySQL course](docs/databases/sql-server-and-mysql.md) or [ordered part readers](docs/databases/sql-server-and-mysql/index.md) |
| Azure | [Azure learning path](docs/learning-paths/azure.md) | [Engineering cheat sheet](docs/cloud/azure/engineering-cheat-sheet.md) and [resource reference](docs/cloud/azure/resource-reference.md) |
| Data science and machine learning | [Practical learning path](docs/learning-paths/machine-learning.md) | [Read the workbook](examples/machine-learning/ml-practical-lessons/Data-Science-and-Machine-Learning.md) · [Lesson downloads and setup](examples/machine-learning/ml-practical-lessons/README.md) |
| Local AI | [Local AI learning path](docs/learning-paths/local-ai.md) | [Ollama and Streamlit chat application lab](docs/ai/local-ai-chat-lab.md) |

Keep the courses' exercise order, prerequisites and code context. SQL Server and MySQL examples use different dialects. Figures and recorded outputs are teaching material; repository checks do not establish that every example runs with every library version. Version-dependent details should be checked against each guide's linked official sources.

<a id="command-cheat-sheets-and-interactive-references"></a>
<a id="guide-command-cheat-sheets-and-interactive-references"></a>

## Command and browser references

| Resource | What it helps you do |
| --- | --- |
| [Git cheat sheet](docs/version-control/git-cheat-sheet.md) | Find commands for commits, branches, collaboration and recovery. |
| [Docker cheat sheet](docs/containers/docker-cheat-sheet.md) | Work with images, containers, builds, Compose and networking. |
| [Podman cheat sheet](docs/containers/podman-cheat-sheet.md) | Look up rootless containers, pods, machines and Quadlet. |
| [Linux command reference](apps/linux-command-reference/README.md) | Search commands and usage examples in a browser; the guide explains offline use. |
| [AI Learning Atlas](apps/ai-learning-atlas/README.md) | Explore topics and role paths, then record and back up your own progress. |
| [AI coding add-ons](docs/ai/coding-addons.md) | Read installation and configuration notes, or use the [filterable browser reader](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-coding-addons/index.html). |
| Agent Team Guide | [Claude Code](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/claude-code-guide.html), [OpenAI Codex](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/openai-codex-guide.html), [GitHub Copilot](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-agent-team-guides/github-copilot-guide.html). |

For offline Linux search, keep the complete application folder together. The repository's Atlas and add-ons readers are standalone HTML files; external documentation links still need internet access. The published Atlas uses a lighter hosted version and offers the complete offline file for download. Atlas completion is self-reported: export a JSON backup before switching browsers, profiles, hosting locations or local-file contexts.

Keep the [AI agent team guide bundle](apps/ai-agent-team-guides/README.md) together for offline cross-links and practice-script downloads. Read its script prerequisites and side effects before running a practice setup.

<a id="developer-utilities-examples-and-templates"></a>

## Utilities, environments and templates

| Resource | What it provides |
| --- | --- |
| [Line-ending converter](tools/powershell/convert-line-endings/README.md) | Convert supported UTF-8 files between LF and CRLF. |
| [Windows system maintenance](tools/powershell/system-maintenance/README.md) | Inspect a fixed PowerShell repair, update, networking and cleanup sequence before deciding to run it. |
| [Local services stack](examples/containers/local-services/README.md) | Configure a practice Compose environment for databases, messaging, search and identity services. |
| [WSL2 configuration](examples/wsl/README.md) | Adapt memory, CPU, swap and networking settings for your machine. |
| [AI client configuration](examples/ai-clients/README.md) | Review opt-in Codex and Claude snapshots and Copilot guidance. |
| [AI instruction templates](templates/ai-instructions/README.md) | Reuse guidance for Codex, Claude, Copilot and ChatGPT deliberately. |
| [IPTV directory and VLC guide](docs/media/iptv/playlists.md) | Consult a dated media-directory reference with playback instructions. |

Windows maintenance starts its entire system-changing sequence immediately and has no dry-run mode. Read its prerequisites and limitations first. The Compose example needs local environment variables and binds published ports to loopback; its imported image tags have not been deployment-verified. An IPTV directory entry does not confirm that a third-party stream currently works.

<a id="use-the-collection-locally"></a>

## Use a local copy

```sh
git clone https://github.com/gcfernando/developer-guides-and-tools.git
cd developer-guides-and-tools
```

Open the selected guide or browser application from the copy. Follow its companion README to install dependencies and run examples. For the [ML practical lessons](examples/machine-learning/ml-practical-lessons/README.md), keep the complete workbook folder together and extract each lesson ZIP before running its Python scripts. Keep practice files and private configuration separate from reference material.

<a id="repository-structure"></a>

## Repository map

Use these entry points to browse each part of the collection. The [complete resource catalog](documentation.md) lists the reading formats by subject.

| Area | What you will find | Start here |
| --- | --- | --- |
| Learning paths | Suggested study order for Python, C#/.NET, SQL, Azure, machine learning and local AI | [Choose a path](docs/learning-paths/index.md) |
| `docs/` | Courses, cheat sheets, AI guides and the IPTV/VLC reference | [Browse guides by subject](documentation.md) |
| `apps/` | Linux search, AI Learning Atlas, coding add-ons and agent team browser guides | [Browse browser tools](apps/README.md) |
| `examples/` | ML lessons, local Compose services, WSL2 settings and AI client configuration | [Browse practice examples](examples/README.md) |
| `tools/` | PowerShell line-ending conversion and Windows maintenance | [Browse utilities](tools/README.md) |
| `templates/` | Reusable Codex, Claude, Copilot and ChatGPT instructions | [Choose an instruction template](templates/ai-instructions/README.md) |
| `maintenance/` | Content conventions, migration history and source provenance | [Content style](maintenance/content-style-guide.md) · [Migration record](maintenance/migration/README.md) · [Validation record](maintenance/validation-report.md) |
| Website | Published homepage, navigation, layout, styling and source-link conversion | [Homepage source](https://github.com/gcfernando/developer-guides-and-tools/blob/main/index.md) · [Navigation](https://github.com/gcfernando/developer-guides-and-tools/blob/main/_data/navigation.yml) · [Configuration](https://github.com/gcfernando/developer-guides-and-tools/blob/main/_config.yml) · [Layout source](https://github.com/gcfernando/developer-guides-and-tools/blob/main/_layouts/default.html) · [Styles](https://github.com/gcfernando/developer-guides-and-tools/blob/main/assets/css/documentation.css) · [Link plugin](https://github.com/gcfernando/developer-guides-and-tools/blob/main/_plugins/source_links.rb) |
| Resource catalog | Resource registrations and generated public routes | [Resource list](https://github.com/gcfernando/developer-guides-and-tools/blob/main/_data/resources.yml) · [Route map](https://github.com/gcfernando/developer-guides-and-tools/blob/main/_data/routes.json) |
| Build, tests and CI | Shared generators, link checks, app checks and publishing | [Development commands](#development-and-validation) · [Scripts](https://github.com/gcfernando/developer-guides-and-tools/tree/main/scripts) · [Tests](https://github.com/gcfernando/developer-guides-and-tools/tree/main/tests) · [Workflows](https://github.com/gcfernando/developer-guides-and-tools/tree/main/.github/workflows) |

App-specific sources and tests live beside their application. See [CONTRIBUTING.md](CONTRIBUTING.md) for source/output ownership and where to add material.

### How future additions fit

| New material | Recommended home |
| --- | --- |
| Written guide or cheat sheet | `docs/<subject>/` |
| Interactive reader or application | `apps/<application>/` |
| Runnable demonstration | `examples/<subject>/` |
| Single-runtime utility | `tools/<runtime>/<utility>/` |
| Multi-language utility | `tools/<utility>/` |
| Reusable starter configuration | `templates/<subject>/` |

<a id="build-and-validate"></a>
<a id="guide-build-and-validate"></a>

## Development and validation

Documentation contributors need Node.js 22 or newer and Python 3.12 or newer for the full build and checks. From the repository root:

```sh
npm ci
npm run build
npm test
```

The build generates the catalog, AI add-ons and Atlas readers, Linux command table and SQL part readers. Tests check generated output, links, provenance, Linux behavior, and Atlas content, runtime and embedded exercises. Edit generated content through its source as described in [CONTRIBUTING.md](CONTRIBUTING.md).

To build and preview the Jekyll website, install Ruby with Bundler, then run from the repository root:

```sh
bundle install
npm run site:build
npm run check:site
python scripts/serve-preview.py
```

Open the address printed by the preview server. The configured base path is `/developer-guides-and-tools/`. Rebuild after edits; this preview serves the built files without watching sources. The Pages workflow uses the same build command and deploys the website when changes reach `main`.

## Troubleshooting

- **An example cannot find its data:** use the working directory stated in its companion guide and preserve bundled relative paths.
- **A command or package differs:** check the installed version and the guide's official references; the collection contains dated snapshots.
- **Atlas progress is missing:** return to the original browser context or restore an exported JSON backup.
- **A local build reports stale generated output:** follow the source ownership rules in the contribution guide, rebuild and inspect the resulting changes.

<a id="contributing-provenance-and-licensing"></a>

## Contributing, support and license

Use [repository issues](https://github.com/gcfernando/developer-guides-and-tools/issues) for resource corrections and requests. Follow [CONTRIBUTING.md](CONTRIBUTING.md), the [content style guide](maintenance/content-style-guide.md) and the [repository standards](REPOSITORY_STANDARDS.md). Report sensitive findings through the [security guidance](SECURITY.md).

The [migration record](maintenance/migration/README.md) and [source map](maintenance/migration/source-map.csv) account for the original collections and preserved files. Old hosted URLs require redirects at their original hosting locations; the source map does not implement redirects.

No reuse license was supplied for the original collections, and this repository grants no new rights. Read [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), including the dataset and external-source qualifications, before reuse or redistribution.

<a id="repository-maintenance"></a>

<!-- Preserve links to earlier README sections. -->
<a id="contents"></a>
