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
def pcs(x,y):
    return box(x,y,22,16,'#4a86c8')+box(x+6,y+17,10,3,'#777')
def cloud(cx,cy,rx,ry,fill='#fbf3a0'):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="#111" stroke-width="1.5"/>'
# ---------- scan 153 (printed 144) ----------
s=page(153,U,'144','MAN (end); Figure 5.20; c. WAN','مین (اختتام)؛ شکل ۵.۲۰؛ ج۔ وین','MAN (پای)؛ انځور ۵.۲۰؛ ج. WAN','p144')
F=Flow(s)
add(s,'a','Metropolitan Area Network connects multiple geographically nearby LANs to one another (over an area of up to a few dozen kilometers). Recent use of MAN technology has been the rapid development of cellular phone systems.','میٹروپولیٹن ایریا نیٹ ورک جغرافیائی لحاظ سے قریبی متعدد لین کو ایک دوسرے سے جوڑتا ہے (چند درجن کلومیٹر تک کے علاقے میں)۔ مین ٹیکنالوجی کا حالیہ استعمال سیلولر فون سسٹمز کی تیز ترقی ہے۔','ښاري سیمه شبکه څو جغرافیايي نژدې LANs یو له بل سره نښلوي (تر څو لسګونو کیلومترو سیمې پورې). د MAN ټکنالوجۍ وروستی کارونه د ګرځنده تلیفون سیسټمونو چټکه پراختیا ده.')
def man():
    b=cloud(220,125,170,34)+T(220,128,'Metropolitan Area Network',11,'middle',700)
    b+='<circle cx="60" cy="40" r="28" fill="#fff" stroke="#111"/>'
    for a in (10,50,95,140,185,230):
        pass
    for x,y in [(30,10),(60,2),(90,10),(20,40),(95,40),(35,70),(65,75),(90,65)]: b+=pcs(x-10,y-4)
    b+=ln(85,60,180,115)
    b+=ln(150,20,150,45)+ln(150,45,230,45)+ln(190,45,190,115)
    for x in (140,170,200,230): b+=pcs(x,50)
    b+=pcs(138,5)+pcs(138,25)
    b+=box(360,40,18,18,'#6bc')+ln(378,50,420,50)+ln(369,40,369,15)+pcs(340,40)+pcs(395,40)+pcs(375,15)+pcs(375,70)+ln(369,58,369,70)
    b+=ln(300,105,360,60)
    b+=ln(220,160,220,175)+ln(130,175,300,175)+ln(130,175,130,215)
    for x in (140,170,200,230): b+=pcs(x,195)
    b+=pcs(125,155)+pcs(125,180)+pcs(205,160)+pcs(260,160)
    return svg(440,230,'Metropolitan area network: several LANs of different layouts joined through a city network',b)
