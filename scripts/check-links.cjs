const fs=require('node:fs');
const path=require('node:path');
const MarkdownIt=require('markdown-it');
const {parseHTML}=require('linkedom');
const {ROOT,walk,relative,read,frontMatter}=require('./lib.cjs');
const md=new MarkdownIt({html:true});
const files=walk().filter(f=>/\.(md|html)$/.test(f)&&!relative(f).startsWith('maintenance/')&&!relative(f).startsWith('scripts/')&&!relative(f).startsWith('_layouts/'));
const problems=[];
const external=new Map();
let checked=0;
for(const file of files){
  const name=relative(file);const text=read(name);
  const content=name.endsWith('.md')?md.render(frontMatter(text).body):text;
  const {document}=parseHTML(content);
  for(const el of document.querySelectorAll('[href],[src]')){
    const url=el.getAttribute('href')||el.getAttribute('src');
    if(/^https?:\/\//i.test(url)&&!['preconnect','dns-prefetch'].includes(el.getAttribute('rel'))&&!url.startsWith('https://gcfernando.github.io/developer-guides-and-tools')&&!url.startsWith('https://github.com/gcfernando/developer-guides-and-tools')){
      const clean=url.split('#')[0];
      external.set(clean,[...new Set([...(external.get(clean)||[]),name])]);
    }
    if(!url||url.startsWith('#')||/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(url)||url.includes('{{')||url.includes('{%'))continue;
    const target=decodeURIComponent(url.split(/[?#]/)[0]);
    if(!target)continue;
    checked++;
    const dest=path.resolve(path.dirname(file),target);
    if(!dest.startsWith(ROOT+path.sep)&&dest!==ROOT){problems.push(name+': escapes repository: '+url);continue;}
    if(!fs.existsSync(dest))problems.push(name+': missing '+url);
    else {
      let current=ROOT;
      for(const part of path.relative(ROOT,dest).split(path.sep).filter(Boolean)){
        if(!fs.readdirSync(current).includes(part)){problems.push(name+': path case does not match: '+url);break;}
        current=path.join(current,part);
      }
    }
  }
}
const exportIndex=process.argv.indexOf('--export-external');
if(exportIndex>=0){
  const dest=path.resolve(ROOT,process.argv[exportIndex+1]);
  fs.mkdirSync(path.dirname(dest),{recursive:true});
  fs.writeFileSync(dest,JSON.stringify([...external].map(([url,sources])=>({url,sources})),null,2)+'\n');
  console.log('Exported '+external.size+' external URLs. Planned destination URLs are checked against the local built site.');
}
if(problems.length){console.error(problems.join('\n'));process.exitCode=1;}
else console.log('PASS: '+checked+' relative file links across '+files.length+' documents and applications.');
