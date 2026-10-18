from chemlib import *
c=cell
def ball(x,y,sg,r=14):
    col='#e88aa8' if sg=='+' else '#8cc8e8'
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#555"/>'+T(x,y+5,sg,14,'middle',700)
def grid(x0,y0,shift=0):
    o=''
    for j in range(4):
        for i in range(4):
            sg='+' if (i+j)%2==0 else '−'
            o+=ball(x0+i*36+(shift if j>=2 else 0),y0+j*36,sg)
    return o
f17=grid(30,40)+T(250,95,'Layer',11,'middle')+T(250,110,'slips',11,'middle')+'<path d="M215 120 h70" stroke="#2a6ab8" stroke-width="2"/>'+grid(330,40,18)+'<path d="M320 110 h180" stroke="#2a6ab8"/>'+T(520,20,'Crystal breaks here',9,'end')+'<path d="M40 5 l-25 25" stroke="#a04050" stroke-width="5"/>'+T(260,215,'Figure 6.17 An Ionic Crystal is Brittle and Breaks by Hammering',12,'middle',700,'#a02040')
dia='<polygon points="60,80 100,40 160,40 200,80 130,150" fill="#c8b8e8" stroke="#557"/><path d="M60 80 h140 M100 40 l30 40 l30 -40 M130 80 v70" stroke="#557" fill="none"/>'+T(130,170,'Diamond',11,'middle',700)
gra='<polygon points="260,70 400,55 400,115 260,100" fill="#555"/><polygon points="300,60 400,50 400,70 310,75" fill="#d88" /><rect x="260" y="75" width="140" height="25" fill="#333"/>'+T(340,150,'Graphite',11,'middle',700)
f18=dia+gra+T(215,205,'Figure 6.18 Diamond and Graphite',12,'middle',700,'#a02040')
def metal():
    o=''
    for j in range(5):
        for i in range(5):
            x=40+i*66+(j%2)*10;y=30+j*52
            o+=f'<circle cx="{x}" cy="{y}" r="15" fill="#8cc8e8" stroke="#468"/>'+T(x,y+5,'+',15,'middle',700)
            o+=f'<circle cx="{x+33}" cy="{y+14}" r="4" fill="#e0607a" stroke="#833"/><circle cx="{x+8}" cy="{y+24}" r="4" fill="#e0607a" stroke="#833"/>'
    return o+T(190,285,'Figure 6.19 Internal Structure of Metallic Solids',12,'middle',700,'#a02040')

s=page(207,'chem11-solids','Figures 6.17, 6.18 · 6.5.2 Covalent Solids','شکل 6.17، 6.18 · 6.5.2 ہم ذرّی ٹھوس','شکلونه 6.17، 6.18 · 6.5.2 کوولنټ جامدات','covalent-solids')
head(s,'h652','6.5.2 Covalent Solids','6.5.2 ہم ذرّی ٹھوس','6.5.2 کوولنټ جامدات')
add(s,'c1',f'In covalent solids (sometimes called covalent network crystals), atoms are{SO} held together entirely by covalent bonds in an extensive three-dimensional rigid{SO} network. No separate molecules are present in covalent solids, as in the case of{SO} molecular solids. Covalent bond in these crystals, are very strong and a huge{SO} amount of energy is needed to break these bonds. Some examples of covalent{SO} crystals are diamond, silicon carbide etc.',
 f'ہم ذرّی ٹھوس (جنہیں کبھی ہم ذرّی جالی قلم کہا جاتا ہے) میں ایٹم {SO} مکمل طور پر ہم ذرّی بندھنوں سے ایک وسیع سہ ابعادی سخت {SO} جال میں ایک ساتھ بندھے ہوتے ہیں۔ ہم ذرّی ٹھوس میں الگ سالمے موجود نہیں ہوتے، جیسا کہ سالماتی ٹھوس کی صورت میں ہوتا ہے {SO}۔ ان قلموں میں ہم ذرّی بندھن بہت مضبوط ہوتے ہیں اور انہیں توڑنے کے لیے بہت زیادہ توانائی درکار ہوتی ہے {SO}۔ ہم ذرّی قلموں کی کچھ مثالیں ہیرا، سلیکون کاربائیڈ وغیرہ ہیں {SO}۔',
 f'په کوولنټ جامداتو کې (چې ځینې وخت کوولنټ جالیزې کرسټالونه بلل کېږي) اتومونه {SO} په بشپړه توګه د کوولنټ بندونو په واسطه په یوه پراخه درې بعدي کلکه {SO} جالۍ کې یو ځای نیول شوي وي. په کوولنټ جامداتو کې جلا مالیکولونه نه شته، لکه څنګه چې په مالیکولي جامداتو کې وي {SO}. په دې کرسټالونو کې کوولنټ بندونه ډېر قوي دي او د دې بندونو ماتولو لپاره ډېره انرژي په کار ده {SO}. د کوولنټ کرسټالونو ځینې بېلګې الماس، سیلیکون کاربایډ او نور دي {SO}.')
