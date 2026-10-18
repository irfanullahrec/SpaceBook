from cshelp import *
c=cell
U='u5'
def H(s,k,en,ur,ps,**m): add(s,k,en,ur,ps,kind='heading',**m)
NOTE=' Photographs and clip-art are not reproduced; diagrams are redrawn as simplified coded SVG with the printed labels. Watermark, border lines, page-edge shadows and handwriting are excluded.'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
def rect(x,y,w,h,t='',sz=11,fill='#fff',anchor='middle',wt=700):
    b=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#111"/>'
    if t: b+=T(x+w/2,y+h/2+4,t,sz,anchor,wt)
    return b
def ln(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#111" stroke-width="1.2"/>'
def parts(net,host,title):
    b=T(250,16,title,11,'middle',700)
    b+=rect(40,24,int(420*net/4),34,'Network Part',11)+rect(40+int(420*net/4),24,int(420*host/4),34,'Host Part',11)
    b+=T(40,72,'bits 0',9,'start',400)+T(40+int(420*net/4),72,'7-8 / 15-16 / 23-24',8,'middle',400)+T(460,72,'31',9,'end',400)
    b+=T(40+int(420*net/8),90,f'{net} Octet'+('s' if net>1 else ''),12,'middle',700)+T(40+int(420*net/4)+int(420*host/8),90,f'{host} Octet'+('s' if host>1 else ''),12,'middle',700)
    return svg(500,100,f'Octet layout of a class address: {net} network octets and {host} host octets',b)
# ---------- scan 177 (printed 168) ----------
s=page(177,U,'168','Figure 5.30 Classes of IP Addresses; Class A; Class B — start','شکل ۵.۳۰ آئی پی ایڈریس کی کلاسز؛ کلاس اے؛ کلاس بی — آغاز','انځور ۵.۳۰ د IP پتو ټولګي؛ A ټولګی؛ B ټولګی — پیل','p168')
F=Flow(s)
def classes():
    b=''
    rows=[('Class A','0.0.0.0 - 127.255.255.255',1,'24 bits (Node Id)'),('Class B','128.0.0.0 - 191.255.255.255',2,'16 bits (Node ID)'),('Class C','192.0.0.0 - 223.255.255.255',3,'8 Bits (Node ID)')]
    for k,(n,rng,net,hostlab) in enumerate(rows):
        y=10+k*80
        b+=T(5,y+24,n,11,'start',700)
        w=360
        nw=int(w*net/4) if net<3 else int(w*0.75)
        b+=rect(70,y+8,nw,28,'',9)+rect(70+nw,y+8,w-nw,28,hostlab,10)
        b+=T(75,y+27,['0','10','110'][k],10,'start',700)
        b+=ln(70,y+46,70+nw,y+46)+T(70+nw/2,y+60,'Net ID',10,'middle',700)
        b+=T(440,y+27,rng,10,'start',700)
    return svg(640,260,'Bit layout of Class A, B and C IP addresses with their address ranges',b)
s['figures']=[dict(svg=classes(),id='cs11-s177-fig1',caption='Figure 5.30 Classes of IP Addresses',captionUrdu='شکل ۵.۳۰ آئی پی ایڈریس کی کلاسز',captionPashto='انځور ۵.۳۰ د IP پتو ټولګي',labels=[lab('Net ID','نیٹ ورک آئی ڈی','د شبکې پېژند'),lab('Node ID','نوڈ آئی ڈی','د غوټې پېژند')]),
 dict(svg=parts(1,3,'Class A: bits 0 to 31'),id='cs11-s177-fig2',caption='Class A address layout',captionUrdu='کلاس اے ایڈریس کی ترتیب',captionPashto='د A ټولګي پتې ترتیب',labels=[lab('Network Part','نیٹ ورک حصہ','د شبکې برخه'),lab('Host Part','ہوسٹ حصہ','د کوربه برخه')])]
F.fg(0)
H(s,'h1','Class A','کلاس اے','A ټولګی')
add(s,'a','Class A is used for the large networks and is implemented by large companies with many network devices. Binary address for the class A starts with 0. Its range is between 1 to 126 and the default subnet mask of this class is 255.0.0.0. Its Network part consists of 1 octet and Host part consists of 3 octets. An example of the class A is 100.10.11.1.','کلاس اے بڑے نیٹ ورکس کے لیے استعمال ہوتی ہے اور بہت سے نیٹ ورک آلات والی بڑی کمپنیاں اسے نافذ کرتی ہیں۔ کلاس اے کا بائنری ایڈریس ۰ سے شروع ہوتا ہے۔ اس کی حد ۱ سے ۱۲۶ کے درمیان ہے اور اس کلاس کا طے شدہ سب نیٹ ماسک ۲۵۵.۰.۰.۰ ہے۔ اس کا نیٹ ورک حصہ ۱ آکٹیٹ اور ہوسٹ حصہ ۳ آکٹیٹس پر مشتمل ہے۔ کلاس اے کی ایک مثال ۱۰۰.۱۰.۱۱.۱ ہے۔','A ټولګی د لویو شبکو لپاره کارول کېږي او د ډیرو شبکې وسایلو لرونکو لویو شرکتونو لخوا پلي کېږي. د A ټولګي دوتایي پته له ۰ نه پیلېږي. کچه یې له ۱ نه ۱۲۶ ترمنځ ده او د دې ټولګي ډیفالټ فرعي شبکې ماسک ۲۵۵.۰.۰.۰ دی. د شبکې برخه یې ۱ اکټېټ او د کوربه برخه ۳ اکټېټونه لري. د A ټولګي یوه بېلګه ۱۰۰.۱۰.۱۱.۱ ده.')
s['figures'][1]['svg']=parts(1,3,'bits 0 / 7-8 / 15-16 / 23-24 / 31')
F.fg(1)
H(s,'h2','Class B','کلاس بی','B ټولګی')
add(s,'b','Class B addresses scheme is used for the medium sized networks. The binary address for the class B starts with 10. The range of the IP address in the class B is between 128 to 191 and the default subnet mask of this class B is','کلاس بی ایڈریسنگ اسکیم درمیانے سائز کے نیٹ ورکس کے لیے استعمال ہوتی ہے۔ کلاس بی کا بائنری ایڈریس ۱۰ سے شروع ہوتا ہے۔ کلاس بی میں آئی پی ایڈریس کی حد ۱۲۸ سے ۱۹۱ کے درمیان ہے اور اس کلاس بی کا طے شدہ سب نیٹ ماسک','B ټولګي د پتو طرحه د منځنیو کچو شبکو لپاره کارول کېږي. د B ټولګي دوتایي پته له ۱۰ نه پیلېږي. په B ټولګي کې د IP پتې کچه له ۱۲۸ نه ۱۹۱ ترمنځ ده او د دې B ټولګي ډیفالټ فرعي شبکې ماسک',cont=True)
F.done()
fin(s,'Printed page 168: Figure 5.30 Classes of IP Addresses (bit-field charts of Class A, B and C with the printed address ranges 0.0.0.0 - 127.255.255.255, 128.0.0.0 - 191.255.255.255 and 192.0.0.0 - 223.255.255.255, “Net ID” and the Node ID fields of 24, 16 and 8 bits; the tiny bit numbering is not legible and is not reproduced; redrawn as simplified coded SVG), “Class A” with its paragraph and octet chart (redrawn as coded SVG) and the start of “Class B” (the sentence continues on the next page). The top of the page is slightly cut.')
# ---------- scan 178 (printed 169) ----------
s=page(178,U,'169','Class B (end); Class C; Class D; Class E','کلاس بی (اختتام)؛ کلاس سی؛ کلاس ڈی؛ کلاس ای','B ټولګی (پای)؛ C ټولګی؛ D ټولګی؛ E ټولګی','p169')
F=Flow(s)
add(s,'a','255.255.0.0. Its Network part consists of 2 octets and Host part also consists of 2 octets. An example of the class B address is 150.101.110.120.','۲۵۵.۲۵۵.۰.۰ ہے۔ اس کا نیٹ ورک حصہ ۲ آکٹیٹس اور ہوسٹ حصہ بھی ۲ آکٹیٹس پر مشتمل ہے۔ کلاس بی ایڈریس کی ایک مثال ۱۵۰.۱۰۱.۱۱۰.۱۲۰ ہے۔','۲۵۵.۲۵۵.۰.۰ دی. د شبکې برخه یې ۲ اکټېټونه او د کوربه برخه هم ۲ اکټېټونه لري. د B ټولګي پتې یوه بېلګه ۱۵۰.۱۰۱.۱۱۰.۱۲۰ ده.',cont=True)
s['figures']=[dict(svg=parts(2,2,'bits 0 / 7-8 / 15-16 / 23-24 / 31'),id='cs11-s178-fig1',caption='Class B address layout',captionUrdu='کلاس بی ایڈریس کی ترتیب',captionPashto='د B ټولګي پتې ترتیب',labels=[lab('Network Part','نیٹ ورک حصہ','د شبکې برخه'),lab('Host Part','ہوسٹ حصہ','د کوربه برخه')]),
 dict(svg=parts(3,1,'bits 0 / 7-8 / 15-16 / 23-24 / 31'),id='cs11-s178-fig2',caption='Class C address layout',captionUrdu='کلاس سی ایڈریس کی ترتیب',captionPashto='د C ټولګي پتې ترتیب',labels=[lab('Network Part','نیٹ ورک حصہ','د شبکې برخه'),lab('Host Part','ہوسٹ حصہ','د کوربه برخه')])]
F.fg(0)
H(s,'h1','Class C','کلاس سی','C ټولګی')
add(s,'b','Class C is used for the small networks. The binary address for the class C starts with 110. The range addresses in the class C is between 192 to 223 and the default subnet mask for this class is 255.255.255. Its Network part consists of 3 octets and Host part consists of 1 octet. An example of the Class C IP address is 210.190.100.150.','کلاس سی چھوٹے نیٹ ورکس کے لیے استعمال ہوتی ہے۔ کلاس سی کا بائنری ایڈریس ۱۱۰ سے شروع ہوتا ہے۔ کلاس سی میں ایڈریسز کی حد ۱۹۲ سے ۲۲۳ کے درمیان ہے اور اس کلاس کا طے شدہ سب نیٹ ماسک ۲۵۵.۲۵۵.۲۵۵ ہے۔ اس کا نیٹ ورک حصہ ۳ آکٹیٹس اور ہوسٹ حصہ ۱ آکٹیٹ پر مشتمل ہے۔ کلاس سی آئی پی ایڈریس کی ایک مثال ۲۱۰.۱۹۰.۱۰۰.۱۵۰ ہے۔','C ټولګی د کوچنیو شبکو لپاره کارول کېږي. د C ټولګي دوتایي پته له ۱۱۰ نه پیلېږي. په C ټولګي کې د پتو کچه له ۱۹۲ نه ۲۲۳ ترمنځ ده او د دې ټولګي ډیفالټ فرعي شبکې ماسک ۲۵۵.۲۵۵.۲۵۵ دی. د شبکې برخه یې ۳ اکټېټونه او د کوربه برخه ۱ اکټېټ لري. د C ټولګي IP پتې یوه بېلګه ۲۱۰.۱۹۰.۱۰۰.۱۵۰ ده.')
F.fg(1)
H(s,'h2','Class D','کلاس ڈی','D ټولګی')
add(s,'c','Class D is for special use for multicasting. The binary addresses for the class D starts with 1110 and the IP address ranges from 224 to 239. An example of the class D IP address is 230.150.110.11','کلاس ڈی ملٹی کاسٹنگ کے خصوصی استعمال کے لیے ہے۔ کلاس ڈی کے بائنری ایڈریسز ۱۱۱۰ سے شروع ہوتے ہیں اور آئی پی ایڈریس کی حد ۲۲۴ سے ۲۳۹ ہے۔ کلاس ڈی آئی پی ایڈریس کی ایک مثال ۲۳۰.۱۵۰.۱۱۰.۱۱ ہے۔','D ټولګی د څو غوښتنې (ملټي کاسټینګ) ځانګړي کارونې لپاره دی. د D ټولګي دوتایي پتې له ۱۱۱۰ نه پیلېږي او د IP پتې کچه له ۲۲۴ نه ۲۳۹ ده. د D ټولګي IP پتې یوه بېلګه ۲۳۰.۱۵۰.۱۱۰.۱۱ ده.')
H(s,'h3','Class E','کلاس ای','E ټولګی')
add(s,'d','Class E is under experimental research. The binary address can start with 111 and the decimal can be in range from 240 to 255. An example of the class E IP address is 245.101.110.110','کلاس ای تجرباتی تحقیق کے تحت ہے۔ بائنری ایڈریس ۱۱۱ سے شروع ہو سکتا ہے اور اعشاری ۲۴۰ سے ۲۵۵ کی حد میں ہو سکتا ہے۔ کلاس ای آئی پی ایڈریس کی ایک مثال ۲۴۵.۱۰۱.۱۱۰.۱۱۰ ہے۔','E ټولګی د تجربوي څېړنې لاندې دی. دوتایي پته له ۱۱۱ نه پیلېدای شي او لسیزه کچه له ۲۴۰ نه ۲۵۵ کېدای شي. د E ټولګي IP پتې یوه بېلګه ۲۴۵.۱۰۱.۱۱۰.۱۱۰ ده.')
F.done()
fin(s,'Printed page 169: the end of the Class B text (continuing from page 168), the octet chart for Class B (2 + 2 octets), “Class C” with its octet chart (3 + 1 octets), “Class D” and “Class E”. The printed default subnet mask of Class C is “255.255.255” (the final “.0” is missing) and the printed binary start for Class E is “111”; both are given as printed. A handwritten number beside the chart and a handwritten word “class” are excluded. The left edge is slightly cut.')
# ---------- scan 179 (printed 170) ----------
s=page(179,U,'170','b. Subnet Masks; Figure 5.31','ب۔ سب نیٹ ماسک؛ شکل ۵.۳۱','ب. فرعي شبکې ماسکونه؛ انځور ۵.۳۱','p170')
F=Flow(s)
H(s,'h1','b. Subnet Masks','ب۔ سب نیٹ ماسک','ب. فرعي شبکې ماسکونه')
add(s,'a','Subnet Mask indicates the network portion of an IP address. Like the IP address, the subnet mask is a dotted-decimal number. Usually all hosts within a LAN use the same subnet mask. Subnet mask is a 32-bit combination used to describe which portion of an address refers to the subnet and which part refers to the host. Figure 5.31 shows default subnet masks for usable IP addresses that are mapped to the first three classes of IP addresses.','سب نیٹ ماسک آئی پی ایڈریس کے نیٹ ورک حصے کی نشاندہی کرتا ہے۔ آئی پی ایڈریس کی طرح سب نیٹ ماسک بھی ڈاٹڈ ڈیسیمل نمبر ہے۔ عموماً لین کے اندر تمام ہوسٹس ایک ہی سب نیٹ ماسک استعمال کرتے ہیں۔ سب نیٹ ماسک ۳۲ بٹ کا مجموعہ ہے جو یہ بیان کرنے کے لیے استعمال ہوتا ہے کہ ایڈریس کا کون سا حصہ سب نیٹ سے اور کون سا ہوسٹ سے متعلق ہے۔ شکل ۵.۳۱ آئی پی ایڈریسز کی پہلی تین کلاسز سے ملنے والے قابلِ استعمال آئی پی ایڈریسز کے طے شدہ سب نیٹ ماسک دکھاتی ہے۔','فرعي شبکې ماسک د IP پتې د شبکې برخه ښيي. د IP پتې په څېر فرعي شبکې ماسک هم یوه نقطه لرونکې لسیزه شمېره ده. معمولاً په LAN کې ټول کوربه ورته فرعي شبکې ماسک کاروي. فرعي شبکې ماسک ۳۲ بټ ګډون دی چې د دې بیانولو لپاره کارول کېږي چې د پتې کومه برخه فرعي شبکې ته او کومه برخه کوربه ته اشاره کوي. ۵.۳۱ انځور د IP پتو لومړیو درېیو ټولګیو سره نښلول شوي د کارونې وړ IP پتو لپاره ډیفالټ فرعي شبکې ماسکونه ښيي.')
def sm():
    b=''
    defs=[('CLASS A (1-126)','Default subnet mask = 255.0.0.0',1),('CLASS B (128-191)','Default subnet mask = 255.255.0.0',2),('CLASS C (192-223)','Default subnet mask = 255.255.255.0',3)]
    vals=['255','0']
    for k,(t,m,n) in enumerate(defs):
        y=10+k*105
        b+=T(10,y+14,t,15,'start',700)+T(10,y+32,m,12,'start',700)
        b+=rect(300 if False else 10+n*0,y+40,0,0)
        for i in range(4):
            lab_='Network' if i<n else 'Host'
            b+=rect(10+i*100,y+44,90,24,lab_,11,'#fff')+T(55+i*100,y+90,'255' if i<n else '0',15,'middle',700)
        b+=rect(10+n*100,y+36,(4-n)*100-10,8,'Subnets/Hosts',7,'#6a6','middle')
    return svg(430,330,'Default subnet masks of Class A, B and C: network octets 255 and host octets 0',b)
s['figures']=[dict(svg=sm(),id='cs11-s179-fig1',caption='Figure 5.31 Subnet Masks',captionUrdu='شکل ۵.۳۱ سب نیٹ ماسک',captionPashto='انځور ۵.۳۱ فرعي شبکې ماسکونه',labels=[lab('Network','نیٹ ورک','شبکه'),lab('Host','ہوسٹ','کوربه'),lab('Subnets/Hosts','سب نیٹس/ہوسٹس','فرعي شبکې/کوربه'),lab('Default subnet mask','طے شدہ سب نیٹ ماسک','ډیفالټ فرعي شبکې ماسک')])]
F.fg(0)
F.done()
fin(s,'Printed page 170: “b. Subnet Masks” with its paragraph and Figure 5.31 Subnet Masks (default masks for CLASS A (1-126) 255.0.0.0, CLASS B (128-191) 255.255.0.0 and CLASS C (192-223) 255.255.255.0 with Network, Host and Subnets/Hosts boxes; redrawn as coded SVG). The top of the page is slightly cut.')
# ---------- scan 180 (printed 171) ----------
s=page(180,U,'171','Summary of Unit 5 (1)','یونٹ ۵ کا خلاصہ (۱)','د ۵ واحد لنډیز (۱)','p171')
F=Flow(s)
H(s,'h1','SUMMARY','خلاصہ','لنډیز')
L(s,[('b1','A network is a collection of independent computers or nodes that communicate with each other on a shared network medium.','نیٹ ورک آزاد کمپیوٹرز یا نوڈز کا مجموعہ ہے جو ایک مشترکہ نیٹ ورک وسیلے پر ایک دوسرے سے رابطہ کرتے ہیں۔','شبکه د خپلواکو کمپیوټرونو یا غوټو ټولګه ده چې په ګډې شبکې رسنۍ یو له بل سره اړیکه نیسي.'),('b2','Sender or Transmitter is a device that sends the message.','بھیجنے والا یا ٹرانسمیٹر وہ آلہ ہے جو پیغام بھیجتا ہے۔','لېږونکی یا ټرانسمیټر هغه وسیله ده چې پیغام لېږي.'),('b3','Message is the data or information that is to be communicated.','پیغام وہ ڈیٹا یا معلومات ہے جس کی ترسیل کی جانی ہو۔','پیغام هغه ډېټا یا معلومات دي چې اړیکه پرې کېږي.'),('b4','Medium is the physical path that message uses to travel from source to destination.','وسیلہ وہ طبعی راستہ ہے جسے پیغام ماخذ سے منزل تک سفر کے لیے استعمال کرتا ہے۔','رسنۍ هغه فزیکي لار ده چې پیغام د سرچینې نه منزل ته د سفر لپاره کاروي.'),('b5','Receiver is the device which receives transmitted message.','وصول کنندہ وہ آلہ ہے جو بھیجا گیا پیغام وصول کرتا ہے۔','ترلاسه کوونکی هغه وسیله ده چې لېږل شوی پیغام ترلاسه کوي.'),('b6','A protocol is a set of rules that governs data communications.','پروٹوکول قواعد کا وہ مجموعہ ہے جو ڈیٹا مواصلات کو چلاتا ہے۔','پروتوکول د قواعدو یوه ټولګه ده چې د ډېټا اړیکې چلوي.'),('b7','In Simplex mode, the communication takes place in only one direction.','سمپلیکس موڈ میں مواصلات صرف ایک سمت میں ہوتے ہیں۔','په یو لورې حالت کې اړیکې یوازې په یو لوري کېږي.'),('b8','In half-duplex mode, each station can transmit and receive data, but not at the same time.','ہاف ڈپلیکس موڈ میں ہر اسٹیشن ڈیٹا بھیج اور وصول کر سکتا ہے لیکن ایک ہی وقت میں نہیں۔','په نیم دوه لورې حالت کې هره ایستګاه ډېټا لېږلای او ترلاسه کولای شي، خو په یو وخت کې نه.'),('b9','In Full-duplex mode, both stations can send and receive the data simultaneously','فل ڈپلیکس موڈ میں دونوں اسٹیشن بیک وقت ڈیٹا بھیج اور وصول کر سکتے ہیں۔','په بشپړ دوه لورې حالت کې دواړه ایستګاوې ډېټا په یو وخت لېږلای او ترلاسه کولای شي.'),('b10','In synchronous transmission, large volumes of information can be transmitted block-by-block or word-by-word simultaneously.','ہم وقت ترسیل میں معلومات کی بڑی مقدار بلاک بہ بلاک یا لفظ بہ لفظ بیک وقت منتقل کی جا سکتی ہے۔','په همغږي لېږد کې د معلوماتو لوی حجمونه بلاک په بلاک یا کلمه په کلمه په یو وخت لېږدول کېدای شي.'),('b11','In asynchronous transmission, data is transmitted one byte at a ‘time’.','غیر ہم وقت ترسیل میں ڈیٹا ایک وقت میں ایک بائٹ منتقل ہوتا ہے۔','په ناهمغږي لېږد کې ډېټا په یو وخت یو بایټ لېږدول کېږي.'),('b12','Guided media are the physical links in which signals are confined along a narrow path.','رہنمائی یافتہ وسائط وہ طبعی ربط ہیں جن میں اشارے ایک تنگ راستے تک محدود رہتے ہیں۔','لارښوونه شوې رسنۍ هغه فزیکي تړاوونه دي چې سیګنالونه په کې په یوه تنګه لار پورې محدود وي.'),('b13','Unguided media also called Wireless media transports signals without using any physical conductor between the two devices communicating.','غیر رہنمائی یافتہ وسائط، جنہیں وائرلیس وسائط بھی کہتے ہیں، رابطہ کرنے والے دو آلات کے درمیان کسی طبعی موصل کے بغیر اشارے منتقل کرتے ہیں۔','بې لارښوونې رسنۍ، چې بې سیمه رسنۍ هم ورته ویل کېږي، د اړیکه نیوونکو دوو وسایلو ترمنځ پرته له کوم فزیکي تېرونکي سیګنالونه لېږدوي.')],'sum')
F.done()
fin(s,'Printed page 171: the heading “SUMMARY” of Unit 5 and thirteen bulleted points (the summary continues on the next page). Handwritten words (“message uses to”, “takes only”, “med”) between the lines are excluded. The running header is cut at the top.')
