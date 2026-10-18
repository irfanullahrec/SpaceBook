"""Pak Studies XII PDF112 (spread): right page re-scans p.209 (duplicate of PDF111); p.210 — Ch.11 cutting of forests."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
t.h('Cutting of forests:', 'جنگلات کا کٹاؤ:', 'د ځنګلونو پرې کول:')
t.p('Forests are very important for any country. Through them the climate and the environment are improved, and the level of pollution decreases. To remedy the effects of poisonous and harmful gases, more oxygen is needed, which can be obtained from trees. But in Pakistan there is a severe shortage of forests, and the area of our forests (of the total area of the country) is only 4.8 per cent, whereas according to the world standard it should be 25 per cent. The tragedy is that the present area too is decreasing further because of the reckless cutting of forests.',
    'جنگلات کسی بھی ملک کے لیے بہت اہم ہوتے ہیں۔ ان سے آب و ہوا اور ماحول کی اصلاح ہوتی ہے، آلودگی کی سطح کم ہوتی ہے۔ زہریلی اور ضرر رساں گیسوں کے اثرات کے تدارک کے لیے زیادہ آکسیجن کی ضرورت ہے جو درختوں سے میسر ہو سکتی ہے، لیکن پاکستان میں جنگلات کی شدید کمی ہے اور ہمارے جنگلات کا رقبہ (ملک کے مجموعی رقبے کا) صرف 4.8 فی صد ہے جب کہ عالمی معیار کے مطابق اسے 25 فی صد ہونا چاہیے۔ المیہ یہ ہے کہ موجودہ رقبہ بھی جنگلات کی بے دریغ کٹائی کے باعث مزید کم ہوتا جا رہا ہے۔',
    'ځنګلونه د هر هېواد لپاره ډېر مهم وي. له دوی سره اقلیم او چاپېریال ښه کېږي او د ککړتیا کچه کمېږي. د زهرجنو او زیانمنو ګازونو د اغېزو د مخنیوي لپاره ډېر اکسیجن اړین دی، چې له ونو ترلاسه کېدای شي. خو په پاکستان کې د ځنګلونو سخت کمښت دی، او زموږ د ځنګلونو ساحه (د هېواد د ټولې ساحې) یوازې ۴.۸ سلنه ده، په داسې حال کې چې د نړیوال معیار له مخې باید ۲۵ سلنه وي. غمیزه دا ده چې اوسنۍ ساحه هم د ځنګلونو د بې‌پروا پرې کولو له امله لا کمېږي.')
rec = BOOK.record(t, 'pak12-ch11-text-7', 'Chapter 11 text (7)', 'بابِ یازدہم — متن (۷)', 'یوولسم څپرکی — متن (۷)', 112, [210])
rec['sourceNote'] = 'The right page of this spread is a second scan of p.209 (already transcribed from PDF111) and is not repeated. The rest of p.210 is blank in print.'
issues = [{'id': 'pak12-pdf112', 'unit': 11, 'printedPage': 209,
           'description': 'PDF112’s right page duplicates p.209 (also in PDF111); only p.210 is transcribed. p.210 gives forest cover as 4.8% and the world standard as 25% (p.166 said “at least one-fourth”); retained as printed.'}]

if __name__ == '__main__':
    BOOK.save(112, [(11, rec)], issues=issues)
