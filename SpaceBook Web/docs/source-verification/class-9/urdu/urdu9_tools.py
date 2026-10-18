# -*- coding: utf-8 -*-
"""Load/save Class 9 Urdu (js/urdu_data.js, var URDU_DATA) and record page progress. printed = PDF - 2."""
import io, json, os, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
JS = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'js', 'urdu_data.js'))
PROGRESS = os.path.join(HERE, 'progress.json')
LOCK = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'tmp', 'class-content-shared.lock'))
LOAD = ("const fs=require('fs'),vm=require('vm');const c={window:{}};vm.createContext(c);"
        "vm.runInContext(fs.readFileSync(PATH,'utf8'),c);process.stdout.write(JSON.stringify(c.URDU_DATA));")


# Scans out of order (checked against the printed page numbers on the images).
PRINTED_OVERRIDE = {64: 64, 65: 63, 66: 62}


def printed_of(pdf):
    if pdf in PRINTED_OVERRIDE:
        return PRINTED_OVERRIDE[pdf]
    return pdf - 2 if pdf > 2 else None


def _parts():
    s = io.open(JS, encoding='utf-8', newline='').read()
    a = s.index('var URDU_DATA = [')
    b = s.index('\r\nif (typeof DATA') if '\r\nif (typeof DATA' in s else s.index('\nif (typeof DATA')
    return s[:a], s[b:], s


def load(path=None):
    out = subprocess.check_output(['node', '-e', LOAD.replace('PATH', json.dumps(path or JS))])
    return json.loads(out.decode('utf-8'))


def save(data):
    head, tail, orig = _parts()
    CRLF = chr(13) + chr(10)
    body = 'var URDU_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';' + chr(10)
    if CRLF in orig:
        body = body.replace(chr(10), CRLF)
    tmp = JS + '.tmp'
    io.open(tmp, 'w', encoding='utf-8', newline='').write(head + body + tail)
    if load(tmp) != data:
        os.remove(tmp)
        raise SystemExit('round-trip mismatch')
    os.replace(tmp, JS)


def lesson(data, n):
    return next(u for u in data if u['number'] == n)


def record_pages(entries, next_page=None):
    p = json.load(io.open(PROGRESS, encoding='utf-8')) if os.path.exists(PROGRESS) else dict(
        subject='Urdu', sourcePdf='D:/SpaceBook/Books/9th/9th urdu/PDF/9th Urdu.pdf', totalPdfPages=150, pages={})
    for pdf, status, note in entries:
        p['pages'][str(pdf)] = dict(printed=printed_of(pdf), status=status, note=note)
    p['counts'] = {}
    for v in p['pages'].values():
        p['counts'][v['status']] = p['counts'].get(v['status'], 0) + 1
    if next_page:
        p['nextPdfPage'] = next_page
    p['updatedAt'] = datetime.datetime.now().isoformat(timespec='seconds')
    json.dump(p, io.open(PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return p
