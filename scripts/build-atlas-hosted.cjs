const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {parseHTML} = require('linkedom');
const {ROOT, read} = require('./lib.cjs');

function hostedFiles(source) {
  const {document} = parseHTML(source.toString());
  const files = {};
  const asset = (name, extension, content) => {
    const hash = crypto.createHash('sha256').update(content).digest('hex').slice(0, 12);
    const filename = `reader-assets/${name}.${hash}.${extension}`;
    files[filename] = content;
    return filename;
  };
  const styles = [...document.head.querySelectorAll('style')];
  const css = asset('reader', 'css', styles.map(node => node.textContent).join('\n') + '\n' +
    read('apps/ai-learning-atlas/source/hosted.css'));
  const stylesheet = document.createElement('link');
  stylesheet.rel = 'stylesheet';
  stylesheet.href = css;
  styles[0].replaceWith(stylesheet);
  styles.slice(1).forEach(node => node.remove());

  const scripts = [...document.body.querySelectorAll(':scope > script:not([type="application/json"])')];
  const runtime = asset('runtime', 'js', scripts.map(node => node.textContent).join('\n;\n') +
    "\ndocument.documentElement.dataset.atlasRuntimeReady = 'true';\n");
  scripts.forEach(node => node.remove());
  const content = [];
  const defer = node => {
    const placeholder = document.createElement(node.tagName === 'SECTION' ? 'section' : 'template');
    if (node.tagName === 'SECTION') {
      placeholder.id = node.id;
      placeholder.className = node.className;
      const height = node.id === 'beginner-workshop' ? 6000 : node.id === 'library' ? 16000 : 1800;
      placeholder.style.minHeight = `${height}px`;
    }
    placeholder.setAttribute('data-atlas-fragment', String(content.length));
    content.push(node.outerHTML);
    node.replaceWith(placeholder);
  };
  for (const section of [...document.querySelectorAll('main > .section')]) {
    if (!['start', 'entry-check'].includes(section.id)) defer(section);
  }
  for (const data of [...document.body.querySelectorAll(':scope > script[type="application/json"]')]) defer(data);
  const payload = asset('content', 'json', JSON.stringify(content));
  const loader = document.createElement('script');
  loader.defer = true;
  loader.src = asset('loader', 'js', read('scripts/templates/atlas-loader.js'));
  loader.setAttribute('data-atlas-content', payload);
  loader.setAttribute('data-atlas-runtime', runtime);
  document.head.append(loader);

  document.querySelector('.shell').setAttribute('inert', '');
  const status = document.createElement('aside');
  status.id = 'atlas-load-status';
  status.setAttribute('role', 'status');
  status.style.cssText = 'position:fixed;bottom:16px;right:16px;z-index:100;padding:12px;background:#fff;color:#1a2741;border:1px solid #7787a3;border-radius:8px;max-width:calc(100% - 32px)';
  status.innerHTML = '<span>Loading the complete reader...</span> <a href="offline.html">Open the single-file reader</a>';
  document.body.append(status);
  const noscript = document.createElement('noscript');
  noscript.innerHTML = '<p>This hosted reader requires JavaScript. <a href="offline.html">Open the complete single-file reader</a> to read without JavaScript.</p>';
  document.body.prepend(noscript);
  const download = document.createElement('a');
  download.href = 'offline.html';
  download.setAttribute('download', '');
  download.textContent = 'Download the complete offline HTML';
  document.querySelector('main footer').append(' · ', download);
  files['index.html'] = '<!doctype html>\n' + document.documentElement.outerHTML + '\n';
  files['offline.html'] = source;
  return files;
}

function expandHosted(source, fragments) {
  if (!Array.isArray(fragments) || fragments.some(item => typeof item !== 'string')) {
    throw new Error('Invalid hosted Atlas fragment payload.');
  }
  const {document} = parseHTML(source);
  const placeholders = [...document.querySelectorAll('[data-atlas-fragment]')];
  if (placeholders.length !== fragments.length) throw new Error('Hosted Atlas fragment count does not match its HTML.');
  placeholders.forEach((node, index) => {
    if (node.getAttribute('data-atlas-fragment') !== String(index)) throw new Error('Hosted Atlas fragments are out of order.');
    const template = document.createElement('template');
    template.innerHTML = fragments[index];
    node.replaceWith(template.content);
  });
  return document.toString();
}

if (require.main === module) {
  const site = process.argv.includes('--site');
  const destination = path.join(ROOT, site ? '_site/apps/ai-learning-atlas' : '.runtime/atlas-hosted');
  if (site && !fs.existsSync(path.join(destination, 'index.html'))) {
    throw new Error('Build the actual Jekyll site before preparing its hosted Atlas reader.');
  }
  const source = fs.readFileSync(path.join(ROOT, 'apps/ai-learning-atlas/index.html'));
  const files = hostedFiles(source);
  for (const [name, content] of Object.entries(files)) {
    const target = path.join(destination, name);
    fs.mkdirSync(path.dirname(target), {recursive: true});
    fs.writeFileSync(target, content);
  }
  console.log(`Built hosted Atlas at ${destination}; the complete offline HTML is preserved byte-for-byte.`);
}

module.exports = {hostedFiles, expandHosted};
