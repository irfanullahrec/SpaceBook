/* A matching independent scan resolves the smudged exponent on printed290. */
(function(){
 const q=MATH_12_DATA[9].exercises.flatMap(ex=>ex.problems||[]).find(item=>item.id==='ex-10-1-q2');
 if(!q||q.legibilityRecovered)return;
 q.originalLegibilityReview={question:q.question,answer:q.answer,steps:q.steps,sourceQuestionBlocks:q.sourceQuestionBlocks,sourceStatus:q.sourceStatus,solutionStatus:q.solutionStatus,sourceClarification:q.sourceClarification};
 q.question=q.question.replace('y′+y=e raised to a smudged source exponent','y′+y=e^(−x)');
 q.steps=[
  '(a) Differentiate y=e^x+e^(2x): y′=e^x+2e^(2x), y″=e^x+4e^(2x). The residual is (1−3+2)e^x+(4−6+2)e^(2x)=0.',
  '(b) For x>0, y=x−x ln x gives y′=−ln x. Hence xy′+x−y=−x ln x+x−(x−x ln x)=0.',
  '(c) The matching independent scan clearly prints y′+y=e^(−x). For y=(x+c)e^(−x), y′=(1−x−c)e^(−x), and adding y gives e^(−x). The stated equation is satisfied.',
  '(d) For y=e^x+e^(−x), y′=e^x−e^(−x) and y″=e^x+e^(−x). Substitution into the printed equation gives y″−3y′+2y=6e^(−x), not zero.',
  'Thus parts (a), (b) and (c) hold. Part (d) is a printed inconsistency: the given function solves y″−y=0, while the printed equation has the family Ce^x+De^(2x). The original part (d) remains visible.'
 ];
 q.solution=q.steps.join('\n');q.answer='(a), (b) and (c) verified. Part (d) does not solve the printed equation: its residual is 6e^(−x).';
 q.solutionStatus='worked and checked; part (d) printed inconsistency retained';
 q.sourceStatus='independent_scan_legibility_resolved';
 q.sourceClarification='The matching scan on printed page290 resolves the exponent in part(c) as −x. Part(d) is legible but mathematically inconsistent; its equation has not been silently corrected.';
 q.sourceQuestionBlocks=[{type:'figure',src:'assets/math12/ode290-q2c-independent.png',caption:'Exercise10.1 Q2(c): exponent −x confirmed in the matching independent scan',alt:'y=(x+c)e to the power −x, and dy/dx+y=e to the power −x.',displayWidth:580}];
 q.sourceReferences=[...q.sourceReferences,{page:290,pdfPage:295,sourceUrl:'https://drive.google.com/file/d/1z5fdQlJ09IRZUGqjyGPxQkwWubHuCjQJ/view',sourceCrop:'assets/math12/ode290-q2c-independent.png',verification:'Independent matching-edition scan visually inspected on2026-10-18; exponent reads−x.'}];
 q.legibilityRecovered=true;
 globalThis.MATH12_LEGIBILITY_RECOVERY_REPORT={resolved:['ex-10-1-q2 part(c)'],remainingSourceLimitedAnswers:['ex-2-1-q5 photographic endpoints','ex-12-2-q5 missing integrand and partition'],additionalInspection:'Matching scan printed31 still does not specify both profile endpoints; printed323 still omits the integrand in Q5.',originalRecordPreserved:true};
})();
