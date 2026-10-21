const fs=require('fs');const p='js/vr_auto.js';let s=fs.readFileSync(p,'utf8');
const rep=(a,b)=>{if(!s.includes(a))throw new Error('missing: '+a.slice(0,60));s=s.replace(a,()=>b);};
rep("const SYM = { '−': '-',", String.raw`const SYM = { 'Ω': '\Omega ', '−': '-',`);
rep("  /* ---------- plain unicode math -> TeX (null when anything is not understood) ---------- */\n", String.raw`  /* multi-letter unit symbols are read as units only straight after a number or another unit ("12.8 kg", "3 m s⁻¹") */
  const UNITN = new Set(['kg', 'cm', 'mm', 'km', 'Hz', 'Pa', 'eV', 'keV', 'MeV', 'mol', 'rad', 'kW', 'MW', 'kJ', 'kN', 'ms', 'ns', 'dm', 'mg', 'mL', 'kPa', 'Wb', 'kHz', 'MHz', 'GHz', 'nm', 'dB']);
  const unitTok = tk => { const t = tk.replace(/^[(]+|[).,;:]+$/g, ''); const m = /^([A-Za-z]+)[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]*$/.exec(t); return !!m && UNITN.has(m[1]); };
  const numEnd = tk => /[0-9)]$/.test(tk.replace(/[.,;:]+$/, ''));
  /* ---------- plain unicode math -> TeX (null when anything is not understood) ---------- */
`);
rep("        if (m.length > 1) return null;             // a real word, not maths", String.raw`        if (UNITN.has(m) && /[0-9)}]\s*$|mathrm\{[A-Za-z]+\}\s*$/.test(out)) { out += (/\s$/.test(out) ? '' : ' ') + '\,\mathrm{' + m + '}'; i += m.length; continue; }
        if (m.length > 1) return null;             // a real word, not maths`);
rep("    toks.forEach(tk => { if (isWord(tk)) flush(); else cur.push(tk); });", String.raw`    let prevTk = '';
    toks.forEach(tk => { if (isWord(tk) && !(unitTok(tk) && cur.length && (numEnd(prevTk) || unitTok(prevTk)))) flush(); else cur.push(tk); prevTk = tk; });`);
fs.writeFileSync(p,s);
