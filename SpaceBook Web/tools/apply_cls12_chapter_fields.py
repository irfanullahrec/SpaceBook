"""Chapter-level fields for class-12: Biology-style titleUrdu/urduSummary/englishSummary.

chem units 13-24, phys units 11-20, stat chapters 1-9 get all three fields.
english gets urduSummary only (titleUrdu/titlePashto/englishSummary already full).
"""
import sys, os, io, json, shutil, datetime

sys.stdout.reconfigure(encoding='utf-8')
JS = r'D:\SpaceBook\SpaceBook Web\js'
TMP = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'opencode', 'cls12_apply_backup')
stamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

CHEM = [
    ('s and p-Block Elements', 's اور p بلاک عناصر'),
    ('d and f-Block Elements: Transition Elements', 'd اور f بلاک عناصر: گزرا ہوئے عناصر'),
    ('Organic Compounds', 'عضویاتی مرکبات'),
    ('Hydrocarbons', 'ہائیڈرو کاربنز'),
    ('Alkyl Halides and Amines', 'آلکل ہیلائیڈز اور ایمینز'),
    ('Alcohols, Phenols and Ethers', 'الکہولز، فینولز اور ایثرز'),
    ('Carbonyl Compounds I: Aldehydes and Ketones', 'کربنیل مرکبات I: الڈیہائیڈز اور کیتونز'),
    ('Carbonyl Compounds II: Carboxylic Acids and Functional Derivatives',
     'کربنیل مرکبات II: کاربوکسیلک تیزاب اور فنکشنل اشتقاقات'),
    ('Biochemistry', 'حیاتیاتی کیمیا'),
    ('Industrial Chemistry', 'صنعتی کیمیا'),
    ('Environmental Chemistry', 'ماحولیاتی کیمیا'),
    ('Analytical Chemistry', 'تجزیاتی کیمیا'),
]
PHYS = [
    ('Electrostatics', 'ایلیکٹروسٹیٹکس (برقی سکون)'),
    ('Current Electricity', 'کرنٹ برقیات'),
    ('Electromagnetism', 'الیکٹرو میگنیٹزم'),
    ('Electromagnetic Induction', 'الیکٹرو میگنیٹک اندکشن'),
    ('Alternating Current', 'متبادل کرنٹ'),
    ('Physics of Solids', 'ٹھوس کے فزکس'),
    ('Electronics', 'الیکٹرانکس'),
    ('Dawn of Modern Physics', 'جدید فزکس کا آغاز'),
    ('Atomic Spectra', 'ایٹمی طیف'),
    ('Nuclear Physics', 'نوکلیائی فزکس'),
]
STAT = [
    ('Probability', 'امکان'),
    ('Random Variables and Probability Distributions', 'بے ترتیب متغیرات اور امکان کی توزیعات'),
    ('Special Discrete Probability Distributions', 'مخصوص مصنوفہ امکان توزیعات'),
    ('Special Continuous Probability Distributions', 'مخصوص مسلسل امکان توزیعات'),
    ('Sampling and Sampling Distributions', 'نمونہ گیری اور نمونہ گیری توزیعات'),
    ('Estimation', 'تخمین'),
    ('Hypothesis Testing', 'فرضیات کی جانچ'),
    ('Association of Attributes', 'خصوصیات کا تعلق'),
    ('Experimental Design', 'تجرباتی ڈیزائن'),
]

SUM = {
    'chem': ("Unit {n}: '{t}' covers core concepts, definitions, laws, and applications of chemistry according to the KPK curriculum.",
             "یونیٹ {n}: '{u}' خیبر پختونخوا ٹیکسٹ بک بورڈ کے نصاب کے مطابق کیمیا کے بنیادی تصورات، تعاریف، قوانین اور طریقۂ کار کا احاطہ کرتا ہے۔"),
    'phys': ("Unit {n}: '{t}' covers fundamental principles, derivations, laws, and applications of physics according to the KPK curriculum.",
             "یونیٹ {n}: '{u}' خیبر پختونخوا ٹیکسٹ بک بورڈ کے نصاب کے مطابق فزکس کے بنیادی اصول، استخراجات، قوانین اور طریقۂ کار کا احاطہ کرتا ہے۔"),
    'stat': ("Chapter {n}: '{t}' covers core concepts, formulas, methods, and applications of statistics according to the KPK curriculum.",
             "باب {n}: '{u}' خیبر پختونخوا ٹیکسٹ بک بورڈ کے نصاب کے مطابق شماریات کے بنیادی تصورات، قواعد، فارمولا اور عملی مثالوں کا احاطہ کرتا ہے۔"),
    'eng': (None,
            "باب {n}: '{u}' خیبر پختونخوا ٹیکسٹ بک بورڈ کے نصاب کے مطابق نثر، شاعری اور ادب کے فن، موضوعات اور ان کے تجزیے کا احاطہ کرتا ہے۔"),
}


def load(fn):
    src = io.open(os.path.join(JS, fn), encoding='utf-8').read()
    return src, json.loads(src[src.find('['):src.rfind(']') + 1])


def save(fn, raw, arr):
    i, j = raw.find('['), raw.rfind(']')
    out = raw[:i] + json.dumps(arr, ensure_ascii=False, indent=2) + raw[j + 1:]
    chk = os.path.join(TMP, '_check.js')
    with io.open(chk, 'w', encoding='utf-8') as fh:
        fh.write(out)
    if os.system('node --check "%s"' % chk) != 0:
        print(fn, 'NODE CHECK FAILED - SKIPPED')
        return False
    shutil.copy2(os.path.join(JS, fn), os.path.join(TMP, f'{stamp}_{fn}'))
    tmp = os.path.join(JS, fn + '.tmp')
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(out)
    os.replace(tmp, os.path.join(JS, fn))
    return True


for key, fn, first_unit, spec in (
        ('chem', 'chem_12_data.js', 13, CHEM),
        ('phys', 'phys_12_data.js', 11, PHYS),
        ('stat', 'stat_12_data.js', 1, STAT)):
    raw, arr = load(fn)
    assert len(arr) == len(spec), (fn, len(arr), len(spec))
    e_t, u_t = SUM[key]
    for i, (c, (title, title_urdu)) in enumerate(zip(arr, spec)):
        n = first_unit + i
        assert c.get('title') == title, (fn, i, c.get('title'), title)
        c['titleUrdu'] = title_urdu
        c['englishSummary'] = e_t.format(n=n, t=title)
        c['urduSummary'] = u_t.format(n=n, u=title_urdu)
    ok = save(fn, raw, arr)
    print(fn, 'chapters filled:', len(arr) if ok else 'FAILED')

raw, arr = load('english_12_data.js')
u_t = SUM['eng'][1]
for i, c in enumerate(arr, 1):
    c['urduSummary'] = u_t.format(n=i, u=c.get('titleUrdu') or c.get('title'))
ok = save('english_12_data.js', raw, arr)
print('english_12_data.js urduSummary filled:', len(arr) if ok else 'FAILED')
