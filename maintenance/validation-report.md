# Consolidation validation — 28 October 2026

## Scope and preservation

The merged library is at C:/Gehan/Projects/a/developer-guides-and-tools. The supplied KnowledgeBase and Other_Projects folders were not modified.

The 51 retained original files have source checksums and explicit destinations/dispositions in [source-map.csv](migration/source-map.csv). This dated report describes the initial consolidation; it is not a current verification run.

Imported byte-exact snapshots have Git attributes that preserve their original line endings on Windows and Linux. Personal Copilot application state is excluded from reusable examples and remains in the untouched original folder.

## Completed checks

| Check | Observed result |
|---|---|
| Source inventory and SHA-256 verification | Original source checksums and destination presence checked at consolidation |
| Source document links | 453 relative links resolved across 49 Markdown/HTML documents and applications |
| Generated catalog | 25 registered resources and 37 explicit page routes |
| Existing Linux checks | Passed generated-table freshness, 361 commands, 16 categories, literal search and markup escaping checks |
| Node integrity tests | Six tests passed: catalog/routes, add-ons content, Atlas targets/progress, JavaScript/JSON syntax, Compose inputs/bindings, configuration parsing |
| Jekyll production build | Successful; custom source-link handling included |
| Built website | 40 HTML pages and 724 internal links passed metadata, destination, fragment-anchor and exclusion checks |
| Browser review | Homepage rendered; navigation worked; searching the generated add-ons reader for SonarQube returned one add-on |

## External references

Checked 679 distinct authored external URLs: 676 were reachable and three GNU manual references timed out. The timeouts also occurred through a separate web reader. They remain unresolved availability checks, not confirmed missing pages.

Font preconnect/DNS-prefetch origins are connection hints and are excluded from the content-link audit. Planned destination repository/site URLs are validated against local source and the built site rather than treated as deployed pages.

The full URL list, source documents, HTTP results and limitations are recorded in [external-links.json](migration/external-links.json).

## Limits and publication state

This verification did not run every code example, perform Windows maintenance, provision cloud resources, start containers or verify third-party stream playback. External HTTP success does not validate page content, fragments or installation instructions.

Jekyll's inherited Primer theme emits Sass deprecation warnings; the production build completed successfully. The isolated Ruby and dependency setup is under ignored local runtime/vendor folders.

GitHub Pages Source was changed to GitHub Actions by the user. A read-only repository check found only README.md published at that time; the locally merged files and custom workflow had not been uploaded. No repository settings, push, publication or deletion was performed by this merge operation. Old-host redirects and the licensing decision remain separate owner actions.

## Reproduce

~~~sh
npm ci
npm run build
npm test
node scripts/verify-migration.cjs --sources ../
bundle install
bundle exec jekyll build
npm run check:site
~~~

The source-folder audit requires the original two sibling folders. Other checks operate from the merged repository alone.
