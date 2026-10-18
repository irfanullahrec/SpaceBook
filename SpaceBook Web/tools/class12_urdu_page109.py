"""Urdu XII PDF109 (spread): pp.208–209 — Poem 5 'ستارے' (sonnet; N. M. Rashid, d.1975 — public domain from 2026) full text + مشق Q1–Q6 + note."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.h('Stars (a sonnet) — N. M. Rashid', 'ستارے (سانیٹ) — ن۔م۔ راشدؔ', 'ستوري (سانېټ) — ن.م. راشد')
Q = [
 [('Issuing from the paradise-garden of moon and stars, a stream of song', 'نکل کر جُوئے نغمہ خُلد زارِ ماہ و انجم سے', 'د سپوږمۍ او ستورو له جنتي باغ نه د سندرې یوه ویاله راوځي'),
  ('flows slowly, slowly through the expanses of space;', 'فضا کی وسعتوں میں ہے رواں آہستہ آہستہ', 'او د فضا په پراخوالي کې ورو ورو بهېږي؛'),
  ('slowly, slowly towards the lament-filled world', 'بہ سُوئے نوحہ آبادِ جہاں آہستہ آہستہ', 'ورو ورو د وېر‌ډکې نړۍ په لور'),
  ('a garden of melody comes issuing forth!', 'نکل کر آ رہی ہے اک گلستانِ ترنّم سے!', 'د ترنم له یوه ګلستانه راوځي!')],
 [('The stars, with their sweet, intoxicating, gentle smile,', 'ستارے اپنے میٹھے مدبھرے ہلکے تبسّم سے', 'ستوري په خپلې خوږې، مستې، سپکې موسکا'),
  ('keep making Nature young, slowly, slowly;', 'کیے جاتے ہیں فطرت کو جواں آہستہ آہستہ', 'طبیعت ورو ورو ځوانوي؛'),
  ('they tell her a tale, slowly, slowly;', 'سُناتے ہیں اسے اک داستاں آہستہ آہستہ', 'ورو ورو ورته یوه کیسه اوروي؛'),
  ('the land of life is entranced by their speech!', 'دیارِ زندگی مدہوش ہے اُن کے تکلّم سے!', 'د ژوند ملک د هغوی په خبرو بې‌خوده دی!')],
 [('This has been the habit of these stars since the first day:', 'یہی عادت ہے روزِ اوّلیں سے ان ستاروں کی', 'له لومړۍ ورځې د دې ستورو همدا عادت دی:'),
  ('they shine so that joy may rule in the world;', 'چمکتے ہیں کہ دُنیا میں مسرّت کی حکومت ہو', 'ځلېږي چې په نړۍ کې د خوښۍ واکمني وي؛'),
  ('they shine so that man may forget the cares of existence.', 'چمکتے ہیں کہ انساں فکرِ ہستی کو بُھلا ڈالے', 'ځلېږي چې انسان د هستۍ اندېښنه هېره کړي.')],
 [('Every ray of these pieces of light carries this longing:', 'لیے ہے یہ تمنا ہر کرن ان نور پاروں کی', 'د دې رڼا ټوټو هره وړانګه دا ارمان لري:'),
  ('that some day this earthly world may be a cradle of beauty and grace,', 'کبھی یہ خاک داں گہوارۂ حسن و لطافت ہو', 'چې یوه ورځ دا خاورین کور د ښکلا او لطافت زانګو شي،'),
  ('that some day man may find again his lost paradise!', 'کبھی انسان اپنی گُم شدہ جنّت کو پھر پا لے!', 'چې یوه ورځ انسان خپل ورک شوی جنت بیا ومومي!')],
]
for i, q in enumerate(Q, 1):
    t.p(f'Stanza {i}', f'بند {"۰۱۲۳۴"[i]}', f'بند {i}')
    t.group('lines', q)
t.p('(Kulliyat-e-Rashid, Lahore, Mavra Publishers, 2nd edition 1991)', '(کلیاتِ راشدؔ، لاہور، ماورا پبلشرز بار دوم ۱۹۹۱ء)', '(کلیات راشد، لاهور، ماورا خپرندویه، دویم چاپ ۱۹۹۱ز)')
po = BOOK.record(t, 'urdu12-u22-poem', 'Poem text (sonnet)', 'متنِ نظم (سانیٹ)', 'د نظم متن (سانېټ)', 109, [208, 209])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write a summary of this poem.', '۱۔ اس نظم کا خلاصہ لکھیں۔', '۱. د دې نظم لنډیز ولیکئ.'),
    ('2. Describe in your own words the scene of stars twinkling in the sky at night.', '۲۔ رات کے وقت آسمان پر جگمگاتے ستاروں کا منظر اپنے الفاظ میں بیان کریں۔', '۲. د شپې پر اسمان د ځلېدونکو ستورو منظره په خپلو کلمو بیان کړئ.'),
    ('3. Write the central idea of the poem “Sitare”.', '۳۔ نظم ’’ستارے‘‘ کا مرکزی خیال لکھیں۔', '۳. د "ستوري" نظم مرکزي فکر ولیکئ.'),
    ('4. According to the poet, what has been the habit of the stars since the first day?', '۴۔ شاعر کے مطابق ستاروں کی روزِ اوّلیں سے کون سی عادت ہے؟', '۴. د شاعر په وینا له لومړۍ ورځې د ستورو کوم عادت دی؟'),
    ('5. Write the possessive compounds (murakkab-e iẓāfī) and conjunctive compounds (murakkab-e ʿaṭfī) from this poem separately.', '۵۔ اِس نظم سے مرکبِ اضافی اور مرکبِ عطفی الگ الگ کر کے لکھیں۔', '۵. له دې نظمه اضافي مرکبات او عطفي مرکبات بېل بېل ولیکئ.'),
    ('6. What does the poet mean by “lost paradise”?', '۶۔ ’’گُم شدہ جنت‘‘ سے شاعر کی کیا مراد ہے؟', '۶. د "ورک شوي جنت" څخه د شاعر مطلب څه دی؟'),
])
ex = BOOK.record(e, 'urdu12-u22-exercise', 'Exercise', 'مشق', 'تمرین', 109, [209])

n = Builder()
n.p('*N. M. Rashid also made experiments in the form of the sonnet. Dividing the last six lines of the above sonnet into two stanzas, he has given each stanza the (rhyme) order c-d-e.', '*ن۔م۔ راشدؔ نے سانیٹ کی ہیئت میں بھی تجربے کیے ہیں۔ درج بالا سانیٹ کے آخری چھے مصرعوں کو دو بند میں تقسیم کر کے ہر بند کی ترتیب ج۔د۔ر رکھ دی ہے۔', '*ن.م. راشد د سانېټ په بڼه کې هم تجربې کړې. د پورتني سانېټ وروستۍ شپږ مصرعې یې په دوو بندونو وېشلې او د هر بند (قافیې) ترتیب یې ج-د-ر ایښی.')
nt = BOOK.record(n, 'urdu12-u22-note', 'Note: Rashid’s sonnet form', 'سانیٹ کی ہیئت (حاشیہ)', 'د سانېټ بڼه (یادښت)', 109, [209])
issues = [{'id': 'urdu12-pdf109', 'unit': 22, 'printedPage': 209, 'description': 'A stray mark “ا” is printed beside the first line of the last tercet on p.209; excluded. The poem is a 14-line sonnet (4+4+3+3) and is transcribed in full (Rashid d.1975 — public domain from 1 Jan 2026).'}]

if __name__ == '__main__':
    BOOK.save(109, [(22, po), (22, ex), (22, nt)], issues=issues, complete_units=[22])
