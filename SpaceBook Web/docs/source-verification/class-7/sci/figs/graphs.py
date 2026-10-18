"""graphs.py KEY 'linegraph spec' [KEY spec ...] -> adds to graphs.json"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
import figs
p = Path(__file__).with_name('graphs.json')
d = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
a = sys.argv[1:]
for k, spec in zip(a[::2], a[1::2]):
    d[k] = figs.linegraph(spec)
p.write_text(json.dumps(d), encoding='utf-8'); print('ok', list(d))
