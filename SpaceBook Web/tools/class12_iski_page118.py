"""Islamiat (Ikhtiari) XII PDF118: pp.226–227 — Makkah sermon notes and commentary; Farewell Sermon (two extracts). Run: python class12_iski_page118.py"""
from class12_iski_common import BOOK, Builder, rec, P, L, AR


def p118():
    b = Builder()
    L(b, [('[gharartu] I deceived.', '[غَرَرْتُ] میں نے دھوکا دیا۔', '[غررت] ما وغولاوه.'),
          ('[kaffah] All.', '[كَافَّةً] تمام', '[کافة] ټول.'),
          ('[latubʿathunna] You will certainly be raised again after death.', '[لَتُبْعَثُنَّ] تم موت کے بعد دوبارہ ضرور اٹھائے جاؤ گے', '[لتبعثن] له مرګ وروسته به خامخا بیا راپورته کېږئ.'),
          ('[latamutunna] Death will certainly come to you.', '[لَتَمُوْتُنَّ] تمہیں ضرور موت آئے گی', '[لتموتن] خامخا به مړه کېږئ.'),
          ('[latuhasabunna] Your account will certainly be taken.', '[لَتُحَاسَبُنَّ] تمہارا ضرور حساب لیا جائے گا۔', '[لتحاسبن] خامخا به ستاسو حساب اخیستل کېږي.'),
          ('[latujzawunna] You will certainly be given recompense.', '[لَتُجْزَوُنَّ] تمہیں ضرور بدلہ دیا جائے گا۔', '[لتجزون] خامخا به بدله درکول کېږي.'),
          ('[abadan] Forever.', '[اَبَدًا] ہمیشہ', '[ابدا] تل.')])
    b.p('Commentary: In this sermon Huzoor ﷺ made his family aware about the Hereafter. We see these features in this sermon.', 'تبصرہ: اس خطبے میں حضور اقدس صلی اللہ علیہ وآلہٖ وسلم نے اپنے اہل و عیال کو آخرت کے بارے میں آگاہ کیا۔ ہم اس خطبے میں یہ خصوصیات دیکھتے ہیں۔', 'تبصره: په دې خطبه کې حضور اقدس ﷺ خپله کورنۍ د آخرت په اړه خبره کړه. په دې خطبه کې دا ځانګړنې وینو.')
    L(b, [('1. Brevity', '۱۔ اختصار', '۱. لنډوالی'), ('2. Easy words', '۲۔ آسان الفاظ', '۲. اسانه الفاظ'),
          ('3. Simile: death has been likened to sleep and coming alive again to waking.', '۳۔ تشبیہ: موت کو نیند سے اور دوبارہ زندہ ہونے کو جاگنے سے تشبیہ دی ہے۔', '۳. تشبیه: مرګ له خوب او بیا ژوندي کېدل له راویښېدو سره تشبیه شوي.'),
          ('4. Style of emphasis: to stress his point he ﷺ adopted the style of emphasis — you will certainly die, etc.', '۴۔ اسلوبِ تاکید: اپنی بات پر زور دینے کے لیے تاکید کا اسلوب اختیار فرمایا۔ تم ضرور مرو گے۔ وغیرہ۔', '۴. د ټینګار اسلوب: د خپلې خبرې د ټینګار لپاره یې د تاکید اسلوب غوره کړ — تاسو به خامخا مړه کېږئ، او نور.')])
    b.p('He ﷺ established the custom of praise and glorification at the beginning of the sermon.', 'آپ صلی اللہ علیہ وآلہٖ وسلم نے خطبے کے شروع میں حمد و ثنا کا رواج ڈالا۔', 'هغه ﷺ د خطبې په پیل کې د حمد او ثنا دود جوړ کړ.')
    b.h('The Farewell Sermon', 'خطبۂ حجۃ الوداع', 'د حجة الوداع خطبه')
    AR(b, 'يٰٓاَيُّهَا النَّاسُ اِنَّهٗ لَا نَبِيَّ بَعْدِيْ وَلَآ اُمَّةَ بَعْدَكُمْ ۞ اَلَا فَاعْبُدُوْا رَبَّكُمْ ۞ وَصَلُّوْا خَمْسَكُمْ ۞ وَصُوْمُوْا شَهْرَكُمْ وَاَدُّوْا زَكٰوةَ اَمْوَالِكُمْ طَيِّبَةً بِهَا اَنْفُسُكُمْ ۞ وَتَحُجُّوْنَ بَيْتَ رَبِّكُمْ ۞ وَاَطِيْعُوْا وُلَاةَ اَمْرِكُمْ ۞ تَدْخُلُوْا جَنَّةَ رَبِّكُمْ')
    P(b, [('Translation: O people! There is no prophet after me, nor will any Ummah be born after you. Beware! So worship your Lord, and offer your five daily prayers, and keep the fasts of your month (Ramadan), and pay the zakat of your wealth with willing hearts, and perform the Hajj of the House of your Lord, and obey your rulers; you will enter the Paradise of your Lord.', 'ترجمہ: اے لوگو! نہ تو میرے بعد کوئی پیغمبر ہے اور نہ تمہارے بعد کوئی امت پیدا ہونے والی ہے۔ خبردار! پس اپنے پروردگار کی عبادت کرو اور اپنی پنجگانہ نماز ادا کرو، اور روزے رکھو اپنے مہینے (رمضان) کے، اور زکوٰۃ ادا کرو اپنے مالوں کی خوش دلی کے ساتھ، اور حج ادا کرو اپنے رب کے گھر کا، اور اپنے حکام کی اطاعت کرو، اپنے پروردگار کے جنت میں داخل ہو گے۔', 'ژباړه: اې خلکو! نه له ما وروسته کوم پیغمبر شته او نه له تاسو وروسته کوم امت پیدا کېدونکی دی. خبردار! نو د خپل رب عبادت وکړئ، پنځه وخته لمونځ ادا کړئ، د خپلې میاشتې (رمضان) روژې ونیسئ، د خپلو مالونو زکات په خوښ زړه ورکړئ، د خپل رب د کور حج ادا کړئ، او د خپلو واکمنانو اطاعت وکړئ؛ د خپل رب جنت ته به ننوځئ.'),
          ('(Ibn Jarir, Ibn \'Asakir from Abu Umamah)', '(ابن جریر، ابن عساکر عن ابی امامہ)', '(ابن جریر، ابن عساکر له ابو امامه)')])
    b.h('Difficult words and meanings:', 'مشکل الفاظ اور معنی:', 'ستونزمن الفاظ او ماناوې')
    L(b, [('[la nabiyya ba\'di] There will be no prophet after me.', '[لَا نَبِيَّ بَعْدِيْ] میرے بعد کوئی نبی نہیں ہوگا۔', '[لا نبي بعدي] له ما وروسته به هېڅ نبي نه وي.'),
          ('[tadkhulu] You will enter.', '[تَدْخُلُوْا] داخل ہو جاؤ', '[تدخلوا] ننوځئ.'),
          ('[wulat] Plural of wali (rulers).', '[وُلَاة] والی کی جمع (حکام)', '[ولاة] د «والي» جمع (واکمنان).'),
          ('[addu] Pay.', '[اَدُّوْا] ادا کرو', '[ادوا] ادا کړئ.'),
          ('[ala] Beware.', '[اَلَا] خبردار', '[الا] خبردار.'),
          ('[bayt] House.', '[بَيْت] گھر', '[بیت] کور.')])
    r1 = rec(b, 6, 226, 118, [226])
    t = Builder()
    AR(t, 'اُوْصِيْكُمْ عِبَادَ اللّٰهِ بِتَقْوَى اللّٰهِ وَاَحُثُّكُمْ عَلٰى طَاعَتِهٖ ۞ اَيُّهَا النَّاسُ اِنَّ دِمَآءَكُمْ وَاَمْوَالَكُمْ عَلَيْكُمْ حَرَامٌ اِلٰٓى اَنْ تَلْقَوْا رَبَّكُمْ كَحُرْمَةِ يَوْمِكُمْ هٰذَا فِيْ شَهْرِكُمْ هٰذَا فِيْ بَلَدِكُمْ هٰذَا فَمَنْ كَانَتْ عِنْدَهٗ اَمَانَةٌ فَلْيُؤَدِّهَا اِلَى الَّذِي ائْتَمَنَهٗ عَلَيْهَا وَاِنَّ رِبَا الْجَاهِلِيَّةِ مَوْضُوْعٌ وَّاِنَّ اَوَّلَ رِبًا اَبْدَاُ بِهٖ رِبَا عَمِّي الْعَبَّاسِ بْنِ عَبْدِ الْمُطَّلِبِ وَاِنَّ دِمَآءَ الْجَاهِلِيَّةِ مَوْضُوْعَةٌ وَّاِنَّ اَوَّلَ دَمٍ اَبْدَاُ بِهٖ دَمُ عَامِرِ بْنِ رَبِيْعَةَ بْنِ الْحَارِثِ بْنِ عَبْدِ الْمُطَّلِبِ', 'سنن ابی داؤد: ۳۳۳۴')
    t.p('Translation: O servants of Allah! I enjoin upon you the taqwa of Allah, and urge you to His obedience. O people! Indeed your blood and your property, till meeting your Lord, are unlawful in the same way as the sanctity of this day of today in this month of today and this city of today. Whoever has a trust with him, let him return it to the one who entrusted it to him; and indeed the interest of the Ignorance has ended, and I begin with the interest of my uncle Abbas bin Abd al-Muttalib. The blood-claims of the Ignorance have ended, and first of all I begin with the blood of Amir bin Rabi\'ah bin Harith bin Abd al-Muttalib.', 'ترجمہ: اے اللہ کے بندو! میں تمہیں اللہ کے تقویٰ کی وصیت کرتا ہوں اور تمہیں اس کی اطاعت کی ترغیب دیتا ہوں۔ اے لوگو! بے شک تمہارے خون اور تمہارے مال تمہارے رب سے ملاقات تک اسی طرح حرام ہیں جیسے آج کے دن، آج کے مہینے اور آج کے شہر کی حرمت ہے۔ جس کے پاس امانت ہو تو وہ اس کو لوٹا دے جس نے اس کو امانت دی اور بے شک جاہلیت کا سود ختم ہے اور میں اپنے چچا عباس بن عبدالمطلب کے سود سے ابتداء کرتا ہوں۔ جاہلیت کے خون ختم ہیں اور سب سے پہلے میں عامر بن ربیعہ بن حارث بن عبدالمطلب کے خون سے ابتداء کرتا ہوں۔', 'ژباړه: اې د الله بندګانو! زه تاسو ته د الله د تقوا وصیت کوم او د هغه اطاعت ته مو هڅوم. اې خلکو! بې‌شکه ستاسو وینې او ستاسو مالونه تر خپل رب سره تر لیدو پورې همداسې حرام دي لکه د نن ورځې، د نن میاشتې او د نن ښار حرمت. چا سره چې امانت وي، هغه ته دې یې ورکړي چې امانت یې ورسپارلی؛ او بې‌شکه د جاهلیت سود ختم دی، او زه د خپل تره عباس بن عبدالمطلب له سوده پیل کوم. د جاهلیت وینې ختمې دي، او تر ټولو مخکې د عامر بن ربیعه بن حارث بن عبدالمطلب له وینې پیل کوم.')
    t.h('Difficult words and meanings:', 'مشکل الفاظ اور معنی:', 'ستونزمن الفاظ او ماناوې')
    L(t, [('[usikum] I enjoin upon you.', '[اُوْصِيْكُمْ] میں تمہیں وصیت کرتا ہوں۔', '[اوصیکم] تاسو ته وصیت کوم.'),
          ('[talqaw] You meet.', '[تَلْقَوْا] تم ملو', '[تلقوا] ګورئ (سره مخ کېږئ).'),
          ('[ahuththukum] I urge you.', '[اَحُثُّكُمْ] میں تمہیں ترغیب دیتا ہوں۔', '[احثکم] تاسو هڅوم.'),
          ('[shahr] Month.', '[شَهْر] مہینہ', '[شهر] میاشت.'),
          ('[dima\'] Plural of dam: blood.', '[دِمَآء] دم کی جمع خون', '[دماء] د «دم» جمع: وینې.'),
          ('[fal-yu\'addiha] So let him return it.', '[فَلْيُؤَدِّهَا] پس اسے ادا کرے', '[فلیؤدها] نو هغه دې یې ادا کړي.')])
    t.p('Commentary: This extract has been taken from the Farewell Sermon. The following features are found in this sermon.', 'تبصرہ: یہ اقتباس خطبۂ حجۃ الوداع سے لیا گیا ہے۔ اس خطبے میں درج ذیل خصوصیات پائی جاتی ہیں۔', 'تبصره: دا اقتباس د حجة الوداع له خطبې اخیستل شوی. په دې خطبه کې لاندې ځانګړنې موندل کېږي.')
    L(t, [('1. Simplicity of words.', '۱۔ الفاظ کی سادگی۔', '۱. د الفاظو ساده‌والی.'),
          ('2. Simile: the sanctity of human blood and property has been likened to the sanctity of the day of \'Arafah, the month of Dhul-Hijjah and Makkah al-Mu\'azzamah.', '۲۔ تشبیہ: انسانی خون اور مال کی حرمت کو عرفہ کے دن اور ذی الحجہ کے مہینے اور مکہ معظمہ کی حرمت سے تشبیہ دی۔', '۲. تشبیه: د انساني وینې او مال حرمت د عرفې د ورځې، د ذی الحجې د میاشتې او د مکې معظمې له حرمت سره تشبیه شوی.'),
          ('3. By the use of inna emphasis was created in the speech.', '۳۔ اِنَّ کے استعمال سے کلام میں تاکید پیدا کی۔', '۳. د «انّ» په کارولو په کلام کې تاکید پیدا شو.'),
          ('4. Unfamiliar and difficult words were avoided. This is a masterpiece of Arabic language and literature.', '۴۔ نامانوس اور مشکل الفاظ سے اجتناب کیا۔ یہ عربی زبان و ادب کا شاہکار ہے۔', '۴. له نااشنا او ستونزمنو الفاظو ډډه شوې. دا د عربي ژبې او ادب شاهکار دی.'),
          ('5. The statement of the basic belief, that is, the finality of prophethood, and of the duties with brevity and comprehensiveness, which is the best example of the characteristic of him ﷺ, jawami\' al-kalim (comprehensive speech).', '۵۔ اساسی عقیدہ یعنی ختم نبوت اور فرائض کا اختصار اور جامعیت سے بیان جو کہ آپ صلی اللہ علیہ وآلہٖ وسلم کی خصوصیت جوامع الکلم کا بہترین نمونہ ہے۔', '۵. د بنسټیزې عقیدې یعنې ختم نبوت او د فرایضو په لنډوالي او جامعیت سره بیان، چې د هغه ﷺ د «جوامع الکلم» د ځانګړنې غوره بېلګه ده.')])
    BOOK.save(118, [(6, r1), (6, rec(t, 6, 227, 118, [227]))], issues=[{'id': 'iski12-pdf118', 'unit': 6, 'printedPage': 226,
               'description': 'Second Farewell Sermon extract reference printed "(سنن ابی داؤد: ۳۳۳۴)". A neighbouring book cover is visible at the right edge of the p.227 scan — excluded.'}])


if __name__ == '__main__':
    p118()
