# Contributing

Make focused corrections and include the resource, section, environment, relevant version, expected result and evidence. Preserve author attribution, prerequisites, example context and qualifications.

## Content and generated files

Choose a home by purpose, then subject. Use `docs/<subject>/` for guides, `apps/<name>/` for browser applications, `examples/<subject>/<name>/` for runnable demonstrations, `tools/<runtime>/<name>/` for single-runtime utilities, and `templates/<category>/<name>/` for reusable starting material. A multi-language utility can live directly in `tools/<name>/`. Shared repository automation belongs in `scripts/`, not the user-facing tools catalog.

Add a subject within an existing category before introducing a new top-level category. Avoid catch-all folders and empty directories. Keep each substantial resource's requirements, assets and relevant checks together; small resources may remain flat. Follow the [style guide](maintenance/content-style-guide.md).

| Edit this source | Generated output | Build command |
| --- | --- | --- |
| `_data/resources.yml` and page front matter | `documentation.md`, `_data/routes.json` | `npm run build:catalog` |
| `docs/ai/coding-addons.md`, `scripts/templates/ai-addons.*` | `apps/ai-coding-addons/index.html` | `npm run build:addons` |
| `apps/linux-command-reference/data.js` and generator | Embedded table in that app's `index.html` | `npm run build:linux` |
| `apps/ai-learning-atlas/source/`, `exercises/` and `build.py` | Atlas standalone `index.html` | `npm run build:atlas` |
| `examples/machine-learning/ml-handbook/Data_Science_Handbook.md` | `docs/data-science/machine-learning-handbook.md` | `npm run build:handbook` |
| `docs/databases/sql-server-and-mysql.md` | SQL part readers and their index in the adjacent `sql-server-and-mysql/` folder | `npm run build:sql` |

Do not hand-edit generated output. `npm run build` runs all generators in dependency order, with the catalog last. The SQL full-course document remains authoritative; part readers are generated views, not independently maintained copies. The ML bundle README is a separate beginner course, not the source of the generated reference handbook.

Register resources in `_data/resources.yml`. Keep one authoritative home and cross-link related guides, apps and examples instead of copying them. Add a topic or resource type only when used; tags or relationship fields should be added with a consumer and validation, not as unused metadata.

Preserve bundle-relative dataset paths, imported byte-identical files, published routes and anchors. Preserve Atlas topic IDs, checkbox IDs and backup format. Keep utility instructions beside scripts and dated upstream snapshots clearly labeled. A directory entry does not establish that a service was tested.

## Validate

~~~sh
npm ci
npm run build
npm test
npm run check:repository
bundle install
npm run site:build
npm run check:site
~~~

Node.js 22+, Python 3.12+ and the declared npm dependencies are required for the complete root build/check sequence. Ruby and Bundler are needed only for the Jekyll site. `npm test` includes generated freshness, shared integration checks, Linux checks and the Atlas runtime, content, arithmetic and embedded-exercise checks. For a focused change use `npm run check:linux` or `npm run check:atlas`; run the aggregate checks before submitting.

`npm run site:build` first builds the real Jekyll site, then prepares the lightweight hosted Atlas at its existing public URL and publishes a byte-identical `offline.html` download. The repository's standalone `apps/ai-learning-atlas/index.html` is not overwritten by hosted generation. `npm run site:serve` builds and serves that output with the configured base path; rebuild after edits, since this preview is not a watcher. Ruby/Bundler must be available on the current shell's PATH, and gem installation must use organization-approved network access.

Review changed output. Execute other changed examples only in an appropriate disposable environment, and report exactly what was tested. Root checks do not run SQL examples, start Compose services, open the Tkinter GUI or perform browser accessibility/performance audits.

`npm run check:links` checks case-sensitive source paths, Markdown and plain-text links and fragments, HTML anchors, embedded Atlas links, local assets, navigation and current-site URLs against the route map, including the historical reading copies in `maintenance/migration/legacy/`. Unrendered template URLs in `.md`, `.markdown` or `.txt` files fail the check. Original migration documents are preserved in lossless `.gz` archives; the provenance check verifies their decompressed bytes against the original checksums. Do not keep duplicate originals as `.txt` files: document libraries can index their obsolete links and HTML anchors. `npm run check:site` checks the actual Jekyll output, including rendered anchors, CSS/SVG references and sitemap destinations; source checks do not substitute for this step. Authored templates are checked through their generated output.

