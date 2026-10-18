from ishisthelp import *
c=cell
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def P(s,ur,en,ps,**m): add(s,f'p{len(s["paras"])+1}',en,ur,ps,**m)
def Q(s,ur,en,ps,g='q',**m): add(s,f'q{len(s["paras"])+1}',en,ur,ps,listGroup=g,exerciseId='ishist11-ch17-q',tab='exercise',role='question',**m)
NOTE=' English and Pashto are our translations (need native review); watermark, handwriting, page-edge shadows, a thumb at the page edge and ornamental borders excluded. Scan n = printed page n-1 (file = {p//2+1:03d}_page_2 for even printed page p, {(p-1)//2+1:03d}_page_1 for odd p).'
def fin(s,note):
    s['sourceNote']=note+NOTE; s['vocabulary']={}; save(s)
SA='صلی اللہ علیہ و علیٰ آلہ واصحابہ وسلم'
SP='صلی الله علیه وعلی آله واصحابه وسلم'
RA='رضی اللہ عنہ'
AS='علیہ السلام'
YN='  ہاں/نہیں'
# scan 287 = file 144_page_2, printed 286
s=page(287,'ch17','286','Umar bin Abd al-Aziz: official duties (end); the Islamic empire','عمر بن عبد العزیز: فرائضِ منصبی (اختتام)؛ اسلامی سلطنت','عمر بن عبدالعزیز: منصبي دندې (پای)؛ اسلامي سلطنت','ch17p286')
F=Flow(s)
P(s,'بھی بڑی محنت اور مشقت سے سرانجام دیتے تھے، مسلسل کام کرنے کی وجہ سے آپ کو آرام کرنے کا مشورہ دیا جاتا لیکن آپ ٹال دیا کرتے تھے۔ دن بھر رعایا کے مقدمات اور معاملات میں مصروف رہتے۔ عشاء کی نماز کے بعد صوبائی گورنروں کو احکامات لکھواتے اور دوسرے دفتری کام سرانجام دیتے اس کے بعد مجلسِ شوریٰ سے مشورے لیتے، سونے کے لیے بہت کم وقت ہوتا تھا۔','also with great effort and hard work; because of continuous work he was advised to rest but he used to put it off. The whole day he remained busy with the cases and affairs of the subjects. After the Isha prayer he had orders written to the provincial governors and performed other office work; after that he took advice from the Majlis-e-Shura; there was very little time for sleep.','هم په ډېر زیار او مشقت سرته رسول، د پرله پسې کار کولو له امله ورته د آرام مشوره ورکول کېده خو هغه ځنډاوه. ټوله ورځ د رعیت په قضیو او معاملو بوخت و. د ماسخوتن له لمانځه وروسته به یې والیانو ته حکمونه لیکل او نور دفتري کارونه به یې سرته رسول له دې وروسته به یې له مجلس شورا مشورې اخیستلې، د ویده کېدو لپاره ډېر لږ وخت و.')
H(s,'اسلامی سلطنت:','The Islamic Empire:','اسلامي سلطنت:')
P(s,f'حضرت عمر بن عبد العزیز {RA} نے ولید بن عبد الملک کی وسیع و عریض سلطنت کو اسلامی سلطنت بنا دیا، اس کے لیے اپنی جان کی قربانی بھی دینی پڑی لیکن آپ نے اسلامی انقلاب برپا کیا۔ آپ کی عظیم سیرت کی وجہ سے غیر مسلم بھی آپ کو قدر کی نگاہ سے دیکھتے تھے۔ آپ کی وفات پر قیصرِ روم نے مندرجہ ذیل الفاظ کہے:','Hazrat Umar bin Abd al-Aziz made the vast empire of Walid bin Abd al-Malik an Islamic empire; for this he even had to sacrifice his life, but he brought about an Islamic revolution. Because of his great character even non-Muslims looked at him with respect. On his death the Caesar of Rome said the following words:',f'حضرت عمر بن عبدالعزیز رضی الله عنه د ولید بن عبدالملک پراخه سلطنت اسلامي سلطنت وګرځوله، د دې لپاره یې خپله ساه هم قرباني کړه خو هغه اسلامي انقلاب راوست. د هغه د عظیم سیرت له امله غیر مسلمانانو هم هغه ته په درناوي کتل. د هغه د وفات پر مهال د روم قیصر لاندې ټکي وویل:')
P(s,f'’’اگر حضرت عیسیٰ {AS} کے بعد کوئی مردوں کو زندہ کر سکتا تو وہ حضرت عمر بن عبد العزیز {RA} ہی ہو سکتے تھے، مجھے اس راہب کی حالت پر کوئی تعجب نہیں جس نے دروازے بند کر کے دنیا چھوڑ دی، مجھے اس شخص کی حالت پر تعجب ہے جس کے قدموں کے نیچے دنیا تھی لیکن اس نے اس کو پامال کر کے راہبانہ زندگی اختیار کی۔‘‘','“If after Hazrat Isa anyone could bring the dead to life, it could have been Hazrat Umar bin Abd al-Aziz; I am not at all surprised at the condition of that monk who shut the doors and left the world; I am surprised at the condition of the man under whose feet was the world but who trampled it and adopted a monastic life.”','“که د حضرت عیسی علیه السلام وروسته کوم څوک مړي ژوندي کولای شي نو هغه حضرت عمر بن عبدالعزیز رضی الله عنه ښایي، ما ته د هغه راهب په حالت هېڅ تعجب نشته چې دروازې یې وتړلې او دنیا یې پرېښوده، ما ته د هغه چا په حالت تعجب دی چې د پښو لاندې یې دنیا وه خو هغه هغه پایمال کړ او راهبانه ژوند یې غوره کړ.”')
F.done()
fin(s,'Printed page 286: the end of the section on the official duties of Umar bin Abd al-Aziz, “اسلامی سلطنت” and the words of the Caesar of Rome at his death. The handwritten scribbles at the upper left corner are excluded. The sentence at the top is the continuation from page 285.')
# scan 288 = file 144_page_1, printed 287
s=page(288,'ch17','287','Chapter 17 exercise questions: yes/no (start)','مشقی سوالات (سترہواں باب): ہاں/نہیں (آغاز)','تمرین پوښتنې (اولسم باب): هو/نه (پیل)','ch17p287')
F=Flow(s)
H(s,'مشقی سوالات','Exercise Questions','تمرین پوښتنې')
Q(s,f'۱۔ حضرت عمر بن عبد العزیز {RA} کی اصلاحات پر روشنی ڈالیے۔','1. Throw light on the reforms of Hazrat Umar bin Abd al-Aziz.','۱. د حضرت عمر بن عبدالعزیز رضی الله عنه په اصلاحاتو رڼا واچوئ.')
Q(s,f'۲۔ حضرت عمر بن عبد العزیز {RA} کی سیرت اور کارہائے نمایاں پر بحث کیجیے۔','2. Discuss the biography and outstanding achievements of Hazrat Umar bin Abd al-Aziz.','۲. د حضرت عمر بن عبدالعزیز رضی الله عنه په سیرت او مهمو کارنامو بحث وکړئ.')
Q(s,f'۳۔ حضرت عمر بن عبد العزیز {RA} کو پانچواں خلیفہ راشد کیوں کہا جاتا ہے؟ دلائل دیجیے۔','3. Why is Hazrat Umar bin Abd al-Aziz called the fifth Rightly Guided Caliph? Give arguments.','۳. حضرت عمر بن عبدالعزیز رضی الله عنه ولې پنځم خلیفه راشد بلل کېږي؟ دلیلونه ورکړئ.')
Q(s,'۴۔ ہاں یا نہیں میں جواب دیں۔','4. Answer in yes or no.','۴. په هو یا نه ځواب ورکړئ.')
for u,e,p in [
 ('(i) موسیٰ بن نصیر کو ڈیڑھ کوڑی کا محتاج کیا گیا۔','(i) Musa bin Nusayr was reduced to poverty.','(i) موسی بن نصیر محتاج کړل شو.'),
 ('(ii) سلیمان کی کوتاہ اندیشی سے خلافتِ اسلامیہ کو ناقابلِ تلافی نقصان پہنچا۔','(ii) The Islamic caliphate suffered irreparable loss from the shortsightedness of Sulayman.','(ii) د سلیمان د کوتاه نظرۍ له امله اسلامي خلافت ته نه جبرانیدونکی زیان ورسېد.'),
 (f'(iii) حضرت عمر بن عبد العزیز {RA} سلیمان بن عبد الملک کا حقیقی بھائی تھا۔','(iii) Hazrat Umar bin Abd al-Aziz was the real brother of Sulayman bin Abd al-Malik.','(iii) حضرت عمر بن عبدالعزیز رضی الله عنه د سلیمان بن عبدالملک ریښتینی ورور و.'),
 (f'(iv) حضرت عمر بن عبد العزیز {RA} نے غصب شدہ جاگیریں واپس کر دیں۔','(iv) Hazrat Umar bin Abd al-Aziz returned the confiscated estates.','(iv) حضرت عمر بن عبدالعزیز رضی الله عنه غصب شوي جاګیرونه بیرته ورکړل.'),
 ('(v) مروان نے باغِ فدک کو اپنی جاگیر بنا دیا تھا۔','(v) Marwan had made the garden of Fadak his own estate.','(v) مروان د فدک باغ خپل جاګیر کړی و.'),
 ('(vi) حضرت عمر ثانی بیت المال کو عوام کی امانت سمجھتے تھے۔','(vi) Hazrat Umar II regarded the Bayt al-Mal as a trust of the people.','(vi) حضرت عمر ثاني بیت المال د عوامو امانت ګاڼه.'),
 ('(vii) حضرت عمر ثانی نے فرمان جاری کیا کہ نماز کے وقت سارا کام چھوڑ دیا جائے۔','(vii) Hazrat Umar II issued a decree that at the time of prayer all work be left.','(vii) حضرت عمر ثاني فرمان جاري کړ چې د لمانځه پر مهال دې ټول کار پرېښودل شي.')]:
    Q(s,u+YN,e+'  Yes / No',p+'  هو / نه',g='q4')
