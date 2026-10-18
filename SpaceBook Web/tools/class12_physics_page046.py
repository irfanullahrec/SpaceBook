"""Sequential source correction for PDF page 46 of Class 12 Physics."""
import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions, shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(page):return {'pdfPage':46,'printedPage':page,'sourcePdf':SOURCE}

KEYPOINTS=[
 pair('KEY POINTS','اہم نکات','مهم ټکي'),
 pair('Steady current: the continuous flow of free electrons.', 'مستقل برقی رو: آزاد الیکٹرانوں کا مسلسل بہاؤ۔','ثابت جریان: د ازادو الکترونونو پرله‌پسې بهېدل.'),
 pair(r'Electric current: the net charge flowing through the cross-section area A per unit time. \(I=\frac{Q}{t}\)',r'برقی رو: فی اکائی وقت رقبۂ مقطع A سے گزرنے والا خالص چارج۔ \(I=\frac{Q}{t}\)',r'برېښنايي جریان: په واحد وخت کې د مقطع A له لارې تېرېدونکی خالص چارج. \(I=\frac{Q}{t}\)'),
 pair(r'Ohm’s law: the magnitude of the current in metals is proportional to the applied voltage as long as the temperature of the conductor is kept constant. \(V=IR\)',r'اوم کا قانون: دھاتوں میں برقی رو کی مقدار لگائے گئے وولٹیج کے متناسب ہوتی ہے، بشرطیکہ موصل کا درجۂ حرارت مستقل رکھا جائے۔ \(V=IR\)',r'د اوم قانون: په فلزونو کې د جریان اندازه له لګېدلي ولتاژ سره متناسب ده، تر هغه چې د هادي تودوخه ثابته وساتل شي. \(V=IR\)'),
 pair('Resistance: the opposition offered by the substance to the flow of free electrons.', 'مزاحمت: مادہ آزاد الیکٹرانوں کے بہاؤ میں جو رکاوٹ پیدا کرتا ہے۔','مقاومت: هغه مخالفت چې ماده د ازادو الکترونونو د بهېدو پر وړاندې کوي.'),
 pair('Conductance (G): the reciprocal of resistance of a conductor.', 'موصل کی موصلت (G): موصل کی مزاحمت کا معکوس۔','هادي هاديتوب (G): د هادي د مقاومت معکوس.'),
 pair('Temperature co-efficient of resistance: increase in resistance per ohm original resistance per degree rise in temperature.', 'مزاحمت کا درجۂ حرارت ضریب: درجۂ حرارت میں فی درجے اضافے پر اصل مزاحمت کے فی اوہم میں مزاحمت کا اضافہ۔','د مقاومت د تودوخې ضریب: د تودوخې په هره درجه لوړېدو د اصلي مقاومت د هر اوم په مقابل کې د مقاومت زیاتوالی.'),
 pair('Thermistor: a heat sensitive device usually made of a semiconductor material whose resistance changes very rapidly with change of temperature.', 'تھرمسٹر: حرارت سے حساس آلہ، جو عموماً نیم موصل مادے سے بنتا ہے اور درجۂ حرارت بدلنے سے اس کی مزاحمت بہت تیزی سے بدلتی ہے۔','ترمېسټر: د تودوخې حساسه وسیله چې عموماً له نیمه‌هادي مادې جوړه وي او د تودوخې له بدلون سره یې مقاومت ډېر ژر بدلېږي.'),
 pair('Source of electromotive force: a device which converts non-electrical energy into electrical energy.', 'برقی محرکہ قوت کا منبع: ایسا آلہ جو غیر برقی توانائی کو برقی توانائی میں تبدیل کرتا ہے۔','د برېښنايي محرکې قوې سرچینه: هغه وسیله چې غیربرېښنايي انرژي په برېښنايي انرژۍ بدلوي.'),
 pair('Electric power: the rate at which work is done in an electric circuit.', 'برقی طاقت: برقی سرکٹ میں کام ہونے کی شرح۔','برېښنايي توان: په برېښنايي مدار کې د کار د ترسره کېدو کچه.'),
 pair('Kirchhoff’s law: the algebraic sum of the currents meeting at a junction in an electrical circuit is zero.', 'کرخوف کا قانون: برقی سرکٹ کے جوڑ پر ملنے والی برقی روؤں کا الجبری مجموعہ صفر ہوتا ہے۔','د کرخوف قانون: په برېښنايي مدار کې په پیوند کې د یوځای کېدونکو جریانونو جبري مجموعه صفر ده.'),
]

