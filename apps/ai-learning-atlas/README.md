---
layout: default
permalink: /apps/ai-learning-atlas/guide/
title: "AI Learning Atlas: Offline Reader and Progress Guide"
description: Use role paths, search AI topics, record progress and export a
  backup in the standalone AI Learning Atlas.
---

# 🧠 AI Learning Atlas — Offline Reader and Progress Guide

The [AI Learning Atlas](index.html) is a standalone HTML study handbook with 51 topic groups, 1,607 subtopics and 14 suggested professional paths. It helps you choose what to study, find a topic, plan a lab and record your own progress.

## 📦 Prerequisites

Open the hosted handbook through the link above, or download the HTML file for offline use in a modern browser. No web server, Python environment, account or API key is needed to read it. JavaScript enables search, role selection, copying and progress controls. External reference links require internet access; the handbook uses no external fonts or scripts.

## 🚀 Quick start

1. Open the [published AI Learning Atlas](index.html) or your downloaded `AI-Learning-Atlas-Complete.html` in a browser.
2. Choose the profession closest to your work. Its dashboard shows Essential and Recommended topics and the next unchecked topic.
3. Open that topic, check its prerequisites and read the suggested lab and completion evidence. A role path can assume knowledge from topics outside its selected list.
4. Complete the exercise in a separate practice project. The handbook supplies study directions, not runnable implementations for every lab.
5. Mark the topic complete when you have evidence, and export a JSON backup of your progress.

The role priorities are editorial recommendations. They are not a certification syllabus or a guarantee that a particular curriculum suits every job.

## 🔎 Search and navigation

Type at least two characters into search. All query terms must appear in a result's title or context; the interface shows up to 35 results. Search covers professions, topics and individual subtopics. Selecting a result opens collapsed topic content and jumps to its target.

Press `/` outside an editable field to focus search. Down Arrow moves into results; Up/Down navigate them. The profession selector also controls the relevance matrix and progress dashboard. Essential and Recommended topics form the dashboard's core path; Advanced topics and milestones do not contribute to its percentage.

## 💾 Progress, backups and privacy

Checkmarks, the selected profession and the theme use browser local storage when available. Storage belongs to that browser context; it is not an account-based sync service. The hosted page and a downloaded local file use separate storage contexts; switching between them does not automatically transfer progress. Export a backup from the original context and restore it in the new one. Local-file storage behavior, private browsing, clearing site data or moving the file can affect persistence.

| Control | Stored or exported information |
|---|---|
| Mark done / topic checkboxes | Self-reported completion shared by the topic card and checklist |
| Copy progress summary | Text list of checked items; it does not include a full selected-role backup |
| Export progress backup | JSON with schema version, selected profession, export time and all checkbox states |
| Restore a backup | Validates the JSON structure and boolean checkbox fields, asks before replacing current checks, then restores the selected role |
| Clear progress | Asks before clearing checkmarks; it does not clear the selected profession or theme |

The import control rejects files larger than 250,000 bytes. Exported JSON does not include the theme, notes, code, screenshots or exercise evidence. Keep that evidence separately. If browser storage is unavailable, a restored session may still display progress without retaining it after closing; keep the exported file.

The reader makes no network requests to save progress. Following an external reference or pasting material into an AI assistant is a separate action governed by that service's data handling.

## 🤖 Using the tutor prompt

The workshop section contains a reusable prompt and worked examples. Copy it into an assistant you are authorized to use, fill in your role and subtopics, then perform and verify the exercises yourself. Words such as `DONE`, `DEBUG` and `PROGRESS` are suggested conversational conventions, not built-in commands implemented by this HTML file.

The handbook does not call a model, execute labs, inspect test results or award completion automatically. A checkmark records your choice; the surrounding assessment criteria describe evidence you should collect.

## 🛠️ Troubleshooting and maintenance

- **Progress disappeared:** check the browser/profile and file location, then restore your JSON backup. Do not assume local storage will migrate with a renamed or moved file.
- **Copy fails:** select and copy the displayed text manually. Browser clipboard permissions and secure-context rules vary.
- **A prerequisite is outside my path:** study the referenced topic or establish equivalent knowledge before continuing.
- **A tool's API differs:** follow the linked publisher documentation for the installed version. Topic labels and suggested stacks are a learning snapshot.

The file embeds its content, styles, two behavior scripts and a generated search index. When maintaining it, keep topic IDs, search records, role priorities and progress-checkbox IDs aligned. The current search index contains 14 profession records, 51 topic records and 1,607 subtopic records; all targets resolved during the documentation review. That structural check does not validate the educational effectiveness of every proposed lab.

## 🔗 Related documentation

[Repository overview](../../README.md) · [Documentation index](../../documentation.md) · [AI coding add-ons guide](../../docs/ai/coding-addons.md)
