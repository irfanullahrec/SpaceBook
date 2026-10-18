"""Hard-link Class 5 JPG scans 0-based as D:/SpaceBook/_cls5_jpg/<subj>/NNN.jpg (scan _page_001 -> 000.jpg)."""
import os, re, sys
from pathlib import Path
BOOKS = Path(r'D:\SpaceBook\Books\5th')
DST = Path(r'D:\SpaceBook\_cls5_jpg')
SUBJ = {'math': '5th Maths', 'eng': '5th English', 'sci': '5th General Science', 'urdu': '5th Urdu', 'isl': '5th Islamiat',
        'sst': '5th Social Study', 'sstum': '5th Social Study UM', 'pashto': '5th Pashto'}
for key in (sys.argv[1:] or SUBJ):
    out = DST / key
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted((BOOKS / SUBJ[key] / 'JPG').glob('*.jpg')):
        m = re.search(r'_page_(\d+)\.jpg$', f.name)
        t = out / f'{int(m.group(1)) - 1:03}.jpg'
        if not t.exists():
            os.link(f, t)
        n += 1
    print(key, n)
