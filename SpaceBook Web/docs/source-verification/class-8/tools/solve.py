"""Step-by-step SpaceBook solutions (not printed in the textbook) for Class 8 (copied from the Class 6 tool) Mathematics exercises.

Every generator computes the answer itself, so the working is always arithmetically correct.
A step is {'en','ur','ps'} narration plus optional 'm' (LaTeX shown under it) and/or 'svg'.
"""
import re
from collections import Counter
from math import gcd
import figs

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
              'index': to_index, 'hcfpf': hcf_pf, 'hcfdiv': hcf_div, 'lcmpf': lcm_pf, 'lcmdiv': lcm_div, 'firstmult': first_multiples, 'square': square, 'opposite': opposite, 'between': between, 'six': six, 'represent': represent, 'greater': greater, 'order': order, 'absval': absval, 'absorder': absorder, 'iexpr': iexpr, 'missing': missing, 'verify': verify, 'comm': comm, 'assoc': assoc, 'mul': mul, 'inverse': inverse, 'div': div, 'bodmas': bodmas}


def generate(kind, text, *args):
    return GENERATORS[kind](text, *args)
