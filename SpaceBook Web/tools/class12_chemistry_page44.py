"""PDF44: printed80 project and Unit15 opening on right half."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
def build(identity,title,ut,pt,rows,blocks=None):
 paras=[pair(*r) for r in rows];layout=[{'type':'paragraph','indices':[i]} for i in range(len(rows))]
 return section(identity,title,ut,pt,paras,layout,blocks or [],'80 / Unit15 opening')
rows=[
('5. (a). Explain the oxidation states of copper.','5. (a). تانبے کی تکسیدی حالتیں واضح کریں۔','5. (a). د مسو د اکسیدېشن حالتونه روښانه کړئ.'),
('(b). Write down some important reactions of hexaaquacopper (II) ions with hydroxide ions, ammonia and carbonate ions.','(b). ہائیڈرو آکسائیڈ آئنوں، امونیا اور کاربونیٹ آئنوں سے ہیکسا ایکوا کاپر(II) آئنوں کے بعض اہم تعاملات لکھیں۔','(b). له هایدروکسایډ ایونونو، امونیا او کاربونېټ ایونونو سره د هېکسا اکوا مسو(II) ایونونو ځینې مهم تعاملونه ولیکئ.'),
('Project','منصوبہ','پروژه'),
('Take a small amount of powder hydrated copper sulphate salt and heat in container. The colour of the hydrated copper sulphate is deep blue. During heating the deep blue colour fads and ultimately disappear. Record your observations.','ہائیڈریٹڈ کاپر سلفیٹ نمک کے سفوف کی تھوڑی مقدار لیں اور برتن میں گرم کریں۔ اس کا رنگ گہرا نیلا ہے۔ گرم کرتے وقت گہرا نیلا رنگ مدھم ہوتا اور آخر غائب ہوتا ہے۔ مشاہدات درج کریں۔','د اوبه لرونکې مسو سلفېټ مالګې د پوډر لږه اندازه واخلئ او په لوښي کې یې توده کړئ. رنګ یې سخت نیلي دی. په تودولو سخت نیلي رنګ کمېږي او په پای کې ورکېږي. مشاهدې ثبت کړئ.'),
('1. Observe the colour change after heating and see what happened after heating.','1. گرم کرنے کے بعد رنگ کی تبدیلی دیکھیں اور کیا ہوا مشاہدہ کریں۔','1. له تودولو وروسته رنګي بدلون وګورئ او ووینئ چې څه پېښ شول.'),
('2. Why the deep blue colour of the copper disappears.','2. تانبے کا گہرا نیلا رنگ کیوں غائب ہوتا ہے۔','2. د مسو سخت نیلي رنګ ولې ورکېږي.'),
('3. Can you explain the reason of colour change?','3. کیا رنگ کی تبدیلی کی وجہ واضح کر سکتے ہیں؟','3. د رنګ د بدلون دلیل روښانه کولای شئ؟'),
('4. Add some water to the heated copper sulphate and observe what happened.','4. گرم کاپر سلفیٹ میں کچھ پانی ڈالیں اور کیا ہوا مشاہدہ کریں۔','4. تود شوي مسو سلفېټ ته لږې اوبه زیاتې کړئ او ووینئ چې څه پېښ شول.'),
('5. Explain why the deep blue colour reappears.','5. گہرا نیلا رنگ دوبارہ کیوں آتا ہے، واضح کریں۔','5. روښانه کړئ چې سخت نیلي رنګ ولې بېرته راځي.')]
project=build('14.18','Unit14 exercise continuation and project','یونٹ14 مشق کا تسلسل اور منصوبہ','د واحد14 تمرین دوام او پروژه',rows);project['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':44,'printedPage':80}]
rows=[('Unit 15 — Organic Compounds','یونٹ15 — نامیاتی مرکبات','واحد15 — عضوي مرکبات'),('After studying this unit, students will be able to:','یہ یونٹ پڑھنے کے بعد طلبہ اس قابل ہوں گے:','د دې واحد له لوستلو وروسته زده کوونکي به وکولای شي:'),
('Define organic chemistry and organic compounds. (Remembering)','نامیاتی کیمیا اور نامیاتی مرکبات کی تعریف کریں۔ (یاد کرنا)','عضوي کیمیا او عضوي مرکبات تعریف کړي. (یادول)'),
('Explain why there is such a diversity and magnitude of organic compounds. (Analyzing)','نامیاتی مرکبات کے اتنے تنوع اور کثرت کی وجہ واضح کریں۔ (تجزیہ)','روښانه کړي چې ولې عضوي مرکبات دومره تنوع او ډېروالی لري. (شننه)'),
('Classify organic compounds on structural basis. (Analyzing)','ساخت کی بنیاد پر نامیاتی مرکبات کی درجہ بندی کریں۔ (تجزیہ)','عضوي مرکبات د جوړښت له مخې ډلبندي کړي. (شننه)'),
('Explain the use of coal as a source of both aromatic and aliphatic hydrocarbons. (Understanding)','ارومیٹک اور ایلیفیٹک دونوں ہائیڈروکاربنوں کے ماخذ کے طور پر کوئلے کا استعمال واضح کریں۔ (سمجھنا)','د اروماتیکو او الیفاتیکو دواړو هایدروکاربنونو د سرچینې په توګه د ډبرو سکرو کارول روښانه کړي. (پوهېدل)'),
('Explain the use of plants as a source of organic compounds. (Understanding)','نامیاتی مرکبات کے ماخذ کے طور پر پودوں کا استعمال واضح کریں۔ (سمجھنا)','د عضوي مرکباتو د سرچینې په توګه د بوټو کارول روښانه کړي. (پوهېدل)'),
('Explain that organic compounds are also synthesized in the laboratory. (Understanding)','واضح کریں کہ نامیاتی مرکبات تجربہ گاہ میں بھی تیار ہوتے ہیں۔ (سمجھنا)','روښانه کړي چې عضوي مرکبات په لابراتوار کې هم جوړېږي. (پوهېدل)'),
('Define functional groups and homologous series. (Remembering)','فعلی گروپوں اور ہم سلسلہ خاندان کی تعریف کریں۔ (یاد کرنا)','فعالي ګروپونه او همولوګ لړۍ تعریف کړي. (یادول)')]
table={'id':'chem12-unit15-allocation','headers':['Teaching','Assessment','Weightage %'],'rows':[['3','1','3']],'translations':[{'language':'اردو','headers':['تدریس','جانچ','وزن %'],'rows':[['3','1','3']]},{'language':'پښتو','headers':['تدریس','ارزونه','وزن %'],'rows':[['3','1','3']]}]}
opening=build('chem12-u15-opening','Unit15 learning outcomes','یونٹ15 کے تعلیمی نتائج','د واحد15 د زده کړې پایلې',rows,[table]);opening['sourceLayout'].insert(1,{'type':'sourceDataTable','tableId':table['id']});opening['sourceChapterNumber']=15;opening['insertBefore']='15.1';opening['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':44,'printedPage':None,'position':'right Unit15 opening'}];opening['sourceCoverIllustrationReview']='Decorative molecular cover graphic inspected; exact chemical structure reconstruction unresolved. Do not claim this page fully verified.'
if __name__=='__main__':save(44,[project,opening],trim=[{'id':'15.1','sourceChapterNumber':15,'startsAt':'Introduction'}],issues=[{'id':'chem12-unit15-cover-molecules','pdfPage':44,'description':'Unit15 cover molecular artwork remains pending reconstruction/fidelity review; no scan embedded.'}],chapter_number=14)
