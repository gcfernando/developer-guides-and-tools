# Contributing

Make focused corrections and include the resource, section, environment, relevant version, expected result and evidence. Preserve author attribution, prerequisites, example context and qualifications.

## Content and generated files

- Add the resource to _data/resources.yml and use the [style guide](maintenance/content-style-guide.md).
- Edit docs/ai/coding-addons.md for AI add-ons content; run npm run build:addons.
- Edit apps/linux-command-reference/data.js for Linux commands; run node apps/linux-command-reference/generate-static.cjs.
- The published ML handbook is generated from examples/machine-learning/ml-handbook/Data_Science_Handbook.md. Preserve the bundle layout and dataset paths.
- Preserve Atlas topic IDs, checkbox IDs and backup format. Update its guide when counts or behavior change.
- Keep runnable utility instructions beside the script.
- Keep dated upstream snapshots clearly labeled; do not describe a directory entry as a tested service.

## Validate

~~~sh
npm ci
npm run build
npm test
bundle install
bundle exec jekyll build
npm run check:site
~~~

Review changed output. Execute changed examples only in an appropriate disposable environment, and report exactly what was tested.

Do not add credentials, personal application-state files, private account identifiers or unverified licensing claims. Use placeholders and ignored .env files for local configuration.

## Pull requests

Describe the user-visible correction, relevant resource versions and actual validation. For ML changes, install the Tkinter example requirements and run python scripts/validate-ml-handbook.py --smoke. The graphical window and every notebook block require separate manual checks.

The source-folder checksum audit is a local migration check; normal contributions do not need the original sibling folders.

## Shared repository conventions

Follow [repository standards](REPOSITORY_STANDARDS.md). Run `python .github/scripts/check_repository.py` with Python 3.12 or later, alongside the content and site checks above. Keep Markdown links case-correct and preserve stable public routes, anchors and imported snapshots.
