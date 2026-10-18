"""PDF16: flame colours and GroupIIA atomic properties, printed24–25."""
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save
paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def head(en,ur,ps):add(en,ur,ps,'heading')
def table(block):blocks.append(block);layout.append({'type':'sourceDataTable','tableId':block['id']})
add('The smaller the positive ion, the higher the charge density and greater the effect on the carbonate ion. As we move down the group, the positive ions become bigger, so they have less effect on the carbonate ions near them. In other words, carbonates become more thermally stable down the group.',
    'مثبت آئن جتنا چھوٹا ہو، اس کی بار کثافت اتنی زیادہ اور کاربونیٹ آئن پر اثر اتنا بڑا ہوتا ہے۔ گروپ میں نیچے جانے پر مثبت آئن بڑے ہوتے ہیں، اس لیے قریب کے کاربونیٹ آئنوں پر ان کا اثر کم ہوتا ہے۔ دوسرے لفظوں میں، گروپ میں نیچے کاربونیٹس کا حرارتی استحکام بڑھتا ہے۔',
    'مثبت ایون چې هر څومره کوچنی وي، د چارج کثافت یې لوړ او پر کاربونېټ ایون یې اغېز ډېر وي. په ګروپ کې ښکته تګ سره مثبت ایونونه لویېږي، نو پر نږدې کاربونېټ ایونونو لږ اغېز لري. په بله وینا، په ګروپ کې ښکته د کاربونېټونو حرارتي ثبات زیاتېږي.')
head('Extension to Nitrates and Hydrogen Carbonates','نائٹریٹس اور ہائیڈروجن کاربونیٹس تک توسیع','نایټرېټونو او هایدروجن کاربونېټونو ته غځونه')
add('The phenomena of polarization is exactly the same for nitrates and hydrogen carbonates. The small positive ions at the top of the group polarize the nitrate or hydrogen carbonate ions to a greater extent than the larger positive ions at the bottom of the group. Again, the Group – IA compounds need more heat than those in Group – IIA because the Group – IA ions are less polarizing. Thus, thermal stability of anion of Group – I and Group – II increases down the group. The reason is increasing size and decreasing charge density of metal ions.',
    'نائٹریٹس اور ہائیڈروجن کاربونیٹس کے لیے قطبی بننے کا عمل بالکل یکساں ہے۔ گروپ کے اوپر کے چھوٹے مثبت آئن، نیچے کے بڑے مثبت آئنوں کی نسبت نائٹریٹ یا ہائیڈروجن کاربونیٹ آئنوں کو زیادہ قطبی بناتے ہیں۔ گروپ IA کے مرکبات کو گروپ IIA کے مرکبات سے زیادہ حرارت درکار ہے، کیونکہ گروپ IA کے آئن کم قطبی بناتے ہیں۔ چنانچہ گروپ I اور II کے منفی آئن کا حرارتی استحکام گروپ میں نیچے بڑھتا ہے۔ وجہ دھاتی آئنوں کی بڑھتی جسامت اور گھٹتی بار کثافت ہے۔',
    'د نایټرېټونو او هایدروجن کاربونېټونو لپاره د قطبي کېدو پدیده کټ مټ یو شان ده. د ګروپ په پاس کې کوچني مثبت ایونونه د لاندې لویو مثبت ایونونو په پرتله نایټرېټ یا هایدروجن کاربونېټ ایونونه ډېر قطبي کوي. بیا د IA ګروپ مرکبات د IIA ګروپ له مرکباتو ډېره تودوخه غواړي، ځکه د IA ګروپ ایونونه لږ قطبي کوي. نو د I او II ګروپ د منفي ایون حرارتي ثبات په ګروپ کې ښکته زیاتېږي. لامل یې د فلزي ایونونو لویېدونکې اندازه او کمېدونکی چارج کثافت دی.')
