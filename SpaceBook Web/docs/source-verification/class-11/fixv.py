p='verify_stat_pages.cjs'
lines=open(p,encoding='utf-8').read().split('\n')
for i,l in enumerate(lines):
    if l.startswith("  if(expected.paras.some(p=>vocabTerms"):
        lines[i]="  if(expected.paras.some(p=>vocabTerms.some(term=>(' '+p.en.toLowerCase().replace(/[^a-z0-9]+/g,' ')+' ').includes(' '+term.toLowerCase()+' '))))assert(lesson.includes('popovertarget='),'Interactive vocabulary available');"
open(p,'w',encoding='utf-8').write('\n'.join(lines))
