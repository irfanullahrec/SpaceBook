import re
exec(open('D:/SpaceBook/SpaceBook Web/tmp/c8ps_fill1.py',encoding='utf8').read().split("add('013'")[0])
T={
('027','q 4 | لاندې ورکړي'):[
 ('تاریخ','موږ د اسلام تاریخ ډېر په شوق لولو۔','We read the history of Islam with great interest.','ہم اسلام کی تاریخ بڑے شوق سے پڑھتے ہیں۔'),
 ('مذهب','زمونږ مذهب اسلام دے۔','Our religion is Islam.','ہمارا مذہب اسلام ہے۔'),
 ('ریاست','مدینه منوره لومړنۍ اسلامي ریاست وه۔','Madina was the first Islamic state.','مدینہ منورہ پہلی اسلامی ریاست تھی۔'),
 ('فلسفه','د ژوند فلسفه د نېکۍ کولو درس راکوي۔','The philosophy of life teaches us to do good.','زندگی کا فلسفہ نیکی کا درس دیتا ہے۔'),
 ('منشور','حجة الوداع خطبه د انساني حقونو منشور دے۔','The Farewell Sermon is a charter of human rights.','خطبۂ حجۃ الوداع انسانی حقوق کا منشور ہے۔')],
('033','q 4 | لاندې ورکړې شوي'):[
 ('خلافت','حضرت عثمان رضي الله عنه دریم خلیفه وو چې په خلافت کښې ئې خدمتونه وکړل۔','Hazrat Usman (RA) was the third caliph and served during his caliphate.','حضرت عثمان رضی اللہ عنہ تیسرے خلیفہ تھے۔'),
 ('هجرت','صحابه کرامو حبشې ته هجرت وکړ۔','The companions migrated to Abyssinia.','صحابہ کرام نے حبشہ کی طرف ہجرت کی۔'),
 ('خدمت','مور پلار ته خدمت کول ډېر ثواب لري۔','Serving parents carries great reward.','والدین کی خدمت میں بڑا ثواب ہے۔'),
 ('بیعت','خلیفه ته د مسلمانانو بیعت وکړ۔','The Muslims gave allegiance to the caliph.','مسلمانوں نے خلیفہ کی بیعت کی۔'),
 ('شهادت','د حضرت عثمان رضي الله عنه شهادت یو غمجن واقعه وه۔','The martyrdom of Hazrat Usman (RA) was a sad event.','حضرت عثمان رضی اللہ عنہ کی شہادت ایک غمناک واقعہ تھا۔')],
('042','q 4 | لاندې ورکړې'):[
 ('معاهده','ګندمک معاهده په ۱۸۷۹ کال کښې وشوه۔','The Treaty of Gandamak was made in 1879.','معاہدۂ گندمک ۱۸۷۹ میں ہوا۔'),
 ('حکمراني','امیر ښۀ حکمراني وکړه۔','The ruler governed well.','امیر نے اچھی حکمرانی کی۔'),
 ('حمله','دښمن په ښار حمله وکړه۔','The enemy attacked the city.','دشمن نے شہر پر حملہ کیا۔'),
 ('فوځونه','دواړه فوځونه د جنګ لپاره تیار شول۔','Both armies got ready for battle.','دونوں فوجیں جنگ کے لیے تیار ہو گئیں۔'),
 ('تېښته','دښمن د جنګ نه تېښته وکړه۔','The enemy fled from the battle.','دشمن جنگ سے بھاگ گیا۔')],
('050','q 5 | دا لفظونه'):[
 ('کتاب','کتاب زمونږ ښۀ ملګرے دے۔','A book is our good friend.','کتاب ہمارا اچھا دوست ہے۔'),
 ('رڼا','د علم رڼا ټولو ته ګټوره ده۔','The light of knowledge benefits everyone.','علم کی روشنی سب کے لیے مفید ہے۔'),
 ('شپه','په شپه کښې ستوري ځلېږي۔','Stars shine at night.','رات کو ستارے چمکتے ہیں۔'),
 ('دیوال','دیوال ته انځور ځړول شو۔','A picture was hung on the wall.','دیوار پر تصویر لگائی گئی۔'),
 ('شخصیت','ښۀ اخلاق د شخصیت ښکلا ده۔','Good manners are the beauty of personality.','اچھے اخلاق شخصیت کا حسن ہیں۔')],
('065','q 2 | لاندیني ټکي'):[
 ('ناشته','ما سهار ناشته وکړ۔','I had breakfast in the morning.','میں نے صبح ناشتہ کیا۔'),
 ('تعبیر','د خوب تعبیر ورته ښۀ وو۔','The interpretation of the dream was good for him.','خواب کی تعبیر اس کے لیے اچھی تھی۔'),
 ('وعده','وعده پوره کول ضروري دي۔','Keeping a promise is necessary.','وعدہ پورا کرنا ضروری ہے۔'),
 ('خوب','ما په خوب کښې ښۀ باغ ولید۔','I saw a nice garden in a dream.','میں نے خواب میں خوبصورت باغ دیکھا۔'),
 ('نصیحت','مشرانو ته نصیحت اوریدل پکار دي۔','One should listen to the advice of elders.','بزرگوں کی نصیحت سننی چاہیے۔')],
('071','q 4 | دا لفظونه'):[
 ('قبضه','دښمن په ښار قبضه وکړه۔','The enemy captured the city.','دشمن نے شہر پر قبضہ کیا۔'),
 ('غزا','مجاهدینو په غزا کښې برخه واخیسته۔','The mujahideen took part in the holy war.','مجاہدین نے غزا میں حصہ لیا۔'),
 ('وطن','وطن ته مینه د ایمان برخه ده۔','Love for the homeland is part of faith.','وطن سے محبت ایمان کا حصہ ہے۔'),
 ('لښکر','لښکر د سرحد په لور روان شو۔','The army moved towards the border.','لشکر سرحد کی طرف روانہ ہوا۔'),
 ('مقابله','مونږ د دښمن مقابله وکړه۔','We faced the enemy.','ہم نے دشمن کا مقابلہ کیا۔')],
('077','q 5 | لاندیني لفظونه'):[
 ('کردار','ښۀ کردار د انسان زیور دے۔','Good character is the ornament of a person.','اچھا کردار انسان کا زیور ہے۔'),
 ('مزاج','زما د استاذ مزاج ډېر نرم دے۔','My teacher\'s temperament is very gentle.','میرے استاد کا مزاج بہت نرم ہے۔'),
 ('عادت','سهار وختي پاڅېدل ښۀ عادت دے۔','Waking up early is a good habit.','صبح جلدی اٹھنا اچھی عادت ہے۔'),
 ('رواج','زمونږ په کلي کښې دغه رواج شته۔','This custom exists in our village.','ہمارے گاؤں میں یہ رواج ہے۔'),
 ('ژبه','پښتو زمونږ مورنۍ ژبه ده۔','Pashto is our mother tongue.','پشتو ہماری مادری زبان ہے۔')],
('091','q 4 | دا لفظونه'):[
 ('چالاکه','ګیدړ ډېر چالاکه وو۔','The fox was very clever.','لومڑی بہت چالاک تھی۔'),
 ('ناڅاپه','ناڅاپه باران پیل شو۔','It suddenly began to rain.','اچانک بارش شروع ہو گئی۔'),
 ('راجمع','ټول ماشومان په ښوونځي کښې راجمع شول۔','All the children gathered in the school.','سب بچے اسکول میں جمع ہو گئے۔'),
 ('هوښیارتیا','په هوښیارتیا سره کار وکړه۔','Do the work with intelligence.','ہوشیاری سے کام کرو۔'),
 ('غر','د غر سر په واورو پټ دے۔','The mountain top is covered with snow.','پہاڑ کی چوٹی برف سے ڈھکی ہے۔')],
('107','q 3 | دا لفظونه'):[
 ('ایسار','ایسار د ښۀ انسان نښه ده۔','Sacrifice is the sign of a good person.','ایثار اچھے انسان کی نشانی ہے۔'),
 ('جنګ جګړه','جنګ جګړه ښۀ نۀ ده۔','War and fighting are not good.','لڑائی جھگڑا اچھا نہیں۔'),
 ('خدمتګار','خدمتګار د مېلمنو خدمت کوي۔','The servant serves the guests.','خادم مہمانوں کی خدمت کرتا ہے۔'),
 ('خواو شا','د کور خواو شا ونې ولګول شوې۔','Trees were planted around the house.','گھر کے ارد گرد درخت لگائے گئے۔'),
 ('زنځیر','قېدي په زنځیر تړلے وو۔','The prisoner was tied with a chain.','قیدی زنجیر سے بندھا تھا۔')],
('122','q 3 | دا لفظونه'):[
 ('ماشوم','ماشوم په مور پسې ژاړي۔','The child cries for its mother.','بچہ ماں کے لیے روتا ہے۔'),
 ('جینۍ','جینۍ کتاب لولي۔','The girl reads a book.','لڑکی کتاب پڑھتی ہے۔'),
 ('هلک','هلک په ډګر کښې لوبې کوي۔','The boy plays in the field.','لڑکا میدان میں کھیلتا ہے۔'),
 ('ښځه','ښځه په کور کښې کار کوي۔','The woman works at home.','عورت گھر میں کام کرتی ہے۔'),
 ('نوکر','نوکر د چا کار کوي۔','The servant does his master\'s work.','نوکر مالک کا کام کرتا ہے۔')],
('134','q 4 | لاندې ورکړي'):[
 ('آزادي','آزادي ډېره لویه نعمت ده۔','Freedom is a very great blessing.','آزادی بہت بڑی نعمت ہے۔'),
 ('جلسه','په ښوونځي کښې جلسه وشوه۔','A meeting was held in the school.','اسکول میں جلسہ ہوا۔'),
 ('جلوس','د آزادۍ په ورځ جلوس وویستل شو۔','A procession was taken out on Independence Day.','یومِ آزادی پر جلوس نکالا گیا۔'),
 ('غازیان','غازیان د وطن ساتونکي دي۔','The ghazis are the guardians of the homeland.','غازی وطن کے محافظ ہیں۔'),
 ('خدائي خدمتګار','خدائي خدمتګارو د آزادۍ لپاره جدوجهد وکړ۔','The Khudai Khidmatgars struggled for freedom.','خدائی خدمتگاروں نے آزادی کے لیے جدوجہد کی۔')],
('151','q 6 | دا لفظونه'):[
 ('قلا','بالاحصار په پېښور کښې یوه قلا ده۔','Bala Hisar is a fort in Peshawar.','بالا حصار پشاور میں ایک قلعہ ہے۔'),
 ('دروازه','د کور دروازه بنده ده۔','The door of the house is closed.','گھر کا دروازہ بند ہے۔'),
 ('نمونه','دا د ښکلې هنر ښۀ نمونه ده۔','This is a good sample of fine art.','یہ خوبصورت فن کا اچھا نمونہ ہے۔'),
 ('حویلۍ','زمونږ حویلۍ ډېره پراخه ده۔','Our courtyard house is very spacious.','ہماری حویلی بہت کشادہ ہے۔'),
 ('مقبره','د بزرګ مقبره په غرۍ کښې ده۔','The saint\'s tomb is on the hill.','بزرگ کا مقبرہ پہاڑی پر ہے۔')],
('166','q 4 | دا لفظونه'):[
 ('کرکټ','کرکټ زما خوښه لوبه ده۔','Cricket is my favourite game.','کرکٹ میری پسندیدہ کھیل ہے۔'),
 ('فارمېټ','د لوبې درې فارمېټونه دي۔','The game has three formats.','کھیل کے تین فارمیٹ ہیں۔'),
 ('عالمي کپ','پاکستان په ۱۹۹۲ کښې عالمي کپ وګټلو۔','Pakistan won the World Cup in 1992.','پاکستان نے ۱۹۹۲ میں عالمی کپ جیتا۔'),
 ('میچ','نن د پاکستان او هند میچ دے۔','Today is the Pakistan-India match.','آج پاکستان اور بھارت کا میچ ہے۔'),
 ('رېکارډ','هغه نوے رېکارډ جوړ کړ۔','He set a new record.','اس نے نیا ریکارڈ بنایا۔')],
}
for (pg,pre),items in T.items():
    add(pg,pre,'؛ '.join(f'{w}: {p}' for w,p,_,_ in items),
        ' '.join(f'{w}: {e}' for w,_,e,_ in items)+' (model sentences; Not verified by a native speaker)',
        ' '.join(f'{w}: {u}' for w,_,_,u in items))
