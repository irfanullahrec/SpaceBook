"""Mutalia-e-Quran XII PDF116: p.113 — Lesson 11 exercise Q2 items 5–7, Q3, activities, teachers' guidance. Run: python class12_quran_page116.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p116():
    b = Builder()
    AR(b, f'(5) {words(33, 22)}', 'According to the verse, what conduct did the believers adopt on seeing the armies of the disbelievers?', 'آیت کریمہ کے مطابق کفار کے لشکروں کو دیکھ کر مومنین نے کیا طرزِ عمل اختیار کیا؟', 'د آیت له مخې مؤمنانو د کافرانو لښکرې ولیدې نو کوم چلند یې غوره کړ؟')
    AR(b, f'(6) {words(33, 31)}', 'In the verse, what glad tidings have been given to the Mothers of the Believers (may Allah be pleased with them) for obeying Allah Almighty and His Messenger (peace and blessings of Allah be upon him)?', 'آیت کریمہ میں اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت پر امہات المومنین رضی اللہ تعالیٰ عنہن کو کیا خوش خبریاں دی گئی ہیں؟', 'په آیت کې د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت لپاره امهات المؤمنین رضي الله عنهن ته کوم زېري ورکړل شوي؟')
    AR(b, f'(7) {words(33, 33, 1, 16)}', 'In the verse, what matters have the Mothers of the Believers (may Allah be pleased with them) been instructed in?', 'آیت کریمہ میں امہات المومنین رضی اللہ تعالیٰ عنہن کو کن اُمور کی تلقین کی گئی ہے؟', 'په آیت کې امهات المؤمنین رضي الله عنهن ته د کومو چارو لارښوونه شوې؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(33, 6)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Ahzab.', 'سُوْرَةُ الْأَحْزَابِ کا تعارف تحریر کریں۔', 'د سورة الاحزاب پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(33, 7)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Ahzab.', 'سُوْرَةُ الْأَحْزَابِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الاحزاب ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(33, 9)}', *TR)
    AR(b, f'(3b) {words(33, 21)}', 'What teaching has been given in the verse to the people of faith concerning the Messenger of Allah (peace and blessings of Allah be upon him)?', 'آیت کریمہ میں اہلِ ایمان کو رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے حوالے سے کیا تعلیم دی گئی ہے؟', 'په آیت کې مؤمنانو ته د رسول الله صلی الله علیه وعلی آله واصحابه وسلم په اړه کومه زده‌کړه ورکړل شوې؟')
    b.h(*ACT)
    L(b, [('Search for blessed hadiths on the virtues and merits of the pure Ahl al-Bayt (may Allah be pleased with them), and learn basic information about them from your teachers.', 'اہلِ بیتِ اطہار رضی اللہ عنہم کے فضائل و مناقب پر احادیثِ مبارکہ تلاش کریں اور ان سے متعلق بنیادی معلومات اساتذہ کرام سے معلوم کریں۔', 'د پاک اهل بیت رضي الله عنهم د فضیلتونو او مناقبو په اړه مبارکې حدیثونه ولټوئ او د هغو په اړه بنسټیز معلومات له ښوونکو زده کړئ.'),
          ('Students: become aware of important points concerning the battle of Ahzab.', 'طلبہ کو غزوۂ احزاب کے متعلق اہم نکات سے آگاہ کریں۔', 'زده‌کوونکي دې د احزابو د غزا په اړه له مهمو ټکو خبر شي.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the virtues and merits of three of the Pure Wives from among the Mothers of the Believers (may Allah be pleased with them).', 'امہات المومنین رضی اللہ تعالیٰ عنہن میں سے تین ازواجِ مطہرات رضی اللہ تعالیٰ عنہن کے فضائل و مناقب سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي له امهات المؤمنین رضي الله عنهن څخه د درېیو پاکو مېرمنو له فضیلتونو او مناقبو خبر کړئ.'),
          ('In Surah al-Ahzab the blessed person of the Holy Prophet (peace and blessings of Allah be upon him) has been declared the "uswah hasanah" (best example) for the Muslims. Introduce the students to the prominent aspects of the pure Sirah and encourage them to mould their lives accordingly.', 'سُوْرَةُ الْأَحْزَابِ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی ذاتِ بابرکات کو مسلمانوں کے لیے "اسوۂ حسنہ" (بہترین نمونہ) قرار دیا گیا ہے۔ طلبہ کو سیرتِ طیبہ کے نمایاں پہلو روشناس کرائیں اور ان کے مطابق اپنی زندگی کو ڈھالنے کی ترغیب دیں۔', 'په سورة الاحزاب کې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم برکتناکه ذات مسلمانانو ته "اسوه حسنه" (غوره بېلګه) ګرځول شوې؛ زده‌کوونکي د پاکې سیرت له څرګندو اړخونو اشنا کړئ او هغوی وهڅوئ چې خپل ژوند ورسره سم جوړ کړي.')])
    BOOK.save(116, [(11, rec(b, 11, 116, 116, kind='exercise'))], complete_units=[11], issues=[{'id': 'mq12-pdf116', 'unit': 11, 'printedPage': 113,
               'description': 'The second student activity is printed "طلبہ کو ... سے آگاہ کریں" as if addressed to teachers (kept). Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p116()
