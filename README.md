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

Practical guides, command references and examples for learning Python, C#/.NET, SQL, Azure and machine learning.

[![Repository standards](https://github.com/gcfernando/developer-guides-and-tools/actions/workflows/repository-standards.yml/badge.svg)](https://github.com/gcfernando/developer-guides-and-tools/actions/workflows/repository-standards.yml) [![Read the documentation](https://img.shields.io/badge/Read-the_documentation-2563eb?style=flat-square)](https://gcfernando.github.io/developer-guides-and-tools/)

Use this library when you want a structured learning path, a command to look up, or a documented example to adapt. Read in your browser on GitHub or the [documentation website](https://gcfernando.github.io/developer-guides-and-tools/); each runnable resource has its own requirements.

<a id="choose-a-learning-path"></a>
<a id="guide-choose-a-learning-path"></a>

## Start here

| Your goal | First step |
| --- | --- |
| Learn a subject from the beginning | Choose a [learning path](docs/learning-paths/index.md), then follow its guides in order. |
| Find a specific command or concept | Use the [reference index below](#command-and-browser-references) or [complete resource catalog](documentation.md). |
| Run an example or utility | Choose a [practice environment](examples/README.md) or [PowerShell utility](tools/README.md), and read its setup and side effects first. |

New to the collection? The [getting-started guide](docs/getting-started.md) explains how to choose a resource and organize a practice session. Reading needs only a browser or Markdown viewer. There is no shared installer for all examples.

<a id="data-science-and-machine-learning"></a>
<a id="guide-data-science-and-machine-learning"></a>
<a id="programming-databases-and-cloud"></a>

## Learning guides

| Subject | Start with | Reference or practice material |
| --- | --- | --- |
| Python | [Python learning path](docs/learning-paths/python.md) | [Object-oriented programming](docs/python/oop.md) and [special methods](docs/python/special-methods.md) |
| C# and .NET | [C#/.NET learning path](docs/learning-paths/csharp-dotnet.md) | [Object-oriented design and testing](docs/csharp-dotnet/oop.md) |
| SQL | [SQL learning path](docs/learning-paths/sql.md) | [SQL Server and MySQL course](docs/databases/sql-server-and-mysql.md) |
| Azure | [Azure learning path](docs/learning-paths/azure.md) | [Engineering cheat sheet](docs/cloud/azure/engineering-cheat-sheet.md) and [resource reference](docs/cloud/azure/resource-reference.md) |
| Machine learning | [Machine learning path](docs/learning-paths/machine-learning.md) | [Illustrated handbook](docs/data-science/machine-learning-handbook.md) and [datasets, notebook setup and Tkinter example](examples/machine-learning/ml-handbook/README.md) |
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

For offline Linux search, keep the complete application folder together. The Atlas and add-ons readers are standalone HTML files; external documentation links still need internet access. Atlas completion is self-reported: export a JSON backup before switching browsers, profiles, hosting locations or local-file contexts.

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

Open the selected guide or browser application from the copy. Follow its companion README to install dependencies and run examples. For notebooks and the house-price application, use the [handbook setup guide](examples/machine-learning/ml-handbook/README.md); it explains working directories, Tk support, optional dependencies and generated model files. Keep practice files, saved models and private configuration separate from reference material.

<a id="repository-structure"></a>

The content is grouped into `docs/` (guides), `apps/` (browser tools), `tools/` (utilities), `examples/` (practice environments) and `templates/` (reusable instructions). The [resource catalog](documentation.md) indexes them; `scripts/` and `tests/` maintain the documentation, and `maintenance/` records content conventions and provenance.

<a id="build-and-validate"></a>
<a id="guide-build-and-validate"></a>

## Development and validation

Documentation contributors need Node.js 22 or newer. From the repository root:

```sh
npm ci
npm run build
npm test
```

The build generates the resource catalog, AI add-ons reader and published ML handbook. Tests check generated output, local links, application structure, provenance and Linux-reference behavior. Edit generated content through its source as described in [CONTRIBUTING.md](CONTRIBUTING.md). The [handbook validation guide](examples/machine-learning/ml-handbook/README.md#guide-validation) explains the optional Python model-service smoke check; it does not open the GUI or execute every notebook block.

To build and preview the Jekyll website, install Ruby with Bundler, then run from the repository root:

```sh
bundle install
bundle exec jekyll build
npm run check:site
bundle exec jekyll serve
```

Open the address printed by Jekyll. The configured base path is `/developer-guides-and-tools/`. The Pages workflow builds and deploys the website when changes reach `main`.

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
