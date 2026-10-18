"""Islamic History XII PDF64 slot: the scan order is swapped — PDF65 shows pp.120–121 and PDF64 shows pp.122–123.
This slot stores pp.120–121 (cited as PDF65) so the reader follows printed order; page065.py stores pp.122–123 (cited as PDF64).
p.120 — (B) provincial system, judiciary; p.121 — judiciary (end), intelligence, (C) military system (start). Run: python class12_ihist_page064.py"""
from class12_ihist_common import BOOK, Builder, rec, S, L


def p64():
    b = Builder()
    b.h('(B) The provincial system', '(ب) صوبائی نظام', '(ب) ولایتي نظام')
    S(b, [(None, ('The caliphs of the Banu Abbas, for administrative convenience, divided the sultanate into many provinces. Considerable changes were made in the provinces of the era of the Banu Umayyah. The head of a province was called amir, wali or \'amil. The caliph himself appointed the amirs. In the beginning the amirs were transferred quickly, but later the amirs kept becoming permanent; rather, declaring their autonomy, they would obtain its deed from the caliph.', 'بنو عباس کے خلفاء نے انتظامی سہولت کے لئے سلطنت کو کئی صوبوں میں تقسیم کیا۔ بنو امیہ کے دور کے صوبوں میں کافی تبدیلیاں کی گئیں۔ صوبے کے سربراہ کو امیر، والی یا عامل کہا جاتا تھا۔ امیروں کا تقرر خلیفہ خود کرتا تھا۔ شروع میں امیروں کو جلدی جلدی تبدیل کیا جاتا تھا۔ لیکن بعد میں امیر مستقل ہوتے گئے۔ بلکہ اپنی خود مختاری کا اعلان کر کے خلیفہ سے اس کی سند حاصل کر لیتے۔', 'د بنو عباس خلفاوو د اداري اسانتیا لپاره سلطنت په ډېرو ولایتونو ووېشه؛ د بنو امیه د دورې په ولایتونو کې ډېر بدلونونه راغلل. د ولایت مشر ته امیر، والي یا عامل ویل کېده؛ امیران به پخپله خلیفه ټاکل. په پیل کې امیران ژر ژر بدلېدل، خو وروسته امیران دایمي شول؛ بلکې د خپلې خپلواکۍ له اعلان وروسته به یې له خلیفه سند ترلاسه کاوه.')),
          (None, ('The amir himself appointed the provincial officials. In the era of the Banu Abbas\'s government there were approximately twenty-four provinces, among which the large provinces were as follows.', 'صوبائی حکام کا تقرر امیر خود کرتا تھا۔ بنو عباس کے دورِ حکومت میں تقریباً چوبیس صوبے تھے۔ جن میں بڑے بڑے صوبے مندرجہ ذیل تھے۔', 'ولایتي چارواکي امیر پخپله ټاکل. د بنو عباس د حکومت په دوره کې نږدې څلېرویشت ولایتونه وو چې لوی لوی یې دا لاندې وو.'))])
    L(b, [('1. Egypt', '۱۔ مصر', '۱. مصر'),
          ('2. North Africa', '۲۔ شمالی افریقہ', '۲. شمالي افریقا'),
          ('3. al-Jazirah, Azerbaijan and Armenia', '۳۔ جزیرہ آذربائیجان اور آرمینیا', '۳. جزیره، اذربایجان او ارمنیا'),
          ('4. Hijaz (Makkah, Madinah and Central Arabia)', '۴۔ حجاز (مکہ، مدینہ اور وسطی عرب)', '۴. حجاز (مکه، مدینه او منځنی عرب)'),
          ('5. Yemen, Kufa, Sawad', '۵۔ یمن، کوفہ، سواد', '۵. یمن، کوفه، سواد'),
          ('6. Basra, Bahrain and northern Iraq', '۶۔ بصرہ، بحرین اور شمالی عراق', '۶. بصره، بحرین او شمالي عراق'),
          ('7. Fars, Khurasan', '۷۔ فارس، خراسان', '۷. فارس، خراسان'),
          ('8. Mawara\' al-Nahr', '۸۔ ماوراء النہر', '۸. ماوراءالنهر'),
          ('9. Ahwaz', '۹۔ اہواز', '۹. اهواز'),
          ('10. Sindh, Punjab', '۱۰۔ سندھ، پنجاب', '۱۰. سند، پنجاب'),
          ('11. Syria', '۱۱۔ شام', '۱۱. شام'),
          ('12. Southern Iran and Mosul', '۱۲۔ جنوبی ایران اور موصل', '۱۲. سوېلي ایران او موصل')])
    S(b, [(('Department of justice:', 'محکمہ انصاف:', 'د عدلیې محکمه'),
           ('Every town had its own deputy qadi. In the large cities there were qadis. In the beginning the provincial amirs appointed them, but later the Qadi al-Qudat of Baghdad appointed them directly. In matters of justice no concession of any kind was given. With all …', 'ہر قصبے کا اپنا نائب قاضی ہوتا تھا۔ بڑے شہروں میں قاضی ہوتے تھے۔ شروع میں صوبائی امیر ان کا تقرر کرتا تھا۔ لیکن بعد میں بغداد کا قاضی القضاۃ براہِ راست ان کا تقرر کرتا۔ انصاف کے سلسلے میں کسی قسم کی رعایت نہیں دی جاتی تھی۔ سب کے ساتھ', 'هر قصبه خپل نایب قاضي درلود؛ په لویو ښارونو کې قاضیان وو. په پیل کې ولایتي امیر هغوی ټاکل، خو وروسته د بغداد قاضي القضات په مستقیم ډول ټاکل. د انصاف په برخه کې هېڅ ډول رعایت نه کېده؛ له ټولو سره …'))])
    r1 = rec(b, 25, 120, 65, [120])
    t = Builder()
    S(t, [(None, ('… equal treatment was given. Deputy qadis were also called \'adil. The decisions of the disputes of non-Muslims were made by their own religious leaders. The biggest court of the country was called Dar al-\'Adl. Its head was the Qadi al-Qudat or the caliph. The hajib and the vizier too performed the duties of judges. All the courts of the country worked under the Qadi al-Qudat.', 'یکساں سلوک کیا جاتا تھا۔ نائب قاضی، عادل بھی کہلاتے تھے۔ غیر مسلموں کے جھگڑوں کے فیصلے ان کے اپنے مذہبی پیشوا کیا کرتے تھے۔ ملک کی سب سے بڑی عدالت دارالعدل کہلاتی تھی۔ اس کا سربراہ قاضی القضاۃ یا خلیفہ ہوتا تھا۔ حاجب اور وزیر بھی ججوں کے فرائض سرانجام دیتے تھے۔ ملک کی تمام عدالتیں قاضی القضاۃ کے ماتحت کام کرتی تھیں۔', '… یو شان چلند کېده. نایب قاضیانو ته «عادل» هم ویل کېده. د غیر مسلمانانو د شخړو پرېکړې د هغوی خپلو مذهبي مشرانو کولې. د هېواد تر ټولو لویه محکمه «دارالعدل» بلل کېده؛ مشر یې قاضي القضات یا خلیفه و؛ حاجب او وزیر هم د قاضیانو دندې سرته رسولې؛ د هېواد ټولې محکمې د قاضي القضات تر لاس لاندې کار کاوه.')),
          (('Department of intelligence:', 'محکمہ جاسوسی:', 'د استخباراتو محکمه'),
           ('In the era of the Banu Abbas the department of intelligence was better organised. Government spies were spread in every corner of the country in the guise of merchants and preachers. They kept the caliph informed of all important events.', 'بنو عباس کے دور میں محکمہ جاسوسی بہتر طور پر منظم کیا گیا۔ سرکاری جاسوس سوداگروں اور واعظوں کے بھیسوں میں ملک کے کونے کونے میں پھیلے ہوئے تھے۔ وہ خلیفہ کو تمام اہم واقعات سے باخبر رکھتے تھے۔', 'د بنو عباس په دوره کې د استخباراتو محکمه ښه منظمه شوه؛ دولتي جاسوسان د سوداګرو او واعظانو په بڼه د هېواد په هر ګوټ کې خپاره وو؛ خلیفه یې له ټولو مهمو پېښو خبر ساته.'))])
    t.h('(C) The military system', '(ج) فوجی نظام', '(ج) پوځي نظام')
    S(t, [(None, ('The army of the Banu Abbas was counted among the best armies of the world. The army of the Banu Umayyah consisted only of Arabs. In the era of the Banu Abbas there were different divisions of the army. All the people of the realm could be recruited in them. Equal treatment was given to all people. In salaries too there was no difference of any kind. In Mansur\'s era there were three large divisions of the army.', 'بنو عباس کی فوج کا شمار دنیا کی بہترین فوجوں میں ہوتا تھا۔ بنو امیہ کی فوج صرف عربوں پر مشتمل تھی۔ بنو عباس کے دور میں فوج کے مختلف حصے تھے۔ ان میں مملکت کے تمام لوگ بھرتی ہو سکتے تھے۔ تمام لوگوں کے ساتھ مساوی سلوک کیا جاتا تھا۔ تنخواہوں میں بھی کسی قسم کا فرق نہیں تھا۔ منصور کے دور میں فوج کے تین بڑے حصے یا ڈویژن تھے۔', 'د بنو عباس پوځ د نړۍ په غوره پوځونو کې شمېرل کېده. د بنو امیه پوځ یوازې له عربو جوړ و. د بنو عباس په دوره کې د پوځ بېلابېلې برخې وې؛ د هېواد ټول خلک پکې ګمارل کېدای شول؛ له ټولو خلکو سره برابر چلند کېده؛ په معاشونو کې هم هېڅ توپیر نه و. د منصور په دوره کې د پوځ درې لویې برخې یا ډیویژنونه وو.'))])
    L(t, [('1. North Arab division (Mudari)', '۱۔ شمالی عرب حصہ (مضری)', '۱. شمالي عرب برخه (مضري)'),
          ('2. South Arab division (Yamani)', '۲۔ جنوبی عرب حصہ (یمنی)', '۲. سوېلي عرب برخه (یمني)'),
          ('3. Khurasani division. In Mu\'tasim\'s era further divisions were added to the army:', '۳۔ خراسانی حصہ معتصم کے دور میں فوج میں مزید حصوں کا اضافہ کیا گیا۔', '۳. خراساني برخه. د معتصم په دوره کې پوځ ته نورې برخې ورزیاتې شوې:'),
          ('4. Turkish division', '۴۔ ترک حصہ', '۴. ترکي برخه'),
          ('5. African division', '۵۔ افریقی حصہ۔', '۵. افریقايي برخه')])
    BOOK.save(64, [(25, r1), (25, rec(t, 25, 121, 65, [121]))], issues=[{'id': 'ihist12-pdf064', 'unit': 25, 'printedPage': 120,
               'description': 'Scan order swapped: PDF64 shows pp.122–123 and PDF65 shows pp.120–121. To keep printed order in the reader, this PDF64 slot stores pp.120–121 (records cite PDF65) and the PDF65 slot stores pp.122–123 (records cite PDF64). Printed list item 3 runs straight into the sentence about Mu\'tasim\'s additions — kept. Student mark "④" excluded.'}])


if __name__ == '__main__':
    p64()
