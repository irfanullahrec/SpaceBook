const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),ctx=vm.createContext({console});
const read=file=>fs.readFileSync(path.join(root,file),'utf8');
vm.runInContext(read('js/math_12_data.js'),ctx);
const before=vm.runInContext('JSON.stringify(MATH_12_DATA[3])',ctx);
vm.runInContext(read('js/math12_unit4_translations.js'),ctx);
const unit=vm.runInContext('MATH_12_DATA[3]',ctx),report=vm.runInContext('MATH12_UNIT4_TRANSLATION_REPORT',ctx);
assert(report);
const strip=value=>{
  if(Array.isArray(value))return value.map(strip);
  if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).filter(([key])=>!key.endsWith('Translations')).map(([key,val])=>[key,strip(val)]));
  return value;
};
assert.deepEqual(strip(JSON.parse(JSON.stringify(unit))),strip(JSON.parse(before)),'English or mathematical source data changed');
const math=text=>Array.from(String(text).matchAll(/\\\([\s\S]*?\\\)/g),m=>m[0]).sort();
const rows=[];
for(const section of unit.sections){
  if(!report.completedSectionIds.includes(section.id))continue;
  function inspect(value){
    if(!value||typeof value!=='object')return;
    if(Array.isArray(value)){value.forEach(inspect);return;}
    if(value.en&&value.ur&&value.ps){
      if(!value.mathematicalNotation){
        assert(/[\u0600-\u06ff]/.test(value.ur),'Missing Urdu text: '+value.en);
        assert(/[\u0600-\u06ff]/.test(value.ps),'Missing Pashto text: '+value.en);
      }
      assert.deepEqual(math(value.ur),math(value.en),'Urdu formula changed: '+value.en);
      assert.deepEqual(math(value.ps),math(value.en),'Pashto formula changed: '+value.en);
      rows.push(value);
    }
    Object.values(value).forEach(inspect);
  }
  inspect(section.sourceBlocks);
}
for(const section of report.sections){
  assert.equal(section.missing.length,0,'Untranslated fields in '+section.id);
  assert.equal(section.fields,section.translatedFields);
}
const snapshot=JSON.stringify(unit);
vm.runInContext(read('js/math12_unit4_translations.js'),ctx);
assert.equal(JSON.stringify(unit),snapshot,'Repeated translation load changed content');
const result={date:new Date().toISOString(),passed:true,scope:report.scope,completedSectionIds:report.completedSectionIds,nextSection:report.nextSection,sections:report.sections,checkedTranslationRows:rows.length,checks:['source text/formula preservation','every targeted field translated','Urdu and Pashto script','inline LaTeX preserved','repeated load preserves data'],limitations:'These checks validate attachment, script and formula preservation. They do not replace a language review or integrated browser testing.'};
fs.writeFileSync(path.join(root,'docs/source-verification/class-12/math12-unit4-translations.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
