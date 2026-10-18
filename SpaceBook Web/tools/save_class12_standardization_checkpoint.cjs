/* Save a fresh, bounded checkpoint without altering earlier book audits. */
const fs=require('fs'),path=require('path'),vm=require('vm');const root=path.resolve(__dirname,'..');
const read=f=>fs.readFileSync(path.join(root,f),'utf8');const s={};vm.createContext(s);
const mathFiles=['math_12_data','math12_unit6_source_recovery','math12_translation_completions',...Array.from({length:11},(_,i)=>'math12_unit'+(i+2)+'_translations'),'math12_answer_repairs','math12_legibility_recovery','math12_unit9_practice','math12_unit6_exercise61_recovery','math12_study_views'];
for(const name of mathFiles)if(fs.existsSync(path.join(root,'js/'+name+'.js')))vm.runInContext(read('js/'+name+'.js'),s);
vm.runInContext('this.math=MATH_12_DATA;',s);
const json=file=>fs.existsSync(path.join(root,file))?JSON.parse(read(file)):null;
const mathViews=json('docs/source-verification/class-12/math12-view-check.json');
const sharedViews=json('docs/source-verification/class-12/shared-view-check.json');
const questions=s.math.flatMap(ch=>(ch.exercises||[]).flatMap(ex=>ex.problems||[]));
const unresolved=questions.filter(q=>/partial|unresolved|under_specified/i.test(q.solutionStatus||q.sourceStatus||''));
const report={updatedUtc:new Date().toISOString(),status:'in_progress',request:'Make all Class12 subjects match Class9 contents/structure/views and complete every question answer, including MCQs; Mathematics first.',
 activeWork:'Mathematics source recovery and translations; shared Class12 views and first science exercise banks',
 mathematics:{units:s.math.length,workedExamples:s.math.reduce((n,ch)=>n+(ch.workedExamples||[]).length,0),activeExerciseGroups:questions.length,exerciseGroupsWithAnswer:questions.filter(q=>q.answer||q.solution||q.steps?.length).length,studyBank:s.math.reduce((out,ch)=>{const b=s.getMath12StudyBank(ch);for(const k of ['mcqs','shortQuestions','longQuestions'])out[k]+=b[k].length;return out;},{mcqs:0,shortQuestions:0,longQuestions:0}),
  recoveredUnit6:s.math[5].recoveredPageCompanion?{printedPages:[142,157],source:'docs/source-verification/class-12/sources/math12-unit6-recovered.pdf',content:'Mathematical facts and original SpaceBook explanations; not verbatim external prose',exercise61Groups:s.math[5].exercises.find(ex=>ex.id==='ex-6-5').problems.length,completeTextbookTranscription:false}:null,
  unresolvedSourceAnswers:unresolved.map(q=>({id:q.id,status:q.solutionStatus||q.sourceStatus})),
  translations:{unit1:s.MATH12_TRANSLATION_COMPLETIONS_REPORT,...Object.fromEntries(Array.from({length:11},(_,i)=>['unit'+(i+2),s['MATH12_UNIT'+(i+2)+'_TRANSLATION_REPORT']||'pending'])),scopeNote:'Section coverage only; frontmatter, objectives and separate worked-answer banks are not certified complete.'},
  viewCheck:mathViews?{passed:!!mathViews.passed,checkedUtc:mathViews.checkedUtc}:null,complete:false},
 sharedViews:sharedViews?{passed:!!sharedViews.passed,checkedUtc:sharedViews.checkedUtc,subjectsChecked:sharedViews.subjects.length,currentStep:sharedViews.currentStep,pageErrors:sharedViews.pageErrors}:null,
 search:json('docs/source-verification/class-12/search-check.json'),
 scienceBanks:{chemistryUnit13:json('docs/source-verification/class-12/chem12-unit13-study-check.json'),physicsUnit11:json('docs/source-verification/class-12/phys12-unit11-study-check.json')},
 remaining:['Finish and check remaining Mathematics Urdu/Pashto source passages and new answer translations.','Retain two mathematically under-specified source questions with complete conditional/method explanations.','Finish source-to-question and answer mapping in remaining Physics, Chemistry, Statistics, languages and humanities units.','Replace unanswered template prompts with relevant answered source questions; preserve original source text.','Complete final source/formula/diagram review and browser checks before claiming any whole-class completion.'],
 benchmark:{verifiedPagesPerHour:null,reason:'This pass combines UI work, answer repair and source recovery; no timed whole-page verified throughput was measured.'},
 projectChecks:{},nextAction:'Continue the exact unfinished Mathematics translation section reported above; integrate/check new source banks and then continue remaining subjects.'};
for(const [name,file]of [['validate','tmp/class12-validate.log'],['smoke','tmp/class12-smoke.log']])if(fs.existsSync(path.join(root,file))){const lines=read(file).split(/\r?\n/);report.projectChecks[name]={passed:!lines.some(line=>/^FAIL\s/.test(line)||/TypeError:/.test(line)),failures:lines.filter(line=>/^FAIL\s/.test(line)),crash:lines.find(line=>/TypeError:/.test(line))||null,log:file};}
const target=path.join(root,'docs/source-verification/class-12/standardization-progress.json'),temp=target+'.tmp';fs.writeFileSync(temp,JSON.stringify(report,null,2)+'\n');fs.renameSync(temp,target);
console.log(JSON.stringify({status:report.status,exerciseGroups:questions.length,studyBank:report.mathematics.studyBank,nextMathTranslation:s.MATH12_UNIT2_TRANSLATION_REPORT?.nextSection,sharedViewCheck:report.sharedViews?.passed,checkpoint:target}));
