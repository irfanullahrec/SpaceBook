"""fix_echo_answers7.py - Class 7 Maths: the answer line of an "equivalent fractions" or "mixed number to improper fraction" solution repeated the given fraction
(1.4 Q2, 1.5 Q2, Review 1 Q4: 17 questions, found by tools/launch/answer_match_audit.js 2026-10-30). The working above the answer line was right
(7/24 -> 14/48, 21/72, 28/96; 3 5/6 -> 23/6) but the line a student reads as THE answer said 7/24 and 3 5/6.

    python fix_echo_answers7.py [--dry]

msol_run.py now writes the right answer line; this script puts the same line into the stored math/gen_solutions.json (so build_math7.py picks it up
without running the whole engine again). Idempotent: an entry whose answer line is no longer the given line is left alone."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
GEN = HERE / 'math' / 'gen_solutions.json'
EQ = 'Multiply the numerator and denominator by the same number'
IMP = 'Mixed number to improper fraction'


def main():
    dry = '--dry' in sys.argv
    gen = json.loads(GEN.read_text(encoding='utf-8'))
    fixed = 0
    for key, v in gen.items():
        st = v.get('steps') or []
        if len(st) < 3 or not st[0].get('m') or not st[1].get('en', '').startswith((EQ, IMP)):
            continue
        given, last = st[0]['m'].replace(' ', ''), st[-1].get('m', '').replace(' ', '')
        if given != last:
            continue
        if st[1]['en'].startswith(EQ):
            m = re.fullmatch(r'\\frac\{(-?\d+)\}\{(-?\d+)\}', given)
            if not m:
                raise SystemExit('cannot read %s: %s' % (key, given))
            a, b = int(m.group(1)), int(m.group(2))
            tex = ',\\ '.join('\\frac{%d}{%d}' % (a * k, b * k) for k in (2, 3, 4))
        else:
            m = re.fullmatch(r'(\d+)\\frac\{(\d+)\}\{(\d+)\}', given)
            if not m:
                raise SystemExit('cannot read %s: %s' % (key, given))
            w, n, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
            tex = '\\frac{%d}{%d}' % (w * d + n, d)
        st[-1]['m'] = tex
        v['answer'] = '$' + tex + '$'
        fixed += 1
        print(key, '->', tex)
    print('answer lines corrected:', fixed)
    if not dry:
        GEN.write_text(json.dumps(gen, ensure_ascii=False), encoding='utf-8')


if __name__ == '__main__':
    main()
