const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const http=require('node:http');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
const root=path.join(__dirname,'..');
const guide=require('../guide.json');
const output=path.join(root,'test-results');
fs.mkdirSync(output,{recursive:true});
const edge='C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const executable=process.env.GUIDE_BROWSER_PATH || (fs.existsSync(edge)?edge:undefined);
const report={checks:[],errors:[],scope:'Standalone reader only; isolated browser; no add-on installations, personal profile, live account or real clipboard used.'};
async function check(name,work){try{await work();report.checks.push({name,pass:true});console.log('PASS '+name);}catch(error){report.checks.push({name,pass:false,error:error.stack});console.error('FAIL '+name+': '+error.message);}}
function linear(v){v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4;}
function luminance(rgb){return rgb.map(linear).reduce((s,x,i)=>s+x*[.2126,.7152,.0722][i],0);}
function ratio(a,b){const x=luminance(a),y=luminance(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);}
(async()=>{
 const server=http.createServer((req,res)=>{if(req.url?.split('?')[0]!=='/index.html'){res.writeHead(404);res.end();return;}res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(path.join(root,'index.html')));});
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 let browser;
 try{
  browser=await chromium.launch({headless:true,...(executable?{executablePath:executable}:{})});
  for(const protocol of ['http','file']){
   const url=protocol==='file'?pathToFileURL(path.join(root,'index.html')).href:'http://127.0.0.1:'+server.address().port+'/index.html';
   const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light',reducedMotion:'reduce',offline:protocol==='file'});
   await context.addInitScript(()=>{window.__copied=[];Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async text=>{window.__copied.push(text);}}});});
   const page=await context.newPage();page.on('pageerror',error=>report.errors.push(error.message));
   await page.goto(url);
   await check(protocol+': all cards and comparison/nav entries',async()=>{
    assert.equal(await page.locator('.tool-card').count(),39);
    assert.equal(await page.locator('.nav a:visible').count(),39);
    assert.equal(await page.locator('.tool-card:visible').count(),39);
    assert.equal(await page.locator('#count').textContent(),'39 add-ons shown');
   });
   await check(protocol+': compatibility, counts and warnings for every client',async()=>{
    for(const client of ['claude','codex','copilot','vscode','canvas']){
     await page.locator('#clientFilter').selectOption(client);
     const expected=guide.cards.filter(c=>c.clients[client].status==='documented').length;
     assert.equal(await page.locator('.tool-card:visible').count(),expected);
     assert.equal(await page.locator('.nav a:visible').count(),expected);
     assert.equal(await page.locator('#count').textContent(),expected+' add-ons shown');
     const common=await page.locator('.tool-card:visible').evaluateAll(nodes=>nodes.every(n=>!n.querySelector('.card-shared>.warning').hidden && getComputedStyle(n.querySelector('.card-shared>.warning')).display!=='none'));
     assert.ok(common);
     assert.equal(await page.locator('.client-section:visible:not([data-client="'+client+'"])').count(),0);
    }
   });
   await check(protocol+': explicit unverified opt-in excludes unavailable',async()=>{
    await page.locator('#clientFilter').selectOption('copilot');
    await page.locator('#includeUnverified').check();
    const expected=guide.cards.filter(c=>['documented','unverified'].includes(c.clients.copilot.status)).length;
    assert.equal(await page.locator('.tool-card:visible').count(),expected);
    assert.equal(await page.locator('#card-chronicle-stats-my-ai-usage').isVisible(),false);
    assert.ok(await page.locator('.unverified-notice:visible').count()>0);
   });
   await check(protocol+': search synchronizes nav and matrix; empty/reset',async()=>{
    await page.locator('#reset').click();await page.locator('#query').fill('sonarqube');
    assert.equal(await page.locator('.tool-card:visible').count(),1);
    assert.equal(await page.locator('.nav a:visible').count(),1);
    await page.locator('#comparison').evaluate(n=>{n.open=true;});
    assert.equal(await page.locator('tr[data-card]:visible').count(),1);
    await page.locator('#query').fill('__missing_742__');
    assert.ok(await page.locator('#empty').isVisible());assert.equal(await page.locator('.nav a:visible').count(),0);
    await page.locator('#emptyReset').click();assert.equal(await page.locator('.tool-card:visible').count(),39);
   });
   await check(protocol+': search excludes hidden client text',async()=>{
    await page.locator('#clientFilter').selectOption('claude');await page.locator('#query').fill('serena setup codex');
    assert.equal(await page.locator('.tool-card:visible').count(),0);
    await page.locator('#reset').click();
   });
   await check(protocol+': direct hash reveals hidden target; legacy and malformed hashes',async()=>{
    await page.locator('#clientFilter').selectOption('claude');await page.locator('#query').fill('headroom');
    await page.evaluate(()=>{location.hash='card-figma-codex-plugin';});
    await page.waitForFunction(()=>!document.getElementById('card-figma-codex-plugin').hidden);
    assert.equal(await page.locator('#query').inputValue(),'');
    assert.equal(await page.locator('#card-figma-codex-plugin').evaluate(n=>document.activeElement===n),true);
    await page.goto(url+'#documentation-and-verification-notes');
    await page.waitForFunction(()=>{const r=document.getElementById('documentation-and-verification-notes').getBoundingClientRect();return r.top<innerHeight && r.bottom>0;});
    await page.goto(url+'#headroom');
    assert.ok(await page.locator('#card-headroom').isVisible());
    await page.goto(url+'#%E0%A4%A');
   });
   await check(protocol+': copied text and manual fallback',async()=>{
    await page.goto(url);const button=page.locator('.command .copy').first();
    await button.click();assert.equal(await button.textContent(),'Copied');
    const expected=await page.locator('.command code').first().textContent();
    assert.equal(await page.evaluate(()=>window.__copied.at(-1)),expected);
    await page.evaluate(()=>{navigator.clipboard.writeText=async()=>{throw new Error('Clipboard denied');};});
    await button.click();assert.match(await button.textContent(),/Selected/);
    // Browser selection serializes a terminal block's final layout newline differently.
    assert.equal(await page.evaluate(()=>getSelection().toString().trimEnd()),expected.trimEnd());
   });
   await check(protocol+': theme persists, controls and text meet contrast',async()=>{
    for(const dark of [true,false]){
     const current=await page.locator('body').evaluate(n=>n.classList.contains('dark'));
     if(current!==dark)await page.locator('#theme').click();
     assert.equal(await page.locator('#theme').getAttribute('aria-pressed'),String(dark));
     for(const selector of ['.instructions','.help','.metadata','.warning','.sidebar label','#theme','.command-bar','h2','a']){
      const colors=await page.locator(selector).first().evaluate(n=>{
       const fg=getComputedStyle(n).color.match(/[\d.]+/g).slice(0,3).map(Number);let p=n,bg;
       while(p){const c=getComputedStyle(p).backgroundColor;if(c!=='rgba(0, 0, 0, 0)' && c!=='transparent'){bg=c.match(/[\d.]+/g).slice(0,3).map(Number);break;}p=p.parentElement;}
       return {fg,bg};
      });
      assert.ok(colors.bg,selector);assert.ok(ratio(colors.fg,colors.bg)>=4.5,selector+' contrast '+ratio(colors.fg,colors.bg));
     }
    }
    await page.locator('#theme').click();await page.reload();assert.equal(await page.locator('#theme').getAttribute('aria-pressed'),'true');
   });
   await check(protocol+': keyboard skip link, reduced motion and mobile layout',async()=>{
    await page.goto(url);await page.keyboard.press('Tab');assert.equal(await page.locator('.skip').evaluate(n=>document.activeElement===n),true);
    await page.keyboard.press('Enter');assert.equal(await page.locator('#main').evaluate(n=>document.activeElement===n),true);
    assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior),'auto');
    await page.setViewportSize({width:390,height:844});
    await page.locator('#clientFilter').selectOption('vscode');
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
    await page.screenshot({path:path.join(output,'reader-'+protocol+'-mobile.png')});
    await page.setViewportSize({width:1440,height:1000});
   });
   await context.close();
  }
  await check('blocked storage does not prevent initialization',async()=>{
   const context=await browser.newContext();await context.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw new Error('Storage blocked');}});});
   const page=await context.newPage();await page.goto(pathToFileURL(path.join(root,'index.html')).href);
   await page.locator('#theme').click();assert.equal(await page.locator('.tool-card:visible').count(),39);await context.close();
  });
 }catch(error){report.errors.push(error.stack);console.error(error);}finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));fs.writeFileSync(path.join(output,'browser-report.json'),JSON.stringify(report,null,2));}
 assert.equal(report.errors.length,0,report.errors.join('\n'));assert.equal(report.checks.length,19);assert.ok(report.checks.every(c=>c.pass),'Browser checks failed; see test-results/browser-report.json');
})().catch(error=>{console.error(error);process.exitCode=1;});
