const fs = require('node:fs');
const path = require('node:path');
const {ROOT, walk, relative, read, frontMatter, yaml} = require('./lib.cjs');
const {cssLinks, parseDocument, decodedFragment} = require('./link-utils.cjs');

async function main() {
  const {default: Slugger} = await import('github-slugger');
  const config = yaml.parse(read('_config.yml'));
  const origin = new URL(config.url).origin;
  const base = config.baseurl.replace(/\/$/, '');
  const routes = new Map(Object.entries(JSON.parse(read('_data/routes.json'))).map(([file, route]) => [base + route, file]));
  const includeRuntimeDocs = process.argv.includes('--include-runtime-docs');
  const runtime = path.join(ROOT, '.runtime');
  const all = [...walk(), ...(includeRuntimeDocs && fs.existsSync(runtime) ? walk(runtime) : [])].map(relative);
  const exact = new Set(all);
  const directories = new Set(['']);
  for (const file of all) {
    let directory = path.posix.dirname(file);
    while (directory !== '.') {
      directories.add(directory);
      directory = path.posix.dirname(directory);
    }
  }
  const excluded = file => config.exclude.some(item => file === item || file.startsWith(item + '/'));
  const textDocument = file => /\.(md|markdown|txt)$/i.test(file);
  const template = file => file.startsWith('_layouts/') || file.startsWith('scripts/templates/') || file.startsWith('apps/ai-learning-atlas/source/');
  const files = all.filter(file => (textDocument(file) || /\.(html|css|svg)$/i.test(file)) && !template(file) &&
    (!file.startsWith('.runtime/') || textDocument(file)));
  const documents = new Map();
  const external = new Map();
  const problems = [];
  const deferred = [];
  const counts = {documents: files.length, localLinks: 0, fragments: 0, publishedLinks: 0, externalUrls: 0};
  function document(file) {
    if (!documents.has(file)) {
      const text = read(file);
      documents.set(file, parseDocument(textDocument(file) ? frontMatter(text).body : text, textDocument(file), Slugger));
    }
    return documents.get(file);
  }
  function fail(file, url, reason) { problems.push({file, url, reason}); }
  function fragment(file, target, hash, url) {
    if (!hash || !(textDocument(target) || /\.(html|svg)$/i.test(target))) return;
    const id = decodedFragment(hash);
    if (!id) return;
    counts.fragments++;
    if (!document(target).anchors.has(id)) fail(file, url, `missing anchor "${id}" in ${target}`);
  }
  function externalLink(url, file) {
    const clean = new URL(url);
    if (!['http:', 'https:'].includes(clean.protocol)) return;
    clean.hash = '';
    const key = clean.href;
    if (!external.has(key)) external.set(key, new Set());
    external.get(key).add(file);
  }
  function target(file, name, hash, url, published = false) {
    name = path.posix.normalize(name).replace(/^\.\//, '').replace(/\/$/, '');
    if (name === '.') name = '';
    if (name === '..' || name.startsWith('../')) return fail(file, url, 'escapes repository');
    if (directories.has(name)) {
      if (published) {
        const index = [name + '/index.html', name + '/index.md'].find(candidate => exact.has(candidate));
        if (!index) return fail(file, url, `published directory has no index: ${name}`);
        name = index;
      } else if (hash) {
        const index = [name + '/README.md', name + '/index.md', name + '/index.html'].find(candidate => exact.has(candidate));
        if (!index) return fail(file, url, `directory fragment has no readable index: ${name}`);
        name = index;
      } else return;
    }
    if (!exact.has(name)) return fail(file, url, `missing or case-mismatched path: ${name}`);
    if (published && excluded(name)) return fail(file, url, `target is excluded from publication: ${name}`);
    fragment(file, name, hash, url);
  }
  function check(file, link) {
    const url = link.url?.trim();
    if (!url) return;
    if (url.includes('{{') || url.includes('{%')) {
      if (textDocument(file)) return fail(file, url, 'unrendered template URL in Markdown or plain text; use a concrete source or published link');
      deferred.push({file, url, reason: 'requires template rendering'});
      return;
    }
    if (/^(?:data|mailto|tel|blob|javascript):/i.test(url)) return;
    if (/^[a-z][a-z0-9+.-]*:/i.test(url) && !/^https?:/i.test(url)) {
      deferred.push({file, url, reason: 'non-HTTP protocol'});
      return;
    }
    try {
      if (/^(?:https?:|\/\/)/i.test(url)) {
        const parsed = new URL(url, config.url);
        const pathname = decodeURIComponent(parsed.pathname);
        if (parsed.origin === origin && (pathname === base || pathname.startsWith(base + '/'))) {
          counts.publishedLinks++;
          let route = routes.get(pathname) || routes.get(pathname + '/');
          if (route) return target(file, route, parsed.hash.slice(1), url, true);
          return target(file, pathname.slice(base.length + 1), parsed.hash.slice(1), url, true);
        }
        const prefix = '/' + config.repository + '/';
        if (parsed.hostname === 'raw.githubusercontent.com' && pathname.startsWith(prefix + 'main/')) {
          counts.localLinks++;
          return target(file, pathname.slice((prefix + 'main/').length), parsed.hash.slice(1), url);
        }
        if (parsed.hostname === 'github.com' && pathname.startsWith(prefix)) {
          const match = pathname.slice(prefix.length).match(/^(?:blob|tree|raw)\/main\/(.+)$/);
          if (match) {
            counts.localLinks++;
            return target(file, match[1], parsed.hash.slice(1), url);
          }
        }
        return externalLink(parsed.href, file);
      }
      counts.localLinks++;
      const hashIndex = url.indexOf('#');
      const hash = hashIndex < 0 ? '' : url.slice(hashIndex + 1);
      const pathname = decodeURIComponent((hashIndex < 0 ? url : url.slice(0, hashIndex)).split('?')[0]);
      if (!pathname) return fragment(file, file, hash, url);
      if (pathname.startsWith('/')) {
        const route = routes.get(pathname) || routes.get(pathname + '/');
        if (route) return target(file, route, hash, url, true);
        if (!pathname.startsWith(base + '/')) return fail(file, url, 'root-relative URL is outside the configured site base path');
        return target(file, pathname.slice(base.length + 1), hash, url, true);
      }
      if (textDocument(file) && link.tag === 'A' && /\.html?$/i.test(pathname)) {
        fail(file, url, 'HTML reader link must use its published browser URL');
      }
      target(file, path.posix.join(path.posix.dirname(file), pathname), hash, url);
    } catch (error) {
      if (!(error instanceof URIError || error instanceof TypeError)) throw error;
      fail(file, url, `invalid URL encoding: ${error.message}`);
    }
  }
  for (const file of files) {
    const links = file.endsWith('.css') ? cssLinks(read(file)).map(url => ({url, tag: 'CSS', attribute: 'url'})) : document(file).links;
    for (const link of links) check(file, link);
  }
  for (const item of yaml.parse(read('_data/navigation.yml'))) check('_data/navigation.yml', {url: base + item.url});
  const records = [...external].sort(([a], [b]) => a.localeCompare(b)).map(([url, sources]) => ({url, sources: [...sources].sort()}));
  counts.externalUrls = records.length;
  const report = {
    counts, problems: [...new Map(problems.map(item => [JSON.stringify(item), item])).values()], deferred,
    limits: 'Markdown and plain-text documents use GitHub heading IDs plus explicit anchors. Actual Jekyll heading IDs, Liquid templates and post-render URL rewriting require check:site. Atlas generated templates/search records are expanded; arbitrary JavaScript URLs are not executed. Historical reading copies and .txt files are checked; compressed .gz originals are verified by the provenance check. Runtime documentation is included only with --include-runtime-docs; dependency caches and generated runtime previews are excluded.'
  };
  for (const [flag, value] of [['--export-external', records], ['--report', report]]) {
    const index = process.argv.indexOf(flag);
    if (index >= 0) {
      if (!process.argv[index + 1] || process.argv[index + 1].startsWith('--')) throw new Error(`${flag} needs a file path`);
      const dest = path.resolve(ROOT, process.argv[index + 1]);
      fs.mkdirSync(path.dirname(dest), {recursive: true});
      fs.writeFileSync(dest, JSON.stringify(value, null, 2) + '\n');
    }
  }
  if (report.problems.length) {
    for (const problem of report.problems) console.error(`${problem.file}: ${problem.reason}: ${problem.url}`);
    process.exitCode = 1;
  } else console.log(`PASS: ${counts.localLinks} local links, ${counts.publishedLinks} published links and ${counts.fragments} fragments across ${counts.documents} documents/assets.`);
  console.log(`External inventory: ${records.length} URLs; template/protocol links deferred: ${deferred.length}.`);
}

main().catch(error => { console.error(error); process.exitCode = 1; });
