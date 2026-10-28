const fs=require('node:fs');
const path=require('node:path');
const {parseHTML}=require('linkedom');
const {ROOT,read,yaml}=require('./lib.cjs');
const site=path.join(ROOT,'_site');
if(!fs.existsSync(site))throw new Error('Build Jekyll before checking the site.');
const config=yaml.parse(read('_config.yml'));
const errors=[];const documents=new Map();let links=0;
function scan(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=path.join(dir,e.name);if(e.isDirectory())scan(f);else if(e.name.endsWith('.html'))documents.set(f,parseHTML(fs.readFileSync(f,'utf8')).document);}}
scan(site);
const anchors=new Map([...documents].map(([file,doc])=>[file,new Set([...doc.querySelectorAll('[id],a[name]')].flatMap(n=>[n.id,n.getAttribute('name')]).filter(Boolean))]));
function checkAnchor(file,fragment,origin,url){
  if(!fragment||fragment.startsWith(':~:text='))return;
  if(anchors.has(file)&&!anchors.get(file).has(decodeURIComponent(fragment)))errors.push(path.relative(site,origin)+': missing anchor '+url);
}
for(const [file,document] of documents){
  const canonical=document.querySelector('link[rel="canonical"]')?.getAttribute('href');
  if(!canonical||!canonical.startsWith(config.url+config.baseurl+'/'))errors.push(path.relative(site,file)+': missing or incorrect canonical URL');
  const title=document.querySelector('title')?.textContent?.trim();
  if(!title)errors.push(path.relative(site,file)+': missing title');
  if(!document.querySelector('meta[name="description"]')?.getAttribute('content'))errors.push(path.relative(site,file)+': missing description');
  for(const e of document.querySelectorAll('[href],[src]')){
    let url=e.getAttribute('href')||e.getAttribute('src');if(!url||url.startsWith('mailto:')||url.startsWith('data:'))continue;
    if(url.startsWith('#')){checkAnchor(file,url.slice(1),file,url);continue;}
    let dest;
    if(url.startsWith(config.url+config.baseurl+'/'))url=url.slice(config.url.length);
    else if(/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(url))continue;
    const clean=decodeURIComponent(url.split(/[?#]/)[0]);
    if(clean.startsWith('/')){
      if(!clean.startsWith(config.baseurl+'/'))continue;
      dest=path.join(site,clean.slice(config.baseurl.length));
    }else dest=path.resolve(path.dirname(file),clean);
    if(dest===site||dest.startsWith(site+path.sep)){
      links++;
      if(fs.existsSync(dest)&&fs.statSync(dest).isDirectory())dest=path.join(dest,'index.html');
      if(!fs.existsSync(dest))errors.push(path.relative(site,file)+': missing '+url);
      else checkAnchor(dest,url.split('#')[1],file,url);
    }
  }
}
for(const hidden of ['maintenance','scripts','tests','node_modules','.runtime'])if(fs.existsSync(path.join(site,hidden)))errors.push('Excluded directory was published: '+hidden);
if(!fs.existsSync(path.join(site,'sitemap.xml')))errors.push('Missing sitemap.xml');
if(errors.length){console.error([...new Set(errors)].join('\n'));process.exitCode=1;}else console.log('PASS: '+documents.size+' built pages, '+links+' internal links, metadata and publication exclusions.');
