const fs=require('fs');const p='js/vr_auto.js';let s=fs.readFileSync(p,'utf8');
const rep=(a,b)=>{if(!s.includes(a))throw new Error('missing: '+a.slice(0,50));s=s.replace(a,()=>b);};
rep("  /* ---------- plain unicode math -> TeX (null when anything is not understood) ---------- */\n",
"  /* units written after a number (\"12.8 V\", \"5 × 60 s\", \"16 A·Ω\"): shown upright, the text is kept as written */\n  const UNIT1 = /^(?:V|A|W|J|C|N|m|s|g|K|T|F|H|L|S|G)$/;\n  const UNITN = new Set(['kg', 'cm', 'mm', 'km', 'Hz', 'Pa', 'eV', 'keV', 'MeV', 'mol', 'rad', 'kW', 'MW', 'kJ', 'kN', 'ms', 'ns', 'dm', 'mg', 'mL', 'kPa', 'Wb', 'cal', 'kcal', 'atm', 'kHz', 'MHz', 'GHz', 'nm', 'dB', 'cd']);\n  /* ---------- plain unicode math -> TeX (null when anything is not understood) ---------- */\n");
rep("    while (i < s.length) {\n      const ch = s[i];\n      if (SUP[ch]",
"    let unitMode = false;\n    while (i < s.length) {\n      const ch = s[i];\n      if (!(ch === ' ' || ch === '·' || ch === '/' || ch === 'Ω' || SUP[ch] !== undefined || SUB[ch] !== undefined || /[A-Za-z]/.test(ch))) unitMode = false;\n      if (unitMode && ch === 'Ω') { out += '\\,\\mathrm{\\Omega}'; i++; continue; }\n      if (SUP[ch]");
rep("        const m = /^[A-Za-z]+/.exec(s.slice(i))[0];\n        const f = FUNCS",
"        const m = /^[A-Za-z]+/.exec(s.slice(i))[0];\n        if ((unitMode || (s[i - 1] === ' ' && /[0-9]\s*$/.test(out))) && (UNIT1.test(m) || UNITN.has(m))) { out += '\\,\\mathrm{' + m + '}'; unitMode = true; i += m.length; continue; }\n        unitMode = false;\n        const f = FUNCS");
rep("      if (OPS.includes(run)) return false;\n      let r = run","      if (OPS.includes(run) || UNITN.has(run)) return false;\n      let r = run");
fs.writeFileSync(p,s);
