from ishisthelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,g='q',**m): add(s,f'q{len(s["paras"])+1}',en,ur,ps,listGroup=g,exerciseId='ishist11-ch18-q',tab='exercise',role='question',**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting, page-edge shadows, a thumb at the page edge and ornamental borders excluded. Scan n = printed page n-1 (file = {p//2+1:03d}_page_2 for even printed page p, {(p-1)//2+1:03d}_page_1 for odd p).'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
SA='صلی اللہ علیہ و علیٰ آلہ واصحابہ وسلم'
SP='صلی الله علیه وعلی آله واصحابه وسلم'
RA='رضی اللہ عنہ'
TF='(درست/غلط)'
# scan 307 = file 154_page_2, printed 306
s=page(307,'ch18','306','Hisham: his biography (end)','ہشام: سیرت (اختتام)','هشام: سیرت (پای)','ch18p306')
F=Flow(s)
P(s,'کی سخت تاکید کیا کرتا تھا۔ ہشام کو عیش و عشرت سے نفرت تھی۔ رعایا کے اخلاق پر خاص توجہ دی جاتی تھی۔ ہشام بڑا علم دوست اور فن پرور تھا، علماء و فضلاء کی بہت قدر کرتا تھا۔ ہشام نے دفتری نظام کو از سرِ نو منظم کر کے اسے جدید خطوط پر استوار کیا دفاتر میں ڈسپلن اور ترتیب پیدا کی۔ بیت المال کو منظم کیا گیا اب اس میں ایک پیسہ کی بھی خرد برد نہیں ہو سکتی تھی۔ مذہبی معاملات میں بہت سنجیدہ تھے بدعت وغیرہ سے سخت نفرت تھی۔ معد بن درہم کو خلقِ قرآن کا مسئلہ پیدا کرنے کی وجہ سے قتل کروا دیا۔ غیلان بن یونس کو پھانسی دی گئی۔ ہشام عیش و عشرت سے دور بھاگتا تھا شراب موسیقی سے نفرت تھی۔ ہشام کو علم و فن سے گہری دلچسپی تھی۔ امام زہری سے چار سو احادیث کا مجموعہ مرتب کروایا۔ ایرانیوں کی ایک تاریخی کتاب کا ترجمہ فارسی اور عربی میں کروایا۔ الغرض ہشام مستقل مزاج، بلند حوصلہ اور بہادر حکمران تھا۔','(he used to emphasise) strictly. Hisham hated luxury and pleasure. Special attention was paid to the morals of the subjects. Hisham was a great lover of knowledge and patron of the arts; he greatly respected scholars and learned men. Hisham, reorganising the office system anew, put it on modern lines and created discipline and order in the offices. The Bayt al-Mal was organised; now not even a penny could be embezzled in it. He was very serious in religious matters and had a strong hatred of innovations. Ma’bad bin Dirham was killed for raising the question of the createdness of the Quran. Ghaylan bin Yunus was hanged. Hisham ran away from luxury and pleasure and hated wine and music. Hisham had a deep interest in knowledge and arts; he had a collection of four hundred hadith compiled by Imam Zuhri. He had a historical book of the Iranians translated into Persian and Arabic (sic). In short, Hisham was a steadfast, high-spirited and brave ruler.','(ټینګار یې کاوه) په سختۍ. هشام له عیش او عشرت نفرت کاوه. د رعیت اخلاقو ته ځانګړې پام کېده. هشام ډېر د علم دوست او هنر پالونکی و، د عالمانو او فاضلانو ډېر قدر یې کاوه. هشام د دفتري نظام له سره منظم کولو سره هغه په نویو خطونو ودراوه او په دفترونو کې یې نظم او ترتیب پیدا کړ. بیت المال منظم شو اوس په هغه کې د یو پیسې خورد برد هم نه شو کېدای. په دیني معاملو کې ډېر جدي و له بدعت نه یې سخت نفرت کاوه. معبد بن درهم د خلق قرآن د مسئلې د پیدا کولو له امله ووژل شو. غیلان بن یونس په دار ځړول شو. هشام له عیش او عشرت تښتېده له شرابو او موسیقۍ یې نفرت کاوه. هشام ته په علم او هنر ژوره دلچسپي وه. له امام زهري نه یې د څلورو سوو احادیثو ټولګه ترتیب کړه. د ایرانیانو یو تاریخي کتاب ژباړه یې په فارسي او عربي کې وکړه. لنډه دا چې هشام ټینګ مزاجه، لوړ حوصلې او زړور حکمران و.')
F.done()
fin(s,'Printed page 306: the end of the biography of Hisham bin Abd al-Malik (continuing from page 305): his thrift, care for the morals of the subjects, patronage of knowledge, reorganisation of offices and of the Bayt al-Mal, strictness in religion (the killing of Ma’bad bin Dirham and Ghaylan bin Yunus), the collection of hadith by Imam Zuhri, and the translation of a Persian historical book. A row of two or three stars at the end is as printed (handwritten stars over it are excluded). The first words are the end of the sentence from page 305.')
# scan 308 = file 154_page_1, printed 307
s=page(308,'ch18','307','Chapter 18 exercise questions','مشقی سوالات (اٹھارہواں باب)','تمرین پوښتنې (اتلسم باب)','ch18p307')
F=Flow(s)
H(s,'سوالات','Questions','پوښتنې')
Q(s,'۱۔ ہشام بن عبد الملک کی سیرت اور کارنامے تحریر کریں۔','1. Write the biography and the achievements of Hisham bin Abd al-Malik.','۱. د هشام بن عبدالملک سیرت او کارنامې ولیکئ.')
Q(s,'۲۔ ہشام بن عبد الملک کے دور کے مشہور واقعات لکھیں۔','2. Write the famous events of the period of Hisham bin Abd al-Malik.','۲. د هشام بن عبدالملک د دورې مشهورې پېښې ولیکئ.')
Q(s,'۳۔ ہشام بن عبد الملک کی مختلف مہمات کا ذکر کریں۔','3. Mention the various campaigns of Hisham bin Abd al-Malik.','۳. د هشام بن عبدالملک مختلفې مهمې یاد کړئ.')
Q(s,'۴۔ مندرجہ ذیل پر مختصر نوٹ لکھیں۔','4. Write short notes on the following.','۴. په لاندې باندې لنډ یادښت ولیکئ.')
Q(s,'(۱) امام زید بن علی   (۲) عباسی تحریک','(1) Imam Zayd bin Ali   (2) The Abbasid movement','(۱) امام زید بن علي   (۲) عباسي خوځښت',g='q4')
Q(s,'۵۔ مندرجہ ذیل خالی جگہیں پُر کریں۔','5. Fill in the following blanks.','۵. لاندې تشې ځایونه ډک کړئ.')
for u,e,p in [
 ('(i) یزید ثانی عبد الملک کا اور یزید اول کا ........ تھا۔','(i) Yazid II was the ........ of Abd al-Malik and of Yazid I.','(i) یزید ثاني د عبدالملک او د یزید اول ........ و.'),
 ('(ii) یزید ثانی نے ........ کے دور کی یاد تازہ کر دی۔','(ii) Yazid II refreshed the memory of the period of ........','(ii) یزید ثاني د ........ د دورې یادونه تازه کړه.'),
 ('(iii) ہشام کا شمار بنو امیہ کے ........ اہم خلفاء میں ہوتا ہے۔','(iii) Hisham is counted among the ........ important caliphs of Banu Umayyah.','(iii) د هشام شمېر د بنو امیه په ........ مهمو خلفاو کې کېږي.'),
 ('(iv) شمالی افریقہ میں ........ کے کارخانے بنائے گئے۔','(iv) In North Africa factories of ........ were built.','(iv) په شمالي افریقا کې د ........ کارخانې جوړې شوې.')]:
    Q(s,u,e,p,g='q5')
Q(s,'۶۔ درست/غلط جواب پر (✓) نشان لگائیں۔','6. Put a (✓) mark on the true/false answer.','۶. پر سم / ناسم ځواب (✓) نښه ولګوئ.')
for u,e,p in [
 ('(i) یزید ثانی عبد الملک کا بیٹا تھا۔','(i) Yazid II was the son of Abd al-Malik.','(i) یزید ثاني د عبدالملک زوی و.'),
 ('(ii) عبد الملک نے یزید کی بیٹی عاتکہ سے شادی کی تھی۔','(ii) Abd al-Malik had married Atikah, the daughter of Yazid.','(ii) عبدالملک د یزید له لور عاتکې سره واده کړی و.'),
 ('(iii) یزید ثانی متقی اور پرہیز گار تھے۔','(iii) Yazid II was God-fearing and pious.','(iii) یزید ثاني متقي او پرهېزګار و.'),
 ('(iv) یزید ثانی کو عبد الملک کا عیاش اور فضول خرچ بیٹا کہا گیا ہے۔','(iv) Yazid II has been called the pleasure-loving and wasteful son of Abd al-Malik.','(iv) یزید ثاني ته د عبدالملک عیاش او بې ځایه لګښت کوونکی زوی ویل شوی دی.'),
 ('(v) یزید ثانی کی محبوب لونڈی حبابہ تھی۔','(v) The favourite slave-girl of Yazid II was Habbabah.','(v) د یزید ثاني محبوبه وینځه حبابه وه.')]:
    Q(s,u+'  '+TF,e+'  (true / false)',p+'  (سم / ناسم)',g='q6')
F.done()
fin(s,'Printed page 307: the exercise of Chapter 18 (headed “سوالات”: questions 1–4, blanks (i)–(iv) of question 5 and true/false items (i)–(v) of question 6; the list continues on the next page). The handwritten answers in the blanks (e.g. “نواسہ”, “یزید اول”, “تین”, “کپڑے”), handwritten ticks and the pencil marks are excluded; the blanks are left empty. The printed “درست/غلط” beside each item is added after the item text.')
# scan 309 = file 155_page_2, printed 308
s=page(309,'ch18','308','Chapter 18 exercise (end): true/false (vi)–(xx)','سوالات (اختتام): درست/غلط (vi) تا (xx)','پوښتنې (پای): سم / ناسم (vi) تر (xx)','ch18p308')
F=Flow(s)
for u,e,p in [
 ('(vi) یزید ثانی 40 سال کی عمر میں فوت ہوا۔','(vi) Yazid II died at the age of 40 years.','(vi) یزید ثاني په ۴۰ کلنۍ کې وفات شو.'),
 ('(vii) یزید ثانی کے بعد ہشام تخت نشین ہوا۔','(vii) After Yazid II Hisham ascended the throne.','(vii) د یزید ثاني وروسته هشام په تخت کېناست.'),
 ('(viii) ہشام نے 20 سال حکومت کی۔','(viii) Hisham ruled for 20 years.','(viii) هشام ۲۰ کاله حکومت وکړ.'),
 ('(ix) خاقان نے بخارا اور سمرقند پر حملے کیے۔','(ix) The Khaqan attacked Bukhara and Samarqand.','(ix) خاقان پر بخارا او سمرقند بریدونه وکړل.'),
 ('(x) سندھ کا گورنر جنید بن عبد الرحمٰن تھا۔','(x) The governor of Sindh was Junayd bin Abd al-Rahman.','(x) د سند والي جنید بن عبدالرحمن و.'),
 ('(xi) راجہ داہر کا بیٹا جے سنگھ مسلمان ہو گیا۔','(xi) The son of Raja Dahir, Jai Singh, became a Muslim.','(xi) د راجا داهر زوی جے سنګ مسلمان شو.'),
 ('(xii) حکم بن عوانہ کو سندھ کا گورنر مقرر کیا گیا۔','(xii) Hakam bin Awanah was appointed governor of Sindh.','(xii) حکم بن عوانه د سند والي وټاکل شو.'),
 ('(xiii) والیِ اندلس کے امیر عنسہ نے پیش قدمی کی۔','(xiii) The ruler of Andalus, Amir Anbasah, advanced.','(xiii) د اندلس والي امیر عنبسه مخکې تګ وکړ.'),
 ('(xiv) ٹورس کے قریب مشہور جنگ لڑی گئی۔','(xiv) A famous battle was fought near Tours.','(xiv) د تورس ته نژدې مشهور جګړه وشوه.'),
 ('(xv) جنگِ ٹورس میں عبد الرحمٰن شہید ہوئے۔','(xv) Abd al-Rahman was martyred in the Battle of Tours.','(xv) د تورس په جګړه کې عبدالرحمن شهید شو.'),
 ('(xvi) افریقہ کا گورنر عبد اللہ بن حجاب تھا۔','(xvi) The governor of Africa was Abdullah bin Hajjab.','(xvi) د افریقا والي عبدالله بن حجاب و.'),
 ('(xvii) حضرت امام زین العابدین کے بیٹے امام زید تھے۔','(xvii) The son of Hazrat Imam Zayn al-Abidin was Imam Zayd.','(xvii) د حضرت امام زین العابدین زوی امام زید و.'),
 ('(xviii) محمد بن علی حمیمہ میں ٹھہرے ہوئے تھے۔','(xviii) Muhammad bin Ali was staying at Humaymah.','(xviii) محمد بن علي په حمیمه کې اوسېده.'),
 ('(xix) ہشام 55 سال کی عمر میں فوت ہوا۔','(xix) Hisham died at the age of 55 years.','(xix) هشام په ۵۵ کلنۍ کې وفات شو.'),
 ('(xx) ہشام کا شمار بنو امیہ کے تین مشہور خلفاء میں ہوتا ہے۔','(xx) Hisham is counted among the three famous caliphs of Banu Umayyah.','(xx) د هشام شمېر د بنو امیه په درېیو مشهورو خلفاو کې کېږي.')]:
    Q(s,u+'  '+TF,e+'  (true / false)',p+'  (سم / ناسم)',g='q6')
F.done()
fin(s,'Printed page 308: true/false items (vi)–(xx) of question 6 of the exercise of Chapter 18, followed by a row of three stars. The handwritten ticks are excluded. The printed statement (xi) is as printed even though the name (Jai Singh) differs from the earlier text. The printed “کے امیر عنسہ” is as printed.')
# scan 310 = file 155_page_1, printed 309
s=page(310,'ch19','309','Chapter 19: Walid bin Yazid (125–126 AH / 743–744 CE) — accession; Nasr bin Sayyar; Yahya bin Zayd','انیسواں باب: ولید بن یزید (125ھ تا 126ھ بمطابق 743ء تا 744ء) — تخت نشینی؛ نصر بن سیار؛ یحییٰ بن زید','نولسم باب: ولید بن یزید (۱۲۵ تر ۱۲۶ هـ د ۷۴۳ تر ۷۴۴ ز) — تخت ناستې؛ نصر بن سیار؛ یحیی بن زید','ch19p309')
F=Flow(s)
H(s,'انیسواں باب','Chapter 19','نولسم باب')
H(s,'ولید بن یزید','Walid bin Yazid','ولید بن یزید')
H(s,'(125ھ تا 126ھ بمطابق 743ء تا 744ء)','(125 AH to 126 AH, corresponding to 743 CE to 744 CE)','(۱۲۵ تر ۱۲۶ هجري د ۷۴۳ تر ۷۴۴ زېږدیز سره سم)')
P(s,'تخت نشینی: ہشام کی موت کے بعد یزید بن عبد الملک کا بیٹا ولید بن یزید تخت نشین ہوا۔ ولید اوباش، شرابی اور عیاش تھا۔ ولید ہر لحاظ سے نااہل حکمران تھا اس نے عمال کو تبدیل کر کے نئے انتظامات کیے تمام صوبائی سربراہوں کو بیعت لینے کے لیے لکھا اس کے ساتھ ہی اس نے اپنے بیٹوں حکم اور عثمان کو اپنا ولی عہد مقرر کیا ان کی بیعت کا سلسلہ بھی شروع کیا گشتی فرمان عراق اور خراسان بھیجا گیا۔','Accession: After the death of Hisham, the son of Yazid bin Abd al-Malik, Walid bin Yazid, ascended the throne. Walid was a debauched, drunkard and pleasure-seeker. Walid was an incompetent ruler in every respect; he made new arrangements by changing the officials; he wrote to all the provincial heads to take the pledge; along with this he appointed his sons Hakam and Uthman as his heirs and also began the series of pledges to them; circular decrees were sent to Iraq and Khurasan.','تخت ناستې: د هشام له مړینې وروسته د یزید بن عبدالملک زوی ولید بن یزید په تخت کېناست. ولید اوباش، شرابي او عیاش و. ولید په هر لحاظ نااهله حکمران و هغه عمال بدلولو سره نوي انتظامات وکړل ټولو ولایتي مشرانو ته یې د بیعت اخیستلو لپاره ولیکل له هغې سره یې خپل زامن حکم او عثمان خپل ولیعهد وټاکل د هغوی د بیعت لړۍ یې هم پیل کړه ګرځنده فرمانونه عراق او خراسان ته ولېږل شول.')
H(s,'نصر بن سیار:','Nasr bin Sayyar:','نصر بن سیار:')
P(s,'ولید نے نصر بن سیار کو خراسان کا گورنر مقرر کیا بعد میں یوسف نے منت سماجت کر کے اسے معزول کروا دیا۔ نصر کو لکھا کہ اپنے اہل و عیال، اموال و تحائف کے ساتھ چلے آؤ۔ نصر نے اپنی مرضی کے عمال مقرر کر کے دمشق کا رخ کیا لیکن راستے میں نصر کو پتہ چلا کہ شام میں فتنہ و فساد برپا ہو چکا ہے اور یوسف بھاگ چکا ہے نصر واپس خراسان چلا گیا۔','Walid appointed Nasr bin Sayyar governor of Khurasan; later Yusuf, by entreaties, had him dismissed. He wrote to Nasr to come with his family and wealth and gifts. Nasr, appointing officials of his own choice, turned towards Damascus, but on the way Nasr learnt that sedition and disorder had broken out in Syria and Yusuf had fled; Nasr went back to Khurasan.','ولید نصر بن سیار د خراسان والي وټاکه وروسته یوسف په زارۍ هغه معزول کړ. نصر ته یې ولیکل چې له خپلې کورنۍ، مالونو او ډالیو سره راشه. نصر د خپلې خوښې عمال ټاکلو سره د دمشق لوري ته مخ کړ خو په لار کې نصر ته معلومه شوه چې په شام کې فتنه او فساد جوړ شوی او یوسف تښتېدلی دی نصر بیرته خراسان ته ولاړ.')
H(s,'یحییٰ بن زید:','Yahya bin Zayd:','یحیی بن زید:')
P(s,'یحییٰ بن زید اپنے باپ زید بن علی کی شہادت کے بعد خراسان چلا گیا۔ بلخ میں حریش بن ظہر کے مکان میں رہائش اختیار کی۔ یوسف نے نصر کو لکھا کہ یحییٰ کو گرفتار کیا جائے اور دمشق بھیج دیا جائے۔ نصر نے حریش کو سخت سزائیں دیں لیکن اس نے','Yahya bin Zayd went to Khurasan after the martyrdom of his father Zayd bin Ali. He took residence in the house of Harish bin Zuhayr in Balkh. Yusuf wrote to Nasr that Yahya be arrested and sent to Damascus. Nasr gave severe punishments to Harish but he','یحیی بن زید د خپل پلار زید بن علي له شهادت وروسته خراسان ته ولاړ. په بلخ کې یې د حریش بن ظهیر په کور کې استوګنه غوره کړه. یوسف نصر ته ولیکل چې یحیی دې ونیول شي او دمشق ته دې ولېږل شي. نصر حریش ته سختې سزاګانې ورکړې خو هغه',cont=True)
F.done()
fin(s,'Printed page 309: the title page of Chapter 19 (“انیسواں باب — ولید بن یزید (125ھ تا 126ھ بمطابق 743ء تا 744ء)”; the dates are overwritten by handwriting and read from the print), the accession of Walid bin Yazid, Nasr bin Sayyar and Yahya bin Zayd (the sentence continues on the next page). A thumb at the lower left is excluded. The printed “منت سماجت” is as printed.')
