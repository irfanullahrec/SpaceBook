"""PDF149 printed292–293: triglyceride formation, waxes, compound and derived lipids, 21.4.2 structure (Table 21.2), 21.4.3 properties of lipids."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow149');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def lines(rows,kind='list'):
 s0=len(paras)
 for r in rows:paras.append(pair(*r))
 layout.append({'type':kind,'indices':list(range(s0,len(paras)))})
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'glycerol':('گلیسرول','ګلیسرول'),'fatty acid':('فیٹی ایسڈ','غوړ اسید'),'Triacylglycerol':('ٹرائی ایسائل گلیسرول','ټرای اسایل ګلیسرول'),'(triglyceride)':('(ٹرائی گلیسرائیڈ)','(ټرای ګلیسرایډ)'),
   'Name of Lipids/ Fatty Acids':('لپڈز/فیٹی ایسڈز کا نام','د لیپیډونو/غوړ اسیدونو نوم'),'Structure':('ساخت','جوړښت'),'Stearic acid':('سٹیرک ایسڈ','سټیریک اسید'),'Oleic acid':('اولیک ایسڈ','اولېیک اسید'),
   'Wax (from bee hive)':('موم (شہد کے چھتے سے)','موم (د مچیو له ځالې)'),'Phospholipids':('فاسفو لپڈز','فاسفو لیپیډونه'),'(saturated)':('(سیر شدہ)','(مشبوع)'),'phosphate group':('فاسفیٹ گروپ','فاسفېټ ګروپ'),'choline':('کولین','کولین')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def triglyc(lang):
 s=F.start(140)+t(200,30,'CH₂OH',15)+line(178,36,178,48)+t(240,62,'CHOH + 3RCOOH',15)+line(178,68,178,80)+t(200,96,'CH₂OH',15)+t(170,122,lb(lang,'glycerol'),12)+t(270,122,lb(lang,'fatty acid'),12)
 s+=F.arrow(340,450,58)+t(540,30,'CH₂COOR',15)+line(510,36,510,48)+t(580,62,'CHCOOR + 3H₂O',15)+line(510,68,510,80)+t(540,96,'CH₂COOR',15)+t(550,120,lb(lang,'Triacylglycerol'),12)+t(550,136,lb(lang,'(triglyceride)'),12)
 return s.replace('viewBox="0 0 850 140"','viewBox="0 0 850 145"')+'</svg>'
def table(lang):
 s=F.start(470)+'<rect x="1" y="1" width="848" height="468" fill="none" stroke="#222" stroke-width="1.5"/>'+'<rect x="1" y="1" width="848" height="46" fill="#fce4ec"/>'
 for y in (47,92,170,232):s+=line(0,y,850,y,1)
 s+=line(170,0,170,470,1)+t(85,28,lb(lang,'Name of Lipids/ Fatty Acids'),12)+t(510,30,lb(lang,'Structure'),14)
 s+=t(85,74,lb(lang,'Stearic acid'),13)+t(510,75,'CH₃(CH₂)₁₄COOH  '+lb(lang,'(saturated)'),15)
 s+=t(85,136,lb(lang,'Oleic acid'),13)+t(420,112,'CH₃(CH₂)₇',14)+line(450,118,475,132)+t(500,140,'C=C',15)+line(525,132,550,118)+t(600,112,'(CH₂)₇COOH',14)+line(487,146,480,154)+t(476,166,'H',13)+line(513,146,520,154)+t(524,166,'H',13)
 s+=t(85,206,lb(lang,'Wax (from bee hive)'),12)+t(510,215,'CH₃(CH₂)₂₈CH₂—O—C(CH₂)₁₄CH₃',15)+line(573,192,573,180)+line(579,192,579,180)+t(576,176,'O',12)
 s+=t(85,350,lb(lang,'Phospholipids'),13)
 L=lambda x,y,v:f'<text x="{x}" y="{y}" text-anchor="end" font-family="Arial,sans-serif" font-size="13" fill="#17212b">{v}</text>'
 s+=L(368,282,'H₃C—(CH₂)₁₄—')+t(375,282,'C',13)+t(420,282,'—O—',13)+t(470,282,'CH₂',13)+line(372,268,372,254)+line(378,268,378,254)+t(375,250,'O',11)
 s+=L(368,342,'H₃C—(CH₂)₃—C=C—(CH₂)₇—')+t(375,342,'C',13)+t(420,342,'—O—',13)+t(470,342,'C—H',13)+line(372,348,372,362)+line(378,348,378,362)+t(375,374,'O',11)+t(232,358,'H  H',11)
 s+=line(465,288,465,328)+line(465,348,465,396)+t(470,412,'H₂C',13)+t(515,412,'—O—',13)+t(560,412,'P',13)+t(590,412,'—O—',13)+t(700,412,'CH₂—CH₂—N⁺(CH₃)₃',13)
 s+=line(557,398,557,384)+line(563,398,563,384)+t(560,380,'O',11)+line(560,416,560,432)+t(560,446,'O⁻',11)
 s+='<rect x="440" y="262" width="60" height="160" fill="none" stroke="#333"/>'+t(470,462,lb(lang,'glycerol'),11)
 s+='<rect x="530" y="366" width="60" height="88" fill="none" stroke="#333"/>'+t(560,466,lb(lang,'phosphate group'),11)+'<rect x="612" y="394" width="180" height="26" fill="none" stroke="#333"/>'+t(700,466,lb(lang,'choline'),11)
 s+=t(300,252,lb(lang,'fatty acid'),11)+t(250,392,lb(lang,'fatty acid'),11)
 return s+'</svg>'

visual('chem12-p149-triglyceride-formation',triglyc)
add('(ii) Waxes','(ii) موم','(ii) موم','heading')
lines([('Wax is an ester of long-chain high molecular weight alcohol (usually mono-hydroxy) and a fatty acid.','موم لمبی زنجیر والی زیادہ سالماتی وزن کی الکوحل (عموماً مونو ہائیڈروآکسی) اور فیٹی ایسڈ کا ایسٹر ہے۔','موم د اوږد ځنځیر لرونکي لوړ مالیکولي وزن الکول (معمولاً مونو هایدروکسي) او یو غوړ اسید ایسټر دی.'),
 ('The acids and alcohols normally found in waxes have chains of the order of 12–34 carbon atoms in length.','موم میں عام طور پر پائے جانے والے ایسڈز اور الکوحلز کی زنجیروں کی لمبائی 12–34 کاربن ایٹموں کے لگ بھگ ہوتی ہے۔','هغه اسیدونه او الکولونه چې معمولاً په موم کې موندل کېږي د 12–34 کاربني اټومونو په اندازه ځنځیرونه لري.'),
 ('For example, bees wax and carnauba wax etc.','مثلاً شہد کی مکھی کا موم اور کارنوبا موم وغیرہ۔','د بېلګې په توګه د مچیو موم او کارنوبا موم او نور.')])
add('2. Compound Lipids','2. مرکب لپڈز','2. مرکب لیپیډونه','heading')
add('These are the esters of fatty acids with alcohols containing some additional groups, as well. These are further divided into.','یہ الکوحلز کے ساتھ فیٹی ایسڈز کے ایسٹرز ہیں جن میں کچھ اضافی گروپ بھی ہوتے ہیں۔ ان کی مزید تقسیم یہ ہے۔','دا له الکولونو سره د غوړ اسیدونو ایسټرونه دي چې ځینې اضافي ګروپونه هم لري. دا نور په لاندې ډول وېشل کېږي.')
lines([('i. Phospholipids: These lipids contain fatty acids, phosphoric acid, nitrogenous bases along with some other constituents. They are also called phosphatides.','i. فاسفو لپڈز: ان لپڈز میں فیٹی ایسڈز، فاسفورک ایسڈ، نائٹروجنی اساس اور کچھ دوسرے اجزا ہوتے ہیں۔ انہیں فاسفاٹائیڈز بھی کہتے ہیں۔','i. فاسفو لیپیډونه: دا لیپیډونه غوړ اسیدونه، فاسفوریک اسید، نایټروجني قلوي او ځینې نورې برخې لري. دوی ته فاسفاټایډونه هم وايي.'),
 ('ii. Glycolipids: They contain fatty acid, alcohol and carbohydrates. They are present in large amount in the white matter of brain and in the myelin sheaths of nerves.','ii. گلائیکو لپڈز: ان میں فیٹی ایسڈ، الکوحل اور کاربوہائیڈریٹس ہوتے ہیں۔ یہ دماغ کے سفید مادے اور اعصاب کے مائیلن غلافوں میں بڑی مقدار میں ہوتے ہیں۔','ii. ګلایکو لیپیډونه: دوی غوړ اسید، الکول او کاربوهایدرېټونه لري. د دماغ په سپین مادې او د عصبونو په مایلین پوښونو کې په زیاته اندازه شته.'),
 ('iii. Sulpholipids: They contain a sulphate group in addition to fatty acids, alcohol and carbohydrate.','iii. سلفو لپڈز: ان میں فیٹی ایسڈز، الکوحل اور کاربوہائیڈریٹ کے علاوہ ایک سلفیٹ گروپ ہوتا ہے۔','iii. سلفو لیپیډونه: دوی د غوړ اسیدونو، الکول او کاربوهایدرېټ سربېره یو سلفېټ ګروپ لري.'),
 ('iv. Lipo-Proteins: These are the complexes of lipids with proteins.','iv. لپو پروٹینز: یہ پروٹینز کے ساتھ لپڈز کے کمپلیکس ہیں۔','iv. لیپو پروټینونه: دا له پروټینونو سره د لیپیډونو کمپلېکسونه دي.')],'lines')
add('3. Derived Lipids','3. ماخوذ لپڈز','3. مشتق لیپیډونه','heading')
add('These are the substances derived by the hydrolysis of simple and compound lipids. These include fatty acids, alcohols, steroids, terpens, arytenoids etc.','یہ وہ مادے ہیں جو سادہ اور مرکب لپڈز کی ہائیڈرولائسز سے حاصل ہوتے ہیں۔ ان میں فیٹی ایسڈز، الکوحلز، سٹیرائیڈز، ٹرپینز، کیروٹینائیڈز وغیرہ شامل ہیں۔','دا هغه مواد دي چې د ساده او مرکب لیپیډونو له هایدرولایسس څخه اخیستل کېږي. په دې کې غوړ اسیدونه، الکولونه، سټېرایډونه، ټرپینونه، کاروټینوایډونه او نور شامل دي.')
add('21.4.2 Structure','21.4.2 ساخت','21.4.2 جوړښت','heading')
add('Lipid has no common structure. The most common occurring lipids are triglycerides and phospholipids. Triglycerides are fats and oils. Triglycerides have a glycerol backbone bonded to three fatty acids. If the three fatty acids are similar, the fats are called simple triglycerides. If the fatty acids are not similar, they are known as mixed triglycerides.','لپڈ کی کوئی مشترک ساخت نہیں۔ سب سے عام پائے جانے والے لپڈز ٹرائی گلیسرائیڈز اور فاسفو لپڈز ہیں۔ ٹرائی گلیسرائیڈز چکنائیاں اور تیل ہیں۔ ٹرائی گلیسرائیڈز میں گلیسرول کا ڈھانچہ تین فیٹی ایسڈز سے جڑا ہوتا ہے۔ اگر تینوں فیٹی ایسڈز یکساں ہوں تو چکنائیوں کو سادہ ٹرائی گلیسرائیڈز کہتے ہیں۔ اگر فیٹی ایسڈز یکساں نہ ہوں تو انہیں مخلوط ٹرائی گلیسرائیڈز کہتے ہیں۔','لیپیډ ګډ جوړښت نه لري. تر ټولو عام موندل کېدونکي لیپیډونه ټرای ګلیسرایډونه او فاسفو لیپیډونه دي. ټرای ګلیسرایډونه غوړي او تېل دي. ټرای ګلیسرایډونه د ګلیسرول ملا تیر لري چې له دریو غوړ اسیدونو سره تړلی دی. که درې واړه غوړ اسیدونه ورته وي، غوړي ساده ټرای ګلیسرایډونه بلل کېږي. که غوړ اسیدونه ورته نه وي، ګډ ټرای ګلیسرایډونه بلل کېږي.')
add('The second most common lipids are phospholipids. They are found in cell membrane of animals and plants. Phospholipids contain glycerol and fatty acids as well as phosphoric acid and low molecular weight alcohol. Some lipids and their structure are given in Table 21.2','دوسرے سب سے عام لپڈز فاسفو لپڈز ہیں۔ یہ جانوروں اور پودوں کی خلوی جھلی میں پائے جاتے ہیں۔ فاسفو لپڈز میں گلیسرول اور فیٹی ایسڈز کے ساتھ فاسفورک ایسڈ اور کم سالماتی وزن کی الکوحل بھی ہوتی ہے۔ چند لپڈز اور ان کی ساخت جدول 21.2 میں دی گئی ہے','دویم تر ټولو عام لیپیډونه فاسفو لیپیډونه دي. د ژویو او بوټو په حجروي غشا کې موندل کېږي. فاسفو لیپیډونه ګلیسرول او غوړ اسیدونه او همدارنګه فاسفوریک اسید او ټیټ مالیکولي وزن الکول لري. ځینې لیپیډونه او جوړښت یې په جدول 21.2 کې ورکړل شوي')
add('Table 21.2 Lipids and their Structure','جدول 21.2 لپڈز اور ان کی ساخت','جدول 21.2 لیپیډونه او جوړښت یې')
visual('chem12-table21-2',table)
add('21.4.3 Properties of Lipids','21.4.3 لپڈز کی خصوصیات','21.4.3 د لیپیډونو ځانګړنې','heading')
add('i. Physical Properties','i. طبعی خصوصیات','i. فزیکي ځانګړنې','heading')
lines([('Natural fats are colourless, odourless and tasteless.','قدرتی چکنائیاں بے رنگ، بے بو اور بے ذائقہ ہیں۔','طبیعي غوړي بې رنګه، بې بویه او بې خونده دي.'),
 ('They are insoluble in water but are highly soluble in organic solvents like benzene, ether, chloroform etc.','یہ پانی میں ناحل پذیر لیکن بینزین، ایتھر، کلوروفارم وغیرہ جیسے نامیاتی محللوں میں بہت حل پذیر ہیں۔','دوی په اوبو کې نه حلېږي خو په عضوي محللونو لکه بنزین، ایتر، کلوروفورم او نورو کې ډېر حلېږي.'),
 ('They have well defined melting and solidifying points.','ان کے نقطۂ پگھلاؤ اور انجماد واضح طور پر متعین ہیں۔','دوی د ویلې کېدو او جامد کېدو ښه ټاکلي ټکي لري.'),
 ('They have low specific gravity and, therefore, float on the surface of water.','ان کی مخصوص کثافت کم ہے اس لیے یہ پانی کی سطح پر تیرتے ہیں۔','دوی ټیټ مخصوص وزن لري، نو د اوبو پر سطحه لامبو وهي.')])
add('ii. Chemical Properties','ii. کیمیائی خصوصیات','ii. کیمیاوي ځانګړنې','heading')
add('Hydrolysis','ہائیڈرولائسز','هایدرولایسس','heading')
add('Natural fats undergo hydrolysis with acids or bases in boiling water where they produce free acids and glycerol.','قدرتی چکنائیاں ابلتے پانی میں تیزابوں یا اساسوں سے ہائیڈرولائز ہو کر آزاد ایسڈز اور گلیسرول بناتی ہیں۔','طبیعي غوړي په ایشېدونکو اوبو کې له اسیدونو یا قلویاتو سره هایدرولایز کېږي او ازاد اسیدونه او ګلیسرول تولیدوي.')
record=section('21.11','Lipid classification, structure and properties','لپڈز کی درجہ بندی، ساخت اور خصوصیات','د لیپیډونو ډلبندي، جوړښت او ځانګړنې',paras,layout,blocks,'292–293')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':149,'printedPages':[292,293]}]
record['sourceContinuesOnPdfPage']=150
issues=[{'id':'chem12-p292-printing','printedPage':292,'description':'Triacylglycerol drawn as CH₂COOR/CHCOOR (ester linkage written C–COOR rather than C–OCOR) and "arytenoids" (carotenoids) in derived lipids; retained as printed.'}]
carry=[{'from':'21.11','to':'21.12','startsAt':'In case of base hydrolysis'}]
if __name__=='__main__':save(149,[record],carry=carry,issues=issues,chapter_number=21)
