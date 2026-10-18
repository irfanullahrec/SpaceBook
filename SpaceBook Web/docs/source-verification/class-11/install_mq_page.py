"""Install a source-reviewed English scan; validate before replacing active data."""
import json, pathlib, re, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
TARGET = ROOT / 'js/mq_11_data.js'
page_file = pathlib.Path(sys.argv[1]).resolve()
record = json.loads(page_file.read_text(encoding='utf-8'))
page = record['source']['pdfPage']
assert 1 <= page <= 193
chapter = record.pop('chapter')
vocab = record.pop('vocabulary', {})
paras = record.pop('paras')
calls = []
for row in paras:
    en, ur, ps = row.pop('en'), row.pop('ur'), row.pop('ps')
    assert en and ur and ps and row.get('id')
    calls.append('mq11Pair(' + ','.join(json.dumps(x, ensure_ascii=False) for x in (ur, en, ps, row)) + ')')
record['paras'] = '__PAIRS__'
section = json.dumps(record, ensure_ascii=False).replace('"__PAIRS__"', '[\n' + ',\n'.join(calls) + '\n]')
start = f'// BEGIN MQ SOURCE SCAN {page}'
end = f'// END MQ SOURCE SCAN {page}'
block = start + '\nmq11AddSection(' + json.dumps(chapter) + ',' + section + ');\n'
for term, meanings in vocab.items():
    block += 'mq11WordVocabulary[' + json.dumps(term) + ']=' + json.dumps(meanings, ensure_ascii=False) + ';\n'
block += end + '\n'
text = TARGET.read_text(encoding='utf-8')
if start in text:
    a, b = text.index(start), text.index(end) + len(end)
    candidate = text[:a] + block.rstrip() + text[b:]
else:
    legacy = re.search(r'^const chem11P' + str(page) + r'\s*=.*$', text, re.M)
    if legacy:
        close = re.search(r'^chem11AddSection\([^\n]*pdfPage\s*:\s*' + str(page) + r'\b[^\n]*\);', text[legacy.start():], re.M)
        assert close, 'Cannot safely locate legacy page boundary'
        b = legacy.start() + close.end()
        candidate = text[:legacy.start()] + block.rstrip() + text[b:]
    else:
        assert not re.search(r'pdfPage\s*:\s*' + str(page) + r'\b', text), 'Existing page needs explicit boundary review'
        candidate = text.rstrip() + '\n\n' + block
assert len({r['id'] for r in paras}) == len(paras), 'Duplicate IDs in page'
tmp = ROOT / 'tmp/class-11/mq-data-candidate.js'
tmp.write_text(candidate, encoding='utf-8')
subprocess.run(['node', '--check', str(tmp)], check=True)
assert TARGET.read_text(encoding='utf-8') == text, 'Data changed during validation; retry with fresh read'
TARGET.write_text(candidate, encoding='utf-8')
print(f'Installed scan {page}: {len(paras)} source paragraphs/options with paired translations')