def mcq(q, opts): return {'question':q,'choices':opts}
MCQS=[
 mcq(pair('Three resistors of resistance R each are combined in various ways. Which of the following cannot be obtained?', 'R مزاحمت والے تین مزاحم مختلف طریقوں سے جوڑے جاتے ہیں۔ درج ذیل میں سے کون سی قدر حاصل نہیں کی جا سکتی؟','درې مقاومتونه چې هر یو R مقاومت لري، په بېلابېلو لارو یوځای کېږي. له لاندې کوم یو نه شي ترلاسه کېدای؟'),[
  pair(r'A. \(3R\,\Omega\)',r'A. \(3R\,\Omega\)',r'A. \(3R\,\Omega\)'),pair(r'B. \(\frac{2R}{4}\,\Omega\)',r'B. \(\frac{2R}{4}\,\Omega\)',r'B. \(\frac{2R}{4}\,\Omega\)'),pair(r'C. \(\frac{R}{3}\,\Omega\)',r'C. \(\frac{R}{3}\,\Omega\)',r'C. \(\frac{R}{3}\,\Omega\)'),pair(r'D. \(\frac{2R}{3}\,\Omega\)',r'D. \(\frac{2R}{3}\,\Omega\)',r'D. \(\frac{2R}{3}\,\Omega\)')]),
 mcq(pair('When n resistances each of value r are connected in parallel, the resultant resistance is x. When these n resistances are connected in series, total resistance is', 'جب r قدر کے n مزاحم متوازی جوڑے جائیں تو حاصل مزاحمت x ہے۔ ان n مزاحموں کو سلسلہ وار جوڑنے پر کل مزاحمت کیا ہو گی؟','کله چې د r ارزښت لرونکي n مقاومتونه موازي ونښلول شي، پایله‌ییز مقاومت x وي. د همدې n مقاومتونو په لړۍ نښلولو ټول مقاومت به څومره وي؟'),[
  pair(r'A. \(nx\)',r'A. \(nx\)',r'A. \(nx\)'),pair(r'B. \(rnx\)',r'B. \(rnx\)',r'B. \(rnx\)'),pair(r'C. \(\frac{x}{n}\)',r'C. \(\frac{x}{n}\)',r'C. \(\frac{x}{n}\)'),pair(r'D. \(n^2x\)',r'D. \(n^2x\)',r'D. \(n^2x\)')]),
 mcq(pair('Two bulbs marked 200 watt–250 volts and 100 watt–250 volts are joined in series to a 250 volts supply. Power consumed in circuit is', '200 واٹ–250 وولٹ اور 100 واٹ–250 وولٹ کے دو بلب 250 وولٹ سپلائی کے ساتھ سلسلہ وار جوڑے گئے ہیں۔ سرکٹ میں استعمال ہونے والی طاقت ہے:', 'د 200 واټه–250 ولټه او 100 واټه–250 ولټه دوه څراغونه له 250 ولټه سرچینې سره په لړۍ نښلول شوي. په مدار کې مصرفېدونکی توان دی:'),[
  pair('A. 33 watt','A. 33 واٹ','A. 33 واټه'),pair('B. 67 watt','B. 67 واٹ','B. 67 واټه'),pair('C. 100 watt','C. 100 واٹ','C. 100 واټه'),pair('D. 300 watt','D. 300 واٹ','D. 300 واټه')]),
 mcq(pair('Resistance of a wire is r ohms. The wire is stretched to double its length, then its resistance in ohms is', 'ایک تار کی مزاحمت r اوہم ہے۔ تار کو کھینچ کر اس کی لمبائی دوگنی کر دی جاتی ہے، تو اوہم میں اس کی مزاحمت ہو گی:', 'د یوه سیم مقاومت r اوم دی. سیم داسې غځول کېږي چې اوږدوالی یې دوه برابره شي؛ نو مقاومت به یې په اوم کې څومره وي؟'),[
  pair(r'A. \(r/2\)',r'A. \(r/2\)',r'A. \(r/2\)'),pair(r'B. \(4r\)',r'B. \(4r\)',r'B. \(4r\)'),pair(r'C. \(2r\)',r'C. \(2r\)',r'C. \(2r\)'),pair(r'D. \(r/4\)',r'D. \(r/4\)',r'D. \(r/4\)')]),
 mcq(pair(r'\(10^6\) electrons are moving through a wire per second. The current developed is',r'\(10^6\) الیکٹران فی سیکنڈ تار میں سے گزر رہے ہیں۔ پیدا ہونے والی برقی رو ہے:',r'\(10^6\) الکترونونه په هره ثانیه کې له سیم څخه تېرېږي. پیدا شوی جریان دی:'),[
  pair(r'A. \(1.6\times10^{-19}\text{ A}\)',r'A. \(1.6\times10^{-19}\text{ A}\)',r'A. \(1.6\times10^{-19}\text{ A}\)'),pair(r'B. \(1\text{ A}\)',r'B. \(1\text{ A}\)',r'B. \(1\text{ A}\)'),pair(r'C. \(1.6\times10^{-13}\text{ A}\)',r'C. \(1.6\times10^{-13}\text{ A}\)',r'C. \(1.6\times10^{-13}\text{ A}\)'),pair(r'D. \(10^6\text{ A}\)',r'D. \(10^6\text{ A}\)',r'D. \(10^6\text{ A}\)')]),
 mcq(pair('When a wire is stretched and its radius becomes r/2, then its resistance will be', 'جب تار کو کھینچ کر اس کا رداس r/2 ہو جائے تو اس کی مزاحمت ہو گی:', 'کله چې سیم وغځول شي او شعاع یې r/2 شي، مقاومت به یې وي:'),[
  pair(r'A. \(16R\)',r'A. \(16R\)',r'A. \(16R\)'),pair(r'B. \(4R\)',r'B. \(4R\)',r'B. \(4R\)'),pair(r'C. \(2R\)',r'C. \(2R\)',r'C. \(2R\)'),pair('D. 0','D. 0','D. 0')]),
 mcq(pair('How much voltage is required to make 2 A flow through a resistance of 8 Ω?', '8 Ω مزاحمت میں 2 A برقی رو گزارنے کے لیے کتنا وولٹیج درکار ہے؟','د 8 Ω مقاومت له لارې د 2 A جریان د تېرولو لپاره څومره ولتاژ ته اړتیا ده؟'),[
  pair(r'A. \(16\text{ A}\,\Omega^{-1}\)',r'A. \(16\text{ A}\,\Omega^{-1}\)',r'A. \(16\text{ A}\,\Omega^{-1}\)'),pair(r'B. \(16\,\Omega\,\text{A}^{-1}\)',r'B. \(16\,\Omega\,\text{A}^{-1}\)',r'B. \(16\,\Omega\,\text{A}^{-1}\)'),pair(r'C. \(16\text{ A}\,\Omega\)',r'C. \(16\text{ A}\,\Omega\)',r'C. \(16\text{ A}\,\Omega\)'),pair(r'D. \(\text{A}^{-1}\,\Omega^{-1}\)',r'D. \(\text{A}^{-1}\,\Omega^{-1}\)',r'D. \(\text{A}^{-1}\,\Omega^{-1}\)')]),
 mcq(pair('A wire of uniform cross-section, area A, length L and resistance R is cut into two equal parts. The resistivity of each part will be', 'یکساں رقبۂ مقطع A، لمبائی L اور مزاحمت R والی تار کو دو برابر حصوں میں کاٹا جاتا ہے۔ ہر حصے کی مزاحمت النوعی ہو گی:', 'یو شان مقطع A، اوږدوالي L او مقاومت R لرونکی سیم په دوو مساوي برخو وېشل کېږي. د هرې برخې مخصوص مقاومت به وي:'),[
  pair('A. doubled','A. دوگنی','A. دوه برابره'),pair('B. halved','B. آدھی','B. نیمایي'),pair('C. remains the same','C. وہی رہتی ہے','C. هماغسې پاتې کېږي'),pair('D. one fourth','D. ایک چوتھائی','D. څلورمه برخه')]),
]

