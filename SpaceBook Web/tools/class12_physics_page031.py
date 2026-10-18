from class12_source_review import upsert, section, checkpoint, sync_companions
from class12_physics_page013 import SOURCE, svg

COVER=[
 ('CURRENT ELECTRICITY','برقی رو','برېښنايي جریان'),
 ('How does an electric eel catch its prey?','برقی بام مچھلی اپنے شکار کو کیسے پکڑتی ہے؟','برېښنايي مارماهی خپل ښکار څنګه نیسي؟'),
]

OUTCOMES=[
 ('describe the concept of steady current.','مستقل برقی رو کا تصور بیان کریں۔','د ثابت برېښنايي جریان مفهوم بیانول.'),
 ("state Ohm’s law.",'اوہم کا قانون بیان کریں۔','د اوهم قانون بیانول.'),
 ('define resistivity and explain its dependence upon temperature.','مخصوص مزاحمت کی تعریف کریں اور درجۂ حرارت پر اس کا انحصار واضح کریں۔','مقاومت‌ځانګړتیا تعریفول او پر تودوخې یې تړاو تشریح کول.'),
 ('define conductance and conductivity of a conductor.','موصل کی موصلیت اور برقی چالکتا کی تعریف کریں۔','د هادي کنډکټانس او برېښنايي چالکتیا تعریفول.'),
 ('state the characteristics of a thermistor and its use to measure low temperatures.','تھرمسٹر کی خصوصیات اور کم درجۂ حرارت ناپنے میں اس کا استعمال بیان کریں۔','د ترمیسټر ځانګړنې او د ټیټې تودوخې د اندازه کولو لپاره یې کارونه بیانول.'),
 ('distinguish between e.m.f. and p.d. using energy considerations.','توانائی کے لحاظ سے برقی محرک قوت اور فرقِ پوٹینشل میں فرق کریں۔','د انرژۍ له مخې د الکتروموتوري قوې او پوتنشیالي توپیر ترمنځ توپیر کول.'),
 ('explain the internal resistance of sources and its consequences for external circuits.','منابع کی اندرونی مزاحمت اور بیرونی سرکٹوں پر اس کے نتائج بیان کریں۔','د سرچینو داخلي مقاومت او پر بهرنیو مدارونو یې اغېزې تشریح کول.'),
 ('describe some sources of e.m.f.','برقی محرک قوت کے چند ذرائع بیان کریں۔','د الکتروموتوري قوې ځینې سرچینې بیانول.'),
 ('describe the conditions for maximum power transfer.','زیادہ سے زیادہ طاقت کی منتقلی کی شرائط بیان کریں۔','د اعظمي توان د لېږد شرایط بیانول.'),
 ('describe a thermocouple and its function.','تھرموکپل اور اس کا کام بیان کریں۔','ترموکوپل او دنده یې بیانول.'),
 ('explain the variation of thermoelectric e.m.f. with temperature.','درجۂ حرارت کے ساتھ تھرمو الیکٹرک برقی محرک قوت کی تبدیلی واضح کریں۔','له تودوخې سره د ترموبرېښنايي الکتروموتوري قوې بدلون تشریح کول.'),
 ("apply Kirchhoff’s first law as conservation of charge to solve problems.",'مسائل حل کرنے کے لیے کرخوف کا پہلا قانون، بطور بقائے بار، استعمال کریں۔','د مسئلو د حل لپاره د چارج د بقا په توګه د کرخوف لومړی قانون کارول.'),
 ("apply Kirchhoff’s second law as conservation of energy to solve problems.",'مسائل حل کرنے کے لیے کرخوف کا دوسرا قانون، بطور بقائے توانائی، استعمال کریں۔','د مسئلو د حل لپاره د انرژۍ د بقا په توګه د کرخوف دویم قانون کارول.'),
 ('describe the working of a rheostat in a potential-divider circuit.','پوٹینشل ڈیوائیڈر سرکٹ میں ریوسٹیٹ کا کام بیان کریں۔','په پوتنشیال وېشونکي مدار کې د ریوستات کار بیانول.'),
 ('describe what a Wheatstone bridge is and how it is used to find an unknown resistance.','وہیٹ اسٹون برج کیا ہے اور نامعلوم مزاحمت معلوم کرنے کے لیے اسے کیسے استعمال کرتے ہیں؟','وېټسټون پل څه شی دی او د نامعلوم مقاومت د موندلو لپاره څنګه کارول کېږي؟'),
 ('describe the function of a potentiometer to measure and compare potentials without drawing any current from the circuit.','سرکٹ سے رو لیے بغیر پوٹینشل ناپنے اور موازنہ کرنے میں پوٹینشیومیٹر کا کام بیان کریں۔','له مداره د جریان له اخیستلو پرته د پوتنشیالونو د اندازه کولو او پرتله کولو لپاره د پوتنشیومیټر دنده بیانول.'),
]

