const fs=require('fs');const p='js/vr_auto.js';let s=fs.readFileSync(p,'utf8');
const a="        if (PROD.has(m))";
if(!s.includes(a))throw 1;
s=s.replace(a,()=>"        if (m.length === 1 && 'VAWJCNmsgKTFH'.includes(m) && s[i - 1] === ' ' && /[0-9)]\s*$/.test(out)) { out += '\\,\\mathrm{' + m + '}'; i++; continue; }\n"+a);
fs.writeFileSync(p,s);
