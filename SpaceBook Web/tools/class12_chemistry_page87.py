"""PDF87 printed166–167: Table 7.1 boiling points; preparation of alkyl halides; reactivity (start)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow87');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'alcohol':('الکوحل','الکول'),'halogen acid':('ہیلوجن تیزاب','هالوجني اسید'),'alkyl halide':('الکائل ہیلائیڈ','الکایل هالایډ'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),
   'ethyl bromide':('ایتھائل برومائیڈ','ایتیل برومایډ'),'ethyl iodide':('ایتھائل آئیوڈائیڈ','ایتیل ایوډایډ'),'ethyl chloride':('ایتھائل کلورائیڈ','ایتیل کلوراید'),
   'anhydrous ZnCl₂':('بے آب ZnCl₂','بې اوبو ZnCl₂'),'phosphorous trihalides':('فاسفورس ٹرائی ہیلائیڈز','فاسفورس ټرای هالایډونه'),'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),
   'methyl chloride':('میتھائل کلورائیڈ','میتایل کلوراید'),'thionyl chloride':('تھائیونائل کلورائیڈ','تیونیل کلوراید'),'alkyl chloride':('الکائل کلورائیڈ','الکایل کلوراید'),'pyridine':('پیریڈین','پیریډین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def scheme(lang,rows,w=850):
 s=F.start(70*len(rows)+10,w)
 for i,(l,ln,cond,r,rn) in enumerate(rows):
  y=40+70*i;s+=t(200,y,l,17)+(t(200,y+22,'   '.join(lb(lang,x) for x in ln),12) if ln else '')
  s+=F.arrow(340,470,y-6,lb(lang,cond) if cond else '')+t(640,y,r,17)+(t(640,y+22,lb(lang,rn),12) if rn else '')
 return s+'</svg>'

tb={'id':'chem12-table17-1','headers':['Name','X=F','X=Cl','X=Br','X=I'],
 'rows':[['methyl halide','−78','−29','−4','42'],['ethyl halide','−38','13','38','72'],['n-propyl halide','−2','47','71','102'],['n-butyl halide','32','78','101','130'],['isopropyl halide','−9','34','59','89'],['isobutyl halide','25','69','91','120']],
 'translations':[{'language':'اردو','headers':['نام','X=F','X=Cl','X=Br','X=I'],'rows':[['میتھائل ہیلائیڈ','−78','−29','−4','42'],['ایتھائل ہیلائیڈ','−38','13','38','72'],['n-پروپائل ہیلائیڈ','−2','47','71','102'],['n-بیوٹائل ہیلائیڈ','32','78','101','130'],['آئسوپروپائل ہیلائیڈ','−9','34','59','89'],['آئسوبیوٹائل ہیلائیڈ','25','69','91','120']]},
                 {'language':'پښتو','headers':['نوم','X=F','X=Cl','X=Br','X=I'],'rows':[['میتایل هالایډ','−78','−29','−4','42'],['ایتیل هالایډ','−38','13','38','72'],['n-پروپیل هالایډ','−2','47','71','102'],['n-بیوټیل هالایډ','32','78','101','130'],['ایزوپروپیل هالایډ','−9','34','59','89'],['ایزوبیوټیل هالایډ','25','69','91','120']]}]}
add('Table 7.1 Boiling Points of Alkyl Halides — Boiling Point (°C)','جدول 7.1 الکائل ہیلائیڈز کے نقطۂ جوش — نقطۂ جوش (°C)','جدول 7.1 د الکایل هالایډونو د ایشېدو ټکي — د ایشېدو ټکی (°C)')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('17.1.4 Preparation of Alkyl Halides','17.1.4 الکائل ہیلائیڈز کی تیاری','17.1.4 د الکایل هالایډونو چمتو کول','heading')
add('Alkyl halides can be prepared by different methods. Some of these are given as under.','الکائل ہیلائیڈز مختلف طریقوں سے تیار کیے جا سکتے ہیں۔ ان میں سے چند درج ذیل ہیں۔','الکایل هالایډونه په بېلابېلو طریقو چمتو کېدای شي. ځینې یې لاندې ورکړل شوې.')
add('17.1.4.1 Reaction of alcohols with halogen halides','17.1.4.1 الکوحلز کا ہیلوجن ہیلائیڈز سے تعامل','17.1.4.1 له هالوجن هالایډونو سره د الکولونو تعامل','heading')
add('Alcohols react with halogen acids to form alkyl halides by replacement of hydroxyl group with halogen atom.','الکوحلز ہیلوجن تیزابوں سے تعامل کر کے ہائیڈروآکسل گروپ کو ہیلوجن ایٹم سے بدل کر الکائل ہیلائیڈز بناتے ہیں۔','الکولونه له هالوجني اسیدونو سره تعامل کوي او د هایدروکسیل ګروپ په هالوجني اټوم بدلولو سره الکایل هالایډونه جوړوي.')
visual('chem12-p87-hx-general',lambda l:scheme(l,[('R — OH  +  H — X',['alcohol','halogen acid'],'','R — X  +  H₂O','alkyl halide')]))
add('Reactivity of halogen acid increases with acid strength. In case of hydrogen chloride, anhydrous zinc chloride is used as catalyst while treating alcohol to produce alkyl chlorides. Tertiary alcohols are more reactive while primary alcohols are least reactive.',
 'ہیلوجن تیزاب کی تعامل پذیری تیزاب کی طاقت کے ساتھ بڑھتی ہے۔ ہائیڈروجن کلورائیڈ کی صورت میں الکوحل سے الکائل کلورائیڈز بنانے کے لیے بے آب زنک کلورائیڈ بطور عمل انگیز استعمال ہوتا ہے۔ ثالثی الکوحلز زیادہ تعامل پذیر جبکہ ابتدائی الکوحلز سب سے کم تعامل پذیر ہیں۔',
 'د هالوجني اسید تعامل وړتیا د اسید له قوت سره زیاتېږي. د هایدروجن کلوراید په حالت کې د الکول څخه د الکایل کلورایډونو د جوړولو پر مهال بې اوبو جست کلوراید د کتلست په توګه کارېږي. درېیمي الکولونه ډېر تعامل کوونکي او لومړني الکولونه تر ټولو لږ تعامل کوونکي دي.')
visual('chem12-p87-hx-examples',lambda l:scheme(l,[('CH₃—CH₂—OH + H—Br',['ethyl alcohol'],'','CH₃—CH₂—Br + H₂O','ethyl bromide'),('CH₃—CH₂—OH + H—I',['ethyl alcohol'],'','CH₃—CH₂—I + H₂O','ethyl iodide'),('CH₃—CH₂—OH + H—Cl',['ethyl alcohol'],'anhydrous ZnCl₂','CH₃—CH₂—Cl + H₂O','ethyl chloride')]))
add('17.1.4.2 Reactions of Alcohols with other Halogenating Agents (SOCl₂, PX₃)','17.1.4.2 دوسرے ہیلوجینیٹنگ عاملوں (SOCl₂، PX₃) سے الکوحلز کے تعاملات','17.1.4.2 له نورو هالوجن ورکوونکو عاملونو (SOCl₂، PX₃) سره د الکولونو تعاملونه','heading')
add('Conversion of alcohol to alkyl halides with halogen acid, has some limitations. In some cases, a side product is also formed due to rearrangement of intermediate carbocation. Secondly, alkenes are also formed as side product due to possible dehydration of alcohols (Section 16.5.5.1). The formation of these side products can be avoided by the use of phosphorus trihalides or thionyl chloride to replace the hydroxyl group with halogens.',
 'ہیلوجن تیزاب سے الکوحل کی الکائل ہیلائیڈز میں تبدیلی کی کچھ حدود ہیں۔ بعض صورتوں میں درمیانی کاربوکیٹائن کی ازسرنو ترتیب کی وجہ سے ایک ضمنی پیداوار بھی بنتی ہے۔ دوسرے، الکوحلز کی ممکنہ آب ربائی (حصہ 16.5.5.1) کی وجہ سے الکینز (دوہرے بند والے) بھی ضمنی پیداوار کے طور پر بنتے ہیں۔ ہائیڈروآکسل گروپ کو ہیلوجنز سے بدلنے کے لیے فاسفورس ٹرائی ہیلائیڈز یا تھائیونائل کلورائیڈ استعمال کر کے ان ضمنی پیداواروں سے بچا جا سکتا ہے۔',
 'له هالوجني اسید سره د الکول په الکایل هالایډونو بدلول ځینې محدودیتونه لري. په ځینو حالتونو کې د منځني کاربوکاټیون د بیا ترتیب له امله یو جانبي محصول هم جوړېږي. دویم، د الکولونو د ممکنه اوبو ایستلو (برخه 16.5.5.1) له امله الکینونه هم د جانبي محصول په توګه جوړېږي. د هایدروکسیل ګروپ په هالوجنونو د بدلولو لپاره د فاسفورس ټرای هالایډونو یا تیونیل کلوراید په کارولو د دې جانبي محصولاتو له جوړېدو مخنیوی کېدای شي.')
add('a. Reaction of alcohol with phosphorous trihalides','a. فاسفورس ٹرائی ہیلائیڈز سے الکوحل کا تعامل','a. له فاسفورس ټرای هالایډونو سره د الکول تعامل','heading')
add('Alcohols when treated with phosphorous trihalides, yield corresponding alkyl halides.','فاسفورس ٹرائی ہیلائیڈز سے عمل کرانے پر الکوحلز متعلقہ الکائل ہیلائیڈز دیتے ہیں۔','الکولونه چې له فاسفورس ټرای هالایډونو سره تعامل وکړي، اړوند الکایل هالایډونه ورکوي.')
visual('chem12-p87-px3',lambda l:scheme(l,[('3R—OH + PX₃',['alcohol','phosphorous trihalides'],'','3R—X + H₃PO₃','alkyl halide'),('3CH₃—OH + PCl₃',['methyl alcohol'],'','3CH₃—Cl + H₃PO₃','methyl chloride'),('3CH₃—CH₂—OH + PBr₃',['ethyl alcohol'],'','3CH₃—CH₂—Br + H₃PO₃','ethyl bromide')]))
add('Phosphorous tribromide and phosphorous triiodide are produced in situ by the reaction of red phosphorous with bromine and iodine respectively.','فاسفورس ٹرائی برومائیڈ اور فاسفورس ٹرائی آئیوڈائیڈ سرخ فاسفورس کے بالترتیب برومین اور آئیوڈین سے تعامل کے ذریعے in situ بنائے جاتے ہیں۔','فاسفورس ټرای برومایډ او فاسفورس ټرای ایوډایډ په ترتیب سره له برومین او ایوډین سره د سور فاسفورس د تعامل په واسطه in situ جوړېږي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('In chemistry, in situ typically means "in the reaction mixture". Some of the reactants are produced in situ or in the reaction mixture, because they may be unstable or toxic, if synthesized outside of the reaction mixture.','کیمیا میں in situ کا مطلب عموماً ”تعاملی آمیزے کے اندر“ ہے۔ بعض متعاملات in situ یعنی تعاملی آمیزے میں ہی بنائے جاتے ہیں، کیونکہ آمیزے سے باہر تیار کرنے پر وہ ناپائیدار یا زہریلے ہو سکتے ہیں۔','په کیمیا کې in situ معمولاً د ”تعاملي ګډولې دننه“ معنا لري. ځینې تعامل کوونکي in situ یا په تعاملي ګډوله کې جوړېږي، ځکه که له ګډولې بهر جوړ شي کېدای شي بې ثباته یا زهرجن وي.')
add('b. Reaction of alcohols with thionyl chloride','b. تھائیونائل کلورائیڈ سے الکوحلز کا تعامل','b. له تیونیل کلوراید سره د الکولونو تعامل','heading')
add('Alcohols react with thionyl chloride in the presence of pyridine to yield the corresponding alkyl chlorides. Pyridine being a base absorbs hydrogen chloride just after its production in the reaction mixture.','الکوحلز پیریڈین کی موجودگی میں تھائیونائل کلورائیڈ سے تعامل کر کے متعلقہ الکائل کلورائیڈز دیتے ہیں۔ پیریڈین اساس ہونے کی وجہ سے تعاملی آمیزے میں بنتے ہی ہائیڈروجن کلورائیڈ کو جذب کر لیتی ہے۔','الکولونه د پیریډین په شتون کې له تیونیل کلوراید سره تعامل کوي او اړوند الکایل کلورایډونه ورکوي. پیریډین د قلوي په توګه په تعاملي ګډوله کې د هایدروجن کلوراید له جوړېدو سمدستي وروسته جذبوي.')
visual('chem12-p87-socl2',lambda l:scheme(l,[('R—OH + SOCl₂',['alcohol','thionyl chloride'],'pyridine','R—Cl + SO₂ + HCl','alkyl chloride'),('CH₃—OH + SOCl₂',['methyl alcohol'],'pyridine','CH₃—Cl + SO₂ + HCl','methyl chloride'),('CH₃—CH₂—OH + SOCl₂',['ethyl alcohol'],'pyridine','CH₃—CH₂—Cl + SO₂ + HCl','ethyl bromide')]))
add('17.1.4.3 Free-Radical Halogenations of Alkanes','17.1.4.3 الکینز (اکیلے بند والے) کی آزاد ریڈیکل ہیلوجینیشن','17.1.4.3 د الکانونو د ازاد رادیکال هالوجینېشن','heading')
add('Alkanes react with halogens in the presence of ultraviolet light or at high temperature, to yield alkyl halides. In this process one or more hydrogen atoms of alkanes are replaced by halogens giving a mixture of different haloalkanes (Section 16.3.2). That is why it is not a good method for preparation of pure alkyl halides.',
 'الکینز (اکیلے بند والے) بالائے بنفشی روشنی کی موجودگی میں یا بلند درجہ حرارت پر ہیلوجنز سے تعامل کر کے الکائل ہیلائیڈز دیتے ہیں۔ اس عمل میں الکینز کے ایک یا زیادہ ہائیڈروجن ایٹم ہیلوجنز سے بدل کر مختلف ہیلو الکینز کا آمیزہ دیتے ہیں (حصہ 16.3.2)۔ اسی لیے یہ خالص الکائل ہیلائیڈز کی تیاری کا اچھا طریقہ نہیں۔',
 'الکانونه د ماورای بنفش رڼا په شتون کې یا په لوړه تودوخه کې له هالوجنونو سره تعامل کوي او الکایل هالایډونه ورکوي. په دې بهیر کې د الکانونو یو یا ډېر هایدروجني اټومونه په هالوجنونو بدلېږي او د بېلابېلو هالوالکانونو ګډوله ورکوي (برخه 16.3.2). له همدې امله دا د خالصو الکایل هالایډونو د چمتو کولو ښه طریقه نه ده.')
add('17.1.5 Reactivity of Alkyl halides','17.1.5 الکائل ہیلائیڈز کی تعامل پذیری','17.1.5 د الکایل هالایډونو تعامل وړتیا','heading')
add('Alkyl halides are reactive due to the polar nature of carbon-halogen (C⁺ᵟ – X⁻ᵟ) bond. The polarity is due to higher electronegativity of halogen than carbon atom, and therefore α–carbon of alkyl halides is electrophilic in nature.',
 'الکائل ہیلائیڈز کاربن–ہیلوجن (C⁺ᵟ – X⁻ᵟ) بند کی قطبی نوعیت کی وجہ سے تعامل پذیر ہیں۔ یہ قطبیت ہیلوجن کی کاربن ایٹم سے زیادہ برقی منفیت کی وجہ سے ہے، اس لیے الکائل ہیلائیڈز کا α–کاربن الیکٹروفائلی نوعیت کا ہوتا ہے۔',
 'الکایل هالایډونه د کاربن–هالوجن (C⁺ᵟ – X⁻ᵟ) تړون د قطبي طبیعت له امله تعامل کوونکي دي. دا قطبیت د کاربني اټوم په پرتله د هالوجن د لوړ الکترونېګاتیویټي له امله دی، نو د الکایل هالایډونو α–کاربن الکتروفایلي طبیعت لري.')
record=section('17.3','Boiling points and preparation of alkyl halides','الکائل ہیلائیڈز کے نقطۂ جوش اور تیاری','د الکایل هالایډونو د ایشېدو ټکي او چمتو کول',paras,layout,blocks,'166–167')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':87,'printedPages':[166,167]}]
record['sourceContinuesOnPdfPage']=88
issues=[{'id':'chem12-p166-table-number','printedPage':166,'description':'Table printed as "Table 7.1" (Unit 17); methyl bromide boiling point printed −4 °C (literature ≈ 4 °C) — printed values retained.'},
        {'id':'chem12-p167-ethyl-bromide-label','printedPage':167,'description':'Third SOCl₂ example product CH₃—CH₂—Cl is printed with the label "ethyl bromide"; retained as printed. Printed "phosphorous" spelling retained.'}]
if __name__=='__main__':save(87,[record],issues=issues,chapter_number=17)
