from urgl import *
# scan 199 = printed 192
s=page(199,'farhang','192','Glossary (Farhang): “Qitaat”, “Ikhlas”, “Ghazaliyat-e-Mir Taqi Mir”, “Khwaja Mir Dard”','فرہنگ: «قطعات»، «اِخلاص»، «غزلیاتِ میر تقی میر»، «خواجہ میر درد»','فرهنګ: «قطعات»، «اخلاص»، «د میر تقي میر غزلونه»، «خواجه میر درد»','gl15')
F=Flow(s)
H(s,'قطعات','Qitaat (Quatrains)','قطعات')
F.tb(0)
H(s,'اِخلاص','Ikhlas','اخلاص')
F.tb(1)
H(s,'غزلیاتِ میر تقی میرؔ','Ghazaliyat-e-Mir Taqi Mir','د میر تقي میر غزلونه')
F.tb(2)
H(s,'خواجہ میر دردؔ','Khwaja Mir Dard','خواجه میر درد')
F.tb(3)
F.done()
a=[('پناہ گزیں','پناہ لینے والے، مہاجرین','refugees, those who take shelter','پناه اخیستونکي، مهاجرین'),('پردہ نشین','خواتین','women who observe purdah','پردې والې میرمنې'),('بھنگی','سوپر، جھاڑو دینے والا','sweeper, one who sweeps','جارو کوونکی'),('جاروب کش','جھاڑو دینے والا','sweeper','جارو کوونکی'),('شانِ بیداری','مستعد ہونے کی علامت','a sign of alertness','د ځیرکتیا نښه'),('غلاظت','گندگی','filth','ګندګي'),('محتسب','احتساب کرنے والا','inspector, one who holds to account','محتسب'),('کمیٹی','میونسپل کمیٹی','municipal committee','ښاروالۍ کمېټه')]
b=[('ہم دوش','کندھے سے کندھا ملا ہوا برابر','shoulder to shoulder, equal','اوږه په اوږه، برابر'),('اِخلاص','خلوص، مہر، مروّت، ہمدردی','sincerity, affection, kindness, sympathy','خلوص، مینه، مروت، همدردي'),('دوام','دائمی، ہمیشہ','permanent, forever','تل، همېشه'),('ثریا','ایک بلند ستارہ','the Pleiades, a high star','یو لوړ ستوری'),('یک جنبشِ گام','ایک قدم کی حرکت','the movement of a single step','د یو قدم حرکت'),('صیاد','شکاری','hunter','ښکاري')]
c3=[('صدا','آواز','sound, voice','غږ'),('دل اُٹھانا','منھ موڑنا، دل چسپی نہ لینا','to turn away, to lose interest','مخ اړول، ګټه نه اخیستل'),('بے خود','غافل','beside oneself, unaware','بې خوده، غافل'),('جبیں','پیشانی','forehead','تندی'),('پرستش','عبادت، پوجا','worship','عبادت، پوجا'),('پیری','بڑھاپا','old age','زوړوالی'),('غم کشاں','غمگین، مغموم، غم اُٹھانے والا','sorrowful, grieving, one who bears grief','غمجن، غم زغمونکی'),('آبِ گرم','گرم پانی، یہاں آنسو مراد ہے','hot water; here, tears','ګرمې اوبه، دلته مراد اوښکې'),('جسمِ خاک','مٹی سے بنا بدن','a body made of clay','له خټې جوړ بدن'),('آلودہ','لتھڑا ہوا، گندا','soiled, dirty','ککړ، ګنده'),('ڈھونا','اُٹھا کر لے جانا','to carry','پورته کول او وړل'),('آبِ حیات','ہمیشہ کی زندگی دینے والا پانی','water giving everlasting life','د همېشه ژوند ورکوونکې اوبه')]
d=[('صریحاً','واضح، صاف','clearly, plainly','واضح، څرګند'),('مقدور','طاقت، قدرت','power, ability','ځواک، قدرت'),('ناسور','پرانا اور لا علاج زخم','a chronic, incurable wound','زړ او بې علاجه زخم'),('مذکور','ذکر ہونا','mentioned','یاد شوی'),('تئیں','تک','till, up to','تر'),('مُحتسِب','احتساب کرنے والا، قاضی','an inspector, a judge','محتسب، قاضي')]
s['tables']=[gtable('“Qitaat”','«قطعات»','«قطعات»',a,'4 + 4 rows.'),gtable('“Ikhlas”','«اِخلاص»','«اخلاص»',b,'3 + 3 rows.'),gtable('“Ghazaliyat-e-Mir Taqi Mir”','«غزلیاتِ میر تقی میرؔ»','«د میر تقي میر غزلونه»',c3,'6 + 6 rows.'),gtable('“Khwaja Mir Dard”','«خواجہ میر دردؔ»','«خواجه میر درد»',d,'3 + 3 rows.')]
s['sourceNote']='Printed page 192 (scan 199): glossary sections “قطعات” (4 + 4), “اِخلاص” (3 + 3), “غزلیاتِ میر تقی میرؔ” (6 + 6) and “خواجہ میر دردؔ” (3 + 3).'+NOTE
s['vocabulary']={}
save(s)
# scan 200 = printed 193
s=page(200,'farhang','193','Glossary (Farhang): Mushafi, Mirza Ghalib, Mirza Dagh Dehlvi','فرہنگ: شیخ غلام ہمدانی مصحفی، مرزا غالب، مرزا داغ دہلوی','فرهنګ: شیخ غلام همداني مصحفي، مرزا غالب، مرزا داغ دهلوي','gl16')
F=Flow(s)
H(s,'شیخ غلام ہمدانی مصحفیؔ','Sheikh Ghulam Hamdani Mushafi','شیخ غلام همداني مصحفي')
F.tb(0)
H(s,'مرزا غالبؔ','Mirza Ghalib','مرزا غالب')
F.tb(1)
H(s,'مرزا داغؔ دہلوی','Mirza Dagh Dehlvi','مرزا داغ دهلوي')
F.tb(2)
F.done()
a=[('ناگہ','اچانک','suddenly','ناڅاپه'),('گل اندام','پھول جسم والا، محبوب','flower-bodied, the beloved','د ګل په څېر بدن لرونکی، محبوب'),('شکست رنگ','رنگ اُڑ جانا','colour fading, turning pale','رنګ الوتل'),('پُر خمار','نشیلی','intoxicated, languorous','نشه ایزه'),('کف','ہتھیلی، جھاگ','palm; foam','لاس تلی، ځګ'),('لبِ بام','کوٹھے یا چھت کا کنارا','the edge of a roof or terrace','د چت غاړه'),('اسیر','قیدی','prisoner','بندي'),('قطع','ترکِ ملاقات، کاٹنا، چھوڑنا','breaking off contact; cutting, abandoning','پرې کول، پرېښودل')]
b=[('دائم','ہمیشہ، مستقل','always, permanent','تل، همېشه'),('لعل و زمرد','قیمتی اور خوش نما پتھر','ruby and emerald, precious and beautiful stones','قیمتي او ښکلې ډبرې'),('قدم بوسی','قدم چومنا، انتہائی احترام کا اظہار کرنا','to kiss the feet, to show utmost respect','د پښو ښکلول، ډېر درناوی ښودل'),('خستگی','زخمی ہونا، شکستہ حالی','being wounded, a broken state','ټپي کېدل، ماتې حالت'),('حرفِ مکرر','غلطی سے دوبارہ لکھا ہوا لفظ','a word accidentally written twice','په غلطۍ دوه ځله لیکل شوی ټکی'),('بھرم کھلنا','راز کھلنا، اعتبار اُٹھنا','for a secret to be exposed, credibility lost','راز ښکاره کېدل، اعتبار ختمېدل'),('طرۂ پُر پیچ و خم','خم دار بڑی پگڑی جو امارت کی نشانی سمجھی جاتی ہے','a large curled turban-crest considered a sign of nobility','تاوده لویه پګړۍ چې د امارت نښه ګڼل کېږي'),('تیغِ ستم','ظلموں کی تلوار','the sword of oppression','د ظلم تور')]
c3=[('کوئی دم','کچھ دیر کے لیے','for a short while','لږ وخت لپاره'),('کم نگاہی','کم نظری، کم فہمی','narrow vision, lack of understanding','لنډ نظري، کم فهمي')]
s['tables']=[gtable('Mushafi','مصحفیؔ','مصحفي',a,'4 + 4 rows.'),gtable('Mirza Ghalib','غالبؔ','غالب',b,'4 + 4 rows.'),gtable('Mirza Dagh Dehlvi','داغؔ دہلوی','داغ دهلوي',c3,'1 + 1 row.')]
s['sourceNote']='Printed page 193 (scan 200): glossary sections for Sheikh Ghulam Hamdani Mushafi (4 + 4), Mirza Ghalib (4 + 4) and Mirza Dagh Dehlvi (1 + 1). Glossary entries and the pairing follow the earlier glossary page of this poem (scan 185).'+NOTE
s['vocabulary']={}
save(s)
