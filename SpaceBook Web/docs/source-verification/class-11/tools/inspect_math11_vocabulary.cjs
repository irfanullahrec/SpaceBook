const fs=require('fs'),path=require('path'),vm=require('vm');
const root=path.resolve(__dirname,'..'),app=path.resolve(root,'../../..');
const c={window:{}};vm.createContext(c);vm.runInContext(fs.readFileSync(path.join(app,'js/math_11_data.js'),'utf8')+';this.words=MATH_11_WORDS',c);
const known=new Set(Object.keys(c.words));
const words=new Set();
for(let i=Number(process.argv[2]||192);i<=Number(process.argv[3]||196);i++){
 const text=fs.readFileSync(path.join(root,'math/pages/p'+i+'.txt'),'utf8');
 for(const line of text.split('\n')){
  if(!/^(p |q |qp |example |svg |box |#)/.test(line))continue;
  const en=line.split(' || ')[0].replace(/^\S+\s+(?:[^|]+\|\s*)?/,'').replace(/\$[^$]+\$/g,'');
  for(const word of en.toLowerCase().match(/[a-z]+(?:'[a-z]+)?/g)||[])if(word.length>1&&!known.has(word))words.add(word);
 }
}
console.log([...words].sort().join('\n'));
