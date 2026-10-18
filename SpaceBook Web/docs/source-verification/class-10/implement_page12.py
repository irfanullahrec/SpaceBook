from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
marker='  chapter.sourceReview = '
block=r'''
  // PDF page 12, printed page 7: continuation of 10.3.1 and source Example 10.3.
  const sqrtMK='<msqrt><mfrac><mi>m</mi><mi>k</mi></mfrac></msqrt>';
  const twoPi='<mn>2</mn><mi>π</mi>';
  const squareT='<msup><mi>T</mi><mn>2</mn></msup>';
  const fourPiSquared='<mn>4</mn><msup><mi>π</mi><mn>2</mn></msup>';
  const page12Formula=(source,latex,body)=>({source,latex,mathml:`<math xmlns="http://www.w3.org/1998/Math/MathML">${body}</math>`});
  const periodFormula=()=>page12Formula('T = 2π√(m/k)','T=2\\pi\\sqrt{\\frac{m}{k}}','<mi>T</mi><mo>=</mo>'+twoPi+sqrtMK);
  const continuation12=[
    {type:'equation',text:'Taking square root on both sides we have √T² = √4π² √(m/k)',urdu:'دونوں طرف مربع جذر لینے سے ہمیں ملتا ہے √T² = √4π² √(m/k)',pashto:'د دواړو خواوو مربع ریښه اخیستو سره لرو √T² = √4π² √(m/k)',formulas:[page12Formula('√T² = √4π² √(m/k)','\\sqrt{T^2}=\\sqrt{4\\pi^2}\\sqrt{\\frac{m}{k}}','<msqrt>'+squareT+'</msqrt><mo>=</mo><msqrt>'+fourPiSquared+'</msqrt>'+sqrtMK)]},
    {text:'Time-period ‘T’ is the time it takes for the mass spring system to complete one vibration, and is given by the following equation:',urdu:'دورانیہ ‘T’ وہ وقت ہے جس میں کمیت اور سپرنگ کا نظام ایک ارتعاش مکمل کرتا ہے، اور یہ درج ذیل مساوات سے دیا جاتا ہے:',pashto:'دوره ‘T’ هغه وخت دی چې د کتلې او فنر سیستم پکې یو اهتزاز بشپړوي، او د لاندې معادلې له مخې ورکول کېږي:'},
    {type:'equation',text:'hence T = 2π√(m/k)',urdu:'لہٰذا T = 2π√(m/k)',pashto:'نو T = 2π√(m/k)',equationNumber:'10.5',formulas:[periodFormula()]},
    {text:'Where ‘m’ is the mass in kg and ‘k’ is the spring constant in N/m of mass spring system. It is worth noting that time period does not depend upon amplitude of oscillation. Since frequency is the reciprocal of time period therefore the frequency of mass spring system is given as',urdu:'یہاں ‘m’ کمیت ہے جس کی اکائی kg ہے، اور ‘k’ کمیت اور سپرنگ کے نظام کا سپرنگ مستقل ہے جس کی اکائی N/m ہے۔ یہ بات قابلِ توجہ ہے کہ دورانیہ ارتعاش کے حیطے پر منحصر نہیں ہوتا۔ چونکہ تعدد دورانیے کا معکوس ہے، اس لیے کمیت اور سپرنگ کے نظام کا تعدد یوں دیا جاتا ہے',pashto:'دلته ‘m’ کتله ده چې واحد یې kg دی، او ‘k’ د کتلې او فنر د سیستم د فنر ثابت دی چې واحد یې N/m دی. د یادونې وړ ده چې دوره د اهتزاز په لمن پورې اړه نه لري. څرنګه چې فریکونسي د دورې معکوس ده، نو د کتلې او فنر د سیستم فریکونسي داسې ورکول کېږي'},
    {type:'equation',text:'f = 1/(2π) √(k/m)',urdu:'f = 1/(2π) √(k/m)',pashto:'f = 1/(2π) √(k/m)',equationNumber:'10.6',formulas:[page12Formula('f = 1/(2π) √(k/m)','f=\\frac{1}{2\\pi}\\sqrt{\\frac{k}{m}}','<mi>f</mi><mo>=</mo><mfrac><mn>1</mn><mrow>'+twoPi+'</mrow></mfrac><msqrt><mfrac><mi>k</mi><mi>m</mi></mfrac></msqrt>')]}
  ];
  const example12={id:'phys10-example-10.3',sourceNumber:'10.3',title:'EXAMPLE 10.3: MASS OF OSCILLATING MASS SPRING SYSTEM',titleUrdu:'مثال 10.3: ارتعاش کرتی کمیت اور سپرنگ کے نظام کی کمیت',titlePashto:'مثال 10.3: د اهتزاز کوونکي کتلې او فنر د سیستم کتله',source:{pdf:'10thphysics1.pdf',pdfPage:12,printedPage:'7'},answerOrigin:'textbook',sourceParagraphs:[
    {text:'What is the mass of a vertical mass-spring system if it oscillates with a period of 2.0 s and has a spring constant of 20.0 N/m?',urdu:'عمودی کمیت اور سپرنگ کے نظام کی کمیت کیا ہے، اگر وہ 2.0 s کے دورانیے سے ارتعاش کرے اور اس کا سپرنگ مستقل 20.0 N/m ہو؟',pashto:'د کتلې او فنر د عمودي سیستم کتله څومره ده، که په 2.0 s دوره اهتزاز کوي او د فنر ثابت یې 20.0 N/m وي؟'},
    {type:'heading',text:'GIVEN',urdu:'دیا گیا',pashto:'ورکړل شوي'},
    {text:'Spring constant ‘k’ = 20 N/m',urdu:'سپرنگ مستقل ‘k’ = 20 N/m',pashto:'د فنر ثابت ‘k’ = 20 N/m'},
    {text:'Time Period ‘T’ = 2.0 s',urdu:'دورانیہ ‘T’ = 2.0 s',pashto:'دوره ‘T’ = 2.0 s'},
    {type:'heading',text:'REQUIRED',urdu:'مطلوب',pashto:'غوښتل شوي'},
    {text:'Mass ‘m’ = ?',urdu:'کمیت ‘m’ = ؟',pashto:'کتله ‘m’ = ؟'},
    {text:'SOLUTION: The time period for mass spring system is',urdu:'حل: کمیت اور سپرنگ کے نظام کا دورانیہ ہے',pashto:'حل: د کتلې او فنر د سیستم دوره ده',lead:{text:'SOLUTION:',urdu:'حل:',pashto:'حل:'}},
    {type:'equation',text:'T = 2π√(m/k)     squaring T² = [2π√(m/k)]²',urdu:'T = 2π√(m/k)     مربع کرنے سے T² = [2π√(m/k)]²',pashto:'T = 2π√(m/k)     د مربع کولو سره T² = [2π√(m/k)]²',formulas:[periodFormula(),page12Formula('T² = [2π√(m/k)]²','T^2=\\left[2\\pi\\sqrt{\\frac{m}{k}}\\right]^2',squareT+'<mo>=</mo><msup><mrow><mo>[</mo>'+twoPi+sqrtMK+'<mo>]</mo></mrow><mn>2</mn></msup>')]},
    {type:'equation',text:'or T² = 4π² × m/k     isolating m m = (T² × K)/(4π²)',urdu:'یا T² = 4π² × m/k     m کو الگ کرنے سے m = (T² × K)/(4π²)',pashto:'یا T² = 4π² × m/k     د m جلا کولو سره m = (T² × K)/(4π²)',formulas:[page12Formula('T² = 4π² × m/k','T^2=4\\pi^2\\times\\frac{m}{k}',squareT+'<mo>=</mo>'+fourPiSquared+'<mo>×</mo><mfrac><mi>m</mi><mi>k</mi></mfrac>'),page12Formula('m = (T² × K)/(4π²)','m=\\frac{T^2\\times K}{4\\pi^2}','<mi>m</mi><mo>=</mo><mfrac><mrow>'+squareT+'<mo>×</mo><mi>K</mi></mrow><mrow>'+fourPiSquared+'</mrow></mfrac>')]},
    {type:'equation',text:'Putting values m = ((2.0 s)² × 20.0 N/m)/(4 × (3.14)²)     as N = kg m/s²',urdu:'قدریں رکھنے سے m = ((2.0 s)² × 20.0 N/m)/(4 × (3.14)²)     کیونکہ N = kg m/s²',pashto:'د قیمتونو په ایښودلو سره m = ((2.0 s)² × 20.0 N/m)/(4 × (3.14)²)     ځکه N = kg m/s²',formulas:[page12Formula('m = ((2.0 s)² × 20.0 N/m)/(4 × (3.14)²)','m=\\frac{(2.0\\,\\mathrm{s})^2\\times20.0\\,\\mathrm{N}/\\mathrm{m}}{4\\times(3.14)^2}','<mi>m</mi><mo>=</mo><mfrac><mrow><msup><mrow><mo>(</mo><mn>2.0</mn><mi mathvariant="normal">s</mi><mo>)</mo></mrow><mn>2</mn></msup><mo>×</mo><mn>20.0</mn><mfrac><mi mathvariant="normal">N</mi><mi mathvariant="normal">m</mi></mfrac></mrow><mrow><mn>4</mn><mo>×</mo><msup><mrow><mo>(</mo><mn>3.14</mn><mo>)</mo></mrow><mn>2</mn></msup></mrow></mfrac>'),page12Formula('N = kg m/s²','\\mathrm{N}=\\mathrm{kg}\\frac{\\mathrm{m}}{\\mathrm{s}^2}','<mi mathvariant="normal">N</mi><mo>=</mo><mi mathvariant="normal">kg</mi><mfrac><mi mathvariant="normal">m</mi><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></mfrac>')]},
    {type:'equation',text:'so m = (4.0 s² × 20.0 kg m/(s² m))/(4 × 9.86)',urdu:'پس m = (4.0 s² × 20.0 kg m/(s² m))/(4 × 9.86)',pashto:'نو m = (4.0 s² × 20.0 kg m/(s² m))/(4 × 9.86)',formulas:[page12Formula('m = (4.0 s² × 20.0 kg m/(s² m))/(4 × 9.86)','m=\\frac{4.0\\,\\cancel{\\mathrm{s}^2}\\times20.0\\,\\mathrm{kg}\\cancel{\\mathrm{m}}/(\\cancel{\\mathrm{s}^2}\\cancel{\\mathrm{m}})}{4\\times9.86}','<mi>m</mi><mo>=</mo><mfrac><mrow><mn>4.0</mn><menclose notation="updiagonalstrike"><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></menclose><mo>×</mo><mn>20.0</mn><mfrac><mrow><mi mathvariant="normal">kg</mi><menclose notation="updiagonalstrike"><mi mathvariant="normal">m</mi></menclose></mrow><mrow><menclose notation="updiagonalstrike"><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></menclose><menclose notation="updiagonalstrike"><mi mathvariant="normal">m</mi></menclose></mrow></mfrac></mrow><mrow><mn>4</mn><mo>×</mo><mn>9.86</mn></mrow></mfrac>')]},
    {type:'equation',text:'Therefore m = 2.02 kg = 2 kg     Answer',urdu:'لہٰذا m = 2.02 kg = 2 kg     جواب',pashto:'له دې امله m = 2.02 kg = 2 kg     ځواب',formulas:[page12Formula('m = 2.02 kg = 2 kg','m=2.02\\,\\mathrm{kg}=2\\,\\mathrm{kg}','<mi>m</mi><mo>=</mo><mn>2.02</mn><mi mathvariant="normal">kg</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">kg</mi>')]},
    {text:'The mass of the mass-spring oscillator is 2.0 kg.',urdu:'کمیت اور سپرنگ کے ارتعاشی نظام کی کمیت 2.0 kg ہے۔',pashto:'د کتلې او فنر د اهتزاز کوونکي سیستم کتله 2.0 kg ده.'}
  ]};
  const existing12=chapter.workedExamples.find(e=>e.id===example12.id);
  if(existing12) Object.assign(existing12,example12); else chapter.workedExamples.push(example12);
  const start12=springTarget.paras.length;
  springTarget.paras.push(...continuation12);
  springTarget.sourceReferences.push({pdf:'10thphysics1.pdf',pdfPage:12,printedPage:'7'});
  springTarget.sourceLayoutPhysics10.push(...continuation12.map((_,i)=>({type:'paragraph',index:start12+i})),{type:'example',record:existing12||example12});
  springTarget.text=springTarget.paras.map(p=>p.text).join('\n\n');
  springTarget.summary={en:springTarget.text,ur:springTarget.paras.map(p=>p.urdu).join('\n\n'),ps:springTarget.paras.map(p=>p.pashto).join('\n\n')};
'''
assert '// PDF page 12, printed page 7' not in s
s=s.replace(marker,block+'\n'+marker,1).replace('lastFullyVerifiedPdfPage: 11, nextPdfPage: 12','lastFullyVerifiedPdfPage: 12, nextPdfPage: 13')
s=s.replace('renderPhysics10WorkedExample(sec.sourceWorkedExample,field);','renderPhysics10WorkedExample(block.record || sec.sourceWorkedExample,field);',1)
p.write_text(s,encoding='utf-8')
