from pathlib import Path
import os, time
root = Path(r'D:\SpaceBook\SpaceBook Web')
lock = root / 'tmp/class-content-shared.lock'
lock.parent.mkdir(exist_ok=True)
for attempt in range(60):
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); break
    except FileExistsError:
        time.sleep(2)
else:
    raise SystemExit('Shared lock occupied for 2 minutes; retry later without removing it.')
try:
    os.write(fd, b'class-11 wire book isl')
    idx = root / 'index.html'
    t = idx.read_text(encoding='utf-8')
    tag = '  <script src="js/isl_11_data.js?v=20261012_1"></script>'
    if tag not in t:
        anchor = '  <script src="js/eng_11_data.js?v=20261012_1"></script>'
        assert t.count(anchor) == 1
        idx.write_text(t.replace(anchor, anchor + '\n' + tag), encoding='utf-8', newline='\n'); print('index.html tag added')
    dj = root / 'js/data.js'
    d = dj.read_text(encoding='utf-8')
    if '"id": "cls11-isl"' not in d:
        a1 = '      {\n        "id": "cls11-eng",\n        "name": "English",\n        "emoji": "📖",\n        "chapters": 24\n      }'
        assert d.count(a1) == 1
        d = d.replace(a1, a1 + ',\n      {\n        "id": "cls11-isl",\n        "name": "Islamiat (Compulsory)",\n        "emoji": "🕌",\n        "chapters": 7\n      }')
        b1 = '      "action": "cls11-eng"\n    },'
        assert d.count(b1) == 1
        card = ('\n    {\n      "id": "b-cls11-isl",\n      "classId": "cls11",\n      "className": "Class 11",\n      "subject": "Islamiat (Compulsory)",\n'
                '      "title": "Islamiat (Compulsory) 11th Class (HSSC-I)",\n      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",\n      "size": "Source review in progress",\n'
                '      "pages": "7 Units",\n      "pdfPath": "",\n      "color": "#0ea5e9",\n      "icon": "🕌",\n      "available": true,\n      "action": "cls11-isl"\n    },')
        d = d.replace(b1, b1 + card)
        dj.write_text(d, encoding='utf-8', newline='\n'); print('data.js subject + book added')
finally:
    os.close(fd)
    lock.unlink()
