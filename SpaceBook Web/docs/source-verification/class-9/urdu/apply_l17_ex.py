# -*- coding: utf-8 -*-
"""Rebuild lesson 17 (آتش) exercise from PDF 122 (printed 120)."""
import os, sys, datetime
sys.stdout.reconfigure(encoding='utf-8')
import urdu9_tools as T

BLANKS = [
    ('کہتی ہے تجھ کو خلقِ خدا ______', 'غائبانہ کیا'),
    ('طبل و علم ہی پاس ہے اپنے ______', 'نہ ملک و مال'),
    ('یوں مدعی حسد سے نہ دے داد ______', 'تو نہ دے'),
    ('عدم کے کوچ کی لازم ہے فکر ______', 'ہستی میں'),
    ('خدا تو دوست ہے دشمن ______', 'ہزار راہ میں ہے'),
]
TEACHER = 'طلبہ کو قافیہ اور ردیف کی پہچان کرائیں۔'
Q9 = ('غزل نمبر ۱ کے چوتھے شعر میں "دام" کا لفظ بمعنی جال استعمال ہوا ہے۔ اس کے دوسرے معنی "قیمت" بھی ہیں۔ ایسے الفاظ کو ذو معنی الفاظ کہا جاتا ہے۔ طلبہ کم از کم ایسے پانچ الفاظ تلاش کریں جو ذو معنی ہوں اور انھیں الگ الگ جملوں میں اس طرح استعمال کریں کہ دونوں معنی واضح ہو جائیں۔',
      '(۱) دام: جال / قیمت — شکاری نے دام بچھایا۔ اس کتاب کے دام زیادہ ہیں۔ (۲) سونا: دھات / نیند — اس نے سونے کی انگوٹھی خریدی۔ رات کو جلدی سونا چاہیے۔ (۳) ہار: گلے کا زیور / شکست — ماں نے ہار پہنا۔ ٹیم کو ہار ہوئی۔ (۴) کل: گزرا ہوا دن / آنے والا دن — کل بارش ہوئی تھی۔ کل سکول کھلے گا۔ (۵) پر: اوپر / بازو — کتاب میز پر ہے۔ پرندے کے پر رنگین ہیں۔')

if os.path.exists(T.LOCK):
    sys.exit('shared lock held')
open(T.LOCK, 'w', encoding='utf-8').write(f'class9-content-agent urdu lesson17 exercise {datetime.datetime.now().isoformat()}')
try:
    data = T.load()
    ex = T.lesson(data, 17)['exercise']
    sq = ex['shortQuestions']
    q1 = dict(question='پہلی غزل کے قوافی لکھیں۔', answer='پہلی غزل کے قوافی: فسانہ، غائبانہ، خزانہ، آئینہ خانہ، دانہ، زمانہ، نشانہ، عاشقانہ۔')
    q2 = dict(question='دوسری غزل کی ردیف لکھیں۔', answer='دوسری غزل کی ردیف: "راہ میں ہے"۔')
    q7 = dict(question='مندرجہ ذیل کس قسم کے مرکبات ہیں: زیرِ زمین، طبل و علم، رگِ گل، دام و دانہ، شجرِ سایہ دار۔',
              answer='زیرِ زمین: مرکبِ اضافی (ظرفی)۔ طبل و علم: مرکبِ عطفی۔ رگِ گل: مرکبِ اضافی۔ دام و دانہ: مرکبِ عطفی۔ شجرِ سایہ دار: مرکبِ توصیفی۔')
    ex['shortQuestions'] = [q1, q2] + sq[1:5] + [q7, dict(question=Q9[0], answer=Q9[1])]
    ex['blanks'] = [dict(statement=s, answer=a) for s, a in BLANKS]
    nums = ['۱', '۲', '۳', '۴', '۵', '۶', '۷']
    L = ['مشق', ''] + [f'{n}۔ {q["question"]}' for n, q in zip(nums, ex['shortQuestions'][:7])]
    L += ['۸۔ مصرعے مکمل کریں۔'] + [f'({h}) {s}' for h, (s, _) in zip(['الف', 'ب', 'ج', 'د', 'ہ'], BLANKS)]
    L += [f'۹۔ {Q9[0]}', '', 'ہدایت برائے اساتذہ: ' + TEACHER]
    ex['rawExercise'] = '\n'.join(L)
    ex['teacherInstructions'] = [TEACHER]
    ex['answerNote'] = 'SpaceBook answers (the textbook prints no answers).'
    sr = T.lesson(data, 17).setdefault('sourceReview', {})
    sr.setdefault('notes', []).append('Exercise checked against PDF 122 (printed 120): items 1-2 split as printed (قوافی / ردیف), blank (ج) "حد سے" -> "حسد سے", blank (ہ) answer "ہزار راہ میں ہے" (stored "ہے گر زمانہ کیا" mixed in another ghazal), item 9 and teacher instruction added.')
    T.save(data)
finally:
    os.remove(T.LOCK)
print(T.record_pages([(122, 'corrected', 'Lesson 17 exercise: compared with page image; blanks (ج)(ہ) corrected, items 1-2 split, item 9 and teacher instruction added.')])['counts'])
