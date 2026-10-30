# 🧰 Gehan's Project Lab — Developer Tools, Linux and AI Coding Guides

**Read online:** [Documentation website](https://gcfernando.github.io/developer-tools-and-guides/) · [All guides](documentation.md)

An offline Linux command reference, Windows PowerShell utilities, a Podman Compose development stack and practical developer guides.

[![Reference: Linux](https://img.shields.io/badge/Reference-Linux-FCC624)](https://gcfernando.github.io/developer-tools-and-guides/Linux_Commands/guide/)
[![Scripts: PowerShell](https://img.shields.io/badge/Scripts-PowerShell-5391FE)](https://gcfernando.github.io/developer-tools-and-guides/SystemMaintenance/)

## Open in your browser

“View page” opens the hosted version; the filename opens its GitHub source. For offline reading, download each page with its companion assets and follow its guide.

| HTML source | View page | Companion guide |
|---|---|---|
| [Files/AI-Learning-Atlas-Complete.html](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Files/AI-Learning-Atlas-Complete.html) | [Open AI Learning Atlas](https://gcfernando.github.io/developer-tools-and-guides/Files/AI-Learning-Atlas-Complete.html) | [Offline use and saved progress](Files/ai-learning-atlas.md) |
| [Files/ai_coding_plugins_beginners_guide.html](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Files/ai_coding_plugins_beginners_guide.html) | [Open AI coding add-ons guide](https://gcfernando.github.io/developer-tools-and-guides/Files/ai_coding_plugins_beginners_guide.html) | [Markdown edition](Files/ai_coding_plugins_beginners_guide.md) |
| [Linux_Commands/index.html](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Linux_Commands/index.html) | [Open Linux command reference](https://gcfernando.github.io/developer-tools-and-guides/Linux_Commands/) | [Usage and maintenance](Linux_Commands/readme.md) |

<a id="-a-colorful-collection-of-practical-tools-guides-references-and-local-dev-environments-"></a>

<!-- Preserve links to earlier section headings. -->
<a id="gehans-project-lab--developer-tools-linux-and-ai-coding-guides"></a>
<a id="-featured--ai-coding-add-ons-beginners-guide-"></a>
<a id="--open-the-live-guide-"></a>
<a id="-whats-in-the-lab"></a>
<a id="-get-started"></a>
<a id="-linux-commands"></a>
<a id="-iptv-world-explorer-2026"></a>
<a id="-system-maintenance"></a>
<a id="-wsl2-config"></a>
<a id="-services-at-a-glance"></a>
<a id="-linux-reference-highlights"></a>
<a id="-repository-layout"></a>
<a id="-faq"></a>
<a id="-related-repositories"></a>
<a id="️-responsible-use"></a>
<a id="-learn-something--build-something--keep-it-safe-"></a>
<a id="documentation-links"></a>

## 🔎 Overview

This collection is for developers, system administration learners and readers exploring AI coding tools. Each folder is independent. Running utilities or the container stack requires preparation for that particular tool.

## ✨ Features

| Resource | Purpose | Start here |
|---|---|---|
| Linux command reference | Search and filter 361 entries across 16 categories | [Usage and maintenance](Linux_Commands/readme.md) |
| AI coding add-ons guide | Setup and verification examples for 39 add-ons | [Markdown guide](Files/ai_coding_plugins_beginners_guide.md) |
| AI learning atlas | 51 topic groups, 1,607 subtopics and 14 suggested role paths | [Offline reader and progress guide](Files/ai-learning-atlas.md) |
| Windows maintenance | SFC, DISM, updates, network reset and cleanup | [Behavior and limitations](SystemMaintenance/readme.md) |
| Local services stack | Seven services: databases, broker and Kibana | [`Files/compose.yml`](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Files/compose.yml) |
| Line-ending converter | Convert supported UTF-8 files between LF and CRLF | [Examples](#line-endings) |
| WSL2 configuration | CPU, RAM, swap and networking settings | [`Files/.wslconfig`](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Files/.wslconfig) |
| IPTV directory | Dated IPTV-org snapshot and VLC walkthrough | [Playlist guide](Files/iptv_world_explorer_2026.md) |

The IPTV guide includes [authentic VLC screenshots](Files/iptv_world_explorer_2026.md#how-to-play). Directory entries do not prove that each third-party stream currently plays.

## 🚀 Quick start

```sh
git clone https://github.com/gcfernando/developer-tools-and-guides.git
cd developer-tools-and-guides
```

Open the [Linux command reference](https://gcfernando.github.io/developer-tools-and-guides/Linux_Commands/) in a browser. The table works without JavaScript; search and filtering require it. The downloaded reference works offline; Google Fonts are an optional online enhancement.

Use the [documentation index](documentation.md) for written guides. The AI add-ons [HTML edition](https://gcfernando.github.io/developer-tools-and-guides/Files/ai_coding_plugins_beginners_guide.html) and Markdown edition are maintained separately.

## 📦 Prerequisites and installation

| Component | Requirements |
|---|---|
| Browser references | Modern browser; JavaScript for filtering |
| Linux reference maintenance | Node.js; CI uses Node.js 22 |
| PowerShell utilities | PowerShell on Windows; administrator rights for maintenance |
| Container stack | Podman and a Compose provider; memory/disk for selected services |
| WSL settings | WSL2; setting support depends on installed Windows/WSL versions |
| Playlist playback | Internet and an M3U network-playlist player |

There is no repository-wide installer. Follow the selected guide rather than running every example.

## ⚙️ Configuration

Review `x-variables` in [`Files/compose.yml`](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Files/compose.yml): image tags, example credentials and timezone. Confirm image availability and platform compatibility before pulling. Published ports omit a host IP, so they are not restricted to loopback ([Compose port syntax](https://docs.docker.com/reference/compose-file/services/#ports)). Choose appropriate bindings and credentials before startup; Elasticsearch security is disabled in this example.

| Service | Checked-in image tag | Host port(s) |
|---|---|---|
| SQL Server | `2025-latest` | `1433` |
| Elasticsearch | `9.5.2` | `9200` |
| Kibana | `9.5.2` | `5601` |
| Oracle XE | `21-slim` | `1521` |
| MongoDB | `8.0.30-noble` | `27017` |
| RabbitMQ | `4.3.5-management` | `5672`, `15672` |
| MySQL | `8.4.11` | `3306` |

Merge [`Files/.wslconfig`](https://github.com/gcfernando/developer-tools-and-guides/blob/main/Files/.wslconfig) into `%UserProfile%\.wslconfig`, choosing values for your machine. The sample uses up to 8 GB RAM, eight logical processors and 4 GB swap. Save WSL work before `wsl --shutdown`; it stops distributions so settings take effect on restart.

## 💡 Usage

<a id="-local-services-stack"></a>

### Local services stack

From the root, after reviewing configuration:

```powershell
# Inspect before creating services.
podman compose -f Files/compose.yml config

# Start only MySQL; omit mysql to start all services.
podman compose -f Files/compose.yml up -d mysql
podman compose -f Files/compose.yml ps
podman compose -f Files/compose.yml logs mysql

# Retain named data volumes when stopping.
podman compose -f Files/compose.yml down
```

The resolved configuration contains example passwords; keep it out of public reports. Six named volumes retain data across a normal `down`. Adding `-v` deletes those volumes and their data. Image tags describe the configuration, not a verified deployment.

Kibana's `depends_on` names Elasticsearch without a health condition. It orders startup but does not wait for Elasticsearch to become healthy. Inspect the individual service logs when startup is incomplete.

### AI learning atlas

Open the [AI Learning Atlas](https://gcfernando.github.io/developer-tools-and-guides/Files/AI-Learning-Atlas-Complete.html) directly in a browser. The handbook includes role paths, searchable subtopics, suggested labs, a reusable tutor prompt and local progress controls. It does not run a model or assess your work. See the [reader guide](Files/ai-learning-atlas.md) for storage, backup and completion limits.

<a id="line-endings"></a>
<a id="-line-ending-converter"></a>

### Line-ending converter

The second argument is the **existing** ending to convert **from**. Begin with a disposable file or committed working tree:

```powershell
# LF to CRLF.
.\Files\Convert-LineEndings.ps1 .\example.txt LF

# CRLF to LF.
.\Files\Convert-LineEndings.ps1 .\example.txt CRLF

git ls-files --eol
```

Folder mode includes hidden files, prunes `.git`, `bin`, `obj` and `node_modules`, and skips reparse points. Explicit file arguments are processed directly. Empty files, NUL-containing files and UTF-8 BOM files are skipped. Invalid UTF-8 is reported as a failure. Converted files use UTF-8 without BOM. Review output counts: the script does not set a failure exit code.

### Windows maintenance

Read the [maintenance guide](SystemMaintenance/readme.md) and script first. From an elevated PowerShell at the repository root:

```powershell
.\SystemMaintenance\SystemMaintenance.ps1
```

The full sequence runs immediately. It can install updates, interrupt networking, delete diagnostics and temporary files, and schedule disk repair. There is no dry-run mode or per-task selection.

## 🏗️ Architecture

```text
Files/                 Guides, Compose/WSL examples and converter
Linux_Commands/        data.js → generated index.html; app.js adds search
SystemMaintenance/     Windows maintenance script and behavior guide
_config.yml            Jekyll documentation-site configuration
_layouts/ and assets/  Documentation presentation
```

`Linux_Commands/data.js` is the command source of truth. `generate-static.cjs` embeds it into `index.html`; `app.js` creates the interactive view from the same data. The HTML and Markdown AI add-ons editions are separate files.

## 🧪 Development and testing

Run the existing checks from the repository root:

```sh
node Linux_Commands/seo.test.cjs
node --check Linux_Commands/app.js
node Linux_Commands/generate-static.cjs --check
```

After editing `data.js`, run `node Linux_Commands/generate-static.cjs` and review the generated HTML. [CI](https://github.com/gcfernando/developer-tools-and-guides/blob/main/.github/workflows/seo.yml) runs the reference test and JavaScript syntax check. These do not validate Linux command execution, Windows repair outcomes or container startup.

## 🛠️ Troubleshooting and limitations

| Symptom | What to check |
|---|---|
| Search shows no rows | Clear query/category; keep `data.js` and `app.js` next to the page |
| Generated reference is stale | Regenerate `index.html` and rerun checks |
| Compose cannot start | Inspect provider, image tag, architecture, memory, ports and logs |
| Converter reports failures | Check encoding and permissions; review counts and Git diff |
| Maintenance reports completion after errors | Review native output; exit codes are not consistently checked |
| AI add-on instructions differ | Check publisher instructions and installed client version |
| A playlist channel fails | Follow the guide's diagnostics; availability and access vary |

## 🤝 Contributing

Propose focused corrections through the [repository](https://github.com/gcfernando/developer-tools-and-guides), with the file, environment, expected behavior and verification. Keep Linux HTML synchronized with `data.js`, and update both guide editions when changing shared AI add-on content.

## 🔒 Security

Keep private data and credentials out of reports. Use private security reporting if available, or arrange a private channel with the maintainer. Practise security commands only on authorized systems and open streams only where permitted.

## 📄 Support and license

Report documentation problems in [repository issues](https://github.com/gcfernando/developer-tools-and-guides/issues). No license file is present in this checkout; public visibility alone does not specify reuse rights. Refer to upstream projects for their licensing and support.

[Documentation index](documentation.md) · [Knowledge base](https://github.com/gcfernando/developer-guides-and-cheatsheets) · [Python examples](https://github.com/gcfernando/python-projects-and-examples) · [C# examples](https://github.com/gcfernando/csharp-dotnet-examples)
