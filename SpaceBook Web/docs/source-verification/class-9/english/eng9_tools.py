# -*- coding: utf-8 -*-
"""Load/save Class 9 English (js/english_data.js, const ENGLISH_DATA) and record page progress."""
import io, json, os, re, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
JS = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'js', 'english_data.js'))
PROGRESS = os.path.join(HERE, 'progress.json')
LOCK = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'tmp', 'class-content-shared.lock'))
PRINT_OFFSET = 9  # printed page = PDF page - 9 for lesson pages


DUPLICATES = {118: 107, 119: 108, 150: 139}  # PDF page -> printed page it repeats
MISSING_PRINTED = [137]                      # printed pages absent from every scan checked


def printed_of(pdf):
    """Printed page number of a PDF page (from footer OCR, verified on images)."""
    if pdf <= PRINT_OFFSET:
        return None
    if pdf in DUPLICATES:
        return DUPLICATES[pdf]
    if pdf <= 117:
        return pdf - 9
    if pdf <= 147:
        return pdf - 11
    if pdf <= 149:
        return pdf - 10   # printed 137 is missing: PDF 147=136, PDF 148=138
    return pdf - 11


def _split():
    s = io.open(JS, encoding='utf-8', newline='').read()
    i = s.index('const ENGLISH_DATA = ')
    return s[:i], s


def load():
    head, s = _split()
    out = subprocess.check_output(['node', '-e', f"""
const fs=require('fs'),vm=require('vm');const c={{}};vm.createContext(c);
vm.runInContext(fs.readFileSync({json.dumps(JS)},'utf8').replace(/const ENGLISH_DATA/,'var ENGLISH_DATA'),c);
process.stdout.write(JSON.stringify(c.ENGLISH_DATA));"""])
    return json.loads(out.decode('utf-8'))


CHECK = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
         "vm.runInContext(fs.readFileSync(PATH,'utf8').replace(/const ENGLISH_DATA/,'var ENGLISH_DATA'),c);"
         "if(!Array.isArray(c.ENGLISH_DATA)||c.ENGLISH_DATA.length!==15) throw new Error('bad english data');")


def save(data):
    head, orig = _split()
    CRLF = chr(13) + chr(10)
    crlf = CRLF in orig
    head = head.replace(CRLF, chr(10))
    body = head + 'const ENGLISH_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';' + chr(10)
    if crlf:
        body = body.replace(chr(10), CRLF)
    tmp = JS + '.tmp'
    io.open(tmp, 'w', encoding='utf-8', newline='').write(body)
    subprocess.check_call(['node', '-e', CHECK.replace('PATH', json.dumps(tmp))])
    os.replace(tmp, JS)


def unit(data, n):
    return next(u for u in data if u['number'] == n)


def record_pages(entries, next_page=None):
    p = json.load(io.open(PROGRESS, encoding='utf-8'))
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
