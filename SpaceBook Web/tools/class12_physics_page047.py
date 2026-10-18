"""Sequential source correction for PDF page 47 of Class 12 Physics."""
from class12_source_review import upsert, section, checkpoint, sync_companions, shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(page):return {'pdfPage':47,'printedPage':page,'sourcePdf':SOURCE}
def mcq(q,opts):return {'question':q,'choices':opts}

MCQS=[
 mcq(pair(r'The resistivity of two wires is \(\rho_1\) and \(\rho_2\), which are connected in series. If their dimensions are same, then the equivalent resistivity of the combination will be',r'دو تاروں کی مزاحمت النوعی \(\rho_1\) اور \(\rho_2\) ہے اور انہیں سلسلہ وار جوڑا گیا ہے۔ اگر ان کے ابعاد یکساں ہوں تو امتزاج کی مساوی مزاحمت النوعی ہو گی:',r'د دو سیمونو مخصوص مقاومتونه \(\rho_1\) او \(\rho_2\) دي او په لړۍ نښلول شوي. که ابعاد یې یو شان وي، د ترکیب معادل مخصوص مقاومت به وي:'),[
  pair(r'A. \((\rho_1+\rho_2)\)',r'A. \((\rho_1+\rho_2)\)',r'A. \((\rho_1+\rho_2)\)'),
  pair(r'B. \(\frac{1}{\rho_1}+\frac{1}{\rho_2}\)',r'B. \(\frac{1}{\rho_1}+\frac{1}{\rho_2}\)',r'B. \(\frac{1}{\rho_1}+\frac{1}{\rho_2}\)'),
  pair(r'C. \(\frac{\rho_1+\rho_2}{2}\)',r'C. \(\frac{\rho_1+\rho_2}{2}\)',r'C. \(\frac{\rho_1+\rho_2}{2}\)'),
  pair(r'D. \(\frac{\rho_1}{\rho_2}\)',r'D. \(\frac{\rho_1}{\rho_2}\)',r'D. \(\frac{\rho_1}{\rho_2}\)')]),
 mcq(pair('The powers of two electric bulbs are 100 W and 200 W. Which are connected to power supply of 220 V? The ratio of resistance of their filament will be',
  'دو برقی بلبوں کی طاقتیں 100 W اور 200 W ہیں اور انہیں 220 V کی سپلائی سے جوڑا گیا ہے۔ ان کے فلامنٹس کی مزاحمت کا تناسب ہو گا:',
  'د دو برېښنايي څراغونو توانونه 100 W او 200 W دي او د 220 V برېښنايي سرچینې سره نښلول شوي. د فلامنټونو د مقاومت نسبت به وي:'),[
  pair('A. 1:2','A. 1:2','A. 1:2'),pair('B. 2:1','B. 2:1','B. 2:1'),pair('C. 1:3','C. 1:3','C. 1:3'),pair('D. 4:3','D. 4:3','D. 4:3')]),
 mcq(pair('Thermocouple is an arrangement of two different metals', 'تھرموکپل دو مختلف دھاتوں کا انتظام ہے:', 'ترموکوپل د دوو بېلابېلو فلزونو ترتیب دی:'),[
  pair('a) To convert heat energy into electrical energy','a) حرارتی توانائی کو برقی توانائی میں تبدیل کرنا','a) حرارتي انرژي په برېښنايي انرژۍ بدلول'),pair('b) To produce more heat','b) مزید حرارت پیدا کرنا','b) زیاته تودوخه تولیدول'),pair('c) To convert heat energy into chemical energy','c) حرارتی توانائی کو کیمیائی توانائی میں تبدیل کرنا','c) حرارتي انرژي په کیمیاوي انرژۍ بدلول'),pair('d) To convert electric energy into heat energy','d) برقی توانائی کو حرارتی توانائی میں تبدیل کرنا','d) برېښنايي انرژي په حرارتي انرژۍ بدلول')]),
 mcq(pair('In order to achieve high accuracy, the slide wire of a potentiometer should be', 'زیادہ درستی حاصل کرنے کے لیے پوٹینشیومیٹر کی سلائیڈ وائر ہونی چاہیے:', 'د لوړې کره‌والي لپاره د پوتنشیومیتر ښویېدونکی سیم باید:'),[
  pair('A. As long as possible','A. ممکن حد تک لمبی','A. د امکان تر حده اوږد'),pair('B. As short as possible','B. ممکن حد تک چھوٹی','B. د امکان تر حده لنډ'),pair('C. Very thin','C. بہت باریک','C. ډېر نری'),pair('D. Very thick','D. بہت موٹی','D. ډېر پنډ')]),
 mcq(pair('When a potentiometer is used for measurement of voltage of an unknown source, the power consumed in the circuit of the unknown source under null condition is', 'نامعلوم منبع کے وولٹیج کی پیمائش کے لیے پوٹینشیومیٹر استعمال ہو تو صفر حالت میں نامعلوم منبع کے سرکٹ میں استعمال ہونے والی طاقت ہوتی ہے:', 'کله چې د نامعلومې سرچینې د ولتاژ د اندازه کولو لپاره پوتنشیومیتر وکارول شي، د صفر حالت پر مهال د سرچینې په مدار کې مصرفېدونکی توان وي:'),[
  pair('A. high','A. زیادہ','A. لوړ'),pair('B. small','B. کم','B. لږ'),pair('C. ideally zero','C. مثالی طور پر صفر','C. په مثالي ډول صفر'),pair('D. very high','D. بہت زیادہ','D. ډېر لوړ')]),
 mcq(pair('In a Wheatstone bridge method, the bridge is said to be balanced, when the current through the galvanometer is', 'وہیٹ اسٹون برج کے طریقے میں برج کو متوازن کہا جاتا ہے جب گیلوانومیٹر میں برقی رو ہو:', 'د وېټسټون پُل په طریقه کې پُل هغه وخت متوازن بلل کېږي چې د ګالوانومیټر جریان وي:'),[
  pair('A. 1 A','A. 1 A','A. 1 A'),pair('B. 0 A','B. 0 A','B. 0 A'),pair('C. Maximum','C. زیادہ سے زیادہ','C. اعظمي'),pair('D. Half of the maximum value','D. زیادہ سے زیادہ قدر کا نصف','D. د اعظمي ارزښت نیمایي')]),
]
CONCEPT=[
 pair('CONCEPTUAL QUESTIONS','تصوری سوالات','مفهومي پوښتنې'),
 pair('1. A heavy duty battery of a truck maintains a current of 3 A for 24 hour. How much charge flows from the battery during this time?', '1. ٹرک کی ہیوی ڈیوٹی بیٹری 24 گھنٹے تک 3 A برقی رو برقرار رکھتی ہے۔ اس وقت میں بیٹری سے کتنا چارج بہتا ہے؟','1. د لارۍ پیاوړې بیټرۍ د 24 ساعتونو لپاره 3 A جریان ساتي. په دې موده کې له بیټرۍ څخه څومره چارج تېرېږي؟'),
 pair('2. While analysing a circuit the internal resistance of e.m.f. sources are ignored why?', '2. سرکٹ کا تجزیہ کرتے وقت محرکہ قوت کے ذرائع کی اندرونی مزاحمت کو کیوں نظر انداز کیا جاتا ہے؟','2. د مدار د تحلیل پر مهال د محرکې قوې د سرچینو دننی مقاومت ولې له پامه غورځول کېږي؟'),
 pair('3. If aluminium and copper wires of the same length have the same resistance, which has the larger diameter? Why?', '3. اگر ایک ہی لمبائی کے ایلومینیم اور تانبے کے تاروں کی مزاحمت یکساں ہو تو کس تار کا قطر بڑا ہے؟ کیوں؟','3. که د المونیم او مسو د یو شان اوږدوالي سیمونه یو شان مقاومت ولري، د کوم سیم قطر لوی دی؟ ولې؟'),
 pair('4. Under what circumstances can the terminal P.D. of a battery exceed its e.m.f.?', '4. کن حالات میں بیٹری کا ٹرمینل پوٹینشل فرق اس کی محرکہ قوت سے بڑھ سکتا ہے؟','4. په کومو شرایطو کې د بیټرۍ ترمینلي پوتنشیالي توپیر له محرکې قوې څخه زیاتېدای شي؟'),
 pair('5. What is the difference between an e.m.f. and a P.D.?','5. برقی محرکہ قوت اور پوٹینشل فرق میں کیا فرق ہے؟','5. د محرکې قوې او پوتنشیالي توپیر ترمنځ څه توپیر دی؟'),
 pair('6. How are the loop rule and junction rule based on the conservation of energy principle?', '6. حلقے کا قاعدہ اور جوڑ کا قاعدہ توانائی کے بقائے کے اصول پر کیسے مبنی ہیں؟','6. د کړۍ قاعده او د پیوند قاعده د انرژۍ د پایښت پر اصل څنګه ولاړ دي؟'),
 pair('7. Why is a rise in temperature of a conductor accompanied by a rise in the resistance?', '7. موصل کا درجۂ حرارت بڑھنے کے ساتھ مزاحمت کیوں بڑھتی ہے؟','7. د هادي د تودوخې له لوړېدو سره مقاومت ولې زیاتېږي؟'),
 pair('8. Does the direction of e.m.f. provided by a battery depend on the direction of current flow through the battery?', '8. کیا بیٹری کی فراہم کردہ محرکہ قوت کی سمت بیٹری میں برقی رو کے بہاؤ کی سمت پر منحصر ہے؟','8. ایا د بیټرۍ د محرکې قوې لوری د بیټرۍ له لارې د جریان پر لوري پورې تړلی دی؟'),
 pair('9. Voltages are always measured between two points. Why?', '9. وولٹیج ہمیشہ دو نقاط کے درمیان کیوں ناپا جاتا ہے؟','9. ولتاژ تل د دوو نقطو ترمنځ ولې اندازه کېږي؟'),
 pair('10. Is every e.m.f. a potential difference? Is every potential difference an e.m.f.?', '10. کیا ہر محرکہ قوت پوٹینشل فرق ہوتی ہے؟ کیا ہر پوٹینشل فرق محرکہ قوت ہوتا ہے؟','10. ایا هره محرکه قوه پوتنشیالي توپیر دی؟ ایا هر پوتنشیالي توپیر محرکه قوه ده؟'),
 pair('11. How much charge flows in a pocket calculator each minute when the current is 0.0001 A?', '11. جب برقی رو 0.0001 A ہو تو ہر منٹ میں جیب کیلکولیٹر سے کتنا چارج گزرتا ہے؟','11. کله چې جریان 0.0001 A وي، په هره دقیقه کې د جېبي حساب‌ماشین له لارې څومره چارج تېرېږي؟'),
 pair('12. When a Wheatstone bridge is balanced, then no current flows through the galvanometer. Why?', '12. جب وہیٹ اسٹون برج متوازن ہو تو گیلوانومیٹر میں برقی رو کیوں نہیں بہتی؟','12. کله چې وېټسټون پُل متوازن وي، ولې د ګالوانومیټر له لارې جریان نه تېرېږي؟'),
]
COMPREHENSIVE=[
 pair('COMPREHENSIVE QUESTIONS','جامع سوالات','هر اړخیزې پوښتنې'),
 pair('1. Describe the concept of steady state current as a flow of positive, negative or both. Define the unit of current.', '1. مستقل حالت کی برقی رو کے تصور کو مثبت، منفی یا دونوں باروں کے بہاؤ کے طور پر بیان کریں۔ برقی رو کی اکائی کی تعریف کریں۔','1. د ثابت حالت جریان مفهوم د مثبتو، منفي یا دواړو چارجونو د بهېدو په توګه بیان کړئ. د جریان واحد تعریف کړئ.'),
 pair('2. Explain the electronic current in a metallic wire as due to the drift of free electrons in the wire.', '2. دھاتی تار میں الیکٹرانک برقی رو کو تار کے آزاد الیکٹرانوں کے بہاؤ کی وجہ سے سمجھائیں۔','2. په فلزي سیم کې الکتروني جریان د ازادو الکترونونو د ډرېفټ له امله تشریح کړئ.'),
 pair('3. State Ohm’s law. Discuss its scope and validity: (a) discuss resistivity and conductivity of a material; (b) how does resistance change with temperature?', '3. اوم کا قانون بیان کریں۔ اس کے دائرے اور صحت پر بحث کریں: (a) کسی مادے کی مزاحمت النوعی اور موصلیت پر بحث کریں؛ (b) درجۂ حرارت کے ساتھ مزاحمت کیسے بدلتی ہے؟','3. د اوم قانون بیان کړئ او د پلي کېدو ساحه او اعتبار یې وڅېړئ: (a) د مادې مخصوص مقاومت او هاديتوب وڅېړئ؛ (b) مقاومت له تودوخې سره څنګه بدلېږي؟'),
 pair('4. Explain the terms: e.m.f., internal resistance and terminal potential difference of a battery.', '4. د اصطلاحاتو وضاحت کریں: بیٹری کی محرکہ قوت، اندرونی مزاحمت اور ٹرمینل پوٹینشل فرق۔','4. دا اصطلاحات تشریح کړئ: د بیټرۍ محرکه قوه، دننی مقاومت او ترمینلي پوتنشیالي توپیر.'),
 pair('5. Explain the construction of a rheostat. How is it used to (a) control the current, (b) act as a potential divider?', '5. ریوسٹیٹ کی ساخت بیان کریں۔ اسے (a) برقی رو کنٹرول کرنے اور (b) پوٹینشل ڈیوائیڈر کے طور پر کیسے استعمال کیا جاتا ہے؟','5. د ریوستات جوړښت تشریح کړئ. دا څنګه (a) جریان کنټرولوي او (b) د پوتنشیالي وېشونکي په توګه کار کوي؟'),
 pair('6. What is a Wheatstone bridge? Explain with a diagram the balancing, principle and working of this bridge.', '6. وہیٹ اسٹون برج کیا ہے؟ شکل کے ساتھ اس برج کا توازن، اصول اور طریقۂ کار بیان کریں۔','6. وېټسټون پُل څه شی دی؟ د شکل په مرسته د دې پُل توازن، اصل او کار تشریح کړئ.'),
 pair('7. What is a potentiometer? Explain its principle, construction and working. What is the advantage of using a potentiometer for measuring potential difference?', '7. پوٹینشیومیٹر کیا ہے؟ اس کا اصول، ساخت اور کام بیان کریں۔ پوٹینشل فرق ناپنے کے لیے پوٹینشیومیٹر استعمال کرنے کا کیا فائدہ ہے؟','7. پوتنشیومیتر څه شی دی؟ اصل، جوړښت او کار یې تشریح کړئ. د پوتنشیالي توپیر د اندازه کولو لپاره د پوتنشیومیتر کارولو ګټه څه ده؟'),
]