head('13.2.6 Flame Test: Origin of Flame Colours','13.2.6 شعلے کا امتحان: شعلے کے رنگوں کی ابتدا','13.2.6 د لمبې ازموینه: د لمبې د رنګونو سرچینه')
add('The Group–IA elements and their salts impart a characteristic colour to the Bunsen flame. These colours differ from one another as shown below.',
    'گروپ IA کے عناصر اور ان کے نمک بنسن کے شعلے کو مخصوص رنگ دیتے ہیں۔ یہ رنگ ایک دوسرے سے مختلف ہیں، جیسا کہ نیچے دکھایا گیا ہے۔',
    'د IA ګروپ عناصر او مالګې یې د بنسن لمبې ته ځانګړی رنګ ورکوي. دا رنګونه یو له بله توپیر لري، لکه لاندې چې ښودل شوي دي.')
add('Table 13.17 Characteristic Colour to Bunsen Flame of Group – IA Elements','جدول 13.17 گروپ IA کے عناصر کے بنسن شعلے کے مخصوص رنگ','جدول 13.17 د IA ګروپ د عناصرو د بنسن لمبې ځانګړي رنګونه')
table({'id':'chem12-table-13-17','headers':['Elements','Lithium Li','Sodium Na','Potassium K','Rubidium Rb','Cesium Cs'],'rows':[['Flame Colour','Crimson red','Golden yellow','Lilac','Red-violet','Blue-violet']],
       'translations':[{'language':'اردو','headers':['عناصر','لیتھیم Li','سوڈیم Na','پوٹاشیم K','روبیڈیم Rb','سیزیم Cs'],'rows':[['شعلے کا رنگ','گہرا سرخ','سنہری زرد','لیلکی','سرخ بنفشی','نیلا بنفشی']]},
                       {'language':'پښتو','headers':['عناصر','لیتیم Li','سوډیم Na','پوټاشیم K','روبیډیم Rb','سیزیم Cs'],'rows':[['د لمبې رنګ','ژور سور','زرین ژېړ','سپک بنفش','سور بنفش','آبي بنفش']]}]})
add('On heating Group – IA elements or its salt (especially chlorides due to its more volatile nature in a flame), the electrons are excited easily to higher energy levels because of absorption of energy. When these electrons return to their ground states, they emit extra energy in the form of radiations, which fall in the visible region, thereby, imparting a characteristic colour to the flame.',
    'گروپ IA کے عناصر یا ان کے نمک (خصوصاً کلورائیڈز، کیونکہ شعلے میں یہ زیادہ آسانی سے بخارات بنتے ہیں) گرم کرنے پر توانائی جذب کرتے ہیں اور ان کے الیکٹران آسانی سے بلند توانائی سطحوں پر برانگیختہ ہوتے ہیں۔ بنیادی حالت میں واپس آنے پر یہ اضافی توانائی مرئی خطے کی شعاعوں کی صورت میں خارج کرتے ہیں، جس سے شعلے کو مخصوص رنگ ملتا ہے۔',
    'د IA ګروپ د عناصرو یا مالګو په تودولو کې (په ځانګړي ډول کلورایډونه، ځکه په لمبه کې ډېر ژر بخار کېږي)، الکترونونه د انرژۍ د جذب له امله په اسانه لوړو انرژي کچو ته تحریکېږي. کله چې بنسټیزو حالتونو ته بېرته راګرځي، اضافي انرژي د وړانګو په بڼه خوشې کوي، چې په لیدل کېدونکې برخه کې وي؛ نو لمبې ته ځانګړی رنګ ورکوي.')
head('13.3 Group – IIA Elements','13.3 گروپ IIA کے عناصر','13.3 د IIA ګروپ عناصر')
add('Group-IIA elements are commonly called alkaline earth metals. They do not exist free in nature. They exist in combined form. Magnesium and calcium are very abundant in the rocks of Earth’s crust.',
    'گروپ IIA کے عناصر عموماً الکلائن ارتھ دھاتیں کہلاتے ہیں۔ یہ قدرت میں آزاد حالت میں نہیں، بلکہ مرکب صورت میں ہوتے ہیں۔ زمین کی پرت کی چٹانوں میں میگنیشیم اور کیلشیم بہت زیادہ ہیں۔',
    'د IIA ګروپ عناصر عموماً القلي ځمکني فلزونه بلل کېږي. دا په طبیعت کې ازاد نه وي، بلکې په مرکب بڼه وي. مګنیزیم او کلسیم د ځمکې د قشر په ډبرو کې ډېر پرېمانه دي.')
