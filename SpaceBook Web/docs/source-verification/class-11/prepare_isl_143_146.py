from islhelp import *
def P(s,rows,pre='p'):
    for (ur,en,ps,*m) in rows: add(s,f'{pre}{len(s["paras"])+1}',en,ur,ps,**(m[0] if m else {}))
def H(s,ur,en,ps): add(s,f'h{len(s["paras"])+1}',en,ur,ps,kind='heading')
def Q(s,ur,en,ps,**k): add(s,f'q{len(s["paras"])+1}',en,ur,ps,role='question',exerciseId='isl11-u04-q',tab='exercise',**k)
A=lambda **k:dict(kind='aside',**k)
GAP=lambda t:dict(sourceGap=dict(note=t))
def V(ar,en,ps,**k): return (ar,en,ps,A(**k))
NOTE=' The English and Pashto columns are our translations; the Arabic is read from the scan with its vowel marks and needs checking against the source texts. The watermark and "Whatsapp" strip are excluded.'
# scan 144 (printed 136)
s=page(144,'u04','136','Selected Hadith (2)','منتخب احادیث (2)','ټاکل شوي احادیث (۲)','selected-6')
F=Flow(s)
P(s,[V('وَالنَّاسِ اَجْمَعِیْنَ (بخاری، مسلم)','“… and all people.” (Bukhari, Muslim)','“… او ټولو خلکو نه.” (بخاري، مسلم)',sourceGap=dict(note='Completes the hadith from the foot of printed page 135.')),
('ترجمہ: تم میں سے کوئی شخص اس وقت تک ایمان دار نہیں ہو سکتا جب تک کہ میں اُسے اس کے والدین اور اولاد اور سب لوگوں سے بڑھ کر محبوب نہ ہو جاؤں۔','Translation: None of you can be a believer until I become more beloved to him than his parents, his children and all people.','ژباړه: ستاسو هېڅوک مؤمن نشي کېدای تر څو چې زه د هغه په نزد د هغه له مور پلار، اولاد او ټولو خلکو نه ډېر محبوب نشم.'),
V('لَا یُؤْمِنُ اَحَدُکُمْ حَتّٰی یُحِبَّ لِاَخِیْہِ مَا یُحِبُّ لِنَفْسِہٖ (بخاری، ترمذی، نسائی، ابن ماجہ، سنن داری، مسند احمد بن حنبل، اصول کافی بالمعنی)','“None of you believes until he loves for his brother what he loves for himself.” (Bukhari, Tirmidhi, Nasa’i, Ibn Majah, Sunan al-Darimi, Musnad Ahmad ibn Hanbal, Usul al-Kafi — by meaning)','“ستاسو هېڅوک مؤمن نه کېږي تر دې چې خپل ورور ته هغه څه خوښ نه کړي چې ځان ته یې خوښوي.” (بخاري، ترمذي، نسایي، ابن ماجه، سنن داري، مسند احمد بن حنبل، اصول کافي بالمعنی)'),
('ترجمہ: تم میں سے کوئی ایک اس وقت تک مومن نہیں ہو سکتا جب تک کہ وہ اپنے بھائی کے لیے وہ چیز پسند نہ کرے جو اپنے لیے پسند کرتا ہے۔','Translation: None of you can be a believer until he likes for his brother that which he likes for himself.','ژباړه: ستاسو هېڅوک مؤمن نشي کېدای تر څو چې خپل ورور ته هغه شی خوښ نه کړي چې ځان ته یې خوښوي.'),
V('اَلْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُوْنَ مِنْ لِسَانِہٖ وَیَدِہٖ (بخاری، مسلم، ابو داؤد، ترمذی، نسائی، سنن داری، مسند احمد بن حنبل، اصول کافی)','“A Muslim is one from whose tongue and hand the Muslims are safe.” (Bukhari, Muslim, Abu Dawud, Tirmidhi, Nasa’i, Sunan al-Darimi, Musnad Ahmad ibn Hanbal, Usul al-Kafi)','“مسلمان هغه دی چې د هغه له ژبې او لاسه نورو مسلمانانو ته خوندیتوب وي.” (بخاري، مسلم، ابوداود، ترمذي، نسایي، سنن داري، مسند احمد بن حنبل، اصول کافي)'),
('ترجمہ: مسلمان وہ ہے جس کی زبان اور ہاتھ سے دوسرے مسلمان محفوظ ہوں۔','Translation: A Muslim is the one from whose tongue and hand other Muslims are safe.','ژباړه: مسلمان هغه دی چې د هغه له ژبې او لاسه نور مسلمانان خوندي وي.'),
V('لَا یَرْحَمُ اللّٰہُ مَنْ لَّا یَرْحَمُ النَّاسَ (مسلم، ترمذی، مسند احمد بن حنبل)','“Allah does not show mercy to one who does not show mercy to people.” (Muslim, Tirmidhi, Musnad Ahmad ibn Hanbal)','“الله په هغه رحم نه کوي چې پر خلکو رحم نه کوي.” (مسلم، ترمذي، مسند احمد بن حنبل)'),
('ترجمہ: اللہ تعالیٰ اس پر رحم نہیں فرماتے جو لوگوں پر رحم نہیں کرتا۔','Translation: Allah the Exalted does not show mercy to one who does not show mercy to people.','ژباړه: الله تعالی په هغه رحم نه کوي چې پر خلکو رحم نه کوي.'),
V('کُلُّ الْمُسْلِمِ عَلَی الْمُسْلِمِ حَرَامٌ دَمُہٗ وَمَالُہٗ وَعِرْضُہٗ (ابن ماجہ، مسند احمد بن حنبل)','“Every Muslim is sacred to every [other] Muslim: his blood, his property and his honour.” (Ibn Majah, Musnad Ahmad ibn Hanbal)','“د هر مسلمان وینه، مال او عزت پر نورو مسلمانانو حرام دی.” (ابن ماجه، مسند احمد بن حنبل)'),
('ترجمہ: ہر مسلمان کا سب کچھ دوسرے مسلمان پر حرام ہے اس کا خون، اس کا مال اور اس کی عزت۔','Translation: Everything of every Muslim is forbidden [to violate] for another Muslim — his blood, his property and his honour.','ژباړه: د هر مسلمان هر څه پر بل مسلمان حرام دي — د هغه وینه، د هغه مال او د هغه عزت.'),
V('مَا عَالَ مَنِ اقْتَصَدَ (مسند احمد بن حنبل، اصول کافی بالمعنی)','“He who is moderate [in spending] will not become destitute.” (Musnad Ahmad ibn Hanbal, Usul al-Kafi — by meaning)','“څوک چې منځلاري اختیار کړي هغه به محتاج نه شي.” (مسند احمد بن حنبل، اصول کافي بالمعنی)'),
('ترجمہ: جس نے میانہ روی اختیار کی وہ محتاج نہیں ہوگا۔','Translation: Whoever adopted moderation will not become needy.','ژباړه: چا چې منځلاري اختیار کړه هغه به محتاج نه شي.'),
V('مَنْ سَلَکَ طَرِیْقًا یَّطْلُبُ فِیْہِ عِلْمًا سَلَکَ اللّٰہُ بِہٖ طَرِیْقًا مِّنْ طُرُقِ الْجَنَّۃِ (بخاری، ابو داؤد، ترمذی، ابن ماجہ، مسند احمد بن حنبل)','“Whoever treads a path seeking knowledge therein, Allah will make easy for him a path from the paths of Paradise.” (Bukhari, Abu Dawud, Tirmidhi, Ibn Majah, Musnad Ahmad ibn Hanbal)','“څوک چې د علم په لټه کې یوه لار ونیسي، الله به د هغه لپاره د جنت له لارو یوه لار اسانه کړي.” (بخاري، ابوداود، ترمذي، ابن ماجه، مسند احمد بن حنبل)'),
('ترجمہ: جو شخص علم کی تلاش میں کسی راستے پر چلتا ہے تو اللہ تعالیٰ اسے جنت کے','Translation: A person who walks on some path in search of knowledge, Allah the Exalted takes him on [one of the paths] of Paradise','ژباړه: هغه کس چې د علم په لټه کې په کومه لار ځي نو الله تعالی هغه د جنت',GAP('The translation continues at the top of the next page (printed page 137: “راستوں میں سے کسی راستے پر لے جاتا ہے”).'))])
F.done()
s['sourceNote']='Printed page 136 (the page number "136" is printed at the top with "Not for Sale"). The end of the first selected hadith from printed page 135, and six more selected hadith in Arabic with Urdu translations and source references; the last translation continues at the top of printed page 137. The scan lies after printed page 137 in photograph order. A dark strip at the right edge is ignored.'+NOTE
s['vocabulary']={}
save(s)
# scan 143 (printed 137)
s=page(143,'u04','137','Selected Hadith (end); Chapter 4 questions','منتخب احادیث (اختتام)؛ سوالات','ټاکل شوي احادیث (پای)؛ پوښتنې','selected-7')
F=Flow(s)
P(s,[('راستوں میں سے کسی راستے پر لے جاتا ہے۔','… takes him on one of the paths of Paradise.','… له لارو یوې لارې ته یې وړي.',GAP('Completes the translation from the foot of printed page 136.')),
V('اَلْمُؤْمِنُ اَخُو الْمُؤْمِنِ کَالْجَسَدِ الْوَاحِدِ اِنِ اشْتَکٰی شَیْئًا مِّنْہُ وَجَدَ اَلَمَ ذٰلِکَ فِیْ سَائِرِ جَسَدِہٖ (مسلم، ترمذی، مسند احمد بن حنبل، اصول کافی)','“The believer is the brother of the believer like one body; if any part of it complains, the rest of the body feels that pain.” (Muslim, Tirmidhi, Musnad Ahmad ibn Hanbal, Usul al-Kafi)','“مؤمن د مؤمن ورور دی لکه یو بدن؛ که د هغه یوه برخه شکایت وکړي نو د هغه ټول بدن د هغه درد احساسوي.” (مسلم، ترمذي، مسند احمد بن حنبل، اصول کافي)',sourceGap=dict(note='The Arabic is read from a small, partly worn scan; the text follows the standard wording.')),
('ترجمہ: ہر مومن دوسرے مومن کا بھائی ہے۔ جیسے ایک جسم ہے۔ اگر اس جسم کا کوئی حصہ کسی تکلیف میں مبتلا ہو تو وہ اپنے سارے جسم میں تکلیف محسوس کرے گا۔','Translation: Every believer is the brother of another believer, like one body. If any part of that body is afflicted with some pain, it will feel pain in its whole body.','ژباړه: هر مؤمن د بل مؤمن ورور دی. لکه یو بدن. که د دې بدن کومه برخه په تکلیف اخته شي نو هغه به په خپل ټول بدن کې تکلیف احساس کړي.')])
H(s,'سوالات','Questions','پوښتنې')
for ur,en,ps,*k in [('۱۔ قرآنِ مجید کے اسماء کون سے ہیں؟ پہلی وحی کے نزول کا واقعہ تفصیل سے لکھیں۔','1. What are the names of the Glorious Qur’an? Write in detail the incident of the revelation of the first revelation.','۱. د قرآن مجید نومونه کوم دي؟ د لومړۍ وحی د نزول پېښه په تفصیل سره ولیکئ.'),
('۲۔ مکی اور مدنی سورتوں کی خصوصیات تحریر کریں۔','2. Write the characteristics of the Makki and Madani surahs.','۲. د مکي او مدني سورتونو ځانګړتیاوې ولیکئ.'),
('۳۔ حجۃ الوداع کی تفصیل بیان کریں۔','3. Describe in detail the Farewell Hajj.','۳. د حجة الوداع تفصیل بیان کړئ.',dict(sourceGap=dict(note='The first word of this question is partly clipped in the scan (“جۃ الوداع”); it is read as “حجۃ الوداع”, but the question sits oddly within a chapter on the Qur’an and Hadith (perhaps “حجیتِ حدیث” was meant) — the printed wording should be checked against the book.'))),
('۴۔ مختصر نوٹ لکھیں: (۱) قرآنِ مجید کی حفاظت (۲) قرآنِ مجید کی ترتیب۔','4. Write brief notes: (1) preservation of the Glorious Qur’an (2) the arrangement of the Glorious Qur’an.','۴. لنډ نوټ ولیکئ: (۱) د قرآن مجید ساتنه (۲) د قرآن مجید ترتیب.'),
('۵۔ مندرجہ ذیل پر مختصر نوٹ لکھیں: (۱) عہدِ صدیقی میں قرآنِ مجید کی جمع و تدوین (۲) قرآنِ مجید کا اندازِ بیان (۳) قرآنِ مجید کی خوبیاں۔','5. Write brief notes on the following: (1) compilation of the Glorious Qur’an in the Siddiqi age (2) the style of the Glorious Qur’an (3) the merits of the Glorious Qur’an.','۵. په لاندې لنډ نوټ ولیکئ: (۱) د صدیقي دورې کې د قرآن مجید ټولګه (۲) د قرآن مجید د بیان انداز (۳) د قرآن مجید ښېګڼې.'),
('۶۔ حدیث کے معنی بیان کریں۔ حدیث کی اپنی حیثیت کیا ہے؟','6. State the meaning of hadith. What is the legal status of hadith?','۶. د حدیث معنا بیان کړئ. د حدیث خپله حیثیت څه دی؟'),
('۷۔ تدوینِ حدیث کے تینوں ادوار کا تفصیل سے ذکر کریں۔','7. Describe in detail the three periods of the compilation of hadith.','۷. د حدیث د ټولګې درې واړه دورې په تفصیل سره یاد کړئ.'),
('۸۔ صحاحِ ستہ اور ان کے مصنفین کے نام مع ان کے سنِ وفات لکھیں۔','8. Write the Sihah Sittah and the names of their authors with their years of death.','۸. صحاح ستة او د هغو د مصنفینو نومونه د هغوی د وفات د کال سره ولیکئ.'),
('۹۔ اصولِ اربعہ اور ان کے مصنفین کے نام مع ان کے سنِ وفات لکھیں۔','9. Write the Usul-e-Arba‘ah and the names of their authors with their years of death.','۹. اصول اربعه او د هغو د مصنفینو نومونه د هغوی د وفات د کال سره ولیکئ.')]:
    Q(s,ur,en,ps,**(k[0] if k else {}))