For a downloaded copy containing local tooling, run `npm run check:links -- --include-runtime-docs` to also check Markdown and plain-text documentation under `.runtime/`. Dependency `node_modules` folders and generated preview HTML remain outside that optional documentation scan. Locally installed dependency documentation is not repository source; reinstalling a dependency can restore its upstream links.

To check external destinations explicitly, run `node scripts/check-links.cjs --export-external artifacts/link-audit/external-input.json --report artifacts/link-audit/local-report.json`, then `python -B scripts/check-external-links.py artifacts/link-audit/external-input.json --report artifacts/link-audit/external-report.json`. Confirmed HTTP 404/410 responses fail the external check. TLS failures, authentication requirements, rate limits and transient server errors are reported as unverified, not dead links. Local-service and reserved example URLs are reported without probing them; preconnect/DNS hints are not page links. External fragment existence and the correctness of third-party content require separate review. Never disable TLS verification to make a link audit pass.

Use `--strict` when all public URLs must be verified: unresolved requests also return a nonzero exit code. If Python rejects a certificate chain accepted by your organization's operating-system trust store, the optional `--native-tls` mode uses that store through the `truststore` package (`python -m pip install truststore`). It still verifies certificates and hostnames; it does not bypass certificate checks or network access restrictions.

Atlas compatibility fixtures live in `apps/ai-learning-atlas/tests/fixtures/`. Existing `tools/results/` files are frozen historical evidence, not current test status. Write new local reports beneath ignored `artifacts/` or `.runtime/`; retain routine CI reports as workflow artifacts. Do not overwrite historical evidence to imply a new run.

### Microsoft Edge browser checks on Windows

Install the optional tooling with `npm install --prefix .runtime/atlas-tools playwright axe-core lighthouse chrome-launcher`, then run `npm run check:browser`. These checks use the installed Microsoft Edge executable, isolated temporary profiles, offline file URLs and loopback HTTP servers. They do not use personal tabs, saved browsing data or the system clipboard. No separate Chromium download is needed. Reports and screenshots are saved in `artifacts/edge-tests/`.

For visible Edge windows, run `node scripts/check-browser.cjs --headed` and `node apps/ai-learning-atlas/tools/browser_verify.cjs --headed --stage final --gzip --output artifacts/edge-tests/atlas-browser.json`. The extended suite runs headlessly in Edge for PDF printing. `npm run check:browser` also tests the hosted reader over HTTP, existing progress restoration and explicit loading-error recovery. `npm run build:atlas:hosted` stages that same hosted output in ignored `.runtime/atlas-hosted` without pretending to build Jekyll.

Check hosted performance separately, without concurrent browser tests: `npm run check:performance`. It retains the minimum mobile performance score of 90 and uses only the Edge process being measured; machine load can affect the result. Add `--trace` to a direct `browser_verify.cjs --lighthouse` invocation to save diagnostic trace events. Offline file behavior remains covered separately; the hosted reader uses same-origin, content-hashed assets and yields between section insertions instead of blocking the reader with one large startup task.

These suites exercise the three standalone HTML apps, not unbuilt Markdown pages. A fresh Jekyll build and `npm run check:site` remain necessary. Automated accessibility findings and screenshots do not replace screen-reader testing or a human visual review.

Do not add credentials, personal application-state files, private account identifiers or unverified licensing claims. Use placeholders and ignored .env files for local configuration.

For the local services example, copy `.env.example` to `.env` and supply your own values. Existing local `.env` files must not be overwritten. If updating a checkout that already tracks `.env`, remove only its index entry with `git rm --cached -- examples/containers/local-services/.env`; the ignore rule alone does not untrack it.

## Pull requests

Describe the user-visible correction, relevant resource versions and actual validation. For ML changes, install the Tkinter example requirements and run python scripts/validate-ml-handbook.py --smoke. The graphical window and every notebook block require separate manual checks.

The source-folder checksum audit is a local migration check; normal contributions do not need the original sibling folders.

## Shared repository conventions

Follow [repository standards](REPOSITORY_STANDARDS.md). Run `python .github/scripts/check_repository.py` with Python 3.12 or later, alongside the content and site checks above. Keep Markdown links case-correct and preserve stable public routes, anchors and imported snapshots.
