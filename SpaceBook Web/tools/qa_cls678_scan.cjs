// QA scan for Class 6-8 books. Usage: node tools/qa_cls678_scan.cjs [--json out.json]
const fs=require('fs'),vm=require('vm'),path=require('path');
const JS=path.join(__dirname,'..','js');
function load(f){const ctx={window:{},console,document:{},self:{}};vm.runInNewContext(fs.readFileSync(path.join(JS,f),'utf8'),ctx);return ctx;}
const out={books:{},findings:[]};
function F(book,kind,where,msg){out.findings.push({book,kind,where,msg});}
const LATIN=/[A-Za-z]{4,}/, ARAB=/[\u0600-\u06FF]/;
function checkText(book,where,s,field){
  if(typeof s!=='string')return;
  if(/\uFFFD/.test(s))F(book,'fffd',where,field+': replacement char');
  if(/\?\?/.test(s)&&!/\?\?\?/.test(s)===false)F(book,'qmarks',where,field+': ???');
  if(/\|\|/.test(s)&&field!=='cell')F(book,'pipes',where,field+': stray || in '+s.slice(0,50));
  const stars=(s.match(/\*\*/g)||[]).length; if(stars%2)F(book,'stars',where,field+': unbalanced ** '+s.slice(0,60));
  const dollars=(s.replace(/\\$/g,'').match(/\$/g)||[]).length; if(dollars%2)F(book,'dollar',where,field+': unbalanced $ '+s.slice(0,60));
  if(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(s))F(book,'ctrl',where,field+': control char');
  if(/\s{3,}/.test(s))F(book,'spaces',where,field+': 3+ spaces');
}
let curPdf=null;
function audit(cl,subj,B,SOL){
  const key='c'+cl+'-'+subj; const st={units:0,emptyUnits:[],pages:0,q:0,qNoSol:0,badSol:[],emptyAns:0,noUr:0,noPs:0,wideTables:0,svgNoViewBox:0,fm:0,bm:0,exercises:0,mcqNoKey:0};
  out.books[key]=st;
  const book=B.book||{}; st.reviewed=book.reviewedPdfPages; st.total=book.totalPdfPages; st.fm=(book.frontMatter||[]).length; st.bm=(book.backMatter||[]).length;
  const units=B.units||[]; st.units=units.length;
  const isRTLprimary=/^(urdu|arabic|quran|pashto|isl|hpe|drawing)/.test(subj);
  for(const u of units){
    const uw='u'+u.number;
    let blocks=0, lesson=0;
    for(const s of u.sections||[]){ blocks+=(s.blocks||[]).length; }
    if(!blocks)st.emptyUnits.push(u.number); const es=(u.sections||[]).filter(s=>!(s.blocks||[]).length).length; if(es&&es>=(u.sections||[]).length/2)F(key,'emptysecs',uw,es+'/'+(u.sections||[]).length+' sections empty');
    if(!(u.sections||[]).length)F(key,'nosec',uw,'unit has no sections');
    for(const s of u.sections||[]) walk(s.blocks,uw+'/'+(s.id||''));
  }
  walk(book.frontMatter,'front'); walk(book.backMatter,'back');
  function walk(o,where){
    if(Array.isArray(o)){o.forEach(x=>walk(x,where));return;}
    if(!o||typeof o!=='object')return;
    if(o.t==='page'){st.pages++; curPdf=o.pdf;}
    if(o.t==='q'){st.q++; if(o.solId){ if(!SOL[o.solId])st.badSol.push(o.solId); else { const a=SOL[o.solId]; if(!a.answer&&!(a.steps&&a.steps.length)){st.emptyAns++; F(key,'emptyans',where,'solution '+o.solId+' empty');} } } else if(!o.parts||!o.parts.length){ st.qNoSol++; F(key,'q-nosol',where+' pdf'+curPdf,'q '+o.no+': '+String(o.en).slice(0,110)); } }
    if(o.t==='parts'){ for(const p of o.parts||[]){ if(p.solId){ if(!SOL[p.solId])st.badSol.push(p.solId);} else { st.qNoSol++; F(key,'part-nosol',where+' pdf'+curPdf,'part '+p.no+': '+String(p.en).slice(0,110)); } } }
    if(o.t==='exercise')st.exercises++;
    if(o.t==='table'){ const w=Math.max(0,...(o.rows||[]).map(r=>r.length)); if(w>5){st.wideTables++; F(key,'widetable',where,w+' columns');} for(const r of o.rows||[])for(const c of r)checkText(key,where,c,'cell'); }
    if(o.t==='svg'){ if(!/viewBox=/.test(o.svg||'')){st.svgNoViewBox++;F(key,'svg-noviewbox',where,'svg without viewBox');} const m=/<svg[^>]*\swidth="(\d+)/.exec(o.svg||''); if(m&&+m[1]>420)F(key,'svg-fixedwidth',where,'width='+m[1]); }
    if(o.t==='p'||o.t==='h'){
      if(!o.en||!String(o.en).trim())F(key,'empty',where,o.t+' with empty en');
      if(o.t==='p'&&!isRTLprimary&&o.en&&LATIN.test(o.en)&&o.en.length>15){ if(!o.ur){st.noUr++;} if(!o.ps){st.noPs++;} }
    }
    for(const f of ['en','ur','ps','ar']) if(typeof o[f]==='string')checkText(key,where,o[f],f);
    for(const k in o){ if(k==='svg'||k==='tex')continue; const v=o[k]; if(v&&typeof v==='object')walk(v,where); }
  }
}
for(const cl of [6,7,8]){
  for(const f of fs.readdirSync(JS).filter(f=>new RegExp('_'+cl+'_data\.js$').test(f)&&!/^math/.test(f))){
    const c=load(f); const B=c.window['CLS'+cl+'_BOOKS']; const SOL=c.window.CLS6_SOLUTIONS||{};
    for(const s in B){ const bk=B[s]; const b2={units:bk.units, book:bk.book}; audit(cl,s,b2,SOL); }
  }
}
const sum={};for(const f of out.findings){const k=f.book+' '+f.kind;sum[k]=(sum[k]||0)+1;}
out.summary=sum;
if(process.argv.includes('--json'))fs.writeFileSync(process.argv[process.argv.indexOf('--json')+1],JSON.stringify(out,null,1));
console.log(JSON.stringify(out.books,null,0).replace(/\},"/g,'},\n"'));
console.log(Object.entries(sum).sort().map(([k,v])=>k+': '+v).join('\n'));
