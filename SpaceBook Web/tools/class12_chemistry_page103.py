"""PDF103 printed198–199: physical properties of alcohols, Table 18.1, structure, acidity of alcohols."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow103');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'hydrophobic region':('آب گریز حصہ','اوبه نه منونکې سیمه'),'hydrophilic region':('آب دوست حصہ','اوبه خوښوونکې سیمه'),'water':('پانی','اوبه'),'methyl alcohol':('میتھائل الکوحل','میتایل الکول'),
   'alcohol':('الکوحل','الکول'),'sodium alkoxide':('سوڈیم الکوآکسائیڈ','سوډیم الکوکساید'),'ethyl alcohol':('ایتھائل الکوحل','ایتیل الکول'),'sodium ethoxide':('سوڈیم ایتھوآکسائیڈ','سوډیم ایتوکساید'),
   'hydroxide ion':('ہائیڈروآکسائیڈ آئن','هایدروکساید ایون'),'(conjugate base)':('(مزدوج اساس)','(مزدوجه قلوي)'),'alkoxide ion':('الکوآکسائیڈ آئن','الکوکساید ایون')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def hbond(lang):
 s=F.start(110)+t(300,30,'δ+',11)+t(300,48,'H',15)+t(330,62,'Ö:',16)+t(318,44,'δ−',11)+line(326,72,326,88)+t(326,104,'R',15)+t(400,62,'⋯⋯⋯⋯H — Ö:',16)+t(430,44,'δ+',11)+t(470,44,'δ−',11)+line(470,72,470,88)+t(470,104,'R',15)
 return s+'</svg>'
def solub(lang):
 s=F.start(230)+'<rect x="120" y="96" width="250" height="34" rx="16" fill="#f8bbd0" stroke="#222"/>'+t(245,119,'CH₃—CH₂—CH₂—CH₂—',15)
 s+='<ellipse cx="410" cy="113" rx="40" ry="34" fill="#b2ebf2" opacity=".8" stroke="#222"/>'+t(400,119,'O',16)+line(406,100,418,82)+t(424,78,'H',14)
 s+=t(330,40,'O',15)+line(324,46,314,60)+t(308,72,'H',13)+line(336,46,350,64)+t(356,76,'H',13)+t(500,40,'O',15)+line(494,46,482,58)+t(476,70,'H',13)+line(506,46,518,58)+t(524,70,'H',13)
 s+=t(410,170,'H',14)+line(410,154,410,146,1.5,'#222','stroke-dasharray="2 2"')+t(410,200,'O',15)+line(404,206,394,220)+line(416,206,426,220)
 s+=t(245,150,lb(lang,'hydrophobic region'),12,'#ad1457')+t(560,119,lb(lang,'hydrophilic region'),12,'#00838f')
 return s+'</svg>'
def struct(lang):
 s=F.start(170)
 for x,(ang,name,left,right) in zip((220,620),(('104.5°','water','H','H'),('108.9°','methyl alcohol','H₃C','H'))):
  s+=f'<ellipse cx="{x-12}" cy="40" rx="14" ry="20" fill="#5c6bc0" opacity=".8"/><ellipse cx="{x+12}" cy="40" rx="14" ry="20" fill="#5c6bc0" opacity=".8"/>'+t(x,82,'O',17)
  s+=line(x-8,86,x-50,110)+t(x-60,118,left,15)+line(x+8,86,x+50,110)+t(x+60,118,right,15)+t(x,128,ang,14,'#c62828')+t(x+70,70,'0.96Å',13)+t(x,158,lb(lang,name),12)
 return s+'</svg>'
def sodium(lang):
 s=F.start(150)+t(200,40,'2ROH  +  2Na',17)+t(160,62,lb(lang,'alcohol'),12)+F.arrow(320,420,34)+t(570,40,'2RO⁻Na⁺  +  H₂ ↑',17)+t(550,62,lb(lang,'sodium alkoxide'),12)
 s+=t(200,110,'2CH₃CH₂OH  +  2Na',17)+t(160,132,lb(lang,'ethyl alcohol'),12)+F.arrow(320,420,104)+t(590,110,'2CH₃CH₂O⁻Na⁺  +  H₂ ↑',17)+t(560,132,lb(lang,'sodium ethoxide'),12)
 return s+'</svg>'
def pka(lang):
 s=F.start(160)+t(180,40,'H₂O  +  H₂O',17)+t(140,62,lb(lang,'water'),12)+F.eq(280,380,34)+t(490,40,'HO⁻  +  H₃O⁺',17)+t(480,62,lb(lang,'hydroxide ion'),12)+t(480,78,lb(lang,'(conjugate base)'),12)+t(680,40,'pKa = 15.7',15)
 s+=t(180,115,'R—OH  +  H₂O',17)+t(140,137,lb(lang,'alcohol'),12)+F.eq(280,380,109)+t(490,115,'R—O⁻  +  H₃O⁺',17)+t(480,137,lb(lang,'alkoxide ion'),12)+t(480,153,lb(lang,'(conjugate base)'),12)+t(680,115,'pKa = 16-18',15)
 return s+'</svg>'

add('(Table 18.1). Among isomeric alcohols, the boiling points of straight chain alcohols are higher than that of branched.','(جدول 18.1)۔ ہم ترکیب الکوحلز میں سیدھی زنجیر والے الکوحلز کے نقطۂ جوش شاخ دار سے زیادہ ہیں۔','(جدول 18.1). په ایزومري الکولونو کې د مستقیم ځنځیر الکولونو د ایشېدو ټکي له څانګه لرونکو لوړ دي.')
add('The boiling points of alcohols are much higher than those of corresponding alkanes and alkyl halides. The high boiling points of is due to hydrogen bonding among the alcohol molecules.','الکوحلز کے نقطۂ جوش متعلقہ الکینز (اکیلے بند والے) اور الکائل ہیلائیڈز سے بہت زیادہ ہیں۔ زیادہ نقطۂ جوش الکوحل سالمات کے درمیان ہائیڈروجن بندش کی وجہ سے ہے۔','د الکولونو د ایشېدو ټکي له اړوندو الکانونو او الکایل هالایډونو ډېر لوړ دي. لوړ د ایشېدو ټکي د الکول د مالیکولونو ترمنځ د هایدروجني تړون له امله دي.','list')
visual('chem12-p103-alcohol-hbond',hbond)
add('Lower alcohols like methyl, ethyl and propyl alcohols are completely miscible with water. However the solubility of higher alcohols in water falls rapidly, due to increase in size of non-polar hydrophobic alkyl group.','میتھائل، ایتھائل اور پروپائل الکوحلز جیسے کم کاربن والے الکوحلز پانی میں مکمل طور پر قابلِ امتزاج ہیں۔ تاہم غیر قطبی آب گریز الکائل گروپ کا حجم بڑھنے کی وجہ سے بڑے الکوحلز کی پانی میں حل پذیری تیزی سے گھٹتی ہے۔','ټیټ الکولونه لکه میتایل، ایتیل او پروپیل الکولونه له اوبو سره په بشپړه توګه ګډېدونکي دي. خو د غیر قطبي اوبه نه منونکي الکایل ګروپ د اندازې د زیاتېدو له امله په اوبو کې د لوړو الکولونو حلېدنه په چټکۍ کمېږي.','list')
visual('chem12-p103-solubility',solub)
tb={'id':'chem12-table18-1','headers':['Name','Melting Point (°C)','Boiling Points (°C)'],
 'rows':[['methanol','−97','64'],['ethanol','−115','78'],['n-propyl alcohol','−126','97'],['n-butyl alcohol','−90','118'],['isopropyl alcohol','−89','82'],['isobutyl alcohol','−108','108'],['sec-butyl alcohol','−114','99'],['tert-butyl alcohol','−25.5','82'],['ethylene glycol','−12','197'],['glycerol','18','290']],
 'translations':[{'language':'اردو','headers':['نام','نقطۂ پگھلاؤ (°C)','نقطۂ جوش (°C)'],'rows':[['میتھانول','−97','64'],['ایتھانول','−115','78'],['n-پروپائل الکوحل','−126','97'],['n-بیوٹائل الکوحل','−90','118'],['آئسوپروپائل الکوحل','−89','82'],['آئسوبیوٹائل الکوحل','−108','108'],['سیکنڈری بیوٹائل الکوحل','−114','99'],['ٹرشری بیوٹائل الکوحل','−25.5','82'],['ایتھیلین گلائیکول','−12','197'],['گلیسرول','18','290']]},
                 {'language':'پښتو','headers':['نوم','د ویلې کېدو ټکی (°C)','د ایشېدو ټکی (°C)'],'rows':[['میتانول','−97','64'],['ایتانول','−115','78'],['n-پروپیل الکول','−126','97'],['n-بیوټیل الکول','−90','118'],['ایزوپروپیل الکول','−89','82'],['ایزوبیوټیل الکول','−108','108'],['سېکنډري بیوټیل الکول','−114','99'],['ټرشري بیوټیل الکول','−25.5','82'],['ایتیلین ګلایکول','−12','197'],['ګلیسرول','18','290']]}]}
add('Table 18.1 Boiling and Melting Points of Some Alcohols','جدول 18.1 بعض الکوحلز کے نقطۂ جوش اور نقطۂ پگھلاؤ','جدول 18.1 د ځینو الکولونو د ایشېدو او ویلې کېدو ټکي')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('18.1.3 Structure of Alcohols','18.1.3 الکوحلز کی ساخت','18.1.3 د الکولونو جوړښت','heading')
add('Alcohols are alkyl derivatives of water molecules. Water molecule has an angular structure with H–O–H bond angle of 104.5°, which is slightly smaller than tetrahedral angle. Alcohol molecules have a similar geometry where C–O–H angle is higher than 104.5°, and the hybridization of oxygen is sp³. For example the C–O–H bond angle in methyl alcohol is 108.9° (Figure 18.1). The C–O and O–H bond lengths are 142 pm (1.42 Å) and 96 pm (0.96 Å) respectively.',
 'الکوحلز پانی کے سالمات کے الکائل مشتقات ہیں۔ پانی کے سالمے کی ساخت زاویائی ہے جس میں H–O–H بند زاویہ 104.5° ہے، جو چہار سطحی زاویے سے قدرے کم ہے۔ الکوحل سالمات کی جیومیٹری بھی ایسی ہی ہے جس میں C–O–H زاویہ 104.5° سے زیادہ ہے اور آکسیجن کی ہائبرڈائزیشن sp³ ہے۔ مثلاً میتھائل الکوحل میں C–O–H بند زاویہ 108.9° ہے (شکل 18.1)۔ C–O اور O–H بندوں کی لمبائیاں بالترتیب 142 pm (1.42 Å) اور 96 pm (0.96 Å) ہیں۔',
 'الکولونه د اوبو د مالیکولونو الکایلي مشتقات دي. د اوبو مالیکول زاویه یي جوړښت لري چې د H–O–H تړون زاویه یې 104.5° ده، چې له څلورمخي زاویې یو څه کوچنۍ ده. د الکول مالیکولونه ورته جیومټري لري چې پکې د C–O–H زاویه له 104.5° لوړه ده او د اکسیجن هایبرېډیزېشن sp³ دی. د بېلګې په توګه په میتایل الکول کې د C–O–H تړون زاویه 108.9° ده (شکل 18.1). د C–O او O–H تړونونو اوږدوالي په ترتیب سره 142 pm (1.42 Å) او 96 pm (0.96 Å) دي.')
visual('chem12-figure18-1',struct)
add('Figure 18.1 Structure of water and methyl alcohol.','شکل 18.1 پانی اور میتھائل الکوحل کی ساخت۔','شکل 18.1 د اوبو او میتایل الکول جوړښت.')
add('18.1.4 Acidity of Alcohols','18.1.4 الکوحلز کی تیزابیت','18.1.4 د الکولونو تېزابیت','heading')
add('The acidic nature of alcohol is due to presence of polar oxygen-hydrogen (O–H) bond in alcohols. R—O⁻ᵟ—H⁺ᵟ This allows the release of hydrogen atom as proton. Due to this acidic behaviour, alcohols react with sodium or potassium to form alkoxide salt with the liberation of hydrogen gas.',
 'الکوحل کی تیزابی نوعیت الکوحلز میں قطبی آکسیجن–ہائیڈروجن (O–H) بند کی موجودگی کی وجہ سے ہے۔ R—O⁻ᵟ—H⁺ᵟ اس سے ہائیڈروجن ایٹم پروٹان کے طور پر خارج ہو سکتا ہے۔ اس تیزابی رویے کی وجہ سے الکوحلز سوڈیم یا پوٹاشیم سے تعامل کر کے ہائیڈروجن گیس کے اخراج کے ساتھ الکوآکسائیڈ نمک بناتے ہیں۔',
 'د الکول تېزابي طبیعت په الکولونو کې د قطبي اکسیجن–هایدروجن (O–H) تړون د شتون له امله دی. R—O⁻ᵟ—H⁺ᵟ دا د هایدروجني اټوم د پروټون په توګه ازادېدو ته اجازه ورکوي. د همدې تېزابي چلند له امله الکولونه له سوډیم یا پوټاشیم سره تعامل کوي او د هایدروجن ګاز له ازادېدو سره الکوکساید مالګه جوړوي.')
visual('chem12-p103-sodium-alkoxide',sodium)
add('However, alcohols are very weakly acidic, and even less acidic than water, as clear from pKa values.','تاہم الکوحلز بہت کمزور تیزابی ہیں، بلکہ پانی سے بھی کم تیزابی ہیں، جیسا کہ pKa اقدار سے واضح ہے۔','خو الکولونه ډېر کمزوري تېزابي دي، حتی له اوبو هم لږ تېزابي دي، لکه څنګه چې د pKa له ارزښتونو څرګندېږي.')
visual('chem12-p103-pka',pka)
record=section('18.3','Physical properties, structure and acidity of alcohols','الکوحلز کی طبعی خصوصیات، ساخت اور تیزابیت','د الکولونو فزیکي ځانګړنې، جوړښت او تېزابیت',paras,layout,blocks,'198–199')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':103,'printedPages':[198,199]}]
record['sourceContinuesOnPdfPage']=104
issues=[{'id':'chem12-p198-wording','printedPage':198,'description':'Printed "The high boiling points of is due to" retained in English.'}]
trim=[{'id':'18.4','startsAt':'The alkyl group in alcohols releases'}]
if __name__=='__main__':save(103,[record],trim=trim,issues=issues,chapter_number=18)
