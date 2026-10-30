---
layout: default
permalink: /apps/linux-command-reference/guide/
title: "Linux Command Reference — Search 361 Commands Offline"
description: Search 361 Linux commands across 16 categories, read examples and use the reference offline. Review tool requirements and authorized-use boundaries.
---

[Developer guides and tools](../../README.md) · **Linux and security**

<a id="linux-command-reference-for-cybersecurity--361-commands-searchable-and-offline-"></a>

# Linux Command Reference — Search 361 Commands Offline

Find Linux commands by category, description or usage example in a browser. This offline reference contains 361 catalog entries for system administration, penetration testing, capture-the-flag exercises and digital forensics; execution requires the relevant Linux tools and authorization.

---

> *Examples span reconnaissance, permissions, networking, forensics and reverse engineering. Tool availability and options depend on the installed packages and Linux distribution.*

<!-- Preserve links to earlier section headings. -->
<a id="️-whats-inside"></a>
<a id="-what-you-get"></a>
<a id="️-how-to-use-it"></a>
<a id="-features"></a>
<a id="-quick-examples"></a>
<a id="-who-is-this-for"></a>
<a id="-related"></a>
<a id="documentation-links"></a>

<a id="guide-prerequisites"></a>

## Prerequisites

A modern browser is enough for reading. JavaScript enables search and filters. Node.js is required only when maintaining generated HTML or running the checks. To execute catalog examples, use a Linux environment with the relevant packages and permissions.

---

<a id="guide-features-and-categories"></a>

## Features and categories

| Category | Commands | Focus |
|---|---|---|
| 📁 File & Directory | 25 | Navigation, search, attributes |
| 📝 Text & File Content | 26 | grep, awk, sed, strings, hex |
| 🔒 Permissions | 12 | chmod, sudo, ACLs, SUID |
| 👤 User Management | 16 | useradd, last, lastb, finger |
| ⚙️ Process Management | 26 | ps, strace, lsof, cron |
| 🌐 Networking | 52 | nmap, nc, tcpdump, aircrack |
| 🔐 Crypto & Hashing | 19 | hashcat, john, hydra, gpg |
| 🖥️ System Info | 32 | uname, env, journalctl |
| 📦 Package Management | 14 | apt, pip, gem, cargo |
| 💾 Disk & Filesystem | 15 | dd, shred, mount, forensics |
| 🐚 Shell & Scripting | 17 | bash, TTY upgrades, traps |
| 🗜️ Archives | 11 | tar, zip, 7z, rar |
| 🔗 Remote Access | 14 | ssh tunnels, tmux, rsync |
| 🔍 Forensics & Logs | 20 | gdb, radare2, volatility |
| ⬆️ Privilege Escalation (`PrivEsc`) | 16 | SUID, capabilities, PrivEsc |
| 🛠️ Misc Utilities | 46 | docker, kubectl, scripting |
| **Total** | **361** | |

Counts are taken from `data.js`. They count catalog entries, including repeated command names in different categories, rather than 361 distinct installed executables. The source header's older “380+” comment does not match the current data.

---

## Project structure

```text
apps/linux-command-reference/
├── index.html     ← open in any browser, works offline
├── styles.css     ← hacker terminal aesthetic
├── data.js        ← all 361 commands + real-world usage
└── app.js         ← search, filter, category pills
```

## Quick start

