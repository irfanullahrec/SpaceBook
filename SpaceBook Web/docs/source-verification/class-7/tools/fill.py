"""fill.py SUBJ PAGEFILE... : replace {{key}} placeholders with SVG from SUBJ/figs/*.json (merged)."""
import sys, json, re
from pathlib import Path
here = Path(__file__).resolve().parent.parent
subj = sys.argv[1]; d = {}
for f in sorted((here/subj/'figs').glob('*.json')): d.update(json.load(open(f, encoding='utf-8')))
for p in sys.argv[2:]:
    p = Path(p); s = p.read_text(encoding='utf-8')
    s2 = re.sub(r'\{\{(\w+)\}\}', lambda m: d[m.group(1)], s)
    if s2 != s: p.write_text(s2, encoding='utf-8'); print('filled', p)
