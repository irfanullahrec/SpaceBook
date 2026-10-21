const fs=require('fs');const p='js/vr_auto.js';let s=fs.readFileSync(p,'utf8');
const rep=(a,b)=>{if(!s.includes(a))throw new Error('missing: '+a.slice(0,60));s=s.replace(a,()=>b);};
rep("  const numEnd = tk =>", "  let PROD = new Set();   // two-letter products written between two equals signs (\"V = IR = ...\", \"F = ma = ...\") read as variables\n  const numEnd = tk =>");
rep("        if (m.length > 1) return null;             // a real word, not maths", "        if (PROD.has(m)) { out += m.split('').join(' '); i += m.length; continue; }\n        if (m.length > 1) return null;             // a real word, not maths");
rep("    let prevTk = '';\n    toks.forEach(tk => { if (isWord(tk) &&", "    let prevTk = '';\n    PROD = new Set(toks.filter((tk, k) => k > 0 && toks[k - 1] === '=' && /^[A-Za-z]{2}[.,;]?$/.test(tk) && (toks[k + 1] === '=' || (k + 1 === toks.length - 0 && false))).map(tk => tk.replace(/[.,;]+$/, '')));\n    toks.forEach((tk, k) => { if (!PROD.has(tk) && isWord(tk) &&");
fs.writeFileSync(p,s);
