const fs = require('node:fs');
const path = require('node:path');
const yaml = require('yaml');
const ROOT = path.resolve(__dirname, '..');
const excluded = new Set(['.git', 'node_modules', '_site', '.runtime', 'artifacts', 'vendor', '.bundle', '.jekyll-cache', '.sass-cache', '__pycache__']);
function walk(dir = ROOT) {
  return fs.readdirSync(dir, {withFileTypes:true}).flatMap(entry => {
    if (excluded.has(entry.name)) return [];
    const name=path.join(dir,entry.name);
    return entry.isDirectory()?walk(name):[name];
  });
}
function relative(file) { return path.relative(ROOT,file).split(path.sep).join('/'); }
function read(file) { return fs.readFileSync(path.resolve(ROOT,file),'utf8').replace(/^\uFEFF/,'').replace(/\r\n/g,'\n'); }
function frontMatter(text) {
  const match=text.match(/^---\n([\s\S]*?)\n---(?:\n|$)/);
  return {data:match?yaml.parse(match[1]):{},body:match?text.slice(match[0].length):text};
}
function htmlEscape(text) {return String(text).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function output(file,text,check) {
  const dest=path.resolve(ROOT,file);
  if(check) {
    if(!fs.existsSync(dest)||read(file)!==text) throw new Error('Generated file is stale: '+file);
  } else {
    fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,text);
  }
}
module.exports={ROOT,walk,relative,read,frontMatter,htmlEscape,output,yaml};