add(s,'c2',f'Well-known examples are the two allotropes of carbon: diamond and{SO} graphite as shown in figure 6.18.',f'مشہور مثالیں کاربن کے دو دوسرے روپ ہیں: ہیرا اور {SO} گریفائٹ جیسا کہ شکل 6.18 میں دکھایا گیا ہے۔',f'مشهورې بېلګې د کاربن دوه المورفونه دي: الماس او {SO} ګرافایټ لکه څنګه چې په 6.18 شکل کې ښودل شوي.')
head(s,'ph','Properties of Covalent Solids','ہم ذرّی ٹھوس کی خصوصیات','د کوولنټ جامداتو ځانګړنې')
add(s,'p0','Properties of covalent solids are,','ہم ذرّی ٹھوس کی خصوصیات یہ ہیں،','د کوولنټ جامداتو ځانګړنې دا دي،')
pr=[('Covalent solids are also very hard and cannot be broken easily.','ہم ذرّی ٹھوس بھی بہت سخت ہوتے ہیں اور آسانی سے توڑے نہیں جا سکتے۔','کوولنټ جامدات هم ډېر کلک دي او په اسانۍ سره نه ماتېږي.'),
('They have high melting point and heat of fusion.','ان کا نقطۂ پگھلاؤ اور حرارتِ پگھلاؤ بلند ہوتا ہے۔','دوی لوړه د ویلې کېدو نقطه او د ویلې کېدو تودوخه لري.'),
('They are poor conductor of heat and electricity except graphite.','یہ حرارت اور بجلی کے ناقص موصل ہیں سوائے گریفائٹ کے۔','دا د تودوخې او برېښنا ضعیف تېرونکي دي پرته له ګرافایټ.'),
('They are usually insoluble in polar solvents.','یہ عموماً قطبی محللوں میں حل نہیں ہوتے۔','دا معمولاً په قطبي محللونو کې نه حل کېږي.')]
for i,(e,u,p) in enumerate(pr,1): add(s,f'p{i}',f'{i}. {e}',f'{i}۔ {u}',f'{i}. {p}')
s['figures']=[fig(207,'fig6-17',svg(520,230,'Ionic crystal layer slipping under a hammer blow so like charges align and the crystal breaks',f17),'Figure 6.17 An Ionic Crystal is Brittle and Breaks by Hammering','شکل 6.17 آئنی قلم بھربھرا ہوتا ہے اور ہتھوڑے سے ٹوٹ جاتا ہے','شکل 6.17 آیوني کرسټال ماتېدونکی دی او د چکوش په وهلو ماتېږي',[lab('Layer slips','تہہ پھسلتی ہے','طبقه الوځي'),lab('Crystal breaks here','قلم یہاں سے ٹوٹتا ہے','کرسټال دلته ماتېږي')]),
 fig(207,'fig6-18',svg(430,220,'Diamond and graphite as two allotropes of carbon',f18),'Figure 6.18 Diamond and Graphite','شکل 6.18 ہیرا اور گریفائٹ','شکل 6.18 الماس او ګرافایټ',[lab('Diamond','ہیرا','الماس'),lab('Graphite','گریفائٹ','ګرافایټ')])]
