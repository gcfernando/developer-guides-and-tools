const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const zlib = require('node:zlib');

function createReaderServer(target, gzip = false) {
  const directory = path.dirname(target);
  return http.createServer((req, res) => {
    let pathname;
    try { pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname); }
    catch { res.writeHead(400); res.end(); return; }
    if (pathname === '/favicon.ico') { res.writeHead(204); res.end(); return; }
    const file = pathname === '/' || pathname === '/index.html' ? target : path.resolve(directory, '.' + pathname);
    if (!file.startsWith(directory + path.sep)) { res.writeHead(403); res.end(); return; }
    fs.readFile(file, (error, data) => {
      if (error) { res.writeHead(404); res.end(); return; }
      const types = {'.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json'};
      res.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
      if (gzip && /\bgzip\b/.test(req.headers['accept-encoding'] || '')) {
        res.setHeader('Content-Encoding', 'gzip');
        res.setHeader('Vary', 'Accept-Encoding');
        res.end(zlib.gzipSync(data));
      } else res.end(data);
    });
  });
}

async function waitForReader(page) {
  if (!await page.locator('script[data-atlas-content]').count()) return;
  await page.waitForFunction(() => ['true', 'error'].includes(document.documentElement.dataset.atlasReady));
  if (await page.evaluate(() => document.documentElement.dataset.atlasReady) !== 'true') {
    throw new Error(await page.locator('#atlas-load-status').textContent());
  }
}

module.exports = {createReaderServer, waitForReader};
