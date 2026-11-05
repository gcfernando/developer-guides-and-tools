/* Actual computed text/background contrast sampling; not a full WCAG audit.
 * Run: node tools/contrast.cjs [--staged] [--out PATH]
 * Uses development-only Playwright and axe from the repository's .runtime.
 */
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '..');
const repo = path.resolve(root, '../..');
const {chromium} = require(path.join(repo, '.runtime/atlas-tools/node_modules/playwright'));
const axe = fs.readFileSync(path.join(repo, '.runtime/atlas-tools/node_modules/axe-core/axe.min.js'), 'utf8');
const staged = process.argv.includes('--staged');
const outIndex = process.argv.indexOf('--out');
const out = outIndex >= 0 ? path.resolve(process.argv[outIndex+1]) : path.join(root, '.runtime/contrast.json');
let browser;
(async () => {
  browser = await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', headless:true});
  const page = await browser.newPage({viewport:{width:1280,height:900}});
  await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
  if (staged) {
    await page.evaluate(css => {
      document.querySelectorAll('style').forEach(node => node.remove());
      const style = document.createElement('style'); style.textContent = css; document.head.append(style);
    }, fs.readFileSync(path.join(root, 'source/atlas.css'),'utf8'));
    if (!await page.evaluate(() => !!window.AtlasExperience)) {
      await page.addScriptTag({content:fs.readFileSync(path.join(root, 'source/experience.js'),'utf8')});
      await page.evaluate(() => window.AtlasExperience.update(''));
    }
  }
  await page.evaluate(() => {
    for(const section of document.querySelectorAll("main > .section"))section.style.contentVisibility="visible";
    document.querySelectorAll('.topic-card').forEach(card => window.AtlasExperience?.hydrate(card));
    document.querySelectorAll('template[data-path-body]').forEach(t => {t.parentElement.append(t.content); t.remove();});
    document.querySelectorAll('main details').forEach(node => node.open = true);
    document.querySelectorAll('.lesson,.topic-card,.path-item').forEach(node => node.hidden = false);
  });
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  await page.evaluate(() => { document.querySelectorAll('.session-plan').forEach(node => {const t=node.querySelector('template[data-session-body]');if(t){node.append(t.content);t.remove();}}); });
  await page.addScriptTag({content:axe});
  const fingerprint = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
  await page.keyboard.press('Tab');
  const result = {browser:{name:'Microsoft Edge',version:await browser.version()},page_sha256:fingerprint(path.join(root,'index.html')),css_sha256:fingerprint(path.join(root,'source/atlas.css')),staged, viewport:1280, exclusions:['Decorative text within aria-hidden=true (including the brand emoji and search magnifier) is excluded from text contrast sampling.'], themes:{}};
  for (const theme of ['light','dark']) {
    await page.evaluate(t => document.documentElement.dataset.theme=t, theme);
    result.themes[theme] = await page.evaluate(() => {
      const parse = value => {value=value.trim();if(/^#[0-9a-f]{6}$/i.test(value))return [1,3,5].map(i=>parseInt(value.slice(i,i+2),16)).concat(1);return (value.match(/[\d.]+/g)||[]).map(Number);};
      const composite = (front,back) => {const a=front[3]??1;return [0,1,2].map(i=>front[i]*a+back[i]*(1-a)).concat(1);};
      const linear = v => {v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4;};
      const lum = rgb => .2126*linear(rgb[0])+.7152*linear(rgb[1])+.0722*linear(rgb[2]);
      const ratio = (a,b) => {let x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);};
      function effective(node) {
        const lineage=[];for(let p=node;p;p=p.parentElement)lineage.unshift(p);
        let background=[255,255,255,1],gradient=false;
        for(const p of lineage){const s=getComputedStyle(p);background=composite(parse(s.backgroundColor),background);gradient ||= s.backgroundImage !== 'none';}
        return {background,gradient};
      }
      const pairs=new Map(), low=[];
      for(const node of document.body.querySelectorAll('*')) {
        if(![...node.childNodes].some(n=>n.nodeType===Node.TEXT_NODE && n.textContent.trim()))continue;
        // Decorative content explicitly hidden from assistive technology is not
        // a text-contrast requirement; controls retain their accessible labels.
        if(node.closest('[aria-hidden="true"]'))continue;
        if(!node.checkVisibility({visibilityProperty:true,opacityProperty:true}))continue;
        const s=getComputedStyle(node),b=effective(node),fg=composite(parse(s.color),b.background);
        const size=parseFloat(s.fontSize),weight=parseFloat(s.fontWeight)||400;
        const threshold=size>=24||(size>=18.66&&weight>=700)?3:4.5;
        const r=ratio(fg,b.background);
        const item={selector:node.id?'#'+node.id:node.tagName.toLowerCase()+(node.className?'.'+String(node.className).trim().replace(/\s+/g,'.'):''),foreground:s.color,background:b.background.slice(0,3).map(Math.round),size,weight,ratio:+r.toFixed(3),threshold,gradient:b.gradient};
        const key=[s.color,item.background,size,weight,b.gradient].join('|');
        if(!pairs.has(key))pairs.set(key,item);
        if(r<threshold&&!b.gradient)low.push(item);
      }
      const ui = new Map();
      const recordUI = (kind,node,foreground,background,threshold=3) => {
        const r=ratio(foreground,background);
        const item={kind,selector:node.id?'#'+node.id:node.tagName.toLowerCase()+'.'+String(node.className).trim().replace(/\s+/g,'.'),foreground:foreground.slice(0,3),background:background.slice(0,3),ratio:+r.toFixed(3),threshold};
        ui.set([kind,item.foreground,item.background].join('|'),item);
      };
      const controls=[...document.querySelectorAll('select,#site-search,input[type="search"],textarea,button.iconbtn,button.topic-done-btn')].filter(node=>!node.disabled&&!node.closest('[aria-hidden="true"]')&&node.checkVisibility({visibilityProperty:true}));
      for(const node of controls){const style=getComputedStyle(node),outside=effective(node.parentElement).background;
        if(parseFloat(style.borderTopWidth)>0)recordUI('control boundary',node,composite(parse(style.borderTopColor),outside),outside);
        if(node.hasAttribute('placeholder'))recordUI('placeholder',node,composite(parse(getComputedStyle(node,'::placeholder').color),effective(node).background),effective(node).background,4.5);
      }
      const done=document.querySelector('.topic-done-btn');
      if(done){done.classList.add('is-complete');const st=getComputedStyle(done),outside=effective(done.parentElement).background;recordUI('pressed topic boundary',done,composite(parse(st.borderTopColor),outside),outside);done.classList.remove('is-complete');}
      for(const selector of ['#theme-btn','#role-home','#site-search','#lesson-focus','#library-level','#study-note','.topic-done-btn','main summary','.onboarding-choices a']){
        const node=document.querySelector(selector);if(!node||!node.checkVisibility({visibilityProperty:true}))continue;
        node.focus({preventScroll:true});const style=getComputedStyle(node),outside=effective(node.parentElement).background;
        if(style.outlineStyle!=='none')recordUI('keyboard focus outline',node,composite(parse(style.outlineColor),outside),outside);
      }
      const progress=document.querySelector('progress');
      if(progress){const style=getComputedStyle(progress),fill=parse(getComputedStyle(document.documentElement).getPropertyValue('--progress-fill'));recordUI('progress fill versus track (resolved declared colors)',progress,fill,parse(style.backgroundColor));}
      const checkbox=document.querySelector('input[type="checkbox"]');
      if(checkbox){const color=parse(getComputedStyle(checkbox).accentColor);if(color.length>=3)recordUI('native checkbox accent versus surrounding surface',checkbox,color,effective(checkbox.parentElement).background);}
      return {uiPairs:[...ui.values()],lowUI:[...ui.values()].filter(item=>item.ratio<item.threshold),sampledPairs:[...pairs.values()],lowPairs:low,gradientPairs:[...pairs.values()].filter(pair=>pair.gradient),gradientLimit:'Gradient pairs require a pixel-level check; they are listed separately and are not counted as verified AA by this sampler.'};
    });
    const axeResult = await page.evaluate(async () => axe.run(document, {runOnly:{type:'rule',values:['color-contrast']}}));
    result.themes[theme].axe = axeResult.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))}));
    result.themes[theme].axeIncomplete = axeResult.incomplete.map(v=>({id:v.id,nodes:v.nodes.length, details:v.nodes.map(n=>({target:n.target,summary:n.failureSummary,related:n.any.map(a=>({message:a.message,data:a.data}))}))}));
  }
  result.deadSelectors = await page.evaluate(() => {
    const dead=new Set(),invalid=[];
    const dynamic = /:hover|:focus|:target|:checked|:active|:has\(|aria-selected|is-complete|is-selected|is-open|has-next-step/;
    function visit(rules){for(const rule of rules){if(rule.cssRules)visit(rule.cssRules);else if(rule.selectorText){for(const original of rule.selectorText.split(/,(?![^()]*\))/)){
      if(dynamic.test(original)||original.includes('::'))continue;
      const selector=original.replace(/\[data-theme="(?:light|dark)"\]\s*/g,'').replace(/\[data-onboarding="seen"\]\s*/g,'');
      try {if(!document.querySelector(selector))dead.add(original.trim());}catch {invalid.push(original.trim());}
    }}}}
    for(const sheet of document.styleSheets)visit(sheet.cssRules);
    return {dead:[...dead],invalid};
  });
  fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(result,null,2));
  for(const [theme,data] of Object.entries(result.themes)) console.log(theme,JSON.stringify({sampled:data.sampledPairs.length,belowThreshold:data.lowPairs.length,uiPairs:data.uiPairs.length,lowUI:data.lowUI,gradientPairs:data.gradientPairs.length,axeViolations:data.axe.length,axeIncomplete:data.axeIncomplete.map(item=>({id:item.id,nodes:item.nodes}))}));
  console.log('deadSelectors',JSON.stringify(result.deadSelectors));console.log('report',out);
  if(Object.values(result.themes).some(theme=>theme.lowPairs.length||theme.lowUI.length||theme.axe.length))process.exitCode=1;
})().catch(error=>{console.error(error);process.exitCode=1;}).finally(async()=>{if(browser)await browser.close();});