add('Elements of Group-IIA (alkaline earth metals) possess two electrons in the outermost (valence) s-orbital. They form di-positive ions by loss of both the electrons. The elements and their atomic number etc. are given in Table 13.18 below.',
    'گروپ IIA کے عناصر (الکلائن ارتھ دھاتیں) سب سے بیرونی ظرفی s آربیٹل میں دو الیکٹران رکھتے ہیں۔ دونوں الیکٹران کھو کر یہ دو مثبت بار والے آئن بناتے ہیں۔ عناصر اور ان کے ایٹمی نمبر وغیرہ نیچے جدول 13.18 میں دیے گئے ہیں۔',
    'د IIA ګروپ عناصر (القلي ځمکني فلزونه) په تر ټولو بهرني ظرفيتي s اوربیټال کې دوه الکترونونه لري. د دواړو الکترونونو په له لاسه ورکولو دوه مثبت چارج لرونکي ایونونه جوړوي. عناصر او اټومي شمېرې یې په لاندې جدول 13.18 کې ورکړل شوي دي.')
add('Table 13.18 The Electronic Configuration of Group – IIA Elements','جدول 13.18 گروپ IIA کے عناصر کی الیکٹرانی ترتیب','جدول 13.18 د IIA ګروپ د عناصرو الکتروني ترتیب')
rows=[['₄Be','1s², 2s²','[He]2s²'],['₁₂Mg','1s², 2s², 2p⁶, 3s²','[Ne]3s²'],['₂₀Ca','1s², 2s², 2p⁶, 3s², 3p⁶, 4s²','[Ar]4s²'],
      ['₃₈Sr','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶, 5s²','[Kr]5s²'],
      ['₅₆Ba','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶, 5s², 4d¹⁰, 5p⁶, 6s²','[Xe]6s²'],
      ['₈₈Ra','1s², 2s², 2p⁶, 3s², 3p⁶, 4s², 3d¹⁰, 4p⁶, 5s², 4d¹⁰, 5p⁶, 6s², 4f¹⁴, 5d¹⁰, 6p⁶, 7s²','[Rn]7s²']]
table({'id':'chem12-table-13-18','headers':['Elements symbol with atomic No','Electronic configuration',''],'headerRows':[[{'title':'Elements symbol with atomic No'},{'title':'Electronic configuration','colspan':2}]],'rows':rows,
       'translations':[{'language':'اردو','headers':['ایٹمی نمبر کے ساتھ عناصر کی علامتیں','الیکٹرانی ترتیب',''],'headerRows':[[{'title':'ایٹمی نمبر کے ساتھ عناصر کی علامتیں'},{'title':'الیکٹرانی ترتیب','colspan':2}]],'rows':rows},
                       {'language':'پښتو','headers':['د عناصرو سمبولونه له اټومي شمېر سره','الکتروني ترتیب',''],'headerRows':[[{'title':'د عناصرو سمبولونه له اټومي شمېر سره'},{'title':'الکتروني ترتیب','colspan':2}]],'rows':rows}]})
add('All Group – IIA metals except beryllium are white in colour. They are quite reactive and tarnish in air. The values of their densities, melting points and boiling points are higher than those of alkali metals.',
    'بیریلیم کے علاوہ گروپ IIA کی سب دھاتیں سفید ہیں۔ یہ کافی تعامل پذیر ہیں اور ہوا میں ان کی چمک ماند پڑتی ہے۔ ان کی کثافتیں اور پگھلنے اور ابلنے کے درجے الکلی دھاتوں سے زیادہ ہیں۔',
    'له بېریلیم پرته د IIA ګروپ ټول فلزونه سپین دي. دا نسبتاً ډېر تعامل کوونکي دي او په هوا کې خپله ځلا له لاسه ورکوي. کثافتونه، د وېلې کېدو او اېشېدو ټکي یې د القلي فلزونو په پرتله لوړ دي.')
