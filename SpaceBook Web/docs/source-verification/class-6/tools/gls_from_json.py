"""Write glossary .gls sources from a JSON list.

Usage: python tools/gls_from_json.py SUBJ FILE.json
Each item: {"scan": 102, "printed": 89, "lesson": 7, "ord": "السَّابِعُ", "en": "Lesson 7", "ps": "اووم لوست",
            "rows": ["AR = UR = EN = PS", ...]}
Then run tools/gloss_expand.py SUBJ NNN... to build the pages.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
subj, path = sys.argv[1], sys.argv[2]
for it in json.loads(Path(path).read_text(encoding='utf-8')):
    L = [f"@printed {it['printed']}", '@status back-matter',
         f"@sec 26-{it['lesson']} | فرہنگ: الدرس {it['ord']} || Glossary: {it['en']} || لغتنامه: {it['ps']}",
         '@tab glossary', f"## **اَلدَّرْسُ {it['ord']}** || {it['en']} || {it['ps']}"]
    L += ['g ' + r for r in it['rows']]
    L += it.get('extra', [])
    (HERE / subj / 'src' / f"p{it['scan']:03}.gls").write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('wrote', f"p{it['scan']:03}.gls")