s['figures']=[dict(svg=man(),id='cs11-s153-fig1',caption='Figure 5.20 Metropolitan Area Network',captionUrdu='شکل ۵.۲۰ میٹروپولیٹن ایریا نیٹ ورک',captionPashto='انځور ۵.۲۰ ښاري سیمه شبکه',labels=[lab('Metropolitan Area Network','میٹروپولیٹن ایریا نیٹ ورک','ښاري سیمه شبکه')])]
F.fg(0)
H(s,'h1','c. WAN (Wide Area Networks)','ج۔ وین (وائڈ ایریا نیٹ ورکس)','ج. WAN (پراخه سیمه شبکې)')
add(s,'b','WAN (Wide Area Network) covers large distance for communication between computers. Its nodes may span cities, states, or even countries. It interconnects many LANs and MANs. WAN uses fiber optics, microwaves and satellites technology for communication. For example, nationwide ATM (Automated Teller Machines) used in banking represent a common application of a wide area network.','وین (وائڈ ایریا نیٹ ورک) کمپیوٹرز کے درمیان مواصلات کے لیے وسیع فاصلہ طے کرتا ہے۔ اس کے نوڈز شہروں، ریاستوں یا حتیٰ کہ ممالک میں پھیلے ہو سکتے ہیں۔ یہ بہت سے لین اور مین کو آپس میں جوڑتا ہے۔ وین مواصلات کے لیے فائبر آپٹکس، مائیکرو ویوز اور سیٹلائٹ ٹیکنالوجی استعمال کرتا ہے۔ مثلاً بینکاری میں استعمال ہونے والی ملک گیر اے ٹی ایم (آٹومیٹڈ ٹیلر مشینیں) وائڈ ایریا نیٹ ورک کے عام استعمال کی نمائندگی کرتی ہیں۔','WAN (پراخه سیمه شبکه) د کمپیوټرونو ترمنځ د اړیکو لپاره لوی واټن پوښي. د هغې غوټې کېدای شي ښارونه، ایالتونه یا حتی هیوادونه پوښي. دا ډیر LANs او MANs سره نښلوي. WAN د اړیکو لپاره فایبر اپټیکس، مایکرو څپې او د سپوږمکۍ ټکنالوجي کاروي. د بېلګې په توګه په بانکدارۍ کې کارېدونکې هیواد پراخه ATM (خپلکاره پیسې ورکوونکې ماشینونه) د پراخې سیمې شبکې عامه کارونه ښيي.')
add(s,'c','The most well-known WAN is the Internet, which may cover the entire globe. Most WANs (like the Internet) are not owned by any one organization but rather exist under collective or distributed ownership and management.','سب سے مشہور وین انٹرنیٹ ہے جو پورے کرۂ ارض کا احاطہ کر سکتا ہے۔ زیادہ تر وین (جیسے انٹرنیٹ) کسی ایک ادارے کی ملکیت نہیں ہوتے بلکہ اجتماعی یا تقسیم شدہ ملکیت اور انتظام کے تحت موجود ہوتے ہیں۔','تر ټولو مشهوره WAN انټرنېټ دی چې ټوله نړۍ پوښلای شي. ډیری WANs (لکه انټرنېټ) د یوې ادارې ملکیت نه دي بلکې د ګډې یا وېشل شوې ملکیت او اداره کولو لاندې شتون لري.')
F.done()
fin(s,'Printed page 144: the sentence on MAN (continuing from page 143), Figure 5.20 Metropolitan Area Network (several LANs of ring, bus and star layouts drawn around a cloud with the printed text “Metropolitan Area Network”; redrawn as a simplified coded SVG) and “c. WAN (Wide Area Networks)” with two paragraphs. The word “Internet” in the last paragraph is printed in bold. The printed key words are given as printed.')
# ---------- scan 154 (printed 145) ----------
s=page(154,U,'145','Figure 5.21; d. VPN','شکل ۵.۲۱؛ د۔ وی پی این','انځور ۵.۲۱؛ د. VPN','p145')
F=Flow(s)
def wan():
    b=T(190,22,'Wide Area Network',13,'middle',700)+T(190,38,'of ANZ Company',13,'middle',700)+T(60,20,'Country A',13,'middle',700)+T(320,22,'Country B',13,'middle',700)+T(30,125,'Country C',13,'middle',700)+T(340,125,'Country D',13,'middle',700)
    b+='<circle cx="190" cy="115" r="75" fill="none" stroke="#555" stroke-dasharray="3 3"/>'+T(190,78,'Communication',8,'middle',700)+T(190,88,'Sub-System',8,'middle',700)
    nodes=[(150,95),(225,90),(190,125),(115,130),(260,125),(190,160)]
    for x,y in nodes: b+=f'<ellipse cx="{x}" cy="{y}" rx="14" ry="7" fill="#5b9bd5" stroke="#111"/>'
    b+=ln(150,95,190,125)+ln(225,90,190,125)+ln(115,130,190,125)+ln(260,125,190,125)+ln(190,160,190,125)+ln(150,95,225,90)
    for (cx,cy,l) in [(60,60,'LAN'),(320,60,'LAN'),(60,155,'LAN'),(320,160,'LAN')]:
        b+=cloud(cx,cy,48,30,'#f6f6f6')+T(cx-25,cy-18,l,7,'start',700)+box(cx-20,cy-10,18,26,'#888')+pcs(cx+5,cy-8)+pcs(cx+5,cy+14)
    b+=ln(95,75,160,95)+ln(290,70,225,90)+ln(95,150,115,130)+ln(290,155,260,125)
    return svg(380,200,'Wide area network of a company linking LANs in four countries through a communication sub-system',b)
