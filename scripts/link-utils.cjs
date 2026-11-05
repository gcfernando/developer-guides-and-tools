const MarkdownIt = require('markdown-it');
const {parseHTML} = require('linkedom');

function cssLinks(css) {
  const urls = [];
  const pattern = /\/\*[\s\S]*?\*\/|url\(\s*(?:"([^"]*)"|'([^']*)'|([^)\s]+))\s*\)|@import\s+["']([^"']+)["']/gi;
  for (const match of css.matchAll(pattern)) {
    const url = match[1] ?? match[2] ?? match[3] ?? match[4];
    if (url !== undefined) urls.push(url);
  }
  return urls;
}

function parseDocument(text, markdown, Slugger) {
  if (markdown) {
    const md = new MarkdownIt({html: true, linkify: true});
    md.linkify.set({fuzzyLink: false});
    const slugger = new Slugger();
    md.renderer.rules.heading_open = (tokens, i, options, env, renderer) => {
      const inline = md.renderer.renderInline(tokens[i + 1].children, options, env);
      const {document} = parseHTML(`<span>${inline}</span>`);
      tokens[i].attrSet('id', slugger.slug(document.querySelector('span').textContent));
      return renderer.renderToken(tokens, i, options);
    };
    // GitHub/Jekyll support Markdown inside the collection's disclosure/div wrappers.
    // Leave code blocks intact while making these block boundaries visible to MarkdownIt.
    const lines = text.split('\n');
    const code = new Set();
    for (const token of md.parse(text, {})) {
      if (['fence', 'code_block'].includes(token.type)) {
        for (let i = token.map[0]; i < token.map[1]; i++) code.add(i);
      }
    }
    text = lines.map((line, i) => code.has(i) ? line : line.replace(
      /<\/?(?:div|details|summary)\b[^>]*>/gi, tag => `\n\n${tag}\n\n`
    )).join('\n');
    text = md.render(text);
  }
  const {document} = parseHTML(text);
  const anchors = new Set();
  const links = [];
  const roots = [document];
  const visited = new Set();
  for (let i = 0; i < roots.length; i++) {
    for (const node of roots[i].querySelectorAll('*')) {
      if (visited.has(node)) continue;
      visited.add(node);
      if (node.id) anchors.add(node.id);
      if (node.tagName === 'A' && node.hasAttribute('name')) anchors.add(node.getAttribute('name'));
      for (const attribute of ['href', 'src', 'poster', 'action', 'formaction', 'xlink:href']) {
        if (attribute === 'href' && node.tagName === 'LINK' &&
          /(?:^|\s)(?:preconnect|dns-prefetch)(?:\s|$)/.test(node.getAttribute('rel') || '')) continue;
        if (node.hasAttribute(attribute)) links.push({url: node.getAttribute(attribute), tag: node.tagName, attribute});
      }
      if (node.tagName === 'OBJECT' && node.hasAttribute('data')) links.push({url: node.getAttribute('data'), tag: node.tagName, attribute: 'data'});
      if (node.tagName === 'META' && /^(?:og:(?:url|image|video|audio)(?::url)?|twitter:(?:url|image))$/.test(
        node.getAttribute('property') || node.getAttribute('name') || ''
      ) && node.hasAttribute('content')) {
        links.push({url: node.getAttribute('content'), tag: node.tagName, attribute: 'content'});
      }
      if (node.hasAttribute('srcset')) {
        for (const candidate of node.getAttribute('srcset').split(/,\s+(?![^,]*;base64)/)) {
          const url = candidate.trim().split(/\s+/)[0];
          if (url) links.push({url, tag: node.tagName, attribute: 'srcset'});
        }
      }
      const css = node.tagName === 'STYLE' ? node.textContent : node.getAttribute('style');
      for (const url of cssLinks(css || '')) links.push({url, tag: node.tagName, attribute: 'css'});
      if (node.tagName === 'TEMPLATE') roots.push(node.content);
      if (node.tagName === 'SCRIPT' && node.hasAttribute('data-topic-json')) {
        roots.push(parseHTML(JSON.parse(node.textContent)).document);
      }
    }
  }
  const atlas = document.getElementById('atlas-data');
  if (atlas) {
    const data = JSON.parse(atlas.textContent);
    const directories = [...visited].filter(node => node.hasAttribute('data-topic-subtopics'));
    for (const record of data.search || []) {
      links.push({url: record.href, tag: 'ATLAS', attribute: 'search'});
      if (record.type === 'Subtopic' && directories.some(node =>
        record.href.startsWith(`#subtopic-${node.getAttribute('data-topic-subtopics')}-`))) {
        anchors.add(record.href.slice(1));
      }
    }
  }
  return {document, anchors, links};
}

function decodedFragment(fragment) {
  return decodeURIComponent(fragment.split(':~:text=')[0]);
}

module.exports = {cssLinks, parseDocument, decodedFragment};
