"""PDF162 printed318–319: reforming process, fractional distillation of petroleum (Figure 22.1), Table 22.3 fractions and uses."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow162');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
FR=[('Refinery Gas < 20°C','ریفائنری گیس < 20°C','د تصفیه خونې ګاز < 20°C'),('Petroleum Ether 20°C–60°C','پیٹرولیم ایتھر 20°C–60°C','پټرولیم ایتر 20°C–60°C'),('Naphtha 60°C–100°C','نیفتھا 60°C–100°C','نفتا 60°C–100°C'),
    ('Gasoline (Petrol) 80°C–180°C','گیسولین (پیٹرول) 80°C–180°C','ګازولین (پټرول) 80°C–180°C'),('Kerosine 160°C–300°C','مٹی کا تیل 160°C–300°C','د خاورو تېل 160°C–300°C'),('Diesel Oil 250°C–350°C','ڈیزل آئل 250°C–350°C','ډیزل تېل 250°C–350°C'),
    ('Lubricating Oil 300°C–370°C','چکنا کرنے والا تیل 300°C–370°C','غوړوونکي تېل 300°C–370°C'),('Fuel Oil 400°C–600°C','فیول آئل 400°C–600°C','فیول آیل 400°C–600°C'),('Residue > 600°C','باقیات > 600°C','پاتې شونې > 600°C')]
def col(lang):
 k={'en':0,'ur':1,'ps':2}[lang]
 s=F.start(470)+'<rect x="330" y="40" width="130" height="400" rx="30" fill="#ef9a9a" stroke="#555" stroke-width="2"/>'
 for i in range(9):
  y=60+i*42;s+=f'<path d="M345 {y+20} h20 v-8 h20 v8 h20 v-8 h20 v8 h20" fill="none" stroke="#5d4037" stroke-width="1.5"/>'+line(460,y+22,560,y+22,4,'#c62828')+t(650,y+18,FR[i][k],12)
 s+='<rect x="190" y="360" width="80" height="70" rx="12" fill="#ef5350" stroke="#555"/>'+line(270,400,330,400,3)+t(230,452,['Furnace','بھٹی','بټۍ'][k],12)+F.arrow(110,185,380)+t(140,368,['Crude Oil','خام تیل','خام تېل'][k],12)
 s+=t(395,28,['COOL (25°C)','ٹھنڈا (25°C)','سوړ (25°C)'][k],12)
 return s+'</svg>'

add('ii. Reforming Process','ii. ریفارمنگ کا عمل','ii. د ریفارمنګ عملیه','heading')
add('The process of reforming of hydrocarbon is carried out by using heat, pressure and/or catalyst in order to obtain desired products. In this process, heavy naphtha is converted into aromatics such as benzene, toluene and xylene as well as hydrogen as by-product. Reforming process breaks down the molecules of low octane rating naphtha into high octane gasoline blending components (reformates). It is one of the most important processes in oil refineries.','ہائیڈروکاربن کی ریفارمنگ کا عمل مطلوبہ مصنوعات حاصل کرنے کے لیے حرارت، دباؤ اور/یا عمل انگیز استعمال کر کے کیا جاتا ہے۔ اس عمل میں بھاری نیفتھا بینزین، ٹولوئین اور زائلین جیسے ارومیٹکس میں اور ضمنی پیداوار کے طور پر ہائیڈروجن میں بدلتا ہے۔ ریفارمنگ کا عمل کم اوکٹین درجے والے نیفتھا کے سالمات کو زیادہ اوکٹین والے گیسولین کے آمیزشی اجزا (ریفارمیٹس) میں توڑتا ہے۔ یہ تیل صاف کرنے کے کارخانوں کے اہم ترین عمل میں سے ایک ہے۔','د هایدروکاربن د ریفارمنګ عملیه د غوښتل شویو محصولاتو د ترلاسه کولو لپاره د تودوخې، فشار او/یا کتلست په کارولو ترسره کېږي. په دې عملیه کې درنه نفتا په اروماتیکونو لکه بنزین، ټولوین او زایلین او د ضمني محصول په توګه په هایدروجن بدلېږي. د ریفارمنګ عملیه د ټیټ اوکټین درجې نفتا مالیکولونه د لوړ اوکټین ګازولین په ګډوونکو برخو (ریفارمېټونو) ماتوي. دا د تېلو په تصفیه خونو کې یوه تر ټولو مهمه عملیه ده.')
add('Fractional Distillation of Petroleum','پیٹرولیم کی جزوی کشید','د پټرولیم جزوي تقطیر','heading')
add('Petroleum in the unrefined form is called crude oil. It is a naturally occurring thick viscous brown or greenish black liquid, which is obtained from earth crust. The crude oil consists of different substances. These substances in crude oil are miscible. Therefore they do not separate out into layers. Thus, fractional distillation, which is carried out in the fractionating towers, is used in refining petroleum. Fractional distillation is the process of heating up a mixture containing different substances with different boiling points and after condensation drawing the different fractions off. Each fraction is not a pure compound but is a mixture of different hydrocarbons with similar boiling points. Crude oil is first treated to remove the sulphur or sulphur compounds that may be present. The cleaned hydrocarbon material is then distilled and fractions with various boiling ranges are collected. (Figure 22.1).',
 'غیر صاف شدہ پیٹرولیم کو خام تیل کہتے ہیں۔ یہ قدرتی طور پر پایا جانے والا گاڑھا لیسدار بھورا یا سبزی مائل سیاہ مائع ہے جو زمین کی پرت سے حاصل ہوتا ہے۔ خام تیل مختلف مادوں پر مشتمل ہے۔ خام تیل میں یہ مادے باہم حل پذیر ہیں اس لیے یہ تہوں میں الگ نہیں ہوتے۔ لہٰذا پیٹرولیم کی صفائی میں جزوی کشید استعمال ہوتی ہے جو فریکشنیٹنگ ٹاورز میں کی جاتی ہے۔ جزوی کشید مختلف نقطۂ جوش والے مختلف مادوں پر مشتمل آمیزے کو گرم کرنے اور تکثیف کے بعد مختلف اجزا الگ نکالنے کا عمل ہے۔ ہر جز خالص مرکب نہیں بلکہ ملتے جلتے نقطۂ جوش والے مختلف ہائیڈروکاربنز کا آمیزہ ہے۔ خام تیل کو پہلے موجود سلفر یا سلفر کے مرکبات دور کرنے کے لیے صاف کیا جاتا ہے۔ پھر صاف شدہ ہائیڈروکاربن مادے کی کشید کی جاتی ہے اور مختلف نقطۂ جوش کی حدود والے اجزا جمع کیے جاتے ہیں۔ (شکل 22.1)۔',
 'نه تصفیه شوي پټرولیم ته خام تېل وايي. دا په طبیعي ډول موندل کېدونکی ټینګ چسپناک نسواري یا شنه مایل تور مایع دی چې د ځمکې له قشر ترلاسه کېږي. خام تېل له بېلابېلو موادو جوړ دي. په خامو تېلو کې دا مواد ګډېدونکي دي، نو په پوړونو نه جلا کېږي. له همدې امله د پټرولیم په تصفیه کې جزوي تقطیر کارېږي چې د فرکشنېټنګ په برجونو کې ترسره کېږي. جزوي تقطیر د بېلابېلو د ایشېدو ټکو لرونکو بېلابېلو موادو د ګډولې د تودولو او له تکاثف وروسته د بېلابېلو برخو د ایستلو عملیه ده. هره برخه خالص مرکب نه دی بلکې د ورته د ایشېدو ټکو لرونکو بېلابېلو هایدروکاربنونو ګډوله ده. خام تېل لومړی د شته سلفر یا سلفري مرکباتو د لرې کولو لپاره درملنه کېږي. بیا پاک شوي هایدروکاربني مواد تقطیر کېږي او د بېلابېلو د ایشېدو حدونو برخې راټولېږي. (شکل 22.1).')
visual('chem12-figure22-1',col)
add('Figure 22.1 Fractional distillation column.','شکل 22.1 جزوی کشید کا مینار۔','شکل 22.1 د جزوي تقطیر برج.')
add('The main goal of refinery operations is the production of gasoline. The principal fractions obtained during fractional distillation are given in Table 22.3.','ریفائنری کی کارروائیوں کا بنیادی مقصد گیسولین کی پیداوار ہے۔ جزوی کشید کے دوران حاصل ہونے والے بنیادی اجزا جدول 22.3 میں دیے گئے ہیں۔','د تصفیه خونې د عملیاتو اصلي موخه د ګازولین تولید دی. د جزوي تقطیر پر مهال ترلاسه شوې اصلي برخې په جدول 22.3 کې ورکړل شوې.')
add('Table 22.3 Fractions of Petroleum and their Important Uses','جدول 22.3 پیٹرولیم کے اجزا اور ان کے اہم استعمالات','جدول 22.3 د پټرولیم برخې او مهمې کارونې یې')
tb={'id':'chem12-table22-3','headers':['S. No.','Fraction','Number of carbon atoms per molecule','Boiling point (°C)','Important uses'],
 'rows':[['1','Refinery gas','C₁ to C₄','below 20','use as a fuel; making other organic compounds'],['2','Petroleum ether','C₅ – C₆','20–60','use as a solvent'],['3','Light naphtha','C₆ – C₇','60–100','use as a solvent; use as a raw material for making other petrochemicals'],
  ['4','Gasoline','C₇ – C₁₀','80–180','use as a motor fuel'],['5','Kerosene (Paraffin oil)','C₁₁ – C₁₅','160–300','use as a jet fuel; use for oil fired domestic heating'],['6','Heavy oil (Diesel oil, gas oil)','C₁₅ – C₁₈','250–350','use as a fuel for diesel engines; making greases, vaseline, candles etc'],
  ['7','Lubricating oil','C₁₈ – C₅₀','300–370','use for lubricating heavy machinery'],['8','Fuel oil','C₅₀ – C₇₀','400–600','use as fuel for ships and factories; use as industrial fuel'],['9','Residue (Solid mass)','More than C₇₀','above 600','metalling roads']],
 'translations':[{'language':'اردو','headers':['نمبر شمار','جز','فی سالمہ کاربن ایٹموں کی تعداد','نقطۂ جوش (°C)','اہم استعمالات'],
  'rows':[['1','ریفائنری گیس','C₁ سے C₄','20 سے کم','بطور ایندھن؛ دوسرے نامیاتی مرکبات بنانا'],['2','پیٹرولیم ایتھر','C₅ – C₆','20–60','بطور محلل'],['3','ہلکا نیفتھا','C₆ – C₇','60–100','بطور محلل؛ دوسرے پیٹرو کیمیکلز بنانے کے خام مال کے طور پر'],
   ['4','گیسولین','C₇ – C₁₀','80–180','بطور موٹر ایندھن'],['5','مٹی کا تیل (پیرافن آئل)','C₁₁ – C₁₅','160–300','بطور جیٹ ایندھن؛ تیل سے گھریلو حرارت'],['6','بھاری تیل (ڈیزل آئل، گیس آئل)','C₁₅ – C₁₈','250–350','ڈیزل انجنوں کے ایندھن کے طور پر؛ گریس، ویسلین، موم بتیاں وغیرہ بنانا'],
   ['7','چکنا کرنے والا تیل','C₁₈ – C₅₀','300–370','بھاری مشینری کو چکنا کرنے کے لیے'],['8','فیول آئل','C₅₀ – C₇₀','400–600','بحری جہازوں اور کارخانوں کے ایندھن کے طور پر؛ صنعتی ایندھن'],['9','باقیات (ٹھوس مادہ)','C₇₀ سے زیادہ','600 سے زیادہ','سڑکوں کی تعمیر (پختگی)']]},
  {'language':'پښتو','headers':['شمېره','برخه','په هر مالیکول کې د کاربني اټومونو شمېر','د ایشېدو ټکی (°C)','مهمې کارونې'],
  'rows':[['1','د تصفیه خونې ګاز','C₁ تر C₄','له 20 ښکته','د سونګ په توګه؛ د نورو عضوي مرکباتو جوړول'],['2','پټرولیم ایتر','C₅ – C₆','20–60','د محلل په توګه'],['3','سپکه نفتا','C₆ – C₇','60–100','د محلل په توګه؛ د نورو پټرو کیمیکلونو د جوړولو خام مواد'],
   ['4','ګازولین','C₇ – C₁₀','80–180','د موټر سونګ په توګه'],['5','د خاورو تېل (پارافین آیل)','C₁₁ – C₁₅','160–300','د جټ سونګ په توګه؛ د تېلو په واسطه کورنۍ ګرمول'],['6','درانه تېل (ډیزل، ګاز آیل)','C₁₅ – C₁₈','250–350','د ډیزل انجنونو سونګ؛ د ګریس، واسلین، شمعو او نورو جوړول'],
   ['7','غوړوونکي تېل','C₁₈ – C₅₀','300–370','د درنو ماشینونو غوړولو لپاره'],['8','فیول آیل','C₅₀ – C₇₀','400–600','د کښتیو او فابریکو سونګ؛ صنعتي سونګ'],['9','پاتې شونې (جامده کتله)','له C₇₀ ډېر','له 600 پورته','د سړکونو پخول']]}]}
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
record=section('22.5','Reforming, fractional distillation and petroleum fractions','ریفارمنگ، جزوی کشید اور پیٹرولیم کے اجزا','ریفارمنګ، جزوي تقطیر او د پټرولیم برخې',paras,layout,blocks,'318–319')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':162,'printedPages':[318,319]}]
record['sourceContinuesOnPdfPage']=163
record['sourceIllustrationReview']='Figure 22.1 distillation-column artwork re-drawn as labelled schematic SVG.'
carry=[{'from':'22.5','to':'22.6','startsAt':'Synthetic Polymers (PVC and Nylon)'}]
if __name__=='__main__':save(162,[record],carry=carry,chapter_number=22)
