/* Progressive reader enhancements. Load before reader.js; no network requests. */
(() => {
  'use strict';

  const byId = id => document.getElementById(id);
  const main = document.querySelector('main');
  const home = byId('role-home');
  const matrix = byId('role-filter');
  const library = byId('library');
  const cards = Array.from(document.querySelectorAll('.topic-card'));
  const atlas = JSON.parse(byId('atlas-data').textContent);
  const corePriorities = new Set(['Essential', 'Recommended']);
  const controls = {};
  const temporarilyRevealed = new Set();
  let role = '';
  let dismissedNextRole = null;
  let printState = null;
  let updateBarOffset = () => {};

  function element(tag, attributes = {}, text = '') {
    const node = document.createElement(tag);
    for (const [key, value] of Object.entries(attributes)) node.setAttribute(key, value);
    if (text) node.textContent = text;
    return node;
  }

  function readLocal(key) {
    try { return localStorage.getItem(key); } catch { return null; }
  }

  function saveLocal(key, value) {
    try { localStorage.setItem(key, value); } catch { /* The choice still works for this visit. */ }
  }

  function topicNumber(card) {
    return Number(card.querySelector('[data-complete-topic]')?.dataset.completeTopic ||
      card.id.match(/^topic-(\d+)/)?.[1]);
  }

  function completed(number) {
    return !!byId(`complete-topic-${String(number).padStart(2, '0')}`)?.checked;
  }

  function hydrate(card) {
    if (!card) return;
    const template = card.querySelector('template[data-topic-body]');
    if (!template) return;
    const host = card.querySelector('.topic-body-host');
    if (!host) return;
    let fragment = template.content;
    const encoded = fragment.querySelector('script[data-topic-json]');
    if (encoded) {
      const decoded = document.createElement('template');
      decoded.innerHTML = JSON.parse(encoded.textContent);
      fragment = decoded.content;
    }
    const directory = fragment.querySelector('[data-topic-subtopics]');
    if (directory) {
      const prefix = `#subtopic-${directory.dataset.topicSubtopics}-`;
      for (const entry of atlas.search) {
        if (entry.type !== 'Subtopic' || !entry.href.startsWith(prefix)) continue;
        const item = document.createElement('li');
        item.id = entry.href.slice(1);
        item.textContent = entry.title;
        directory.append(item);
      }
    }
    // Move nodes rather than clone them: every authored ID continues to occur once.
    host.append(fragment);
    template.remove();
    const holder = card.querySelector('[data-progress-holder]');
    if (holder) {
      for (const label of Array.from(holder.querySelectorAll('label'))) {
        const input = label.querySelector('input.save-check');
        const unit = input && byId(input.id.replace(/-(practice|transfer)$/, ''));
        const destination = unit?.querySelector('.topic-details-inner') || unit;
        if (destination) destination.append(label);
      }
      // A missing destination must not silently discard a learner's saved control.
      if (holder.querySelector('.save-check')) {
        holder.hidden = false;
        holder.removeAttribute('aria-hidden');
        holder.setAttribute('aria-label', 'Additional saved unit checks');
      } else holder.remove();
    }
    document.dispatchEvent(new CustomEvent('atlas-topic-hydrated', {detail: {id: card.id}}));
  }

  function renderPathBody(item) {
    const template = item.querySelector('template[data-path-body]');
    if (!template) return;
    item.append(template.content);
    template.remove();
  }

  function hydrateSession(details) {
    const template = details.querySelector('template[data-session-body]');
    if (!template) return;
    details.append(template.content);
    template.remove();
  }

  function applyPathPreviews() {
    for (const list of document.querySelectorAll('.path-list')) {
      if (!list.closest('.role-detail')?.open) continue;
      const items = Array.from(list.querySelectorAll('.path-item'));
      if (!items.length) continue;
      const unfinished = items.filter(item => {
        const link = item.querySelector('a[href^="#topic-"]');
        return !completed(Number(link?.getAttribute('href').match(/^#topic-(\d+)/)?.[1]));
      });
      const preview = new Set((unfinished.length ? unfinished : items).slice(0, 3));
      const showAll = list.dataset.showAll === 'true';
      for (const item of items) {
        item.hidden = !showAll && !preview.has(item);
        if (!item.hidden && item.closest('.role-detail')?.open) renderPathBody(item);
      }
      const button = list.nextElementSibling?.matches('[data-show-path]') ? list.nextElementSibling : null;
      if (button) {
        button.hidden = items.length <= 3;
        button.setAttribute('aria-expanded', String(showAll));
        button.textContent = showAll ? 'Show first three unfinished topics' : `Show all (${items.length})`;
      }
    }
  }

  function initializePathPreviews() {
    for (const list of document.querySelectorAll('.path-list')) {
      if (!list.closest('.role-detail')?.open) continue;
      if (!list.id) list.id = `path-preview-${list.closest('.role-detail').id}`;
      if (list.nextElementSibling?.matches('[data-show-path]')) continue;
      const button = element('button', {
        type: 'button', class: 'iconbtn path-preview-toggle no-print',
        'data-show-path': '', 'aria-controls': list.id, 'aria-expanded': 'false'
      });
      button.addEventListener('click', () => {
        list.dataset.showAll = String(list.dataset.showAll !== 'true');
        applyPathPreviews();
      });
      list.after(button);
    }
    applyPathPreviews();
  }

  function reveal(hash, {scroll = true} = {}) {
    let id;
    try { id = decodeURIComponent(String(hash || '').replace(/^#/, '')); } catch { return null; }
    if (!id) return null;
    const number = id.match(/^(?:topic|subtopic|unit)-(\d{2})(?:-|$)/)?.[1] || atlas.lazyTargets?.[id];
    const card = number && cards.find(node => topicNumber(node) === Number(number));
    if (card) {
      library.style.contentVisibility = 'visible';
      hydrate(card);
      temporarilyRevealed.add(card.id);
      card.hidden = false;
      card.removeAttribute('aria-hidden');
      if (controls.status) controls.status.textContent = 'Opened linked topic. Your filters remain selected; change a filter to return to its results.';
    }
    const target = byId(id);
    if (!target) return null;
    const section = target.closest('.section');
    if (section) section.style.contentVisibility = 'visible';
    if (target.matches?.('.section')) {
      const panel = target.querySelector(':scope > details.reference-panel');
      if (panel) panel.open = true;
    }
    for (let parent = target; parent; parent = parent.parentElement) {
      if (parent.matches?.('details')) parent.open = true;
      if (parent.matches?.('.path-item')) { parent.hidden = false; renderPathBody(parent); }
    }
    if (scroll) requestAnimationFrame(() => target.scrollIntoView({block: 'start', behavior: 'auto'}));
    return target;
  }

  function buildOnboarding() {
    const box = byId('atlas-onboarding');
    if (!box) return;
    for (const choice of box.querySelectorAll('[data-start-choice]')) {
      choice.addEventListener('click', () => saveLocal('ai-atlas-onboarding-v1', choice.dataset.startChoice));
    }
    byId('dismiss-onboarding').addEventListener('click', () => {
      saveLocal('ai-atlas-onboarding-v1', 'dismissed');
      box.hidden = true;
      const destination = byId('start')?.querySelector('h1');
      if (destination) { destination.tabIndex = -1; destination.focus({preventScroll: true}); }
    });
    box.hidden = !!readLocal('ai-atlas-onboarding-v1');
  }

  function buildFilters() {
    if (!library) return;
    const panel = element('div', {class: 'card library-controls no-print', id: 'library-controls'});
    const makeSelect = (id, label, options) => {
      const fieldLabel = element('label', {for: id}, label);
      const select = element('select', {id});
      for (const [value, text] of options) select.append(element('option', {value}, text));
      fieldLabel.append(select);
      panel.append(fieldLabel);
      select.addEventListener('change', () => { temporarilyRevealed.clear(); filterLibrary(); });
      return select;
    };
    controls.level = makeSelect('library-level', 'Topic level', [
      ['', 'All levels'], ['level-1', 'Foundations'], ['level-2', 'Core AI and ML'],
      ['level-3', 'Modern AI'], ['level-4', 'Production AI'], ['level-5', 'Specializations'], ['level-6', 'Projects']
    ]);
    controls.priority = makeSelect('library-priority', 'Priority for selected profession', [
      ['', 'All priorities'], ...['Essential', 'Recommended', 'Advanced', 'Optional', 'Not required now'].map(value => [value, value]), ['Not listed', 'Not listed']
    ]);
    controls.difficulty = makeSelect('library-difficulty', 'Difficulty', [
      ['', 'All difficulties'], ['Beginner', 'Beginner'], ['Intermediate', 'Intermediate'], ['Advanced', 'Advanced']
    ]);
    controls.completion = makeSelect('library-completion', 'Topic scope completion', [
      ['', 'Any completion status'], ['unfinished', 'Unfinished'], ['complete', 'Self-reported complete']
    ]);
    const allLabel = element('label', {class: 'checkrow library-all'});
    controls.all = element('input', {id: 'library-all-topics', type: 'checkbox'});
    allLabel.append(controls.all, document.createTextNode('All topics'));
    controls.all.addEventListener('change', () => { temporarilyRevealed.clear(); filterLibrary(); });
    controls.other = element('button', {type: 'button', class: 'iconbtn', 'aria-expanded': 'false'}, 'Show other topics');
    controls.other.addEventListener('click', () => {
      controls.all.checked = !controls.all.checked;
      temporarilyRevealed.clear();
      filterLibrary();
    });
    controls.reset = element('button', {type: 'button', class: 'iconbtn'}, 'Reset library filters');
    controls.reset.addEventListener('click', () => {
      for (const field of [controls.level, controls.priority, controls.difficulty, controls.completion]) field.value = '';
      controls.all.checked = false;
      temporarilyRevealed.clear();
      filterLibrary();
    });
    controls.status = element('p', {id: 'library-status', role: 'status', 'aria-live': 'polite', 'aria-atomic': 'true'});
    panel.append(allLabel, controls.other, controls.reset, controls.status);
    library.querySelector('.section-heading')?.after(panel);
  }

  function filterLibrary() {
    if (!controls.status) return;
    const priorities = atlas.priorities[role] || {};
    const showAll = !role || controls.all.checked;
    const otherCount = cards.filter(card => !corePriorities.has(priorities[String(topicNumber(card))])).length;
    let visible = 0;
    for (const card of cards) {
      const number = topicNumber(card);
      const priority = priorities[String(number)] || 'Not listed';
      const difficulty = card.dataset.difficulty || Array.from(card.querySelectorAll('.topic-meta span')).map(node => node.textContent).find(text => /Beginner|Intermediate|Advanced/.test(text)) || '';
      const priorityIsExplicit = !!controls.priority.value;
      const show = (!controls.level.value || card.classList.contains(controls.level.value)) &&
        (!priorityIsExplicit || priority === controls.priority.value) &&
        (!controls.difficulty.value || difficulty.includes(controls.difficulty.value)) &&
        (!controls.completion.value || completed(number) === (controls.completion.value === 'complete')) &&
        (showAll || priorityIsExplicit || corePriorities.has(priority));
      card.hidden = !show && !temporarilyRevealed.has(card.id);
      card.setAttribute('aria-hidden', String(card.hidden));
      if (!card.hidden) visible++;
    }
    controls.priority.disabled = !role;
    controls.all.disabled = !role;
    controls.other.hidden = !role || !!controls.priority.value;
    controls.other.setAttribute('aria-hidden', String(controls.other.hidden));
    controls.other.textContent = controls.all.checked ? 'Show my path topics' : `Show other topics (${otherCount})`;
    controls.other.setAttribute('aria-expanded', String(controls.all.checked));
    controls.status.textContent = `${visible} of ${cards.length} topics shown${role && !showAll ? ' for your selected learning path' : ''}. Topic order is unchanged.`;
  }

  function buildNextStep() {
    const topbar = document.querySelector('.topbar');
    if (!topbar) return;
    const bar = element('aside', {class: 'next-step-bar no-print', id: 'next-step-bar', 'aria-label': 'Next step in my learning path', hidden: ''});
    const text = element('span', {id: 'next-step-summary'});
    const link = element('a', {id: 'next-step-open', class: 'chip', href: '#choose-role'}, 'Open');
    const dismiss = element('button', {type: 'button', class: 'iconbtn', 'aria-label': 'Dismiss next step bar'}, 'Dismiss');
    dismiss.addEventListener('click', () => {
      dismissedNextRole = role;
      bar.hidden = true;
      document.documentElement.classList.remove('has-next-step');
      // Keep keyboard focus in the reading viewport after its control disappears.
      const target = document.elementFromPoint?.(innerWidth * 0.6, innerHeight * 0.45)?.closest('p, h2, h3, summary, a, button') || home;
      if (target) {
        if (!target.matches('a, button, input, select, summary')) target.tabIndex = -1;
        target.focus({preventScroll: target !== home});
      }
    });
    bar.append(text, link, dismiss);
    topbar.after(bar);
    updateBarOffset = () => {
      // An unselected first visit has no bar; avoid forcing full-page layout.
      if (bar.hidden) return;
      document.documentElement.style.setProperty('--atlas-topbar-height', `${topbar.getBoundingClientRect?.().height || 72}px`);
    };
    if (typeof ResizeObserver === 'function') new ResizeObserver(updateBarOffset).observe(topbar);
  }

  function updateNextStep() {
    const bar = byId('next-step-bar');
    if (!bar) return;
    const valid = !!role && Object.hasOwn(atlas.priorities, role);
    bar.hidden = !valid || dismissedNextRole === role;
    document.documentElement.classList.toggle('has-next-step', !bar.hidden);
    if (!bar.hidden) requestAnimationFrame(updateBarOffset);
    if (!valid) return;
    const label = home.options[home.selectedIndex]?.textContent.trim() || role;
    const nextName = byId('next-topic-name')?.textContent.trim() || 'Choose your next topic';
    const percent = byId('home-role-meter')?.value || 0;
    const nextHref = byId('next-topic-link')?.getAttribute('href') || '#role-paths';
    const nextNumber = nextHref.match(/^#topic-(\d+)/)?.[1];
    const unitChecks = nextNumber ? Array.from(document.querySelectorAll(`input[id^="unit-${nextNumber}-"]`)) : [];
    const detail = unitChecks.length ? ` · next topic unit checks ${unitChecks.filter(check => check.checked).length}/${unitChecks.length}` : '';
    byId('next-step-summary').textContent = `${label} · ${nextName} · ${percent}% of topic scopes${detail}`;
    byId('next-step-open').href = nextHref;
  }

  function labelMatrix() {
    const label = document.querySelector('label[for="role-filter"]');
    if (label) label.textContent = `Showing priorities for: ${home?.options[home.selectedIndex]?.textContent.trim() || 'choose a profession'} (change)`;
  }

  function update(nextRole = home?.value || '') {
    const changed = role !== nextRole;
    role = Object.hasOwn(atlas.priorities, nextRole) ? nextRole : '';
    if (changed) {
      temporarilyRevealed.clear();
      if (controls.priority) controls.priority.value = '';
      if (controls.all) controls.all.checked = false;
    }
    filterLibrary();
    updateNextStep();
    labelMatrix();
    applyPathPreviews();
  }

  function prepareNavigation() {
    const nav = document.querySelector('#sidebar nav[aria-label="Primary sections"]');
    const sections = [
      ['start', 'Start'], ['entry-check', 'Entry check'], ['beginner-workshop', 'Beginner workshop'],
      ['choose-role', 'Choose profession'], ['role-paths', 'My path'], ['projects', 'Projects'],
      ['progress', 'Progress'], ['library', 'Topic library (reference)'], ['relevance', 'Relevance matrix'],
      ['glossary', 'Glossary'], ['assessment-guide', 'Assessment'], ['learn-with-ai', 'AI tutor'],
      ['official-resources', 'Official references']
    ];
    const navMatches = nav && Array.from(nav.querySelectorAll('.navlink')).map(link => link.getAttribute('href')).join('|') === sections.map(([id]) => '#'+id).join('|');
    if (nav && !navMatches) {
      nav.replaceChildren(...sections.filter(([id]) => byId(id)).map(([id, label]) => element('a', {class: 'navlink', href: `#${id}`}, label)));
    }
    // Preserve every support section and all topic-card ordering. Only move the
    // top-level destinations into the same order as the one primary navigation.
    const staticOrder = main && Array.from(main.children).filter(node => sections.some(([id]) => node.id === id)).map(node => node.id).join('|');
    if (main && byId('start')?.parentElement === main && staticOrder !== sections.map(([id]) => id).join('|')) {
      const marker = element('span', {hidden: ''});
      main.insertBefore(marker, byId('start'));
      for (const [id] of sections) {
        const section = byId(id);
        if (section?.parentElement === main) main.insertBefore(section, marker);
      }
      marker.remove();
    }
    if (typeof IntersectionObserver !== 'function') return;
    const visible = new Map();
    let lastCurrent = '';
    const updateCurrent = () => {
      const top = innerHeight * 0.15;
      const bottom = innerHeight * 0.35;
      const candidates = Array.from(visible.values()).map(node => {
        const rect = node.getBoundingClientRect();
        return {id:node.id, overlap:Math.max(0,Math.min(rect.bottom,bottom)-Math.max(rect.top,top)), distance:Math.abs(rect.top-top)};
      }).filter(item=>item.overlap>0).sort((a,b)=>b.overlap-a.overlap||a.distance-b.distance);
      const current = candidates[0]?.id || '';
      if (current === lastCurrent) return;
      lastCurrent = current;
      for (const link of nav?.querySelectorAll('.navlink') || []) {
        if (link.getAttribute('href') === `#${current}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    };
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) visible.set(entry.target.id, entry.target);
        else visible.delete(entry.target.id);
      }
      updateCurrent();
    }, {rootMargin: '-15% 0px -65% 0px', threshold: 0});
    let scheduled = false;
    window.addEventListener('scroll', () => {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(() => { scheduled = false; updateCurrent(); });
    }, {passive:true});
    for (const [id] of sections) if (byId(id)) observer.observe(byId(id));
  }

  function prepareMatrixHint() {
    const wrapper = byId('relevance')?.querySelector('.tablewrap');
    if (!wrapper) return;
    const hint = element('p', {id: 'matrix-scroll-hint', class: 'matrix-scroll-hint'}, 'On a narrow screen, swipe or use the keyboard to scroll this topic and priority table horizontally.');
    wrapper.before(hint);
    wrapper.tabIndex = 0;
    wrapper.setAttribute('role', 'region');
    wrapper.setAttribute('aria-label', 'Topic priorities table');
    wrapper.setAttribute('aria-describedby', hint.id);
  }

  document.addEventListener('toggle', event => {
    if (event.target.matches?.('.topic-details') && event.target.open) hydrate(event.target.closest('.topic-card'));
    if (event.target.matches?.('.role-detail') && event.target.open) initializePathPreviews();
    if (event.target.matches?.('.session-plan') && event.target.open) hydrateSession(event.target);
  }, true);
  document.addEventListener('change', event => {
    if (event.target.matches?.('.save-check')) setTimeout(() => update(), 0);
  });
  document.addEventListener('atlas-progress-restored', () => update());
  byId('reset-progress')?.addEventListener('click', () => setTimeout(() => update(), 0));
  for (const selector of [home, matrix]) selector?.addEventListener('change', () => setTimeout(() => update(), 0));

  window.addEventListener('beforeprint', () => {
    for (const card of cards) hydrate(card);
    for (const item of document.querySelectorAll('.path-item')) renderPathBody(item);
    for (const template of document.querySelectorAll('template[data-session-body]')) hydrateSession(template.parentElement);
    // Capture newly hydrated details too, so print does not leave every unit open.
    printState = Array.from(document.querySelectorAll('details')).map(node => [node, node.open]);
    for (const details of document.querySelectorAll('main details')) details.open = true;
  });
  window.addEventListener('afterprint', () => {
    for (const [node, open] of printState || []) node.open = open;
    printState = null;
  });

  buildOnboarding();
  buildFilters();
  buildNextStep();
  prepareNavigation();
  prepareMatrixHint();
  initializePathPreviews();
  window.AtlasExperience = {hydrate, reveal, update};
  // reader.js invokes update after restoring the role and reveal before native anchors.
})();
