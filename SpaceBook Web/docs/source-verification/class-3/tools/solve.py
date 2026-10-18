"""Step-by-step SpaceBook solutions (not printed in the textbook) for Class 6 Mathematics exercises.

Every generator computes the answer itself, so the working is always arithmetically correct.
A step is {'en','ur','ps'} narration plus optional 'm' (LaTeX shown under it) and/or 'svg'.
"""
import re
from collections import Counter
from math import gcd
import figs
from figs import grid

X = r' \times '


def S(en, ur, ps, m=None, svg=None):
    step = {'en': en, 'ur': ur, 'ps': ps}
    if m:
        step['m'] = m
    if svg:
        step['svg'] = svg
    return step


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def lst(xs, en=True):
    xs = [str(x) for x in xs]
    if len(xs) == 1:
        return xs[0]
    return ', '.join(xs[:-1]) + (' and ' if en else '، ') + xs[-1]


def lst_ur(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else '، '.join(xs[:-1]) + ' اور ' + xs[-1]


def lst_ps(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else '، '.join(xs[:-1]) + ' او ' + xs[-1]


def primes_of(n):
    out, p = [], 2
    while n > 1:
        while n % p == 0:
            out.append(p)
            n //= p
        p += 1 if p == 2 else 2
        if p * p > n and n > 1:
            out.append(n)
            break
    return out


def index_tex(fs):
    c = Counter(fs)
    return X.join(f'{p}^{{{k}}}' if k > 1 else str(p) for p, k in sorted(c.items()))


def expanded_tex(fs):
    return X.join(str(p) for p in fs)


# ---------------------------------------------------------------- factors / multiples
def factors(text, *_):
    n = nums(text)[0]
    steps = [S(f'To find the factors of {n}, divide {n} by 1, 2, 3, … one by one. Each exact division gives a pair of factors. We stop when the pairs start repeating.',
               f'{n} کے اجزائے ضربی معلوم کرنے کے لیے {n} کو 1، 2، 3، … سے باری باری تقسیم کریں۔ ہر پوری تقسیم سے اجزائے ضربی کا ایک جوڑا ملتا ہے۔ جب جوڑے دہرانے لگیں تو رک جائیں۔',
               f'د {n} د ضربي اجزاوو د موندلو لپاره {n} په 1، 2، 3، … یو په یو ووېشئ. هر بشپړ وېش د ضربي اجزاوو یوه جوړه راکوي. کله چې جوړې تکرار شي، ودرېږئ.')]
    found = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            q = n // d
            found += [d, q]
            if d == q:
                steps.append(S(f'{n} ÷ {d} = {q}. Both factors are the same ({d}), so we stop here.',
                               f'{n} ÷ {d} = {q}۔ دونوں اجزائے ضربی ایک جیسے ({d}) ہیں، اس لیے یہاں رک جائیں۔',
                               f'{n} ÷ {d} = {q}. دواړه ضربي اجزا یو شان ({d}) دي، نو دلته ودرېږئ.', m=f'{n} = {d}{X}{q}'))
            else:
                steps.append(S(f'{n} ÷ {d} = {q} with no remainder, so {d} and {q} are factors.',
                               f'{n} ÷ {d} = {q} اور کوئی باقی نہیں، اس لیے {d} اور {q} اجزائے ضربی ہیں۔',
                               f'{n} ÷ {d} = {q} او هېڅ پاتې شونی نشته، نو {d} او {q} ضربي اجزا دي.', m=f'{n} = {d}{X}{q}'))
        d += 1
    last = d - 1
    if last * last != n:
        steps.append(S(f'The next number to try would be bigger than the other factor in the pair, so the pairs now repeat. We stop.',
                       f'اب آزمایا جانے والا اگلا عدد جوڑے کے دوسرے جزو سے بڑا ہو گا، یعنی جوڑے دہرائے جائیں گے۔ اس لیے رک جاتے ہیں۔',
                       f'اوس به بل ازمول کېدونکی عدد د جوړې له بل جز څخه لوی وي، یعنې جوړې تکرارېږي. نو درېږو.'))
    fs = sorted(set(found))
    steps.append(S(f'Factors of {n} are {lst(fs)}.', f'{n} کے اجزائے ضربی {lst_ur(fs)} ہیں۔', f'د {n} ضربي اجزا {lst_ps(fs)} دي.'))
    return {'steps': steps, 'answer': f'{lst(fs)}'}


def multiples(text, limit=None, *_):
    vals = nums(text)
    n = vals[0]
    limit = int(limit) if limit else vals[1]
    ms = list(range(n, limit, n))
    steps = [S(f'Multiples of {n} are found by multiplying {n} by 1, 2, 3, … We keep going while the answer is less than {limit}.',
               f'{n} کے اضعاف {n} کو 1، 2، 3، … سے ضرب دے کر ملتے ہیں۔ جب تک جواب {limit} سے کم ہو، ہم ضرب دیتے رہتے ہیں۔',
               f'د {n} ضربونه د {n} په 1، 2، 3، … کې د ضربولو له لارې لاسته راځي. تر هغه دوام ورکوو چې ځواب له {limit} څخه کم وي.')]
    rows = [ms[i:i + 4] for i in range(0, len(ms), 4)]
    for r in rows:
        steps.append(S('Next multiples:', 'اگلے اضعاف:', 'نور ضربونه:',
                       m=r',\quad '.join(f'{v // n}{X}{n} = {v}' for v in r)))
    k = len(ms) + 1
    steps.append(S(f'{k} × {n} = {k * n}, which is not less than {limit}, so we stop.',
                   f'{k} × {n} = {k * n}، جو {limit} سے کم نہیں، اس لیے رک جاتے ہیں۔',
                   f'{k} × {n} = {k * n}، چې له {limit} څخه کم نه دی، نو درېږو.'))
    steps.append(S(f'Multiples of {n} less than {limit} are {lst(ms)}.', f'{limit} سے کم {n} کے اضعاف {lst_ur(ms)} ہیں۔',
                   f'له {limit} څخه کم د {n} ضربونه {lst_ps(ms)} دي.'))
    return {'steps': steps, 'answer': lst(ms)}


def first_multiples(text, count, *_):
    n = nums(text)[0]
    count = int(count)
    ms = [n * k for k in range(1, count + 1)]
    steps = [S(f'Multiply {n} by 1, 2, 3, … to get its multiples. We need the first {count}.',
               f'{n} کے اضعاف حاصل کرنے کے لیے اسے 1، 2، 3، … سے ضرب دیں۔ ہمیں پہلے {count} چاہئیں۔',
               f'د {n} د ضربونو لپاره یې په 1، 2، 3، … کې ضرب کړئ. لومړي {count} ته اړتیا لرو.',
               m=r',\quad '.join(f'{k}{X}{n} = {n * k}' for k in range(1, count + 1))),
             S(f'The first {count} multiples of {n} are {lst(ms)}.', f'{n} کے پہلے {count} اضعاف {lst_ur(ms)} ہیں۔', f'د {n} لومړي {count} ضربونه {lst_ps(ms)} دي.')]
    return {'steps': steps, 'answer': lst(ms)}


def square(text, *_):
    n = nums(text)[0]
    steps = [S(f'The square of {n} means {n} multiplied by itself.', f'{n} کے مربع کا مطلب ہے {n} کو خود سے ضرب دینا۔', f'د {n} مربع یعنې {n} په خپل ځان کې ضربول.', m=f'{n}^{{2}} = {n}{X}{n}')]
    if n >= 10 and n % 10:
        t, o = n - n % 10, n % 10
        steps.append(S(f'Easy way: break the second {n} into {t} + {o} and multiply {n} by each part.',
                       f'آسان طریقہ: دوسرے {n} کو {t} + {o} میں توڑیں اور {n} کو ہر حصے سے ضرب دیں۔',
                       f'اسانه لاره: دوهم {n} په {t} + {o} ووېشئ او {n} په هره برخه کې ضرب کړئ.',
                       m=f'{n}{X}{t} = {n * t},\\qquad {n}{X}{o} = {n * o}'))
        steps.append(S('Now add the two answers.', 'اب دونوں جوابات جمع کریں۔', 'اوس دواړه ځوابونه جمع کړئ.', m=f'{n * t} + {n * o} = {n * n}'))
    elif n >= 10:
        steps.append(S(f'{n} ends in 0: multiply {n // 10} × {n // 10} = {(n // 10) ** 2} and write two zeros after it.',
                       f'{n} کے آخر میں 0 ہے: {n // 10} × {n // 10} = {(n // 10) ** 2} اور اس کے بعد دو صفر لکھیں۔',
                       f'{n} په 0 پای ته رسېږي: {n // 10} × {n // 10} = {(n // 10) ** 2} او وروسته یې دوه صفرونه ولیکئ.', m=f'{n}^{{2}} = {n * n}'))
    else:
        steps.append(S('Use the multiplication table.', 'پہاڑا استعمال کریں۔', 'د ضرب جدول وکاروئ.', m=f'{n}{X}{n} = {n * n}'))
    steps.append(S(f'So, the square of {n} is {n * n}.', f'لہٰذا {n} کا مربع {n * n} ہے۔', f'نو د {n} مربع {n * n} دی.'))
    return {'steps': steps, 'answer': f'${n}^2 = {n * n}$'}


def _int(v):
    return int(v.replace('–', '-').replace('−', '-').replace('+', '').replace(' ', ''))


def _sg(v):
    return '0' if v == 0 else ('+' if v > 0 else '–') + str(abs(v))


def opposite(text, *_):
    v = _int(re.search(r'[+\-–−]?\s*\d+', text).group())
    o = -v
    if v == 0:
        steps = [S('0 is neither positive nor negative, so the opposite of 0 is 0 itself.', '0 نہ مثبت ہے نہ منفی، اس لیے 0 کا مخالف 0 ہی ہے۔', '0 نه مثبت دی نه منفي، نو د 0 مخالف پخپله 0 دی.')]
    else:
        side, other = ('right', 'left') if v > 0 else ('left', 'right')
        su, ou = ('دائیں', 'بائیں') if v > 0 else ('بائیں', 'دائیں')
        sp, op_ = ('ښي', 'کیڼ') if v > 0 else ('کیڼ', 'ښي')
        steps = [S('The opposite of an integer is the same distance from 0, on the other side of 0. Just change the sign.',
                   'کسی صحیح عدد کا مخالف 0 سے اتنے ہی فاصلے پر، 0 کی دوسری طرف ہوتا ہے۔ صرف علامت بدل دیں۔',
                   'د تام عدد مخالف له 0 څخه په هماغه واټن، د 0 بل لوري ته وي. یوازې نښه بدله کړئ.'),
                 S(f'{_sg(v)} is {abs(v)} steps to the {side} of 0, so its opposite is {abs(v)} steps to the {other}: {_sg(o)}.',
                   f'{_sg(v)} صفر سے {abs(v)} قدم {su} طرف ہے، اس لیے اس کا مخالف {abs(v)} قدم {ou} طرف ہے: {_sg(o)}۔',
                   f'{_sg(v)} له 0 څخه {abs(v)} ګامه {sp} لوري ته دی، نو مخالف یې {abs(v)} ګامه {op_} لوري ته دی: {_sg(o)}.',
                   svg=figs.nline(f'{-abs(v) - 1}..{abs(v) + 1} | circ={v},{o}') if abs(v) <= 25 else None)]
    return {'steps': steps, 'answer': _sg(o)}


def between(text, *_):
    a, b = [_int(x) for x in re.findall(r'[+\-–−]?\d+', text)[:2]]
    lo, hi = min(a, b), max(a, b)
    vals = list(range(lo + 1, hi))
    steps = [S(f'Start just after {_sg(lo)} and count up by 1 until just before {_sg(hi)}. The two given numbers themselves are not included.',
               f'{_sg(lo)} کے فوراً بعد سے شروع کریں اور {_sg(hi)} سے ذرا پہلے تک ایک ایک بڑھائیں۔ دیے گئے دونوں اعداد شامل نہیں۔',
               f'له {_sg(lo)} وروسته پیل وکړئ او تر {_sg(hi)} مخکې پورې یو یو زیات کړئ. ورکړل شوي دواړه عددونه نه شاملېږي.',
               svg=figs.nline(f'{lo}..{hi} | dots=' + ','.join(map(str, vals))) if vals and hi - lo <= 40 else None),
             S(f'Integers between {_sg(lo)} and {_sg(hi)}:', f'{_sg(lo)} اور {_sg(hi)} کے درمیان صحیح اعداد:', f'د {_sg(lo)} او {_sg(hi)} ترمنځ تام عددونه:',
               m=', '.join(str(v) for v in vals) if vals else r'\text{none}')]
    return {'steps': steps, 'answer': ', '.join(_sg(v) for v in vals) or 'none'}


def six(text, *_):
    m = re.search(r'([<>])\s*([+\-–−]?\d+)', text)
    op, v = m.group(1), _int(m.group(2))
    vals = [v - k for k in range(1, 7)] if op == '<' else [v + k for k in range(1, 7)]
    if op == '<':
        en, ur, ps = (f'Integers less than {_sg(v)} lie to the left of it on the number line. Take the six nearest ones.',
                      f'{_sg(v)} سے کم صحیح اعداد عددی لائن پر اس کے بائیں طرف ہوتے ہیں۔ قریب ترین چھ لیں۔',
                      f'له {_sg(v)} څخه کم تام عددونه په عددي کرښه د هغه کیڼ لوري ته وي. نږدې شپږ واخلئ.')
    else:
        en, ur, ps = (f'Integers greater than {_sg(v)} lie to the right of it on the number line. Take the six nearest ones.',
                      f'{_sg(v)} سے بڑے صحیح اعداد عددی لائن پر اس کے دائیں طرف ہوتے ہیں۔ قریب ترین چھ لیں۔',
                      f'له {_sg(v)} څخه لوی تام عددونه په عددي کرښه د هغه ښي لوري ته وي. نږدې شپږ واخلئ.')
    steps = [S(en, ur, ps, svg=figs.nline(f'{min(vals + [v]) - 1}..{max(vals + [v]) + 1} | circ={v} | dots=' + ','.join(map(str, vals)))),
             S('Six such integers (any six correct integers are also right):', 'ایسے چھ صحیح اعداد (کوئی بھی چھ درست اعداد بھی صحیح ہیں):', 'شپږ داسې تام عددونه (هر شپږ سم عددونه هم سم دي):',
               m=', '.join(str(x) for x in vals))]
    return {'steps': steps, 'answer': ', '.join(_sg(x) for x in vals)}


def _ints(text):
    return [_int(x) for x in re.findall(r'[+\-–−]?\s*\d+', text)]


def represent(text, *_):
    a, b = _ints(text)[:2]
    lo, hi = min(a, b), max(a, b)
    vals = list(range(lo, hi + 1))
    steps = [S('Draw a line, mark 0 in the middle and equal steps on both sides. Positive integers go to the right of 0, negative integers to the left.',
               'ایک لائن کھینچیں، درمیان میں 0 لگائیں اور دونوں طرف برابر قدم بنائیں۔ مثبت صحیح اعداد 0 کے دائیں اور منفی بائیں طرف آتے ہیں۔',
               'یوه کرښه رسم کړئ، په منځ کې 0 ولګوئ او دواړو خواوو ته برابر ګامونه جوړ کړئ. مثبت تام عددونه د 0 ښي او منفي کیڼ لوري ته راځي.'),
             S(f'Mark every integer from {_sg(lo)} to {_sg(hi)} with a dot ({len(vals)} integers).', f'{_sg(lo)} سے {_sg(hi)} تک ہر صحیح عدد پر نقطہ لگائیں ({len(vals)} صحیح اعداد)۔',
               f'له {_sg(lo)} تر {_sg(hi)} پورې پر هر تام عدد نقطه ولګوئ ({len(vals)} تام عددونه).',
               svg=figs.nline(f'{min(lo, 0) - 1}..{max(hi, 0) + 1} | dots=' + ','.join(map(str, vals))))]
    return {'steps': steps, 'answer': f'{_sg(lo)}, …, {_sg(hi)} marked on the number line'}


def greater(text, *_):
    a, b = _ints(text)[:2]
    g, s_ = max(a, b), min(a, b)
    if a < 0 and b < 0:
        why = (f'Both are negative. The one with the smaller number part is greater: {abs(g)} is smaller than {abs(s_)}, so {_sg(g)} is closer to 0, on the right of {_sg(s_)}.',
               f'دونوں منفی ہیں۔ جس کا عددی حصہ چھوٹا ہو وہ بڑا ہے: {abs(g)}، عدد {abs(s_)} سے چھوٹا ہے، اس لیے {_sg(g)} صفر کے زیادہ قریب اور {_sg(s_)} کے دائیں طرف ہے۔',
               f'دواړه منفي دي. چې عددي برخه یې کوچنۍ وي هغه لوی دی: {abs(g)} له {abs(s_)} کوچنی دی، نو {_sg(g)} صفر ته نږدې او د {_sg(s_)} ښي لوري ته دی.')
    elif a >= 0 and b >= 0:
        why = (f'Both are positive, so the bigger number is greater.', 'دونوں مثبت ہیں، اس لیے بڑا عدد بڑا ہے۔', 'دواړه مثبت دي، نو لوی عدد لوی دی.')
    else:
        why = ('Every positive integer (and 0) is greater than every negative integer.', 'ہر مثبت صحیح عدد (اور 0) ہر منفی صحیح عدد سے بڑا ہوتا ہے۔', 'هر مثبت تام عدد (او 0) له هر منفي تام عدد لوی وي.')
    steps = [S(*why), S(f'So {_sg(g)} is greater.', f'لہٰذا {_sg(g)} بڑا ہے۔', f'نو {_sg(g)} لوی دی.', m=f'{g} > {s_}')]
    return {'steps': steps, 'answer': f'{_sg(g)} is greater'}


def order(text, direction='asc', *_):
    v = _ints(text)
    neg = sorted(x for x in v if x < 0)
    pos = sorted(x for x in v if x > 0)
    zero = [x for x in v if x == 0]
    asc = sorted(v)
    res = asc if direction == 'asc' else asc[::-1]
    steps = [S('Sort the negative integers first: the one with the biggest number part is the smallest.', 'پہلے منفی صحیح اعداد ترتیب دیں: جس کا عددی حصہ سب سے بڑا ہو وہ سب سے چھوٹا ہے۔',
               'لومړی منفي تام عددونه ترتیب کړئ: چې عددي برخه یې تر ټولو لویه وي هغه تر ټولو کوچنی دی.', m=' < '.join(map(str, neg)) if len(neg) > 1 else (str(neg[0]) if neg else r'\text{none}'))]
    if zero:
        steps.append(S('0 comes after all the negative integers and before all the positive integers.', '0 تمام منفی اعداد کے بعد اور تمام مثبت اعداد سے پہلے آتا ہے۔', '0 له ټولو منفي عددونو وروسته او له ټولو مثبتو مخکې راځي.'))
    steps.append(S('Then sort the positive integers from smallest to greatest.', 'پھر مثبت صحیح اعداد کو چھوٹے سے بڑے کی ترتیب میں لکھیں۔', 'بیا مثبت تام عددونه له کوچني څخه لوي ته ترتیب کړئ.',
                   m=' < '.join(map(str, pos)) if len(pos) > 1 else (str(pos[0]) if pos else r'\text{none}')))
    if direction == 'asc':
        steps.append(S('Ascending order (smallest to greatest):', 'صعودی ترتیب (چھوٹے سے بڑا):', 'صعودي ترتیب (له کوچني لوي ته):', m=',\\ '.join(map(str, res))))
    else:
        steps.append(S('Descending order (greatest to smallest) is the same list read backwards:', 'نزولی ترتیب (بڑے سے چھوٹا) یہی فہرست الٹی پڑھنے سے ملتی ہے:', 'نزولي ترتیب (له لوي کوچني ته) همدا لیست له شا نه لوستل دي:', m=',\\ '.join(map(str, res))))
    return {'steps': steps, 'answer': ', '.join(_sg(x) for x in res)}


def absval(text, *_):
    v = _ints(text)[0]
    steps = [S('The absolute value is the distance of the integer from 0 on the number line. Distance has no direction, so just drop the sign.',
               'مطلق قیمت عددی لائن پر صحیح عدد کا صفر سے فاصلہ ہے۔ فاصلے کی کوئی سمت نہیں ہوتی، اس لیے صرف علامت ہٹا دیں۔',
               'مطلق ارزښت په عددي کرښه د تام عدد واټن له 0 څخه دی. واټن لوری نه لري، نو یوازې نښه لرې کړئ.'),
             S(f'{_sg(v)} is {abs(v)} steps from 0.', f'{_sg(v)} صفر سے {abs(v)} قدم دور ہے۔', f'{_sg(v)} له 0 څخه {abs(v)} ګامه لرې دی.', m=f'|{v if v <= 0 else "+" + str(v)}| = {abs(v)}')]
    return {'steps': steps, 'answer': f'$|{v if v <= 0 else "+" + str(v)}| = {abs(v)}$'}


def absorder(text, *_):
    v = _ints(text)
    a = [abs(x) for x in v]
    steps = [S('First write the absolute value of each integer (drop every sign).', 'پہلے ہر صحیح عدد کی مطلق قیمت لکھیں (ہر علامت ہٹا دیں)۔', 'لومړی د هر تام عدد مطلق ارزښت ولیکئ (هره نښه لرې کړئ).',
               m=',\\ '.join(f'|{x if x <= 0 else "+" + str(x)}| = {abs(x)}' for x in v)),
             S('Ascending order (smallest to greatest):', 'صعودی ترتیب (چھوٹے سے بڑا):', 'صعودي ترتیب (له کوچني لوي ته):', m=',\\ '.join(map(str, sorted(a)))),
             S('Descending order (greatest to smallest):', 'نزولی ترتیب (بڑے سے چھوٹا):', 'نزولي ترتیب (له لوي کوچني ته):', m=',\\ '.join(map(str, sorted(a, reverse=True))))]
    return {'steps': steps, 'answer': 'Ascending: ' + ', '.join(map(str, sorted(a))) + '; Descending: ' + ', '.join(map(str, sorted(a, reverse=True)))}


def _norm(text):
    return text.replace('–', '-').replace('−', '-').replace('$', '').replace('\\times', '*').replace('×', '*')


def _terms_signed(expr):
    """'(+4) - (+2) + (-3)' -> [(+1, 4), (-1, 2), (+1, -3)]  (operator sign, integer)"""
    expr = _norm(expr).strip()
    out = []
    for op, val in re.findall(r'([+\-]?)\s*\(?\s*([+\-]?\s*\d+)\s*\)?', expr):
        out.append((-1 if op == '-' else 1, int(val.replace(' ', ''))))
    return out


def _t(v):
    return f'({v:+d})'.replace('+', '+') if v else '0'


def _addrule(a, b):
    """Narrate a + b by the textbook rule; returns (step, result)."""
    r = a + b
    if (a >= 0) == (b >= 0) or a == 0 or b == 0:
        sign = '+' if (a > 0 or b > 0) else '–'
        if a == 0 or b == 0:
            return S(f'Adding 0 does not change a number.', '0 جمع کرنے سے عدد نہیں بدلتا۔', 'د 0 جمع کول عدد نه بدلوي.', m=f'{_t(a)} + {_t(b)} = {_t(r)}'), r
        return S(f'Same signs: add the absolute values {abs(a)} + {abs(b)} = {abs(r)} and keep the common sign ({sign}).',
                 f'یکساں علامتیں: مطلق قیمتیں جمع کریں {abs(a)} + {abs(b)} = {abs(r)} اور مشترک علامت ({sign}) لگائیں۔',
                 f'ورته نښې: مطلق ارزښتونه جمع کړئ {abs(a)} + {abs(b)} = {abs(r)} او مشترکه نښه ({sign}) ولګوئ.', m=f'{_t(a)} + {_t(b)} = {_t(r)}'), r
    big = a if abs(a) >= abs(b) else b
    if r == 0:
        return S(f'{_t(a)} and {_t(b)} are opposites, so their sum is 0.', f'{_t(a)} اور {_t(b)} ایک دوسرے کے مخالف ہیں، اس لیے مجموعہ 0 ہے۔',
                 f'{_t(a)} او {_t(b)} یو د بل مخالف دي، نو مجموعه یې 0 ده.', m=f'{_t(a)} + {_t(b)} = 0'), r
    sign = '+' if big > 0 else '–'
    return S(f'Opposite signs: subtract the absolute values {max(abs(a), abs(b))} − {min(abs(a), abs(b))} = {abs(r)} and take the sign of the integer with the greater absolute value ({sign}).',
             f'مخالف علامتیں: مطلق قیمتیں تفریق کریں {max(abs(a), abs(b))} − {min(abs(a), abs(b))} = {abs(r)} اور بڑی مطلق قیمت والے صحیح عدد کی علامت ({sign}) لگائیں۔',
             f'مخالفې نښې: مطلق ارزښتونه تفریق کړئ {max(abs(a), abs(b))} − {min(abs(a), abs(b))} = {abs(r)} او د لوي مطلق ارزښت لرونکي تام عدد نښه ({sign}) ولګوئ.',
             m=f'{_t(a)} + {_t(b)} = {_t(r)}'), r


def iexpr(text, mode='', *_):
    terms = _terms_signed(text)
    steps = []
    vals = [s * v for s, v in terms]
    if any(s < 0 for s, _ in terms):
        steps.append(S('Change every subtraction into addition of the opposite integer (keep the first number unchanged).',
                       'ہر تفریق کو مخالف صحیح عدد کی جمع میں بدل دیں (پہلا عدد ویسا ہی رہے)۔',
                       'هر تفریق د مخالف تام عدد په جمع بدل کړئ (لومړی عدد مه بدلوئ).',
                       m=' + '.join(_t(v) for v in vals)))
    acc = vals[0]
    partial = [0, acc]
    for v in vals[1:]:
        st, acc = _addrule(acc, v)
        steps.append(st)
        partial.append(acc)
    if mode == 'nl':
        lo, hi = min(partial) - 1, max(partial) + 1
        arcs = ' | '.join(f'{partial[i]}>{partial[i + 1]} {"above" if i % 2 == 0 else "below"}' for i in range(len(partial) - 1) if partial[i] != partial[i + 1])
        steps.insert(0, S('On the number line: start at 0, move right for a positive number and left for a negative number.',
                          'عددی لائن پر: 0 سے شروع کریں، مثبت عدد کے لیے دائیں اور منفی عدد کے لیے بائیں جائیں۔',
                          'په عددي کرښه: له 0 پیل وکړئ، د مثبت عدد لپاره ښي او د منفي عدد لپاره کیڼ لوري ته لاړ شئ.',
                          svg=figs.nline(f'{lo}..{hi} | circ={acc} | {arcs}')))
    steps.append(S(f'Answer: {_t(acc) if acc else 0}', f'جواب: {_t(acc) if acc else 0}', f'ځواب: {_t(acc) if acc else 0}'))
    return {'steps': steps, 'answer': f'{acc:+d}' if acc else '0'}


def missing(text, *_):
    t = _norm(text).replace('_', '?')
    t = re.sub(r'\?+', '?', t)
    lhs, rhs = t.split('=')
    def side(s):
        out = []
        for op, val in re.findall(r'([+\-]?)\s*\(?\s*([+\-]?\s*\d+|\?)\s*\)?', s):
            out.append((-1 if op == '-' else 1, None if val == '?' else int(val.replace(' ', ''))))
        return out
    L, R = side(lhs), side(rhs)
    # move everything to: sum(L) - sum(R) = 0, solve for the single unknown
    known = sum(s * v for s, v in L if v is not None) - sum(s * v for s, v in R if v is not None)
    coef = sum(s for s, v in L if v is None) - sum(s for s, v in R if v is None)
    x = -known // coef
    filled = text
    for pat in ('______', '_____', '____', '___', '__', '_'):
        if pat in filled:
            filled = filled.replace(pat, f'({x:+d})' if x else '0', 1)
            break
    steps = [S('The blank is an unknown integer. Undo the operations around it using the inverse operation (addition ↔ subtraction).',
               'خالی جگہ ایک نامعلوم صحیح عدد ہے۔ اس کے گرد کی عملیات کو الٹی عملیات (جمع ↔ تفریق) سے ختم کریں۔',
               'تشه ځای یو نامعلوم تام عدد دی. د هغه شاوخوا عملیې په معکوسه عملیه (جمع ↔ تفریق) لرې کړئ.'),
             S(f'Collect the known integers: they make {known:+d} on the blank\'s side when everything is moved to one side.',
               f'معلوم صحیح اعداد اکٹھے کریں: سب کچھ ایک طرف لے جانے پر یہ {known:+d} بنتے ہیں۔',
               f'معلوم تام عددونه راټول کړئ: کله چې هر څه یو اړخ ته یوسو، {known:+d} جوړېږي.'),
             S(f'So the missing integer is {x:+d}.' if x else 'So the missing integer is 0.', f'لہٰذا نامعلوم صحیح عدد {x:+d} ہے۔' if x else 'لہٰذا نامعلوم صحیح عدد 0 ہے۔',
               f'نو نامعلوم تام عدد {x:+d} دی.' if x else 'نو نامعلوم تام عدد 0 دی.'),
             S('Check by putting it in the blank:', 'خالی جگہ میں رکھ کر جانچیں:', 'تش ځای ته یې کېږدئ او وازمویئ:', m=_norm(filled).replace('*', r'\times '))]
    return {'steps': steps, 'answer': f'{x:+d}' if x else '0'}


def _pyexpr(text):
    t = _norm(text)
    t = t.replace('{', '(').replace('[', '(').replace('}', ')').replace(']', ')').replace('x', '*')
    t = re.sub(r'\s+', ' ', t).strip()
    t = t + ')' * max(0, t.count('(') - t.count(')'))
    t = '(' * max(0, t.count(')') - t.count('(')) + t
    return t


def _show(e):
    return e.replace('*', r' \times ').replace('-', '-')


def _reduce(expr):
    """Return list of intermediate expressions, innermost brackets first, ending in a single integer."""
    states = [expr]
    cur = expr
    for _ in range(30):
        m = None
        for g in re.finditer(r'\(([^()]*)\)', cur):
            if re.fullmatch(r'\s*[+\-]?\s*\d+\s*', g.group(1)):
                continue
            m = g
            break
        if m:
            v = eval(m.group(1), {'__builtins__': {}})
            rep = f'({v})' if v < 0 else str(v)
            cur = cur[:m.start()] + rep + cur[m.end():]
        else:
            v = eval(cur, {'__builtins__': {}})
            cur = str(v)
        if cur != states[-1]:
            states.append(cur)
        if re.fullmatch(r'-?\d+', cur):
            break
    return states


def _val(expr):
    return eval(expr, {'__builtins__': {}})


def _side_steps(label_en, label_ur, label_ps, expr):
    states = _reduce(expr)
    return [S(f'{label_en}: simplify brackets first, then add.', f'{label_ur}: پہلے قوسین حل کریں، پھر جمع کریں۔', f'{label_ps}: لومړی قوسونه حل کړئ، بیا جمع کړئ.',
              m=' = '.join(_show(s) for s in states))], _val(expr)


def verify(text, mode='check', *_):
    """Evaluate both sides of 'lhs = rhs'. mode 'check' states true/false; 'verify' proves LHS = RHS."""
    lhs, rhs = [_pyexpr(x) for x in text.split('=')[:2]]
    s1, a = _side_steps('Left side', 'بایاں طرف', 'کیڼ اړخ', lhs)
    s2, b = _side_steps('Right side', 'دایاں طرف', 'ښي اړخ', rhs)
    same = a == b
    if same:
        concl = S(f'Both sides are {a}, so L.H.S = R.H.S. The statement is true.', f'دونوں طرف {a} ہیں، اس لیے L.H.S = R.H.S۔ بیان درست ہے۔', f'دواړه اړخونه {a} دي، نو L.H.S = R.H.S. بیان سم دی.', m=f'{a} = {b}')
    else:
        concl = S(f'The left side is {a} but the right side is {b}. They are not equal, so the statement is false.', f'بایاں طرف {a} ہے مگر دایاں طرف {b} ہے۔ یہ برابر نہیں، اس لیے بیان غلط ہے۔',
                  f'کیڼ اړخ {a} دی خو ښي اړخ {b} دی. دا برابر نه دي، نو بیان غلط دی.', m=rf'{a} \neq {b}')
    return {'steps': s1 + s2 + [concl], 'answer': ('True' if same else 'False') + f' (L.H.S = {a}, R.H.S = {b})'}


def comm(text, mode='', *_):
    if mode == 'mul':
        return comm_mul(text)
    a, b = [_ints(text)[0], _ints(text)[1]]
    A, B = f'({a})', f'({b})'
    steps = [S('Commutative Law: a + b = b + a (changing the order does not change the sum). Let us test it with the given integers.',
               'قانونِ مبادلہ: a + b = b + a (ترتیب بدلنے سے مجموعہ نہیں بدلتا)۔ آئیے دیے گئے صحیح اعداد سے جانچیں۔',
               'د تبادلې قانون: a + b = b + a (د ترتیب بدلول مجموعه نه بدلوي). راځئ ورکړل شوو تامو عددونو سره یې وازمویو.')]
    s1, v1 = _side_steps('a + b', 'a + b', 'a + b', f'{A} + {B}')
    s2, v2 = _side_steps('b + a', 'b + a', 'b + a', f'{B} + {A}')
    steps += s1 + s2 + [S(f'Both give {v1}, so a + b = b + a. The Commutative Law is verified.', f'دونوں کا نتیجہ {v1} ہے، اس لیے a + b = b + a۔ قانونِ مبادلہ ثابت ہوا۔',
                         f'دواړه {v1} ورکوي، نو a + b = b + a. د تبادلې قانون ثابت شو.', m=f'{A} + {B} = {B} + {A} = {v1}')]
    return {'steps': steps, 'answer': f'Verified: both sides = {v1}'}


def assoc(text, mode='', *_):
    if mode == 'mul':
        return assoc_mul(text)
    a, b, c = _ints(text)[:3]
    A, B, C = f'({a})', f'({b})', f'({c})'
    steps = [S('Associative Law: (a + b) + c = a + (b + c) (the grouping does not change the sum). Let us test it.',
               'قانونِ تلازم: (a + b) + c = a + (b + c) (گروہ بندی بدلنے سے مجموعہ نہیں بدلتا)۔ آئیے جانچیں۔',
               'د اتحاد قانون: (a + b) + c = a + (b + c) (د ګروپ کولو بدلول مجموعه نه بدلوي). راځئ وازمویو.')]
    s1, v1 = _side_steps('(a + b) + c', '(a + b) + c', '(a + b) + c', f'({A} + {B}) + {C}')
    s2, v2 = _side_steps('a + (b + c)', 'a + (b + c)', 'a + (b + c)', f'{A} + ({B} + {C})')
    steps += s1 + s2 + [S(f'Both give {v1}, so the Associative Law is verified.', f'دونوں کا نتیجہ {v1} ہے، اس لیے قانونِ تلازم ثابت ہوا۔', f'دواړه {v1} ورکوي، نو د اتحاد قانون ثابت شو.',
                         m=f'({A} + {B}) + {C} = {A} + ({B} + {C}) = {v1}')]
    return {'steps': steps, 'answer': f'Verified: both sides = {v1}'}


def mul(text, mode='', *_):
    a, b = _ints(text)[:2]
    p = a * b
    sa, sb = ('positive' if a > 0 else 'negative'), ('positive' if b > 0 else 'negative')
    if a == 0 or b == 0:
        return {'steps': [S('Any integer multiplied by 0 gives 0.', 'کسی بھی صحیح عدد کو 0 سے ضرب دینے پر 0 ملتا ہے۔', 'هر تام عدد په 0 کې ضرب 0 ورکوي.', m=f'({a}) \\times ({b}) = 0')], 'answer': '0'}
    steps = []
    if mode == 'nl' and not (a < 0 and b < 0):
        count, step = (b, a) if b > 0 else (a, b)
        pts = [step * k for k in range(count + 1)]
        arcs = ' | '.join(f'{pts[i]}>{pts[i + 1]} above' for i in range(count))
        steps.append(S(f'Multiplication is repeated addition: {count} jumps of {step} starting from 0.', f'ضرب بار بار جمع ہے: 0 سے شروع کر کے {step} کی {count} چھلانگیں۔',
                       f'ضرب تکراري جمع ده: له 0 څخه پیل کړئ او د {step} {count} کودونه وکړئ.',
                       m=' + '.join(f'({step})' for _ in range(count)) + f' = {p}',
                       svg=figs.nline(f'{min(pts + [0]) - 1}..{max(pts + [0]) + 1} | circ={p} | {arcs}')))
    elif mode == 'nl':
        steps.append(S('Two negative integers are hard to show on a number line (as the textbook says), so we use the sign rule.', 'دو منفی صحیح اعداد کو عددی لائن پر دکھانا مشکل ہے (جیسا کہ کتاب میں ہے)، اس لیے ہم علامت کا قاعدہ استعمال کرتے ہیں۔',
                       'دوه منفي تام عددونه په عددي کرښه ښودل ستونزمن دي (لکه څنګه چې په کتاب کې دي)، نو د نښې قاعده کاروو.'))
    steps.append(S(f'Step 1 – multiply the absolute values: {abs(a)} × {abs(b)} = {abs(p)}.', f'مرحلہ 1 – مطلق قیمتیں ضرب دیں: {abs(a)} × {abs(b)} = {abs(p)}۔', f'لومړی پړاو – مطلق ارزښتونه ضرب کړئ: {abs(a)} × {abs(b)} = {abs(p)}.', m=rf'|{a}| \times |{b}| = {abs(a)} \times {abs(b)} = {abs(p)}'))
    if (a > 0) == (b > 0):
        rule = ('Both are ' + sa + ', same signs, so the product is positive.', f'دونوں {"مثبت" if a > 0 else "منفی"} ہیں، علامتیں یکساں ہیں، اس لیے حاصلِ ضرب مثبت ہے۔', f'دواړه {"مثبت" if a > 0 else "منفي"} دي، نښې یو شان دي، نو حاصل ضرب مثبت دی.')
    else:
        rule = ('One is positive and the other is negative, opposite signs, so the product is negative.', 'ایک مثبت اور دوسرا منفی ہے، علامتیں مخالف ہیں، اس لیے حاصلِ ضرب منفی ہے۔', 'یو مثبت او بل منفي دی، نښې مخالفې دي، نو حاصل ضرب منفي دی.')
    steps.append(S('Step 2 – decide the sign. ' + rule[0], 'مرحلہ 2 – علامت طے کریں۔ ' + rule[1], 'دوهم پړاو – نښه وټاکئ. ' + rule[2]))
    steps.append(S(f'So the product is {p:+d}.', f'لہٰذا حاصلِ ضرب {p:+d} ہے۔', f'نو حاصل ضرب {p:+d} دی.', m=f'({a}) \\times ({b}) = {p}'))
    return {'steps': steps, 'answer': f'{p:+d}'}


def comm_mul(text):
    a, b = _ints(text)[:2]
    p = a * b
    steps = [S('Commutative Law under multiplication: a × b = b × a (changing the order does not change the product).',
               'ضرب کے تحت قانونِ مبادلہ: a × b = b × a (ترتیب بدلنے سے حاصلِ ضرب نہیں بدلتا)۔',
               'د ضرب لاندې د تبادلې قانون: a × b = b × a (د ترتیب بدلول حاصل ضرب نه بدلوي).'),
             S(f'a × b = ({a}) × ({b}) = {p}', f'a × b = ({a}) × ({b}) = {p}', f'a × b = ({a}) × ({b}) = {p}', m=rf'({a}) \times ({b}) = {p}'),
             S(f'b × a = ({b}) × ({a}) = {p}', f'b × a = ({b}) × ({a}) = {p}', f'b × a = ({b}) × ({a}) = {p}', m=rf'({b}) \times ({a}) = {p}'),
             S(f'Both products are {p}, so the Commutative Law is verified.', f'دونوں حاصلِ ضرب {p} ہیں، اس لیے قانونِ مبادلہ ثابت ہوا۔', f'دواړه حاصل ضربونه {p} دي، نو د تبادلې قانون ثابت شو.')]
    return {'steps': steps, 'answer': f'Verified: both sides = {p}'}


def assoc_mul(text):
    a, b, c = _ints(text)[:3]
    ab, bc, p = a * b, b * c, a * b * c
    steps = [S('Associative Law under multiplication: (a × b) × c = a × (b × c).', 'ضرب کے تحت قانونِ تلازم: (a × b) × c = a × (b × c)۔', 'د ضرب لاندې د اتحاد قانون: (a × b) × c = a × (b × c).'),
             S('Left side: multiply the first two, then the third.', 'بایاں طرف: پہلے دو کو ضرب دیں، پھر تیسرے سے۔', 'کیڼ اړخ: لومړي دوه ضرب کړئ، بیا په درېیم کې.',
               m=rf'[({a}) \times ({b})] \times ({c}) = ({ab}) \times ({c}) = {p}'),
             S('Right side: multiply the last two, then the first.', 'دایاں طرف: آخری دو کو ضرب دیں، پھر پہلے سے۔', 'ښي اړخ: وروستي دوه ضرب کړئ، بیا په لومړي کې.',
               m=rf'({a}) \times [({b}) \times ({c})] = ({a}) \times ({bc}) = {p}'),
             S(f'Both sides are {p}, so the Associative Law is verified.', f'دونوں طرف {p} ہیں، اس لیے قانونِ تلازم ثابت ہوا۔', f'دواړه اړخونه {p} دي، نو د اتحاد قانون ثابت شو.')]
    return {'steps': steps, 'answer': f'Verified: both sides = {p}'}


def inverse(text, *_):
    t = _norm(text)
    m = re.search(r'\\frac\{\s*([+\-]?\d+)\s*\}\{\s*([+\-]?\d+)\s*\}', t)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        shown = rf'\frac{{{a}}}{{{b}}}'
    else:
        a, b = _ints(text)[0], 1
        shown = str(a)
    num, den = b, a
    if den < 0:
        num, den = -num, -den
    inv = str(num) if den == 1 else rf'\frac{{{num}}}{{{den}}}' if num > 0 else rf'-\frac{{{-num}}}{{{den}}}'
    steps = [S('The multiplicative inverse (reciprocal) is the number that gives 1 when multiplied by the given number. Just turn the number upside down (an integer n is n/1).',
               'ضربی معکوس (مقلوب) وہ عدد ہے جسے دیے گئے عدد سے ضرب دینے پر 1 ملے۔ عدد کو الٹ دیں (صحیح عدد n کو n/1 سمجھیں)۔',
               'ضربي معکوس (معکوس کسر) هغه عدد دی چې له ورکړل شوي عدد سره ضرب 1 ورکوي. عدد سرچپه کړئ (تام عدد n لکه n/1 وګڼئ).'),
             S('Flip the numerator and denominator; keep the sign.', 'شمار کنندہ اور نسب نما کو الٹ دیں؛ علامت وہی رہے۔', 'صورت او مخرج سرچپه کړئ؛ نښه همغه پاتې شي.', m=f'{shown} \\;\\longrightarrow\\; {inv}'),
             S('Check: the product is 1.', 'جانچ: حاصلِ ضرب 1 ہے۔', 'ازموینه: حاصل ضرب 1 دی.', m=rf'{shown} \times {inv} = 1')]
    return {'steps': steps, 'answer': f'${inv}$'}


def div(text, *_):
    a, b = _ints(text)[:2]
    if a == 0:
        return {'steps': [S(f'0 divided by any non-zero integer is always 0 (0 shared into {abs(b)} parts gives nothing in each part).',
                            f'0 کو کسی بھی غیر صفر صحیح عدد سے تقسیم کرنے پر ہمیشہ 0 ملتا ہے (0 کو {abs(b)} حصوں میں بانٹنے سے ہر حصے میں کچھ نہیں آتا)۔',
                            f'0 پر هر غیر صفري تام عدد وېشل تل 0 ورکوي (0 په {abs(b)} برخو وېشل په هره برخه کې هېڅ نه ورکوي).', m=f'0 \\div ({b}) = 0')],
                'answer': '0'}
    q = a // b if a % b == 0 else a / b
    steps = [S(f'Step 1 – divide the absolute values: {abs(a)} ÷ {abs(b)} = {abs(q)}.', f'مرحلہ 1 – مطلق قیمتیں تقسیم کریں: {abs(a)} ÷ {abs(b)} = {abs(q)}۔', f'لومړی پړاو – مطلق ارزښتونه ووېشئ: {abs(a)} ÷ {abs(b)} = {abs(q)}.',
               m=rf'|{a}| \div |{b}| = {abs(a)} \div {abs(b)} = {abs(q)}')]
    if (a > 0) == (b > 0):
        steps.append(S('Step 2 – both integers have the same sign, so the quotient is positive.', 'مرحلہ 2 – دونوں صحیح اعداد کی علامت ایک جیسی ہے، اس لیے خارجِ قسمت مثبت ہے۔', 'دوهم پړاو – د دواړو تامو عددونو نښه یو شان ده، نو خارج قسمت مثبت دی.'))
    else:
        steps.append(S('Step 2 – the integers have different signs, so the quotient is negative.', 'مرحلہ 2 – صحیح اعداد کی علامتیں مختلف ہیں، اس لیے خارجِ قسمت منفی ہے۔', 'دوهم پړاو – د تامو عددونو نښې بېلې دي، نو خارج قسمت منفي دی.'))
    steps.append(S(f'Check with multiplication: ({b}) × ({q}) = {a}.', f'ضرب سے جانچیں: ({b}) × ({q}) = {a}۔', f'په ضرب یې وازمویئ: ({b}) × ({q}) = {a}.', m=rf'({a}) \div ({b}) = {q:+d}' if isinstance(q, int) else rf'({a}) \div ({b}) = {q}'))
    return {'steps': steps, 'answer': f'{q:+d}' if isinstance(q, int) else str(q)}


from fractions import Fraction as _F

_BR = {'(': ')', '{': '}', '[': ']', '<': '>'}
_BRNAME = {'(': ('parentheses', 'گول قوسین', 'ګردو قوسونو'), '{': ('curly brackets', 'منحنی قوسین', 'ګونجو قوسونو'),
           '[': ('square brackets', 'مربع قوسین', 'مربع قوسونو'), '<': ('vinculum (bar)', 'وِنکیولم (لکیر)', 'وینکولم (کرښې)')}
_OPNAME = {':': ('divide', 'تقسیم کریں', 'ووېشئ'), '*': ('multiply', 'ضرب دیں', 'ضرب کړئ'),
           '+': ('add', 'جمع کریں', 'جمع کړئ'), '-': ('subtract', 'تفریق کریں', 'تفریق کړئ')}


def _btok(src):
    """Tokens: ('n', Fraction, style) | ('op', c) | ('o', c) | ('c', c). Syntax: 17&1/2 mixed, 3/4 fraction, 2.5 decimal, ':' divide, '*' times, <..> vinculum."""
    toks, i = [], 0
    src = _norm(src)
    while i < len(src):
        ch = src[i]
        if ch.isspace():
            i += 1
            continue
        m = re.match(r'(\d+)&(\d+)/(\d+)|(\d+)/(\d+)|(\d+\.\d+)|(\d+)', src[i:])
        if m and m.start() == 0:
            if m.group(1):
                toks.append(('n', int(m.group(1)) + _F(int(m.group(2)), int(m.group(3))), 'mixed'))
            elif m.group(4):
                toks.append(('n', _F(int(m.group(4)), int(m.group(5))), 'frac'))
            elif m.group(6):
                toks.append(('n', _F(m.group(6)), 'dec'))
            else:
                toks.append(('n', _F(int(m.group(7))), 'int'))
            i += m.end()
            continue
        if ch in _BR:
            toks.append(('o', ch))
        elif ch in _BR.values():
            toks.append(('c', ch))
        elif ch in '+-*:':
            toks.append(('op', ch))
        else:
            raise ValueError('bad char ' + ch)
        i += 1
    return toks


def _fmt(v, style, latex=True, decmode=False):
    if v.denominator == 1:
        return str(v.numerator)
    if decmode or style == 'dec':
        d = v.denominator
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5
        if d == 1:
            s = f'{float(v):.10f}'.rstrip('0').rstrip('.')
            return s
    if style == 'mixed' and v > 1:
        w = v.numerator // v.denominator
        r = v - w
        return f'{w}\\frac{{{r.numerator}}}{{{r.denominator}}}' if latex else f'{w} {r.numerator}/{r.denominator}'
    return f'\\frac{{{v.numerator}}}{{{v.denominator}}}' if latex else f'{v.numerator}/{v.denominator}'


def _btex(toks, decmode):
    out = []
    for t in toks:
        if t[0] == 'n':
            out.append(_fmt(t[1], t[2], True, decmode))
        elif t[0] == 'op':
            out.append({'+': '+', '-': '-', '*': r'\times', ':': r'\div'}[t[1]])
        elif t[0] == 'o':
            out.append({'(': '(', '{': r'\{', '[': '[', '<': r'\overline{'}[t[1]])
        else:
            out.append({')': ')', '}': r'\}', ']': ']', '>': '}'}[t[1]])
    return ' '.join(out).replace(r'\overline{ ', r'\overline{')


def bodmas(text, *_):
    toks = _btok(text)
    decmode = not any(t[0] == 'n' and t[2] in ('frac', 'mixed') for t in toks)
    steps = [S('Follow BODMAS: start with the innermost bracket (bar, then ( ), then { }, then [ ]). Inside a bracket: divide, then multiply, then add and subtract from left to right.',
               'BODMAS پر عمل کریں: سب سے اندر والے قوسین سے شروع کریں (لکیر، پھر ( )، پھر { }، پھر [ ])۔ قوسین کے اندر: پہلے تقسیم، پھر ضرب، پھر بائیں سے دائیں جمع اور تفریق۔',
               'BODMAS تعقیب کړئ: له تر ټولو دننه قوس پیل وکړئ (کرښه، بیا ( )، بیا { }، بیا [ ]). د قوس دننه: لومړی وېش، بیا ضرب، بیا له کیڼ څخه ښي ته جمع او تفریق.',
               m=_btex(toks, decmode))]
    for _ in range(80):
        # find innermost group
        start, end, kind = None, len(toks), None
        stack = []
        for i, t in enumerate(toks):
            if t[0] == 'o':
                stack.append(i)
            elif t[0] == 'c':
                start = stack.pop()
                end = i
                kind = toks[start][1]
                break
        lo, hi = (start + 1, end) if start is not None else (0, len(toks))
        seg = toks[lo:hi]
        if len(seg) == 1 and start is not None:
            toks = toks[:start] + seg + toks[end + 1:]
            continue
        if len(seg) == 1:
            break
        ops = [(j, s[1]) for j, s in enumerate(seg) if s[0] == 'op']
        pick = next((j for j, o in ops if o == ':'), None)
        if pick is None:
            pick = next((j for j, o in ops if o == '*'), None)
        if pick is None:
            pick = ops[0][0]
        a, op, b = seg[pick - 1], seg[pick][1], seg[pick + 1]
        r = {'+': a[1] + b[1], '-': a[1] - b[1], '*': a[1] * b[1], ':': a[1] / b[1]}[op]
        style = 'dec' if decmode else ('frac' if r.denominator != 1 else 'int')
        new = ('n', r, style)
        sa, sb, sr = (_fmt(x, st, False, decmode) for x, st in ((a[1], a[2]), (b[1], b[2]), (r, style)))
        sym = {'+': '+', '-': '−', '*': '×', ':': '÷'}[op]
        where = _BRNAME[kind] if kind else ('the remaining expression', 'باقی عبارت', 'پاتې افاده')
        extra_en = extra_ur = extra_ps = ''
        if op == ':' and b[1].denominator != 1:
            extra_en, extra_ur, extra_ps = (' (to divide by a fraction, multiply by its reciprocal)', ' (کسر سے تقسیم کرنے کے لیے اس کے مقلوب سے ضرب دیں)', ' (پر کسر د وېش لپاره یې په معکوس کې ضرب کړئ)')
        en = f'In the {where[0]}, {_OPNAME[op][0]}: {sa} {sym} {sb} = {sr}{extra_en}.' if kind else f'Now {_OPNAME[op][0]}: {sa} {sym} {sb} = {sr}{extra_en}.'
        ur = f'{where[1]} میں {_OPNAME[op][1]}: {sa} {sym} {sb} = {sr}{extra_ur}۔' if kind else f'اب {_OPNAME[op][1]}: {sa} {sym} {sb} = {sr}{extra_ur}۔'
        ps = f'په {where[2]} کې {_OPNAME[op][2]}: {sa} {sym} {sb} = {sr}{extra_ps}.' if kind else f'اوس {_OPNAME[op][2]}: {sa} {sym} {sb} = {sr}{extra_ps}.'
        seg = seg[:pick - 1] + [new] + seg[pick + 2:]
        toks = toks[:lo] + seg + toks[hi:]
        steps.append(S(en, ur, ps, m='= ' + _btex(toks, decmode)))
    v = toks[0][1]
    if v.denominator != 1 and not decmode and abs(v) > 1:
        w = int(v.numerator / v.denominator)
        r = abs(v - w)
        final = f'{w}\\frac{{{r.numerator}}}{{{r.denominator}}}'
        steps.append(S('Change the improper fraction into a mixed number.', 'غیر واجب کسر کو مخلوط عدد میں بدلیں۔', 'ناسم کسر په ګډ عدد بدل کړئ.', m=f'{_fmt(v, "frac")} = {final}'))
    else:
        final = _fmt(v, 'frac', True, decmode)
    return {'steps': steps, 'answer': f'${final}$'}


def _num(s):
    s = s.strip()
    m = re.fullmatch(r'(\d+)\s*\\frac\{(\d+)\}\{(\d+)\}', s)
    if m:
        return int(m.group(1)) + _F(int(m.group(2)), int(m.group(3))), s
    return _F(s), s


def _dec(v, places=2):
    if v.denominator == 1:
        return str(v.numerator)
    d = v.denominator
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    if d == 1:
        return f'{float(v):.10f}'.rstrip('0').rstrip('.')
    return f'{float(v):.{places}f}'


def _term(v):
    d = v.denominator
    for q in (2, 5):
        while d % q == 0:
            d //= q
    return d == 1


def pctof(text, *_):
    """'15 % of 35', '67\\frac{1}{7}% of 780', '9.25% of Rs 300' -> value."""
    t = text.replace('$', '')
    m = re.search(r'([\d.]+(?:\s*\\frac\{\d+\}\{\d+\})?)\s*%\s*of\s*(Rs\s*)?([\d.]+)\s*(.*)', t)
    p, ptxt = _num(m.group(1))
    rs, total, unit = m.group(2), _F(m.group(3)), m.group(4).strip()
    v = p * total / 100
    pre = 'Rs ' if rs else ''
    suf = f' {unit}' if unit else ''
    ptex = ptxt if '\\frac' in ptxt else _dec(p)
    steps = [S('"Percent" means "out of 100", and "of" means multiply. So write the percentage as a fraction over 100 and multiply by the quantity.',
               '"فیصد" کا مطلب ہے "100 میں سے" اور "کا" کا مطلب ضرب ہے۔ اس لیے فیصد کو 100 کے نسب نما والے کسر میں لکھیں اور مقدار سے ضرب دیں۔',
               '"سلنه" یعنې "له 100 څخه" او "د" یعنې ضرب. نو سلنه د 100 مخرج لرونکي کسر په بڼه ولیکئ او په مقدار کې یې ضرب کړئ.',
               m=rf'{ptex}\% \text{{ of }} {pre}{_dec(total)} = \frac{{{ptex}}}{{100}} \times {_dec(total)}')]
    if p.denominator != 1 and '\\frac' in ptxt:
        steps.append(S(f'First change the mixed number into an improper fraction: {ptxt.replace(chr(92) + "frac", "")} = {p.numerator}/{p.denominator}.',
                       f'پہلے مخلوط عدد کو غیر واجب کسر میں بدلیں: {p.numerator}/{p.denominator}۔', f'لومړی ګډ عدد په ناسم کسر بدل کړئ: {p.numerator}/{p.denominator}.',
                       m=rf'{ptxt} = \frac{{{p.numerator}}}{{{p.denominator}}}'))
        steps.append(S('Multiply and simplify.', 'ضرب دیں اور سادہ کریں۔', 'ضرب یې کړئ او ساده یې کړئ.',
                       m=rf'\frac{{{p.numerator}}}{{{p.denominator} \times 100}} \times {_dec(total)} = {_dec(v)}'))
    else:
        steps.append(S('Multiply and simplify.', 'ضرب دیں اور سادہ کریں۔', 'ضرب یې کړئ او ساده یې کړئ.', m=rf'\frac{{{ptex} \times {_dec(total)}}}{{100}} = \frac{{{_dec(p * total)}}}{{100}} = {_dec(v)}'))
    approx = '' if _term(v) else '≈ '
    steps.append(S(f'So, {ptex}% of {pre}{_dec(total)}{suf} = {approx}{pre}{_dec(v)}{suf}.', f'لہٰذا {pre}{_dec(total)}{suf} کا {ptex}% = {pre}{_dec(v)}{suf}۔', f'نو د {pre}{_dec(total)}{suf} {ptex}% = {pre}{_dec(v)}{suf}.'))
    return {'steps': steps, 'answer': f'{approx}{pre}{_dec(v)}{suf}'}


def pct(text, *_):
    """'50 out of 600' -> percentage."""
    t = text.replace('$', '')
    m = re.search(r'(Rs\s*)?([\d.]+)\s*(\w*)\s*out\s*(?:of)?\s*(Rs\s*)?([\d.]+)', t)
    a, b = _F(m.group(2)), _F(m.group(5))
    v = a / b * 100
    exact = _term(v)
    steps = [S(f'Write it as a fraction: {_dec(a)} out of {_dec(b)} = {_dec(a)}/{_dec(b)}.', f'اسے کسر کی صورت میں لکھیں: {_dec(b)} میں سے {_dec(a)} = {_dec(a)}/{_dec(b)}۔',
               f'د کسر په بڼه یې ولیکئ: له {_dec(b)} څخه {_dec(a)} = {_dec(a)}/{_dec(b)}.', m=rf'\frac{{{_dec(a)}}}{{{_dec(b)}}}'),
             S('Multiply the fraction by 100 and put the % sign.', 'کسر کو 100 سے ضرب دیں اور % کی علامت لگائیں۔', 'کسر په 100 کې ضرب کړئ او د % نښه ولګوئ.',
               m=rf'\frac{{{_dec(a)}}}{{{_dec(b)}}} \times 100\% = {_dec(v)}\%' if exact else rf'\frac{{{_dec(a)}}}{{{_dec(b)}}} \times 100\% = \frac{{{v.numerator}}}{{{v.denominator}}}\% \approx {_dec(v)}\%')]
    return {'steps': steps, 'answer': f'{_dec(v)}%' if exact else f'≈ {_dec(v)}%'}


def colourpct(text, *_):
    p = int(re.search(r'\d+', text).group())
    full, rest = divmod(p, 10)
    rects = []
    if full:
        rects.append(f'#22c55e:1-{full}:1-10')
    if rest:
        rects.append(f'#22c55e:{full + 1}-{full + 1}:1-{rest}')
    steps = [S(f'{p}% means {p} out of 100, so colour {p} of the 100 small squares.', f'{p}% کا مطلب ہے 100 میں سے {p}، اس لیے 100 چھوٹے مربعوں میں سے {p} رنگیں۔',
               f'{p}% یعنې له 100 څخه {p}، نو له 100 کوچنیو مربعو {p} رنګ کړئ.'),
             S(f'Each column has 10 squares: colour {full} full column{"s" if full != 1 else ""}' + (f' and {rest} more square{"s" if rest != 1 else ""}.' if rest else '.'),
               f'ہر کالم میں 10 مربع ہیں: {full} پورے کالم' + (f' اور {rest} مزید مربع رنگیں۔' if rest else ' رنگیں۔'),
               f'په هره ستنه کې 10 مربعات دي: {full} بشپړې ستنې' + (f' او {rest} نور مربعات رنګ کړئ.' if rest else ' رنګ کړئ.'),
               svg=grid('10x10 | ' + ' ; '.join(rects)))]
    return {'steps': steps, 'answer': f'{p} squares coloured'}


def comparepct(text, *_):
    """'22 out of 60 and 54 out of 60' -> which is greater as a percentage."""
    pairs = [(a.rstrip('.'), b.rstrip('.')) for a, b in re.findall(r'(\d+(?:\.\d+)?)\s*out\s*(?:of)?\s*(\d+(?:\.\d+)?)', text)]
    vals = []
    steps = [S('Change each quantity into a percentage, then compare the percentages.', 'ہر مقدار کو فیصد میں بدلیں، پھر فیصد کا موازنہ کریں۔', 'هر مقدار په سلنه بدل کړئ، بیا سلنې پرتله کړئ.')]
    for a, b in pairs:
        r = pct(f'{a} out of {b}')
        v = _F(a) / _F(b) * 100
        vals.append((v, f'{a} out of {b}', r['answer']))
        steps.append(S(f'{a} out of {b}:', f'{b} میں سے {a}:', f'له {b} څخه {a}:', m=r['steps'][1]['m']))
    vals_sorted = sorted(vals, key=lambda x: x[0], reverse=True)
    if vals_sorted[0][0] == vals_sorted[-1][0]:
        steps.append(S('The percentages are equal.', 'فیصد برابر ہیں۔', 'سلنې برابرې دي.'))
        ans = 'Both are equal'
    else:
        order = ' > '.join(x[2] for x in vals_sorted)
        steps.append(S(f'Compare: {order}. So "{vals_sorted[0][1]}" is the greatest as a percentage.', f'موازنہ: {order}۔ لہٰذا "{vals_sorted[0][1]}" فیصد کے لحاظ سے سب سے زیادہ ہے۔',
                       f'پرتله: {order}. نو "{vals_sorted[0][1]}" د سلنې له مخې تر ټولو ډېر دی.'))
        ans = f'{vals_sorted[0][1]} ({vals_sorted[0][2]}) is greater'
    return {'steps': steps, 'answer': ans}


def change(text, *_):
    """'500 decreased by 17%' / '18% increase in 1350'."""
    t = text.replace('$', '')
    m = re.search(r'([\d.]+)\s*(increased|decreased)\s*by\s*([\d.]+)\s*%', t)
    if m:
        base, kind, p = _F(m.group(1)), m.group(2)[:8], _F(m.group(3))
    else:
        m = re.search(r'([\d.]+)\s*%\s*(increase|decrease)\s*in\s*([\d.]+)', t)
        p, kind, base = _F(m.group(1)), m.group(2), _F(m.group(3))
    up = kind.startswith('increase')
    amt = p * base / 100
    new = base + amt if up else base - amt
    word = ('increase', 'اضافہ', 'زیاتوالی') if up else ('decrease', 'کمی', 'کموالی')
    steps = [S(f'Step 1 – find the {word[0]}: {_dec(p)}% of {_dec(base)}.', f'مرحلہ 1 – {word[1]} معلوم کریں: {_dec(base)} کا {_dec(p)}%۔', f'لومړی پړاو – {word[2]} معلوم کړئ: د {_dec(base)} {_dec(p)}%.',
               m=rf'\frac{{{_dec(p)}}}{{100}} \times {_dec(base)} = {_dec(amt)}'),
             S(f'Step 2 – {"add it to" if up else "subtract it from"} the original quantity.', f'مرحلہ 2 – اسے اصل مقدار {"میں جمع کریں" if up else "میں سے تفریق کریں"}۔',
               f'دوهم پړاو – دا له اصلي مقدار {"سره جمع کړئ" if up else "څخه تفریق کړئ"}.', m=f'{_dec(base)} {"+" if up else "-"} {_dec(amt)} = {_dec(new)}')]
    return {'steps': steps, 'answer': f'{word[0].capitalize()} = {_dec(amt)}; new value = {_dec(new)}'}


def ratio(text, *_):
    """'35 to 55' / '4 : 8' / '3.1 : 6.2' -> simplest form a : b."""
    a, b = [_F(x) for x in re.findall(r'\d+(?:\.\d+)?', re.sub(r'(\d)\s*\.\s*(\d)', r'\1.\2', text))[:2]]
    steps = [S(f'Write the ratio: {_dec(a)} : {_dec(b)}.', f'نسبت لکھیں: {_dec(a)} : {_dec(b)}۔', f'نسبت ولیکئ: {_dec(a)} : {_dec(b)}.', m=f'{_dec(a)} : {_dec(b)}')]
    if a.denominator != 1 or b.denominator != 1:
        k = 10 ** max(len(_dec(a).split('.')[-1]) if '.' in _dec(a) else 0, len(_dec(b).split('.')[-1]) if '.' in _dec(b) else 0)
        a, b = a * k, b * k
        steps.append(S(f'Remove the decimals: multiply both terms by {k}.', f'اعشاریہ ختم کریں: دونوں ارکان کو {k} سے ضرب دیں۔', f'اعشاریې لرې کړئ: دواړه حدونه په {k} کې ضرب کړئ.', m=f'{_dec(a)} : {_dec(b)}'))
    a, b = int(a), int(b)
    g = gcd(a, b)
    if g > 1:
        steps.append(S(f'The highest common factor of {a} and {b} is {g}. Divide both terms by {g}.', f'{a} اور {b} کا عاد اعظم {g} ہے۔ دونوں ارکان کو {g} سے تقسیم کریں۔',
                       f'د {a} او {b} لوی مشترک قاسم {g} دی. دواړه حدونه پر {g} ووېشئ.', m=rf'\frac{{{a} \div {g}}}{{{b} \div {g}}} = \frac{{{a // g}}}{{{b // g}}}'))
    else:
        steps.append(S(f'{a} and {b} have no common factor other than 1, so the ratio is already in its simplest form.', f'{a} اور {b} کا 1 کے سوا کوئی مشترک جزوِ ضربی نہیں، اس لیے نسبت پہلے ہی سادہ ترین صورت میں ہے۔',
                       f'د {a} او {b} له 1 پرته ګډ ضربي جز نشته، نو نسبت دمخه په تر ټولو ساده بڼه دی.'))
    steps.append(S(f'Simplest form: {a // g} : {b // g}', f'سادہ ترین صورت: {a // g} : {b // g}', f'تر ټولو ساده بڼه: {a // g} : {b // g}', m=f'{a // g} : {b // g}'))
    return {'steps': steps, 'answer': f'{a // g} : {b // g}'}


def rfrac(text, *_):
    a, b = re.findall(r'\d+(?:\s*\.\s*\d+)?', text)[:2]
    a, b = a.replace(' ', ''), b.replace(' ', '')
    steps = [S('The first term (antecedent) becomes the numerator and the second term (consequent) becomes the denominator.', 'پہلا رکن (مقدم) شمار کنندہ اور دوسرا رکن (تالی) نسب نما بن جاتا ہے۔',
               'لومړی حد (مقدم) صورت او دوهم حد (تالي) مخرج کېږي.', m=rf'{a} : {b} = \frac{{{a}}}{{{b}}}')]
    fr = _F(a) / _F(b)
    if (str(fr.numerator), str(fr.denominator)) != (a, b):
        if '.' in a or '.' in b:
            k = 10 ** max(len(x.split('.')[1]) if '.' in x else 0 for x in (a, b))
            ai, bi = int(round(float(a) * k)), int(round(float(b) * k))
            steps.append(S(f'Remove the decimals: multiply both terms by {k}.', f'اعشاریہ ختم کریں: دونوں ارکان کو {k} سے ضرب دیں۔', f'اعشاریه لرې کړئ: دواړه حدونه په {k} کې ضرب کړئ.',
                           m=rf'\frac{{{a}}}{{{b}}} = \frac{{{ai}}}{{{bi}}}'))
            a, b = str(ai), str(bi)
        g = gcd(int(a), int(b))
        if g > 1:
            steps.append(S(f'Write the fraction in its lowest terms: divide the top and bottom by their HCF, {g}.',
                           f'کسر کو مختصر ترین صورت میں لکھیں: شمار کنندہ اور نسب نما کو ان کے عاد اعظم {g} سے تقسیم کریں۔',
                           f'کسر په ساده ترینه بڼه ولیکئ: صورت او مخرج د هغوی پر لوی مشترک قاسم {g} ووېشئ.',
                           m=rf'\frac{{{a} \div {g}}}{{{b} \div {g}}} = \frac{{{fr.numerator}}}{{{fr.denominator}}}'))
        return {'steps': steps, 'answer': rf'$\frac{{{fr.numerator}}}{{{fr.denominator}}}$'}
    return {'steps': steps, 'answer': rf'$\frac{{{a}}}{{{b}}}$'}


def contr(text, names='', *_):
    """'a : b = 4 : 5 and b : c = 5 : 6' -> continued ratio by Method II, then simplest form."""
    nums_ = [int(x) for x in re.findall(r'\d+', re.sub(r'[a-z]\s*:\s*[a-z]', '', text))][:4]
    a1, b1, b2, c2 = nums_
    letters = names.split(',') if names else re.findall(r'\b([a-z])\s*:\s*([a-z])', text)
    if not names:
        letters = [letters[0][0], letters[0][1], letters[1][1]] if len(letters) >= 2 else ['a', 'b', 'c']
    r = [a1 * b2, b1 * b2, b1 * c2]
    g = gcd(gcd(r[0], r[1]), r[2])
    s = [x // g for x in r]
    L = ' : '.join(letters)
    steps = [S(f'The common (middle) term must have the same value in both ratios. Use Method II (cross multiplication).', 'مشترک (درمیانی) رکن کی قیمت دونوں نسبتوں میں ایک جیسی ہونی چاہیے۔ طریقہ II (آڑی ضرب) استعمال کریں۔',
               'ګډ (منځنی) حد باید په دواړو نسبتونو کې یو شان ارزښت ولري. دوهمه طریقه (صلیبي ضرب) وکاروئ.',
               svg=figs.cross(f'{",".join(letters)} | {a1}:{b1} | {b2}:{c2}')),
             S(f'First term = {a1} × {b2} = {r[0]}; middle term = {b1} × {b2} = {r[1]}; last term = {b1} × {c2} = {r[2]}.',
               f'پہلا رکن = {a1} × {b2} = {r[0]}؛ درمیانی رکن = {b1} × {b2} = {r[1]}؛ آخری رکن = {b1} × {c2} = {r[2]}۔',
               f'لومړی حد = {a1} × {b2} = {r[0]}؛ منځنی حد = {b1} × {b2} = {r[1]}؛ وروستی حد = {b1} × {c2} = {r[2]}.', m=f'{L} = {r[0]} : {r[1]} : {r[2]}')]
    if g > 1:
        steps.append(S(f'All three terms can be divided by {g}, so simplify.', f'تینوں ارکان {g} سے تقسیم ہو سکتے ہیں، اس لیے سادہ کریں۔', f'درې واړه حدونه پر {g} وېشل کېږي، نو ساده یې کړئ.', m=f'{L} = {s[0]} : {s[1]} : {s[2]}'))
    return {'steps': steps, 'answer': f'{L} = {s[0]} : {s[1]} : {s[2]}'}


def share(text, *_):
    """'7500 | 4 : 6 : 5' -> share of each part."""
    total_s, rat = text.split('|')
    total = _F(re.search(r'\d+(?:\.\d+)?', total_s.replace(',', '')).group())
    parts = [int(x) for x in re.findall(r'\d+', rat)]
    S_ = sum(parts)
    shares = [total * p / S_ for p in parts]
    steps = [S(f'Add the terms of the ratio: {" + ".join(map(str, parts))} = {S_}.', f'نسبت کے ارکان جمع کریں: {" + ".join(map(str, parts))} = {S_}۔', f'د نسبت حدونه جمع کړئ: {" + ".join(map(str, parts))} = {S_}.')]
    for i, (p, v) in enumerate(zip(parts, shares)):
        steps.append(S(f'Share {i + 1} = {p}/{S_} of {_dec(total)}', f'حصہ {i + 1} = {_dec(total)} کا {p}/{S_}', f'برخه {i + 1} = د {_dec(total)} {p}/{S_}', m=rf'\frac{{{p}}}{{{S_}}} \times {_dec(total)} = {_dec(v)}'))
    steps.append(S(f'Check: {" + ".join(_dec(v) for v in shares)} = {_dec(sum(shares))} ✓', f'جانچ: {" + ".join(_dec(v) for v in shares)} = {_dec(sum(shares))} ✓', f'ازموینه: {" + ".join(_dec(v) for v in shares)} = {_dec(sum(shares))} ✓'))
    return {'steps': steps, 'answer': ', '.join(_dec(v) for v in shares)}


def urate(text, *_):
    """'28 | kilometres | 4 | hour' -> unit rate."""
    a, ua, b, ub = [x.strip() for x in text.split('|')]
    a, b = _F(a), _F(b)
    v = a / b
    steps = [S(f'A unit rate compares with ONE {ub}. Write it as a ratio and divide both terms by {_dec(b)}.', f'اکائی شرح ایک {ub} سے موازنہ کرتی ہے۔ اسے نسبت کی صورت میں لکھیں اور دونوں ارکان کو {_dec(b)} سے تقسیم کریں۔',
               f'واحد نرخ له یوه {ub} سره پرتله کوي. د نسبت په بڼه یې ولیکئ او دواړه حدونه پر {_dec(b)} ووېشئ.',
               m=rf'{_dec(a)} : {_dec(b)} = \frac{{{_dec(a)} \div {_dec(b)}}}{{{_dec(b)} \div {_dec(b)}}} = \frac{{{_dec(v)}}}{{1}}'),
             S(f'So the rate is {_dec(v)} {ua} per {ub}.', f'لہٰذا شرح {_dec(v)} {ua} فی {ub} ہے۔', f'نو نرخ په هر {ub} {_dec(v)} {ua} دی.')]
    return {'steps': steps, 'answer': f'{"" if _term(v) else "≈ "}{_dec(v)} {ua} per {ub}'}


def seq(text, count='3', *_):
    """'4, 9, 14 19' -> term-to-term rule and next terms."""
    v = [int(x) for x in re.findall(r'\d+', text.replace(',', ' , '))]
    n = int(count)
    d = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    if len(set(d)) == 1:
        k = d[0]
        nxt = [v[-1] + k * (i + 1) for i in range(n)]
        rule = (f'add {k}', f'{k} جمع کریں', f'{k} جمع کړئ') if k > 0 else (f'subtract {-k}', f'{-k} تفریق کریں', f'{-k} تفریق کړئ')
        show = ' \\;\\; '.join(f'{v[i]} \\xrightarrow{{{"+" if k > 0 else "-"}{abs(k)}}} {v[i + 1]}' for i in range(min(3, len(v) - 1)))
        how = ('Find the difference between neighbouring terms', 'پڑوسی ارکان کا فرق معلوم کریں', 'د ګاونډیو حدونو توپیر معلوم کړئ')
    else:
        r = _F(v[1], v[0])
        assert all(_F(v[i + 1], v[i]) == r for i in range(len(v) - 1)), 'unknown pattern'
        nxt, cur = [], _F(v[-1])
        for _ in range(n):
            cur = cur * r
            nxt.append(int(cur) if cur.denominator == 1 else cur)
        if r > 1:
            rule = (f'multiply by {r}', f'{r} سے ضرب دیں', f'په {r} کې ضرب کړئ')
            show = ' \\;\\; '.join(f'{v[i]} \\xrightarrow{{\\times {r}}} {v[i + 1]}' for i in range(min(3, len(v) - 1)))
        else:
            q = 1 / r
            rule = (f'divide by {q}', f'{q} سے تقسیم کریں', f'پر {q} ووېشئ')
            show = ' \\;\\; '.join(f'{v[i]} \\xrightarrow{{\\div {q}}} {v[i + 1]}' for i in range(min(3, len(v) - 1)))
        how = ('The differences are not equal, so check multiplying or dividing', 'فرق برابر نہیں، اس لیے ضرب یا تقسیم جانچیں', 'توپیرونه برابر نه دي، نو ضرب یا وېش وازمویئ')
    steps = [S(f'{how[0]}: each term is made from the one before by the same rule.', f'{how[1]}: ہر رکن پچھلے رکن سے ایک ہی قاعدے سے بنتا ہے۔', f'{how[2]}: هر حد له مخکیني څخه په یوه قاعده جوړېږي.', m=show),
             S(f'Term-to-term rule: start at {v[0]} and {rule[0]} each time.', f'رکن سے رکن کا قاعدہ: {v[0]} سے شروع کریں اور ہر بار {rule[1]}۔', f'له حد څخه حد ته قاعده: له {v[0]} پیل وکړئ او هر ځل {rule[2]}.'),
             S('Apply the rule to the last term again and again.', 'قاعدہ آخری رکن پر بار بار لگائیں۔', 'قاعده په وروستي حد بیا بیا پلي کړئ.', m=', '.join(map(str, v)) + ', ' + ', '.join(f'\\mathbf{{{x}}}' for x in nxt))]
    return {'steps': steps, 'answer': f'Rule: {rule[0]}; next terms: ' + ', '.join(map(str, nxt))}


def evalx(text, *_):
    """'LATEX ;; PYEXPR ;; x=2, y=-2' -> substitute and simplify step by step (BODMAS chain)."""
    tex, py, vs = [x.strip() for x in text.split(';;')]
    vals = dict((k.strip(), int(v)) for k, v in (p.split('=') for p in vs.split(',')))
    sub_tex = re.sub(r'(\\[a-zA-Z]+)|([a-zA-Z])', lambda m: m.group(1) if m.group(1) else (f'({vals[m.group(2)]})' if m.group(2) in vals else m.group(2)), tex)
    sub_tex = re.sub(r'(\d|\))\(', r'\1 \\times (', sub_tex)
    sub_tex = re.sub(r'\)\s*\(', r') \\times (', sub_tex)
    py_sub = re.sub(r'\b([a-zA-Z])\b', lambda m: f'({vals[m.group(1)]})' if m.group(1) in vals else m.group(1), py)
    def pw(m):
        base, e = m.group(1), int(m.group(2))
        return '(' + '*'.join([base] * e) + ')'
    for _ in range(5):
        py_sub = re.sub(r'(\(-?\d+\)|\d+)\*\*(\d+)', pw, py_sub)
    states = _reduce(py_sub)
    val = _val(py_sub)
    steps = [S('Replace each variable by its given value. Put negative values in brackets so the signs stay correct.',
               'ہر متغیر کی جگہ اس کی دی گئی قیمت رکھیں۔ منفی قیمتوں کو قوسین میں رکھیں تاکہ علامتیں درست رہیں۔',
               'د هر متحول پر ځای ورکړل شوی ارزښت کېږدئ. منفي ارزښتونه په قوسونو کې کېږدئ چې نښې سمې پاتې شي.', m=sub_tex),
             S('Powers mean repeated multiplication. Now simplify using BODMAS (brackets first, then ×/÷, then +/−).',
               'طاقت کا مطلب بار بار ضرب ہے۔ اب BODMAS سے سادہ کریں (پہلے قوسین، پھر ×/÷، پھر +/−)۔',
               'توان یعنې تکراري ضرب. اوس د BODMAS په مرسته ساده کړئ (لومړی قوسونه، بیا ×/÷، بیا +/−).',
               m=' = '.join(_show(s) for s in states[:1] + states[1:])),
             S(f'The value of the expression is {val}.', f'عبارت کی قیمت {val} ہے۔', f'د افادې ارزښت {val} دی.', m=f'= {val}')]
    return {'steps': steps, 'answer': str(val)}


def _alg_terms(expr):
    """'4ab + b^2 - 2' -> [(coef Fraction, key 'ab', display 'ab')]; key normalises variable order (yx^2 -> x^2y)."""
    e = expr.replace('$', '').replace('–', '-').replace('−', '-').replace(' ', '')
    e = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}', r'(\1/\2)', e)
    if e and e[0] not in '+-':
        e = '+' + e
    out = []
    for sign, body in re.findall(r'([+-])([^+-]+)', e):
        m = re.match(r'(\(\d+/\d+\)|\d+(?:\.\d+)?)?(.*)', body)
        c = m.group(1)
        coef = _F(c.strip('()')) if c else _F(1)
        if sign == '-':
            coef = -coef
        var = m.group(2)
        factors = re.findall(r'([a-z])(?:\^\{?(\d+)\}?)?', var)
        powers = {}
        for v, p in factors:
            powers[v] = powers.get(v, 0) + int(p or 1)
        key = ''.join(f'{v}^{p}' if p > 1 else v for v, p in sorted(powers.items()))
        out.append((coef, key))
    return out


def _fmt_term(coef, key, first=False):
    disp = re.sub(r'\^(\d+)', r'^{\1}', key)
    a = abs(coef)
    cs = '' if (a == 1 and key) else (str(a.numerator) if a.denominator == 1 else rf'\frac{{{a.numerator}}}{{{a.denominator}}}')
    sign = '-' if coef < 0 else ('' if first else '+')
    return f'{sign} {cs}{disp}'.strip() if not first else f'{sign}{cs}{disp}'


def _fmt_poly(terms):
    terms = [(c, k) for c, k in terms if c != 0]
    if not terms:
        return '0'
    return ' '.join(_fmt_term(c, k, i == 0) for i, (c, k) in enumerate(terms))


def combine(text, *_):
    """'4ab + b^2 ;; ab + 2b^2 - 2' (expressions to add) or with '-;;' for subtraction: 'A -;; B'.
    Also accepts the book's wording: 'A, B, C' (add) and 'X from Y' (Y - X)."""
    text = text.replace('$', '').replace('–', '-').replace('−', '-')
    if ' from ' in text:
        x, y = text.split(' from ')
        text = y + ' -;; ' + x
    text = text.replace(',', ' ;; ')
    text = re.sub(r'\)\s*\+\s*\(', ' ;; ', text).replace('(', '').replace(')', '')
    if '-;;' in text:
        a, b = text.split('-;;')
        a = a.replace(';;', '+')
        ta, tb = _alg_terms(a), [(-c, k) for c, k in _alg_terms(b)]
        steps = [S('To subtract, change the sign of every term of the expression being subtracted, then add.',
                   'تفریق کے لیے تفریق کی جانے والی عبارت کے ہر رکن کی علامت بدلیں، پھر جمع کریں۔',
                   'د تفریق لپاره د تفریق کېدونکې افادې د هر حد نښه بدله کړئ، بیا جمع کړئ.', m=_fmt_poly(ta) + ' ' + ' '.join(_fmt_term(c, k) for c, k in tb))]
        allt = ta + tb
    else:
        parts = [p for p in text.split(';;')]
        allt = [t for p in parts for t in _alg_terms(p)]
        steps = [S('Write all the expressions together (horizontal form).', 'تمام عبارتیں ایک ساتھ لکھیں (افقی صورت)۔', 'ټولې افادې یوځای ولیکئ (افقي بڼه).', m=_fmt_poly(allt))]
    groups, order = {}, []
    for c, k in allt:
        if k not in groups:
            groups[k] = []
            order.append(k)
        groups[k].append(c)
    order = sorted(order, key=lambda k: (k == '', order.index(k)))
    grouped = ' + '.join('(' + ' '.join(_fmt_term(c, k, i == 0) for i, c in enumerate(groups[k])) + ')' for k in order if len(groups[k]) > 1)
    if grouped:
        steps.append(S('Bring the like terms together (same variables with the same powers).', 'یکساں ارکان کو اکٹھا کریں (ایک جیسے متغیرات اور ایک جیسی طاقتیں)۔', 'ورته حدونه یوځای کړئ (یو شان متحولونه په یو شان توانونو).', m=grouped))
    res = [(sum(groups[k]), k) for k in order]
    steps.append(S('Add the coefficients of the like terms; the variables and powers stay the same. Unlike terms are copied as they are.',
                   'یکساں ارکان کے ضارب جمع کریں؛ متغیرات اور طاقتیں وہی رہتی ہیں۔ غیر یکساں ارکان ویسے ہی لکھے جاتے ہیں۔',
                   'د ورته حدونو ضریبونه جمع کړئ؛ متحولونه او توانونه همغه پاتې کېږي. نا ورته حدونه هماغسې لیکل کېږي.', m=_fmt_poly(res)))
    return {'steps': steps, 'answer': f'${_fmt_poly(res)}$'}


def _lin(side, var):
    """Linear side -> (a, b) meaning a*var + b. Supports k(...), x/2, \\frac{x}{2}, \\frac{3}{4}x, decimals."""
    from sympy import sympify, Symbol, expand, Rational, nsimplify
    s = side.replace('$', '').replace('–', '-').replace('−', '-').replace('×', '*').replace('÷', '/')
    s = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'((\1)/(\2))', s)
    s = s.replace('{', '(').replace('}', ')').replace('[', '(').replace(']', ')')
    s = re.sub(r'(\d|\))\s*([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z])\s*\(', r'\1*(', s)
    e = expand(nsimplify(sympify(s, locals={var: Symbol(var)}), rational=True))
    X = Symbol(var)
    return e.coeff(X, 1), e.coeff(X, 0)


def _q(v, dec=False):
    from sympy import Rational
    v = Rational(v)
    if v.q == 1:
        return str(v.p)
    if dec:
        f = float(v)
        if abs(round(f, 4) - f) < 1e-12:
            return f'{f:g}'
    return rf'\frac{{{v.p}}}{{{v.q}}}' if v > 0 else rf'-\frac{{{-v.p}}}{{{v.q}}}'


def _linstr(a, b, var, dec=False):
    if a == 0:
        return _q(b, dec)
    co = '' if a == 1 else '-' if a == -1 else _q(a, dec)
    t = f'{co}{var}'
    if b == 0:
        return t
    return f'{t} {"+" if b > 0 else "-"} {_q(abs(b), dec)}'


def lineq(text, var=None, *_):
    """Solve a linear equation in one variable with balance-method steps and verification."""
    t = text.replace('$', '').strip().rstrip('.')
    dec = '.' in t
    if not (var and var.isalpha() and len(var) == 1):
        var = (re.findall(r'(?<![a-z])([a-z])(?![a-z])', re.sub(r'\\[a-z]+', '', t)) or ['x'])[0]
    lhs, rhs = t.split('=')
    a1, b1 = _lin(lhs, var)
    a2, b2 = _lin(rhs, var)
    A, B = a1 - a2, b2 - b1
    q = lambda v: _q(v, dec)
    steps = [S('Write the equation. Whatever we do to one side, we must do to the other side.',
               'مساوات لکھیں۔ جو عمل ایک طرف کریں وہی دوسری طرف بھی کریں۔',
               'معادله ولیکئ. هر څه چې په یوه اړخ کوو، باید په بل اړخ یې هم وکړو.', m=t)]
    simple_l = _linstr(a1, b1, var, dec)
    if a2 != 0:
        if a2 > 0:
            w = (f'Subtract {_linstr(a2, 0, var, dec)} from both sides to bring all the {var}-terms to the left side.',
                 f'دونوں اطراف سے {_linstr(a2, 0, var, dec)} تفریق کریں تاکہ {var} والے تمام ارکان بائیں طرف آ جائیں۔',
                 f'له دواړو اړخونو {_linstr(a2, 0, var, dec)} تفریق کړئ چې د {var} ټول حدونه کیڼ اړخ ته راشي.')
        else:
            w = (f'Add {_linstr(-a2, 0, var, dec)} to both sides to bring all the {var}-terms to the left side.',
                 f'دونوں اطراف میں {_linstr(-a2, 0, var, dec)} جمع کریں تاکہ {var} والے تمام ارکان بائیں طرف آ جائیں۔',
                 f'دواړو اړخونو ته {_linstr(-a2, 0, var, dec)} ورزیات کړئ چې د {var} ټول حدونه کیڼ اړخ ته راشي.')
        steps.append(S(*w, m=f'{_linstr(A, b1, var, dec)} = {q(b2)}'))
    elif simple_l.replace(' ', '') != lhs.replace(' ', ''):
        steps.append(S('Simplify the left side (open brackets / write fractions as coefficients and add like terms).',
                       'بائیں طرف سادہ کریں (قوسین کھولیں / کسر کو ضارب کے طور پر لکھیں اور یکساں ارکان جمع کریں)۔',
                       'کیڼ اړخ ساده کړئ (قوسونه پرانیزئ / کسرونه د ضریب په توګه ولیکئ او ورته حدونه جمع کړئ).',
                       m=f'{simple_l} = {q(b2)}'))
    if b1 != 0:
        if b1 > 0:
            w = (f'Subtract {q(b1)} from both sides to leave the {var}-term alone.',
                 f'دونوں اطراف سے {q(b1)} تفریق کریں تاکہ {var} والا رکن اکیلا رہ جائے۔',
                 f'له دواړو اړخونو {q(b1)} تفریق کړئ چې د {var} حد یوازې پاتې شي.')
        else:
            w = (f'Add {q(-b1)} to both sides to leave the {var}-term alone.',
                 f'دونوں اطراف میں {q(-b1)} جمع کریں تاکہ {var} والا رکن اکیلا رہ جائے۔',
                 f'دواړو اړخونو ته {q(-b1)} ورزیات کړئ چې د {var} حد یوازې پاتې شي.')
        steps.append(S(*w, m=f'{_linstr(A, 0, var, dec)} = {q(B)}'))
    sol = B / A
    from sympy import Rational
    A_r = Rational(A)
    if A == -1:
        steps.append(S('Multiply both sides by −1.', 'دونوں اطراف کو −1 سے ضرب دیں۔', 'دواړه اړخونه په −1 کې ضرب کړئ.', m=f'{var} = {q(sol)}'))
    elif A != 1 and A_r.q != 1 and not dec:
        steps.append(S(f'Multiply both sides by {q(1 / A)} (the reciprocal of {q(A)}).', f'دونوں اطراف کو {q(1 / A)} ({q(A)} کے معکوس) سے ضرب دیں۔',
                       f'دواړه اړخونه په {q(1 / A)} ({q(A)} معکوس) کې ضرب کړئ.', m=rf'{var} = {q(B)} \times {q(1 / A)} = {q(sol)}'))
    elif A != 1:
        steps.append(S(f'Divide both sides by {q(A)} (the coefficient of {var}).', f'دونوں اطراف کو {q(A)} ({var} کے ضارب) سے تقسیم کریں۔',
                       f'دواړه اړخونه پر {q(A)} (د {var} ضریب) ووېشئ.', m=rf'{var} = \frac{{{q(B)}}}{{{q(A)}}}' + ('' if rf'\frac{{{q(B)}}}{{{q(A)}}}' == q(sol) else f' = {q(sol)}')))
    chk_l = a1 * sol + b1
    chk_r = a2 * sol + b2
    assert chk_l == chk_r
    steps.append(S(f'Check: put {var} = {q(sol)} in the original equation. L.H.S = {q(chk_l)} and R.H.S = {q(chk_r)}, so the answer is correct.',
                   f'جانچ: اصل مساوات میں {var} = {q(sol)} رکھیں۔ بایاں رخ = {q(chk_l)} اور دایاں رخ = {q(chk_r)}، اس لیے جواب درست ہے۔',
                   f'ازموینه: په اصلي معادله کې {var} = {q(sol)} کېږدئ. کیڼ اړخ = {q(chk_l)} او ښی اړخ = {q(chk_r)}، نو ځواب سم دی.',
                   m=rf'\text{{L.H.S}} = {q(chk_l)} = \text{{R.H.S}}'))
    extra = ''
    extra = ''
    if Rational(sol).q != 1:
        f = float(sol)
        if abs(round(f, 4) - f) < 1e-12:
            extra = '' if '.' in q(sol) else f' (= {f:g})'
        else:
            extra = f' (≈ {f:.2f})'
    return {'steps': steps, 'answer': f'${var} = {q(sol)}${extra}'}


def _n(v):
    from decimal import Decimal
    d = Decimal(str(v)).normalize()
    s = format(d, 'f')
    return s


def pathq(text, *_):
    """'L W d in|out unit' -> area of a path/border inside or outside a rectangle (square: L = W)."""
    from decimal import Decimal as D
    L, W, d, mode, unit = text.split()
    L, W, d = D(L), D(W), D(d)
    big = (L + 2 * d, W + 2 * d) if mode == 'out' else (L, W)
    small = (L, W) if mode == 'out' else (L - 2 * d, W - 2 * d)
    A1, A2 = big[0] * big[1], small[0] * small[1]
    u2 = unit + '^2'
    if mode == 'out':
        s1 = S(f'The path is outside, so the large rectangle is {_n(d)} {unit} longer on each side: length = {_n(L)} + 2 × {_n(d)} = {_n(big[0])} {unit}, width = {_n(W)} + 2 × {_n(d)} = {_n(big[1])} {unit}.',
               f'راستہ باہر ہے، اس لیے بڑا مستطیل ہر طرف {_n(d)} {unit} بڑا ہے: لمبائی = {_n(L)} + 2 × {_n(d)} = {_n(big[0])} {unit}، چوڑائی = {_n(W)} + 2 × {_n(d)} = {_n(big[1])} {unit}۔',
               f'لار بهر ده، نو لوی مستطیل په هره خوا {_n(d)} {unit} لوی دی: اوږدوالی = {_n(L)} + 2 × {_n(d)} = {_n(big[0])} {unit}، پلنوالی = {_n(W)} + 2 × {_n(d)} = {_n(big[1])} {unit}.')
    else:
        s1 = S(f'The path is inside, so the small rectangle is {_n(d)} {unit} shorter on each side: length = {_n(L)} − 2 × {_n(d)} = {_n(small[0])} {unit}, width = {_n(W)} − 2 × {_n(d)} = {_n(small[1])} {unit}.',
               f'راستہ اندر ہے، اس لیے چھوٹا مستطیل ہر طرف {_n(d)} {unit} چھوٹا ہے: لمبائی = {_n(L)} − 2 × {_n(d)} = {_n(small[0])} {unit}، چوڑائی = {_n(W)} − 2 × {_n(d)} = {_n(small[1])} {unit}۔',
               f'لار دننه ده، نو کوچنی مستطیل په هره خوا {_n(d)} {unit} کوچنی دی: اوږدوالی = {_n(L)} − 2 × {_n(d)} = {_n(small[0])} {unit}، پلنوالی = {_n(W)} − 2 × {_n(d)} = {_n(small[1])} {unit}.')
    steps = [s1,
             S('Find the area of the large rectangle and of the small rectangle.', 'بڑے اور چھوٹے مستطیل کا رقبہ معلوم کریں۔', 'د لوی او کوچني مستطیل مساحت معلوم کړئ.',
               m=rf'{_n(big[0])} \times {_n(big[1])} = {_n(A1)}\ \text{{{u2}}}, \quad {_n(small[0])} \times {_n(small[1])} = {_n(A2)}\ \text{{{u2}}}'.replace('^2}', '}^2')),
             S('Area of the path = area of large rectangle − area of small rectangle.', 'راستے کا رقبہ = بڑے مستطیل کا رقبہ − چھوٹے مستطیل کا رقبہ۔', 'د لارې مساحت = د لوی مستطیل مساحت − د کوچني مستطیل مساحت.',
               m=rf'{_n(A1)} - {_n(A2)} = {_n(A1 - A2)}\ \text{{{unit}}}^2')]
    return {'steps': steps, 'answer': f'{_n(A1 - A2)} {unit}²'}


def sqrect(text, *_):
    """'sq S unit' or 'rect L W unit' -> area and perimeter."""
    from decimal import Decimal as D
    p = text.split()
    if p[0] == 'sq':
        s, u = D(p[1]), p[2]
        A, P = s * s, 4 * s
        steps = [S('Area of a square = side × side.', 'مربع کا رقبہ = ضلع × ضلع۔', 'د مربع مساحت = ضلع × ضلع.', m=rf'{_n(s)} \times {_n(s)} = {_n(A)}\ \text{{{u}}}^2'),
                 S('Perimeter of a square = 4 × side.', 'مربع کا احاطہ = 4 × ضلع۔', 'د مربع محیط = 4 × ضلع.', m=rf'4 \times {_n(s)} = {_n(P)}\ \text{{{u}}}')]
    else:
        l, w, u = D(p[1]), D(p[2]), p[3]
        A, P = l * w, 2 * (l + w)
        steps = [S('Area of a rectangle = length × width.', 'مستطیل کا رقبہ = لمبائی × چوڑائی۔', 'د مستطیل مساحت = اوږدوالی × پلنوالی.', m=rf'{_n(l)} \times {_n(w)} = {_n(A)}\ \text{{{u}}}^2'),
                 S('Perimeter of a rectangle = 2(length + width).', 'مستطیل کا احاطہ = 2(لمبائی + چوڑائی)۔', 'د مستطیل محیط = 2(اوږدوالی + پلنوالی).', m=rf'2({_n(l)} + {_n(w)}) = 2 \times {_n(l + w)} = {_n(P)}\ \text{{{u}}}')]
    return {'steps': steps, 'answer': f'Area = {_n(A)} {u}², Perimeter = {_n(P)} {u}'}


def solidq(text, kind=None, *_):
    """'cube a unit' or 'cuboid l w h unit' -> volume and total surface area.
    With kind given, text may be the book's wording: '5 cm' or 'l = 21 cm, w = 11 cm, h = 6 cm'."""
    from decimal import Decimal as D
    if kind:
        t = text.replace('$', '')
        nums = re.findall(r'\d+(?:\.\d+)?', t)
        unit = (re.findall(r'\d\s*(cm|mm|m)\b', t) or ['cm'])[0]
        text = f'{kind} {" ".join(nums)} {unit}'
    p = text.split()
    if p[0] == 'cube':
        a, u = D(p[1]), p[2]
        V, A = a * a * a, 6 * a * a
        steps = [S('Volume of a cube = length × length × length.', 'مکعب کا حجم = لمبائی × لمبائی × لمبائی۔', 'د مکعب حجم = اوږدوالی × اوږدوالی × اوږدوالی.',
                   m=rf'{_n(a)} \times {_n(a)} \times {_n(a)} = {_n(V)}\ \text{{{u}}}^3'),
                 S('Surface area of a cube = 6 × (length)², because it has 6 equal square faces.', 'مکعب کا سطحی رقبہ = 6 × (لمبائی)²، کیونکہ اس کے 6 برابر مربع رخ ہیں۔',
                   'د مکعب سطحي مساحت = 6 × (اوږدوالی)²، ځکه 6 برابر مربع مخونه لري.', m=rf'6 \times {_n(a)}^2 = 6 \times {_n(a * a)} = {_n(A)}\ \text{{{u}}}^2')]
    else:
        l, w, h, u = D(p[1]), D(p[2]), D(p[3]), p[4]
        V = l * w * h
        A = 2 * (l * w + l * h + w * h)
        steps = [S('Volume of a cuboid = length × width × height.', 'مکعب نما کا حجم = لمبائی × چوڑائی × اونچائی۔', 'د مستطیلي مکعب حجم = اوږدوالی × پلنوالی × جګوالی.',
                   m=rf'{_n(l)} \times {_n(w)} \times {_n(h)} = {_n(V)}\ \text{{{u}}}^3'),
                 S('Surface area of a cuboid = 2 × [(l × w) + (l × h) + (w × h)].', 'مکعب نما کا سطحی رقبہ = 2 × [(l × w) + (l × h) + (w × h)]۔', 'د مستطیلي مکعب سطحي مساحت = 2 × [(l × w) + (l × h) + (w × h)].',
                   m=rf'2 \times [{_n(l * w)} + {_n(l * h)} + {_n(w * h)}] = 2 \times {_n(l * w + l * h + w * h)} = {_n(A)}\ \text{{{u}}}^2')]
    return {'steps': steps, 'answer': f'Volume = {_n(V)} {u}³, Surface area = {_n(A)} {u}²'}


def pieq(text, *_):
    """'Label=value; Label=value; ...' -> central angles and the pie chart."""
    import figs
    from fractions import Fraction
    items = [(a.strip(), Fraction(b.strip())) for a, b in (x.split('=') for x in text.split(';') if x.strip())]
    total = sum(v for _, v in items)
    tot = _n(float(total)) if total.denominator != 1 else str(total.numerator)
    rows = []
    for lab, v in items:
        ang = v / total * 360
        vs = str(v.numerator) if v.denominator == 1 else _n(float(v))
        a = str(ang.numerator) if ang.denominator == 1 else f'{float(ang):.2f}'.rstrip('0').rstrip('.')
        approx = '' if ang.denominator == 1 else r'\approx '
        rows.append(rf'\text{{{lab}}} & \frac{{{vs}}}{{{tot}}} \times 360^\circ {"=" if not approx else approx} {a}^\circ')
    steps = [S(f'Find the total of all the values: {tot}.', f'تمام قیمتوں کا مجموعہ معلوم کریں: {tot}۔', f'د ټولو ارزښتونو مجموعه ومومئ: {tot}.',
               m=' + '.join(str(v.numerator) if v.denominator == 1 else _n(float(v)) for _, v in items) + f' = {tot}'),
             S('Angle of each sector = (value ÷ total) × 360°.', 'ہر قطاع کا زاویہ = (قیمت ÷ کل) × 360°۔', 'د هر قطاع زاویه = (ارزښت ÷ ټول) × 360°.',
               m=r'\begin{array}{ll} ' + r' \\ '.join(rows) + r' \end{array}'),
             S('Check that the angles add up to 360°, then draw each sector with a protractor, starting from a radius.',
               'جانچیں کہ زاویوں کا مجموعہ 360° ہے، پھر ایک رداس سے شروع کر کے چاندے سے ہر قطاع بنائیں۔',
               'وګورئ چې د زاویو مجموعه 360° ده، بیا له یوې شعاع پیل وکړئ او په زاویه پیما هر قطاع رسم کړئ.')]
    steps[-1]['svg'] = figs.pie('; '.join(f'{lab}={float(v)}' for lab, v in items))
    return {'steps': steps, 'answer': 'Pie chart with angles ' + ', '.join(
        f'{lab} {float(v / total * 360):.2f}'.rstrip('0').rstrip('.') + '°' for lab, v in items)}


def stat(text, kind='mean', *_):
    """'46, 50, 39' with kind mean|median|mode -> worked solution."""
    from fractions import Fraction
    from collections import Counter
    vals = [Fraction(x) for x in re.findall(r'\d+(?:\.\d+)?', text.replace(',', ' '))]
    fmt = lambda v: str(v.numerator) if v.denominator == 1 else _n(float(v))
    n = len(vals)
    if kind == 'mean':
        s = sum(vals)
        m = s / n
        ans = fmt(m) if m.denominator in (1, 2, 4, 5, 8, 10) else f'{float(m):.2f}'
        approx = '=' if m.denominator in (1, 2, 4, 5, 8, 10) else r'\approx'
        steps = [S(f'Add all the values. There are n = {n} values.', f'تمام قیمتیں جمع کریں۔ کل n = {n} قیمتیں ہیں۔', f'ټول ارزښتونه جمع کړئ. ټول n = {n} ارزښتونه دي.',
                   m=' + '.join(fmt(v) for v in vals) + f' = {fmt(s)}'),
                 S('Mean = sum of values ÷ number of values.', 'اوسط = قیمتوں کا مجموعہ ÷ قیمتوں کی تعداد۔', 'اوسط = د ارزښتونو مجموعه ÷ د ارزښتونو شمېر.',
                   m=rf'\overline{{X}} = \frac{{\Sigma X}}{{n}} = \frac{{{fmt(s)}}}{{{n}}} {approx} {ans}')]
        return {'steps': steps, 'answer': ans}
    if kind == 'median':
        sv = sorted(vals)
        steps = [S('Arrange the values in ascending order.', 'قیمتوں کو صعودی ترتیب میں لکھیں۔', 'ارزښتونه په صعودي ترتیب ولیکئ.', m=', '.join(fmt(v) for v in sv))]
        if n % 2:
            k = (n + 1) // 2
            med = sv[k - 1]
            steps.append(S(f'n = {n} is odd, so the median is the ((n + 1) ÷ 2)th = {k}th value.', f'n = {n} طاق ہے، اس لیے وسطانیہ ((n + 1) ÷ 2) = {k}واں رکن ہے۔',
                           f'n = {n} طاق دی، نو منځنی ((n + 1) ÷ 2) = {k}م ارزښت دی.', m=rf'\text{{Median}} = {fmt(med)}'))
        else:
            k = n // 2
            a, b = sv[k - 1], sv[k]
            med = (a + b) / 2
            steps.append(S(f'n = {n} is even, so the median is the mean of the {k}th and {k + 1}th values.', f'n = {n} جفت ہے، اس لیے وسطانیہ {k}ویں اور {k + 1}ویں قیمت کا اوسط ہے۔',
                           f'n = {n} جفت دی، نو منځنی د {k}م او {k + 1}م ارزښت اوسط دی.', m=rf'\text{{Median}} = \frac{{{fmt(a)} + {fmt(b)}}}{{2}} = {fmt(med)}'))
        return {'steps': steps, 'answer': fmt(med)}
    c = Counter(vals)
    top = max(c.values())
    modes = sorted(v for v, k in c.items() if k == top)
    tbl = ', '.join(f'{fmt(v)} → {k}' for v, k in sorted(c.items()))
    steps = [S('Count how many times each value occurs (its frequency).', 'گنیں کہ ہر قیمت کتنی بار آتی ہے (اس کا تعدد)۔', 'وشمېرئ چې هر ارزښت څو ځله راځي (تکرار یې).', m=r'\text{' + tbl + '}')]
    if top == 1:
        steps.append(S('Every value occurs only once, so there is no mode.', 'ہر قیمت صرف ایک بار آتی ہے، اس لیے کوئی عادہ نہیں۔', 'هر ارزښت یوازې یو ځل راځي، نو ډېرتکراری نشته.'))
        return {'steps': steps, 'answer': 'No mode'}
    steps.append(S(f'The value(s) with the greatest frequency ({top}) is the mode.', f'سب سے زیادہ تعدد ({top}) والی قیمت عادہ ہے۔', f'هغه ارزښت چې تر ټولو ډېر تکرار ({top}) لري ډېرتکراری دی.',
                   m=r'\text{Mode} = \hat{X} = ' + ', '.join(fmt(v) for v in modes)))
    return {'steps': steps, 'answer': ', '.join(fmt(v) for v in modes)}


def longdiv_spec(divisor, dividend):
    s = str(dividend)
    cur, started, qd, lines = 0, False, '', []
    for i, ch in enumerate(s):
        cur = cur * 10 + int(ch)
        if not started and cur < divisor and i < len(s) - 1:
            continue
        q = cur // divisor
        if started:
            lines.append(f'{cur}@{i}')
        if q or not started:
            lines.append(f'-{q * divisor}@{i}')
        qd += str(q)
        started = True
        cur -= q * divisor
    lines.append(f'{cur}@{len(s) - 1}')
    return f'{divisor} | {dividend} | {int(qd)}@{len(s) - 1} | ' + ' ; '.join(lines)


def is_factor(text, *_):
    d, n = nums(text)[:2]
    q, r = divmod(n, d)
    svg = figs.longdiv(longdiv_spec(d, n))
    steps = [S(f'To check if {d} is a factor of {n}, divide {n} by {d}.', f'یہ جانچنے کے لیے کہ {d}، عدد {n} کا جزوِ ضربی ہے یا نہیں، {n} کو {d} سے تقسیم کریں۔',
               f'د دې ازمویلو لپاره چې {d} د {n} ضربي جز دی که نه، {n} پر {d} ووېشئ.', svg=svg),
             S(f'The quotient is {q} and the remainder is {r}.', f'خارجِ قسمت {q} اور باقی {r} ہے۔', f'خارج قسمت {q} او پاتې شونی {r} دی.', m=f'{n} \\div {d} = {q}\\ \\text{{r}}\\ {r}')]
    if r:
        steps.append(S(f'The remainder is not zero, so {d} is not a factor of {n}.', f'باقی صفر نہیں، اس لیے {d}، عدد {n} کا جزوِ ضربی نہیں ہے۔',
                       f'پاتې شونی صفر نه دی، نو {d} د {n} ضربي جز نه دی.'))
        ans = f'No, {d} is not a factor of {n}.'
    else:
        steps.append(S(f'The remainder is zero, so {d} is a factor of {n}.', f'باقی صفر ہے، اس لیے {d}، عدد {n} کا جزوِ ضربی ہے۔',
                       f'پاتې شونی صفر دی، نو {d} د {n} ضربي جز دی.'))
        ans = f'Yes, {d} is a factor of {n}.'
    return {'steps': steps, 'answer': ans}


# ---------------------------------------------------------------- prime factorization / index notation
def _ladder_steps(n):
    fs = primes_of(n)
    rows, cur = [], n
    for p in fs:
        rows.append(f'{p}:{cur}')
        cur //= p
    rows.append(':1')
    return fs, figs.ladder(', '.join(rows))


def prime_index(text, method='ladder', *_):
    n = nums(text)[0]
    fs = primes_of(n)
    steps = [S(f'Start with {n}. Always divide by the smallest prime number that divides it exactly (try 2, then 3, 5, 7, …).',
               f'{n} سے شروع کریں۔ ہمیشہ اس سب سے چھوٹے مفرد عدد سے تقسیم کریں جو اسے پورا پورا تقسیم کرے (پہلے 2، پھر 3، 5، 7، …)۔',
               f'له {n} څخه پیل وکړئ. تل پر هغه تر ټولو کوچني لومړني عدد ووېشئ چې په بشپړ ډول یې وېشي (لومړی 2، بیا 3، 5، 7، …).')]
    cur = n
    for p in fs:
        steps.append(S(f'{cur} ÷ {p} = {cur // p}', f'{cur} ÷ {p} = {cur // p}', f'{cur} ÷ {p} = {cur // p}'))
        cur //= p
    if method == 'tree':
        spec, node = '', n
        parts = []
        for p in fs[:-1]:
            parts.append((node, p))
            node //= p
        def build(i):
            if i == len(parts):
                return f'{node}*'
            v, p = parts[i]
            return f'{v}({p}*,{build(i + 1)})'
        svg = figs.ftree(build(0) if parts else f'{n}*')
        steps.append(S('The same work drawn as a factor tree (the circled numbers are prime):', 'یہی کام فیکٹر ٹری کی صورت میں (دائرے والے اعداد مفرد ہیں):',
                       'هم دا کار د ضربي ونې په بڼه (په کړۍ کې عددونه لومړني دي):', svg=svg))
    else:
        steps.append(S('The same work written as a division ladder:', 'یہی کام تقسیم کی سیڑھی کی صورت میں:', 'هم دا کار د وېش د زینې په بڼه:', svg=_ladder_steps(n)[1]))
    steps.append(S(f'We reached 1, so we stop. Multiply all the prime divisors to write {n} in expanded form.',
                   f'ہم 1 تک پہنچ گئے، اس لیے رک جاتے ہیں۔ تمام مفرد مقسوم علیہ کو ضرب کی صورت میں لکھیں، یہ {n} کی پھیلی ہوئی صورت ہے۔',
                   f'1 ته ورسېدو، نو درېږو. ټول لومړني وېشونکي د ضرب په بڼه ولیکئ، دا د {n} پراخه بڼه ده.', m=f'{n} = {expanded_tex(fs)}'))
    c = Counter(fs)
    rep = [f'{p} appears {k} times → ${p}^{{{k}}}$' for p, k in sorted(c.items()) if k > 1]
    if rep:
        steps.append(S('Count how many times each prime repeats and write that count as the index (power): ' + '; '.join(rep) + '.',
                       'گنیں کہ ہر مفرد عدد کتنی بار آیا ہے اور اس گنتی کو قوت نما بنا دیں: ' + '؛ '.join(f'{p} کو {k} بار → ${p}^{{{k}}}$' for p, k in sorted(c.items()) if k > 1) + '۔',
                       'وشمېرئ چې هر لومړنی عدد څو ځله راغلی او دا شمېر توان وګرځوئ: ' + '؛ '.join(f'{p} {k} ځله → ${p}^{{{k}}}$' for p, k in sorted(c.items()) if k > 1) + '.',
                       m=f'{n} = {index_tex(fs)}'))
    else:
        steps.append(S('No prime repeats, so the index form is the same as the expanded form.', 'کوئی مفرد عدد دہرایا نہیں گیا، اس لیے قوت نما کی صورت پھیلی ہوئی صورت جیسی ہے۔',
                       'هېڅ لومړنی عدد نه دی تکرار شوی، نو د توان بڼه د پراخې بڼې په څېر ده.', m=f'{n} = {index_tex(fs)}'))
    return {'steps': steps, 'answer': f'${n} = {index_tex(fs)}$'}


def _terms(tex):
    t = tex.replace('$', '').replace(' ', '')
    out = []
    for term in t.split(r'\times'):
        m = re.fullmatch(r'(\d+)(?:\^\{?(\d+)\}?)?', term)
        out.append((int(m.group(1)), int(m.group(2) or 1)))
    return out


def expand(text, *_):
    terms = _terms(text)
    steps = [S('The index (small raised number) tells how many times the base is multiplied by itself.',
               'قوت نما (اوپر لکھا چھوٹا عدد) بتاتا ہے کہ اساس کو کتنی بار خود سے ضرب دیا گیا ہے۔',
               'توان (پورته لیکل شوی کوچنی عدد) ښيي چې قاعده څو ځله په خپل ځان کې ضرب شوې ده.')]
    for b, k in terms:
        if k > 1:
            steps.append(S(f'${b}^{{{k}}}$ means {b} written {k} times and multiplied.', f'${b}^{{{k}}}$ کا مطلب ہے {b} کو {k} بار لکھ کر ضرب دینا۔',
                           f'${b}^{{{k}}}$ یعنې {b} {k} ځله لیکل او ضربول.', m=f'{b}^{{{k}}} = ' + X.join([str(b)] * k)))
        else:
            steps.append(S(f'{b} has no index, so it is written once.', f'{b} پر کوئی قوت نما نہیں، اس لیے اسے ایک بار لکھیں۔',
                           f'{b} توان نه لري، نو یو ځل لیکل کېږي.', m=str(b)))
    full = X.join(X.join([str(b)] * k) for b, k in terms)
    steps.append(S('Put all the parts together:', 'تمام حصے ایک ساتھ لکھیں:', 'ټولې برخې یوځای ولیکئ:', m=full))
    return {'steps': steps, 'answer': f'${full}$'}


def to_index(text, *_):
    fs = [b for b, k in _terms(text) for _ in range(k)]
    c = Counter(fs)
    steps = [S('Group the same numbers together and count how many times each one is multiplied.',
               'ایک جیسے اعداد کو اکٹھا کریں اور گنیں کہ ہر عدد کتنی بار ضرب ہوا ہے۔',
               'یو شان عددونه یوځای کړئ او وشمېرئ چې هر یو څو ځله ضرب شوی دی.')]
    for b, k in sorted(c.items()):
        if b == 1:
            steps.append(S('1 does not change a product, and 1 to any power is still 1, so 1 can be left out.',
                           '1 کسی حاصلِ ضرب کو نہیں بدلتا اور 1 کی کوئی بھی طاقت 1 ہی رہتی ہے، اس لیے 1 کو چھوڑا جا سکتا ہے۔',
                           '1 حاصل ضرب نه بدلوي او د 1 هر توان 1 پاتې کېږي، نو 1 پرېښودل کېدای شي.'))
            continue
        steps.append(S(f'{b} is multiplied {k} time{"s" if k > 1 else ""}, so we write ${b}^{{{k}}}$.' if k > 1 else f'{b} appears only once, so it stays {b}.',
                       f'{b} کو {k} بار ضرب دیا گیا ہے، اس لیے ${b}^{{{k}}}$ لکھیں۔' if k > 1 else f'{b} صرف ایک بار آیا ہے، اس لیے {b} ہی رہے گا۔',
                       f'{b} {k} ځله ضرب شوی، نو ${b}^{{{k}}}$ لیکو.' if k > 1 else f'{b} یوازې یو ځل راغلی، نو {b} پاتې کېږي.',
                       m=(X.join([str(b)] * k) + ' = ' + f'{b}^{{{k}}}') if k > 1 else str(b)))
    ans = X.join(f'{b}^{{{k}}}' if k > 1 else str(b) for b, k in sorted(c.items()) if b != 1)
    steps.append(S('Index notation:', 'قوت نما کی صورت:', 'د توان بڼه:', m=ans))
    return {'steps': steps, 'answer': f'${ans}$'}


# ---------------------------------------------------------------- HCF and LCM
def _factor_lines(ns):
    lines = []
    for n in ns:
        fs = primes_of(n)
        lines.append((n, fs))
    return lines


def hcf_pf(text, *_):
    ns = nums(text)
    lines = _factor_lines(ns)
    steps = [S('Step 1: Write each number as a product of prime factors (division ladder).',
               'مرحلہ 1: ہر عدد کو مفرد اجزائے ضربی کے حاصلِ ضرب کی صورت میں لکھیں (تقسیم کی سیڑھی)۔',
               'لومړی پړاو: هر عدد د لومړنیو ضربي اجزاوو د حاصل ضرب په بڼه ولیکئ (د وېش زینه).',
               svg='<div style="display:flex;gap:28px;flex-wrap:wrap;justify-content:center">' + ''.join(_ladder_steps(n)[1] for n in ns) + '</div>')]
    for n, fs in lines:
        steps.append(S(f'Prime factors of {n}', f'{n} کے مفرد اجزائے ضربی', f'د {n} لومړني ضربي اجزا', m=f'{n} = {expanded_tex(fs)}'))
    counts = [Counter(fs) for _, fs in lines]
    common = Counter(dict((p, min(c[p] for c in counts)) for p in set.intersection(*[set(c) for c in counts])))
    common_list = sorted(common.elements())
    if common_list:
        h = 1
        for p in common_list:
            h *= p
        steps.append(S(f'Step 2: Pick the prime factors that are common to ALL the numbers: {", ".join(map(str, common_list))}.',
                       f'مرحلہ 2: وہ مفرد اجزائے ضربی چنیں جو تمام اعداد میں مشترک ہیں: {"، ".join(map(str, common_list))}۔',
                       f'دوهم پړاو: هغه لومړني ضربي اجزا وټاکئ چې په ټولو عددونو کې مشترک دي: {"، ".join(map(str, common_list))}.'))
        steps.append(S('Step 3: Multiply the common prime factors. This product is the HCF.', 'مرحلہ 3: مشترک مفرد اجزائے ضربی کو ضرب دیں۔ یہی حاصلِ ضرب عاد اعظم ہے۔',
                       'درېیم پړاو: مشترک لومړني ضربي اجزا ضرب کړئ. همدا حاصل ضرب لوی مشترک قاسم دی.',
                       m=r'\text{HCF} = ' + (expanded_tex(common_list) + ' = ' if len(common_list) > 1 else '') + str(h)))
    else:
        h = 1
        steps.append(S('Step 2: No prime factor is common to all the numbers. Only 1 divides all of them, so HCF = 1.',
                       'مرحلہ 2: کوئی مفرد جزوِ ضربی تمام اعداد میں مشترک نہیں۔ صرف 1 ان سب کو تقسیم کرتا ہے، اس لیے عاد اعظم = 1۔',
                       'دوهم پړاو: هېڅ لومړنی ضربي جز په ټولو عددونو کې مشترک نه دی. یوازې 1 ټول وېشي، نو لوی مشترک قاسم = 1.', m=r'\text{HCF} = 1'))
    return {'steps': steps, 'answer': f'HCF = {h}'}


def _stair_spec(a, b):
    big, small = max(a, b), min(a, b)
    parts = []
    while True:
        q, r = divmod(big, small)
        parts.append(f'{small}|{big}|{q}|-{q * small}' + (',0' if r == 0 else ''))
        if r == 0:
            return ' ; '.join(parts), small
        big, small = small, r


def hcf_div(text, *_):
    ns = sorted(nums(text), reverse=True)
    steps = [S('Divide the greater number by the smaller one. Then keep dividing the last divisor by the remainder. When the remainder becomes 0, the last divisor is the HCF.',
               'بڑے عدد کو چھوٹے سے تقسیم کریں۔ پھر پچھلے مقسوم علیہ کو باقی سے تقسیم کرتے رہیں۔ جب باقی 0 ہو جائے تو آخری مقسوم علیہ عاد اعظم ہے۔',
               'لوی عدد پر کوچني ووېشئ. بیا وروستی وېشونکی پر پاتې شوني وېشئ. کله چې پاتې شونی 0 شي، وروستی وېشونکی لوی مشترک قاسم دی.')]
    h = ns[0]
    first = True
    for n in ns[1:]:
        spec, nh = _stair_spec(h, n)
        if first:
            steps.append(S(f'Find the HCF of {ns[0]} and {n}.', f'{ns[0]} اور {n} کا عاد اعظم معلوم کریں۔', f'د {ns[0]} او {n} لوی مشترک قاسم معلوم کړئ.', svg=figs.stair(spec)))
            steps.append(S(f'The remainder is 0, so the HCF of {ns[0]} and {n} is {nh}.', f'باقی 0 ہے، اس لیے {ns[0]} اور {n} کا عاد اعظم {nh} ہے۔',
                           f'پاتې شونی 0 دی، نو د {ns[0]} او {n} لوی مشترک قاسم {nh} دی.'))
        else:
            steps.append(S(f'Now find the HCF of {h} and the next number {n}.', f'اب {h} اور اگلے عدد {n} کا عاد اعظم معلوم کریں۔', f'اوس د {h} او بل عدد {n} لوی مشترک قاسم معلوم کړئ.', svg=figs.stair(spec)))
            steps.append(S(f'The last divisor is {nh}.', f'آخری مقسوم علیہ {nh} ہے۔', f'وروستی وېشونکی {nh} دی.'))
        h, first = nh, False
    steps.append(S(f'So, the HCF of {lst(sorted(nums(text)))} is {h}.', f'لہٰذا {lst_ur(sorted(nums(text)))} کا عاد اعظم {h} ہے۔', f'نو د {lst_ps(sorted(nums(text)))} لوی مشترک قاسم {h} دی.', m=rf'\text{{HCF}} = {h}'))
    return {'steps': steps, 'answer': f'HCF = {h}'}


def lcm_pf(text, *_):
    ns = nums(text)
    lines = _factor_lines(ns)
    steps = [S('Step 1: Write each number as a product of prime factors.', 'مرحلہ 1: ہر عدد کو مفرد اجزائے ضربی کے حاصلِ ضرب کی صورت میں لکھیں۔',
               'لومړی پړاو: هر عدد د لومړنیو ضربي اجزاوو د حاصل ضرب په بڼه ولیکئ.',
               svg='<div style="display:flex;gap:28px;flex-wrap:wrap;justify-content:center">' + ''.join(_ladder_steps(n)[1] for n in ns) + '</div>')]
    for n, fs in lines:
        steps.append(S(f'Prime factors of {n}', f'{n} کے مفرد اجزائے ضربی', f'د {n} لومړني ضربي اجزا', m=f'{n} = {expanded_tex(fs)} = {index_tex(fs)}'))
    best = {}
    for n, fs in lines:
        for p, k in Counter(fs).items():
            if k > best.get(p, (0, 0))[0]:
                best[p] = (k, n)
    steps.append(S('Step 2: Take every prime that appears, the greatest number of times it appears in any one number. (This is the same as common factors × non-common factors.)',
                   'مرحلہ 2: ہر وہ مفرد عدد لیں جو کہیں بھی آیا ہو، اتنی بار جتنی بار وہ کسی ایک عدد میں سب سے زیادہ آیا ہو۔ (یہی مشترک × غیر مشترک اجزائے ضربی ہے۔)',
                   'دوهم پړاو: هر هغه لومړنی عدد واخلئ چې راغلی وي، هومره ځله چې په یوه عدد کې تر ټولو ډېر راغلی وي. (دا همغه مشترک × غیر مشترک ضربي اجزا دي.)'))
    for p, (k, n) in sorted(best.items()):
        steps.append(S(f'{p}: at most {k} time{"s" if k > 1 else ""} (in {n}) → ${p}^{{{k}}}$' if k > 1 else f'{p}: at most once (in {n}) → {p}',
                       f'{p}: زیادہ سے زیادہ {k} بار ({n} میں) → ${p}^{{{k}}}$' if k > 1 else f'{p}: زیادہ سے زیادہ ایک بار ({n} میں) → {p}',
                       f'{p}: تر ټولو ډېر {k} ځله (په {n} کې) → ${p}^{{{k}}}$' if k > 1 else f'{p}: تر ټولو ډېر یو ځل (په {n} کې) → {p}'))
    tex = X.join(f'{p}^{{{k}}}' if k > 1 else str(p) for p, (k, _) in sorted(best.items()))
    val = 1
    for p, (k, _) in best.items():
        val *= p ** k
    steps.append(S('Step 3: Multiply them. The product is the LCM.', 'مرحلہ 3: انہیں ضرب دیں۔ حاصلِ ضرب ذو اضعاف اقل ہے۔', 'درېیم پړاو: ضرب یې کړئ. حاصل ضرب کوچنی مشترک ضرب دی.',
                   m=rf'\text{{LCM}} = {tex} = {val}'))
    return {'steps': steps, 'answer': f'LCM = {val}'}


def lcm_div(text, *_):
    ns = nums(text)
    cur = list(ns)
    rows, divs = [], []
    while any(x > 1 for x in cur):
        cands = sorted(set(p for x in cur if x > 1 for p in primes_of(x)))
        two = [p for p in cands if sum(1 for x in cur if x % p == 0) >= 2]
        p = two[0] if two else cands[0]
        rows.append(f'{p}:' + ', '.join(map(str, cur)))
        divs.append(p)
        cur = [x // p if x % p == 0 else x for x in cur]
    rows.append(':' + ', '.join(map(str, cur)))
    val = 1
    for p in divs:
        val *= p
    steps = [S('Write the numbers in one line. Divide by a prime that divides at least two of them; numbers it does not divide are copied down unchanged. When no prime divides two numbers, divide by a prime that divides one. Stop when every number becomes 1.',
               'اعداد ایک لائن میں لکھیں۔ ایسے مفرد عدد سے تقسیم کریں جو کم از کم دو اعداد کو تقسیم کرے؛ جو عدد تقسیم نہ ہو اسے ویسے ہی نیچے لکھ دیں۔ جب کوئی مفرد عدد دو اعداد کو تقسیم نہ کرے تو ایک کو تقسیم کرنے والا مفرد عدد لیں۔ جب سب اعداد 1 ہو جائیں تو رک جائیں۔',
               'عددونه په یوه کرښه کې ولیکئ. پر داسې لومړني عدد ووېشئ چې لږ تر لږه دوه عددونه ووېشي؛ کوم عدد چې نه وېشل کېږي هماغسې لاندې ولیکئ. کله چې هېڅ لومړنی عدد دوه عددونه ونه وېشي، پر هغه لومړني ووېشئ چې یو یې وېشي. کله چې ټول عددونه 1 شي، ودرېږئ.',
               svg=figs.ladder('; '.join(rows))),
             S('Multiply all the prime divisors on the left side. The product is the LCM.', 'بائیں طرف کے تمام مفرد مقسوم علیہ کو ضرب دیں۔ حاصلِ ضرب ذو اضعاف اقل ہے۔',
               'په کیڼ اړخ ټول لومړني وېشونکي ضرب کړئ. حاصل ضرب کوچنی مشترک ضرب دی.', m=rf'\text{{LCM}} = {expanded_tex(divs)} = {val}')]
    return {'steps': steps, 'answer': f'LCM = {val}'}




GENERATORS = {'factors': factors, 'multiples': multiples, 'isfactor': is_factor, 'prime': prime_index, 'expand': expand,
              'index': to_index, 'hcfpf': hcf_pf, 'hcfdiv': hcf_div, 'lcmpf': lcm_pf, 'lcmdiv': lcm_div, 'firstmult': first_multiples, 'square': square, 'opposite': opposite, 'between': between, 'six': six, 'represent': represent, 'greater': greater, 'order': order, 'absval': absval, 'absorder': absorder, 'iexpr': iexpr, 'missing': missing, 'verify': verify, 'comm': comm, 'assoc': assoc, 'mul': mul, 'inverse': inverse, 'div': div, 'bodmas': bodmas, 'pctof': pctof, 'pct': pct, 'colourpct': colourpct, 'comparepct': comparepct, 'change': change, 'ratio': ratio, 'rfrac': rfrac, 'contr': contr, 'share': share, 'urate': urate, 'seq': seq, 'evalx': evalx, 'combine': combine, 'lineq': lineq, 'pathq': pathq, 'sqrect': sqrect, 'solidq': solidq, 'pieq': pieq, 'stat': stat}


# ---- Class 3: column addition / subtraction / multiplication with place-value steps ----
_PLACES = [('ones', 'اکائیاں', 'یووالي'), ('tens', 'دہائیاں', 'لسیزې'), ('hundreds', 'سینکڑے', 'سلیزې'),
           ('thousands', 'ہزار', 'زرګونه'), ('ten thousands', 'دس ہزار', 'لس زرګونه')]


def _colarr(rows, op, res):
    """LaTeX column layout: rows of numbers, operator on the last row, a rule, then the result."""
    w = max(len(str(x)) for x in rows + [res])
    cells = lambda s: ' & '.join(list(str(s).rjust(w)).__iter__()).replace('  ', '')
    def row(s, sign=''):
        s = str(s).rjust(w)
        return (sign + ' & ' if True else '') + ' & '.join(c if c != ' ' else '' for c in s)
    body = [row(r) for r in rows[:-1]] + [row(rows[-1], op)]
    return r'\begin{array}{c' + 'c' * w + '} ' + r' \\ '.join(body) + r' \\ \hline ' + row(res) + r' \end{array}'


def colop(text, *_):
    t = text.replace(',', '').replace('−', '-').replace('×', 'x').replace('–', '-')
    m = re.search(r'(\d+)\s*([+\-x;])\s*(\d+)', t)
    if not m:
        raise ValueError('colop: cannot read ' + text)
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
    if op == ';':
        op = '+'
    steps = []
    if op == '+':
        res, carry = a + b, 0
        da, db = str(a)[::-1], str(b)[::-1]
        for i in range(max(len(da), len(db))):
            x = int(da[i]) if i < len(da) else 0
            y = int(db[i]) if i < len(db) else 0
            s = x + y + carry
            pe, pu, pp = _PLACES[i]
            extra = f' + {carry} carried' if carry else ''
            extra_u = f' + {carry} حاصل' if carry else ''
            extra_p = f' + {carry} لېږدول شوی' if carry else ''
            if s >= 10:
                steps.append(S(f'Add {pe}: {x} + {y}{extra} = {s}. Write {s % 10} and carry 1 to the next place.',
                               f'{pu} جمع کریں: {x} + {y}{extra_u} = {s}۔ {s % 10} لکھیں اور 1 اگلے مقام پر لے جائیں۔',
                               f'{pp} جمع کړئ: {x} + {y}{extra_p} = {s}. {s % 10} ولیکئ او 1 بل ځای ته یوسئ.'))
                carry = 1
            else:
                steps.append(S(f'Add {pe}: {x} + {y}{extra} = {s}.', f'{pu} جمع کریں: {x} + {y}{extra_u} = {s}۔', f'{pp} جمع کړئ: {x} + {y}{extra_p} = {s}.'))
                carry = 0
        if carry:
            pe, pu, pp = _PLACES[len(str(res)) - 1]
            steps.append(S(f'Write the carried 1 in the {pe} place.', f'حاصل 1 کو {pu} کے مقام پر لکھیں۔', f'لېږدول شوی 1 د {pp} په ځای کې ولیکئ.'))
        steps.append(S(f'So {a:,} + {b:,} = {res:,}.', f'لہٰذا {a:,} + {b:,} = {res:,}۔', f'نو {a:,} + {b:,} = {res:,}.', m=_colarr([a, b], '+', res)))
        return {'steps': steps, 'answer': f'{res:,}'}
    if op == '-':
        if b > a:
            raise ValueError('colop: negative result ' + text)
        res = a - b
        da = [int(c) for c in str(a)[::-1]]
        db = [int(c) for c in str(b)[::-1]] + [0] * (len(str(a)) - len(str(b)))
        for i in range(len(da)):
            pe, pu, pp = _PLACES[i]
            if da[i] < db[i]:
                j = i + 1
                while da[j] == 0:
                    j += 1
                da[j] -= 1
                for k in range(j - 1, i, -1):
                    da[k] += 9
                da[i] += 10
                ne, nu, np_ = _PLACES[i + 1]
                if j > i + 1:
                    je, ju, jp = _PLACES[j]
                    steps.append(S(f'{pe.capitalize()}: {da[i] - 10} is less than {db[i]}. The next place is 0, so borrow 1 from the {je}: each 0 in between becomes 9 and {da[i] - 10} becomes {da[i]}. {da[i]} − {db[i]} = {da[i] - db[i]}.',
                                   f'{pu}: {da[i] - 10}، {db[i]} سے چھوٹا ہے۔ اگلا مقام 0 ہے، اس لیے {ju} سے 1 ادھار لیں: درمیان کا ہر 0، 9 بن جاتا ہے اور {da[i] - 10} بن جاتا ہے {da[i]}۔ {da[i]} − {db[i]} = {da[i] - db[i]}۔',
                                   f'{pp}: {da[i] - 10} له {db[i]} کوچنی دی. بل ځای 0 دی، نو له {jp} څخه 1 پور واخلئ: په منځ کې هر 0 په 9 بدلېږي او {da[i] - 10} کېږي {da[i]}. {da[i]} − {db[i]} = {da[i] - db[i]}.'))
                    continue
                steps.append(S(f'{pe.capitalize()}: {da[i] - 10} is less than {db[i]}, so borrow 1 from the {ne}: {da[i] - 10} becomes {da[i]}. {da[i]} − {db[i]} = {da[i] - db[i]}.',
                               f'{pu}: {da[i] - 10}، {db[i]} سے چھوٹا ہے، اس لیے {nu} سے 1 ادھار لیں: {da[i] - 10} بن جاتا ہے {da[i]}۔ {da[i]} − {db[i]} = {da[i] - db[i]}۔',
                               f'{pp}: {da[i] - 10} له {db[i]} کوچنی دی، نو له {np_} څخه 1 پور واخلئ: {da[i] - 10} کېږي {da[i]}. {da[i]} − {db[i]} = {da[i] - db[i]}.'))
            else:
                steps.append(S(f'Subtract {pe}: {da[i]} − {db[i]} = {da[i] - db[i]}.', f'{pu} تفریق کریں: {da[i]} − {db[i]} = {da[i] - db[i]}۔', f'{pp} تفریق کړئ: {da[i]} − {db[i]} = {da[i] - db[i]}.'))
        steps.append(S(f'So {a:,} − {b:,} = {res:,}. Check: {res:,} + {b:,} = {a:,}.', f'لہٰذا {a:,} − {b:,} = {res:,}۔ جانچ: {res:,} + {b:,} = {a:,}۔', f'نو {a:,} − {b:,} = {res:,}. ازموینه: {res:,} + {b:,} = {a:,}.', m=_colarr([a, b], '-', res)))
        return {'steps': steps, 'answer': f'{res:,}'}
    # multiplication: b is the 1-digit multiplier (or the smaller number)
    if a < b:
        a, b = b, a
    res, carry = a * b, 0
    da = str(a)[::-1]
    for i, c in enumerate(da):
        x = int(c)
        s = x * b + carry
        pe, pu, pp = _PLACES[i]
        extra = f' + {carry} carried' if carry else ''
        extra_u = f' + {carry} حاصل' if carry else ''
        extra_p = f' + {carry} لېږدول شوی' if carry else ''
        last = i == len(da) - 1
        if s >= 10 and not last:
            steps.append(S(f'Multiply the {pe}: {x} × {b}{extra} = {s}. Write {s % 10} and carry {s // 10}.', f'{pu} کو ضرب دیں: {x} × {b}{extra_u} = {s}۔ {s % 10} لکھیں اور {s // 10} آگے لے جائیں۔',
                           f'{pp} ضرب کړئ: {x} × {b}{extra_p} = {s}. {s % 10} ولیکئ او {s // 10} مخ ته یوسئ.'))
            carry = s // 10
        else:
            steps.append(S(f'Multiply the {pe}: {x} × {b}{extra} = {s}. Write {s}.', f'{pu} کو ضرب دیں: {x} × {b}{extra_u} = {s}۔ {s} لکھیں۔', f'{pp} ضرب کړئ: {x} × {b}{extra_p} = {s}. {s} ولیکئ.'))
            carry = 0
    steps.append(S(f'So {a} × {b} = {res:,}.', f'لہٰذا {a} × {b} = {res:,}۔', f'نو {a} × {b} = {res:,}.', m=_colarr([a, b], r'\times', res)))
    return {'steps': steps, 'answer': f'{res:,}'}


GENERATORS['colop'] = colop


def mental(text, *_):
    """Class 3: mental addition/subtraction of 2-digit numbers by splitting into tens and ones."""
    t = text.replace('−', '-')
    m = re.search(r'(\d+)\s*([+\-])\s*(\d+)', t)
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
    at, ao, bt, bo = a // 10 * 10, a % 10, b // 10 * 10, b % 10
    if op == '+':
        r = a + b
        st = [S(f'Split into tens and ones: {a} = {at} + {ao} and {b} = {bt} + {bo}.', f'دہائیوں اور اکائیوں میں توڑیں: {a} = {at} + {ao} اور {b} = {bt} + {bo}۔', f'په لسیزو او یووالو یې ووېشئ: {a} = {at} + {ao} او {b} = {bt} + {bo}.'),
              S(f'Add the tens: {at} + {bt} = {at + bt}. Add the ones: {ao} + {bo} = {ao + bo}.', f'دہائیاں جمع کریں: {at} + {bt} = {at + bt}۔ اکائیاں جمع کریں: {ao} + {bo} = {ao + bo}۔', f'لسیزې جمع کړئ: {at} + {bt} = {at + bt}. یووالي جمع کړئ: {ao} + {bo} = {ao + bo}.'),
              S(f'Put them together: {at + bt} + {ao + bo} = {r}.', f'دونوں کو ملائیں: {at + bt} + {ao + bo} = {r}۔', f'دواړه یوځای کړئ: {at + bt} + {ao + bo} = {r}.', m=f'{a} + {b} = {r}')]
    else:
        r = a - b
        st = [S(f'Take away the tens first: {a} − {bt} = {a - bt}.', f'پہلے دہائیاں نکالیں: {a} − {bt} = {a - bt}۔', f'لومړی لسیزې کمې کړئ: {a} − {bt} = {a - bt}.'),
              S(f'Then take away the ones: {a - bt} − {bo} = {r}.', f'پھر اکائیاں نکالیں: {a - bt} − {bo} = {r}۔', f'بیا یووالي کم کړئ: {a - bt} − {bo} = {r}.', m=f'{a} - {b} = {r}')]
    return {'steps': st, 'answer': str(r)}


GENERATORS['mental'] = mental


def divq(text, *_):
    """Class 3: A ÷ B (exact) with the long-division layout and a multiplication check."""
    a, b = nums(text.replace(',', ''))[:2]
    q, r = divmod(a, b)
    steps = []
    if a >= 10 and a // 10 >= b:
        t, o = a // 10, a % 10
        qt, rt = divmod(t, b)
        steps.append(S(f'Divide the tens first: {t} ÷ {b} = {qt}' + (f' remainder {rt}.' if rt else '.'), f'پہلے دہائیاں تقسیم کریں: {t} ÷ {b} = {qt}' + (f'، باقی {rt}۔' if rt else '۔'), f'لومړی لسیزې ووېشئ: {t} ÷ {b} = {qt}' + (f'، پاتې {rt}.' if rt else '.')))
        rest = rt * 10 + o
        steps.append(S(f'Bring down the ones: {rest} ÷ {b} = {rest // b}.', f'اکائیاں نیچے لائیں: {rest} ÷ {b} = {rest // b}۔', f'یووالي راکوز کړئ: {rest} ÷ {b} = {rest // b}.'))
    else:
        steps.append(S(f'Use the table of {b}: {b} × {q} = {b * q}.', f'{b} کا پہاڑا استعمال کریں: {b} × {q} = {b * q}۔', f'د {b} جدول وکاروئ: {b} × {q} = {b * q}.'))
    steps.append(S(f'So {a} ÷ {b} = {q}' + (f' remainder {r}' if r else '') + f'. Check: {q} × {b} = {q * b}.', f'لہٰذا {a} ÷ {b} = {q}' + (f'، باقی {r}' if r else '') + f'۔ جانچ: {q} × {b} = {q * b}۔',
                   f'نو {a} ÷ {b} = {q}' + (f'، پاتې {r}' if r else '') + f'. ازموینه: {q} × {b} = {q * b}.', m=rf'{a} \div {b} = {q}', svg=figs.longdiv(longdiv_spec(b, a)) if a >= 10 else None))
    return {'steps': steps, 'answer': str(q) + (f' remainder {r}' if r else '')}


GENERATORS['divq'] = divq


def fracop(text, *_):
    r"""Class 3: add or subtract two fractions with the same denominator, e.g. '3/7 + 2/7' or '\frac{3}{7} - \frac{2}{7}'."""
    t = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}', r'\1/\2', text).replace('−', '-').replace('$', '')
    m = re.search(r'(\d+)/(\d+)\s*([+\-])\s*(\d+)/(\d+)', t)
    a, d1, op, b, d2 = int(m.group(1)), int(m.group(2)), m.group(3), int(m.group(4)), int(m.group(5))
    assert d1 == d2, 'fracop needs equal denominators: ' + text
    r = a + b if op == '+' else a - b
    sym = '+' if op == '+' else '-'
    if op == '+':
        st = [S(f'The denominators are the same ({d1}), so add the numerators only: {a} + {b} = {r}.', f'نسب نما ایک جیسے ہیں ({d1})، اس لیے صرف شمار کنندہ جمع کریں: {a} + {b} = {r}۔', f'مخرجونه یو شان دي ({d1})، نو یوازې صورتونه جمع کړئ: {a} + {b} = {r}.',
                m=rf'\frac{{{a}}}{{{d1}}} + \frac{{{b}}}{{{d1}}} = \frac{{{a} + {b}}}{{{d1}}} = \frac{{{r}}}{{{d1}}}')]
    else:
        st = [S(f'The denominators are the same ({d1}), so subtract the numerators only: {a} − {b} = {r}.', f'نسب نما ایک جیسے ہیں ({d1})، اس لیے صرف شمار کنندہ تفریق کریں: {a} − {b} = {r}۔', f'مخرجونه یو شان دي ({d1})، نو یوازې صورتونه تفریق کړئ: {a} − {b} = {r}.',
                m=rf'\frac{{{a}}}{{{d1}}} - \frac{{{b}}}{{{d1}}} = \frac{{{a} - {b}}}{{{d1}}} = \frac{{{r}}}{{{d1}}}')]
    return {'steps': st, 'answer': f'${"0" if r == 0 else rf"\frac{{{r}}}{{{d1}}}"}$'}


GENERATORS['fracop'] = fracop


_UNITS = {('km', 'm'): 1000, ('m', 'cm'): 100, ('kg', 'g'): 1000, ('l', 'ml'): 1000, ('h', 'min'): 60, ('min', 's'): 60}
_UNAME = {'km': ('km', 'کلومیٹر', 'کیلومتره'), 'm': ('m', 'میٹر', 'متره'), 'cm': ('cm', 'سینٹی میٹر', 'سانتي متره'),
          'kg': ('kg', 'کلوگرام', 'کیلوګرامه'), 'g': ('g', 'گرام', 'ګرامه'), 'l': ('l', 'لیٹر', 'لیتره'), 'ml': ('ml', 'ملی لیٹر', 'ملي لیتره'),
          'h': ('h', 'گھنٹے', 'ساعته'), 'min': ('min', 'منٹ', 'دقیقې'), 's': ('s', 'سیکنڈ', 'ثانیې')}


def measop(text, *_):
    """Class 3: 'A big B small +/- C big D small' (e.g. '4 m 65 cm + 5 m 12 cm'); adds/subtracts each unit separately,
    carrying or borrowing with the unit ratio (km/m 1000, m/cm 100, kg/g 1000, l/ml 1000, h/min 60)."""
    t = text.replace('−', '-').replace(',', '')
    toks = re.findall(r'(\d+)\s*(km|kg|ml|min|cm|m|g|l|L|h|s)\b|([+\-])', t)
    vals, op = [], None
    for n, u, o in toks:
        if o:
            op = o
        else:
            vals.append((int(n), u.lower()))
    (a, ub), (b, us), (c, _), (d, _) = vals[:4]
    k = _UNITS[(ub, us)]
    BE, BU, BP = _UNAME[ub]
    SE, SU, SP = _UNAME[us]
    steps = []
    if op == '+':
        small, big = b + d, a + c
        steps.append(S(f'Add the {SE} first: {b} {us} + {d} {us} = {small} {us}.', f'پہلے {SU} جمع کریں: {b} + {d} = {small} {SU}۔', f'لومړی {SP} جمع کړئ: {b} + {d} = {small} {SP}.'))
        steps.append(S(f'Add the {BE}: {a} {ub} + {c} {ub} = {big} {ub}.', f'{BU} جمع کریں: {a} + {c} = {big} {BU}۔', f'{BP} جمع کړئ: {a} + {c} = {big} {BP}.'))
        if small >= k:
            steps.append(S(f'{small} {us} is more than {k} {us} = 1 {ub}, so carry 1 {ub}: {big + 1} {ub} {small - k} {us}.', f'{small} {SU}، {k} {SU} = 1 {BU} سے زیادہ ہیں، اس لیے 1 {BU} آگے لے جائیں: {big + 1} {BU} {small - k} {SU}۔',
                           f'{small} {SP} له {k} {SP} = 1 {BP} څخه زیات دي، نو 1 {BP} مخ ته یوسئ: {big + 1} {BP} {small - k} {SP}.'))
            big, small = big + 1, small - k
    else:
        if b < d:
            steps.append(S(f'{b} {us} is less than {d} {us}, so borrow 1 {ub} = {k} {us}: {a} {ub} {b} {us} becomes {a - 1} {ub} {b + k} {us}.', f'{b} {SU}، {d} {SU} سے کم ہیں، اس لیے 1 {BU} = {k} {SU} ادھار لیں: {a - 1} {BU} {b + k} {SU}۔',
                           f'{b} {SP} له {d} {SP} کم دي، نو 1 {BP} = {k} {SP} پور واخلئ: {a - 1} {BP} {b + k} {SP}.'))
            a, b = a - 1, b + k
        small, big = b - d, a - c
        steps.append(S(f'Subtract the {SE}: {b} {us} − {d} {us} = {small} {us}.', f'{SU} تفریق کریں: {b} − {d} = {small} {SU}۔', f'{SP} تفریق کړئ: {b} − {d} = {small} {SP}.'))
        steps.append(S(f'Subtract the {BE}: {a} {ub} − {c} {ub} = {big} {ub}.', f'{BU} تفریق کریں: {a} − {c} = {big} {BU}۔', f'{BP} تفریق کړئ: {a} − {c} = {big} {BP}.'))
    ans = f'{big} {ub} {small} {us}'
    steps.append(S(f'Answer: {ans}.', f'جواب: {big} {BU} {small} {SU}۔', f'ځواب: {big} {BP} {small} {SP}.'))
    return {'steps': steps, 'answer': ans}


GENERATORS['measop'] = measop


def generate(kind, text, *args):
    return GENERATORS[kind](text, *args)
