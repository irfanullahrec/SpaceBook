# -*- coding: utf-8 -*-
"""Write front-matter pages p000-p008 of Class 9 Computer Science (English-medium Grade X book)."""
import json, re
from pathlib import Path
from toc_src import TOC

HERE = Path(__file__).resolve().parent
m = json.load(open('D:/SpaceBook/_c9render/toc10.json', encoding='utf-8'))
units = {}
for line in (HERE / 'units.tsv').read_text(encoding='utf-8').splitlines():
    if line and not line.startswith('#'):
        n, en, ur, ps, _ = line.split('\t')
        units['Unit ' + n] = (ur, ps)
EXTRA = {'Key Points': ('اہم نکات', 'مهم ټکي'), 'Answers to MCQs': ('کثیر الانتخابی سوالات کے جوابات', 'د څو ځوابه پوښتنو ځوابونه'),
         'List of Figures': ('اشکال کی فہرست', 'د شکلونو لړلیک'), 'List of Tables': ('جدولوں کی فہرست', 'د جدولونو لړلیک'),
         'List of Symbols': ('علامات کی فہرست', 'د نښو لړلیک'), 'List of Notepad ++ Commands': ('Notepad ++ کمانڈز کی فہرست', 'د Notepad ++ د کمانډونو لړلیک'),
         'Bibliography': ('کتابیات', 'د ماخذونو لړلیک'), 'About the Authors': ('مصنفین کا تعارف', 'د لیکوالانو پېژندنه')}


def tr(no, title):
    if no in units:
        return units[no]
    if no in m:
        return m[no][0], m[no][2]
    if title in EXTRA:
        return EXTRA[title]
    if title in m:
        return m[title][0], m[title][2]
    raise SystemExit('no translation for ' + no + ' ' + title)


