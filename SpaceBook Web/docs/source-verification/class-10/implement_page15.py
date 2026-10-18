from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
block=r'''
  // PDF page 15, printed page 10: source solution and pendulum period derivation.
  const sourceEquation15=(source,latex,body,prefixes=['','',''],number)=>({type:'equation',text:prefixes[0]+source,urdu:prefixes[1]+source,pashto:prefixes[2]+source,...(number?{equationNumber:number}:{}),formulas:[page12Formula(source,latex,body)]});
  const rest15='<msub><mi>F</mi><mtext>rest</mtext></msub><mo>=</mo><mo>−</mo>';
  const unitAcceleration15='<mi mathvariant="normal">m</mi><msup><mi mathvariant="normal">s</mi><mn>−2</mn></msup>';
  const targetExample15=oldExample14||example14;
  targetExample15.sourceParagraphs.push(
    sourceEquation15('F_rest = -0.1000 kg × 9.8 m s⁻² sin10°','F_{\\mathrm{rest}}=-0.1000\\,\\mathrm{kg}\\times9.8\\,\\mathrm{m\\,s}^{-2}\\sin10^\\circ',rest15+'<mn>0.1000</mn><mi mathvariant="normal">kg</mi><mo>×</mo><mn>9.8</mn>'+unitAcceleration15+'<mi>sin</mi><mn>10</mn><mo>°</mo>',['Putting values ','قدریں رکھنے سے ','د قیمتونو په ایښودلو سره ']),
    sourceEquation15('F_rest = -0.98 kg m s⁻² × 0.17','F_{\\mathrm{rest}}=-0.98\\,\\mathrm{kg\\,m\\,s}^{-2}\\times0.17',rest15+'<mn>0.98</mn><mi mathvariant="normal">kg</mi>'+unitAcceleration15+'<mo>×</mo><mn>0.17</mn>',['or ','یا ','یا ']),
    {type:'equation',text:'F_rest = -0.167 N     Answer',urdu:'F_rest = -0.167 N     جواب',pashto:'F_rest = -0.167 N     ځواب',formulas:[page12Formula('F_rest = -0.167 N','F_{\\mathrm{rest}}=-0.167\\,\\mathrm{N}',rest15+'<mn>0.167</mn><mi mathvariant="normal">N</mi>')]},
    {text:'The magnitude of the restoring force acting on the pendulum is 0.167 N.',urdu:'پنڈولم پر عمل کرنے والی بحالی قوت کی مقدار 0.167 N ہے۔',pashto:'پر رقاص د عمل کوونکي بېرته راوستونکي ځواک اندازه 0.167 N ده.'}
  );
  targetExample15.sourceReferences.push({pdf:'10thphysics1.pdf',pdfPage:15,printedPage:'10'});
  targetExample15.continuationExpected=false;
  const assignment15={id:'phys10-assignment-10.4',sourceNumber:'10.4',source:{pdf:'10thphysics1.pdf',pdfPage:15,printedPage:'10'},answerOrigin:'not supplied on this page',title:{text:'ASSIGNMENT 10.4: CALCULATING ANGLE',urdu:'مشق 10.4: زاویے کا حساب',pashto:'دنده 10.4: د زاویې محاسبه'},question:{text:'At what angle must a pendulum be displaced to create a restoring force of 4.00 N on a bob with a mass of 500.0 g?',urdu:'500.0 g کمیت کے گولے پر 4.00 N کی بحالی قوت پیدا کرنے کے لیے پنڈولم کو کس زاویے تک ہٹانا ہوگا؟',pashto:'د 500.0 g کتلې پر ګولۍ د 4.00 N بېرته راوستونکي ځواک د پیدا کولو لپاره باید رقاص په کومه زاویه بې ځایه شي؟'}};
  const oldAssignment15=chapter.sourceAssignments.find(a=>a.id===assignment15.id);
  if(oldAssignment15) Object.assign(oldAssignment15,assignment15); else chapter.sourceAssignments.push(assignment15);
  pendulumTarget.sourceLayoutPhysics10.push({type:'assignment',record:oldAssignment15||assignment15});
  const gOverL15='<mfrac><mi>g</mi><mi>l</mi></mfrac>';
  const periodRatio15='<mfrac><mrow>'+fourPiSquared+'</mrow>'+squareT+'</mfrac>';
  const derivation15=[
    {text:'10.4.1 Time period ‘T’ and frequency ‘f’ of simple pendulum: It can be shown that the acceleration and displacement of a simple pendulum are related by its time-period T (the time it takes for the mass spring system to complete one cycle) by the following equation:',urdu:'10.4.1 سادہ پنڈولم کا دورانیہ ‘T’ اور تعدد ‘f’: یہ دکھایا جا سکتا ہے کہ سادہ پنڈولم کی تعجیل اور نقل مکانی اس کے دورانیے T (کمیت اور سپرنگ کے نظام کے ایک چکر مکمل کرنے میں لگنے والا وقت) کے ذریعے درج ذیل مساوات سے متعلق ہیں:',pashto:'10.4.1 د ساده رقاص دوره ‘T’ او فریکونسي ‘f’: ښودل کېدای شي چې د ساده رقاص تعجیل او بې ځایه کېدل د هغه د دورې T (هغه وخت چې د کتلې او فنر سیستم پکې یوه دوره بشپړوي) له لارې په لاندې معادله سره تړلي دي:',lead:{text:'10.4.1 Time period ‘T’ and frequency ‘f’ of simple pendulum:',urdu:'10.4.1 سادہ پنڈولم کا دورانیہ ‘T’ اور تعدد ‘f’:',pashto:'10.4.1 د ساده رقاص دوره ‘T’ او فریکونسي ‘f’:'}},
    sourceEquation15('a = -(4π²/T²)x','a=-\\frac{4\\pi^2}{T^2}x','<mi>a</mi><mo>=</mo><mo>−</mo>'+periodRatio15+'<mi>x</mi>',['','',''],'1'),
    sourceEquation15('a = -(g/l)x','a=-\\frac{g}{l}x','<mi>a</mi><mo>=</mo><mo>−</mo>'+gOverL15+'<mi>x</mi>',['From equation 10.7, we have ','مساوات 10.7 سے ہمارے پاس ہے ','له معادلې 10.7 څخه لرو '],'2'),
    sourceEquation15('-(g/l)x = -(4π²/T²)x','\\cancel{-}\\frac{g}{l}\\cancel{x}=\\cancel{-}\\frac{4\\pi^2}{T^2}\\cancel{x}','<menclose notation="updiagonalstrike"><mo>−</mo></menclose>'+gOverL15+'<menclose notation="updiagonalstrike"><mi>x</mi></menclose><mo>=</mo><menclose notation="updiagonalstrike"><mo>−</mo></menclose>'+periodRatio15+'<menclose notation="updiagonalstrike"><mi>x</mi></menclose>',['Comparing equation 1 and 2, we get ','مساوات 1 اور 2 کا موازنہ کرنے سے ملتا ہے ','د معادلې 1 او 2 په پرتله کولو سره ترلاسه کوو ']),
    {type:'equation',text:'or g/l = 4π²/T²     re-arranging T² = 4π² l/g',urdu:'یا g/l = 4π²/T²     ترتیب بدلنے سے T² = 4π² l/g',pashto:'یا g/l = 4π²/T²     د بیا ترتیبولو سره T² = 4π² l/g',formulas:[page12Formula('g/l = 4π²/T²','\\frac{g}{l}=\\frac{4\\pi^2}{T^2}',gOverL15+'<mo>=</mo>'+periodRatio15),page12Formula('T² = 4π² l/g','T^2=4\\pi^2\\frac{l}{g}',squareT+'<mo>=</mo>'+fourPiSquared+'<mfrac><mi>l</mi><mi>g</mi></mfrac>')]},
    sourceEquation15('√T² = √4π² √(l/g)','\\sqrt{T^2}=\\sqrt{4\\pi^2}\\sqrt{\\frac{l}{g}}','<msqrt>'+squareT+'</msqrt><mo>=</mo><msqrt>'+fourPiSquared+'</msqrt><msqrt><mfrac><mi>l</mi><mi>g</mi></mfrac></msqrt>',['Taking square root on both sides, we have ','دونوں طرف مربع جذر لینے سے ہمارے پاس ہے ','د دواړو خواوو مربع ریښه اخیستو سره لرو ']),
    sourceEquation15('T = 2π√(l/g)','T=2\\pi\\sqrt{\\frac{l}{g}}','<mi>T</mi><mo>=</mo>'+twoPi+'<msqrt><mfrac><mi>l</mi><mi>g</mi></mfrac></msqrt>',['Hence ','لہٰذا ','نو '],'10.8'),
    {text:'Equation 10.8 shows that the time period ‘T’ of simple pendulum depends directly on the length ‘l’ of the pendulum and inversely on gravitational acceleration ‘g’. The period of the pendulum does not depend on the mass of the pendulum bob. The period of a pendulum does not depend on its amplitude.',urdu:'مساوات 10.8 دکھاتی ہے کہ سادہ پنڈولم کا دورانیہ ‘T’ پنڈولم کی لمبائی ‘l’ پر براہِ راست اور ثقلی تعجیل ‘g’ پر معکوس طور پر منحصر ہے۔ پنڈولم کا دورانیہ اس کے گولے کی کمیت پر منحصر نہیں ہوتا۔ پنڈولم کا دورانیہ اس کے حیطے پر منحصر نہیں ہوتا۔',pashto:'معادله 10.8 ښيي چې د ساده رقاص دوره ‘T’ د رقاص په اوږدوالي ‘l’ مستقیم او د جاذبې په تعجیل ‘g’ معکوس ډول پورې اړه لري. د رقاص دوره د رقاص د ګولۍ په کتله پورې اړه نه لري. د رقاص دوره د هغه په لمن پورې اړه نه لري.'}
  ];
  const first15=pendulumTarget.paras.length;
  pendulumTarget.paras.push(...derivation15);
  pendulumTarget.sourceLayoutPhysics10.push(...derivation15.map((_,i)=>({type:'paragraph',index:first15+i})));
  pendulumTarget.sourceReferences.push({pdf:'10thphysics1.pdf',pdfPage:15,printedPage:'10'});
  pendulumTarget.sourceClarifications=[{text:'Editorial clarification: The parenthesis under 10.4.1 prints “mass spring system”; this section concerns a simple pendulum. Equation 10.8 gives T proportional to the square root of l and inversely proportional to the square root of g, for small-angle oscillations. Example 10.4 uses sin10° rounded to 0.17; its printed answer is retained.',urdu:'ادارتی وضاحت: 10.4.1 کے تحت قوسین میں “کمیت اور سپرنگ کا نظام” چھپا ہے؛ یہ حصہ سادہ پنڈولم کے متعلق ہے۔ مساوات 10.8 کے مطابق چھوٹے زاویے کے ارتعاشات کے لیے T، l کے مربع جذر کے راست متناسب اور g کے مربع جذر کے معکوس متناسب ہے۔ مثال 10.4 میں sin10° کو تقریباً 0.17 لیا گیا ہے؛ چھپا ہوا جواب برقرار رکھا گیا ہے۔',pashto:'د سمونګر وضاحت: د 10.4.1 لاندې په قوسونو کې «د کتلې او فنر سیستم» چاپ شوی؛ دا برخه د ساده رقاص په اړه ده. د معادلې 10.8 له مخې د کوچنۍ زاویې اهتزازونو لپاره T د l له مربع ریښې سره مستقیم او د g له مربع ریښې سره معکوس تناسب لري. په مثال 10.4 کې sin10° نږدې 0.17 اخیستل شوی؛ چاپ شوی ځواب ساتل شوی دی.'}];
  const flatten15=pendulumTarget.paras.flatMap(p=>p.type==='list'?p.items:[p]);
  pendulumTarget.text=flatten15.map(p=>p.text).join('\n\n');
  pendulumTarget.summary={en:pendulumTarget.text,ur:flatten15.map(p=>p.urdu).join('\n\n'),ps:flatten15.map(p=>p.pashto).join('\n\n')};
  if(legacyPendulum) legacyPendulum.desc=pendulumTarget.text;
'''
assert '// PDF page 15, printed page 10' not in s
s=s.replace('  chapter.sourceReview = ',block+'\n  chapter.sourceReview = ',1).replace('lastFullyVerifiedPdfPage: 14, nextPdfPage: 15','lastFullyVerifiedPdfPage: 15, nextPdfPage: 16')
p.write_text(s,encoding='utf-8')
