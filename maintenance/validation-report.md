# Consolidation validation — 28 October 2026

## Scope and preservation

The merged library is at C:/Gehan/Projects/a/developer-guides-and-tools. The supplied KnowledgeBase, Other_Projects and MLHandbook folders were not modified.

All 176 original files have source checksums and explicit destinations/dispositions in [source-map.csv](migration/source-map.csv). All 125 MLHandbook originals are byte-identical in examples/machine-learning/ml-handbook/. Additional setup documents and requirements files are new additions.

Imported byte-exact snapshots have Git attributes that preserve their original line endings on Windows and Linux. Personal Copilot application state is excluded from reusable examples and remains in the untouched original folder.

## Completed checks

| Check | Observed result |
|---|---|
| Source inventory and SHA-256 verification | All 176 original files unchanged; all destinations present |
| MLHandbook copy | All 125 supplied files copied byte for byte |
| Source document links | 453 relative links resolved across 49 Markdown/HTML documents and applications |
| Generated catalog | 25 registered resources and 37 explicit page routes |
| Existing Linux checks | Passed generated-table freshness, 361 commands, 16 categories, literal search and markup escaping checks |
| Node integrity tests | Six tests passed: catalog/routes, add-ons content, Atlas targets/progress, JavaScript/JSON syntax, Compose inputs/bindings, configuration parsing |
| Jekyll production build | Successful; custom source-link handling included |
| Built website | 40 HTML pages and 724 internal links passed metadata, destination, fragment-anchor and exclusion checks |
| Browser review | Homepage and integrated ML handbook rendered; navigation worked; searching the generated add-ons reader for SonarQube returned one add-on |
| ML data files | All 31 CSV/JSONL/SQLite files parsed or passed SQLite integrity checks |
| ML illustrations | All 91 PNGs decoded and were reviewed in contact sheets |
| Python application | Both Python files parsed; model-service smoke workflow passed |

## Model-service smoke workflow

Executed with Python 3.12.10, pandas 2.2.3, scikit-learn 1.6.1 and joblib 1.4.2 in a temporary workspace. The graphical window was not opened.

- Trained and persisted version 1 on the supplied 2025 data.
- Predicted with the saved model and rejected an out-of-range input.
- Updated with 2026 data and saved version 2.
- Reloaded version 1 after rollback and reproduced its prediction.
- Rejected a repeated update of the same data.

The recorded run had initial held-out MAE 18,944 and R² 0.906. These are results for the supplied teaching data and environment, not real-world model guarantees. Details and data-file inventories are in [ml-validation.json](migration/ml-validation.json).

## External references

Checked 679 distinct authored external URLs: 676 were reachable and three GNU manual references timed out. The timeouts also occurred through a separate web reader. They remain unresolved availability checks, not confirmed missing pages.

Font preconnect/DNS-prefetch origins are connection hints and are excluded from the content-link audit. Planned destination repository/site URLs are validated against local source and the built site rather than treated as deployed pages.

The full URL list, source documents, HTTP results and limitations are recorded in [external-links.json](migration/external-links.json).

## Limits and publication state

This verification did not run every notebook/code example, launch the Tkinter graphical interface, perform Windows maintenance, provision cloud resources, start containers or verify third-party stream playback. External HTTP success does not validate page content, fragments or installation instructions.

Jekyll's inherited Primer theme emits Sass deprecation warnings; the production build completed successfully. The isolated Ruby and dependency setup is under ignored local runtime/vendor folders.

GitHub Pages Source was changed to GitHub Actions by the user. A read-only repository check found only README.md published at that time; the locally merged files and custom workflow had not been uploaded. No repository settings, push, publication or deletion was performed by this merge operation. Old-host redirects and the licensing decision remain separate owner actions.

## Reproduce

~~~sh
npm ci
npm run build
npm test
node scripts/verify-migration.cjs --sources ../
python scripts/validate-ml-handbook.py --smoke
bundle install
bundle exec jekyll build
npm run check:site
~~~

The source-folder audit requires the original three sibling folders. Other checks operate from the merged repository alone. CI installs the Python model dependencies before its smoke check.