[Open the published Linux command reference](https://gcfernando.github.io/developer-guides-and-tools/apps/linux-command-reference/index.html). For offline use, keep the downloaded HTML, CSS and scripts together:

1. Download or clone the [developer-guides-and-tools repository](https://github.com/gcfernando/developer-guides-and-tools).
2. Open `apps/linux-command-reference/index.html` in any modern browser — no installation, build step, or web server is needed.
3. Type in the search box or click a category to filter the commands.

To add or change a command, edit `data.js`: each entry is an array of `[command, category, description, usage]`, where the usage field may contain HTML such as `<code>` and `<br>`.

After editing `data.js`, run `node generate-static.cjs` in this folder and commit the updated `index.html`. The generator embeds the same command reference in the HTML so it remains readable without JavaScript; search and filtering still run in the browser. Run `node generate-static.cjs --check` to verify the embedded table is current. Node.js is only needed for maintenance, not for browsing the reference.

---

## Browser behavior

- 🔎 **Live search** — filter by command name, category, or usage
- 🏷️ **Category pills** — click to filter by topic instantly
- 💻 **Usage examples** — each command includes an example to read and adapt
- **Terminal theme** — scanlines, phosphor green, grid
- 📴 **Offline** — no internet required after download (the page can optionally load Google Fonts when online)
- **Separate source files** — HTML, CSS, and JS fully separated

---

## Read-only practice examples

These examples inspect your current Linux environment:

```bash
# Print the working directory.
pwd

# Read local help for a command before adapting an example.
man find

# List files, including hidden names, in the current directory.
ls -la
```

The catalog also includes commands that alter files, permissions, networking or services. Read the surrounding context and work only in an environment you are authorized to administer or test.

<a id="guide-development-and-verification"></a>

## Development and verification

From the repository root:

```sh
node apps/linux-command-reference/seo.test.cjs
node --check apps/linux-command-reference/app.js
node apps/linux-command-reference/generate-static.cjs --check
```

The test verifies 361 entries, 16 categories, generated-table consistency, literal search and safe command markup. It does not execute or verify the Linux commands themselves. The [Validate library workflow](https://github.com/gcfernando/developer-guides-and-tools/actions/workflows/validate.yml) runs these checks through `npm test` with Node.js 22.

## Troubleshooting and limitations

### Reading the existing command descriptions

Some catalog descriptions need qualification. The reference checks validate the browser data and generated table; they do not establish that every example does what its annotation says.

| Entry | Correction when interpreting the catalog |
|---|---|
| `wc` | GNU `wc -c` counts bytes and `-m` counts characters; `-b` is not its byte-count option. See the [GNU manual](https://www.gnu.org/s/coreutils/manual/html_node/wc-invocation.html). |
| `sed` | The example without an in-place option prints transformed text; it does not change the named configuration file. See the [sed overview](https://www.gnu.org/software/sed/manual/html_node/Overview.html). |
| `xargs` | Default whitespace splitting can misinterpret filenames with spaces or newlines. NUL-delimited input is needed when handling arbitrary filenames; see [GNU filename handling](https://www.gnu.org/software/findutils/manual/html_node/find_html/Safe-File-Name-Handling.html). |
| `test` | `test -f` checks whether a path is a regular file, not whether its contents can be read. |
| `strings` | `/proc/PID/exe` refers to the process's executable file; reading it does not inspect the process's live memory. |

Search is a case-insensitive literal substring match across all four fields. It does not parse regular expressions or split a query into independent words. Highlighting applies to command names and descriptions; matching usage text can remain unhighlighted. Use the category dropdown for keyboard selection; the clickable category pills are spans without equivalent keyboard handlers.

- If search returns nothing, clear both the category and search query.
- Keep `index.html`, `styles.css`, `data.js` and `app.js` together when copying the reference.
- Without JavaScript, the generated table remains readable; live filters require JavaScript.
- A missing Google Font does not prevent offline use.
- Commands span multiple distributions and optional packages; check the installed tool's help rather than assuming every entry is available.

---

## Disclaimer

> This reference is for **educational purposes only**.
> Always practice in a **legal environment** you own or have explicit permission to test.
> Platforms: [TryHackMe](https://tryhackme.com) · [HackTheBox](https://hackthebox.com) · [OverTheWire](https://overthewire.org)

---

## Intended audience

- Beginners learning Linux for cybersecurity
- CTF players who want a fast offline reference
- Pentesters doing recon and enumeration
- Security students preparing for OSCP / CEH / eJPT
- Anyone who keeps googling the same commands

---

## Related documentation

- [Developer tools and guides — repository overview](../../README.md)
- [Python port scanner](https://github.com/gcfernando/python-projects-and-examples/blob/main/Port%20Scanner/readme.md)
- [Git, Docker, and Podman command cheat sheets](https://github.com/gcfernando/developer-guides-and-tools)

---

<!-- Preserve links to earlier README sections. -->
<a id="-browser-behavior"></a>
<a id="-development-and-verification"></a>
<a id="-disclaimer"></a>
<a id="-features-and-categories"></a>
<a id="-intended-audience"></a>
<a id="-prerequisites"></a>
<a id="-project-structure"></a>
<a id="-quick-start"></a>
<a id="-read-only-practice-examples"></a>
<a id="-related-documentation"></a>
<a id="-troubleshooting-and-limitations"></a>
