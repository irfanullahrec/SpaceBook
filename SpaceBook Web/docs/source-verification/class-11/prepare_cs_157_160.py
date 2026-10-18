from cshelp import *
c=cell
U='u5'
def H(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,kind='heading',**m)
NOTE=' Photographs and clip-art are not reproduced; diagrams are redrawn as simplified coded SVG with the printed labels. Watermark, border lines, page-edge shadows and handwriting are excluded.'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
def box(x,y,w,h,fill='#555'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#111"/>'
def ln(x1,y1,x2,y2,col='#111',w=1.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"/>'
def mon(x,y):
    return box(x,y,50,34,'#7a7ad6')+box(x-6,y+36,62,8,'#999')
# ---------- scan 157 (printed 148) ----------
s=page(157,U,'148','b. Ring Topology; Figure 5.24; advantages and disadvantages — start','ب۔ رنگ ٹوپولوجی؛ شکل ۵.۲۴؛ فوائد اور نقصانات — آغاز','ب. حلقه توپولوژي؛ انځور ۵.۲۴؛ ګټې او زیانونه — پیل','p148')
F=Flow(s)
H(s,'h1','b. Ring Topology','ب۔ رنگ ٹوپولوجی','ب. حلقه توپولوژي')
add(s,'a','In a ring topology, every node is logically connected to two other preceding and succeeding nodes, forming a ring. Traffic flows through the entire ring until it reaches its destination.','رنگ ٹوپولوجی میں ہر نوڈ منطقی طور پر دو دوسرے پچھلے اور اگلے نوڈز سے جڑا ہوتا ہے اور اس طرح ایک حلقہ بن جاتا ہے۔ ٹریفک پورے حلقے میں اس وقت تک بہتی ہے جب تک وہ اپنی منزل تک نہ پہنچ جائے۔','په حلقه توپولوژۍ کې هره غوټه منطقي توګه له دوو نورو مخکینیو او وروستیو غوټو سره وصل وي او حلقه جوړوي. ترافیک په ټوله حلقه کې بهېږي تر څو منزل ته ورسېږي.')
add(s,'b','Data packets travel in a single direction around the ring from one network device to the next. Each network device acts as a repeater, meaning it regenerates the signal the packets they receive and then send them on to the next computer in the ring.','ڈیٹا پیکٹس حلقے کے گرد ایک ہی سمت میں ایک نیٹ ورک آلے سے اگلے تک سفر کرتے ہیں۔ ہر نیٹ ورک آلہ ریپیٹر کا کام کرتا ہے، یعنی وہ جو پیکٹس وصول کرتا ہے ان کے اشارے کو دوبارہ پیدا کرتا ہے اور پھر انہیں حلقے میں اگلے کمپیوٹر کو بھیج دیتا ہے۔','د ډېټا کڅوړې د حلقې شاوخوا په یوه لوري کې له یوې شبکې وسیلې نه بلې ته سفر کوي. هره شبکې وسیله د ریپیټر په توګه کار کوي، یعنې هغه سیګنال بیا جوړوي چې کڅوړې یې ترلاسه کوي او بیا هغه د حلقې بل کمپیوټر ته لېږي.')
def ring():
    b=T(300,20,'Ring Topology',20,'middle',700)
    b+=ln(95,45,95,45)+ln(80,60,160,60,'#d9541e')+ln(85,95,45,140,'#d9541e')+ln(170,70,210,110,'#d9541e')+ln(65,155,250,155,'#d9541e')
    b=T(300,20,'Ring Topology',20,'start',700)
    b+=mon(20,25)+mon(150,25)+mon(5,100)+mon(250,100)
    return svg(430,170,'Ring topology: computers connected one after another in a ring',b)
def ring2():
    b=T(250,25,'Ring Topology',18,'start',700)
    A=(40,20);B=(160,20);C=(70,100);D=(280,80)
    b+=ln(90,45,160,45,'#d9541e')+ln(80,100,45,60,'#d9541e')+ln(200,60,285,95,'#d9541e')+ln(120,125,285,125,'#d9541e')
    b+=mon(*A)+mon(*B)+mon(*C)+mon(*D)
    return svg(400,170,'Ring topology: three computers joined in a ring',b)
s['figures']=[dict(svg=ring2(),id='cs11-s157-fig1',caption='Figure 5.24 Ring Topology',captionUrdu='شکل ۵.۲۴ رنگ ٹوپولوجی',captionPashto='انځور ۵.۲۴ حلقه توپولوژي',labels=[lab('Ring Topology','رنگ ٹوپولوجی','حلقه توپولوژي')])]
F.fg(0)
H(s,'h2','Advantages of Ring Topology','رنگ ٹوپولوجی کے فوائد','د حلقه توپولوژۍ ګټې')
L(s,[('a1','Even when the load on the network increases, its performance is better than that of Bus topology.','نیٹ ورک پر بوجھ بڑھنے پر بھی اس کی کارکردگی بس ٹوپولوجی سے بہتر رہتی ہے۔','حتی کله چې په شبکه بار زیات شي، فعالیت یې د بس توپولوژۍ نه ښه وي.'),('a2','There is no need for network server to control the connectivity between workstations.','ورک اسٹیشنز کے درمیان کنیکٹیویٹی کو کنٹرول کرنے کے لیے نیٹ ورک سرور کی ضرورت نہیں۔','د کاري ایستګاوو ترمنځ د نښلولو د کنټرول لپاره د شبکې خدمتګار ته اړتیا نشته.'),('a3','Additional components do not affect the performance of network.','اضافی اجزاء نیٹ ورک کی کارکردگی کو متاثر نہیں کرتے۔','اضافي اجزا د شبکې فعالیت نه اغېزمنوي.'),('a4','Each computer has equal access to resources.','ہر کمپیوٹر کو وسائل تک یکساں رسائی حاصل ہے۔','هر کمپیوټر سرچینو ته مساوي لاسرسی لري.')],'rg_adv')
H(s,'h3','Disadvantages of Ring Topology','رنگ ٹوپولوجی کے نقصانات','د حلقه توپولوژۍ زیانونه')
L(s,[('d1','Each packet of data must pass through all the computers between source and destination. This makes it slower than Star topology.','ڈیٹا کے ہر پیکٹ کو ماخذ اور منزل کے درمیان تمام کمپیوٹرز سے گزرنا پڑتا ہے۔ اس سے یہ اسٹار ٹوپولوجی سے سست ہو جاتی ہے۔','د ډېټا هره کڅوړه باید د سرچینې او منزل ترمنځ له ټولو کمپیوټرونو تېره شي. دا یې د ستورې توپولوژۍ نه ورو کوي.'),('d2','If one workstation or port goes down, the entire network gets affected.','اگر ایک ورک اسٹیشن یا پورٹ خراب ہو جائے تو پورا نیٹ ورک متاثر ہوتا ہے۔','که یوه کاري ایستګاه یا پورټ ودرېږي نو ټوله شبکه اغېزمنېږي.')],'rg_dis')
F.done()
fin(s,'Printed page 148: “b. Ring Topology” with two paragraphs, Figure 5.24 Ring Topology (three computers joined by lines, titled “Ring Topology”; redrawn as coded SVG), the advantages of a ring topology (four bullets) and the first two disadvantages (the list continues on the next page).')
# ---------- scan 158 (printed 149) ----------
s=page(158,U,'149','Ring disadvantages (end); c. Bus Topology; Figure 5.25; advantages — start','رنگ کے نقصانات (اختتام)؛ ج۔ بس ٹوپولوجی؛ شکل ۵.۲۵؛ فوائد — آغاز','د حلقې زیانونه (پای)؛ ج. بس توپولوژي؛ انځور ۵.۲۵؛ ګټې — پیل','p149')
F=Flow(s)
L(s,[('d3','Network is highly dependent on the wire which connects different components.','نیٹ ورک کا انحصار اس تار پر بہت زیادہ ہے جو مختلف اجزاء کو جوڑتی ہے۔','شبکه ډیره د هغه تار پورې تړلې ده چې مختلف اجزا نښلوي.'),('d4','Ring topologies can be difficult to troubleshoot.','رنگ ٹوپولوجیز میں خرابی تلاش کرنا مشکل ہو سکتا ہے۔','د حلقه توپولوژیو د ستونزو حل کول ستونزمن کېدای شي.'),('d5','Adding or removing computers from this type of topology can disrupt the operation of the network.','اس قسم کی ٹوپولوجی میں کمپیوٹرز شامل کرنے یا ہٹانے سے نیٹ ورک کا عمل متاثر ہو سکتا ہے۔','په دې ډول توپولوژۍ کې د کمپیوټرونو زیاتول یا لېرې کول د شبکې عملیات خرابولای شي.')],'rg_dis2')
H(s,'h1','c. Bus Topology','ج۔ بس ٹوپولوجی','ج. بس توپولوژي')
add(s,'a','In the bus topology, each node (computer, server or peripheral device) is attached to a single common cable. This topology type is considered a passive topology because the computers on a bus just sit and listen. When they “hear” data on the wire that belongs to them, they accept that data. When they are ready to transmit, they make sure no one else on the bus is transmitting and then they send their packets of information on the network.','بس ٹوپولوجی میں ہر نوڈ (کمپیوٹر، سرور یا پیریفرل آلہ) ایک ہی مشترکہ کیبل سے جڑا ہوتا ہے۔ اس قسم کی ٹوپولوجی کو غیر فعال ٹوپولوجی سمجھا جاتا ہے کیونکہ بس پر موجود کمپیوٹرز صرف بیٹھ کر سنتے رہتے ہیں۔ جب وہ تار پر اپنا ڈیٹا ’’سنتے‘‘ ہیں تو اسے قبول کر لیتے ہیں۔ جب وہ ترسیل کے لیے تیار ہوتے ہیں تو یقینی بناتے ہیں کہ بس پر کوئی اور ترسیل نہیں کر رہا اور پھر معلومات کے پیکٹس نیٹ ورک پر بھیجتے ہیں۔','په بس توپولوژۍ کې هره غوټه (کمپیوټر، خدمتګار یا پیریفرل وسیله) یوه ګډ کېبل سره نښلول شوې ده. دا ډول توپولوژي غیر فعاله توپولوژي ګڼل کېږي ځکه چې په بس کمپیوټرونه یوازې ناست وي او اورېدل کوي. کله چې دوی په تار هغه ډېټا “واوري” چې دوی پورې اړه لري، هغه مني. کله چې دوی د لېږد لپاره چمتو وي، ډاډ ترلاسه کوي چې په بس بل څوک نه لېږي او بیا د معلوماتو کڅوړې په شبکه لېږي.')
add(s,'b','Bus network typically uses coaxial networking cable hooked in to each computer using a T-connector. Each end of the network is terminated using a terminator specific to a cable.','بس نیٹ ورک عموماً کواکسیئل نیٹ ورکنگ کیبل استعمال کرتا ہے جسے ٹی کنیکٹر کے ذریعے ہر کمپیوٹر سے جوڑا جاتا ہے۔ نیٹ ورک کے ہر سرے کو کیبل کے مخصوص ٹرمینیٹر سے ختم کیا جاتا ہے۔','د بس شبکه معمولاً کوکسیل شبکه کېبل کاروي چې د T-نښلوونکي په کارولو سره هر کمپیوټر ته نښلول کېږي. د شبکې هر سر د کېبل ځانګړي ټرمینېټر په کارولو سره پای ته رسول کېږي.')
def bus():
    b=T(260,25,'Bus Topology',20,'start',700)
    b+=mon(10,10)+mon(170,15)+mon(65,100)+mon(280,95)
    b+=ln(30,85,30,85)+ln(35,60,35,78,'#d9541e')+ln(35,78,300,78,'#d9541e')+ln(195,60,195,78,'#d9541e')+ln(90,78,90,100,'#d9541e')+ln(300,78,300,95,'#d9541e')
    return svg(430,160,'Bus topology: four computers attached to a single common cable',b)
s['figures']=[dict(svg=bus(),id='cs11-s158-fig1',caption='Figure 5.25 Bus Topology',captionUrdu='شکل ۵.۲۵ بس ٹوپولوجی',captionPashto='انځور ۵.۲۵ بس توپولوژي',labels=[lab('Bus Topology','بس ٹوپولوجی','بس توپولوژي')])]
F.fg(0)
H(s,'h2','Advantages of a Bus Topology','بس ٹوپولوجی کے فوائد','د بس توپولوژۍ ګټې')
L(s,[('a1','Bus topology costs very less.','بس ٹوپولوجی کی لاگت بہت کم ہے۔','د بس توپولوژۍ لګښت ډیر لږ دی.'),('a2','Easy to connect a computer or peripheral to a linear bus.','خطی بس سے کمپیوٹر یا پیریفرل جوڑنا آسان ہے۔','یو کمپیوټر یا پیریفرل خطي بس ته نښلول اسانه دي.')],'bs_adv')
F.done()
fin(s,'Printed page 149: the last three disadvantages of a ring topology (continuing from page 148), “c. Bus Topology” with two paragraphs, Figure 5.25 Bus Topology (four computers on one common cable; redrawn as coded SVG) and the first two advantages of a bus topology (the list continues on the next page). The caption of Figure 5.25 is printed “Figure”.')
# ---------- scan 159 (printed 150) ----------
s=page(159,U,'150','Bus advantages (end); disadvantages; d. Mesh Topology — start','بس کے فوائد (اختتام)؛ نقصانات؛ د۔ میش ٹوپولوجی — آغاز','د بس ګټې (پای)؛ زیانونه؛ د. جال توپولوژي — پیل','p150')
F=Flow(s)
L(s,[('a3','Requires less cable length than a other topologies.','دوسری ٹوپولوجیز کے مقابلے میں کم کیبل کی لمبائی درکار ہوتی ہے۔','د نورو توپولوژیو په پرتله لږ کېبل اوږدوالی غواړي.'),('a4','It is easy to set-up and extend bus network.','بس نیٹ ورک کو ترتیب دینا اور بڑھانا آسان ہے۔','د بس شبکه جوړول او غځول اسانه دي.'),('a5','Linear Bus network is mostly used in small networks.','لکیری بس نیٹ ورک زیادہ تر چھوٹے نیٹ ورکس میں استعمال ہوتا ہے۔','خطي بس شبکه ډیره په کوچنیو شبکو کې کارول کېږي.')],'bs_adv2')
H(s,'h1','Disadvantages of a Bus Topology','بس ٹوپولوجی کے نقصانات','د بس توپولوژۍ زیانونه')
L(s,[('d1','Entire network shuts down if there is a break in the main cable. Loose and detached connections may also affect the entire network.','اگر مرکزی کیبل میں خرابی ہو تو پورا نیٹ ورک بند ہو جاتا ہے۔ ڈھیلے اور الگ ہونے والے کنکشن بھی پورے نیٹ ورک کو متاثر کر سکتے ہیں۔','که په اصلي کېبل کې ماتېدل وي نو ټوله شبکه بنده کېږي. سست او جلا شوي پیوستونه هم ټوله شبکه اغېزمنولای شي.'),('d2','There is a limit on central cable length and number of nodes that can be connected.','مرکزی کیبل کی لمبائی اور جڑنے والے نوڈز کی تعداد پر حد ہے۔','د مرکزي کېبل اوږدوالي او د هغو غوټو شمېر چې وصلېدای شي محدودیت شته.'),('d3','Proper termination is required to dump signals. Use of terminators is must.','سگنلز کو ختم کرنے کے لیے مناسب ٹرمینیشن ضروری ہے۔ ٹرمینیٹرز کا استعمال لازمی ہے۔','د سیګنالونو د لېرې کولو لپاره مناسب پای ته رسول اړین دي. د ټرمینېټرونو کارول حتمي دي.'),('d4','It is difficult to detect and troubleshoot fault at individual station.','انفرادی اسٹیشن پر خرابی کا پتہ لگانا اور اسے دور کرنا مشکل ہے۔','په انفرادي ایستګاه کې د نیمګړتیا موندل او حل کول ستونزمن دي.'),('d5','It is not suitable for networks with heavy traffic.','یہ بھاری ٹریفک والے نیٹ ورکس کے لیے موزوں نہیں۔','دا د درنې ترافیک لرونکو شبکو لپاره مناسب نه دی.')],'bs_dis')
H(s,'h2','d. Mesh Topology','د۔ میش ٹوپولوجی','د. جال توپولوژي')
add(s,'a','In a mesh network topology, each of the network node, computer and other devices, are interconnected with one another.','میش نیٹ ورک ٹوپولوجی میں نیٹ ورک کا ہر نوڈ، کمپیوٹر اور دیگر آلات ایک دوسرے سے آپس میں جڑے ہوتے ہیں۔','په جال شبکه توپولوژۍ کې د شبکې هره غوټه، کمپیوټر او نور وسایل یو له بل سره نښلول شوي وي.')
add(s,'b','In a full mesh, every device in the network is connected to every other device. In reality, a partial mesh is commonly used in backbone environments to provide fault-tolerant connections between critical servers and network devices. Unlike each of the previous topologies, messages sent on a mesh network can take any of several possible paths from source to destination. This type of topology is very expensive as there are many redundant connections, thus it is not mostly used in computer networks. It is commonly used in wireless networks. Flooding or routing technique is used in mesh topology.','مکمل میش میں نیٹ ورک کا ہر آلہ ہر دوسرے آلے سے جڑا ہوتا ہے۔ حقیقت میں جزوی میش عموماً بیک بون ماحول میں اہم سرورز اور نیٹ ورک آلات کے درمیان خرابی برداشت کرنے والے کنکشن فراہم کرنے کے لیے استعمال ہوتا ہے۔ پچھلی ہر ٹوپولوجی کے برعکس میش نیٹ ورک پر بھیجے گئے پیغامات ماخذ سے منزل تک کئی ممکنہ راستوں میں سے کوئی بھی راستہ اختیار کر سکتے ہیں۔ اس قسم کی ٹوپولوجی بہت مہنگی ہے کیونکہ اس میں بہت سے غیر ضروری کنکشن ہوتے ہیں، اس لیے یہ کمپیوٹر نیٹ ورکس میں زیادہ استعمال نہیں ہوتی۔ یہ عموماً وائرلیس نیٹ ورکس میں استعمال ہوتی ہے۔ میش ٹوپولوجی میں فلڈنگ یا روٹنگ تکنیک استعمال ہوتی ہے۔','په بشپړ جال کې د شبکې هره وسیله له هرې بلې وسیلې سره وصل وي. په حقیقت کې یو جزوي جال معمولاً په شا هډوکي چاپېریال کې د مهمو خدمتګارانو او شبکې وسایلو ترمنځ د نیمګړتیا زغملو وړ پیوستونو برابرولو لپاره کارول کېږي. د پخوانیو توپولوژیو برعکس په جال شبکه لېږل شوي پیغامونه کولای شي له سرچینې نه منزل ته د څو ممکنو لارو هره لار ونیسي. دا ډول توپولوژي ډیره قیمتي ده ځکه چې ډیر زیات پیوستونه لري، نو په کمپیوټر شبکو کې ډیره نه کارول کېږي. دا معمولاً په بې سیمو شبکو کې کارول کېږي. په جال توپولوژۍ کې د سېل یا لارښوونې تخنیک کارول کېږي.')
F.done()
fin(s,'Printed page 150: the end of the bus advantages (continuing from page 149), the disadvantages of a bus topology (five bullets) and “d. Mesh Topology” with two paragraphs. Figure 5.26 Mesh Topology follows on the next page. The last line of the mesh paragraph reads “Flooding or routing technique is used in mesh topology” as printed. The scan is photographed at an angle and the right edge of the text is slightly clipped.')
# ---------- scan 160 (printed 151) ----------
s=page(160,U,'151','Figure 5.26 Mesh Topology; advantages and disadvantages of a mesh topology','شکل ۵.۲۶ میش ٹوپولوجی؛ میش ٹوپولوجی کے فوائد اور نقصانات','انځور ۵.۲۶ جال توپولوژي؛ د جال توپولوژۍ ګټې او زیانونه','p151')
F=Flow(s)
def mesh():
    import math
    pts=[(210,60),(330,100),(330,190),(210,230),(90,190),(90,100)]
    b=''
    for i,(x,y) in enumerate(pts):
        for (x2,y2) in pts[i+1:]: b+=ln(x,y+10,x2,y2+10)
    for x,y in pts: b+=box(x-14,y-8,28,22,'#7ac6e8')
    b+=T(210,20,'Computer',12,'middle',700)+T(75,70,'Computer',12,'middle',700)+T(350,85,'Computer',12,'middle',700)+T(75,235,'Computer',12,'middle',700)+T(350,235,'Computer',12,'middle',700)+T(210,275,'Computer',12,'middle',700)
    return svg(440,290,'Mesh topology: six computers each connected to every other computer',b)
s['figures']=[dict(svg=mesh(),id='cs11-s160-fig1',caption='Figure 5.26 Mesh Topology',captionUrdu='شکل ۵.۲۶ میش ٹوپولوجی',captionPashto='انځور ۵.۲۶ جال توپولوژي',labels=[lab('Computer','کمپیوٹر','کمپیوټر')])]
F.fg(0)
H(s,'h1','Advantages of Mesh topology','میش ٹوپولوجی کے فوائد','د جال توپولوژۍ ګټې')
L(s,[('a1','Data can be transmitted from different devices simultaneously. This topology can withstand high traffic.','ڈیٹا مختلف آلات سے بیک وقت منتقل کیا جا سکتا ہے۔ یہ ٹوپولوجی بھاری ٹریفک برداشت کر سکتی ہے۔','ډېټا له مختلفو وسایلو په یو وخت لېږدول کېدای شي. دا توپولوژي لوړ ترافیک زغملای شي.'),('a2','Even if one of the components fails there is always an alternative link present. So data transfer doesn’t get affected.','اگر کوئی ایک جزو ناکام بھی ہو جائے تو ہمیشہ ایک متبادل ربط موجود ہوتا ہے۔ اس لیے ڈیٹا کی منتقلی متاثر نہیں ہوتی۔','که یو جز هم ناکام شي، تل یو بدیل تړاو شته. نو د ډېټا لېږد نه اغېزمنېږي.'),('a3','Expansion and modification in topology can be done without disrupting other nodes.','ٹوپولوجی میں توسیع اور ترمیم دوسرے نوڈز میں خلل ڈالے بغیر کی جا سکتی ہے۔','په توپولوژۍ کې پراختیا او تعدیل د نورو غوټو د خرابولو پرته کېدای شي.')],'ms_adv')
H(s,'h2','Disadvantages of Mesh topology','میش ٹوپولوجی کے نقصانات','د جال توپولوژۍ زیانونه')
L(s,[('d1','There are high chances of redundancy in many of the network connections.','نیٹ ورک کے کئی کنکشنز میں فالتو پن کے امکانات زیادہ ہیں۔','د شبکې په ډیرو پیوستونو کې د زیاتوالي لوړ احتمال شته.'),('d2','Overall cost of this network is too high as compared to other network topologies.','دوسری نیٹ ورک ٹوپولوجیز کے مقابلے میں اس نیٹ ورک کی مجموعی لاگت بہت زیادہ ہے۔','د نورو شبکې توپولوژیو په پرتله د دې شبکې ټوله لګښت ډیر لوړ دی.'),('d3','Set-up and maintenance of this topology is very difficult. Even administration of the network is challenging.','اس ٹوپولوجی کی ترتیب اور دیکھ بھال بہت مشکل ہے۔ حتیٰ کہ نیٹ ورک کا انتظام بھی چیلنجنگ ہے۔','د دې توپولوژۍ جوړول او ساتنه ډیره ستونزمنه ده. حتی د شبکې مدیریت هم ننګونکی دی.')],'ms_dis')
F.done()
fin(s,'Printed page 151: Figure 5.26 Mesh Topology (six computers each joined to every other computer, each marked with the printed label “Computer”; redrawn as coded SVG), the advantages (three bullets) and the disadvantages (three bullets) of a mesh topology. A handwritten word at the top right is excluded.')
