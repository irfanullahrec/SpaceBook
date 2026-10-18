"""Synchronize source corrections into the existing definition/formula views."""
from class12_chemistry_opening import ROOT, OUT
import json,os,time
retire=['AH=737kJ.mol-1','AH=1476kJ.mol1','H0-5=0','(Where M = Li, Na, K, Rb, Cs)',
        'NOT FOR SALE heating. The following reactions describe the thermal decomposition of the nitrates (Where M = Be, Mg, Ca, Ba and Sr).',
        'The following reactions describe the decomposition of the carbonate (Where M = Be, Mg, Ca, Ba and Sr).','HOet oxed Jumber =']
def main():
    marker='// BEGIN CLASS12 CHEMISTRY SOURCE COMPANION SYNC';end='// END CLASS12 CHEMISTRY SOURCE COMPANION SYNC'
    block=marker+'\n{ const retiredFragments = '+json.dumps(retire,ensure_ascii=False)+''';
const chapter=CHEM_12_DATA.find(item=>item.number===13);
chapter.formulas=(chapter.formulas||[]).filter(item=>!retiredFragments.includes(item.formula));
for(const owner of CHEM_12_DATA){
 if(owner.number!==13&&owner.sections.some(section=>section.sourceClass12Chemistry))owner.sourceWordMeanings={...(chapter.sourceWordMeanings||{}),...(owner.sourceWordMeanings||{})};
 owner.formulas=owner.formulas||[];
for(const source of owner.sections.filter(section=>section.sourceClass12Chemistry)){
 let heading=source.title,number=0;
 for(const block of source.sourceLayout){
  if(block.type==='heading')heading=block.indices.map(index=>source.paras[index].text).join(' ');
  if(block.type!=='equation')continue;
  const pair=source.paras[block.indices[0]],id=source.id+'-equation-'+(++number);
  const entry={id,name:heading,formula:pair.text,note:'Source textbook equation; printed notation retained.',
   urdu:pair.urdu,pashto:pair.pashto,sourceSectionId:source.id,sourceParagraphIndices:block.indices,
   sourceReferences:source.sourceReferences,answerOrigin:'source_textbook'};
  const index=owner.formulas.findIndex(item=>item.id===id);
  if(index<0)owner.formulas.push(entry);else owner.formulas[index]=entry;
 }
}
}
const source=chapter.sections.find(section=>section.id==='chem12-u13-introduction');
const definition=chapter.definitions.find(item=>item.term==='s and p-Block Elements');
if(definition&&source){
 const pairs=[source.paras[0],source.paras[1]];
 Object.assign(definition,{def:pairs.map(pair=>pair.text).join('\\n\\n'),
  defUrdu:pairs.map(pair=>pair.urdu).join('\\n\\n'),defPashto:pairs.map(pair=>pair.pashto).join('\\n\\n'),
  sourceParagraphs:pairs,sourceSectionId:source.id,sourceParagraphIndices:[0,1],
  sourceReferences:source.sourceReferences,answerOrigin:'source_textbook_excerpt'});
}
}
'''+end+'\n'
    lock=ROOT/'tmp/class-content-shared.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    try:
        os.write(fd,f'class12-chemistry pid={os.getpid()}\n'.encode());os.close(fd);fd=None
        path=ROOT/'js/chem_12_data.js';text=path.read_text(encoding='utf-8')
        if marker in text:
            start=text.index(marker);stop=text.index(end,start)+len(end);text=text[:start]+block+text[stop:]
        else:text=text.rstrip()+'\n\n'+block
        temp=path.with_name(path.name+'.chem12.tmp');temp.write_text(text,encoding='utf-8')
        for attempt in range(6):
            try:os.replace(temp,path);break
            except PermissionError:
                if attempt==5:raise
                time.sleep(.15)
    finally:
        if fd is not None:os.close(fd)
        lock.unlink()
    (OUT/'chemistry-companion-repair.json').write_text(json.dumps({'retiredLegacyFormulaFragments':retire,'reason':'OCR fragments, prose and legend text were mislabeled as equations. Correct source equations are derived from the repaired sections. Source prose in unreviewed lessons is preserved.','definitionSourceSection':'chem12-u13-introduction'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Formula and definition views now derive the repaired Chemistry source content.')
if __name__=='__main__':main()
