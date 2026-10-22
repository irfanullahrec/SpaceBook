"""Class 8 Maths: last residue. Every stub part that still has no worked solution (figure too small to read, data cropped in the scan,
information not in the book) gets an honest labelled entry: the printed key when there is one, otherwise the method.
Needs tmp/m8_leaves.json. Idempotent (re-reads its own output). Writes class-8/math/dsl/u8v.txt."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parent / 'math' / 'dsl' / 'u8v.txt'
g = json.load(open(HERE.parent / 'math' / 'gen_solutions.json', encoding='utf8'))
leaves = json.load(open(ROOT / 'tmp' / 'm8_leaves.json', encoding='utf8'))
own = {ln.split(' ~')[0] for ln in OUT.read_text(encoding='utf-8').splitlines() if ' ~' in ln} if OUT.exists() else set()
L = []
BAD = ('|', '~', ';;', '=>', '@@', '%%')


def clean(t):
    t = re.sub(r'\s+', ' ', t or '').strip()
    return '' if any(c in t for c in BAD) else t


for l in leaves:
    ex = l['ex']
    for p in ([p for p, _ in l['parts']] or ['']):
        k = f"{ex}|{l['q']}|{p}"
        if k in g and k not in own:
            continue
        key = clean(str(l.get('key') or ''))
        if key and key != 'None':
            en = (f'The figure or data for this item is not legible in the scan (or is not given in the book), so a worked solution cannot be built from it. '
                  f'The printed key gives: {key}')
            ur = (f'اس سوال کی شکل یا معلومات سکین میں پڑھی نہیں جا سکتیں (یا کتاب میں نہیں دی گئیں)، اس لیے مرحلہ وار حل نہیں بن سکتا۔ چھپی کلید کے مطابق: {key}')
            ps = (f'د دې پوښتنې انځور یا معلومات په سکین کې نه لوستل کیږي (یا په کتاب کې نه دي ورکړل شوي)، نو ګام په ګام حل نه جوړیږي. د چاپ شوې کلیل له مخې: {key}')
            ans = key
        else:
            en = ('The figure for this item is not legible in the scan, so only the method can be given: read the coordinates or lengths from the figure, '
                  'apply the rule of the section (rotation, enlargement, congruence or construction) step by step, and check the result against the figure.')
            ur = ('اس سوال کی شکل سکین میں پڑھی نہیں جا سکتی، اس لیے صرف طریقہ دیا جا سکتا ہے: شکل سے محدد یا لمبائیاں پڑھیں، حصے کے قاعدے (گردش، بڑا کرنا، مطابقت یا تعمیر) کو مرحلہ وار لگائیں اور نتیجہ شکل سے جانچیں۔')
            ps = ('د دې پوښتنې انځور په سکین کې نه لوستل کیږي، نو یوازې طریقه ورکول کیږي: له انځور څخه همغږي یا اوږدوالی ولولئ، د برخې قاعده (ګرځېدنه، لویول، همغږي یا جوړونه) ګام په ګام وکاروئ او پایله له انځور سره وارزوئ.')
            ans = 'Method only (figure not legible)'
        L.append(f'{k} ~ @text {en}|{ur}|{ps} => {ans} %%')
OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
print(len(L), 'residue rows ->', OUT)