s['figures']=[dict(svg=wan(),id='cs11-s154-fig1',caption='Figure 5.21 Wide Area Network',captionUrdu='شکل ۵.۲۱ وائڈ ایریا نیٹ ورک',captionPashto='انځور ۵.۲۱ پراخه سیمه شبکه',labels=[lab('Country A','ملک الف','هېواد الف'),lab('Country B','ملک ب','هېواد ب'),lab('Country C','ملک ج','هېواد ج'),lab('Country D','ملک د','هېواد د'),lab('Wide Area Network of ANZ Company','اے این زیڈ کمپنی کا وائڈ ایریا نیٹ ورک','د ANZ شرکت پراخه سیمه شبکه'),lab('Communication Sub-System','مواصلاتی ذیلی نظام','د اړیکو فرعي سیسټم')])]
F.fg(0)
H(s,'h1','d. VPN (Virtual Private Network)','د۔ وی پی این (ورچوئل پرائیویٹ نیٹ ورک)','د. VPN (مجازي خصوصي شبکه)')
add(s,'a','A virtual private network (VPN) is a network that uses a public telecommunication infrastructure, such as the Internet or a private network owned by a service provider to provide remote offices or individual users with secure access to their organization’s network. A virtual private network can be contrasted with an expensive system of owned or leased lines that can only be used by one organization. The goal of a VPN is to provide the organization with the same capabilities, but at a much lower cost.','ورچوئل پرائیویٹ نیٹ ورک (وی پی این) ایسا نیٹ ورک ہے جو عوامی ٹیلی کمیونیکیشن بنیادی ڈھانچہ، جیسے انٹرنیٹ یا سروس فراہم کنندہ کی ملکیت کا نجی نیٹ ورک، استعمال کرتا ہے تاکہ دور دراز دفاتر یا انفرادی صارفین کو ان کے ادارے کے نیٹ ورک تک محفوظ رسائی دی جا سکے۔ ورچوئل پرائیویٹ نیٹ ورک کا موازنہ ملکیتی یا کرائے کی لائنوں کے مہنگے نظام سے کیا جا سکتا ہے جو صرف ایک ادارہ استعمال کر سکتا ہے۔ وی پی این کا مقصد ادارے کو وہی صلاحیتیں بہت کم لاگت پر فراہم کرنا ہے۔','مجازي خصوصي شبکه (VPN) یوه شبکه ده چې عامه مخابراتي زېربنا، لکه انټرنېټ یا د خدمت برابروونکي ملکیت خصوصي شبکه، کاروي ترڅو لیرې دفترونو یا انفرادي کاروونکو ته د دوی د ادارې شبکې ته خوندي لاسرسی ورکړي. مجازي خصوصي شبکه د ملکیتي یا کرایه شویو کرښو له قیمتي سیسټم سره پرتله کېدای شي چې یوازې یوه اداره یې کارولای شي. د VPN موخه ادارې ته هماغه وړتیاوې خو په ډیر ټیټ لګښت برابرول دي.')
add(s,'b','A VPN works by using the shared public infrastructure while maintaining privacy through security procedures.','وی پی این مشترکہ عوامی بنیادی ڈھانچہ استعمال کرتے ہوئے سیکیورٹی طریقوں کے ذریعے رازداری برقرار رکھ کر کام کرتا ہے۔','VPN د ګډې عامې زېربنا په کارولو سره د امنیتي کړنلارو له لارې محرمیت ساتلو سره کار کوي.')
add(s,'c','Large corporations, educational institutions, and government agencies use VPN technology to enable remote users to securely connect to a private network. In order to gain access to the private network, a user must be authenticated using a unique identification and a password.','بڑی کارپوریشنز، تعلیمی ادارے اور سرکاری ایجنسیاں دور دراز صارفین کو نجی نیٹ ورک سے محفوظ طریقے سے جڑنے کے قابل بنانے کے لیے وی پی این ٹیکنالوجی استعمال کرتی ہیں۔ نجی نیٹ ورک تک رسائی حاصل کرنے کے لیے صارف کی منفرد شناخت اور پاس ورڈ کے ذریعے تصدیق ہونا ضروری ہے۔','لویې کارپوریشنونه، زده کړې ادارې او دولتي ادارې د VPN ټکنالوجي کاروي ترڅو لیرې کاروونکي وکولای شي چې خصوصي شبکې سره په خوندي ډول وصل شي. د خصوصي شبکې ته د لاسرسي لپاره باید کاروونکی د ځانګړې پېژندنې او پټنوم په کارولو سره تصدیق شي.')
F.done()
fin(s,'Printed page 145: Figure 5.21 Wide Area Network (a diagram of four LANs in Country A, B, C and D joined through a “Communication Sub-System”; redrawn as simplified coded SVG with the printed labels) and “d. VPN (Virtual Private Network)” with three paragraphs. A handwritten mark at the top is excluded.')
# ---------- scan 155 (printed 146) ----------
s=page(155,U,'146','Figure 5.22; 5.1.7 Network Topologies; a. Star Topology — start','شکل ۵.۲۲؛ ۵.۱.۷ نیٹ ورک ٹوپولوجیز؛ الف۔ اسٹار ٹوپولوجی — آغاز','انځور ۵.۲۲؛ ۵.۱.۷ د شبکې توپولوژۍ؛ الف. ستوری توپولوژي — پیل','p146')
F=Flow(s)
def vpn():
    b=cloud(95,70,80,50)+T(95,60,'Corporate',11,'middle',700)+T(95,73,'Intranet',11,'middle',700)
    b=cloud(70,95,55,45)+cloud(230,80,70,50,'#fff')+T(230,85,'Internet',14,'middle',700)+cloud(350,55,50,35)+cloud(340,150,50,35)
    b+=T(70,40,'Corporate',11,'middle',700)+T(70,53,'Intranet',11,'middle',700)
    b+=T(340,15,'Business',11,'start',700)+T(340,28,'Partner/',11,'start',700)+T(340,41,'Supplier',11,'start',700)+T(340,54,'Intranet',11,'start',700)
    b+=T(375,160,'Branch',11,'start',700)+T(375,173,'Office',11,'start',700)+T(375,186,'Intranet',11,'start',700)
    b+=box(210,10,24,18,'#222')+T(240,12,'Remote',11,'start',700)+T(240,25,'Access',11,'start',700)
    b+=ln(100,85,215,28,'#c9a6e0',8)+T(150,60,'VPN',11,'middle',700)
    b+=ln(95,95,320,60,'#c9a6e0',8)+T(200,92,'VPN',11,'middle',700)
    b+=ln(95,105,320,150,'#c9a6e0',8)+T(190,135,'VPN',11,'middle',700)
    for x,y in [(55,70),(75,70),(55,95),(75,105),(330,45),(345,60),(330,140),(350,155)]: b+=pcs(x-8,y-6)
    return svg(430,195,'Virtual private network: corporate intranet linked through the Internet by VPN tunnels to remote access, a business partner and a branch office',b)