STEADY=[
 ('Current electricity is the study of charges in motion. This unit explores electric current, the flow of electric charges in a metallic conductor. Simple electrical circuits can be solved by applying Ohm’s law. For other circuits, Kirchhoff’s rules are applied.', 'برقی رو حرکت کرتے باروں کا مطالعہ ہے۔ اس یونٹ میں برقی رو، یعنی دھاتی موصل میں برقی باروں کے بہاؤ کا جائزہ لیا جاتا ہے۔ سادہ برقی سرکٹ اوہم کے قانون سے حل کیے جا سکتے ہیں؛ دوسرے سرکٹوں کے لیے کرخوف کے قوانین استعمال ہوتے ہیں۔', 'برېښنايي جریان د خوځنده چارجونو مطالعه ده. په دې څپرکي کې برېښنايي جریان، یعنې په فلزي هادي کې د برېښنايي چارجونو بهیر څېړو. ساده برېښنايي مدارونه د اوهم په قانون حلېږي؛ د نورو مدارونو لپاره د کرخوف قوانین کارول کېږي.'),
 ('We all enjoy the comforts and benefits of using electricity. Electricity authorities use high-voltage transmission lines and transformers to distribute electricity to homes and industries in a town.', 'ہم سب بجلی کے استعمال سے ملنے والی سہولتوں سے فائدہ اٹھاتے ہیں۔ بجلی کے ادارے شہر کے گھروں اور صنعتوں تک بجلی پہنچانے کے لیے ہائی وولٹیج ترسیلی تاریں اور ٹرانسفارمر استعمال کرتے ہیں۔', 'موږ ټول د برېښنا له اسانتیاوو او ګټو خوند اخلو. د برېښنا ادارې په ښار کې کورونو او صنعتونو ته د برېښنا رسولو لپاره د لوړ ولتاژ لېږدوونکې کرښې او ټرانسفارمرونه کاروي.'),
 ('In this unit we shall briefly discuss the various features associated with moving charges.', 'اس یونٹ میں ہم حرکت کرتے باروں سے وابستہ مختلف خصوصیات کا مختصر جائزہ لیں گے۔', 'په دې څپرکي کې به د خوځنده چارجونو اړوند بېلابېلې ځانګړنې په لنډه توګه وڅېړو.'),
 ('12.1 STEADY CURRENT','12.1 مستقل برقی رو','12.1 ثابت برېښنايي جریان'),
 ('The continuous flow of free electrons is called steady current. The flow of electronic current can be explained by referring to Figure 12.1. A conductor has a large number of free electrons. When an electric field or voltage is applied, the negatively charged free electrons start moving towards the positive terminal around the circuit.', 'آزاد الیکٹرانوں کے مسلسل بہاؤ کو مستقل رو کہتے ہیں۔ الیکٹرانک رو کے بہاؤ کی وضاحت شکل 12.1 سے کی جا سکتی ہے۔ موصل میں بہت سے آزاد الیکٹران ہوتے ہیں۔ برقی میدان یا وولٹیج لگانے پر منفی بار والے آزاد الیکٹران سرکٹ میں مثبت ٹرمینل کی طرف حرکت شروع کرتے ہیں۔', 'د ازادو الکترونونو پرله‌پسې بهیر ته ثابت جریان ویل کېږي. د الکتروني جریان بهیر د شکل 12.1 په مرسته تشریح کېدای شي. په هادي کې ډېر ازاد الکترونونه وي. د برېښنايي میدان یا ولتاژ په لګېدو سره منفي چارج لرونکي ازاد الکترونونه په مدار کې د مثبت ټرمینل پر لور خوځېږي.'),
 ('This directed flow of electrons is called electric current.', 'الیکٹرانوں کے اس سمتی بہاؤ کو برقی رو کہتے ہیں۔', 'د الکترونونو دې سمتي بهیر ته برېښنايي جریان ویل کېږي.'),
 ('Following are the main points:', 'اہم نکات درج ذیل ہیں:', 'لاندې مهم ټکي دي:'),
 ('1. The actual direction of current is from the negative terminal to the positive terminal throughout the part of the circuit external to the cell. However, before electron theory, it was assumed that current flows from the positive terminal to the negative terminal of the cell via the circuit. This convention is so firmly established that it is still in use. This assumed direction is now called conventional current.', '1۔ خلیے کے باہر سرکٹ میں رو کی حقیقی سمت منفی ٹرمینل سے مثبت ٹرمینل کی طرف ہوتی ہے۔ تاہم الیکٹران نظریے سے پہلے یہ فرض کیا جاتا تھا کہ رو سرکٹ سے گزر کر خلیے کے مثبت ٹرمینل سے منفی ٹرمینل کی طرف جاتی ہے۔ یہ رواج اتنا مستحکم ہو چکا ہے کہ اب بھی استعمال ہوتا ہے۔ اس فرضی سمت کو رو کی روایتی سمت کہتے ہیں۔', '1. د حجرې څخه بهر په مدار کې د جریان حقیقي لوری له منفي ټرمینل څخه مثبت ټرمینل ته دی. خو د الکترونونو له نظریې مخکې داسې انګېرل کېده چې جریان د مدار له لارې د حجرې له مثبت ټرمینل څخه منفي ټرمینل ته ځي. دا دود دومره ټینګ شوی چې لا هم کارول کېږي. دې فرضي لوري ته قراردادي جریان ویل کېږي.'),
]

