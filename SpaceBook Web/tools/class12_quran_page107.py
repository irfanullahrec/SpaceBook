"""Mutalia-e-Quran XII PDF107: p.104 — Lesson 10 exercise Q3 (3), activities, teachers' guidance. Run: python class12_quran_page107.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, TR, ACT, TCH, words


def p107():
    b = Builder()
    AR(b, f'(3a) {words(24, 47)}', *TR)
    AR(b, f'(3b) {words(24, 60)}', 'What concession has been stated in the verse for elderly women who stay at home?', 'آیت کریمہ میں خانہ نشین بوڑھی عورتوں کے لیے کیا رخصت بیان کی گئی ہے؟', 'په آیت کې د کورناستو زړو ښځو لپاره کوم رخصت بیان شوی؟')
    b.h(*ACT)
    L(b, [('Draw out important points from the detail given at various places in Surah al-Nur of the conduct of the hypocrites and the sincere believers.', 'سُوْرَةُ النُّوْرِ میں متعدد مقامات پر منافقین اور مخلص مومنین کے طرزِ عمل کی جو تفصیل بیان کی گئی ہے اس سے اہم نکات اخذ کریں۔', 'په سورة النور کې په ګڼو ځایونو کې د منافقانو او مخلصو مؤمنانو د چلند کومه تفصیل چې بیان شوی، له هغه مهم ټکي راوباسئ.'),
          ('In verse 61 of Surah al-Nur, arrange a list of the houses from which people with excuse have been given permission to eat food.', 'سُوْرَةُ النُّوْرِ کی آیت: ۶۱ میں معذور لوگوں کو جن گھروں سے کھانا کھانے کی رخصت دی گئی ہے ان کی فہرست مرتب کریں۔', 'د سورة النور په ۶۱ آیت کې معذورو خلکو ته د کومو کورونو څخه د خوړو د خوړلو رخصت ورکړل شوی، د هغو لړلیک ترتیب کړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware, with explanation, of the parable of the light of Allah Almighty given in Surah al-Nur.', 'سُوْرَةُ النُّوْرِ میں اللہ تعالیٰ کے نور کی جو مثال بیان کی گئی ہے اس کی وضاحت سے طلبہ کو آگاہ کریں۔', 'په سورة النور کې د الله تعالی د نور کوم مثال چې بیان شوی، زده‌کوونکي یې په وضاحت خبر کړئ.'),
          ('Explain to the students with clarity the parable given in Surah al-Nur for the disbelievers and the hypocrites.', 'سُوْرَةُ النُّوْرِ میں کفار اور منافقین کے لیے بیان کی گئی مثال طلبہ کو وضاحت کے ساتھ سمجھائیں۔', 'په سورة النور کې د کافرانو او منافقانو لپاره بیان شوی مثال زده‌کوونکو ته په وضاحت سره وپوهوئ.'),
          ('In Surah al-Nur Allah Almighty has mentioned creating every living creature from water. Encourage the students towards the importance and conservation of water.', 'سُوْرَةُ النُّوْرِ میں اللہ تعالیٰ نے پانی سے ہر جاندار کو پیدا کرنے کا ذکر کیا ہے۔ طلبہ کو پانی کی اہمیت اور حفاظت کی ترغیب دیں۔', 'په سورة النور کې الله تعالی له اوبو د هر ژوندي د پیدا کولو یادونه کړې؛ زده‌کوونکي د اوبو اهمیت او ساتنې ته وهڅوئ.')])
    BOOK.save(107, [(10, rec(b, 10, 107, 107, kind='exercise'))], complete_units=[10], issues=[{'id': 'mq12-pdf107', 'unit': 10, 'printedPage': 104,
               'description': 'Lower half of p.104 blank. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p107()