s['figures']=[dict(svg=vpn(),id='cs11-s155-fig1',caption='Figure 5.22 Virtual Private Network',captionUrdu='شکل ۵.۲۲ ورچوئل پرائیویٹ نیٹ ورک',captionPashto='انځور ۵.۲۲ مجازي خصوصي شبکه',labels=[lab('Corporate Intranet','کارپوریٹ انٹرانیٹ','شرکتي انټرانېټ'),lab('Remote Access','دور دراز رسائی','لیرې لاسرسی'),lab('Business Partner/Supplier Intranet','کاروباری شراکت دار/سپلائر انٹرانیٹ','د سوداګریز شریک/عرضه کوونکي انټرانېټ'),lab('Branch Office Intranet','برانچ آفس انٹرانیٹ','د څانګې دفتر انټرانېټ'),lab('Internet','انٹرنیٹ','انټرنېټ'),lab('VPN','وی پی این','VPN')])]
F.fg(0)
H(s,'h1','5.1.7 Network Topologies','۵.۱.۷ نیٹ ورک ٹوپولوجیز','۵.۱.۷ د شبکې توپولوژۍ')
add(s,'a','Network Topology refers to the physical layout and connectivity of computers in a network. Network topologies are categorized into the following four basic types.','نیٹ ورک ٹوپولوجی سے مراد نیٹ ورک میں کمپیوٹرز کی طبعی ترتیب اور کنیکٹیویٹی ہے۔ نیٹ ورک ٹوپولوجیز کو درج ذیل چار بنیادی اقسام میں تقسیم کیا جاتا ہے۔','د شبکې توپولوژي په شبکه کې د کمپیوټرونو فزیکي ترتیب او نښلولو ته اشاره کوي. د شبکې توپولوژۍ په لاندې څلورو بنسټیزو ډولونو طبقه بندي کېږي.')
L(s,[('t1','Star','اسٹار','ستوری'),('t2','Ring','رنگ','حلقه'),('t3','Bus','بس','بس'),('t4','Mesh','میش','جال')],'tp')
H(s,'h2','a. Star Topology','الف۔ اسٹار ٹوپولوجی','الف. ستوری توپولوژي')
add(s,'b','In a star topology all the nodes (server, workstations, peripherals) on the network are connected directly to a centralized connectivity device called a hub, switch, or router. Each computer is connected with its own cable to a port on the hub. Data on a star network passes through the hub, switch, or router','اسٹار ٹوپولوجی میں نیٹ ورک کے تمام نوڈز (سرور، ورک اسٹیشنز، پیریفرلز) براہِ راست ایک مرکزی کنیکٹیویٹی آلے سے جڑے ہوتے ہیں جسے ہب، سوئچ یا راؤٹر کہتے ہیں۔ ہر کمپیوٹر اپنی کیبل کے ذریعے ہب کے ایک پورٹ سے جڑا ہوتا ہے۔ اسٹار نیٹ ورک پر ڈیٹا اپنی منزل کی طرف بڑھنے سے پہلے ہب، سوئچ یا راؤٹر سے گزرتا ہے','په ستوری توپولوژۍ کې په شبکه ټولې غوټې (خدمتګار، کاري ایستګاوې، پیریفرلونه) مستقیم یوې مرکزي نښلولو وسیلې ته چې هب، سویچ یا روټر بلل کېږي وصل دي. هر کمپیوټر د خپل کېبل په ذریعه د هب پورټ سره وصل دی. په ستوری شبکه کې ډېټا له هب، سویچ یا روټر نه تېرېږي',cont=True)
F.done()
fin(s,'Printed page 146: Figure 5.22 Virtual Private Network (a diagram of a corporate intranet, the Internet, remote access, a business partner/supplier intranet and a branch office intranet joined by VPN tunnels; redrawn as simplified coded SVG with the printed labels), the banner “5.1.7 Network Topologies” with the list a–d and the start of “a. Star Topology” (the sentence continues on the next page). The heading of the topology list and “a. Star Topology” are printed in a purple colour.')
# ---------- scan 156 (printed 147) ----------
s=page(156,U,'147','Star topology (end); Figure 5.23; advantages and disadvantages of a star topology','اسٹار ٹوپولوجی (اختتام)؛ شکل ۵.۲۳؛ اسٹار ٹوپولوجی کے فوائد اور نقصانات','ستوری توپولوژي (پای)؛ انځور ۵.۲۳؛ د ستورې توپولوژۍ ګټې او زیانونه','p147')
F=Flow(s)
add(s,'a','before continuing to its destination. The hub, switch, or router manages and controls all functions of the network. It also acts as a repeater for the data flow. This configuration is common with twisted pair cable; however, it can also be used with coaxial cable or fiber optic cable.','۔ ہب، سوئچ یا راؤٹر نیٹ ورک کے تمام افعال کا انتظام اور کنٹرول کرتا ہے۔ یہ ڈیٹا کے بہاؤ کے لیے ریپیٹر کا کام بھی کرتا ہے۔ یہ ترتیب ٹوئسٹڈ پیئر کیبل کے ساتھ عام ہے؛ تاہم اسے کواکسیئل کیبل یا فائبر آپٹک کیبل کے ساتھ بھی استعمال کیا جا سکتا ہے۔','. هب، سویچ یا روټر د شبکې ټولې دندې اداره او کنټرولوي. دا د ډېټا د جریان لپاره د ریپیټر په توګه هم کار کوي. دا ترتیب د تاو شوې جوړې کېبل سره عام دی؛ خو دا د کوکسیل کېبل یا فایبر اپټیک کېبل سره هم کارېدای شي.',cont=True)
def star():
    b=T(300,20,'Star Topology',20,'middle',700)
    b+=box(130,80,50,12,'#ccc')+T(130,70,'Switch/hub',12,'start',700)
    pos=[(30,30),(200,20),(30,120),(190,130)]
    for x,y in pos: b+=ln(155,86,x+25,y+20,'#d9541e')+box(x,y,50,34,'#7a7ad6')+box(x-5,y+36,60,8,'#999')
    b+=ln(180,86,380,86,'#d9541e')+box(380,60,40,55,'#8a6f4a')
    return svg(440,185,'Star topology: four computers and a server connected to a central switch or hub',b)