ROMAN = ['i', 'ii', 'iii', 'iv']
pages = {}
pages[0] = '''@status front-matter
@issue Source: jpg 001 — front cover. The cover says "For Grade X"; this KPTBB Grade X book is the only Computer Science book in the Class 9 folder and is used for Class 9 by the user's decision (2026-10-13).
@deco Front cover: blue digital background with a laptop, a mouse and a globe made of puzzle pieces; "Test Edition" stamp; "Free From Government NOT FOR SALE"; Khyber Pakhtunkhwa Textbook Board emblem on a red strip.
# A Textbook of Computer Science — For Grade X || کمپیوٹر سائنس کی درسی کتاب — برائے جماعت دہم || د کمپیوټر ساینس درسي کتاب — د لسم ټولګي لپاره
p Free From Government — NOT FOR SALE || حکومت کی طرف سے مفت — برائے فروخت نہیں || د حکومت له خوا وړیا — د پلور لپاره نه
p Khyber Pakhtunkhwa Textbook Board, Peshawar. || خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.
'''
pages[1] = '''@status front-matter
@issue Source: jpg 002 — inner title page (a lighter repeat of the cover); a pen signature by a previous owner is not book content.
# A Textbook of Computer Science — For Grade X || کمپیوٹر سائنس کی درسی کتاب — برائے جماعت دہم || د کمپیوټر ساینس درسي کتاب — د لسم ټولګي لپاره
p Khyber Pakhtunkhwa Textbook Board, Peshawar. || خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.
'''
pages[2] = '''@status front-matter
@issue Source: jpg 003 — imprint page. NOC "Comp-X" confirms this is the Grade X book.
## All rights reserved with the Leading Books Publishers, Peshawar || جملہ حقوق بحق لیڈنگ بکس پبلشرز، پشاور محفوظ ہیں || ټول حقونه د لیډنګ بکس خپرندویانو، پېښور سره خوندي دي
p Approved by: Approved by Directorate of Curriculum & Teacher Education (DCTE), Khyber Pakhtunkhwa, Abbottabad according to the National Curriculum 2009. NOC No. 3430-32/S-04/TBB/Comp-X Dated: 18.06.2021 || منظور کنندہ: ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن (DCTE)، خیبر پختونخوا، ایبٹ آباد نے قومی نصاب 2009 کے مطابق منظور کیا۔ NOC نمبر 3430-32/S-04/TBB/Comp-X مورخہ 18.06.2021 || تصویب کوونکی: د نصاب او ښوونکو د زده کړې ریاست (DCTE)، خیبر پښتونخوا، ایبټ اباد د ۲۰۰۹ ملي نصاب سره سم تصویب کړی. NOC شمېره 3430-32/S-04/TBB/Comp-X نېټه 18.06.2021
p Authors: Mohammad Khalid, OPF Boys College, Islamabad. Khalid Asad, Assistant Professor, Govt: Degree College Wadpagga, Peshawar. || مصنفین: محمد خالد، او پی ایف بوائز کالج، اسلام آباد۔ خالد اسد، اسسٹنٹ پروفیسر، گورنمنٹ ڈگری کالج وڈپگہ، پشاور۔ || لیکوالان: محمد خالد، OPF د هلکانو کالج، اسلام اباد. خالد اسد، اسسټنټ پروفیسر، دولتي ډګري کالج وډپګه، پېښور.
p Review Supervision: Gohar Ali Khan, Director, DCTE Khyber Pakhtunkhwa, Abbottabad. || نظرِ ثانی کی نگرانی: گوہر علی خان، ڈائریکٹر، DCTE خیبر پختونخوا، ایبٹ آباد۔ || د بیاکتنې څارنه: ګوهر علي خان، رئیس، DCTE خیبر پښتونخوا، ایبټ اباد.
p Focal Person: Syed Amjad Ali, Additional Director, Curriculum and Textbook Review, DCTE Khyber Pakhtunkhwa, Abbottabad || فوکل پرسن: سید امجد علی، ایڈیشنل ڈائریکٹر، نصاب و درسی کتب کا جائزہ، DCTE خیبر پختونخوا، ایبٹ آباد || اصلي کس: سید امجد علي، مرستیال رئیس، د نصاب او درسي کتابونو بیاکتنه، DCTE خیبر پښتونخوا، ایبټ اباد
p Re-reviewers: Salahud-Din Ayubi, Assistant Professor of Computer Science, GPGC No. 01 Abbottabad. Faheem Ahmad, Lecturer in Computer Science, GPGC Mandian Abbottabad. Sohail Anjum, SST(IT), Govt: High School No. 04 Abbottabad. Sufian Matloob, Desk Officer, DCTE KP Abbottabad. Shakeel Iqbal, Ex-Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar. || دوبارہ جائزہ کار: صلاح الدین ایوبی، اسسٹنٹ پروفیسر کمپیوٹر سائنس، GPGC نمبر 01 ایبٹ آباد۔ فہیم احمد، لیکچرر کمپیوٹر سائنس، GPGC منڈیاں ایبٹ آباد۔ سہیل انجم، SST(IT)، گورنمنٹ ہائی اسکول نمبر 04 ایبٹ آباد۔ سفیان مطلوب، ڈیسک آفیسر، DCTE KP ایبٹ آباد۔ شکیل اقبال، سابق سبجیکٹ اسپیشلسٹ، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || بیاکتونکي: صلاح الدین ایوبي، د کمپیوټر ساینس اسسټنټ پروفیسر، GPGC شمېره 01 ایبټ اباد. فهیم احمد، د کمپیوټر ساینس لکچرر، GPGC منډیان ایبټ اباد. سهیل انجم، SST(IT)، دولتي عالي ښوونځی شمېره 04 ایبټ اباد. سفیان مطلوب، ډیسک افسر، DCTE KP ایبټ اباد. شکیل اقبال، پخوانی مضمون متخصص، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور.
p Supervision: Nasir Kamal, Desk Officer, Khyber Pakhtunkhwa Textbook Board, Peshawar. || نگرانی: ناصر کمال، ڈیسک آفیسر، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || څارنه: ناصر کمال، ډیسک افسر، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور.
p Printing Supervision: Syed M. Farrulsaqlain, Chairman; Abdul Wali Khan, Member (E&P), Khyber Pakhtunkhwa Textbook Board, Peshawar. || طباعت کی نگرانی: سید ایم فرّ الثقلین، چیئرمین؛ عبدالولی خان، ممبر (E&P)، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || د چاپ څارنه: سید م. فرالثقلین، رئیس؛ عبدالولي خان، غړی (E&P)، د خیبر پښتونخوا درسي کتابونو بورډ، پېښور.
p Printed for academic Year 2023-24. Website: www.kptbb.gov.pk Email: membertbb@yahoo.com Telephone: 091-9217159-60 || تعلیمی سال 2023-24 کے لیے طبع شدہ۔ ویب سائٹ: www.kptbb.gov.pk ای میل: membertbb@yahoo.com ٹیلی فون: 091-9217159-60 || د 2023-24 تعلیمي کال لپاره چاپ شوی. وېب پاڼه: www.kptbb.gov.pk برېښنالیک: membertbb@yahoo.com تلیفون: 091-9217159-60
'''
pages[3] = '''@status front-matter
@issue Source: jpg 004 — dedication page with a hadith in English and two Urdu sayings. A pen scribble ("Replica") by a previous owner is not book content.
p "THE SEEKING OF KNOWLEDGE IS OBLIGATORY FOR EVERY MUSLIM" (AL-TIRMIDHI # 74) || "علم حاصل کرنا ہر مسلمان پر فرض ہے" (الترمذی # 74) || "د علم زده کړه پر هر مسلمان فرض ده" (الترمذي # ۷۴)
p Seeking lawful sustenance is an obligation after the fulfilment of the rights of Allah Almighty. (Al-Hadith) || رزقِ حلال کی کوشش کرنا اللہ تعالیٰ کے حقوق کی ادائیگی کے بعد فرض ہے۔ (الحدیث) || د حلال رزق هڅه د الله تعالیٰ د حقونو له ادا کولو وروسته فرض ده. (الحدیث)
@issue The second box is printed in Urdu only; its English line here is our translation.
p Bribery is a cancer — avoid it! || رشوت ایک ناسور ہے اس سے بچیئے! || بډې یو ناسور دی — ځان ترې وساتئ!
'''
pages[4] = '''@status front-matter
@issue Source: jpg 005 — Qur'anic verse (printed in Urdu translation) and the Textbook Board's feedback form.
p The believers are but brothers, so make peace between your two brothers and fear Allah, that you may receive mercy. (Surah Al-Hujurat: 10) || مومن تو آپس میں بھائی بھائی ہیں۔ پس اپنے دو بھائیوں میں صلح کرا دیا کرو اور اللہ سے ڈرتے رہو تاکہ تم پر رحمت کی جائے۔ (سورۃ الحجرات: ۱۰) || مؤمنان خو یو د بل وروڼه دي، نو د خپلو دوو وروڼو ترمنځ سوله وکړئ او له الله ووېرېږئ چې پر تاسو رحم وشي. (سورة الحجرات: ۱۰)
@issue The verse is printed in Urdu only; its English line here is our translation.
'''
c10 = (HERE.parent.parent / 'class-10' / 'comp' / 'pages' / 'p002.txt').read_text(encoding='utf-8').splitlines()
keep = [l for l in c10 if l.startswith(('## Khyber', 'p Phase', 'table', 'th ', 'tr ', 'endtable', 'p Page No.'))]
pages[4] += '\n'.join(keep) + '\n'
for k, rows in enumerate(TOC):
    out = [f'@status front-matter', f'@issue Source: jpg {k + 6:03} — table of contents ({ROMAN[k]}).']
    if k == 0:
        out.append('# Table of Contents || فہرستِ عنوانات || فهرست')
    out.append(f'table Table of Contents ({ROMAN[k]}) || فہرستِ عنوانات ({ROMAN[k]}) || فهرست ({ROMAN[k]})')
    out.append('th | Unit No || نمبر || شمېره | Topic || عنوان || سرلیک | Page No || صفحہ || مخ')
    for no, title, pg in rows:
        ur, ps = tr(no, title)
        if no.startswith('Unit'):
            nur, nps = 'یونٹ ' + no[5:], no[5:] + ' څپرکی'
        else:
            nur = nps = no
        out.append(f'tr | {no} || {nur} || {nps} | {title} || {ur} || {ps} | {pg} || {pg} || {pg}')
    out.append('endtable')
    pages[5 + k] = '\n'.join(out) + '\n'
for i, t in pages.items():
    (HERE / 'pages' / f'p{i:03}.txt').write_text(t, encoding='utf-8')
print('wrote', sorted(pages))
