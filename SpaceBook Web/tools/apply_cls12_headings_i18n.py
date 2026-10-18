"""Apply cls12_headings_*.json translations to class-12 data files.

Science (chem/phys/stat): section title -> headingUrdu + headingPashto + urduTitle.
  Titles are matched after stripping 'NN(.MM)*' prefixes; 'Textbook lesson
  extract N' placeholders get pattern-based labels; headingUrdu comes from the
  JSON 'urdu' field (Biology-style).
Humanities (9): section heading -> headingPashto (with Pashto 'hapsato N:'
  prefix derived from the original 'حصہ/Section N:' prefix) + urduTitle copy of
  the existing headingUrdu.
English: urduTitle copy of headingUrdu (headingUrdu/headingPashto already full).
"""
import sys, os, io, json, re, shutil, datetime, glob

sys.stdout.reconfigure(encoding='utf-8')
JS = r'D:\SpaceBook\SpaceBook Web\js'
I18N = r'D:\SpaceBook\SpaceBook Web\tools\i18n'
TMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'opencode', 'cls12_apply_backup')

SCIENCE = {'chemistry': 'chem_12_data.js', 'physics': 'phys_12_data.js',
           'statistics': 'stat_12_data.js'}
HUM = {'urdu': 'urdu_12_data.js', 'civics': 'civics_12_data.js',
       'computer': 'computer_12_data.js', 'economics': 'economics_12_data.js',
       'hpe': 'hpe_12_data.js', 'islamiat': 'islamiat_ikhtiari_12_data.js',
       'islhist': 'islamic_history_12_data.js', 'pakstudy': 'pakstudy_12_data.js',
       'quran': 'quran_12_data.js'}
PREFIX = re.compile(r'^(حصہ\s*\d+\s*:|Section\s*\d+\s*:)\s*')
NUMPRE = re.compile(r'^\d{1,2}(?:\.\d{1,2}){0,3}\s+')
EXTRACT = re.compile(r'^Textbook lesson extract (\d+)$')

os.makedirs(TMP, exist_ok=True)
stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
problems = []


def load_map(subj):
    p = os.path.join(I18N, f'cls12_headings_{subj}.json')
    return {e['title']: e for e in json.load(io.open(p, encoding='utf-8'))}


def norm_science(t):
    t = NUMPRE.sub('', (t or '')).strip()
    return t[:-1].strip() if t.endswith(':') else t


def apply_file(fname, subj, kind):
    path = os.path.join(JS, fname)
    raw = io.open(path, encoding='utf-8').read()
    i, j = raw.find('['), raw.rfind(']')
    arr = json.loads(raw[i:j + 1])
    mp = load_map(subj)
    hit = miss = 0

    for c in arr:
        for s in (c.get('sections') or []):
            title = s.get('heading') or s.get('title') or ''
            if kind == 'science':
                m = EXTRACT.match(title)
                if m:
                    n = m.group(1)
                    u = f'درس کا متن {n}'
                    p = f'د سبق متن {n}'
                    s['headingUrdu'] = u
                    s['headingPashto'] = p
                    s['urduTitle'] = u
                    hit += 1
                    continue
                e = mp.get(norm_science(title))
                if not e:
                    miss += 1
                    problems.append(f'{fname}: no translation for {title!r}')
                    continue
                s['headingUrdu'] = e['urdu']
                s['headingPashto'] = e['pashto']
                s['urduTitle'] = e['urdu']
                hit += 1
            else:
                pm = PREFIX.match(title)
                body = title[pm.end():] if pm else title
                e = mp.get(body)
                if not e:
                    miss += 1
                    problems.append(f'{fname}: no translation for {title!r}')
                    continue
                if pm:
                    g = pm.group(1)
                    num = re.search(r'\d+', g).group(0)
                    s['headingPashto'] = f'څاتو {num}: {e["pashto"]}'
                else:
                    s['headingPashto'] = e['pashto']
                if s.get('headingUrdu'):
                    s['urduTitle'] = s['headingUrdu']
                hit += 1

    out = raw[:i] + json.dumps(arr, ensure_ascii=False, indent=2) + raw[j + 1:]
    chk = os.path.join(TMP, '_check.js')
    with io.open(chk, 'w', encoding='utf-8') as fh:
        fh.write(out)
    if os.system('node --check "%s"' % chk) != 0:
        print(f'{fname}: NODE CHECK FAILED - SKIPPED')
        return
    shutil.copy2(path, os.path.join(TMP, f'{stamp}_{fname}'))
    tmp = path + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(out)
    os.replace(tmp, path)
    print(f'{fname}: applied {hit}, missed {miss}')


for subj, f in SCIENCE.items():
    apply_file(f, subj, 'science')
for subj, f in HUM.items():
    apply_file(f, subj, 'hum')
# english: urduTitle parity only (heading fields already complete)
fname = 'english_12_data.js'
path = os.path.join(JS, fname)
raw = io.open(path, encoding='utf-8').read()
i, j = raw.find('['), raw.rfind(']')
arr = json.loads(raw[i:j + 1])
n = 0
for c in arr:
    for s in (c.get('sections') or []):
        if s.get('headingUrdu') and not s.get('urduTitle'):
            s['urduTitle'] = s['headingUrdu']
            n += 1
out = raw[:i] + json.dumps(arr, ensure_ascii=False, indent=2) + raw[j + 1:]
chk = os.path.join(TMP, '_check.js')
with io.open(chk, 'w', encoding='utf-8') as fh:
    fh.write(out)
if os.system('node --check "%s"' % chk) == 0:
    shutil.copy2(path, os.path.join(TMP, f'{stamp}_{fname}'))
    tmp = path + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(out)
    os.replace(tmp, path)
    print(f'{fname}: urduTitle set on {n}')
else:
    print(f'{fname}: NODE CHECK FAILED - SKIPPED')

print('\nproblems:', len(problems))
for p in problems:
    print('  ', p)
