/* Same-site metadata search. The catalog and navigation remain usable without it. */
(() => {
  'use strict';
  const normalize = value => String(value || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

  function searchRecords(records, query, topic = '') {
    const words = normalize(query).trim().split(/\s+/).filter(Boolean);
    return records.filter(record => (!topic || record.topic === topic) && words.every(word =>
      normalize([record.title, record.description, record.topic, record.type, record.level, record.source].join(' ')).includes(word)
    )).map(record => {
      const title = normalize(record.title);
      const score = words.reduce((sum, word) => sum + (title.startsWith(word) ? 4 : title.includes(word) ? 2 : 0), 0);
      return {record, score};
    }).sort((a, b) => b.score - a.score || a.record.title.localeCompare(b.record.title)).map(item => item.record);
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = {normalize, searchRecords};
  if (typeof document === 'undefined') return;
  const panel = document.querySelector('[data-library-search]');
  if (!panel) return;
  const form = panel.querySelector('[data-search-form]');
  const input = panel.querySelector('[data-search-input]');
  const topic = panel.querySelector('[data-search-topic]');
  const status = panel.querySelector('[data-search-status]');
  const results = panel.querySelector('[data-search-results]');

  // A search link also opens the disclosure when it is reached by a fragment.
  const openFromHash = () => {if (location.hash === '#library-search') panel.open = true;};
  openFromHash();
  addEventListener('hashchange', openFromHash);
  document.querySelectorAll('a[href="#library-search"]').forEach(link => link.addEventListener('click', () => {
    panel.open = true;
    if (!form.hidden) input.focus();
  }));

  async function start() {
    const indexURL = new URL(panel.dataset.searchIndex, location.href);
    const response = await fetch(indexURL, {credentials: 'same-origin'});
    if (!response.ok) throw new Error('Index unavailable');
    const data = await response.json();
    if (!Array.isArray(data)) throw new Error('Invalid search index');
    const base = indexURL.pathname.replace(/assets\/data\/library-search\.json$/, '');
    const records = data.filter(record => {
      if (!record || typeof record.title !== 'string' || typeof record.url !== 'string') return false;
      try {
        const url = new URL(record.url, location.href);
        return url.origin === indexURL.origin && url.pathname.startsWith(base);
      } catch {return false;}
    });
    const topics = [...new Set(records.map(record => record.topic).filter(Boolean))].sort();
    for (const name of topics) {
      const option = document.createElement('option');option.value = name;option.textContent = name;topic.append(option);
    }
    let timer;
    function render() {
      clearTimeout(timer);
      results.replaceChildren();
      if (!input.value.trim() && !topic.value) {
        status.textContent = `Search ${records.length} indexed courses, guides and tools. Enter words or choose a topic.`;
        return;
      }
      const matches = searchRecords(records, input.value, topic.value);
      status.textContent = matches.length === 0 ? 'No matches. Try fewer words, a filename, or another topic.' :
        `${matches.length} ${matches.length === 1 ? 'match' : 'matches'}.` + (matches.length > 20 ? ' Showing the first 20; add words to narrow the results.' : '');
      for (const record of matches.slice(0, 20)) {
        const item = document.createElement('li');
        const link = document.createElement('a');link.href = record.url;link.textContent = record.title;item.append(link);
        const metadata = document.createElement('p');metadata.className = 'search-result-meta';
        metadata.textContent = [record.topic, record.type, record.level].filter(Boolean).join(' · ');item.append(metadata);
        if (record.description) {const description = document.createElement('p');description.textContent = record.description;item.append(description);}
        const source = document.createElement('small');source.textContent = record.source;item.append(source);
        results.append(item);
      }
    }
    input.addEventListener('input', () => {clearTimeout(timer);timer = setTimeout(render, 150);});
    topic.addEventListener('change', render);
    form.addEventListener('submit', event => {event.preventDefault();render();});
    form.addEventListener('reset', event => {event.preventDefault();input.value = '';topic.value = '';render();input.focus();});
    form.hidden = false;
    render();
  }
  start().catch(() => {status.textContent = 'Search could not load. Use Browse every topic or Choose a learning path below.';});
})();
