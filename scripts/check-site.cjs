const fs = require('node:fs');
const path = require('node:path');
const {ROOT, read, yaml} = require('./lib.cjs');
const {cssLinks, parseDocument, decodedFragment} = require('./link-utils.cjs');
const {expandHosted} = require('./build-atlas-hosted.cjs');
const site = path.join(ROOT, '_site');
if (!fs.existsSync(site)) throw new Error('Build Jekyll before checking the site.');
const config = yaml.parse(read('_config.yml'));
const base = config.baseurl.replace(/\/$/, '');
const origin = new URL(config.url).origin;
const errors = [];
const documents = new Map();
const files = new Set();
let links = 0;
function scan(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) scan(file);
    else files.add(path.relative(site, file).split(path.sep).join('/'));
  }
}
scan(site);
function document(file) {
  if (!documents.has(file)) {
    const source = fs.readFileSync(path.join(site, file), 'utf8');
    let parsed = parseDocument(source, false);
    const payload = parsed.document.querySelector('script[data-atlas-content]')?.getAttribute('data-atlas-content');
    if (payload) {
      const runtime = parsed.document.querySelector('script[data-atlas-runtime]')?.getAttribute('data-atlas-runtime');
      if (!runtime) throw new Error(`${file}: missing hosted reader runtime reference`);
      const relative = path.posix.normalize(path.posix.join(path.posix.dirname(file), payload));
      if (!files.has(relative)) throw new Error(`${file}: missing hosted reader payload ${payload}`);
      const fragments = JSON.parse(fs.readFileSync(path.join(site, relative), 'utf8'));
      parsed = parseDocument(expandHosted(source, fragments), false);
      parsed.links.push({url: payload}, {url: runtime});
    }
    documents.set(file, parsed);
  }
  return documents.get(file);
}
function check(file, raw) {
  if (!raw || /^(?:mailto|tel|data|blob|javascript):/i.test(raw)) return;
  if (raw.includes('{{') || raw.includes('{%')) {
    errors.push(`${file}: unresolved template in link ${raw}`);
    return;
  }
  try {
    const url = new URL(raw, origin + base + '/' + file);
    if (url.origin !== origin) return;
    const pathname = decodeURIComponent(url.pathname);
    if (pathname !== base && !pathname.startsWith(base + '/')) {
      if (/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(raw)) return;
      errors.push(`${file}: link escapes configured site base path: ${raw}`);
      return;
    }
    links++;
    let target = pathname.slice(base.length).replace(/^\//, '');
    if (!target || target.endsWith('/')) target += 'index.html';
    else if (!files.has(target) && files.has(target + '/index.html')) target += '/index.html';
    if (!files.has(target)) {
      errors.push(`${file}: missing or case-mismatched target ${raw}`);
      return;
    }
    const fragment = decodedFragment(url.hash.slice(1));
    if (fragment && /\.(html|svg)$/i.test(target) && !document(target).anchors.has(fragment)) {
      errors.push(`${file}: missing anchor ${raw}`);
    }
  } catch (error) {
    if (!(error instanceof URIError || error instanceof TypeError)) throw error;
    errors.push(`${file}: invalid URL ${raw}: ${error.message}`);
  }
}
let pages = 0;
for (const file of files) {
  if (/\.(html|svg)$/i.test(file)) {
    const parsed = document(file);
    if (file.endsWith('.html')) {
      pages++;
      const canonical = parsed.document.querySelector('link[rel="canonical"]')?.getAttribute('href');
      if (!canonical || !canonical.startsWith(config.url + base + '/')) errors.push(`${file}: missing or incorrect canonical URL`);
      if (!parsed.document.querySelector('title')?.textContent?.trim()) errors.push(`${file}: missing title`);
      if (!parsed.document.querySelector('meta[name="description"]')?.getAttribute('content')) errors.push(`${file}: missing description`);
    }
    for (const {url} of parsed.links) check(file, url);
  } else if (file.endsWith('.css')) {
    for (const url of cssLinks(fs.readFileSync(path.join(site, file), 'utf8'))) check(file, url);
  }
}
for (const hidden of config.exclude || []) {
  if (fs.existsSync(path.join(site, hidden))) errors.push('Excluded path was published: ' + hidden);
}
for (const required of ['examples/containers/local-services/.env.example', 'apps/ai-learning-atlas/exercises/assistant.py']) {
  if (!files.has(required)) errors.push('Missing downloadable example: ' + required);
}
if (!files.has('sitemap.xml')) errors.push('Missing sitemap.xml');
else {
  for (const match of fs.readFileSync(path.join(site, 'sitemap.xml'), 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)) {
    check('sitemap.xml', match[1].replace(/&amp;/g, '&'));
  }
}
if (!pages) errors.push('No built HTML pages found.');
if (errors.length) {
  console.error([...new Set(errors)].join('\n'));
  process.exitCode = 1;
} else console.log(`PASS: ${pages} built pages, ${links} internal links, fragments, CSS/SVG assets, sitemap and publication exclusions.`);
