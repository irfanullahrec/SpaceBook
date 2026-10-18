"""Targeted Class 12 Physics fidelity fixes and page records (2026-10-12 source-fidelity pass).

Usage from other scripts:
    from class12_physics_fidelity_patch import replace_text, record_page
    replace_text(chapter_index, section_id, [(old, new, lang), ...])   # lang: en|ur|ps
    record_page(pdf, status, evidence, issues=[])
"""
import html, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from class12_source_review import OUT, DATA, replace_json, write_data, shared_class_data_lock
from class12_fidelity_repair import now, update_inventory
import contextlib, time as _time
_base_lock = shared_class_data_lock
@contextlib.contextmanager
def shared_class_data_lock():
    # wait (never force) for another agent's short lock to be released
    for _ in range(240):
        try:
            cm = _base_lock(); cm.__enter__(); break
        except FileExistsError:
            _time.sleep(0.5)
    else:
        raise TimeoutError('shared class-content lock held for over 2 minutes')
    try:
        yield
    finally:
        cm.__exit__(None, None, None)

FIELDS = {'en': ('text', 'english', 'originalText'), 'ur': ('urdu',), 'ps': ('pashto',)}
SEC_FIELDS = {'en': ('theory', 'content'), 'ur': ('urdu',), 'ps': ('pashto',)}

def _apply(section, record, changes):
    hits = 0
    for old, new, lang in changes:
        n = 0
        if lang == 'svg':  # any string in the section (svg fields, sourceBlocks, content)
            def walk(o):
                c = 0
                items = o.items() if isinstance(o, dict) else enumerate(o)
                for k, v in list(items):
                    if isinstance(v, str) and old in v: o[k] = v.replace(old, new); c += v.count(old)
                    elif isinstance(v, (dict, list)): c += walk(v)
                return c
            n = walk(section) + (walk(record) if record is not None else 0)
            if not n: raise ValueError(f'not found in {section["id"]}: {old!r}')
            hits += n; continue
        for p in section.get('paras', []):
            for k in FIELDS[lang]:
                if isinstance(p.get(k), str) and old in p[k]: p[k] = p[k].replace(old, new); n += 1
        for k in SEC_FIELDS[lang]:
            v = section.get(k)
            if isinstance(v, str):
                for o, nw in ((old, new), (html.escape(old), html.escape(new))):
                    if o in v: section[k] = v = v.replace(o, nw); n += 1
        if record is not None and lang == 'en':
            record['paragraphs'] = [q.replace(old, new) for q in record['paragraphs']]
        if not n: raise ValueError(f'not found in {section["id"]}: {old!r}')
        hits += n
    return hits

def replace_text(chapter_index, sid, changes):
    mutate(chapter_index, sid, lambda sec, rec: _apply(sec, rec, changes))

def mutate(chapter_index, sid, fn):
    """fn(section, record_or_None) mutates in place; persisted like replace_text."""
    _apply_orig = _apply
    def _apply_local(section, record, _changes): fn(section, record)
    with shared_class_data_lock():
        if chapter_index:
            unit = 11 + chapter_index
            sp, rp = OUT / f'physics-sections-unit{unit}.json', OUT / f'physics-corrections-unit{unit}.json'
            secs, recs = json.loads(sp.read_text(encoding='utf-8')), json.loads(rp.read_text(encoding='utf-8'))
            section = next(s for s in secs if s['id'] == sid); record = next((r for r in recs if r['id'] == sid), None)
            _apply_local(section, record, None)
            from class12_source_review import upsert
            upsert([record] if record else [], [section], chapter_index)
        else:
            text = DATA.read_text(encoding='utf-8')
            holder = {}
            sec_prefix = 'PHYS_12_DATA[0].sections.unshift(...'
            rec_prefix = 'PHYS_12_DATA[0].reviewedSourcePages = '
            def get_rec(items): holder['rec'] = next((r for r in items if r['id'] == sid), None)
            replace_json(text, rec_prefix, get_rec)
            def mut_sec(items): _apply_local(next(s for s in items if s['id'] == sid), holder['rec'], None)
            text = replace_json(text, sec_prefix, mut_sec)
            if holder['rec'] is not None:
                def put_rec(items):
                    for i, r in enumerate(items):
                        if r['id'] == sid: items[i] = holder['rec']
                text = replace_json(text, rec_prefix, put_rec)
            write_data(text)
            cache = OUT / 'physics-corrections.json'
            saved = json.loads(cache.read_text(encoding='utf-8'))
            if holder['rec'] is not None:
                for i, r in enumerate(saved):
                    if r['id'] == sid: saved[i] = holder['rec']
                cache.write_text(json.dumps(saved, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def record_page(pdf, status, evidence, issues=None):
    path = OUT / 'progress.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    repair = data['fidelityRepair']
    entry = next(e for e in data['pages'] if e['pdfPage'] == pdf)
    entry.update(status=status, evidence=evidence, fidelityVerifiedUtc=now())
    for issue in issues or []:
        rec = {'pdfPage': pdf, 'issue': issue}
        if rec not in data['unresolvedItems']: data['unresolvedItems'].append(rec)
    if pdf not in repair['completedPages']: repair['completedPages'].append(pdf)
    pending = [n for n in repair['queue'] if n not in repair['completedPages']]
    repair['nextPage'] = pending[0] if pending else None
    data.update(nextPage=repair['nextPage'] or 202, lastInspectedPage=max(data.get('lastInspectedPage', 0), pdf),
                nextAction=(f"Physics source-fidelity repair: render and inspect PDF{repair['nextPage']} against the active records "
                            "(tools/class12_physics_fidelity_patch.py for fixes and records). Biology complete." if repair['nextPage']
                            else 'Physics fidelity repair complete; continue with Chemistry per subjectOrder2026_10_12.'))
    verified = [n for n in repair['completedPages'] if next(x for x in data['pages'] if x['pdfPage'] == n)['status'] in ('corrected_verified', 'verified_unchanged')]
    repair['benchmark'].update(processedPages=repair['completedPages'][:], verifiedPages=verified, measuredUtc=now())
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    update_inventory(data)
    print(f'recorded PDF{pdf} {status}; next PDF{repair["nextPage"]}')
