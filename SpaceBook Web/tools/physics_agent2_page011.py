from physics_agent2_sequential import save_page
from physics_agent2_translations import TRANSLATIONS,TITLES
from physics_agent2_layout import LAYOUT

PHOTO=[
 'Selenium is an insulator in the dark and become conductor when expose to light thus it is a photoconductor. The drum, charged with static electricity, can attract the toner particles.',
 'When the paper to be copied is laid on the glass plate, then the dark and light areas of the document produce same image on the drum as shown in figure 11.8. The dark areas retain their positive charge but light areas become conducting, lose their positive charge and become neutral.',
 'Thus the positive charge image of the document remains on the selenium surface.',
 'When a sheet of paper passes over the drum, the particles of toner are attached to it. Heated rollers then melt the toner into the paper to produce the permanent impression of the document.',
]
LASER=[
 'Laser printers use a laser to produce an image on the photoconducting drum as shown in Figure 11.9. In a laser printer, a laser beam is scanned across a photoconducting drum, leaving a positive charge image.',
 'The other steps for charging the drum and transferring the image to paper are the same as in xerography. Laser light can be very precisely controlled, enabling laser printers to produce high-quality images.',
]
INK=[
 'An inkjet printer is another type of printer that uses electric charges in its operation. In an inject printer tiny drops of ink are forced out of a fine nozzle, charged electrostatically and then passed between two oppositely charged plates; a negatively charged drop will be attracted towards a positive plate causing it to be deflected as shown in Figure:11.10.',
 'Whenever ink is to be placed on the paper, the charging control, responding to instructions from the computer, turns off the electric field. The uncharged droplets fly straight through the deflection plates and strike the paper.',
 'What are the basic differences between laser printer and photocopier?',
]

