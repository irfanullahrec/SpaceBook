"""Islamiat (Ikhtiari) XII PDF46: pp.82–83 — exercise Q3 matching + activities; Al-Baqarah 277. Run: python class12_iski_page046.py"""
from class12_iski_common import BOOK, Builder, rec, P, L, V

A = ['اَلرِّبٰوا', 'اَنْفِقُوْا', 'طَيِّبٰتِ', 'يَاْمُرُكُمْ', 'اَلْحِكْمَةَ', 'يَحْزَنُوْنَ', 'اَنْصَارٍ', 'خَبِيْرٌ', 'لَا يَسْتَطِيْعُوْنَ', 'اَغْنِيَآءُ', 'سِرًّا']
B = [('He commands you', 'وہ تمہیں حکم دیتا ہے', 'هغه تاسو ته حکم کوي'), ('Helper', 'مددگار', 'مرستندوی'), ('Wealthy people', 'مال دار لوگ', 'شتمن خلک'),
     ('Pure things', 'پاکیزہ چیزیں', 'پاک شیان'), ('They have no strength', 'وہ طاقت نہیں رکھتے', 'هغوی توان نه لري'), ('You spend', 'آپ خرچ کریں', 'تاسو ولګوئ'),
     ('Secret, hidden', 'خفیہ، پوشیدہ', 'پټ، پوشیده'), ('They will be grieved', 'وہ غمگین ہونگے', 'هغوی به غمجن شي'), ('Wisdom', 'دانائی', 'حکمت'),
     ('Interest', 'سود', 'سود'), ('All-Aware (knowing)', 'جاننے والا', 'خبر، پوهېدونکی')]


