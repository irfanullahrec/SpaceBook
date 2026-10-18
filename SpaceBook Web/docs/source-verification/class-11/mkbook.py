"""Generate a Class 11 source-reader toolchain for one book by cloning the English one.
Usage: python mkbook.py CONFIG.json   (see books/<key>.json for the format)
Creates: js/<key>_11_data.js, <key>lib.py, <key>help.py, install_<key>_page.py, finalize_<key>_page.py,
verify_<key>_pages.cjs, <key>-progress.json and wire_book_<key>.py.  Refuses to overwrite an existing data file."""
import json, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
cfg = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
k = cfg['key']; K = k.upper(); name = cfg['name']; Name = cfg['funcName']
src = cfg.get('srcLang', 'ur'); N = cfg['scans']
data_js = ROOT / f'js/{k}_11_data.js'
assert not data_js.exists(), f'{data_js} exists; will not overwrite'
eng = (ROOT / 'js/eng_11_data.js').read_text(encoding='utf-8')
a = eng.index('function eng11AddSection')
b = eng.index('// BEGIN ENGLISH SOURCE SCAN 1')
code = eng[a:b]
code = re.sub(r'const eng11WordVocabulary = \{.*?\};\n', 'const eng11WordVocabulary = {};\n', code, count=1, flags=re.S)
extras = cfg['extraTabs']
code = code.replace("['glossary','vocabulary','language','grammar','writing']", json.dumps(extras).replace('"', "'").replace(', ', ','))
code = code.replace('renderEnglish11Tab', f'render{Name}11Tab').replace('english11SourceSearchText', f'{k}11SourceSearchText')
code = code.replace('ENG_11', f'{K}_11').replace('eng11', f'{k}11')
# chapters
rows = []
for cid, num, t, tu, tp in cfg['chapters']:
    rows.append("  { id: '%s11-%s', number: %s, title: %s, titleUrdu: %s, titlePashto: %s, pageRange: '', verificationStatus: 'draft: exact source comparison pending', sections: [] }" % (k, cid, (repr(num) if not str(num).isdigit() else num), json.dumps(t, ensure_ascii=False), json.dumps(tu, ensure_ascii=False), json.dumps(tp, ensure_ascii=False)))
head = (f"// Class 11 {name}: page-by-page source records transcribed from the KPTBB scans\n// ({cfg['folder']}, {N} scans). Section source.pdfPage holds the scan number (1..{N}).\n"
        f"const {K}_11_DATA = [\n" + ',\n'.join(rows) + "\n];\n\n")
tail = ''
if src == 'ur':
    tail += f"""
// Urdu-source book: the printed text (Urdu/Arabic) is shown first; English and Pashto renderings are provided below it.
function {k}11Pair(original, english, pashto, extra = {{}}) {{
  return {{ original, text: original, english, pashto, ...extra }};
}}
function {k}11RenderPair(p) {{
  const safe = value => typeof sanitize === 'function' ? sanitize(value) : String(value ?? '');
  let original = safe(p.original), english = safe(p.english), pashto = safe(p.pashto);
  if (p.listType === 'poem') {{ const br = s => s.split(String.fromCharCode(10)).join('<br>'); original = br(original); english = br(english); pashto = br(pashto); }}
  const id = safe(p.id || '');
  const gap = p.sourceGap ? `<p class="{k}11-source-note"><strong>Unresolved source:</strong> ${{safe(p.sourceGap.note)}}</p>` : '';
  const tag = p.kind === 'heading' ? 'h4' : 'p';
  const wrapper = p.kind === 'aside' ? 'aside' : 'article';
  return `<${{wrapper}} data-source-id="${{id}}"><${{tag}} lang="ur" dir="rtl">${{original}}</${{tag}}><details><summary>English / پښتو</summary><p lang="en">${{english}}</p><p lang="ps" dir="rtl">${{pashto}}</p></details>${{gap}}</${{wrapper}}>`;
}}
function {k}11RenderTable(table) {{
  const safe = value => typeof sanitize === 'function' ? sanitize(value) : String(value ?? '');
  const tr = (c) => `<details><summary>English / پښتو</summary><span lang="en">${{safe(c.en)}}</span><br><span lang="ps" dir="rtl">${{safe(c.ps)}}</span></details>`;
  return `<div class="{k}11-table-wrap"><table><caption lang="ur" dir="rtl">${{safe(table.captionUrdu)}}<details><summary>English / پښتو</summary><span lang="en">${{safe(table.caption)}}</span><br><span lang="ps" dir="rtl">${{safe(table.captionPashto)}}</span></details></caption><thead><tr>${{table.headers.map(h => `<th scope="col" lang="ur" dir="rtl">${{safe(h.ur)}}${{tr(h)}}</th>`).join('')}}</tr></thead><tbody>${{table.rows.map(row => `<tr>${{row.map(cell => `<td lang="ur" dir="rtl">${{safe(cell.ur).replace(/\\n/g, '<br>')}}${{cell.sourceGap ? `<p class="{k}11-source-note">Unresolved source: ${{safe(cell.sourceGap.note)}}</p>` : ''}}${{tr(cell)}}</td>`).join('')}}</tr>`).join('')}}</tbody></table></div>`;
}}
function {k}11SourceSearchText(ch) {{
  return [ch.title, ch.titleUrdu, ch.titlePashto, ...(ch.sections || []).flatMap(sec => [
    sec.title, sec.headingUrdu, sec.headingPashto,
    ...(sec.paras || []).flatMap(p => [p.original, p.english, p.pashto]),
    ...(sec.tables || []).flatMap(t => [t.caption, t.captionUrdu, ...(t.rows || []).flat().flatMap(c => [c.en, c.ur])])
  ])].filter(Boolean).join(' ');
}}
"""
tabs_js = json.dumps(cfg['tabs'], ensure_ascii=False)
tail += f"""
(window.CLASS11_BOOKS = window.CLASS11_BOOKS || {{}})['{k}'] = {{
  key: '{k}', subjectId: 'cls11-{k}', data: {K}_11_DATA, render: render{Name}11Tab, searchText: {k}11SourceSearchText,
  tabs: {tabs_js}, pdf: {json.dumps(cfg['pdf'])}, badge: {json.dumps('📖 Class 11 ' + name, ensure_ascii=False)}
}};
"""
data_js.write_text(head + code.rstrip() + '\n' + tail, encoding='utf-8', newline='\n')
# lib / help
lib = (HERE / 'englib.py').read_text(encoding='utf-8').replace('eng11-', f'{k}11-').replace('eng-page-', f'{k}-page-').replace('Class 11 English', f'Class 11 {name}').replace("sourceLanguage='en'", f"sourceLanguage='{src}'")
(HERE / f'{k}lib.py').write_text(lib, encoding='utf-8')
hlp = (HERE / 'enghelp.py').read_text(encoding='utf-8').replace('from englib', f'from {k}lib').replace('eng11-', f'{k}11-')
(HERE / f'{k}help.py').write_text(hlp, encoding='utf-8')
# install
ins = (HERE / 'install_eng_page.py').read_text(encoding='utf-8')
ins = ins.replace('eng_11_data.js', f'{k}_11_data.js').replace('eng11', f'{k}11').replace('english-data-candidate', f'{k}-data-candidate').replace('ENGLISH SOURCE SCAN', f'{K} SOURCE SCAN').replace('<= 240', f'<= {N}')
if src == 'ur':
    ins = ins.replace("for x in (en, ur, ps, row)", "for x in (ur, en, ps, row)")
