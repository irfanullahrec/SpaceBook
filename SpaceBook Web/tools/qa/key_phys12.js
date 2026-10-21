// Adds hand-derived keys to Class 12 Physics textbook MCQs that print no answer (see docs/QA_classes_11_12.md).
const fs=require('fs');const f='js/phys_12_data.js';let s=fs.readFileSync(f,'utf8');
const K={ '11-q1':'C','11-q2':'B','11-q3':'B','11-q4':'C','11-q5':'B','11-q6':'C','11-q8':'A','11-q9':'D','11-q10':'A','11-q13':'A',
 '19-mcq-q1':'B','19-mcq-q2':'A','19-mcq-q3':'C','19-mcq-q4':'C','19-mcq-q5':'C','19-mcq-q6':'C','19-mcq-q7':'B','19-mcq-q8':'A','19-mcq-q9':'C','19-mcq-q10':'C','19-mcq-q11':'D','19-mcq-q12':'C','19-mcq-q13':'C','19-mcq-q14':'B'};
const NOTE={'11-q5':' Volt/metre is an equivalent unit; N/C is the defining form.','11-q13':' Taking W as the work done by the field (the external agent does +qΔV).'};
let n=0;
for(const [k,a] of Object.entries(K)){
 const id='"textbook-exercise-'+k+'"';const i=s.indexOf(id);if(i<0){console.log('missing',k);continue;}
 const tag='"solutionOrigin": "not_provided_in_textbook"';const j=s.indexOf(tag,i);
 const nxt=s.indexOf('"id": "textbook-exercise-',i+10);if(j<0||(nxt>0&&j>nxt)){console.log('no tag',k);continue;}
 s=s.slice(0,j)+'"answer": "'+a+'",\n          "answerOrigin": "Derived (the textbook prints no key); worked out and checked by hand.'+(NOTE[k]||'')+'",\n          '+tag+s.slice(j+tag.length);n++;}
fs.writeFileSync(f,s);console.log('keyed',n);
