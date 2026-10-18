"""PDF104 printed200–201: acid strength of alcohols; preparations — hydration, hydrolysis, Grignard, reduction of carbonyls."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig,_w
F=Fig('arrow104');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),'primary alcohol':('ابتدائی الکوحل','لومړنی الکول'),'secondary alcohol':('ثانوی الکوحل','دویمی الکول'),'tertiary alcohol':('ثالثی الکوحل','درېیمی الکول'),
   'Increasing acid strength':('بڑھتی تیزابی طاقت','زیاتېدونکی تېزابي قوت'),'no reaction':('کوئی تعامل نہیں','هېڅ تعامل نشته'),'ethene':('ایتھین (دوہرا بند)','ایتین'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),
   'methyl iodide':('میتھائل آئیوڈائیڈ','میتایل ایوډایډ'),'Grignard reagent':('گرینیارڈ عامل','ګرینیارډ عامل'),'aldehyde/ketone':('الڈیہائیڈ/کیٹون','الدیهاید/کیټون'),'addition product':('اضافی پیداوار','اضافي محصول'),
   'alcohol':('الکوحل','الکول'),'(workup)':('(ورک اپ)','(ورک اپ)'),'ester':('ایسٹر','ایسټر'),'formaldehyde':('فارم الڈیہائیڈ','فورمالدیهاید')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def lay(x,y,l,r,size=16):
 toks=[l,'—','C','—',r] if l else ['—','C','—']
 tot=sum(_w(k) for k in toks);cx=x-tot/2;out='';cc=0
 for k in toks:
  w=_w(k);out+=t(cx+w/2,y,k,size)
  if k=='C':cc=cx+w/2
  cx+=w
 return out,cc
def carbonyl(x,y,l='',r=''):o,c=lay(x,y,l,r);return o+t(c,y-36,'O',14)+line(c-3,y-30,c-3,y-15)+line(c+3,y-30,c+3,y-15)
def tetra(x,y,top,l,r,bot):o,c=lay(x,y,l,r);return o+t(c,y-36,top,14)+line(c,y-30,c,y-15)+line(c,y+7,c,y+22)+t(c,y+38,bot,14)
def acid(lang):
 s=F.start(170)
 for x,(top,left,bot,name) in zip((110,320,540,750),(('H','H','H','methyl alcohol'),('H','R','H','primary alcohol'),('R','R','H','secondary alcohol'),('R','R','R','tertiary alcohol'))):
  s+=tetra(x,60,top,left,'OH',bot)+t(x,118,lb(lang,name),12)
 s+='<polygon points="740,135 120,135 120,128 80,145 120,162 120,155 740,155" fill="white" stroke="#222"/>'+t(420,150,lb(lang,'Increasing acid strength'),13,'#ad1457')
 return s+'</svg>'
def noreact(lang):return F.start(60)+t(300,35,'R—OH  +  NaOH',17)+F.arrow(400,500,29)+t(600,35,lb(lang,'no reaction'),15)+'</svg>'
def hydration(lang):return F.start(80)+t(220,35,'H₂C=CH₂ + H₂O',17)+t(170,58,lb(lang,'ethene'),12)+F.arrow(330,430,29,'H₂SO₄','100°C')+t(560,35,'CH₃—CH₂—OH',17)+t(560,58,lb(lang,'ethyl alcohol'),12)+'</svg>'
def hydrolysis(lang):return F.start(80)+t(220,35,'CH₃—I + KOH',17)+t(190,58,lb(lang,'methyl iodide'),12)+F.arrow(320,420,29,'Δ','H₂O')+t(560,35,'CH₃—OH + KI',17)+t(540,58,lb(lang,'methyl alcohol'),12)+'</svg>'
def grignard(lang):
 s=F.start(170)+t(100,90,'R—MgX  +',16)+t(70,140,lb(lang,'Grignard reagent'),12)+carbonyl(220,90)+t(220,140,lb(lang,'aldehyde/ketone'),12)+F.arrow(280,350,84)
 s+=tetra(430,90,'O⁻Mg⁺X','','','R')+t(430,152,lb(lang,'addition product'),12)+F.arrow(500,610,84,'H₃O⁺',lb(lang,'(workup)'))+tetra(690,90,'OH','','','R')+t(690,152,lb(lang,'alcohol'),12)
 return s+'</svg>'
def esters(lang):
 s=F.start(150)+t(80,90,'R—MgX  +',16)+carbonyl(220,90,'R/H','OR')+t(220,116,lb(lang,'ester'),12)+F.arrow(300,400,84,'','−MgX(OR)')
 s+=carbonyl(480,90,'R/H','R')+t(480,116,lb(lang,'aldehyde/ketone'),12)+F.arrow(560,650,84,'1. RMgX','2. H₃O⁺')+t(605,124,lb(lang,'(workup)'),12)+tetra(740,90,'OH','R/H','R','R')+t(740,146,lb(lang,'alcohol'),12)
 return s+'</svg>'
def reduce(lang):
 s=F.start(260)+carbonyl(160,60)+t(160,86,lb(lang,'aldehyde/ketone'),12)+F.arrow(300,520,54,'1. LiAlH₄ or NaBH₄, ether','2. H₂O')+tetra(640,60,'OH','','','H')+t(640,118,lb(lang,'alcohol'),12)
 s+=carbonyl(160,190)+t(230,190,'+ H₂',16)+t(160,216,lb(lang,'aldehyde/ketone'),12)+F.arrow(300,520,184,'Ni or Pt or Pd','200°C, 10 atm')+tetra(640,190,'OH','','','H')+t(640,248,lb(lang,'alcohol'),12)
 return s+'</svg>'
def formald(lang):
 return F.start(130)+carbonyl(200,60,'H','H')+t(200,86,lb(lang,'formaldehyde'),12)+F.arrow(300,480,54,'1. LiAlH₄, ether','2. H₂O')+tetra(600,60,'OH','H','H','H')+t(600,118,lb(lang,'methyl alcohol'),12)+'</svg>'

add('The alkyl group in alcohols releases electrons (electron donating group) towards the oxygen atom and therefore decreases the stability of conjugate base of alcohol, alkoxide ion. That is why the alcohols are less acidic than water. Tertiary alcohols are less acidic than secondary alcohols and secondary alcohols are less acidic than primary alcohols, because of the same electron donating effect of alkyl groups discussed above.',
 'الکوحلز میں الکائل گروپ آکسیجن ایٹم کی طرف الیکٹران دیتا ہے (الیکٹران دینے والا گروپ) اور اس لیے الکوحل کے مزدوج اساس، الکوآکسائیڈ آئن، کی پائیداری گھٹا دیتا ہے۔ اسی لیے الکوحلز پانی سے کم تیزابی ہیں۔ اوپر بیان کردہ الکائل گروپوں کے اسی الیکٹران دینے والے اثر کی وجہ سے ثالثی الکوحلز ثانوی سے اور ثانوی الکوحلز ابتدائی سے کم تیزابی ہیں۔',
 'په الکولونو کې الکایل ګروپ د اکسیجني اټوم په لور الکترونونه ورکوي (الکترون ورکوونکی ګروپ) او له همدې امله د الکول د مزدوجې قلوي، الکوکساید ایون، ثبات کموي. له همدې امله الکولونه له اوبو لږ تېزابي دي. د پورته یاد شوي الکایل ګروپونو د همدې الکترون ورکوونکي اغېز له امله درېیمي الکولونه له دویمیو او دویمي الکولونه له لومړنیو لږ تېزابي دي.')
visual('chem12-p104-acid-strength',acid)
add('It is to be noted that alcohols are not acidic enough to react with aqueous NaOH or KOH.','یاد رہے کہ الکوحلز اتنے تیزابی نہیں کہ آبی NaOH یا KOH سے تعامل کریں۔','د یادونې وړ ده چې الکولونه دومره تېزابي نه دي چې له اوبلن NaOH یا KOH سره تعامل وکړي.')
visual('chem12-p104-no-reaction',noreact)
add('18.1.5 Preparations of Alcohols','18.1.5 الکوحلز کی تیاری','18.1.5 د الکولونو چمتو کول','heading')
add('18.1.5.1 Hydration of Alkenes','18.1.5.1 الکینز کی ہائیڈریشن','18.1.5.1 د الکینونو هایدرېشن','heading')
add('Reaction of alkenes in the presence of sulphuric acid yield alcohol upon direct hydration (Section 16.5.7.3).','سلفیورک ایسڈ کی موجودگی میں الکینز (دوہرے بند والے) کا تعامل براہِ راست ہائیڈریشن پر الکوحل دیتا ہے (حصہ 16.5.7.3)۔','د سلفوریک اسید په شتون کې د الکینونو تعامل د مستقیم هایدرېشن پر مهال الکول ورکوي (برخه 16.5.7.3).')
visual('chem12-p104-hydration',hydration)
add('18.1.5.2 Hydrolysis of Alkyl halides','18.1.5.2 الکائل ہیلائیڈز کی ہائیڈرولائسز','18.1.5.2 د الکایل هالایډونو هایدرولیز','heading')
add('Alcohols can be prepared by the hydrolysis of alkyl halides by means of water or an aqueous alkali (Sections 17.1.6.3 and 17.1.6.4).','الکوحلز پانی یا آبی القلی کے ذریعے الکائل ہیلائیڈز کی ہائیڈرولائسز سے تیار کیے جا سکتے ہیں (حصے 17.1.6.3 اور 17.1.6.4)۔','الکولونه د اوبو یا اوبلن القلي په واسطه د الکایل هالایډونو د هایدرولیز له لارې چمتو کېدای شي (برخې 17.1.6.3 او 17.1.6.4).')
visual('chem12-p104-hydrolysis',hydrolysis)
add('18.1.5.3 Reaction of Grignard reagent with Aldehydes and Ketones','18.1.5.3 گرینیارڈ عامل کا الڈیہائیڈز اور کیٹونز سے تعامل','18.1.5.3 له الدیهایډونو او کیټونونو سره د ګرینیارډ عامل تعامل','heading')
add('Grignard reagent adds to the carbonyl group of aldehyde and ketone to form an addition compound which on acid workup gives an alcohol (Section 17.2.3.1).','گرینیارڈ عامل الڈیہائیڈ اور کیٹون کے کاربونل گروپ میں شامل ہو کر اضافی مرکب بناتا ہے جو تیزابی ورک اپ پر الکوحل دیتا ہے (حصہ 17.2.3.1)۔','ګرینیارډ عامل د الدیهاید او کیټون کاربونیل ګروپ ته ورزیاتېږي او اضافي مرکب جوړوي چې د اسیدي ورک اپ پر مهال الکول ورکوي (برخه 17.2.3.1).')
visual('chem12-p104-grignard',grignard)
add('Formaldehyde reacts with Grignard reagents to produce primary alcohols. Other aldehydes give secondary alcohols. Ketones on reaction with Grignard reagent produce tertiary alcohols.','فارم الڈیہائیڈ گرینیارڈ عاملین سے تعامل کر کے ابتدائی الکوحلز بناتا ہے۔ دوسرے الڈیہائیڈز ثانوی الکوحلز دیتے ہیں۔ کیٹونز گرینیارڈ عامل سے تعامل پر ثالثی الکوحلز بناتے ہیں۔','فورمالدیهاید له ګرینیارډ عاملونو سره تعامل کوي او لومړني الکولونه جوړوي. نور الدیهایډونه دویمي الکولونه ورکوي. کیټونونه له ګرینیارډ عامل سره په تعامل کې درېیمي الکولونه جوړوي.')
add('18.1.5.4 Reaction of Grignard reagent with Esters','18.1.5.4 گرینیارڈ عامل کا ایسٹرز سے تعامل','18.1.5.4 له ایسټرونو سره د ګرینیارډ عامل تعامل','heading')
add('Grignard reagents react with esters to yield carbonyl compounds (aldehydes and ketones). These carbonyl compounds react with more of the Grignard reagent in the same reaction mixture and yield alcohols as the final products. Formate ester give secondary while higher esters yield tertiary alcohols (Section 17.2.3.2).',
 'گرینیارڈ عاملین ایسٹرز سے تعامل کر کے کاربونل مرکبات (الڈیہائیڈز اور کیٹونز) دیتے ہیں۔ یہ کاربونل مرکبات اسی تعاملی آمیزے میں مزید گرینیارڈ عامل سے تعامل کر کے آخری پیداوار کے طور پر الکوحلز دیتے ہیں۔ فارمیٹ ایسٹر ثانوی جبکہ بڑے ایسٹرز ثالثی الکوحلز دیتے ہیں (حصہ 17.2.3.2)۔',
 'ګرینیارډ عاملونه له ایسټرونو سره تعامل کوي او کاربونیل مرکبات (الدیهایډونه او کیټونونه) ورکوي. دا کاربونیل مرکبات په همدې تعاملي ګډوله کې له نور ګرینیارډ عامل سره تعامل کوي او د وروستي محصول په توګه الکولونه ورکوي. فورمېټ ایسټر دویمي او لوړ ایسټرونه درېیمي الکولونه ورکوي (برخه 17.2.3.2).')
visual('chem12-p104-esters',esters)
add('18.1.5.5 Reduction of Aldehydes and Ketones','18.1.5.5 الڈیہائیڈز اور کیٹونز کی تخفیف','18.1.5.5 د الدیهایډونو او کیټونونو ارجاع','heading')
add('Carbonyl compounds (aldehydes and ketones) can easily be reduced to alcohols, either by hydrogenation in the presence of nickel, platinum or palladium catalysts at elevated temperature (200°C) and pressure (10 atmosphere); or by using reducing agents such as lithium aluminium hydride (LiAlH₄) or sodium borohydride (NaBH₄) in ether. Following reduction with LiAlH₄ or NaBH₄, a separate workup step with acid or even with pure water is required to liberate the alcohol product.',
 'کاربونل مرکبات (الڈیہائیڈز اور کیٹونز) کو آسانی سے الکوحلز میں تخفیف کیا جا سکتا ہے، یا تو بلند درجہ حرارت (200°C) اور دباؤ (10 کرۂ ہوائی) پر نکل، پلاٹینم یا پیلیڈیم عمل انگیزوں کی موجودگی میں ہائیڈروجینیشن سے، یا ایتھر میں لیتھیم ایلومینیم ہائیڈرائیڈ (LiAlH₄) یا سوڈیم بوروہائیڈرائیڈ (NaBH₄) جیسے تخفیفی عاملوں سے۔ LiAlH₄ یا NaBH₄ سے تخفیف کے بعد الکوحل پیداوار آزاد کرنے کے لیے تیزاب یا خالص پانی سے الگ ورک اپ مرحلہ درکار ہوتا ہے۔',
 'کاربونیل مرکبات (الدیهایډونه او کیټونونه) په اسانۍ الکولونو ته ارجاع کېدای شي، یا په لوړه تودوخه (200°C) او فشار (10 اتموسفیر) کې د نکل، پلاتین یا پالادیم کتلستونو په شتون کې د هایدروجینېشن په واسطه؛ یا په ایتر کې د ارجاع کوونکو عاملونو لکه لیتیم المونیم هایدراید (LiAlH₄) یا سوډیم بوروهایدراید (NaBH₄) په کارولو. د LiAlH₄ یا NaBH₄ سره له ارجاع وروسته د الکول محصول د ازادولو لپاره له اسید یا حتی خالصو اوبو سره جلا ورک اپ پړاو اړین دی.')
visual('chem12-p104-reduction',reduce)
add('Formaldehyde produces methyl alcohol, higher aldehydes give primary alcohols while ketones yield secondary alcohols.','فارم الڈیہائیڈ میتھائل الکوحل بناتا ہے، بڑے الڈیہائیڈز ابتدائی الکوحلز جبکہ کیٹونز ثانوی الکوحلز دیتے ہیں۔','فورمالدیهاید میتایل الکول جوړوي، لوړ الدیهایډونه لومړني الکولونه او کیټونونه دویمي الکولونه ورکوي.')
visual('chem12-p104-formaldehyde',formald)
record=section('18.4','Acidity trend and preparation of alcohols','الکوحلز کی تیزابیت کا رجحان اور تیاری','د الکولونو د تېزابیت رجحان او چمتو کول',paras,layout,blocks,'200–201')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':104,'printedPages':[200,201]}]
record['sourceContinuesOnPdfPage']=105
trim=[{'id':'18.5','startsAt':'R-C-H higher aldehyde'}]
if __name__=='__main__':save(104,[record],trim=trim,chapter_number=18)
