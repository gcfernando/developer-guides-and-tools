/* Additional final-reader behavior checks. Developer tooling; never loaded by index.html.
 * Run explicitly: node tools/browser_extra.cjs [--page index.html] [--output report.json]
 * Uses the isolated Playwright installation in the repository's .runtime directory.
 */
'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const crypto = require('node:crypto');
const http = require('node:http');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(ROOT, '../..');
const {chromium} = require(path.join(REPO, '.runtime/atlas-tools/node_modules/playwright'));
const argv = process.argv.slice(2);
const arg = (key, fallback) => argv.includes(key) ? argv[argv.indexOf(key) + 1] : fallback;
const target = path.resolve(arg('--page', path.join(ROOT, 'index.html')));
const output = path.resolve(arg('--output', path.join(REPO, '.runtime/atlas-browser-extra.json')));
const edge = arg('--browser', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe');
const artifacts = output.replace(/\.json$/i, '') + '-artifacts';
const baseline = JSON.parse(fs.readFileSync(path.join(__dirname, 'baseline.json'), 'utf8'));
const initialHash=crypto.createHash('sha256').update(fs.readFileSync(target)).digest('hex');
const result = {
  page_sha256:initialHash, target,
  checks: [],
  errors: [],
  unverified: [
    'No actual screen reader or speech output was available. Keyboard, live-region attributes, and accessibility-tree observations do not constitute an actual screen-reader sanity check.',
    'The generated two-page print PDFs are execution artifacts. This script checks PDF output and disclosure state, not human visual review of every printed page.',
    'Tap-target and focus checks cover the rendered reader states named in each result; they do not establish behavior in every browser or assistive technology.'
  ]
};

async function check(name, work) {
  if (arg('--stage', 'final') === 'ws11' && name.includes('keyboard Copy original subtopics')) {
    result.checks.push({name, pass:null, deferred:'Topic-number copy output is scheduled for WS12; final mode requires this assertion.'});
    return;
  }
  try {
    const details = await work();
    result.checks.push({name, pass: true, details});
  } catch (error) {
    result.checks.push({name, pass: false, error: error.message});
  }
}

function same(actual, expected, message) {
  assert.deepEqual(actual, expected, message);
}

async function ready(page, url) {
  page.setDefaultTimeout(8000);
  page.setDefaultNavigationTimeout(15000);
  await page.goto(url, {waitUntil: 'load'});
  await page.waitForFunction(() => !!window.AtlasExperience && !!document.getElementById('library-level'));
}

function watch(page, name) {
  page.on('pageerror', error => result.errors.push(`${name}: ${error.message}`));
  page.on('dialog', dialog => dialog.accept());
}

async function chooseRole(page, role = 'backend-software-engineer') {
  await page.locator('#role-home').selectOption(role);
  await page.waitForFunction(role => document.getElementById('role-filter').value === role && !document.getElementById('next-step-bar').hidden, role);
}

async function visibleTopicNumbers(page) {
  return page.locator('.topic-card').evaluateAll(cards => cards.filter(card => !card.hidden && getComputedStyle(card).display !== 'none')
    .map(card => Number(card.querySelector('[data-complete-topic]').dataset.completeTopic)));
}

async function liveCount(page) {
  return page.locator('#library-status').evaluate(node => ({
    text: node.textContent,
    count: Number(node.textContent.match(/^(\d+) of/)?.[1]),
    live: node.getAttribute('aria-live'),
    role: node.getAttribute('role')
  }));
}

async function assertCount(page) {
  const state = await liveCount(page);
  const visible = await visibleTopicNumbers(page);
  same(state.count, visible.length, 'The announced library result count differs from the shown topic count.');
  same(state.live, 'polite');
  same(state.role, 'status');
  return {...state, visible};
}

async function openHash(page, hash) {
  await page.evaluate(hash => {location.hash = hash;}, hash);
  await page.waitForFunction(hash => {
    const target = document.getElementById(hash.replace(/^#/, ''));
    return !!target && target.getClientRects().length > 0;
  }, hash);
  await page.locator(hash).evaluate(node => {
    const destination = node.tagName === 'DETAILS' ? node.querySelector(':scope > summary') : node;
    destination.scrollIntoView({block: 'start', behavior: 'instant'});
  });
  await page.waitForTimeout(150);
}

async function focusGeometry(page, selector) {
  const locator = page.locator(selector).first();
  await page.keyboard.press('Tab');
  await locator.focus();
  await page.waitForTimeout(150);
  return locator.evaluate(node => {
    const rect = node.getBoundingClientRect();
    const intersection = other => {
      if (!other || other.contains(node) || getComputedStyle(other).display === 'none') return 0;
      const box = other.getBoundingClientRect();
      return Math.max(0, Math.min(box.right, rect.right) - Math.max(box.left, rect.left)) *
        Math.max(0, Math.min(box.bottom, rect.bottom) - Math.max(box.top, rect.top));
    };
    const center = {x: rect.x + rect.width / 2, y: rect.y + rect.height / 2};
    const hit = document.elementFromPoint(center.x, center.y);
    return {
      selector: node.id || node.className || node.tagName,
      focused: document.activeElement === node,
      rect: {x: rect.x, y: rect.y, width: rect.width, height: rect.height, bottom: rect.bottom, right: rect.right},
      viewport: {width: innerWidth, height: innerHeight},
      topbarOverlap: intersection(document.querySelector('.topbar')),
      nextBarOverlap: intersection(document.getElementById('next-step-bar')),
      centerReceivesPointer: !!hit && (node === hit || node.contains(hit)),
      hit: hit?.id || hit?.className || hit?.tagName
    };
  });
}

async function inspectWidths(page, protocol) {
  for (const width of [360, 768, 1280, 1600]) {
    await check(`${protocol}: ${width}px expanded code and selected-role overflow`, async () => {
      await page.setViewportSize({width, height: 900});
      await chooseRole(page);
      await openHash(page, '#unit-07-01');
      const dimensions = await page.evaluate(() => {
        const code = Array.from(document.querySelectorAll('.topic-card pre')).filter(node => node.getClientRects().length)
          .map(node => ({clientWidth: node.clientWidth, scrollWidth: node.scrollWidth, documentRight: node.getBoundingClientRect().right}));
        return {width: innerWidth, scrollWidth: document.documentElement.scrollWidth, code, nextStepVisible: !document.getElementById('next-step-bar').hidden};
      });
      same(dimensions.scrollWidth, dimensions.width, 'Expanded topic/code introduced horizontal page overflow.');
      assert(dimensions.code.length > 0, 'No expanded code block was measured.');
      assert(dimensions.nextStepVisible, 'The next-step bar was not exercised.');
      await page.screenshot({path: path.join(artifacts, `${protocol}-${width}-expanded.png`), fullPage: false});
      return dimensions;
    });

    await check(`${protocol}: ${width}px rendered buttons, toggles, and checkbox-label targets are 44px`, async () => {
      const targets = await page.evaluate(() => {
        const candidates = new Set(document.querySelectorAll('button, summary, .upload-label'));
        const missingLabels = [];
        for (const input of document.querySelectorAll('input[type="checkbox"]')) {
          if (!input.getClientRects().length || input.closest('[hidden], [aria-hidden="true"], [inert]')) continue;
          const label = input.closest('label') || input.labels?.[0];
          if (label) candidates.add(label);
          else missingLabels.push(input.id);
        }
        const measured = [];
        for (const node of candidates) {
          if (node.closest('[hidden], [aria-hidden="true"], [inert]') || !node.getClientRects().length) continue;
          const rect = node.getBoundingClientRect();
          const style = getComputedStyle(node);
          if (!rect.width || !rect.height || style.visibility === 'hidden' || style.display === 'none') continue;
          measured.push({id: node.id, tag: node.tagName, text: node.textContent.trim().slice(0, 100), width: rect.width, height: rect.height});
        }
        return {measured: measured.length, missingLabels, undersized: measured.filter(item => item.width < 43.99 || item.height < 43.99)};
      });
      same(targets.missingLabels, [], 'A rendered checkbox has no associated label.');
      same(targets.undersized, [], 'Some rendered interaction targets are smaller than 44 × 44 CSS px.');
      assert(targets.measured > 10, 'Too few interaction targets were exercised.');
      return targets;
    });

    await check(`${protocol}: ${width}px sticky next-step bar does not obscure focused controls`, async () => {
      const geometry = [];
      for (const selector of ['#theme-btn', '[data-complete-topic="07"]', '#unit-07-01-practice', '.up']) {
        const state = await focusGeometry(page, selector);
        geometry.push(state);
        assert(state.focused, `Focus did not reach ${selector}.`);
        assert(state.rect.y >= -1 && state.rect.bottom <= state.viewport.height + 1, `${selector} is focused outside the viewport: ${JSON.stringify(state)}`);
        assert(state.topbarOverlap < 1 && state.nextBarOverlap < 1, `${selector} is covered by a sticky bar: ${JSON.stringify(state)}`);
        assert(state.centerReceivesPointer, `${selector} is covered at its center: ${JSON.stringify(state)}`);
      }
      return geometry;
    });
  }
}

async function inspectMatrix(page, protocol) {
  await check(`${protocol}: 360px relevance table scrolls inside its labeled wrapper`, async () => {
    await page.setViewportSize({width:360,height:900});
    await openHash(page, '#relevance');
    const wrapper=page.locator('#relevance .tablewrap');
    await wrapper.focus();
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(200);
    const observed=await wrapper.evaluate(node=>({clientWidth:node.clientWidth,scrollWidth:node.scrollWidth,scrollLeft:node.scrollLeft,tabIndex:node.tabIndex,pageWidth:document.documentElement.scrollWidth,viewport:innerWidth,hint:getComputedStyle(document.getElementById('matrix-scroll-hint')).display}));
    assert(observed.scrollWidth>observed.clientWidth);
    assert(observed.scrollLeft>0);
    same(observed.tabIndex,0);
    same(observed.pageWidth,observed.viewport);
    assert(observed.hint!=='none');
    return observed;
  });
}

async function inspectFilters(page, protocol) {
  const role = 'backend-software-engineer';
  await page.setViewportSize({width: 1280, height: 900});
  await chooseRole(page, role);
  const priorities = await page.evaluate(role => JSON.parse(document.getElementById('atlas-data').textContent).priorities[role], role);
  const core = Object.entries(priorities).filter(([, value]) => ['Essential', 'Recommended'].includes(value)).map(([number]) => Number(number)).sort((a, b) => a - b);

  await check(`${protocol}: My path default and All topics preserve original topic order`, async () => {
    await page.getByRole('button', {name: 'Reset library filters', exact: true}).click();
    same(await visibleTopicNumbers(page), core, 'The default library is not exactly the selected role’s Essential and Recommended topics.');
    await page.locator('#library-all-topics').check();
    same(await visibleTopicNumbers(page), Array.from({length: 51}, (_, i) => i + 1));
    await page.locator('#library-all-topics').uncheck();
    same(await visibleTopicNumbers(page), core);
    return assertCount(page);
  });

  await check(`${protocol}: level filter narrows the library and announces the actual result count`, async () => {
    await page.getByRole('button', {name: 'Reset library filters', exact: true}).click();
    await page.locator('#library-level').selectOption('level-1');
    same(await visibleTopicNumbers(page), core.filter(number => number <= 5));
    const state = await assertCount(page);
    await page.locator('#library-level').selectOption('');
    return state;
  });

  await check(`${protocol}: role-priority filter reveals a requested deferred priority`, async () => {
    await page.getByRole('button', {name: 'Reset library filters', exact: true}).click();
    const priority = ['Advanced', 'Optional', 'Not required now'].find(value => Object.values(priorities).includes(value));
    assert(priority, 'The selected role provides no deferred-priority fixture.');
    await page.locator('#library-priority').selectOption(priority);
    same(await visibleTopicNumbers(page), Object.entries(priorities).filter(([, value]) => value === priority).map(([number]) => Number(number)).sort((a, b) => a - b));
    const state = await assertCount(page);
    await page.locator('#library-priority').selectOption('');
    return {priority, ...state};
  });

  await check(`${protocol}: difficulty filter matches the displayed difficulty labels`, async () => {
    await page.getByRole('button', {name: 'Reset library filters', exact: true}).click();
    await page.locator('#library-difficulty').selectOption('Intermediate');
    const shown = await page.locator('.topic-card').evaluateAll(cards => cards.filter(card => !card.hidden).map(card => ({
      id: card.id, meta: card.querySelector('.topic-meta').textContent
    })));
    assert(shown.length > 0, 'The difficulty filter returned no test examples.');
    assert(shown.every(card => card.meta.includes('Intermediate')), `Wrong difficulty shown: ${JSON.stringify(shown)}`);
    const state = await assertCount(page);
    await page.locator('#library-difficulty').selectOption('');
    return state;
  });

  await check(`${protocol}: completion filter distinguishes topic scope from unit checks`, async () => {
    await page.getByRole('button', {name: 'Reset library filters', exact: true}).click();
    const topic = page.locator('[data-complete-topic="03"]');
    if (!(await page.locator('#complete-topic-03').isChecked())) await topic.click();
    await page.locator('#library-completion').selectOption('complete');
    const actual = await visibleTopicNumbers(page);
    const expected = await page.locator('.topic-check-grid .save-check').evaluateAll((inputs, core) => inputs.filter(input => input.checked && core.includes(Number(input.id.slice(-2)))).map(input => Number(input.id.slice(-2))), core);
    same(actual, expected);
    assert(actual.includes(3));
    const state = await assertCount(page);
    await page.locator('#library-completion').selectOption('');
    return state;
  });

  await check(`${protocol}: primary and matrix role controls synchronize visibly`, async () => {
    await openHash(page, '#relevance');
    const second = 'ai-and-machine-learning-engineer';
    await page.locator('#role-filter').selectOption(second);
    await page.waitForFunction(value => document.getElementById('role-home').value === value, second);
    same(await page.locator('#role-home').inputValue(), second);
    const label = await page.locator('label[for="role-filter"]').textContent();
    assert(label.includes('Showing priorities for:') && label.includes('AI and Machine Learning Engineer') && label.includes('(change)'), label);
    const expected = await page.evaluate(role => JSON.parse(document.getElementById('atlas-data').textContent).priorities[role]['7'], second);
    const actual = await page.locator('tr[data-topic="7"] .matrix-priority').textContent();
    assert(actual.includes(expected), `${actual} does not contain ${expected}`);
    return {primary: await page.locator('#role-home').inputValue(), matrix: await page.locator('#role-filter').inputValue(), label, topic07: actual};
  });
}

async function inspectOnboarding(page, url, protocol) {
  await check(`${protocol}: onboarding choices are keyboard accessible and persist`, async () => {
    await page.evaluate(() => localStorage.removeItem('ai-atlas-onboarding-v1'));
    await ready(page, url);
    assert(await page.locator('#atlas-onboarding').isVisible());
    same(await page.locator('#atlas-onboarding [data-start-choice]').count(), 3);
    const choice = page.locator('#atlas-onboarding [data-start-choice="beginner"]');
    await choice.focus();
    await page.keyboard.press('Enter');
    same(await page.evaluate(() => location.hash), '#beginner-workshop');
    same(await page.evaluate(() => localStorage.getItem('ai-atlas-onboarding-v1')), 'beginner');
    await page.reload({waitUntil: 'load'});
    assert(await page.locator('#atlas-onboarding').isHidden());
    assert(await page.locator('#role-home').isEnabled());
    await page.evaluate(() => localStorage.removeItem('ai-atlas-onboarding-v1'));
    await ready(page, url);
    await page.locator('#dismiss-onboarding').focus();
    await page.keyboard.press('Enter');
    assert(await page.locator('#atlas-onboarding').isHidden());
    same(await page.evaluate(() => localStorage.getItem('ai-atlas-onboarding-v1')), 'dismissed');
    const focused = await page.evaluate(() => document.activeElement.tagName);
    same(focused, 'H1');
    await page.reload({waitUntil: 'load'});
    assert(await page.locator('#atlas-onboarding').isHidden());
    return {threeChoices: true, choice: 'beginner', dismissedFocus: focused, persistedAfterReload: true};
  });
}

async function inspectScrollTracking(page, protocol) {
  await check(`${protocol}: sidebar tracks the section actually in view`, async () => {
    await page.setViewportSize({width: 1280, height: 900});
    const observations = [];
    for (const id of ['entry-check', 'glossary', 'assessment-guide']) {
      await openHash(page, '#' + id);
      await page.evaluate(id => {
        const node = document.getElementById(id);
        scrollTo({top: scrollY + node.getBoundingClientRect().top - innerHeight * 0.2, behavior: 'instant'});
      }, id);
      await page.waitForFunction(id => document.querySelector('#sidebar .navlink[aria-current="location"]')?.getAttribute('href') === '#' + id, id, {timeout: 3000});
      const current = await page.locator('#sidebar .navlink[aria-current="location"]').evaluateAll(nodes => nodes.map(node => node.getAttribute('href')));
      same(current, ['#' + id]);
      observations.push({section: id, current});
    }
    return observations;
  });
}

async function inspectCopy(page, protocol) {
  await check(`${protocol}: keyboard Copy original subtopics includes topic number and every exact subtopic`, async () => {
    await openHash(page, '#unit-03-01');
    const button = page.locator('.topic-card[id^="topic-03-"] [data-copy-topic]');
    await button.focus();
    await page.keyboard.press('Enter');
    await page.waitForFunction(() => typeof window.__atlasCopiedText === 'string');
    const copied = await page.evaluate(() => window.__atlasCopiedText);
    assert(/\b03\b/.test(copied.split('\n')[0]), 'The copied topic heading omits topic number 03.');
    assert(copied.split('\n')[0].includes('Python Programming'));
    const expected = baseline.subtopics.filter(sub => sub.id.startsWith('subtopic-03-')).map(sub => sub.text);
    const lines = copied.split('\n').filter(line => /^\d+\. /.test(line)).map(line => line.replace(/^\d+\. /, ''));
    same(lines, expected, 'Copied original subtopic text or order differs from the baseline.');
    same(await button.evaluate(node => document.activeElement === node), true);
    return {heading: copied.split('\n')[0], subtopics: lines.length, clipboard: 'mocked writeText or legacy-copy boundary; no system clipboard read'};
  });
}

async function inspectDownloads(page, protocol) {
  await check(`${protocol}: every workshop Blob download exactly matches its inline text and filename`, async () => {
    await openHash(page, '#beginner-workshop');
    await page.locator('#lesson-focus').selectOption('');
    const buttons = page.locator('#beginner-workshop [data-download][data-code]');
    const count = await buttons.count();
    assert(count > 0, 'No embedded workshop downloads were exercised.');
    const files = [];
    for (let i = 0; i < count; i++) {
      const button = buttons.nth(i);
      const reference = await button.evaluate(node => {
        for (let parent = node.parentElement; parent; parent = parent.parentElement) if (parent.tagName === 'DETAILS') parent.open = true;
        return {filename: node.dataset.download, text: document.getElementById(node.dataset.code).textContent};
      });
      const pending = page.waitForEvent('download', {timeout: 8000});
      await button.focus();
      await page.keyboard.press('Enter');
      const downloaded = await pending;
      same(downloaded.suggestedFilename(), reference.filename);
      const actual = fs.readFileSync(await downloaded.path());
      same(actual, Buffer.from(reference.text, 'utf8'), `Inline/download bytes differ for ${reference.filename}.`);
      files.push({filename: reference.filename, bytes: actual.length});
    }
    return {downloads: count, files};
  });
}

async function inspectPrint(page, protocol) {
  await check(`${protocol}: actual PDF pages 1–2 hydrate content and restore disclosure states`, async () => {
    await page.evaluate(() => {
      window.__extraDetailsBefore = Array.from(document.querySelectorAll('details')).map(node => ({node, open: node.open}));
      window.__extraPrintEvents = [];
      window.addEventListener('beforeprint', () => window.__extraPrintEvents.push({
        event: 'beforeprint',
        remainingTopicTemplates: document.querySelectorAll('template[data-topic-body]').length,
        remainingPathTemplates: document.querySelectorAll('template[data-path-body]').length,
        closedMainDetails: Array.from(document.querySelectorAll('main details')).filter(node => !node.open).length
      }));
      window.addEventListener('afterprint', () => window.__extraPrintEvents.push({event: 'afterprint'}));
    });
    const pdfPath = path.join(artifacts, `${protocol}-print-pages-1-2.pdf`);
    const pdf = await page.pdf({path: pdfPath, pageRanges: '1-2', format: 'A4', printBackground: true});
    same(pdf.subarray(0, 5).toString('ascii'), '%PDF-');
    const pageObjects = (pdf.toString('latin1').match(/\/Type\s*\/Page\b/g) || []).length;
    same(pageObjects, 2, 'The requested print artifact does not contain two PDF page objects.');
    await page.waitForTimeout(150);
    const state = await page.evaluate(() => ({
      events: window.__extraPrintEvents,
      changedExistingDetails: window.__extraDetailsBefore.filter(({node, open}) => node.open !== open).map(({node, open}) => ({id: node.id, summary: node.querySelector('summary')?.textContent, before: open, after: node.open})),
      answerKeysLeftOpen: Array.from(document.querySelectorAll('.answer-key')).filter(node => node.open && !window.__extraDetailsBefore.some(before => before.node === node && before.open)).length
    }));
    const before = state.events.find(event => event.event === 'beforeprint');
    assert(before && state.events.some(event => event.event === 'afterprint'), `Real print events were not both observed: ${JSON.stringify(state.events)}`);
    same(before.remainingTopicTemplates, 0);
    same(before.remainingPathTemplates, 0);
    same(before.closedMainDetails, 0);
    same(state.changedExistingDetails, [], 'Printing left existing disclosures in a different state.');
    same(state.answerKeysLeftOpen, 0, 'Printing left newly hydrated answer keys expanded.');
    return {pdfPath, bytes: pdf.length, pageObjects, ...state};
  });
}

async function inspectDeepLinks(browser, url, protocol) {
  for (const width of [360, 1280]) {
    for (const hash of ['#unit-03-01', '#subtopic-51-020']) {
      await check(`${protocol}: initial ${hash} at ${width}px lands in the unobscured viewport`, async () => {
        const context = await browser.newContext({viewport: {width, height: 900}});
        try {
          const page = await context.newPage();
          watch(page, `${protocol} deep-link ${hash}`);
          await ready(page, url + hash);
          await page.waitForFunction(hash => {
            let target = document.getElementById(hash.slice(1));
            if (!target) return false;
            if (target.tagName === 'DETAILS') target = target.querySelector(':scope > summary');
            const rect = target.getBoundingClientRect();
            const top = document.querySelector('.topbar').getBoundingClientRect().bottom;
            const next = document.getElementById('next-step-bar');
            const bottom = next && !next.hidden && getComputedStyle(next).position === 'fixed' ? next.getBoundingClientRect().top : innerHeight;
            return rect.height > 0 && rect.top >= top - 1 && rect.bottom <= bottom + 1;
          }, hash, {timeout: 5000});
          const position = await page.evaluate(hash => {
            const node = document.getElementById(hash.slice(1));
            const target = node.tagName === 'DETAILS' ? node.querySelector(':scope > summary') : node;
            const rect = target.getBoundingClientRect();
            return {hash: location.hash, y: rect.y, bottom: rect.bottom, height: innerHeight, visible: !!node.getClientRects().length, templateRemainingForTopic: !!node.closest('.topic-card')?.querySelector('template[data-topic-body]')};
          }, hash);
          same(position.hash, hash);
          same(position.templateRemainingForTopic, false);
          await page.screenshot({path: path.join(artifacts, `${protocol}-${width}-${hash.slice(1)}.png`), fullPage: false});
          return position;
        } finally { await context.close(); }
      });
    }
  }
}

async function inspectThemes(browser, url, protocol) {
  await check(`${protocol}: OS dark default, live OS changes, saved override, and theme-color track the theme`, async () => {
    const context = await browser.newContext({viewport: {width: 1280, height: 900}, colorScheme: 'dark'});
    try {
      const page = await context.newPage();
      watch(page, `${protocol} themes`);
      await ready(page, url);
      const themeState = () => page.evaluate(() => ({
        theme: document.documentElement.dataset.theme,
        meta: document.querySelector('meta[name="theme-color"]')?.content,
        saved: localStorage.getItem('ai-atlas-theme'),
        validMeta: CSS.supports('color', document.querySelector('meta[name="theme-color"]')?.content || '')
      }));
      const dark = await themeState();
      same(dark.theme, 'dark', 'No saved preference should follow the OS dark theme.');
      same(dark.saved, null, 'Following the OS must not silently save a manual override.');
      assert(dark.meta && dark.validMeta, 'Dark theme-color metadata is missing or malformed.');
      await page.emulateMedia({colorScheme: 'light'});
      await page.waitForFunction(() => document.documentElement.dataset.theme === 'light', null, {timeout: 3000});
      const light = await themeState();
      same(light.saved, null);
      assert(light.meta && light.validMeta && light.meta !== dark.meta, 'theme-color did not change with the theme.');
      await page.emulateMedia({colorScheme: 'dark'});
      await page.waitForFunction(() => document.documentElement.dataset.theme === 'dark', null, {timeout: 3000});
      await page.locator('#theme-btn').focus();
      await page.keyboard.press('Enter');
      const manual = await themeState();
      same(manual.theme, 'light');
      same(manual.saved, 'light');
      same(manual.meta, light.meta);
      await page.emulateMedia({colorScheme: 'light'});
      await page.emulateMedia({colorScheme: 'dark'});
      same((await themeState()).theme, 'light', 'A saved manual preference must override later OS changes.');
      await page.reload({waitUntil: 'load'});
      const reloaded = await themeState();
      same(reloaded.theme, 'light');
      same(reloaded.meta, light.meta);
      return {dark, light, manual, reloaded};
    } finally { await context.close(); }
  });
}

async function inspectReviewFixes(page, url, protocol) {
  await check(`${protocol}: workshop reading view resumes after reload`, async () => {
    await page.locator('#lesson-focus').selectOption('lesson-function');
    await page.reload({waitUntil:'load'});
    same(await page.locator('#lesson-focus').inputValue(),'lesson-function');
    assert(await page.locator('#lesson-function').isVisible());
    return {resumed:'lesson-function'};
  });
  await check(`${protocol}: unit progress appears in the persistent next step`, async () => {
    await chooseRole(page);
    await openHash(page,'#unit-01-01');
    await page.locator('#unit-01-01-practice').check();
    await page.waitForFunction(()=>/unit checks 1\//.test(document.getElementById('next-step-summary').textContent));
    return {summary:await page.locator('#next-step-summary').textContent()};
  });
  await check(`${protocol}: dismissing next step preserves visible keyboard focus`, async () => {
    await page.setViewportSize({width:360,height:900});
    await openHash(page,'#unit-07-01');
    const dismiss=page.locator('#next-step-bar button');
    await dismiss.focus();await page.keyboard.press('Enter');
    assert(await page.locator('#next-step-bar').isHidden());
    const state=await page.evaluate(()=>{const n=document.activeElement,r=n.getBoundingClientRect();return {tag:n.tagName,id:n.id,top:r.top,bottom:r.bottom,height:innerHeight};});
    assert(state.top>=0&&state.top<state.height&&state.bottom>0,JSON.stringify(state));
    assert(state.tag!=='BODY');return state;
  });
}

async function inspectProtocol(browser, url, protocol) {
  const context = await browser.newContext({viewport: {width: 1280, height: 900}, acceptDownloads: true, colorScheme: 'light'});
  try {
    const page = await context.newPage();
    watch(page, protocol);
    await page.addInitScript(() => {
      Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async text => {window.__atlasCopiedText = text;}}});
      document.execCommand = command => {
        if (command !== 'copy') return false;
        window.__atlasCopiedText = document.activeElement?.value || '';
        return true;
      };
    });
    await ready(page, url);
    await inspectWidths(page, protocol);
    await inspectFilters(page, protocol);
    await inspectOnboarding(page, url, protocol);
    await inspectScrollTracking(page, protocol);
    await inspectMatrix(page, protocol);
    await inspectCopy(page, protocol);
    await inspectDownloads(page, protocol);
    await inspectPrint(page, protocol);
    await inspectReviewFixes(page,url,protocol);
  } catch (error) {
    result.errors.push(`${protocol}: ${error.stack}`);
  } finally { await context.close(); }
  await inspectDeepLinks(browser, url, protocol);
  await inspectThemes(browser, url, protocol);
}

async function main() {
  fs.mkdirSync(artifacts, {recursive: true});
  const server = http.createServer((req, res) => {
    const requestPath = new URL(req.url, 'http://127.0.0.1').pathname;
    if (requestPath === '/favicon.ico') { res.writeHead(204); res.end(); return; }
    if (requestPath !== '/index.html' && requestPath !== '/') { res.writeHead(404); res.end(); return; }
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.end(fs.readFileSync(target));
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const httpURL = `http://127.0.0.1:${server.address().port}/index.html`;
  let browser;
  try {
    browser = await chromium.launch({executablePath: edge, headless: true});
    await inspectProtocol(browser, pathToFileURL(target).href, 'file');
    await inspectProtocol(browser, httpURL, 'http');
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
  fs.writeFileSync(output, JSON.stringify(result, null, 2));
  console.log(JSON.stringify({passed: result.checks.filter(check => check.pass).length,
    failed: result.checks.filter(check => check.pass === false), errors: result.errors, deferred:result.checks.filter(check=>check.pass===null), output, artifacts, unverified: result.unverified}, null, 2));
  process.exitCode = result.errors.length || result.checks.some(check => check.pass === false) ? 1 : 0;
}

main().catch(error => {
  result.errors.push(error.stack);
  fs.mkdirSync(path.dirname(output), {recursive: true});
  fs.writeFileSync(output, JSON.stringify(result, null, 2));
  console.error(error);
  process.exitCode = 1;
});
