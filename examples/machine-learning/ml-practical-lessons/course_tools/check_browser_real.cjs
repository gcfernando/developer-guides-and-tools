// Real Chromium checks. No browser package is installed by this script.
// Set ML_COURSE_BROWSER to a Chrome/Edge executable when autodetection is insufficient.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const os = require('node:os');
const path = require('node:path');
const {spawn} = require('node:child_process');
const root = path.resolve(__dirname, '..');
const candidates = [process.env.ML_COURSE_BROWSER,
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome'].filter(Boolean);
const executable = candidates.find(p => fs.existsSync(p));
if (!executable) {console.error('Real browser check unavailable: set ML_COURSE_BROWSER.'); process.exit(2);}
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'ml-real-browser-'));
let browser, server, socket;let browserErrors='';

async function main() {
  server = http.createServer((request, response) => {
    const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
    const file = path.resolve(root, '.' + pathname);
    if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
      response.writeHead(404); response.end('Not found'); return;
    }
    const types = {'.html':'text/html; charset=utf-8', '.png':'image/png', '.csv':'text/csv; charset=utf-8'};
    response.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
    fs.createReadStream(file).pipe(response);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const address = `http://127.0.0.1:${server.address().port}`;
  browser = spawn(executable, ['--headless', '--disable-gpu', '--disable-software-rasterizer', '--no-first-run', '--no-default-browser-check',
    '--remote-debugging-port=0', '--user-data-dir=' + temporary, 'about:blank'],
    {stdio:['ignore','ignore','pipe'], windowsHide:true});
  browser.stderr.on('data',chunk=>{browserErrors=(browserErrors+chunk).slice(-4000)});
  browser.on('error',error=>console.error('Browser launch failed:',error.message));
  const active = path.join(temporary, 'DevToolsActivePort');
  for (let i=0; i<150 && !fs.existsSync(active); i++) await delay(100);
  assert(fs.existsSync(active), 'The browser did not expose its debugging port.');
  const port = fs.readFileSync(active,'utf8').split('\n')[0];
  console.log('Browser debugging port: '+port);
  const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, {method:'PUT',signal:AbortSignal.timeout(15000)})).json();
  socket = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve,reject) => {const timeout=setTimeout(()=>reject(Error('Browser socket did not open.')),15000);socket.addEventListener('open',()=>{clearTimeout(timeout);resolve()},{once:true});socket.addEventListener('error',reject,{once:true});});
  let sequence=0; const pending=new Map(); const exceptions=[];
  socket.addEventListener('message', event => {
    const message=JSON.parse(event.data);
    if (message.id) {const entry=pending.get(message.id); if(entry){pending.delete(message.id);message.error?entry.reject(Error(message.error.message)):entry.resolve(message.result);}}
    if (message.method==='Runtime.exceptionThrown') exceptions.push(message.params.exceptionDetails.text);
  });
  const send=(method,params={}) => new Promise((resolve,reject) => {
    const id=++sequence;const timeout=setTimeout(()=>{pending.delete(id);reject(Error('Browser timed out: '+method));},45000);
    pending.set(id,{resolve:value=>{clearTimeout(timeout);resolve(value)},reject:error=>{clearTimeout(timeout);reject(error)}});socket.send(JSON.stringify({id,method,params}));
  });
  const evaluate=async expression => {
    const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});
    if (result.exceptionDetails) throw Error(JSON.stringify(result.exceptionDetails));
    return result.result.value;
  };
  await send('Page.enable');await send('Runtime.enable');
  async function open(file,width=320) {
    await send('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:false});
    await send('Page.navigate',{url:address+'/'+file});
    for(let i=0;i<100;i++){try{if(await evaluate(`location.pathname===${JSON.stringify('/'+file)} && document.readyState === 'complete'`))break;}catch(error){if(!/context|navigat/i.test(error.message))throw error;}await delay(100);}
    await evaluate('Promise.all([...document.images].map(image => image.decode().catch(() => {})))');
    await delay(100);
  }
  const report={browser:executable,checks:[],limits:['Automated browser checks are not a screen-reader or beginner study.']};
  for(const [file,width] of [['START-HERE.html',320],['LEARNING-PATH.html',320],['Data-Science-and-Machine-Learning.html',320],['Data-Science-and-Machine-Learning.html',1280]]) {
    console.log('Checking '+file+' at '+width+' CSS px.');
    await open(file,width);
    const stats=await evaluate(`({width:innerWidth,pageWidth:document.documentElement.scrollWidth,brokenImages:[...document.images].filter(i=>i.hasAttribute('src')&&!i.complete||i.hasAttribute('src')&&i.naturalWidth===0).map(i=>i.getAttribute('src')),visuals:document.querySelectorAll('.teaching-visual').length,fullSizeButtons:document.querySelectorAll('[data-open-visual]').length,focusTables:[...document.querySelectorAll('.table-frame')].filter(t=>t.tabIndex===0).length})`);
    assert(stats.pageWidth<=width+2,`${file} at ${width}px has page-wide horizontal scrolling: ${stats.pageWidth}`);
    assert.equal(stats.brokenImages.length,0,JSON.stringify(stats.brokenImages));
    if(file.startsWith('LEARNING')) {
      const names=await evaluate(`[...document.querySelectorAll('input[data-course-check]')].map(i=>i.getAttribute('aria-label'))`);
      assert(names.length>0);assert.equal(new Set(names).size,names.length,'Progress controls need distinct module names.');
    }
    if(file.startsWith('Data-')) {
      assert(stats.visuals>=72,'Expected every workbook image to have teaching support.');
      await evaluate(`document.querySelector('[data-open-visual]').click()`);
      assert(await evaluate(`document.getElementById('visual-dialog').open`));
      assert(await evaluate(`document.activeElement.hasAttribute('data-close-visual')`));
      await send('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape',windowsVirtualKeyCode:27});
      await send('Input.dispatchKeyEvent',{type:'keyUp',key:'Escape',code:'Escape',windowsVirtualKeyCode:27});
      await delay(100);
      assert(!(await evaluate(`document.getElementById('visual-dialog').open`)));
      assert(await evaluate(`document.activeElement.hasAttribute('data-open-visual')`),'Closing a figure should return focus to its button.');
      const labels=await evaluate(`[...document.querySelectorAll('button.copy')].map(b=>b.textContent)`);
      assert(labels.includes('Copy terminal command')&&labels.includes('Copy code example')&&labels.includes('Copy example output'));
    }
    report.checks.push({file,...stats});
  }
  await open('START-HERE.html',320);
  await evaluate(`document.documentElement.style.fontSize='200%';`);
  assert(await evaluate(`document.documentElement.scrollWidth<=innerWidth+2`),'Text enlargement should not create page-wide horizontal scrolling.');
  report.checks.push({check:'200% root text at 320 CSS px',passed:true});
  assert.equal(exceptions.length,0,'Browser runtime errors: '+exceptions.join('; '));
  fs.writeFileSync(path.join(root,'course-review','browser-checks.json'),JSON.stringify(report,null,2)+'\n');
  console.log('Real browser checks passed: 320/1280 CSS px, image loading, distinct controls, dialog keyboard/focus, copy labels, 200% root text.');
}

main().catch(error => {const reason=error?.stack||String(error);console.error(reason);fs.writeFileSync(path.join(root,'course-review','browser-checks.json'),JSON.stringify({checked_at_utc:new Date().toISOString(),browser:executable,status:'unverified: browser check did not complete',error:reason,browser_diagnostics:browserErrors,limits:['No passing real-browser result is claimed. Structural page checks run separately.']},null,2)+'\n');process.exitCode=1;}).finally(async () => {
  try{if(socket)socket.close()}catch{}if(browser){browser.kill();await delay(300);}if(server){server.closeAllConnections();server.close();}
  // The target is the exact unique directory created above, never a supplied path.
  try{assert.equal(path.dirname(path.resolve(temporary)),path.resolve(os.tmpdir()));assert(path.basename(temporary).startsWith('ml-real-browser-'));fs.rmSync(temporary,{recursive:true,force:true,maxRetries:5,retryDelay:200});}catch(error){console.error('Temporary browser profile retained:',temporary,error.message);}
});
