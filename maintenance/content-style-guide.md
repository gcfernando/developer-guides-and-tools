# Content and structure conventions

Organize written content by subject under docs/. Put browser applications in apps/, executable utilities in tools/, opt-in environments in examples/ and reusable instruction documents in templates/.

Use lowercase, hyphenated ordinary filenames. Preserve recognized filenames such as README.md, AGENTS.md and CLAUDE.md. Keep each utility's README next to its script.

## Public pages

Use front matter with a descriptive title, description and explicit trailing-slash permalink. Keep the permalink stable when reorganizing the source file. Keep links relative in Markdown so GitHub remains usable; Jekyll's relative-links plugin converts published Markdown targets.

Register discoverable resources in _data/resources.yml. npm run build:catalog derives the catalog and route data from those records and page front matter. Add no empty categories.

## Examples and evidence

State the audience, prerequisites and relevant tool version. Distinguish complete examples, fragments, intentional failures, unexecuted instructions and recorded verification. Use an actual review date only when a review occurred.

Keep database dialects and command destinations clear. Keep author attribution, source links, cleanup guidance and meaningful caveats.

## Maintenance boundaries

The AI add-ons HTML is generated from one Markdown source. The Linux table is generated from data.js. The Atlas standalone HTML is generated from its source folder and embedded exercises; preserve its topic IDs, checkbox IDs, local-storage keys and JSON backup schema. The complete source/output ownership table is in [CONTRIBUTING.md](../CONTRIBUTING.md).

Do not split the large programming courses during the initial import. A later chapter split must preserve sequence, prerequisites, code continuations, exercise solutions and incoming anchors.

SQL has generated part readers for smaller reading sessions. Edit the full-course source and regenerate them; do not maintain parallel course copies. Keep the original full-course route and anchors. An authoring split is a separate migration and must preserve the same contracts. The ML beginner course and reference handbook have different audiences and must not be deduplicated as though they were identical.

Preserve imported images and dataset bytes where provenance requires it. Optimize newly authored assets before adding them, without sacrificing legibility. Existing asset compression requires checking source-map dispositions first.

Changes to shared AI policy require reviewing each client's application notes. Configuration examples must not include account state or credentials.

## Website

Build Jekyll from the repository root. Maintenance archives, scripts, tests, dependencies and runtime artifacts are excluded. Example configuration and utility scripts may be downloaded as static assets; public companion READMEs have explicit routes.

Old-host redirects require deployment at the old hosting location. A URL map in this repository does not implement those redirects.
