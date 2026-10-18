# Copies only the files the live site needs into C:\xampp\htdocs\spacebook (the online site is deployed by
# .github/workflows/deploy.yml instead). Re-run after changes:   python "tools/deploy_htdocs.py"
import os, shutil

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = r"C:\xampp\htdocs\spacebook"
SITE = ['index.html', 'logo_tuitionhub_trans.png', 'css', 'js', 'assets', 'api', 'covers']

copied = size = 0
for item in SITE:
    src = os.path.join(SRC, item)
    files = [src] if os.path.isfile(src) else [os.path.join(dp, f) for dp, _, fs in os.walk(src) for f in fs]
    for f in files:
        rel = os.path.relpath(f, SRC)
        if rel.startswith(os.path.join('api', '.schema-')):
            continue
        dst = os.path.join(DST, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(f, dst)
        copied += 1
        size += os.path.getsize(f)
print(f'copied {copied} files, {size/1e6:.0f} MB to {DST}')