def electron_circuit(lang):
    labels={'en':('Free electrons','Flow of free electrons in a conductor'), 'ur':('آزاد الیکٹران','موصل میں آزاد الیکٹرانوں کا بہاؤ'), 'ps':('ازاد الکترونونه','په هادي کې د ازادو الکترونونو بهیر')}[lang]
    body='<path d="M55 205V80H445V205H265M245 205H55" fill="none" stroke="#cbd5e1" stroke-width="5"/><rect x="115" y="105" width="270" height="64" rx="28" fill="#b45309" stroke="#f97316" stroke-width="4"/>'
    for x in (150,205,260,315): body+=f'<path d="M{x} 136H{x+25}" stroke="#fde68a" stroke-width="4" marker-end="url(#a)"/>'
    body+='<path d="M55 170V115M445 115V170M355 205H300M190 205H135" stroke="#38bdf8" stroke-width="3" marker-end="url(#a)"/>'
    body+='<path d="M245 205V188M230 188H260M237 178H253M265 205V188M250 188H280M257 178H273M285 205V188M270 188H300M277 178H293" stroke="#f8fafc" stroke-width="3"/>'
    body+='<text x="173" y="143">→ e⁻</text><text x="189" y="96">'+labels[0]+'</text><text x="25" y="110">−</text><text x="450" y="110">+</text><text x="139" y="253">−</text><text x="380" y="253">+</text><text x="135" y="285">'+labels[1]+'</text>'
    return '<figure>'+svg(body,500,315,'Battery-driven electron flow through a conductor; electrons move from negative to positive terminal externally')+'<figcaption>FIGURE 12.1</figcaption></figure>'

if __name__=='__main__':
    records=[];sections=[]
    specs=[
      ('phys12-unit12-cover52','Unit 12 — Current Electricity',52,COVER,('برقی رو','برېښنايي جریان'),[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]}],None),
      ('phys12-unit12-outcomes52-53','Unit 12 — Learning outcomes',52,OUTCOMES,('سیکھنے کے نتائج','د زده کړې پایلې'),[{'type':'paragraph','indices':[i]} for i in range(len(OUTCOMES))],None),
      ('phys12-unit12-steady-current53','12.1 Steady current — introduction',53,STEADY,('12.1 مستقل برقی رو — تعارف','12.1 ثابت برېښنايي جریان — سریزه'),[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'visual'},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'paragraph','indices':[7]}],electron_circuit),
    ]
    for identity,title,printed,pairs,headings,layout,visual in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':31,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        item=section(record,pairs,layout,headings);item['kind']='lesson'
        if visual:
            item.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));item['content']+=visual('en')
        records.append(record);sections.append(item)
    upsert(records,sections,chapter_index=1)
    sync_companions(trim_sections=[{'id':'12.1','startsAt':'2. Those substances which have larger number of free electrons','title':'Learning outcomes, introduction and steady current (source review through PDF page 31)'}],chapter_index=1)
    checkpoint(31,'corrected_verified',[r['id'] for r in records],
      'Original spread rendered at 2.5x and inspected. Unit 12 cover title, subtitle, all 16 learning outcomes across printed pages 52–53, introduction, section 12.1 steady-current definition and direction/conventional-current paragraphs transcribed and aligned. Figure 12.1 rebuilt as native SVG; cover art excluded as decoration. Legacy topic trimmed after the reviewed page-53 text, preserving its continuation.',printed_pages=[52,53],chapter_number=12)
