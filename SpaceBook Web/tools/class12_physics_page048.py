"""Sequential source correction for PDF page 48 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions, shared_class_data_lock

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def ref(printed): return {'pdfPage':48,'printedPage':printed,'sourcePdf':SOURCE}
def svg(body,label):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 300" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:560px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

COMPREHENSIVE=[
 pair('COMPREHENSIVE QUESTIONS','جامع سوالات','هر اړخیزې پوښتنې'),
 pair('8. What is thermocouple? Explain the working of thermocouple by drawing its diagram. By sketching curve explain the variation in thermoelectric e.m.f. with Temperature.',
  '8. تھرموکپل کیا ہے؟ اس کا خاکہ بنا کر کام کی وضاحت کریں۔ منحنی خاکہ بنا کر درجۂ حرارت کے ساتھ تھرمو الیکٹرک محرکہ قوت کی تبدیلی بیان کریں۔',
  '8. ترموکوپل څه شی دی؟ د شکل په رسمولو یې کار تشریح کړئ. د منحني په رسمولو د تودوخې له بدلون سره د ترموبرېښنايي محرکې قوې بدلون بیان کړئ.'),
 pair('9. Why we use Kirchoff’s law for circuit problems solution. Explain its rules for circuit solution by giving proper example.',
  '9. د سرکټ د مسئلو د حل لپاره د کرخوف قانون ولې کاروو؟ د مناسب مثال په ورکولو د سرکټ د حل قواعد یې بیان کړئ۔',
  '9. د مدار د مسئلو د حل لپاره د کرخوف قانون ولې کاروو؟ د مناسبې بېلګې په ورکولو د مدار د حل قواعد یې تشریح کړئ.'),
]

NUMERICALS=[
 (1,pair('1. A battery has an e.m.f. of 12.8 V and supplies a current of 3.2 A. What is the resistance of the circuit? How many coulombs leave the battery in 5 minutes?',
  '1. ایک بیٹری کی محرکہ قوت 12.8 V ہے اور یہ 3.2 A برقی رو فراہم کرتی ہے۔ سرکٹ کی مزاحمت کیا ہے؟ 5 منٹ میں بیٹری سے کتنے کولمب خارج ہوتے ہیں؟',
  '1. د بیټرۍ محرکه قوه 12.8 V ده او 3.2 A جریان برابروي. د مدار مقاومت څومره دی؟ په 5 دقیقو کې له بیټرۍ څو کولمبه وځي؟'),
  pair('Answer (4 Ω, 1200 C)','جواب (4 Ω، 1200 C)','ځواب (4 Ω، 1200 C)')),
 (2,pair('2. Two light bulbs designed for 120-V use are rated at 40 W and 60 W. Which light bulb has the greater filament resistance? Why?',
  '2. دو بلب 120-V استعمال کے لیے بنائے گئے ہیں اور ان کی طاقتیں 40 W اور 60 W ہیں۔ کس بلب کے فلامنٹ کی مزاحمت زیادہ ہے؟ کیوں؟',
  '2. دوه څراغونه د 120-V کارونې لپاره جوړ شوي او توانونه یې 40 W او 60 W دي. د کوم څراغ د فلامنټ مقاومت ډېر دی؟ ولې؟'),
  pair('Answer (240 Ω, 360 Ω)','جواب (240 Ω، 360 Ω)','ځواب (240 Ω، 360 Ω)')),
 (3,pair('3. A carbon electrode has a resistance of 0.125 Ω at 20 °C. The temperature coefficient of carbon is −0.0005 at 20 °C. What will be the resistance of the electrode at 85 °C?',
  '3. ایک کاربن الیکٹروڈ کی 20 °C پر مزاحمت 0.125 Ω ہے۔ 20 °C پر کاربن کا درجۂ حرارت عدد −0.0005 ہے۔ 85 °C پر الیکٹروڈ کی مزاحمت کیا ہو گی؟',
  '3. د کاربن الکترود مقاومت په 20 °C کې 0.125 Ω ده. په 20 °C کې د کاربن د تودوخې ضریب −0.0005 دی. په 85 °C کې به د الکترود مقاومت څومره وي؟'),
  pair('Answer (0.12 Ω)','جواب (0.12 Ω)','ځواب (0.12 Ω)')),
 (4,pair('4. Calculate the resistance of wire 10 m long that has a diameter of 2 mm and resistivity of 2.63 × 10⁻⁸ Ω m.',
  '4. 10 m لمبی اور 2 mm قطر والی تار کی مزاحمت معلوم کریں، جس کی مزاحمت النوعی 2.63 × 10⁻⁸ Ω m ہے۔',
  '4. د 10 m اوږد او 2 mm قطر لرونکي سیم مقاومت محاسبه کړئ چې مخصوص مقاومت یې 2.63 × 10⁻⁸ Ω m دی.'),
  pair('Answer (0.0838 Ω)','جواب (0.0838 Ω)','ځواب (0.0838 Ω)')),
 (5,pair('5. A typical 12 V automobile battery has a resistance of 0.012 Ω. What is the terminal voltage of this battery when the starter draws a current of 100 A? Calculate R, Pε, P_R and P_r.',
  '5. ایک عام 12 V آٹوموبائل بیٹری کی مزاحمت 0.012 Ω ہے۔ جب اسٹارٹر 100 A برقی رو لیتا ہے تو بیٹری کا ٹرمینل وولٹیج کیا ہو گا؟ R، Pε، P_R اور P_r معلوم کریں۔',
  '5. د یوه عادي 12 V موټر بیټرۍ مقاومت 0.012 Ω دی. کله چې سټارټر 100 A جریان اخلي، د بیټرۍ ترمینلي ولتاژ څومره دی؟ R، Pε، P_R او P_r محاسبه کړئ.'),
  pair('Answer (10.8 V, 0.108 Ω, 1200 W, 120 W)','جواب (10.8 V، 0.108 Ω، 1200 W، 120 W)','ځواب (10.8 V، 0.108 Ω، 1200 W، 120 W)')),
 (6,pair('6. A 10 watt resistor has a value of 120 Ω. What is the rated current through the resistor?',
  '6. ایک 10 watt مزاحمت کی قدر 120 Ω ہے۔ اس مزاحمت میں مقررہ برقی رو کتنی ہے؟',
  '6. د 10 watt مقاومت ارزښت 120 Ω دی. د مقاومت ټاکل شوی جریان څومره دی؟'),
  pair('Answer (0.2886 A)','جواب (0.2886 A)','ځواب (0.2886 A)')),
 (7,pair('7. A resistor of 50 Ω has a P.D. of 100 V, D.C. across 1 hour. Calculate (a) Power and (b) Energy.',
  '7. ایک 50 Ω مزاحمت پر 1 گھنٹے تک 100 V ڈی سی پوٹینشل فرق ہے۔ (a) طاقت اور (b) توانائی معلوم کریں۔',
  '7. د 50 Ω مقاومت په اوږدو کې د 1 ساعت لپاره 100 V ډي‌سي پوتنشیالي توپیر دی. (a) توان او (b) انرژي محاسبه کړئ.'),
  pair('Answer ((a) 200 W, (b) 0.72 MJ)','جواب ((a) 200 W، (b) 0.72 MJ)','ځواب ((a) 200 W، (b) 0.72 MJ)')),
 (8,pair('8. Calculate the current through a single loop circuit if ε = 120 V, R = 1000 Ω and internal resistance r = 0.01 Ω.',
  '8. اگر ایک حلقی سرکٹ میں ε = 120 V، R = 1000 Ω اور اندرونی مزاحمت r = 0.01 Ω ہو تو برقی رو معلوم کریں۔',
  '8. که په یوه کړۍ مدار کې ε = 120 V، R = 1000 Ω او دننی مقاومت r = 0.01 Ω وي، جریان محاسبه کړئ.'),
  pair('Answer (120 mA)','جواب (120 mA)','ځواب (120 mA)')),
]

Q9=pair('9. Find the terminal potential difference of each cell in circuit of figure.',
 '9. شکل کے سرکٹ میں ہر سیل کا ٹرمینل پوٹینشل فرق معلوم کریں۔','9. د شکل په مدار کې د هرې حجرې ترمینلي پوتنشیالي توپیر ومومئ.')
Q10=pair('10. The voltmeter in the circuit at the right may be considered to be ideal. Values are, ε = 15.0 V; internal resistance, r = 5.00 Ω; R₁ = 100 Ω; R₂ = 300 Ω. Calculate the current in R₁.',
 '10. دائیں طرف کے سرکٹ میں وولٹ میٹر کو مثالی تصور کیا جا سکتا ہے۔ قدریں یہ ہیں: ε = 15.0 V؛ اندرونی مزاحمت r = 5.00 Ω؛ R₁ = 100 Ω؛ R₂ = 300 Ω۔ R₁ میں برقی رو معلوم کریں۔',
 '10. د ښي لوري په مدار کې ولټ‌متر مثالي ګڼل کېدای شي. ارزښتونه دا دي: ε = 15.0 V؛ دننی مقاومت r = 5.00 Ω؛ R₁ = 100 Ω؛ R₂ = 300 Ω. په R₁ کې جریان محاسبه کړئ.')
Q11=pair('11. Three arms of a Wheatstone bridge are of 75 Ω each. What is the resistance of the fourth arm?',
 '11. د وہیٹ اسٹون برج کے تین بازوؤں میں ہر ایک کی مزاحمت 75 Ω ہے۔ چوتھے بازو کی مزاحمت کیا ہے؟',
 '11. د وېټسټون پُل درې مټې هره یوه 75 Ω مقاومت لري. د څلورمې مټې مقاومت څومره دی؟')

def cell(text): return f'<text font-family="Arial,sans-serif" font-size="16" fill="#172033">{text}</text>'
def question9_svg(lang):
 labels={'en':'Figure: two cells, 24 V and 6 V, with internal resistances 0.1 Ω and 0.9 Ω, joined by an 8 Ω resistor.','ur':'شکل: 24 V اور 6 V کے دو سیل، اندرونی مزاحمتیں 0.1 Ω اور 0.9 Ω، اور 8 Ω مزاحمت سے باہم جڑے ہیں۔','ps':'شکل: دوه حجرې، 24 V او 6 V، د 0.1 Ω او 0.9 Ω دننیو مقاومتونو سره، د 8 Ω مقاومت په وسیله نښلول شوې دي.'}
 b='<path d="M100 72H188M378 72H460M100 238H460M188 72H220l10-12 15 24 15-24 15 24 15-24 15 24 15-24 15 24 15-24 15 24 15-24 15 12H378" fill="none" stroke="#334155" stroke-width="3"/>'
 b+='<path d="M100 72V96M100 194V238M460 72V96M460 194V238" stroke="#334155" stroke-width="3"/>'
 b+='<path d="M100 96V104l-10 8 20 12-20 12 20 12-10 8V180M460 96V104l-10 8 20 12-20 12 20 12-10 8V180" fill="none" stroke="#334155" stroke-width="3"/>'
 b+='<path d="M82 180h36m-27 14h18M442 180h36m-27 14h18" stroke="#334155" stroke-width="3"/><text x="255" y="51">8 Ω</text><text x="40" y="147">0.1 Ω</text><text x="42" y="222">24 V</text><text x="480" y="147">0.9 Ω</text><text x="480" y="222">6 V</text>'
 return svg(b,labels[lang])
def question10_svg(lang):
 labels={'en':'Figure: source emf ε and internal resistance r in one branch; parallel resistors R1 and R2 and ideal voltmeter V across the same rails.','ur':'شکل: ایک شاخ میں منبع کی محرکہ قوت ε اور اندرونی مزاحمت r؛ متوازی مزاحمتیں R1، R2 اور انہی سروں کے پار مثالی وولٹ میٹر V۔','ps':'شکل: په یوه څانګه کې د سرچینې محرکه قوه ε او دننی مقاومت r؛ موازي مقاومتونه R1 او R2 او د همدغو رېلونو ترمنځ مثالي ولټ‌متر V.'}
 b='<path d="M90 64H470M90 232H470M90 64V90m0 116v26M470 64v52m0 56v60" fill="none" stroke="#334155" stroke-width="3"/>'
 b+='<path d="M90 90v32m0 20v20m0 34" stroke="#334155" stroke-width="3"/><path d="M72 124h36m-27 14h18" stroke="#334155" stroke-width="3"/><text x="36" y="133">ε</text>'
 b+='<path d="M90 162v8l-10 7 20 12-20 12 20 12-10 7" fill="none" stroke="#334155" stroke-width="3"/><text x="38" y="197">r</text>'
 b+='<path d="M235 64v40l-10 8 20 12-20 12 20 12-10 8v76M330 64v40l-10 8 20 12-20 12 20 12-10 8v76" fill="none" stroke="#334155" stroke-width="3"/><text x="218" y="91">R₁</text><text x="312" y="91">R₂</text>'
 b+='<circle cx="470" cy="148" r="30" fill="#fff" stroke="#334155" stroke-width="3"/><text x="464" y="155" font-size="22">V</text>'
 return svg(b,labels[lang])

def make(identity,title,printed,pairs,layout,titles,refs,diagrams=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':48,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(n) for n in refs]
 if diagrams:
  s.update(diagrams);s['content']+=diagrams['diagramSvg']
 return r,s

if __name__=='__main__':
 comp_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]}]
 c=make('phys12-unit12-comprehensive8-9-86','Comprehensive Questions 8–9',86,COMPREHENSIVE,comp_layout,('جامع سوالات 8–9','هر اړخیزې پوښتنې 8–9'),[86])
 num_pairs=[pair('NUMERICAL PROBLEMS','عددی مسائل','عددي مسئلې')]
 num_layout=[{'type':'heading','indices':[0]}]
 problem_cards=[]
 for n,q,a in NUMERICALS:
  qi=len(num_pairs);num_pairs.extend([q,a]);num_layout.extend([{'type':'paragraph','indices':[qi]},{'type':'paragraph','indices':[qi+1]}])
  problem_cards.append({'id':f'physics12-numerical-{n}','qNo':str(n),'question':q[0],'questionUrdu':q[1],'questionPashto':q[2],
   'answer':a[0].replace('Answer ','').strip(),'answerUrdu':a[1].replace('جواب ','').strip(),'answerPashto':a[2].replace('ځواب ','').strip(),'solutionOrigin':'textbook printed answer','sourceReferences':[ref(86)]})
 n=make('phys12-unit12-numericals1-8-86','Numerical Problems 1–8',86,num_pairs,num_layout,('عددی مسائل 1–8','عددي مسئلې 1–8'),[86])
 q9_pairs=[pair('NUMERICAL PROBLEM 9','عددی مسئلہ 9','عددي مسئله 9'),Q9,pair('Answer (23.8 V, 7.8 V)','جواب (23.8 V، 7.8 V)','ځواب (23.8 V، 7.8 V)')]
 q9=make('phys12-unit12-numerical9-87','Numerical Problem 9 — terminal voltage of two cells',87,q9_pairs,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},{'type':'paragraph','indices':[2]}],('عددی مسئلہ 9 — دو سیلوں کا ٹرمینل وولٹیج','عددي مسئله 9 — د دوو حجرو ترمینلي ولتاژ'),[87],{'diagramSvg':question9_svg('en'),'diagramSvgUrdu':question9_svg('ur'),'diagramSvgPashto':question9_svg('ps')})
 q10_pairs=[pair('NUMERICAL PROBLEM 10','عددی مسئلہ 10','عددي مسئله 10'),Q10,pair('Answer (0.01406 A)','جواب (0.01406 A)','ځواب (0.01406 A)')]
 q10=make('phys12-unit12-numerical10-87','Numerical Problem 10 — ideal voltmeter circuit',87,q10_pairs,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},{'type':'paragraph','indices':[2]}],('عددی مسئلہ 10 — مثالی وولٹ میٹر کا سرکٹ','عددي مسئله 10 — د مثالي ولټ‌متر مدار'),[87],{'diagramSvg':question10_svg('en'),'diagramSvgUrdu':question10_svg('ur'),'diagramSvgPashto':question10_svg('ps')})
 q11_pairs=[pair('NUMERICAL PROBLEM 11','عددی مسئلہ 11','عددي مسئله 11'),Q11,pair('Answer (75 Ω)','جواب (75 Ω)','ځواب (75 Ω)')]
 q11=make('phys12-unit12-numerical11-87','Numerical Problem 11 — balanced Wheatstone bridge',87,q11_pairs,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]}],('عددی مسئلہ 11 — متوازن وہیٹ اسٹون برج','عددي مسئله 11 — متوازن وېټسټون پُل'),[87])
 cards=[{'id':'phys12-unit12-comprehensive-pdf48','exercise':'Unit 12 Comprehensive Questions 8–9','title':'Comprehensive Questions 8–9','problems':[{'id':f'physics12-comprehensive-{i}','qNo':str(i+8),'question':p[0],'questionUrdu':p[1],'questionPashto':p[2],'sourceReferences':[ref(86)]} for i,p in enumerate(COMPREHENSIVE[1:])],'sourceReferences':[ref(86)]},
  {'id':'phys12-unit12-numerical-pdf48','exercise':'Unit 12 Numerical Problems 1–11','title':'Numerical Problems 1–11 (printed pages 86–87)','problems':problem_cards,'sourceReferences':[ref(86),ref(87)]}]
 records=[c[0],n[0],q9[0],q10[0],q11[0]];sections=[c[1],n[1],q9[1],q10[1],q11[1]]
 with shared_class_data_lock():
  upsert(records,sections,chapter_index=1)
  sync_companions(chapter_index=1,retire_sections=['12.13'],trim_sections=[{'id':'12.14','startsAt':'Unit\n13','title':'Unit 13 — next unchecked source page'}],exercises=cards)
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==48:
  checkpoint(48,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 48, printed pages 86–87. Compared Comprehensive Questions 8–9, all Numerical Problems 1–11, all supplied answers, quantities/units and both circuit figures. Preserved the textbook answer strings without adding solutions, coded the two circuit figures as inline SVG with English/Urdu/Pashto accessible labels, paired all text in English/Urdu/Pashto, synchronized translated exercise cards, retired the now-covered legacy exercise continuation and retained the next unchecked Unit 13 text beginning at its printed heading.',printed_pages=[86,87],chapter_number=12)