head('13.3.1 Atomic and Physical Properties','13.3.1 ایٹمی اور طبعی خصوصیات','13.3.1 اټومي او فزیکي ځانګړنې')
head('13.3.1.1 Trend in Atomic Radius','13.3.1.1 ایٹمی رداس کا رجحان','13.3.1.1 د اټومي شعاع تمایل')
add('The atomic radii increase down the group due to the successive addition of extra shell of electrons to each element from Be to Ba.',
    'Be سے Ba تک ہر عنصر میں الیکٹرانوں کے اضافی خول کے مسلسل اضافے کی وجہ سے گروپ میں نیچے ایٹمی رداس بڑھتے ہیں۔',
    'له Be څخه Ba ته په هر عنصر کې د الکترونونو د اضافي پوښ د پرله پسې زیاتېدو له امله په ګروپ کې ښکته اټومي شعاعوې لویېږي.')
add('Table 13.19 Trend in Atomic Radius in Group – IIA Elements','جدول 13.19 گروپ IIA کے عناصر میں ایٹمی رداس کا رجحان','جدول 13.19 د IIA ګروپ په عناصرو کې د اټومي شعاع تمایل')
headers=['Elements','Be','Mg','Ca','Sr','Ba'];values=['112','150','197','215','217']
table({'id':'chem12-table-13-19','headers':headers,'rows':[['Atomic radius (pm)']+values],
       'translations':[{'language':'اردو','headers':['عناصر']+headers[1:],'rows':[['ایٹمی رداس (pm)']+values]},
                       {'language':'پښتو','headers':['عناصر']+headers[1:],'rows':[['اټومي شعاع (pm)']+values]}]})
head('13.3.1.2 Trend in First Ionization Energy','13.3.1.2 پہلی آئنائزیشن توانائی کا رجحان','13.3.1.2 د لومړۍ ایون کېدو انرژۍ تمایل')
add('The first ionization energy of these elements decreases with increase of atomic radii from Be to Ba.',
    'Be سے Ba تک ایٹمی رداس بڑھنے کے ساتھ ان عناصر کی پہلی آئنائزیشن توانائی کم ہوتی ہے۔',
    'له Be څخه Ba ته د اټومي شعاعوو په زیاتېدو سره د دې عناصرو د لومړۍ ایون کېدو انرژي کمېږي.')
add('Table 13.20 Trend in First Ionization Energy in Group IIA Elements','جدول 13.20 گروپ IIA کے عناصر میں پہلی آئنائزیشن توانائی کا رجحان','جدول 13.20 د IIA ګروپ په عناصرو کې د لومړۍ ایون کېدو انرژۍ تمایل')
values=['899.5','737.7','589.8','549.5','502.6']
table({'id':'chem12-table-13-20','headers':headers,'rows':[['1ˢᵗ Ionization energy (kJ/mol)']+values],
       'translations':[{'language':'اردو','headers':['عناصر']+headers[1:],'rows':[['پہلی آئنائزیشن توانائی (kJ/mol)']+values]},
                       {'language':'پښتو','headers':['عناصر']+headers[1:],'rows':[['د لومړۍ ایون کېدو انرژي (kJ/mol)']+values]}]})
head('13.3.1.3 Trend in Electronegativity','13.3.1.3 برقی منفیت کا رجحان','13.3.1.3 د برېښنا منفي توب تمایل')
add('The electronegativity values of these elements are small and decrease from Be to Ba.',
    'ان عناصر کی برقی منفیت کی قدریں کم ہیں اور Be سے Ba تک کم ہوتی ہیں۔',
    'د دې عناصرو د برېښنا منفي توب ارزښتونه ټیټ دي او له Be څخه Ba ته کمېږي.')
record=section('13.12','Flame test and Group IIA atomic properties','شعلے کا امتحان اور گروپ IIA کی ایٹمی خصوصیات','د لمبې ازموینه او د IIA ګروپ اټومي ځانګړنې',paras,layout,blocks,'24–25')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':16,'printedPages':[24,25]}]
if __name__=='__main__':save(16,[record],carry=[{'from':'13.12','to':'13.13','startsAt':'Table 13.21 Trend in Electronegativity'}])