F.done()
s['sourceNote']='Printed page 137 (the page number "137" is printed at the top with "Not for Sale"). The first lines complete the translation from printed page 136; one more selected hadith in Arabic; the heading "سوالات" and Chapter 4 questions 1–9 (questions 4 and 5 have numbered sub-parts). The scan lies before printed page 136 in photograph order. A dark strip at the left edge is ignored. The scan’s question 3 reads “جۃ الوداع”, partly clipped.'+NOTE
s['vocabulary']={}
save(s)
# scan 145 (back matter, unnumbered box page)
s=page(145,'back-matter','','Back matter: a verse of the Qur’an (boxed)','آخری صفحات: قرآنی آیت (چوکھٹے میں)','وروستۍ پاڼې: قرآني آیت (په چوکاټ کې)','back-1')
F=Flow(s)
P(s,[('ایک دوسرے کا مال آپس میں ناحق نہ کھاؤ۔ (سورۃ البقرہ آیت 188)','Do not unjustly eat one another’s wealth among yourselves. (Surah Al-Baqarah, verse 188)','یو د بل مال په خپلو کې په ناحقه مه خورئ. (سورة البقره، آیت ۱۸۸)')])
F.done()
s['sourceNote']='A page with no printed number and no "Not for Sale" line: a decorative box containing the Urdu text of Al-Baqarah 2:188 (“ایک دوسرے کا مال آپس میں ناحق نہ کھاؤ”) with its reference; the rest of the page is blank. It is a filler/quotation page after the last numbered page 137 and is treated as back matter. The scan lies before the next boxed-quotation page in photograph order.'+NOTE
s['vocabulary']={}
save(s)
# scan 146 (back matter, two boxes)
s=page(146,'back-matter','','Back matter: two sayings of the Prophet (boxed)','آخری صفحات: نبی کریم ﷺ کے دو ارشادات (چوکھٹوں میں)','وروستۍ پاڼې: د نبي کریم ﷺ دوه ارشادات (په چوکاټونو کې)','back-2')
F=Flow(s)
P(s,[('(سیدنا) نبی کریم ﷺ نے فرمایا','The (master) Holy Prophet ﷺ said:','(سیدنا) نبي کریم ﷺ وفرمایل:'),
V('اَنَا خَاتَمُ النَّبِیِّیْنَ لَا نَبِیَّ بَعْدِیْ (سنن ترمذی: کتاب الفتن)','“I am the Seal of the Prophets; there is no prophet after me.” (Sunan al-Tirmidhi: Kitab al-Fitan)','“زه د انبیاوو خاتم یم، زما وروسته هېڅ نبي نشته.” (سنن ترمذي: کتاب الفتن)'),
('“میں آخری نبی ہوں، میرے بعد کوئی نبی نہیں”۔','“I am the last prophet; there is no prophet after me.”','“زه وروستی نبي یم، زما وروسته هېڅ نبي نشته”.'),
('(سیدنا) نبی کریم ﷺ نے فرمایا','The (master) Holy Prophet ﷺ said:','(سیدنا) نبي کریم ﷺ وفرمایل:'),
('کسی نے ہرگز کوئی کھانا اپنے ہاتھ کی کمائی سے بہتر نہیں کھایا ہے۔ اللہ تعالیٰ کے نبی داؤد علیہ السلام اپنے ہاتھ کی کمائی کھایا کرتے تھے۔ (صحیح بخاری)','No one has ever eaten a food better than [what comes from] the earning of his own hand. Allah’s prophet Dawud (peace be upon him) used to eat from the earning of his own hand. (Sahih al-Bukhari)','هېچا هېڅکله د خپل لاس د کمایي نه ښه خواړه نه دي خوړلي. د الله نبي داود علیه السلام د خپل لاس کمایي خوړله. (صحیح بخاري)')])
F.done()
s['sourceNote']='A final page with no printed number and no "Not for Sale" line: two decorative boxes — the first with the Arabic saying “اَنَا خَاتَمُ النَّبِیِّیْنَ لَا نَبِیَّ بَعْدِیْ” and its Urdu translation (Sunan al-Tirmidhi, Kitab al-Fitan), the second with an Urdu saying about eating from one’s own earnings (Sahih al-Bukhari). It is the last scan of the book. The left edges of the boxes are clipped by the photograph.'+NOTE
s['vocabulary']={}
save(s)
