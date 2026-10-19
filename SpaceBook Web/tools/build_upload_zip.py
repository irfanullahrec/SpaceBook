# Builds D:\SpaceBook\deploy\spacebook_upload.zip: exactly the files the live site needs, ready to upload to
# public_html/spacebook and extract (cPanel File Manager > Upload, then Extract). Delete the zip from the server
# right after extracting it.
#   python tools/build_upload_zip.py [output.zip]
#
# The zip never contains api/config.php or any other secret. Create api/config.php on the server once, by hand
# (cPanel File Manager > public_html/spacebook/api > New File), from api/config.sample.php with the live values.
# Extracting a new zip leaves that file in place because the zip has no file of that name.
import os, sys, zipfile

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(WEB), "deploy", "spacebook_upload.zip")
SITE = ['index.html', 'logo_tuitionhub_trans.png', 'css', 'js', 'assets', 'api', 'covers']
# never packaged: real credentials, local schema markers, PHP/editor leftovers
SECRET = {'api/config.php', 'api/config.local.php', 'api/.env', '.env'}

def skip(rel):
    name = rel.rsplit('/', 1)[-1]
    return (rel in SECRET or rel.startswith('api/.schema-') or name.startswith('.env')
            or name.endswith(('.bak', '.orig', '.swp', '~')) or '/__pycache__/' in rel)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
n = 0
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for item in SITE:
        src = os.path.join(WEB, item)
        files = [src] if os.path.isfile(src) else [os.path.join(dp, f) for dp, _, fs in os.walk(src) for f in fs]
        for f in files:
            rel = os.path.relpath(f, WEB).replace(os.sep, '/')
            if skip(rel):
                continue
            z.write(f, rel); n += 1
    bad = [i for i in z.namelist() if skip(i)]
assert not bad, f'secret files in package: {bad}'
print(f'{n} files -> {OUT} ({os.path.getsize(OUT)/1e6:.0f} MB); no api/config.php inside')
