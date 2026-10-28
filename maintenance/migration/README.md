# Consolidation record

This repository was assembled locally on 28 October 2026 from sibling folders KnowledgeBase and Other_Projects. The original folders remain intact. No .git directories were present, so there was no local commit history to import.

The later MLHandbook import adds 125 byte-identical files at examples/machine-learning/ml-handbook/. A published handbook page is generated from that preserved source.

## Every original file is accounted for

- source-map.csv records all 176 original files from the three supplied folders, original SHA-256 digests, sizes, destinations and dispositions.
- legacy/ retains the original repository READMEs, documentation indexes, Jekyll configurations, AI add-ons HTML and Linux workflow.
- Identical layouts, CSS and favicon assets were deduplicated.
- Personal Copilot application state is excluded, with its checksum recorded and its role replaced by configuration guidance.

Run node scripts/verify-migration.cjs --sources ../ to verify source coverage, unchanged original checksums and destination presence. This check is optional outside this local workspace.

## Intentional consolidation changes

Local and cross-repository links and published metadata were updated. Long-form course content and the utility implementations were retained.

The AI add-ons browser reader is generated from the Markdown guide, including the newer SonarQube registration clarification. Its original HTML is preserved in legacy/ for comparison. The current local Atlas has 14 role paths; its application, storage keys and backup behavior were retained.

The Compose example now reads passwords from environment variables and binds published ports to loopback. Its README explains .env setup. Imported image tags were retained and were not deployment-tested.

No reuse license was supplied. LICENSE records the pending owner decision without granting new permissions.

## Publication still needs an owner action

The planned destination is gcfernando/developer-guides-and-tools. This local merge did not create, rename, push, archive or delete any GitHub repository and did not deploy either old or new website.

Use url-map.csv to prepare redirects at each original hosting location. Old repository names, raw file links, fragment links and GitHub Pages URLs need separate consideration. Source layout changes do not automatically preserve old URLs.

The destination site's baseurl is /developer-guides-and-tools. Update it and the application canonical URLs if a different final name or custom domain is chosen.

Before moving the Atlas to another browser storage context, export a JSON progress backup and restore it in the new context.

## Import helper

import-sources.py is the one-time provenance/import helper. It refuses to rerun after source-map.csv exists; normal maintenance does not use it. page-routes.json records the initial imported routes; the complete public route map is generated in _data/routes.json by scripts/build-catalog.cjs.