s['figures']=[dict(svg=star(),id='cs11-s156-fig1',caption='Figure 5.23 Star Topology',captionUrdu='شکل ۵.۲۳ اسٹار ٹوپولوجی',captionPashto='انځور ۵.۲۳ ستوری توپولوژي',labels=[lab('Switch/hub','سوئچ/ہب','سویچ/هب'),lab('Star Topology','اسٹار ٹوپولوجی','ستوری توپولوژي')])]
F.fg(0)
H(s,'h1','Advantages of a Star Topology','اسٹار ٹوپولوجی کے فوائد','د ستورې توپولوژۍ ګټې')
L(s,[('a1','Centralized management. It helps in monitoring the network.','مرکزی انتظام۔ یہ نیٹ ورک کی نگرانی میں مدد دیتا ہے۔','مرکزي مدیریت. دا د شبکې په څارنه کې مرسته کوي.'),('a2','Easy to install and configure.','نصب اور ترتیب دینا آسان ہے۔','نصبول او تنظیمول یې اسانه دي.'),('a3','No disruptions to the network when connecting or removing devices.','آلات کو جوڑتے یا ہٹاتے وقت نیٹ ورک میں کوئی خلل نہیں پڑتا۔','د وسایلو د نښلولو یا لېرې کولو پر مهال په شبکه کې هېڅ خنډ نه راځي.'),('a4','Easy to detect faults and to remove parts.','خرابیوں کا پتہ لگانا اور پرزے ہٹانا آسان ہے۔','د نیمګړتیاو موندل او برخې لېرې کول اسانه دي.'),('a5','Failure of one node or link doesn’t affect the rest of network.','ایک نوڈ یا ربط کی ناکامی باقی نیٹ ورک کو متاثر نہیں کرتی۔','د یوې غوټې یا تړاو ناکامي پاتې شبکه نه اغېزمنوي.')],'st_adv')
H(s,'h2','Disadvantages of a Star Topology','اسٹار ٹوپولوجی کے نقصانات','د ستورې توپولوژۍ زیانونه')
L(s,[('d1','Requires more cable than a Bus topology.','بس ٹوپولوجی سے زیادہ کیبل درکار ہے۔','د بس توپولوژۍ په پرتله ډیر کېبل غواړي.'),('d2','If the hub, switch, or concentrator fails, nodes attached become disable.','اگر ہب، سوئچ یا کنسنٹریٹر ناکام ہو جائے تو منسلک نوڈز بے کار ہو جاتے ہیں۔','که هب، سویچ یا کنسنټریټر ناکام شي نو وصل شوې غوټې بې کاره کېږي.'),('d3','More expensive than linear bus topologies because of the cost of the hubs.','ہبز کی لاگت کی وجہ سے لکیری بس ٹوپولوجیز سے زیادہ مہنگا ہے۔','د هبونو د لګښت له امله له خطي بس توپولوژیو نه ډیر قیمتي دی.')],'st_dis')
F.done()
fin(s,'Printed page 147: the end of the star topology paragraph (continuing from page 146; the first word of the continuation is the end of the sentence “… before continuing to its destination.”), Figure 5.23 Star Topology (a switch/hub with three computers and a server; redrawn as coded SVG) and the advantages (five bullets) and disadvantages (three bullets) of a star topology. The printed phrase “become disable” is given as printed.')
