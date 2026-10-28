const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const {ROOT,read}=require('./lib.cjs');
function csv(text) {
  return text.trim().split(/\r?\n/).map(line=>{
    const result=[];let cell='',quoted=false;
    for(let i=0;i<line.length;i++){
      if(line[i]==='"'){if(quoted&&line[i+1]==='"'){cell+='"';i++;}else quoted=!quoted;}
      else if(line[i]===','&&!quoted){result.push(cell);cell='';}else cell+=line[i];
    }
    return [...result,cell];
  });
}
const rows=csv(read('maintenance/migration/source-map.csv'));
const keys=rows.shift();
const entries=rows.map(row=>Object.fromEntries(keys.map((k,i)=>[k,row[i]])));
if(new Set(entries.map(e=>e.source_folder+'/'+e.source_path)).size!==entries.length)throw new Error('Duplicate source mapping.');
for(const row of entries){
  if(!fs.existsSync(path.join(ROOT,row.destination)))throw new Error('Missing destination '+row.destination);
  if(['copied-byte-identical','archived-original','copied'].includes(row.disposition)){
    const actual=crypto.createHash('sha256').update(fs.readFileSync(path.join(ROOT,row.destination))).digest('hex');
    if(actual!==row.source_sha256)throw new Error('Preserved file changed: '+row.destination);
  }
}
const arg=process.argv.indexOf('--sources');
if(arg>=0){
  if(!process.argv[arg+1])throw new Error('--sources requires the parent directory.');
  const parent=path.resolve(ROOT,process.argv[arg+1]);
  const actual=[];
  function scan(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=path.join(dir,e.name);if(e.isDirectory())scan(f);else actual.push(path.relative(parent,f).split(path.sep).join('/'));}}
  for(const source of new Set(entries.map(e=>e.source_folder)))scan(path.join(parent,source));
  const expected=entries.map(e=>e.source_folder+'/'+e.source_path);
  if(actual.length!==expected.length||actual.some(f=>!expected.includes(f)))throw new Error('Original source inventory changed.');
  for(const row of entries){
    const raw=fs.readFileSync(path.join(parent,row.source_folder,row.source_path));
    if(crypto.createHash('sha256').update(raw).digest('hex')!==row.source_sha256)throw new Error('Original modified: '+row.source_folder+'/'+row.source_path);
  }
  console.log('Verified all '+entries.length+' original files remain unchanged; every destination is present.');
} else console.log('Verified provenance: all '+entries.length+' source dispositions have destinations.');
module.exports={csv};
