// node tools/qa/snext.js <stream.txt> <from paragraph> <chars> : prints paragraphs from n until ~chars characters
const fs=require('fs');const L=fs.readFileSync(process.argv[2],'utf8').split('\n');let n=+process.argv[3],c=+process.argv[4],o=[],t=0;
for(let i=n-1;i<L.length&&t<c;i++){o.push(L[i]);t+=L[i].length;}
console.log(o.join('\n'));console.log('--- next from ¶'+(n+o.length));