def prepare():
 TITLES.update({'phys12-front-photocopier12':('فوٹو کاپی مشین: عمل کی وضاحت','فوټو کاپي ماشین: د بهیر تشریح'),'phys12-front-laser12':('ب) لیزر پرنٹر','ب) لېزر چاپګر'),'phys12-front-inkjet13':('ج) انک جیٹ پرنٹر','ج) اېنک جېټ چاپګر')})
 TRANSLATIONS['phys12-front-photocopier12']=[
 ('سیلینیم اندھیرے میں عایق ہوتا ہے اور روشنی پڑنے پر موصل بن جاتا ہے، اس لیے یہ نوری موصل ہے۔ جامد برق سے بار دار ڈرم ٹونر کے ذرات کو اپنی طرف کھینچ سکتا ہے۔','سېلینیم په تیاره کې عایق وي او د رڼا په لګېدو هادي کېږي، نو دا نوري هادي دی. په ساکنې برېښنا چارج شوی ډرم د ټونر ذرې جذبولای شي.'),
 ('کاپی کیا جانے والا کاغذ شیشے کی تختی پر رکھنے سے دستاویز کے تاریک اور روشن حصے ڈرم پر ویسا ہی عکس بناتے ہیں، جیسا کہ شکل 11.8 میں ہے۔ تاریک حصے مثبت بار برقرار رکھتے ہیں، مگر روشن حصے موصل بن کر اپنا مثبت بار کھو دیتے ہیں اور غیر بار دار ہو جاتے ہیں۔','کله چې د کاپي کېدونکي سند کاغذ پر ښیښه کېښودل شي، د سند تیاره او روښانه برخې پر ډرم هماغه انځور جوړوي، لکه په شکل 11.8 کې. تیاره برخې خپل مثبت چارج ساتي، خو روښانه برخې هادي کېږي، مثبت چارج له لاسه ورکوي او خنثی کېږي.'),
 ('اس طرح سیلینیم کی سطح پر دستاویز کا مثبت بار والا عکس باقی رہتا ہے۔','په دې توګه د سند مثبت چارج لرونکی انځور د سېلینیم پر سطحه پاتې کېږي.'),
 ('جب کاغذ کی چادر ڈرم کے اوپر سے گزرتی ہے تو ٹونر کے ذرات اس سے چپک جاتے ہیں۔ گرم رولر ٹونر کو پگھلا کر کاغذ میں جذب کر دیتے ہیں، جس سے دستاویز کا مستقل نقش بن جاتا ہے۔','کله چې د کاغذ پاڼه پر ډرم تېرېږي، د ټونر ذرې ورپورې نښلي. ګرم رولرونه ټونر ویلي کوي او کاغذ ته یې ننباسي، څو د سند دایمي نقش جوړ شي.'),
 ]
 TRANSLATIONS['phys12-front-laser12']=[
 ('لیزر پرنٹر نوری موصل ڈرم پر عکس بنانے کے لیے لیزر استعمال کرتا ہے، جیسا کہ شکل 11.9 میں دکھایا گیا ہے۔ لیزر کی شعاع نوری موصل ڈرم پر اسکین کی جاتی ہے اور مثبت بار والا عکس چھوڑتی ہے۔','لېزر چاپګر د نوري هادي ډرم پر سر د انځور جوړولو لپاره لېزر کاروي، لکه په شکل 11.9 کې. د لېزر وړانګه پر نوري هادي ډرم سکېن کېږي او مثبت چارج لرونکی انځور پرېږدي.'),
 ('ڈرم کو بار دار کرنے اور عکس کو کاغذ پر منتقل کرنے کے باقی مراحل زیروگرافی جیسے ہوتے ہیں۔ لیزر کی روشنی کو نہایت درست انداز میں قابو کیا جا سکتا ہے، اس لیے لیزر پرنٹر اعلیٰ معیار کے عکس بناتے ہیں۔','د ډرم د چارج کولو او کاغذ ته د انځور د لېږد نور ګامونه د زېروګرافي په څېر دي. د لېزر رڼا په ډېر دقیق ډول کنټرولېدای شي، نو لېزر چاپګر د لوړ کیفیت انځورونه جوړوي.'),
 ]
 TRANSLATIONS['phys12-front-inkjet13']=[
 ('انک جیٹ پرنٹر ایک اور قسم کا پرنٹر ہے جو اپنے عمل میں برقی بار استعمال کرتا ہے۔ سیاہی کے چھوٹے قطرے باریک نوزل سے باہر نکالے جاتے ہیں، برقِ سکونی سے بار دار کیے جاتے ہیں اور پھر مخالف بار والی دو تختیوں کے درمیان سے گزارے جاتے ہیں۔ منفی بار والا قطرہ مثبت تختی کی طرف کھنچ کر منحرف ہو جاتا ہے، جیسا کہ شکل 11.10 میں ہے۔','اېنک جېټ چاپګر بل ډول چاپګر دی چې په خپل کار کې برېښنايي چارجونه کاروي. د رنګ واړه څاڅکي له نري نوزل څخه راوځي، په ساکنې برېښنا چارج کېږي او بیا د دوو مخالف چارج لرونکو تختو ترمنځ تېرېږي. منفي چارج لرونکی څاڅکی مثبتې تختې ته جذبېږي او منحرف کېږي، لکه په شکل 11.10 کې.'),
 ('جب سیاہی کاغذ پر ڈالنی ہو تو بار کا کنٹرول کمپیوٹر کی ہدایات کے مطابق برقی میدان بند کر دیتا ہے۔ غیر بار دار قطرے انحرافی تختیوں کے درمیان سے سیدھے گزر کر کاغذ سے ٹکراتے ہیں۔','کله چې رنګ پر کاغذ لګول کېږي، د چارج کنټرول د کمپیوټر د لارښوونو له مخې برېښنايي میدان بندوي. بې چارج څاڅکي د انحراف تختو ترمنځ نېغ تېرېږي او پر کاغذ لګېږي.'),
 ('لیزر پرنٹر اور فوٹو کاپی مشین کے بنیادی فرق کیا ہیں؟','د لېزر چاپګر او فوټو کاپي ماشین اساسي توپیرونه څه دي؟'),
 ]
 for key,paras in [('phys12-front-photocopier12',PHOTO),('phys12-front-laser12',LASER),('phys12-front-inkjet13',INK)]:
  LAYOUT[key]=[{'type':'paragraph','indices':[i]} for i in range(len(paras))]+[{'type':'visual'}]

def fig(n,caption):
 return [{'src':f'assets/physics12/figure-{n}.png','alt':caption,'caption':f'Figure {n}: {caption}'}]

def records():
 return [
 {'id':'phys12-front-photocopier12','printedPage':12,'title':'Photocopiers — Copying process','kind':'lesson','paragraphs':PHOTO,'figures':fig('11.8','A positive-charge image of the letter “A” is created on xerographic drum.')},
 {'id':'phys12-front-laser12','printedPage':[12,13],'title':'B) Laser printer','kind':'lesson','paragraphs':LASER,'figures':fig('11.9','Laser printer with a static laser scanning unit.')},
 {'id':'phys12-front-inkjet13','printedPage':13,'title':'C) Inkjet printers','kind':'lesson','paragraphs':INK,'figures':fig('11.10','Charging of ink droplets between two oppositely charged plates.'),'exercises':[{'id':'quiz-printers-11','title':'Quiz — Printers','problems':[{'id':'quiz-printers-11-q1','question':INK[2],'sourceReferences':[{'pdfPage':11,'printedPage':13}],'solutionOrigin':'not_provided_in_textbook'}]}]},
 ]

if __name__=='__main__':
 prepare()
 save_page(11,records())
