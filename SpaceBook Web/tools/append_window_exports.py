import os

files = [
    ('english_12_data.js', 'ENGLISH_12_DATA'),
    ('pakstudy_12_data.js', 'PAKSTUDY_12_DATA'),
    ('urdu_12_data.js', 'URDU_12_DATA'),
    ('biology_12_data.js', 'BIOLOGY_12_DATA'),
    ('computer_12_data.js', 'COMP_12_DATA'),
    ('civics_12_data.js', 'CIVICS_12_DATA'),
    ('economics_12_data.js', 'ECON_12_DATA'),
    ('hpe_12_data.js', 'HPE_12_DATA'),
    ('islamiat_ikhtiari_12_data.js', 'ISLAMIAT_OPT_12_DATA'),
    ('islamic_history_12_data.js', 'ISLAMIC_HISTORY_12_DATA'),
    ('quran_12_data.js', 'QURAN_12_DATA')
]

for fn, vn in files:
    p = os.path.join('js', fn)
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if f'window.{vn}' not in c:
        c += f"\nif (typeof window !== 'undefined') {{\n  window.{vn} = {vn};\n}}\n"
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {fn}")
    else:
        print(f"Already updated {fn}")
