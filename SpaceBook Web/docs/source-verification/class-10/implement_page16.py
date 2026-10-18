from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
block=r'''
  // PDF page 16, printed page 11: frequency, lab, gravitational-field example/assignment.
  const pendulum16=[
    {text:'Since frequency is the reciprocal of time period therefore the frequency of simple pendulum is given as',urdu:'چونکہ تعدد دورانیے کا معکوس ہے، اس لیے سادہ پنڈولم کا تعدد یوں دیا جاتا ہے',pashto:'څرنګه چې فریکونسي د دورې معکوس ده، نو د ساده رقاص فریکونسي داسې ورکول کېږي'},
    sourceEquation15('f = 1/(2π) √(g/l)','f=\\frac{1}{2\\pi}\\sqrt{\\frac{g}{l}}','<mi>f</mi><mo>=</mo><mfrac><mn>1</mn><mrow>'+twoPi+'</mrow></mfrac><msqrt>'+gOverL15+'</msqrt>',['','',''],'10.9'),
    {type:'heading',text:'LAB WORK',urdu:'تجربہ گاہ کا کام',pashto:'د لابراتوار کار'},
    {text:'To study the effect of the length of a simple pendulum on time, find the value of “g” by calculation.',urdu:'وقت پر سادہ پنڈولم کی لمبائی کے اثر کا مطالعہ کرنے کے لیے، حساب کے ذریعے “g” کی قدر معلوم کریں۔',pashto:'پر وخت د ساده رقاص د اوږدوالي د اغېز د مطالعې لپاره، د محاسبې له لارې د “g” قیمت معلوم کړئ.'}
  ];
  const first16=pendulumTarget.paras.length;
  pendulumTarget.paras.push(...pendulum16);
  pendulumTarget.sourceLayoutPhysics10.push(...pendulum16.map((_,i)=>({type:'paragraph',index:first16+i})));
  pendulumTarget.sourceReferences.push({pdf:'10thphysics1.pdf',pdfPage:16,printedPage:'11'});
  const sqrtLG16='<msqrt><mfrac><mi>l</mi><mi>g</mi></mfrac></msqrt>';
  const example16={id:'phys10-example-10.5',sourceNumber:'10.5',title:'EXAMPLE 10.5: DETERMINING GRAVITATIONAL FIELD STRENGTH',titleUrdu:'مثال 10.5: ثقلی میدان کی شدت معلوم کرنا',titlePashto:'مثال 10.5: د جاذبې میدان د شدت معلومول',source:{pdf:'10thphysics1.pdf',pdfPage:16,printedPage:'11'},answerOrigin:'textbook',sourceParagraphs:[
    {text:'What is the gravitational field strength on planet Mercury, if a 0.500 m pendulum swings with a period of 2.30 s?',urdu:'سیارے عطارد پر ثقلی میدان کی شدت کیا ہے، اگر 0.500 m لمبائی کا پنڈولم 2.30 s کے دورانیے سے جھولتا ہو؟',pashto:'پر عطارد سیاره د جاذبې میدان شدت څومره دی، که د 0.500 m اوږدوالي رقاص په 2.30 s دوره زانګي؟'},
    {type:'heading',text:'GIVEN',urdu:'دیا گیا',pashto:'ورکړل شوي'},
    {text:'Time period ‘T’ = 2.3 s',urdu:'دورانیہ ‘T’ = 2.3 s',pashto:'دوره ‘T’ = 2.3 s'},
    {text:'Length ‘l’ = 0.500 m',urdu:'لمبائی ‘l’ = 0.500 m',pashto:'اوږدوالی ‘l’ = 0.500 m'},
    {type:'heading',text:'REQUIRED',urdu:'مطلوب',pashto:'غوښتل شوي'},
    {text:'gravitational field strength ‘g’ = ?',urdu:'ثقلی میدان کی شدت ‘g’ = ؟',pashto:'د جاذبې میدان شدت ‘g’ = ؟'},
    {text:'SOLUTION: The time period for simple pendulum is',urdu:'حل: سادہ پنڈولم کا دورانیہ ہے',pashto:'حل: د ساده رقاص دوره ده',lead:{text:'SOLUTION:',urdu:'حل:',pashto:'حل:'}},
    {type:'equation',text:'T = 2π√(l/g)     Squaring T² = [2π√(l/g)]²',urdu:'T = 2π√(l/g)     مربع کرنے سے T² = [2π√(l/g)]²',pashto:'T = 2π√(l/g)     د مربع کولو سره T² = [2π√(l/g)]²',formulas:[page12Formula('T = 2π√(l/g)','T=2\\pi\\sqrt{\\frac{l}{g}}','<mi>T</mi><mo>=</mo>'+twoPi+sqrtLG16),page12Formula('T² = [2π√(l/g)]²','T^2=\\left[2\\pi\\sqrt{\\frac{l}{g}}\\right]^2',squareT+'<mo>=</mo><msup><mrow><mo>[</mo>'+twoPi+sqrtLG16+'<mo>]</mo></mrow><mn>2</mn></msup>')]},
    {type:'equation',text:'or T² = 4π² × l/g     Isolating g g = (4π² × l)/T²',urdu:'یا T² = 4π² × l/g     g کو الگ کرنے سے g = (4π² × l)/T²',pashto:'یا T² = 4π² × l/g     د g جلا کولو سره g = (4π² × l)/T²',formulas:[page12Formula('T² = 4π² × l/g','T^2=4\\pi^2\\times\\frac{l}{g}',squareT+'<mo>=</mo>'+fourPiSquared+'<mo>×</mo><mfrac><mi>l</mi><mi>g</mi></mfrac>'),page12Formula('g = (4π² × l)/T²','g=\\frac{4\\pi^2\\times l}{T^2}','<mi>g</mi><mo>=</mo><mfrac><mrow>'+fourPiSquared+'<mo>×</mo><mi>l</mi></mrow>'+squareT+'</mfrac>')]},
    sourceEquation15('g = (4(3.14)² × 0.500 m)/(2.30 s)²','g=\\frac{4(3.14)^2\\times0.500\\,\\mathrm{m}}{(2.30\\,\\mathrm{s})^2}','<mi>g</mi><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mrow><mo>(</mo><mn>3.14</mn><mo>)</mo></mrow><mn>2</mn></msup><mo>×</mo><mn>0.500</mn><mi mathvariant="normal">m</mi></mrow><msup><mrow><mo>(</mo><mn>2.30</mn><mi mathvariant="normal">s</mi><mo>)</mo></mrow><mn>2</mn></msup></mfrac>',['Putting values ','قدریں رکھنے سے ','د قیمتونو په ایښودلو سره ']),
    {type:'equation',text:'Therefore g = 3.73 m/s² = 3.73 N/kg [down]     Answer',urdu:'لہٰذا g = 3.73 m/s² = 3.73 N/kg [نیچے]     جواب',pashto:'نو g = 3.73 m/s² = 3.73 N/kg [ښکته]     ځواب',formulas:[page12Formula('g = 3.73 m/s² = 3.73 N/kg','g=3.73\\,\\frac{\\mathrm{m}}{\\mathrm{s}^2}=3.73\\,\\frac{\\mathrm{N}}{\\mathrm{kg}}','<mi>g</mi><mo>=</mo><mn>3.73</mn><mfrac><mi mathvariant="normal">m</mi><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>3.73</mn><mfrac><mi mathvariant="normal">N</mi><mi mathvariant="normal">kg</mi></mfrac>')]},
    {text:'The gravitational field strength at the surface of mercury is 3.73 N/kg',urdu:'عطارد کی سطح پر ثقلی میدان کی شدت 3.73 N/kg ہے',pashto:'د عطارد پر سطحه د جاذبې میدان شدت 3.73 N/kg دی'}
  ],sourceAside:{heading:{text:'TIP: Gravitational Field',urdu:'نکتہ: ثقلی میدان',pashto:'نکته: د جاذبې میدان'},para:{text:'The gravitational field strength at a point is the gravitational force exerted per unit mass placed at that point.',urdu:'کسی نقطے پر ثقلی میدان کی شدت، اس نقطے پر رکھی گئی فی اکائی کمیت پر لگنے والی ثقلی قوت ہے۔',pashto:'په یوه نقطه کې د جاذبې میدان شدت، په هغه نقطه کې پر ایښودل شوې هر واحد کتله د عمل کوونکي جاذبې ځواک دی.'}}};
  const oldExample16=chapter.workedExamples.find(e=>e.id===example16.id);
  if(oldExample16) Object.assign(oldExample16,example16);else chapter.workedExamples.push(example16);
  pendulumTarget.sourceLayoutPhysics10.push({type:'example',record:oldExample16||example16});
  const assignment16={id:'phys10-assignment-10.5',sourceNumber:'10.5',source:{pdf:'10thphysics1.pdf',pdfPage:16,printedPage:'11'},answerOrigin:'not supplied on this page',title:{text:'ASSIGNMENT 10.5: GRAVITATIONAL FIELD STRENGTH AT EVEREST',urdu:'مشق 10.5: ایورسٹ پر ثقلی میدان کی شدت',pashto:'دنده 10.5: پر اېورېسټ د جاذبې میدان شدت'},question:{text:'What is the gravitational field strength at the top of Mount Everest at an altitude of 8954.0 m, if a pendulum with a length of 1.00 m has a period of 2.01 s?',urdu:'8954.0 m کی بلندی پر ماؤنٹ ایورسٹ کی چوٹی پر ثقلی میدان کی شدت کیا ہے، اگر 1.00 m لمبائی کے پنڈولم کا دورانیہ 2.01 s ہو؟',pashto:'د 8954.0 m په لوړوالي د اېورېسټ غره پر څوکه د جاذبې میدان شدت څومره دی، که د 1.00 m اوږدوالي رقاص دوره 2.01 s وي؟'}};
  const oldAssignment16=chapter.sourceAssignments.find(a=>a.id===assignment16.id);
  if(oldAssignment16) Object.assign(oldAssignment16,assignment16);else chapter.sourceAssignments.push(assignment16);
  pendulumTarget.sourceLayoutPhysics10.push({type:'assignment',record:oldAssignment16||assignment16});
  const flatten16=pendulumTarget.paras.flatMap(p=>p.type==='list'?p.items:[p]);
  pendulumTarget.text=flatten16.map(p=>p.text).join('\n\n');
  pendulumTarget.summary={en:pendulumTarget.text,ur:flatten16.map(p=>p.urdu).join('\n\n'),ps:flatten16.map(p=>p.pashto).join('\n\n')};
  if(legacyPendulum) legacyPendulum.desc=pendulumTarget.text;
'''
assert '// PDF page 16, printed page 11' not in s
s=s.replace('  chapter.sourceReview = ',block+'\n  chapter.sourceReview = ',1).replace('lastFullyVerifiedPdfPage: 15, nextPdfPage: 16','lastFullyVerifiedPdfPage: 16, nextPdfPage: 17')
needle="(i===7 && example.figure ? renderPhysics10SourceFigure(example.figure,field) : '')+"
replacement=needle+"(i===7 && example.sourceAside ? `<aside style=\"padding:.75rem;background:#fff1f2;border:1px solid #e9a4b0;\"><h6>${sanitize(example.sourceAside.heading[field])}</h6><p>${renderPhysics10SourceParagraph(example.sourceAside.para,`${example.id}-tip`,field)}</p></aside>` : '')+"
assert needle in s
s=s.replace(needle,replacement)
p.write_text(s,encoding='utf-8')