(HERE / f'install_{k}_page.py').write_text(ins, encoding='utf-8')
# finalize
fin = (HERE / 'finalize_eng_page.py').read_text(encoding='utf-8').replace('eng-page-', f'{k}-page-').replace('install_eng_page.py', f'install_{k}_page.py').replace('verify_eng_pages.cjs', f'verify_{k}_pages.cjs').replace('english-progress.json', f'{k}-progress.json').replace("English 11 (240 half-page scans)", f"{name} 11 ({N} scans)").replace('English scan page', f'{name} scan page')
(HERE / f'finalize_{k}_page.py').write_text(fin, encoding='utf-8')
# verify
ver = (HERE / 'verify_eng_pages.cjs').read_text(encoding='utf-8').replace('eng_11_data.js', f'{k}_11_data.js').replace('ENG_11_DATA', f'{K}_11_DATA').replace('eng11WordVocabulary', f'{k}11WordVocabulary').replace('renderEnglish11Tab', f'render{Name}11Tab').replace('eng-page-', f'{k}-page-').replace('vm.createContext({sanitize: escape})', 'vm.createContext({sanitize: escape, window: {}})')
if src == 'ur':
    ver = ver.replace('assert.equal(actual.original,row.en,row.id+\' English\');', "assert.equal(actual.original,row.ur,row.id+' Urdu source');")
    ver = ver.replace('assert.equal(actual.urdu,row.ur,row.id+\' Urdu\');', "assert.equal(actual.english,row.en,row.id+' English');")
    ver = ver.replace("if (/[A-Za-z]{4}/.test(row.en.replace(/\\[scan obscured\\]/g,''))) {\n      assert(/[\\u0600-\\u06ff]/.test(row.ur),row.id+' Urdu script');\n      assert(/[\\u0600-\\u06ff]/.test(row.ps),row.id+' Pashto script');\n    }",
                      "if (/[\\u0600-\\u06ff]{4}/.test(row.ur.replace(/\\[scan obscured\\]/g,''))) {\n      assert(/[A-Za-z]{3}/.test(row.en),row.id+' English text');\n      assert(/[\\u0600-\\u06ff]/.test(row.ps),row.id+' Pashto script');\n    }")
(HERE / f'verify_{k}_pages.cjs').write_text(ver, encoding='utf-8')
(HERE / f'{k}-progress.json').write_text(json.dumps({'book': f'{name} 11 ({N} scans)', 'nextScan': 1, 'pages': {}}, ensure_ascii=False, indent=1), encoding='utf-8')
# wire script from template
w = (HERE / 'wire_book_template.py').read_text(encoding='utf-8')
for a_, b_ in {'__K__': k, '__NAME__': json.dumps(name, ensure_ascii=False), '__EMOJI__': json.dumps(cfg['emoji'], ensure_ascii=False), '__NCH__': str(len(cfg['chapters'])), '__BOOKTITLE__': json.dumps(cfg['bookTitle'], ensure_ascii=False)}.items():
    w = w.replace(a_, b_)
(HERE / f'wire_book_{k}.py').write_text(w, encoding='utf-8')
print('generated toolchain for', k)
