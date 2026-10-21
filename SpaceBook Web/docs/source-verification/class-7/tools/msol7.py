"""msol7.py - sequences (arithmetic / geometric / neither) and repeated products as powers."""
import re
from fractions import Fraction
import msol
from msol import step, ParseError

BS = chr(92)


def S(en, ur, ps, m=None):
    d = {'en': en, 'ur': ur, 'ps': ps}
    if m is not None:
        d['m'] = m
    return d


def terms(text):
    t = text.replace('$', '').replace('...', '').replace('…', '').replace('−', '-')
    vals = [Fraction(x) for x in re.findall(r'-?\d+\.?\d*', t)]
    if len(vals) < 3:
        raise ParseError('terms')
    return vals


def f(v):
    return msol.tex_num(v)


def sequence(text, nxt=3):
    a = terms(text)
    diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    steps = [step('given', ', '.join(f(x) for x in a) + ', ' + BS + 'ldots')]
    if all(d == diffs[0] for d in diffs):
        d = diffs[0]
        more = [a[-1] + d * (i + 1) for i in range(nxt)]
        steps.append(S('Differences between consecutive terms:', 'ملحقہ ارکان کا فرق:', 'د ورپسې توکو توپیرونه:', ', '.join(f(x) for x in diffs)))
        steps.append(S(f'The difference is always {f(d)}, so it is an arithmetic sequence: add {f(d)} to get the next term.', f'فرق ہمیشہ {f(d)} ہے، لہٰذا یہ حسابی سلسلہ ہے: اگلا رکن حاصل کرنے کے لیے {f(d)} جمع کریں۔', f'توپیر تل {f(d)} دی، نو دا حسابي لړۍ ده: بل توکی لپاره {f(d)} جمع کړئ.', ', '.join(f(x) for x in more)))
        return steps, ('Arithmetic', more)
    if a[0] != 0 and all(x != 0 for x in a):
        rs = [a[i + 1] / a[i] for i in range(len(a) - 1)]
        if all(r == rs[0] for r in rs):
            r = rs[0]
            more = [a[-1] * r ** (i + 1) for i in range(nxt)]
            steps.append(S('Ratios of consecutive terms:', 'ملحقہ ارکان کی نسبتیں:', 'د ورپسې توکو نسبتونه:', ', '.join(f(x) for x in rs)))
            steps.append(S(f'The ratio is always {f(r)}, so it is a geometric sequence: multiply by {f(r)} to get the next term.', f'نسبت ہمیشہ {f(r)} ہے، لہٰذا یہ ہندسی سلسلہ ہے: اگلا رکن حاصل کرنے کے لیے {f(r)} سے ضرب دیں۔', f'نسبت تل {f(r)} دی، نو دا هندسي لړۍ ده: بل توکی لپاره په {f(r)} ضرب کړئ.', ', '.join(f(x) for x in more)))
            return steps, ('Geometric', more)
    d2 = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
    steps.append(S('Differences between consecutive terms:', 'ملحقہ ارکان کا فرق:', 'د ورپسې توکو توپیرونه:', ', '.join(f(x) for x in diffs)))
    steps.append(S('The differences are not equal and the ratios are not equal, so the sequence is neither arithmetic nor geometric' + (f' (the differences themselves change by {f(d2[0])} each time).' if d2 and all(x == d2[0] for x in d2) else '.'),
                   'فرق برابر نہیں اور نسبتیں بھی برابر نہیں، لہٰذا سلسلہ نہ حسابی ہے نہ ہندسی۔', 'توپیرونه مساوي نه دي او نسبتونه هم مساوي نه دي، نو لړۍ نه حسابي ده نه هندسي.'))
    return steps, ('Neither', [])


def repeated_product(text):
    t = msol.clean_tex(text).replace(BS + 'times', '*')
    parts = [p.strip() for p in t.split('*')]
    if len(parts) < 2 or any(p != parts[0] for p in parts):
        raise ParseError('rep')
    b = parts[0]
    n = len(parts)
    steps = [step('given', f' {BS}times '.join([b] * n)),
             S(f'The same factor {b} is repeated {n} times, so write it as a power (base {b}, exponent {n}); read it "{b} raised to the power {n}".', f'ایک ہی جزو {b} {n} بار آیا ہے، اس لیے طاقت کی صورت میں لکھیں (بنیاد {b}، طاقت {n})؛ پڑھیں "{b} کی طاقت {n}"۔', f'یو شان فکتور {b} {n} ځله راغلی، نو د توان په بڼه یې ولیکئ (بنسټ {b}، توان {n})؛ ولولئ "{b} په توان {n}".', f'{b}^{{{n}}}')]
    return steps, f'{b}^{{{n}}}'
