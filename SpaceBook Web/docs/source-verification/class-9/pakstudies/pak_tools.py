# -*- coding: utf-8 -*-
"""Class 9 Pakistan Studies: scan map, load/save js/pakstudy_data.js (var PAKSTUDY_DATA), progress records.
Global scan g = 1..114 over pakstudy1/2/3.pdf (38 pages each). Printed page map checked against the page images."""
import io, json, os, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
JS = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'js', 'pakstudy_data.js'))
PROGRESS = os.path.join(HERE, 'progress.json')
LOCK = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'tmp', 'class-content-shared.lock'))
DUPLICATE = {11: 10, 39: 38, 77: 76}           # duplicate scan -> first scan of the same printed page
FRONT = {1: 'cover', 2: 'Quran/hadith panel', 3: 'title page', 4: 'imprint', 5: 'contents', 6: 'hadith panel'}
BACK = {110: 'hadith panel', 111: 'back matter', 112: 'back matter', 113: 'back matter', 114: 'back cover'}
MISSING_PRINTED = [52]


def printed_of(g):
    if g in FRONT or g in BACK:
        return None
    if g in DUPLICATE:
        return printed_of(DUPLICATE[g])
    if g <= 10:
        return g - 6
    if g <= 38:
        return g - 7
    if g <= 59:
        return g - 8
    if g <= 76:
        return g - 7
    return g - 8


def source_of(g):
    return f'pakstudy{(g - 1) // 38 + 1}.pdf p{(g - 1) % 38 + 1}'


LOAD = ("const fs=require('fs'),vm=require('vm');const c={window:{}};vm.createContext(c);"
        "vm.runInContext(fs.readFileSync(PATH,'utf8'),c);process.stdout.write(JSON.stringify(c.PAKSTUDY_DATA));")


def load(path=None):
    return json.loads(subprocess.check_output(['node', '-e', LOAD.replace('PATH', json.dumps(path or JS))]).decode('utf-8'))


def save(data):
    s = io.open(JS, encoding='utf-8', newline='').read()
    a = s.index('var PAKSTUDY_DATA = [')
    b = s.rindex('];') + 2
    nl = '\r\n' if '\r\n' in s else '\n'
    body = 'var PAKSTUDY_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
    body = body.replace('\n', nl)
    tmp = JS + '.tmp'
    io.open(tmp, 'w', encoding='utf-8', newline='').write(s[:a] + body + s[b:])
    if load(tmp) != data:
        os.remove(tmp); raise SystemExit('round-trip mismatch')
    os.replace(tmp, JS)


def record_pages(entries):
    p = json.load(io.open(PROGRESS, encoding='utf-8')) if os.path.exists(PROGRESS) else dict(
        subject='Pakistan Studies', sourcePdfs=['D:/SpaceBook/Books/9th/9th Pak Study/PDF/pakstudy%d.pdf' % i for i in (1, 2, 3)],
        totalScans=114, missingPrintedPages=MISSING_PRINTED, pages={})
    for g, status, note in entries:
        p['pages'][str(g)] = dict(source=source_of(g), printed=printed_of(g), status=status, note=note)
    p['counts'] = {}
    for v in p['pages'].values():
        p['counts'][v['status']] = p['counts'].get(v['status'], 0) + 1
    p['updatedAt'] = datetime.datetime.now().isoformat(timespec='seconds')
    json.dump(p, io.open(PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return p