s['figures'][0]['sourceGap']=dict(note='Right edge of Fig. 6.17 is clipped (the "Crystal breaks here" label is partly cut); redrawn as a schematic.')
s['figures'][1]['sourceGap']=dict(note='Photographs of a diamond and a pencil tip redrawn as simple schematics; small labels on the photographs are blurred.')
s['flow']=[dict(type='figure',index=0),dict(type='paragraphs',ids=ids(s,0,3)),dict(type='figure',index=1),dict(type='paragraphs',ids=ids(s,3))]
s['sourceNote']='Printed folio 202. Right edge of the 6.5.2 paragraph is clipped by the page curl; clipped fragments marked [scan obscured]. A CamScanner watermark crosses the page. Photographs redrawn as schematics.'
s['vocabulary']={'covalent network crystal':{'ur':'ہم ذرّی جالی قلم','ps':'کوولنټ جالیزه کرسټال'},'allotrope':{'ur':'دوسرا روپ','ps':'المورف'},'diamond':{'ur':'ہیرا','ps':'الماس'},'graphite':{'ur':'گریفائٹ','ps':'ګرافایټ'}}
save(s)

s=page(208,'chem11-solids','Figure 6.19 · 6.5.3 Metallic Solids','شکل 6.19 · 6.5.3 دھاتی ٹھوس','شکل 6.19 · 6.5.3 فلزي جامدات','metallic-solids')
head(s,'h653','6.5.3 Metallic Solids','6.5.3 دھاتی ٹھوس','6.5.3 فلزي جامدات')
add(s,'m1','In metallic solids, the metal atoms are held together by a special type of bonding, called metallic bond, which is totally different from ionic or covalent bond.','دھاتی ٹھوس میں دھاتی ایٹم ایک خاص قسم کے بندھن سے ایک ساتھ بندھے ہوتے ہیں، جسے دھاتی بندھن کہتے ہیں، جو آئنی یا ہم ذرّی بندھن سے بالکل مختلف ہے۔','په فلزي جامداتو کې فلزي اتومونه د یو ځانګړي ډول بند په واسطه یو ځای نیول شوي وي، چې فلزي بند بلل کېږي، او دا له آیوني یا کوولنټ بند څخه بشپړ توپیر لري.')
add(s,'m2','In metals, the electrons in the outer most orbital of the atoms are generally very loosely bound. Thus, they have high mobility and can move freely from one place to another inside the metallic crystals lattice, much like the molecules in a gas. These are called conduction electrons, or free electrons. The free electrons are uniformly distributed throughout the metals lattice. The metals, by losing these conduction electrons, are transformed into positive ions. Thus a columbic interaction between the positive ion and the negative electrons arises which is termed as the metallic bond. Examples of metallic crystals are copper, aluminum, silver, iron, sodium etc.','دھاتوں میں ایٹموں کے سب سے بیرونی مدار کے الیکٹران عموماً بہت ڈھیلے بندھے ہوتے ہیں۔ اس لیے ان کی نقل پذیری زیادہ ہوتی ہے اور وہ دھاتی قلمی جالی کے اندر ایک جگہ سے دوسری جگہ آزادانہ حرکت کر سکتے ہیں، بالکل گیس کے سالموں کی طرح۔ انہیں ایصالی الیکٹران یا آزاد الیکٹران کہا جاتا ہے۔ آزاد الیکٹران دھاتی جالی میں یکساں طور پر تقسیم ہوتے ہیں۔ دھاتیں ان ایصالی الیکٹرانوں کو کھو کر مثبت آئن بن جاتی ہیں۔ یوں مثبت آئن اور منفی الیکٹرانوں کے درمیان کولمبی تعامل پیدا ہوتا ہے جسے دھاتی بندھن کہا جاتا ہے۔ دھاتی قلموں کی مثالیں تانبا، ایلومینیم، چاندی، لوہا، سوڈیم وغیرہ ہیں۔','په فلزاتو کې د اتومونو تر ټولو بهرني اوربیټل الکترونونه عموماً ډېر سست تړل شوي وي. نو دوی لوړه خوځښتیا لري او د فلزي کرسټالي جالۍ دننه له یوه ځایه بل ځای ته په آزادۍ حرکت کولای شي، لکه د ګاز مالیکولونه. دا د تېرښت الکترونونه یا آزاد الکترونونه بلل کېږي. آزاد الکترونونه د فلز په جالۍ کې یو شان ویشل شوي دي. فلزات د دې تېرښت الکترونونو په له لاسه ورکولو سره په مثبتو آیونونو بدلېږي. په دې توګه د مثبت آیون او منفي الکترونونو ترمنځ کولمبي تعامل رامنځته کېږي چې فلزي بند بلل کېږي. د فلزي کرسټالونو بېلګې مس، المونیم، سپین زر، اوسپنه، سوډیم او نور دي.')
head(s,'ph','Properties of Metallic Solids','دھاتی ٹھوس کی خصوصیات','د فلزي جامداتو ځانګړنې')
add(s,'p0','Some of the properties of metallic solids are,','دھاتی ٹھوس کی کچھ خصوصیات یہ ہیں،','د فلزي جامداتو ځینې ځانګړنې دا دي،')
pr=[('Metallic solids have usually compact structure and the atoms are closely packed together.','دھاتی ٹھوس کی ساخت عموماً کثیف ہوتی ہے اور ایٹم ایک دوسرے کے قریب بھرے ہوتے ہیں۔','فلزي جامدات معمولاً ګنډ جوړښت لري او اتومونه یو بل ته نژدې ډک وي.'),
('They are hard and have high melting point (A few of them are very soft and can be cut with a knife, e.g. sodium).','یہ سخت ہوتے ہیں اور ان کا نقطۂ پگھلاؤ بلند ہوتا ہے (ان میں سے چند بہت نرم ہوتے ہیں اور چاقو سے کاٹے جا سکتے ہیں، مثلاً سوڈیم)۔','دا کلک دي او لوړه د ویلې کېدو نقطه لري (ځینې یې ډېر نرم دي او په چاړې پرې کېدای شي، لکه سوډیم).'),
('These crystals have metallic luster.','ان قلموں میں دھاتی چمک ہوتی ہے۔','دا کرسټالونه فلزي ځلا لري.'),
('The free conduction electrons make the metallic solids good conductors of heat and electricity.','آزاد ایصالی الیکٹران دھاتی ٹھوس کو حرارت اور بجلی کا اچھا موصل بناتے ہیں۔','آزاد تېرښت الکترونونه فلزي جامدات د تودوخې او برېښنا ښه تېرونکي جوړوي.'),
('They are malleable (could be transformed into sheets) and ductile (could be drawn into wires).','یہ قابلِ طرق (چادروں میں ڈھالے جا سکتے ہیں) اور قابلِ سحب (تاروں میں کھینچے جا سکتے ہیں) ہوتے ہیں۔','دا د ټکولو وړ (په پاڼو بدلېدای شي) او د تار کښلو وړ (په تارونو کښل کېدای شي) دي.')]
for i,(e,u,p) in enumerate(pr,1): add(s,f'p{i}',f'{i}. {e}',f'{i}۔ {u}',f'{i}. {p}')
s['figures']=[fig(208,'fig6-19',svg(400,300,'Positive metal ions in a lattice surrounded by free electrons',metal()),'Figure 6.19 Internal Structure of Metallic Solids','شکل 6.19 دھاتی ٹھوس کی اندرونی ساخت','شکل 6.19 د فلزي جامداتو داخلي جوړښت',[lab('Positive metal ion','مثبت دھاتی آئن','مثبت فلزي آیون'),lab('Free electron','آزاد الیکٹران','آزاد الکترون')])]
s['figures'][0]['sourceGap']=dict(note='Printed figure shows ions with scattered electrons; redrawn as a regular schematic, electron positions are illustrative.')
s['flow']=[dict(type='paragraphs',ids=ids(s,0,2)),dict(type='figure',index=0),dict(type='paragraphs',ids=ids(s,2))]
s['sourceNote']='Printed folio 203. Left edge of the text is slightly clipped by the page curl but legible. A CamScanner watermark crosses the page.'
s['vocabulary']={'metallic bond':{'ur':'دھاتی بندھن','ps':'فلزي بند'},'free electrons':{'ur':'آزاد الیکٹران','ps':'آزاد الکترونونه'},'malleable':{'ur':'قابلِ طرق','ps':'د ټکولو وړ'},'ductile':{'ur':'قابلِ سحب','ps':'د تار کښلو وړ'}}
save(s)