def add_record(identity,title,printed,pairs,layout):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':47,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,('',''));s['kind']='lesson';s['sourceReferences']=[ref(n) for n in ([84] if printed==84 else [85])]
 return r,s

if __name__=='__main__':
 exercise_pairs=[];layout=[]
 mcq_card={'id':'phys12-unit12-mcq-pdf47','exercise':'Unit 12 MCQs 9–14','title':'Multiple-choice questions 9–14 (printed page 84)','problems':[],'sourceReferences':[ref(84)]}
 for n,q in enumerate(MCQS,9):
  stem=len(exercise_pairs);exercise_pairs.append(q['question']);layout.append({'type':'paragraph','indices':[stem]})
  opts=[];choices=[]
  for ch in q['choices']:
   idx=len(exercise_pairs);exercise_pairs.append(ch);opts.append(idx);label=ch[0][:2]
   choices.append({'label':label,'text':ch[0][2:].strip(),'textUrdu':ch[1][2:].strip(),'textPashto':ch[2][2:].strip()})
  layout.append({'type':'list','indices':opts})
  mcq_card['problems'].append({'id':f'physics12-mcq-{n}','qNo':str(n),'question':q['question'][0],'questionUrdu':q['question'][1],'questionPashto':q['question'][2],'choices':choices,'sourceReferences':[ref(84)]})
 m=add_record('phys12-unit12-mcq9-14-84','Multiple-choice exercise — questions 9–14',84,exercise_pairs,layout)
 con_pairs=CONCEPT;con_layout=[{'type':'heading','indices':[0]}]+[{'type':'paragraph','indices':[i]} for i in range(1,len(con_pairs))]
 c=add_record('phys12-unit12-conceptual1-12-84-85','Conceptual Questions 1–12',84,con_pairs,con_layout)
 comp_pairs=COMPREHENSIVE;comp_layout=[{'type':'heading','indices':[0]}]+[{'type':'paragraph','indices':[i]} for i in range(1,len(comp_pairs))]
 h=add_record('phys12-unit12-comprehensive1-7-85','Comprehensive Questions 1–7',85,comp_pairs,comp_layout)
 cards=[mcq_card,
  {'id':'phys12-unit12-conceptual-pdf47','exercise':'Unit 12 Conceptual Questions 1–12','title':'Conceptual Questions 1–12','problems':[{'id':f'physics12-conceptual-{n}','qNo':str(n),'question':p[0],'questionUrdu':p[1],'questionPashto':p[2],'sourceReferences':[ref(84 if n<=2 else 85)]} for n,p in enumerate(CONCEPT[1:],1)],'sourceReferences':[ref(84),ref(85)]},
  {'id':'phys12-unit12-comprehensive-pdf47','exercise':'Unit 12 Comprehensive Questions 1–7','title':'Comprehensive Questions 1–7','problems':[{'id':f'physics12-comprehensive-{n}','qNo':str(n),'question':p[0],'questionUrdu':p[1],'questionPashto':p[2],'sourceReferences':[ref(85)]} for n,p in enumerate(COMPREHENSIVE[1:],1)],'sourceReferences':[ref(85)]}]
 with shared_class_data_lock():
  upsert([m[0],c[0],h[0]],[m[1],c[1],h[1]],chapter_index=1)
  sync_companions(chapter_index=1,retire_sections=['12.12'],trim_sections=[{'id':'12.13','startsAt':'What is thermocouple?','title':'Comprehensive Questions 8–9 — printed page 86 pending source review'}],exercises=cards)
 checkpoint(47,'corrected_verified',[m[0]['id'],c[0]['id'],h[0]['id']],'Rendered and inspected PDF page 47, printed pages 84–85. Compared multiple-choice questions 9–14 with every option, all 12 Conceptual Questions, and Comprehensive Questions 1–7. Preserved source question wording/options, added no answers, paired each item in English/Urdu/Pashto, upserted three structured question-bank cards, retired the covered legacy MCQ section and trimmed the remaining extract at the first unchecked Comprehensive Question 8 on printed page 86. Handwritten margin ticks were excluded as later annotations.',printed_pages=[84,85],chapter_number=12)
