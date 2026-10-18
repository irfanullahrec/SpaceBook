"""Mutalia-e-Quran XII PDF98: p.95 — Lesson 9 exercise Q2 item 7, Q3, activities, teachers' guidance. Run: python class12_quran_page098.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p98():
    b = Builder()
    AR(b, f'(7) {words(24, 31, 1, 19)}', 'What guidance has been given to believing women in the verse?', 'آیت کریمہ میں مومن عورتوں کو کیا ہدایات دی گئیں؟', 'په آیت کې مؤمنو ښځو ته کومې لارښوونې شوې؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(24, 3)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Nur.', 'سُوْرَةُ النُّوْرِ کا تعارف تحریر کریں۔', 'د سورة النور پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(24, 26)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Nur.', 'سُوْرَةُ النُّوْرِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة النور ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(24, 27)}', *TR)
    AR(b, f'(3b) {words(24, 23)}', 'For which people has curse in this world and the Hereafter and a great punishment been mentioned in the verse?', 'آیت کریمہ میں کن لوگوں کے لیے دنیا و آخرت میں لعنت اور عذابِ عظیم کا ذکر ہے؟', 'په آیت کې د کومو خلکو لپاره په دنیا او آخرت کې د لعنت او لوی عذاب یادونه شوې؟')
    b.h(*ACT)
    L(b, [('Draw out the important points from the etiquette that has been stated in Surah al-Nur for entering the houses of others.', 'سُوْرَةُ النُّوْرِ میں دوسروں کے گھروں میں داخل ہونے کے جو آداب بیان کیے گئے ہیں اس سے اہم نکات اخذ کریں۔', 'په سورة النور کې د نورو کورونو ته د ننوتلو کوم اداب چې بیان شوي، له هغو مهم ټکي راوباسئ.'),
          ('Arrange a list of the persons before whom believing women have been given exemption from observing purdah in Surah al-Nur.', 'سُوْرَةُ النُّوْرِ میں مومن خواتین کو جن افراد سے پردہ کرنے سے رخصت دی گئی ہے اس کی فہرست مرتب کریں۔', 'په سورة النور کې مؤمنو ښځو ته چې له کومو کسانو د پردې کولو رخصت ورکړل شوی، د هغو لړلیک ترتیب کړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the detailed background of the incident of ifk, the virtues of Sayyidah \'A\'ishah Siddiqah (may Allah be pleased with her), and the important lessons gained from this incident.', 'اساتذہ طلبہ کو واقعۂ اِفک کا تفصیلی پس منظر، سیدہ عائشہ صدیقہ رضی اللہ عنہا کے فضائل اور اس واقعہ سے حاصل ہونے والے اہم اسباق سے آگاہ کریں۔', 'استادان دې زده‌کوونکي د اِفک د پېښې له مفصل شالید، د سیدې عائشې صدیقې رضي الله عنها له فضیلتونو او له دې پېښې څخه له ترلاسه شویو مهمو زده‌کړو خبر کړي.'),
          ('Make the students aware of the meaning of li\'an and the background of the revelation of this command.', 'طلبہ کو لعان کا معنی، اس حکم کے نازل ہونے کا پس منظر سے آگاہ کریں۔', 'زده‌کوونکي د لعان له مانا او د دې حکم د نازلېدو له شالید خبر کړئ.'),
          ('In this surah Allah Almighty has given a stern warning against spreading indecency. Make the students aware of the virtues of adopting modesty and chastity.', 'اس سورت میں اللہ تعالیٰ نے فحاشی پھیلانے پر سخت وعید بیان فرمائی ہے۔ طلبہ کو حیا اور پاک دامنی اختیار کرنے کے فضائل سے آگاہ کریں۔', 'په دې سورت کې الله تعالی د فحاشۍ په خپرولو سخت ګواښ بیان کړی؛ زده‌کوونکي د حیا او پاکلمنۍ د غوره کولو له فضیلتونو خبر کړئ.')])
    BOOK.save(98, [(9, rec(b, 9, 98, 98, kind='exercise'))], complete_units=[9], issues=[{'id': 'mq12-pdf098', 'unit': 9, 'printedPage': 95,
               'description': 'Lower part of p.95 blank. Teacher line "لعان کا معنی، اس حکم ... کا پس منظر سے" printed with a grammatical slip (kept). Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p98()
