(() => {
  'use strict';
  const loader = document.querySelector('script[data-atlas-content]');
  const status = document.getElementById('atlas-load-status');
  const yieldToBrowser = () => new Promise(resolve => setTimeout(resolve, 0));
  async function load() {
    const response = await fetch(loader.dataset.atlasContent);
    if (!response.ok) throw new Error(`Reader content returned HTTP ${response.status}.`);
    const fragments = await response.json();
    const placeholders = [...document.querySelectorAll('[data-atlas-fragment]')];
    if (!Array.isArray(fragments) || fragments.length !== placeholders.length ||
        fragments.some(fragment => typeof fragment !== 'string')) {
      throw new Error('Reader content does not match this page. Reload to get a consistent version.');
    }
    await new Promise(resolve => requestAnimationFrame(() => setTimeout(resolve, 0)));
    for (const [index, placeholder] of placeholders.entries()) {
      if (placeholder.dataset.atlasFragment !== String(index)) throw new Error('Reader sections are out of order.');
      const template = document.createElement('template');
      template.innerHTML = fragments[index];
      placeholder.replaceWith(template.content);
      await yieldToBrowser();
    }
    await new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = loader.dataset.atlasRuntime;
      script.onload = resolve;
      script.onerror = () => reject(new Error('Reader controls could not be loaded.'));
      document.body.append(script);
    });
    if (!window.AtlasExperience || document.documentElement.dataset.atlasRuntimeReady !== 'true') {
      throw new Error('Reader controls did not initialize.');
    }
    document.querySelector('.shell').removeAttribute('inert');
    status.hidden = true;
    // Resolve a fragment that arrived before its element, without adding a history entry.
    if (location.hash) location.replace(location.href);
    document.documentElement.dataset.atlasReady = 'true';
  }
  load().catch(error => {
    console.error('Could not load the Atlas reader:', error);
    status.setAttribute('role', 'alert');
    status.querySelector('span').textContent = `${error.message} `;
    const retry = document.createElement('button');
    retry.type = 'button';
    retry.textContent = 'Retry';
    retry.addEventListener('click', () => location.reload());
    status.append(' ', retry);
    document.documentElement.dataset.atlasReady = 'error';
  });
})();
