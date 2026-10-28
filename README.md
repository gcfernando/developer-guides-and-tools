---
layout: default
title: "Developer Guides, Cheat Sheets & Tools"
description: "Python, data science, machine learning, C#/.NET, SQL and Azure guides, command cheat sheets, interactive references and practical developer tools."
permalink: /repository/
canonical_url: https://gcfernando.github.io/developer-guides-and-tools/
sitemap: false
---

# Developer Guides, Cheat Sheets & Tools

A practical library for learning **Python, data science, machine learning, C#/.NET, SQL and Azure**, finding **Linux, Git, Docker and Podman commands**, and using developer utilities, configuration examples and AI learning resources.

This collection combines the supplied KnowledgeBase, Other_Projects and MLHandbook folders. Choose a course for structured study, a reference for a specific question, or a documented example to run in your own practice environment.

[Getting started](docs/getting-started.md) · [All resources](documentation.md) · [Learning paths](docs/learning-paths/index.md) · [Interactive tools](apps/README.md) · [Utilities](tools/README.md)

## Contents

- [Choose a learning path](#choose-a-learning-path)
- [Data science and machine learning](#data-science-and-machine-learning)
- [Programming, databases and cloud](#programming-databases-and-cloud)
- [Command cheat sheets and interactive references](#command-cheat-sheets-and-interactive-references)
- [Developer utilities, examples and templates](#developer-utilities-examples-and-templates)
- [Use the collection locally](#use-the-collection-locally)
- [Repository structure](#repository-structure)
- [Build and validate](#build-and-validate)
- [Contributing, provenance and licensing](#contributing-provenance-and-licensing)

## Choose a learning path

| Your goal | Suggested starting point |
|---|---|
| Learn Python classes, design and testing | [Python learning path](docs/learning-paths/python.md) |
| Learn data preparation, model training and evaluation | [Data science and machine learning path](docs/learning-paths/machine-learning.md) |
| Learn C# and .NET object-oriented design | [C#/.NET learning path](docs/learning-paths/csharp-dotnet.md) |
| Learn SQL Server or MySQL | [SQL learning path](docs/learning-paths/sql.md) |
| Understand Azure services and resources | [Azure learning path](docs/learning-paths/azure.md) |
| Build a local Ollama and Streamlit chat app | [Local AI learning path](docs/learning-paths/local-ai.md) |

Reading requires a browser or Markdown viewer. Running an example requires the tools and environment named by its own guide; there is no installer that runs every project in this repository.

## Data science and machine learning

The [Data Science and Machine Learning Handbook with Python](docs/data-science/machine-learning-handbook.md) is an illustrated, code-first course with exercises, recorded outputs, datasets and a desktop project.

It covers Python, NumPy, pandas, charts and introductory statistics; data cleaning and feature engineering; model training and evaluation; supervised, unsupervised, semi-supervised and reinforcement learning; and model persistence, monitoring and database/JSON workflows.

The [complete handbook bundle](examples/machine-learning/ml-handbook/README.md) preserves all **125 supplied files**, including **91 images**, **31 CSV/JSONL/SQLite data files** and a **Tkinter house-price application** with training, prediction, updates, model history and rollback. Its original folder layout is retained so relative paths continue to work.

| Resource | Link |
|---|---|
| Read the integrated handbook | [Data science and machine learning guide](docs/data-science/machine-learning-handbook.md) |
| Set up notebooks or the desktop example | [Handbook setup and instructions](examples/machine-learning/ml-handbook/README.md) |
| Read the unchanged source | [Original Data_Science_Handbook.md](examples/machine-learning/ml-handbook/Data_Science_Handbook.md) |
| Explore the supplied data | [Datasets](examples/machine-learning/ml-handbook/datasets/) |
| Inspect the desktop application | [Tkinter app and model service](examples/machine-learning/ml-handbook/tkinter_app/) |

Use the bundle folder as the notebook working directory. The published handbook page is generated from the preserved source; edit that source and rebuild to keep them synchronized. Some chapters download additional data or require optional packages.

The figures and recorded outputs are supplied teaching material. Consolidation checks do not establish that every notebook example ran on every supported library version.

## Programming, databases and cloud

| Subject | Guides |
|---|---|
| Python | [Object-oriented programming](docs/python/oop.md) · [Special methods and attributes](docs/python/special-methods.md) |
| C# and .NET | [Object-oriented programming, design and testing](docs/csharp-dotnet/oop.md) |
| SQL | [SQL Server and MySQL course](docs/databases/sql-server-and-mysql.md) |
| Azure | [Engineering cheat sheet](docs/cloud/azure/engineering-cheat-sheet.md) · [Resource reference](docs/cloud/azure/resource-reference.md) |
| Local AI | [Ollama and Streamlit chat application lab](docs/ai/local-ai-chat-lab.md) |
| AI coding environments | [Coding add-ons installation and configuration guide](docs/ai/coding-addons.md) |

The long-form courses remain complete during this consolidation. Follow their prerequisites, exercise order and code context. Keep SQL dialects separate and check version-dependent cloud and tool details against their linked official sources.

## Command cheat sheets and interactive references

| Resource | Purpose | Start here |
|---|---|---|
| Git cheat sheet | Commits, branches, collaboration and recovery | [Git commands](docs/version-control/git-cheat-sheet.md) |
| Docker cheat sheet | Images, containers, builds, Compose and networking | [Docker commands](docs/containers/docker-cheat-sheet.md) |
| Podman cheat sheet | Rootless containers, pods, machines and Quadlet | [Podman commands](docs/containers/podman-cheat-sheet.md) |
| Linux command reference | Search 361 commands across 16 categories | [Browser page](apps/linux-command-reference/index.html) · [Offline use and maintenance](apps/linux-command-reference/README.md) |
| AI Learning Atlas | Explore 51 topic groups, 1,607 subtopics and 14 role paths | [Browser page](apps/ai-learning-atlas/index.html) · [Progress and backup guide](apps/ai-learning-atlas/README.md) |
| AI coding add-ons reader | Browse and filter the 39-add-on guide | [Standalone HTML](apps/ai-coding-addons/index.html) · [Markdown source](docs/ai/coding-addons.md) |

Download the whole Linux application folder for offline search; its HTML, data, JavaScript and styles belong together. The Atlas and AI add-ons readers are standalone HTML files. External documentation and badges require internet access where used.

Atlas completion is self-reported. Export a JSON progress backup before switching browsers, profiles, hosting locations or local-file contexts, then restore it in the new context.

## Developer utilities, examples and templates

| Resource | What it provides |
|---|---|
| [Windows system maintenance](tools/powershell/system-maintenance/README.md) | A PowerShell repair, update, networking and cleanup sequence, with behavior and limitations |
| [Line-ending converter](tools/powershell/convert-line-endings/README.md) | LF/CRLF conversion for supported UTF-8 text files |
| [Local services stack](examples/containers/local-services/README.md) | 11 services: SQL Server, Elasticsearch, Kibana, Oracle, MongoDB, RabbitMQ, MySQL, Kafka, Kafka UI, Redis and Keycloak |
| [WSL2 configuration](examples/wsl/README.md) | A sample CPU, memory, swap and networking configuration |
| [AI client configuration](examples/ai-clients/README.md) | Opt-in Codex and Claude snapshots, with Copilot configuration guidance |
| [AI instruction templates](templates/ai-instructions/README.md) | Reusable Codex, Claude, Copilot and ChatGPT instructions |
| [IPTV directory and VLC guide](docs/media/iptv/playlists.md) | A dated IPTV-org directory reference with screenshots and playback instructions |

Read each resource before running it. Windows maintenance immediately starts its fixed sequence. The Compose example requires local environment variables and binds published ports to loopback; its imported image tags are not a verified deployment.

The IPTV snapshot belongs to the media reference section and is separate from developer learning paths. A directory entry does not confirm that a third-party stream currently works.

## Use the collection locally

Open a guide directly on GitHub or use a local copy of this folder. Keep practice files, saved models and private configuration separate from authored reference material.

For machine learning notebooks, start in the complete bundle:

~~~sh
cd examples/machine-learning/ml-handbook
python -m venv .venv
~~~

Activate that environment for your terminal, then install the notebook packages:

~~~sh
python -m pip install -r requirements.txt
jupyter lab
~~~

For the smaller desktop example, install its dependency set and run from its application folder:

~~~sh
python -m pip install -r tkinter_app/requirements.txt
cd tkinter_app
python house_price_app.py
~~~

See the [handbook setup guide](examples/machine-learning/ml-handbook/README.md) for working-directory requirements, Tk support and generated model files. Other subjects have their own setup instructions.

## Repository structure

~~~text
docs/          Written guides and learning paths, organized by subject
apps/          Browser applications and companion guides
tools/         Executable utilities with their own instructions
examples/      Complete learning bundles, local services and configuration samples
templates/     Reusable AI instruction documents
scripts/       Catalog/HTML generation and validation
tests/         Application and content integrity checks
maintenance/   Content conventions, source inventories and migration records
_data/         Resource catalog, navigation and public page routes
_layouts/      Shared Jekyll layout
assets/        Shared website styles and branding
~~~

The complete MLHandbook is under examples/machine-learning/ml-handbook/. Its integrated documentation page is under docs/data-science/.

## Build and validate

Use Node.js 22 or newer for the documentation tooling:

~~~sh
npm ci
npm run build
npm test
~~~

The build generates the catalog, AI add-ons reader and published ML handbook. Tests check generated output, local file links, app structure, source provenance and the existing Linux reference behavior.

To validate the ML data and exercise its model service after installing the application dependencies:

~~~sh
python scripts/validate-ml-handbook.py --smoke
~~~

This runs training, prediction, update, persistence and rollback in a temporary workspace. It does not open the graphical application or execute every notebook block.

For the Jekyll website, use Ruby with Bundler:

~~~sh
bundle install
bundle exec jekyll build
npm run check:site
bundle exec jekyll serve
~~~

Open the local address printed by Jekyll. The site builds from the repository root with /developer-guides-and-tools/ as its configured base path.

Validation and GitHub Pages workflows are included. The owner still needs to publish the repository and enable Pages with GitHub Actions; this local consolidation does not deploy a public site.

## Contributing, provenance and licensing

See [CONTRIBUTING.md](CONTRIBUTING.md), the [content style guide](maintenance/content-style-guide.md) and [security reporting guidance](SECURITY.md).

All **176 original files** from the three supplied folders have a destination or explicit disposition in the [source map](maintenance/migration/source-map.csv). The originals remain intact. No Git history was present in the first two supplied folders.

[Migration notes](maintenance/migration/README.md) document the merged content and old URL mappings. Redirecting an old hosted page requires a separate action at that hosting location.

No reuse license was supplied for the original collections, and this consolidation does not grant new rights. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), including the dataset and external-source qualifications.