def add_record(identity,title,printed,pairs,layout,titles):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':46,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(n) for n in ([82] if printed==82 else [83])]
 return r,s

if __name__=='__main__':
 kp_layout=[{'type':'heading','indices':[0]}]+[{'type':'paragraph','indices':[i]} for i in range(1,len(KEYPOINTS))]
 k=add_record('phys12-unit12-key-points82','Key Points — Current Electricity',82,KEYPOINTS,kp_layout,('اہم نکات — کرنٹ الیکٹریسٹی','مهم ټکي — برېښنايي جریان'))
 pairs=[pair('EXERCISE — Choose the best possible answer','مشق — بہترین ممکنہ جواب منتخب کریں','تمرین — تر ټولو غوره ځواب وټاکئ')]
 layout=[{'type':'heading','indices':[0]}]
 card={'id':'phys12-unit12-mcq-pdf46','exercise':'Unit 12 MCQs 1–8','title':'Multiple-choice questions 1–8 (printed page 83)','problems':[],'sourceReferences':[ref(83)]}
 for n,q in enumerate(MCQS,1):
  stem_index=len(pairs);pairs.append(q['question']);layout.append({'type':'paragraph','indices':[stem_index]})
  opt_ids=[]
  choices=[]
  for choice in q['choices']:
   idx=len(pairs);pairs.append(choice);opt_ids.append(idx)
   label,text=choice[0].split('. ',1)
   choices.append({'label':label,'text':text,'textUrdu':choice[1].split('. ',1)[1],'textPashto':choice[2].split('. ',1)[1]})
  layout.append({'type':'list','indices':opt_ids})
  card['problems'].append({'id':f'physics12-mcq-{n}','qNo':str(n),'question':q['question'][0],
   'questionUrdu':q['question'][1],'questionPashto':q['question'][2],'choices':choices,'sourceReferences':[ref(83)]})
 m=add_record('phys12-unit12-mcq1-8-83','Multiple-choice exercise — questions 1–8',83,pairs,layout,('کثیر الانتخابی مشق — سوال 1–8','څو-ټاکنیزه تمرین — پوښتنې 1–8'))
 with shared_class_data_lock():
  upsert([k[0],m[0]],[k[1],m[1]],chapter_index=1)
  sync_companions(chapter_index=1,retire_sections=['12.11'],retire_exercises=['EXERCISE'],
   trim_sections=[{'id':'12.12','startsAt':'The resistivity of two wires','title':'Exercise continuation — printed page 84 pending review'}],
   exercises=[card])
 checkpoint(46,'corrected_verified',[k[0]['id'],m[0]['id']],'Rendered and inspected PDF page 46, printed pages 82–83. Compared all ten Key Points definitions/formulas and multiple-choice questions 1–8, including each printed option. Preserved source option wording and units, paired all text/options with Urdu and Pashto, upserted a translated question-bank card without adding answers, removed the corrupted duplicate legacy exercise card, retired its covered Key Points prefix and trimmed the remaining legacy exercise at the next unreviewed question on printed page 84.',printed_pages=[82,83],chapter_number=12)
