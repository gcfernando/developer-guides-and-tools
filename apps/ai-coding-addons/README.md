# AI coding add-ons reader

This folder is a self-contained source and build for the standalone `index.html`.
The generated HTML includes CSS, JavaScript, content and compatibility data, so it
can be opened directly without a web server or network connection. Publisher
links and actual add-on installation require a network connection.

## Edit and rebuild

Use Node.js 22 or later. From `apps/ai-coding-addons`:

```sh
npm ci --ignore-scripts
npm run build
npm run check:generated
npm test
npm run test:browser
```

On Windows, use `npm.cmd` if the PowerShell wrapper is blocked by execution
policy. Do not change that policy to run this build.

- `guide.json`: 39 maintained cards, five explicit environment statuses per card,
  version/OS qualifications, source links, setup, proof of use and removal.
- `intro.md`, `closing.md`: onboarding, comparison criteria, troubleshooting,
  validation template, scope, privacy and lifecycle guidance.
- `styles.css`, `app.js`: reader presentation and behavior.
- `build.cjs`: generates the single-file HTML; `--check` detects stale output.
- `tests/`: structural and real-browser regression checks.
- `CHANGES.md`: disposition of the 40 review findings.
- `research/source-checks.json`: dated reachability checks for the publisher
  references. Some GitHub HTML pages returned transient 503 responses; the
  matching public raw file was checked as a fallback. Reachability does not
  establish that an integration runs.

`documented` means publisher/platform documentation supports the described path;
it does not mean a live integration was tested. `unverified` is explicitly
excluded from client results unless the reader opts in. `unavailable` identifies
a missing required host capability, such as a terminal without the canvas needed
by a particular app extension. Do not promote a path to tested without recording
its OS, assistant/package versions, scope and observed result.

Add-ons have not been installed or authenticated as part of this revision.
Browser tests exercise the guide, not the 39 integrations.

## Browser tests

The locked Playwright package runs an isolated, headless browser profile. On
Windows the test uses Microsoft Edge at its standard path when available. For
another installed Chromium-based browser set `GUIDE_BROWSER_PATH` to its full
executable path. Otherwise install the matching Playwright Chromium runtime:

```sh
npx playwright install chromium
npm run test:browser
```

The suite covers loopback HTTP and offline `file:` loading, compatibility,
unverified opt-in, filtering, warning visibility, sidebar/matrix synchronization,
direct and legacy fragments, malformed fragments, mocked clipboard success and
manual fallback, theme persistence, blocked storage, keyboard skip navigation,
reduced motion, text contrast and mobile overflow. It never uses a personal
browser profile or writes to the real clipboard. Reports/screenshots go to the
ignored `test-results/` directory.

## Repository-wide build integration

The [repository generator](https://github.com/gcfernando/developer-guides-and-tools/blob/main/scripts/build-ai-addons.cjs)
delegates to this folder's `build.cjs`. The maintained reader sources are
`guide.json`, `intro.md` and `closing.md`; the
[Markdown index](https://github.com/gcfernando/developer-guides-and-tools/blob/main/docs/ai/coding-addons.md)
retains the original guide fragments and links to the reader.

The root build and tests already include this integration. From the repository
root, run:

```sh
npm run build:addons
node apps/ai-coding-addons/build.cjs --check
npm test
```

The generator resolves its own installed dependencies or the compatible
dependencies already declared in the parent package. For browser tests, install
this folder's locked dev dependencies. A local reader test alone does not validate
the parent `check:generated` entry point. `repository-build-integration.patch`
is retained as a historical handoff artifact; do not reapply it to this already
integrated checkout.

Original upstream locations:

- [Markdown guide](https://github.com/gcfernando/developer-guides-and-tools/blob/main/docs/ai/coding-addons.md)
- [Generator](https://github.com/gcfernando/developer-guides-and-tools/blob/main/scripts/build-ai-addons.cjs)