F.done()
fin(s,'Printed page 287: the heading “مشقی سوالات” and the exercise of Chapter 17 (questions 1–3 and yes/no items (i)–(vii) of question 4; the exercise continues on the next page). The ticks over the “ہاں/نہیں” are excluded; a thumb at the lower left is excluded.')
# scan 289 = file 145_page_2, printed 288
s=page(289,'ch17','288','Chapter 17 exercise: blanks (i)–(xvi)','مشقی سوالات: خالی جگہیں (i) تا (xvi)','تمرین پوښتنې: تشې ځایونه (i) تر (xvi)','ch17p288')
F=Flow(s)
Q(s,'۵۔ خالی جگہیں پُر کریں۔','5. Fill in the blanks.','۵. تشې ځایونه ډک کړئ.')
for u,e,p in [
 ('(i) سلیمان بن عبد الملک نے ........ کارروائیاں شروع کیں۔','(i) Sulayman bin Abd al-Malik began ........ actions.','(i) سلیمان بن عبدالملک ........ کړنې پیل کړې.'),
 ('(ii) رومی جرنیل ........ نے سلیمان سے درخواست کی۔','(ii) The Roman general ........ made a request to Sulayman.','(ii) رومي جنرال ........ له سلیمان نه غوښتنه وکړه.'),
 ('(iii) ........ جرجان و طبرستان کو فتح کرنے کی سخت خواہش تھی۔','(iii) ........ had a strong wish to conquer Jurjan and Tabaristan.','(iii) ........ د جرجان او طبرستان د فتح کولو سخته هیله درلوده.'),
 ('(iv) سلیمان نے ........ کو اپنا ولی عہد مقرر کیا۔','(iv) Sulayman appointed ........ as his heir.','(iv) سلیمان ........ خپل ولیعهد وټاکه.'),
 ('(v) سلیمان ........ ہجری میں فوت ہوا۔','(v) Sulayman died in ........ AH.','(v) سلیمان په ........ هجري کې وفات شو.'),
 ('(vi) حضرت عمر بن عبد العزیز ........ کا چچا زاد بھائی تھا۔','(vi) Hazrat Umar bin Abd al-Aziz was the cousin of ........','(vi) حضرت عمر بن عبدالعزیز د ........ د کاکا زوی و.'),
 ('(vii) عمر ثانی کی والدہ حضرت ........ کی پوتی تھی۔','(vii) The mother of Umar II was the granddaughter of Hazrat ........','(vii) د عمر ثاني مور د حضرت ........ لمسۍ وه.'),
 ('(viii) ولید نے عمر ثانی کو ........ کا گورنر مقرر کیا تھا۔','(viii) Walid had appointed Umar II governor of ........','(viii) ولید عمر ثاني د ........ والي ټاکلی و.'),
 ('(ix) عمر ثانی کو پانچواں ........ کہا جاتا ہے۔','(ix) Umar II is called the fifth ........','(ix) عمر ثاني پنځم ........ بلل کېږي.'),
 ('(x) عمر ثانی کی بیوی فاطمہ ........ کی بیٹی تھی۔','(x) The wife of Umar II, Fatimah, was the daughter of ........','(x) د عمر ثاني ښځه فاطمه د ........ لور وه.'),
 ('(xi) شاہی افراد کی ........ واپس کر دیں۔','(xi) The ........ of the royal persons were returned.','(xi) د شاهي کسانو ........ بیرته ورکړل شول.'),
 ('(xii) باغِ فدک کی آمدنی ........ کے لیے وقف تھی۔','(xii) The income of the garden of Fadak was dedicated to ........','(xii) د فدک د باغ عاید د ........ لپاره وقف و.'),
 ('(xiii) عمر ثانی نے عمال کا ........ شروع کیا۔','(xiii) Umar II began the ........ of the officials.','(xiii) عمر ثاني د عمالو ........ پیل کړ.'),
 ('(xiv) بنو امیہ کے خلفاء نے بیت المال کو ........ بنایا ہوا تھا۔','(xiv) The caliphs of Banu Umayyah had made the Bayt al-Mal ........','(xiv) د بنو امیه خلفاو بیت المال ........ ګرځولی و.'),
 ('(xv) عمر ثانی نے مسلمانوں اور ذمیوں کے خون کو ........ قرار دیا۔','(xv) Umar II declared the blood of Muslims and dhimmis ........','(xv) عمر ثاني د مسلمانانو او ذمیانو وینه ........ وګرځوله.'),
 ('(xvi) عمر ثانی فتوحات سے زیادہ اسلام کی ........ کو اہمیت دیتے تھے۔','(xvi) Umar II gave more importance to the ........ of Islam than to conquests.','(xvi) عمر ثاني له فتحو نه زیات د اسلام ........ ته اهمیت ورکاوه.')]:
    Q(s,u,e,p,g='q5')
