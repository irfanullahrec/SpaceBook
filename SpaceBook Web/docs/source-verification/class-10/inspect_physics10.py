import json
from pathlib import Path
text = Path(r'D:\SpaceBook\SpaceBook Web\js\data_phys.js').read_text(encoding='utf-8')
start = text.index('"phys10Chapters": [')
end = text.index('\n});',start)
chapters = json.loads('{'+text[start:end]+'}')['phys10Chapters']
print(json.dumps(chapters[0]['numericals'],ensure_ascii=False,indent=2))
