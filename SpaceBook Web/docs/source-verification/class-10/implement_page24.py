from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
block=r'''
  // PDF page 24, printed page 19: universal wave equation, Example 10.6, Assignment 10.6 and properties opener.
  const wave24=[
    {text:'The distance traveled by wave equal to one wavelength ‘λ’ (Δs = λ) is covered in time equal to time period T (Δt = T), therefore equation 1 can be written as',urdu:'لہر کے ذریعے طے کیا گیا فاصلہ ایک طولِ موج ‘λ’ (Δs = λ) کے برابر ہے، اور یہ دورانیہ T (Δt = T) کے برابر وقت میں طے ہوتا ہے، لہٰذا مساوات 1 یوں لکھی جا سکتی ہے',pashto:'د څپې له خوا طی شوی واټن د یوه څپې له اوږدوالي ‘λ’ (Δs = λ) سره برابر دی او د دورې T (Δt = T) سره برابر وخت کې طی کېږي، نو معادله 1 داسې لیکل کېدای شي'},
    {type:'equation',text:'v = λ/T',urdu:'v = λ/T',pashto:'v = λ/T',equationNumber:'2',formulas:[page12Formula('v = λ/T','v=\\frac{\\lambda}{T}','<mi>v</mi><mo>=</mo><mfrac><mi>λ</mi><mi>T</mi></mfrac>')]},
    {text:'Since time period ‘T’ and frequency ‘f’ are reciprocal of each other, therefore',urdu:'چونکہ دورانیہ ‘T’ اور تعدد ‘f’ ایک دوسرے کے معکوس ہیں، اس لیے',pashto:'څرنګه چې د دورې وخت ‘T’ او فریکونسي ‘f’ د یو بل معکوس دي، نو'},
    {type:'equation',text:'f = 1/T',urdu:'f = 1/T',pashto:'f = 1/T',equationNumber:'3',formulas:[page12Formula('f = 1/T','f=\\frac{1}{T}','<mi>f</mi><mo>=</mo><mfrac><mn>1</mn><mi>T</mi></mfrac>')]},
    {text:'putting equation 3 in equation 2, we get',urdu:'مساوات 3 کو مساوات 2 میں رکھنے سے ہمیں ملتا ہے',pashto:'په معادله 2 کې د معادلې 3 په ایښودلو سره ترلاسه کوو'},
    {type:'equation',text:'v = f λ',urdu:'v = f λ',pashto:'v = f λ',equationNumber:'10.12',formulas:[page12Formula('v = f λ','v=f\\lambda','<mi>v</mi><mo>=</mo><mi>f</mi><mi>λ</mi>')]},
    {text:'Equation 10.12 is also called universal wave equation as it applies to all waves and gives the wave speed in terms of frequency f and wavelength λ.',urdu:'مساوات 10.12 کو عالمگیر لہری مساوات بھی کہتے ہیں، کیونکہ یہ تمام لہروں پر لاگو ہوتی ہے اور تعدد f اور طولِ موج λ کی صورت میں لہر کی رفتار دیتی ہے۔',pashto:'معادله 10.12 د نړیوالې څپیزې معادلې په نوم هم یادېږي، ځکه چې پر ټولو څپو تطبیقېږي او د فریکونسۍ f او څپې اوږدوالي λ له مخې د څپې سرعت ورکوي.'},
    {type:'heading',text:'10.7 PROPERTIES OF WAVES',urdu:'10.7 لہروں کی خصوصیات',pashto:'10.7 د څپو ځانګړنې'},
    {text:'The basic properties of two dimensional waves, such as water waves can be described with the help of ripple tank.',urdu:'دو بعدی لہروں، مثلاً پانی کی لہروں، کی بنیادی خصوصیات کو ریپل ٹینک کی مدد سے بیان کیا جا سکتا ہے۔',pashto:'د دوه بعدي څپو، لکه د اوبو څپو، اساسي ځانګړنې د ریپل ټانک په مرسته بیانېدای شي.'}
  ];
  const example24={id:'phys10-example-10.6',sourceNumber:'10.6',title:'EXAMPLE 10.6: WAVE SPEED',titleUrdu:'مثال 10.6: لہر کی رفتار',titlePashto:'مثال 10.6: د څپې سرعت',source:{pdf:'10thphysics1.pdf',pdfPage:24,printedPage:'19'},answerOrigin:'textbook',sourceParagraphs:[
    {text:'A student vibrates the end of a spring at 2.6 Hz. This produces a wave with a wavelength of 0.37 m. Calculate the speed of the wave.',urdu:'ایک طالب علم سپرنگ کے سرے کو 2.6 Hz پر ارتعاش دیتا ہے۔ اس سے 0.37 m طولِ موج کی لہر پیدا ہوتی ہے۔ لہر کی رفتار معلوم کریں۔',pashto:'یو زده کوونکی د فنر سر په 2.6 Hz اهتزازوي. دا د 0.37 m څپې اوږدوالي لرونکې څپه پیدا کوي. د څپې سرعت محاسبه کړئ.'},
    {type:'heading',text:'GIVEN',urdu:'دیا گیا',pashto:'ورکړل شوي'},
    {text:'frequency ‘f’ = 2.6 Hz',urdu:'تعدد ‘f’ = 2.6 Hz',pashto:'فریکونسي ‘f’ = 2.6 Hz'},
    {text:'wavelength ‘λ’ = 0.37 m',urdu:'طولِ موج ‘λ’ = 0.37 m',pashto:'د څپې اوږدوالی ‘λ’ = 0.37 m'},
    {type:'heading',text:'REQUIRED',urdu:'مطلوب',pashto:'غوښتل شوي'},
    {text:'speed ‘v’ = ?',urdu:'رفتار ‘v’ = ؟',pashto:'سرعت ‘v’ = ؟'},
    {text:'SOLUTION: By universal wave equation',urdu:'حل: عالمگیر لہری مساوات کے مطابق',pashto:'حل: د نړیوالې څپیزې معادلې له مخې',lead:{text:'SOLUTION:',urdu:'حل:',pashto:'حل:'}},
    {type:'equation',text:'v = f λ',urdu:'v = f λ',pashto:'v = f λ',formulas:[page12Formula('v = f λ','v=f\\lambda','<mi>v</mi><mo>=</mo><mi>f</mi><mi>λ</mi>')]},
    {type:'equation',text:'putting values v = 2.6 s⁻¹ × 0.37 m',urdu:'قدریں رکھنے سے v = 2.6 s⁻¹ × 0.37 m',pashto:'د قیمتونو په ایښودلو سره v = 2.6 s⁻¹ × 0.37 m',formulas:[page12Formula('v = 2.6 s⁻¹ × 0.37 m','v=2.6\\,\\mathrm{s}^{-1}\\times0.37\\,\\mathrm{m}','<mi>v</mi><mo>=</mo><mn>2.6</mn><mi mathvariant="normal">s</mi><msup><mn>−1</mn></msup><mo>×</mo><mn>0.37</mn><mi mathvariant="normal">m</mi>')]},
    {type:'equation',text:'Hence v = 0.962 m s⁻¹     Answer',urdu:'لہٰذا v = 0.962 m s⁻¹     جواب',pashto:'نو v = 0.962 m s⁻¹     ځواب',formulas:[page12Formula('v = 0.962 m s⁻¹','v=0.962\\,\\mathrm{m\\,s}^{-1}','<mi>v</mi><mo>=</mo><mn>0.962</mn><mi mathvariant="normal">m</mi><msup><mi mathvariant="normal">s</mi><mn>−1</mn></msup>')]},
    {text:'The answer validates; as reasonable speed for wave in a spring is about 1 m/s.',urdu:'یہ جواب معقول ہے؛ کیونکہ سپرنگ میں لہر کی مناسب رفتار تقریباً 1 m/s ہوتی ہے۔',pashto:'دا ځواب سمون لري؛ ځکه په فنر کې د څپې معقول سرعت شاوخوا 1 m/s وي.'}
  ]};
  const oldExample24=chapter.workedExamples.find(e=>e.id===example24.id);if(oldExample24)Object.assign(oldExample24,example24);else chapter.workedExamples.push(example24);
  const assignment24={id:'phys10-assignment-10.6',sourceNumber:'10.6',source:{pdf:'10thphysics1.pdf',pdfPage:24,printedPage:'19'},answerOrigin:'not supplied on this page',title:{text:'ASSIGNMENT 10.6: WAVELENGTH OF SOUND',urdu:'مشق 10.6: آواز کی طولِ موج',pashto:'دنده 10.6: د غږ څپې اوږدوالی'},question:{text:'A sound wave of wavelength 1.7 × 10⁻² m. Calculate the frequency of sound if its velocity is 343.4 ms⁻¹.',urdu:'1.7 × 10⁻² m طولِ موج کی صوتی لہر ہے۔ اگر اس کی رفتار 343.4 ms⁻¹ ہو تو آواز کی تعدد معلوم کریں۔',pashto:'د 1.7 × 10⁻² m څپې اوږدوالي غږیزه څپه ده. که سرعت یې 343.4 ms⁻¹ وي، د غږ فریکونسي محاسبه کړئ.'}};
  const oldAssignment24=chapter.sourceAssignments.find(a=>a.id===assignment24.id);if(oldAssignment24)Object.assign(oldAssignment24,assignment24);else chapter.sourceAssignments.push(assignment24);
  const first24=wavesTarget.paras.length;wavesTarget.paras.push(...wave24);
  wavesTarget.sourceLayoutPhysics10.push(...wave24.map((_,i)=>({type:'paragraph',index:first24+i})),{type:'example',record:oldExample24||example24},{type:'assignment',record:oldAssignment24||assignment24});
  wavesTarget.sourceReferences.push({pdf:'10thphysics1.pdf',pdfPage:24,printedPage:'19'});
  const flat24=wavesTarget.paras.flatMap(p=>p.type==='list'?p.items:[p]);wavesTarget.text=flat24.map(p=>p.text).join('\n\n');wavesTarget.summary={en:wavesTarget.text,ur:flat24.map(p=>p.urdu).join('\n\n'),ps:flat24.map(p=>p.pashto).join('\n\n')};
  for(const [term,p] of [['Wave speed',wave24[9]]]){const record={id:'phys10-definition-wave-speed',term,def:p.text,sourceParagraph:p,sourceReferences:[{pdf:'10thphysics1.pdf',pdfPage:24,printedPage:'19'}]};const previous=chapter.definitions.find(d=>d.id===record.id);if(previous)Object.assign(previous,record);else chapter.definitions.push(record);}
'''
assert '// PDF page 24, printed page 19' not in s
s=s.replace('  chapter.sourceReview = ',block+'\n  chapter.sourceReview = ',1).replace('lastFullyVerifiedPdfPage: 23, nextPdfPage: 24','lastFullyVerifiedPdfPage: 24, nextPdfPage: 25')
p.write_text(s,encoding='utf-8')