F.done()
fin(s,'Printed page 288: blanks (i)–(xvi) of question 5 of the exercise of Chapter 17. The page is cropped at the right edge in the scan, so the first words of some items are cut off and are restored from the sense; the handwritten answers written in the blanks (e.g. “انتقامی”, “لیو”, “یزید بن مہلب”, “عبد العزیز”, “99”, “عبد الملک”, “عمر فاروق”, “مدینہ”, “خلیفہ”, “عبد الملک”, “جاگیریں”, “رسول اللہ و بنو ہاشم”, “محاسبہ”, “ذاتی جاگیر”, “برابر”, “تبلیغ”) are excluded and the blanks are left empty. The “(ix) عمر ثانی کو … خلیفہ راشد” is given as printed with a gap.')
# scan 290 = file 145_page_1, printed 289
s=page(290,'ch17','289','Chapter 17 exercise (end): blanks (xvii)–(xx)','مشقی سوالات (اختتام): خالی جگہیں (xvii) تا (xx)','تمرین پوښتنې (پای): تشې ځایونه (xvii) تر (xx)','ch17p289')
F=Flow(s)
for u,e,p in [
 ('(xvii) ........ نے عمر ثانی کو فقیہ و مجتہد تسلیم کیا ہے۔','(xvii) ........ acknowledged Umar II as a jurist and mujtahid.','(xvii) ........ عمر ثاني فقیه او مجتهد منلی دی.'),
 ('(xviii) عمر ثانی نے مدینہ کے مشہور فقیہ ........ کو مصر روانہ کیا۔','(xviii) Umar II sent the famous jurist of Madinah, ........, to Egypt.','(xviii) عمر ثاني د مدینې مشهور فقیه ........ مصر ته ولېږه.'),
 ('(xix) عمر ثانی رات کو سونے سے پہلے ........ کیا کرتے تھے۔','(xix) Umar II used to ........ before sleeping at night.','(xix) عمر ثاني د شپې د ویده کېدو مخکې ........ کول.'),
 ('(xx) عمر ثانی ........ کی نماز کے بعد گورنروں کو احکامات لکھواتے تھے۔','(xx) After the ........ prayer Umar II had orders written to the governors.','(xx) عمر ثاني د ........ د لمانځه وروسته والیانو ته حکمونه لیکل.')]:
    Q(s,u,e,p,g='q5')
F.done()
fin(s,'Printed page 289: the last four blanks of question 5 of the exercise of Chapter 17, followed by a row of three stars; the rest of the page is blank (faint show-through). The handwritten answers written in the blanks (“حافظ ذہبی”, “نافع”, “تلاوت قرآن / دعا”, “عشاء”) are excluded. A thumb at the lower left is excluded.')
