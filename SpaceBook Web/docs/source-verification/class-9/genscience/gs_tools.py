# -*- coding: utf-8 -*-
"""Class 9 General Science tools: load/save js/general_science_9_data.js, page map, progress."""
import io, os, json, datetime, re

APP = r'D:\SpaceBook\SpaceBook Web'
DATA_JS = os.path.join(APP, 'js', 'general_science_9_data.js')
LOCK = os.path.join(APP, 'tmp', 'class-content-shared.lock')
HERE = os.path.dirname(os.path.abspath(__file__))
PROGRESS = os.path.join(HERE, 'progress.json')
JPG = 'D:/SpaceBook/Books/9th/9th General Science/JPG/General Science 9th book EM_page_%03d.jpg'
HEAD = '// Class 9 General Science Dataset (KPTBB)\nconst GENERAL_SCIENCE_9_DATA = '
TAIL = (";\n\nif (typeof DATA !== 'undefined' && DATA) { DATA.genSci9Chapters = GENERAL_SCIENCE_9_DATA; }\n"
        "if (typeof window !== 'undefined') { window.GENERAL_SCIENCE_9_DATA = GENERAL_SCIENCE_9_DATA; }\n")


def printed_of(g):
    """JPG g (1-197): 1 cover, 2 advert, 3-4 contents, then printed page = g - 4."""
    return g - 4 if g >= 5 else None


def load():
    s = io.open(DATA_JS, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    body = s[s.index('const GENERAL_SCIENCE_9_DATA = ') + len('const GENERAL_SCIENCE_9_DATA = '):]
    body = body[:body.rindex('];') + 1]
    return json.loads(body)


def save(data):
    txt = HEAD + json.dumps(data, ensure_ascii=False, indent=2) + TAIL
    assert json.loads(txt[len(HEAD):txt.rindex('];') + 1]) == data
    io.open(DATA_JS, 'w', encoding='utf-8', newline='').write(txt.replace('\n', '\r\n'))


def record_pages(entries):
    p = json.load(io.open(PROGRESS, encoding='utf-8')) if os.path.exists(PROGRESS) else dict(
        subject='General Science', source='D:/SpaceBook/Books/9th/9th General Science/JPG (197 pages)', pages={})
    for g, status, note in entries:
        p['pages'][str(g)] = dict(jpg=g, printed=printed_of(g), status=status, note=note)
    p['counts'] = {}
    for v in p['pages'].values():
        p['counts'][v['status']] = p['counts'].get(v['status'], 0) + 1
    p['updatedAt'] = datetime.datetime.now().isoformat(timespec='seconds')
    json.dump(p, io.open(PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return p