def p46():
    b = Builder()
    b.p('Question 3: Match the Arabic words of column A with their meanings in column B.', 'سوال 3: کالم الف کے عربی الفاظ کو کالم ب میں ان کے معانی سے ملائیں۔', 'پوښتنه ۳: د الف ستون عربي ټکي د ب ستون له معناوو سره سمون کړئ.')
    b.table('iski12-match-1', ['Column A', 'Column B'], [[a, x[0]] for a, x in zip(A, B)], ['کالم الف', 'کالم ب'], ['الف ستون', 'ب ستون'],
            [[a, x[1]] for a, x in zip(A, B)], [[a, x[2]] for a, x in zip(A, B)])
    b.h('Activities', 'سرگرمیاں', 'فعالیتونه')
    L(b, [('i. Find three such verses from the Holy Quran in which spending in the way of Allah is mentioned.', 'i۔ قرآنِ مجید میں سے تین ایسی آیات تلاش کریں، جن میں انفاق فی سبیل اللہ کا ذکر ہو۔', 'i. له قرآن مجید څخه داسې درې آیتونه ومومئ چې په کې د انفاق فی سبیل الله یادونه وي.'),
          ('ii. Find and write any one such verse from the Holy Quran in which further commands about interest are mentioned.', 'ii۔ قرآنِ پاک میں سے کوئی ایک آیت ایسی تلاش کر کے لکھیں جس میں سود کے بارے میں مزید احکامات کا ذکر ہو۔', 'ii. له قرآن پاک څخه یو داسې آیت ومومئ او ویې لیکئ چې په کې د سود په اړه نور احکام یاد شوي وي.')])
    r1 = rec(b, 1, 82, 46, [82], kind='exercise')
    t = Builder()
    V(t, ('Verse no. 277', 'آیت نمبر: 277', 'آیت نمبر: ۲۷۷'),
      'اِنَّ الَّذِيْنَ اٰمَنُوْا وَعَمِلُوا الصّٰلِحٰتِ وَاَقَامُوا الصَّلٰوةَ وَاٰتَوُا الزَّكٰوةَ لَهُمْ اَجْرُهُمْ عِنْدَ رَبِّهِمْ ۚ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُوْنَ', '',
      ('Those people who believed and did good deeds, and kept offering prayer and giving zakat — they will receive the reward of their deeds with Allah, and on the Day of Judgement they will have no fear at all, nor will they be grieved.', 'جو لوگ ایمان لائے اور نیک عمل کرتے اور نماز پڑھتے اور زکوٰۃ دیتے رہے ان کو ان کے کاموں کا صلہ اللہ کے ہاں ملے گا اور قیامت کے دن ان کو نہ کچھ خوف ہوگا اور نہ وہ غمناک ہوں گے۔', 'کومو خلکو چې ایمان راوړ، نېک عملونه یې وکړل، لمونځ یې کاوه او زکات یې ورکاوه، د خپلو کارونو بدله به له الله سره ومومي، او د قیامت په ورځ به نه څه وېره ولري او نه به غمجن وي.'),
      [('In this blessed verse Allah the Exalted has mentioned those qualities of the believers by virtue of which Allah the Exalted will grant them the best reward. They will be given a place in Jannat al-Firdaws, and on the Day of Judgement they will have no dread of any kind, nor will they be afflicted with fear of any kind. Those qualities of the believers are as follows.', 'اس آیتِ مبارکہ میں اللہ تعالیٰ نے مومنوں کے ان اوصاف کا ذکر کیا ہے جن کی بدولت انہیں اللہ تعالیٰ بہترین اجر عطا فرمائے گا۔ انہیں جنت الفردوس میں جگہ دی جائے گی اور روزِ قیامت نہ انہیں کسی قسم کا ڈر ہوگا اور نہ ہی وہ کسی قسم کے خوف میں مبتلا ہوں گے۔ مومنوں کے وہ اوصاف درج ذیل ہیں۔', 'په دې مبارک آیت کې الله تعالی د مؤمنانو د هغو صفتونو یادونه کړې چې د هغو په برکت به الله تعالی هغوی ته غوره اجر ورکړي. هغوی ته به په جنت الفردوس کې ځای ورکړل شي، او د قیامت په ورځ به نه هېڅ ډول ډار ولري او نه به په هېڅ ډول وېره اخته وي. د مؤمنانو هغه صفتونه دا دي:')])
    L(t, [('a. They do good deeds.', 'ا۔ نیک کام کرتے ہیں۔', 'الف. نېک کارونه کوي.'),
          ('b. They establish prayer.', 'ب۔ نماز قائم کرتے ہیں۔', 'ب. لمونځ قائموي.'),
          ('c. They pay zakat.', 'ج۔ زکوٰۃ ادا کرتے ہیں۔', 'ج. زکات ورکوي.')])
    P(t, [('As we know, after the articles of faith the second rank is that of acts of worship, and after acts of worship the third rank is that of dealings. The true believers are those who believe in Allah and His Messenger ﷺ, offer prayer, and pay zakat out of the wealth that Allah has granted them. [… text hidden by a folded corner …] has been mentioned again and again in the Holy Quran. In fact these acts of worship are the best [way] of expressing faith [… hidden …]. The third sign has been stated to be that they do good deeds. The scope of good deeds [is very wide] …', 'جیسا کہ ہم جانتے ہیں کہ ایمانیات کے بعد دوسرا درجہ عبادات کا ہے اور عبادات کے بعد تیسرا درجہ معاملات کا ہے۔ اصل ایمان والے وہ ہوتے ہیں جو اللہ اور اس کے رسول صلی اللہ علیہ وآلہٖ وسلم پر ایمان لا[تے ہیں]، نماز ادا کرتے ہیں اور جو مال انہیں اللہ نے عطا کیا ہے اس میں سے زکوٰۃ ادا کرتے ہیں۔ [… مڑے ہوئے کونے کے نیچے متن چھپا ہوا …] قرآن مجید میں بار بار ذکر آیا ہے۔ دراصل یہ عبادات ایمان کے اظہار کا بہترین ط[ریقہ] [… چھپا ہوا …] تیسری نشانی یہ بتائی گئی ہے کہ وہ نیک عمل کرتے ہیں۔ نیک اعمال کا دائرہ کار ب[ہت وسیع ہے] …', 'لکه څنګه چې پوهېږو، له ایمانیاتو وروسته دویمه درجه د عباداتو ده، او له عباداتو وروسته درېیمه درجه د معاملاتو ده. اصلي ایمانوال هغه دي چې پر الله او د هغه پر رسول ﷺ ایمان راوړي، لمونځ ادا کوي، او له هغه مال چې الله ورکړی زکات ورکوي. [… متن د ماتې شوې ګوټ لاندې پټ دی …] په قرآن مجید کې بیا بیا یاد شوی. په اصل کې دا عبادات د ایمان د څرګندولو غوره [طریقه] ده [… پټ …]. درېیمه نښه دا ښوول شوې چې نېک عملونه کوي. د نېکو عملونو ساحه [ډېره پراخه ده] …')])
    BOOK.save(46, [(1, r1), (1, rec(t, 1, 83, 46, [83]))], issues=[{'id': 'iski12-pdf046', 'unit': 1, 'printedPage': 82,
               'description': 'p.82 matching table: column B is printed in jumbled order (exercise), kept as printed; no key printed. p.83: the bottom-left corner of the page is folded over in the scan, hiding the ends of the last four lines; hidden text marked and clipped words supplied in [brackets]. Student handwriting on p.83 excluded.'}])


if __name__ == '__main__':
    p46()
