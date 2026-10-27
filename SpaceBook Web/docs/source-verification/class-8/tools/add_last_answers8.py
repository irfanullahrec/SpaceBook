"""add_last_answers8.py - answers for the last 12 Class 8 Mathematics questions that had no solution at all (2026-10-27):
Review Exercise 1 Q1 b), Exercise 5.3 Q14 a) to f) (Venn diagram), Think Higher of Unit 7 (evaluate x, a to c), Exercise 11.3 Q2 a), b).

    python add_last_answers8.py [--dry]

Why this is not a page-file edit: unlike Classes 5 to 7, js/math_8_data.js and js/math_8_solutions.js are NOT reproducible from
class-8/math/pages with build_math8.py (the 3,238 solution ids were put there by earlier steps; a rebuild from the pages drops them all).
So the two js files are the source of truth for Class 8 solutions, as for apply_gen8.py. This script finds each question in the data by its
printed text, gives it a new solution id and adds the solution; it is idempotent (a second run rewrites the same entries).
It also records the entries in class-8/math/gen_solutions.json (keys ex|q|part) so that a later gen run keeps them.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
APP = HERE.parents[2]
DATA = APP / 'js' / 'math_8_data.js'
SOL = APP / 'js' / 'math_8_solutions.js'
GEN = HERE / 'math' / 'gen_solutions.json'


def load(path, name):
    txt = path.read_text(encoding='utf-8')
    m = re.search(r'(?:const|window\.)\s*' + re.escape(name) + r'\s*=\s*', txt)
    obj, end = json.JSONDecoder().raw_decode(txt, m.end())
    return txt, obj, m.end(), end


def step(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m:
        d['m'] = m
    return d


E = []   # (unit number, English text of the question or part, answer, steps, key)

E.append((1, 'Which of these have 3 significant figures?', 'Options iii) and iv)', [
    step('Count the significant figures of each number: 23.78 has 4, 67.07 has 4, 0.350 has 3 (the zero after the decimal point counts) and 680 has 3 as the textbook counts it.',
         'ہر عدد کے بامعنی ہندسے گنیں: 23.78 میں 4، 67.07 میں 4، 0.350 میں 3 (اعشاریہ کے بعد کا صفر بھی شمار ہوتا ہے) اور 680 میں کتاب کے شمار کے مطابق 3 بامعنی ہندسے ہیں۔',
         'د هر عدد معنا لرونکي رقمونه وشمېرئ: په 23.78 کې 4، په 67.07 کې 4، په 0.350 کې 3 (له اعشاریې وروسته صفر هم شمېرل کېږي) او په 680 کې د کتاب د شمېرنې له مخې 3 دي.'),
    step('So options iii) 0.350 and iv) 680 have 3 significant figures (the printed key gives iii, iv).',
         'اس لیے آپشن iii) 0.350 اور iv) 680 میں 3 بامعنی ہندسے ہیں (چھپی ہوئی کلید iii، iv دیتی ہے)۔',
         'نو انتخابونه iii) 0.350 او iv) 680 3 معنا لرونکي رقمونه لري (چاپ شوې کلیل iii، iv ورکوي).')], 'Review Exercise 1|b|'))

venn = {
    'How many students like only pizza?': ('10', 'Only pizza is the region of the pizza circle that lies outside the other two circles: 10 students.',
        'صرف پیزا والا حصہ پیزا کے دائرے کا وہ حصہ ہے جو باقی دو دائروں سے باہر ہے: 10 طلبہ۔', 'یوازې پیزا برخه د پیزا د دایرې هغه برخه ده چې د نورو دوو دایرو بهر ده: 10 زده کوونکي.', 'a'),
    'How many students like only sandwich?': ('7', 'Only sandwich is the region of the sandwich circle outside the other two circles: 7 students.',
        'صرف سینڈوچ والا حصہ سینڈوچ کے دائرے کا وہ حصہ ہے جو باقی دو دائروں سے باہر ہے: 7 طلبہ۔', 'یوازې سینډوچ برخه د سینډوچ د دایرې هغه برخه ده چې د نورو دوو دایرو بهر ده: 7 زده کوونکي.', 'b'),
    'How many students like both pizza and burger?': ('10', 'Both pizza and burger is the part common to the pizza and burger circles: 4 students like only these two and 6 like all three, so 4 + 6 = 10 students.',
        'پیزا اور برگر دونوں وہ حصہ ہے جو پیزا اور برگر کے دائروں میں مشترک ہے: 4 طلبہ صرف یہی دو پسند کرتے ہیں اور 6 تینوں، اس لیے 4 + 6 = 10 طلبہ۔',
        'پیزا او برګر دواړه هغه برخه ده چې د پیزا او برګر په دایرو کې مشترکه ده: 4 زده کوونکي یوازې همدا دوه خوښوي او 6 درې واړه، نو 4 + 6 = 10 زده کوونکي.', 'c'),
    'How many students like both sandwich and pizza?': ('8', 'Both sandwich and pizza is the part common to the sandwich and pizza circles: 2 students like only these two and 6 like all three, so 2 + 6 = 8 students.',
        'سینڈوچ اور پیزا دونوں وہ حصہ ہے جو سینڈوچ اور پیزا کے دائروں میں مشترک ہے: 2 طلبہ صرف یہی دو پسند کرتے ہیں اور 6 تینوں، اس لیے 2 + 6 = 8 طلبہ۔',
        'سینډوچ او پیزا دواړه هغه برخه ده چې د سینډوچ او پیزا په دایرو کې مشترکه ده: 2 زده کوونکي یوازې همدا دوه خوښوي او 6 درې واړه، نو 2 + 6 = 8 زده کوونکي.', 'd'),
    'How many students like only pizza and sandwich?': ('2', 'Only pizza and sandwich (not burger) is the part shared by those two circles and outside the burger circle: 2 students.',
        'صرف پیزا اور سینڈوچ (برگر نہیں) وہ حصہ ہے جو ان دو دائروں میں مشترک ہے اور برگر کے دائرے سے باہر ہے: 2 طلبہ۔',
        'یوازې پیزا او سینډوچ (برګر نه) هغه برخه ده چې په دغو دوو دایرو کې مشترکه او د برګر له دایرې بهر ده: 2 زده کوونکي.', 'e'),
    'How many students like all three types of food?': ('6', 'All three types of food is the part where all three circles overlap: 6 students.',
        'تینوں قسم کے کھانے وہ حصہ ہے جہاں تینوں دائرے ایک دوسرے کو کاٹتے ہیں: 6 طلبہ۔', 'درې واړه ډوله خواړه هغه برخه ده چې درې واړه دایرې یو بل پرې کوي: 6 زده کوونکي.', 'f'),
}
for text, (ans, en, ur, ps, lab) in venn.items():
    E.append((5, text, ans, [step(en, ur, ps)], '5.3|14|' + lab))

ex = [
    ('$4^2 = 2^x$', 'x = 4', 'a', [step('Write both sides with the same base: 4² = 16 = 2⁴.', 'دونوں طرف ایک ہی اساس لکھیں: 4² = 16 = 2⁴۔', 'دواړه خواوې په یوه بنسټ ولیکئ: 4² = 16 = 2⁴.', '4^2 = (2^2)^2 = 2^4 = 2^x'),
                                   step('When the bases are equal the exponents are equal.', 'جب اساس برابر ہوں تو قوتِ نما بھی برابر ہوتے ہیں۔', 'کله چې بنسټونه مساوي وي نو توانونه هم مساوي وي.', 'x = 4')]),
    ('$9^x = 3^8$', 'x = 4', 'b', [step('Write 9 as 3²: 9^x = (3²)^x = 3^(2x).', '9 کو 3² لکھیں: 9^x = (3²)^x = 3^(2x)۔', '9 د 3² په توګه ولیکئ: 9^x = (3²)^x = 3^(2x).', '9^x = (3^2)^x = 3^{2x} = 3^8'),
                                   step('Equal bases, so the exponents are equal: 2x = 8.', 'اساس برابر ہیں، اس لیے قوتِ نما برابر ہیں: 2x = 8۔', 'بنسټونه مساوي دي، نو توانونه مساوي دي: 2x = 8.', '2x = 8 \\Rightarrow x = 4')]),
    ('$412^x = 1^5$', 'x = 0', 'c', [step('1 raised to any power is 1, so 1⁵ = 1.', '1 کی کوئی بھی قوت 1 ہوتی ہے، اس لیے 1⁵ = 1۔', 'د 1 هر توان 1 وي، نو 1⁵ = 1.', '1^5 = 1'),
                                   step('Any non-zero number raised to the power 0 is 1, so 412^x = 1 gives x = 0.', 'کوئی بھی غیر صفر عدد قوت 0 پر 1 ہوتا ہے، اس لیے 412^x = 1 سے x = 0 ملتا ہے۔', 'هر غیر صفر عدد په توان 0 کې 1 وي، نو 412^x = 1 نه x = 0 ګټو.', '412^x = 1 = 412^0 \\Rightarrow x = 0')]),
]
for text, ans, lab, steps in ex:
    E.append((7, text, ans, steps, 'None|1|' + lab))

E.append((11, 'Construct a frequency distribution table having equal class interval.', '15–19: 8, 20–24: 0, 25–29: 13 (total 21)', [
    step('The smallest mark is 15 and the largest is 28, so the range is 28 − 15 = 13. Take equal class intervals of 5: 15–19, 20–24 and 25–29.',
         'سب سے کم نمبر 15 اور سب سے زیادہ 28 ہے، اس لیے حدود 28 − 15 = 13 ہیں۔ 5 کے برابر جماعتی وقفے لیں: 15–19، 20–24 اور 25–29۔',
         'تر ټولو کم نمره 15 او تر ټولو لوړه 28 ده، نو حد 28 − 15 = 13 دی. د 5 مساوي ټولګي وقفې واخلئ: 15–19، 20–24 او 25–29.'),
    step('Tally the marks that are printed: 15–19 has 15, 15 and six 19s = 8; 20–24 has none = 0; 25–29 has five 25s, one 26, two 27s and five 28s = 13.',
         'چھپے ہوئے نمبروں کی گنتی کریں: 15–19 میں 15، 15 اور چھ 19 = 8؛ 20–24 میں کوئی نہیں = 0؛ 25–29 میں پانچ 25، ایک 26، دو 27 اور پانچ 28 = 13۔',
         'چاپ شوې نمرې وشمېرئ: په 15–19 کې 15، 15 او شپږ 19 = 8؛ په 20–24 کې هېڅ نه = 0؛ په 25–29 کې پنځه 25، یو 26، دوه 27 او پنځه 28 = 13.'),
    step('Frequency distribution table: class 15–19 → frequency 8; class 20–24 → frequency 0; class 25–29 → frequency 13; total 21. (The book says 25 students but prints only 21 marks, so the total is 21.)',
         'تعدد تقسیم کا جدول: جماعت 15–19 ← تعدد 8؛ جماعت 20–24 ← تعدد 0؛ جماعت 25–29 ← تعدد 13؛ کل 21۔ (کتاب میں 25 طلبہ لکھا ہے مگر صرف 21 نمبر چھپے ہیں، اس لیے کل 21 ہے۔)',
         'د فریکونسي ویش جدول: ټولګی 15–19 ← فریکونسي 8؛ ټولګی 20–24 ← فریکونسي 0؛ ټولګی 25–29 ← فریکونسي 13؛ ټول 21. (په کتاب کې 25 زده کوونکي لیکل شوي خو یوازې 21 نمرې چاپ شوې دي، نو ټول 21 دی.)')], '11.3|2|a'))
E.append((11, 'What is total number of students having highest marks.', '5 students', [
    step('The highest mark in the list is 28. It occurs five times (the printed list has 28 five times), so 5 students have the highest marks.',
         'فہرست میں سب سے زیادہ نمبر 28 ہے۔ یہ پانچ بار آیا ہے (چھپی ہوئی فہرست میں 28 پانچ بار ہے)، اس لیے سب سے زیادہ نمبر 5 طلبہ کے ہیں۔',
         'په لیست کې تر ټولو لوړه نمره 28 ده. دا پنځه ځله راغلې (په چاپ شوي لیست کې 28 پنځه ځله دی)، نو تر ټولو لوړې نمرې د 5 زده کوونکو دي.')], '11.3|2|b'))


def find(node, unit_no, text, hits, path=()):
    """collect every dict whose English text equals text (a question or a part)"""
    if isinstance(node, dict):
        if node.get('en') == text and ('no' in node or node.get('t') == 'q'):
            hits.append(node)
        for v in node.values():
            find(v, unit_no, text, hits)
    elif isinstance(node, list):
        for v in node:
            find(v, unit_no, text, hits)


def main():
    dry = '--dry' in sys.argv
    dtxt, units, d0, d1 = load(DATA, 'MATH_8_DATA')
    stxt, sols, s0, s1 = load(SOL, 'MATH_8_SOLUTIONS')
    gen = json.loads(GEN.read_text(encoding='utf-8'))
    nxt = max(int(k[1:]) for k in sols) + 1
    done = 0
    for unit_no, text, ans, steps, key in E:
        unit = next(u for u in units if u['number'] == unit_no)
        hits = []
        find(unit, unit_no, text, hits)
        # a unit lists its exercises twice (in the sections and in unit['exercises']): every copy gets the same solution id
        if not 1 <= len(hits) <= 2:
            raise SystemExit('expected one or two copies of %r in unit %d, found %d' % (text, unit_no, len(hits)))
        sid = next((h['solId'] for h in hits if h.get('solId')), None)
        if not sid:
            sid = 's%d' % nxt
            nxt += 1
        for node in hits:
            node['solId'] = sid
        sols[sid] = {'steps': steps, 'answer': ans}
        gen[key] = {'steps': steps, 'answer': ans, 'verified': False, 'notVerified': False}
        done += 1
    print('answers set:', done, '| solution entries:', len(sols))
    if dry:
        return
    DATA.write_text(dtxt[:d0] + json.dumps(units, ensure_ascii=False) + dtxt[d1:], encoding='utf-8')
    SOL.write_text(stxt[:s0] + json.dumps(sols, ensure_ascii=False) + stxt[s1:], encoding='utf-8')
    GEN.write_text(json.dumps(gen, ensure_ascii=False), encoding='utf-8')


if __name__ == '__main__':
    main()
