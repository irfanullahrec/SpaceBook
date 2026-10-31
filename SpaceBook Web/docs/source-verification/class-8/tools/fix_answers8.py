"""fix_answers8.py - Class 7 and 8 Mathematics: wrong or hard-to-read answer lines found by tools/launch/answer_match_audit.js (2026-10-30).

    python fix_answers8.py [--dry]

1. Class 8: the authored rows in math/dsl/ex_fix.txt (factorize a^2 - 49, divide (x^5 - y^5) by (x - y) ...) replace what the engine had put in
   math/gen_solutions.json (an answer that only repeated the question, or a quotient left as separate fractions).
2. Class 7 and 8: a solution whose working ends in a decimal but whose answer line is the same number written as a fraction or mixed number
   (sqrt(7.84) = 2.8 shown as 2 4/5, (0.98)^2 = 0.9604 shown as 2401/2500) gets the decimal as its answer line.
msol_run.py does the same for a new run of the engine. Run apply_gen8.py (Class 8) and build_math7.py (Class 7) afterwards to rewrite js/. Idempotent."""
import json, re, sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]                     # .../class-8
SV = HERE.parent                                               # .../source-verification
sys.path.insert(0, str(SV / 'class-7' / 'tools'))
import msol_run                                                # noqa: E402  (the engine of Classes 7 and 8)

DEC = re.compile(r'-?\d*\.\d+')


def decimal_answers(gen, label):
    n = 0
    for key, v in gen.items():
        st = v.get('steps') or []
        if len(st) < 3 or not st[-1].get('m') or not st[-2].get('m') or '\\frac' not in st[-1]['m']:
            continue
        prev = st[-2]['m'].strip()
        if not DEC.fullmatch(prev) or '\\frac' in (st[0].get('m') or ''):
            continue
        if re.fullmatch(r'(-?)(\d+)\\frac\{(\d+)\}\{(\d+)\}', st[-1]['m'].replace(' ', '')):
            w = re.fullmatch(r'(-?)(\d+)\\frac\{(\d+)\}\{(\d+)\}', st[-1]['m'].replace(' ', ''))
            val = Fraction(int(w.group(2)) * int(w.group(4)) + int(w.group(3)), int(w.group(4))) * (-1 if w.group(1) else 1)
        else:
            f = re.fullmatch(r'(-?)\\frac\{(\d+)\}\{(\d+)\}', st[-1]['m'].replace(' ', ''))
            if not f:
                continue
            val = Fraction(int(f.group(2)), int(f.group(3))) * (-1 if f.group(1) else 1)
        if val != Fraction(prev):
            raise SystemExit('%s %s: working %s but answer %s' % (label, key, prev, st[-1]['m']))
        st[-1]['m'] = prev
        v['answer'] = '$' + prev + '$' if '$' in str(v.get('answer', '')) else prev
        n += 1
    return n


def main():
    dry = '--dry' in sys.argv
    p8 = HERE / 'math' / 'gen_solutions.json'
    p7 = SV / 'class-7' / 'math' / 'gen_solutions.json'
    g8 = json.loads(p8.read_text(encoding='utf-8'))
    g7 = json.loads(p7.read_text(encoding='utf-8'))
    # 1. authored rows
    dsl = msol_run.load_dsl('8')
    mine = {}
    for ln in (HERE / 'math' / 'dsl' / 'ex_fix.txt').read_text(encoding='utf-8').splitlines():
        ln = ln.strip()
        if ln and not ln.startswith('#') and '~' in ln:
            mine[ln.split('~', 1)[0].strip()] = True
    done = 0
    for key in mine:
        rows, note, ans, force, unv = dsl[key]
        steps, final, lastv = msol_run.dsl_solution(rows, note, None, ans)
        final = msol_run.textify(ans) if ans else final
        steps.append(msol_run.step('ans', final))
        g8[key] = {'steps': steps, 'answer': msol_run.wrap_math(final), 'verified': False}
        done += 1
    print('Class 8 authored answers set:', done)
    # 2. decimals
    print('Class 8 decimal answer lines:', decimal_answers(g8, 'class 8'))
    print('Class 7 decimal answer lines:', decimal_answers(g7, 'class 7'))
    if not dry:
        p8.write_text(json.dumps(g8, ensure_ascii=False), encoding='utf-8')
        p7.write_text(json.dumps(g7, ensure_ascii=False), encoding='utf-8')


if __name__ == '__main__':
    main()
