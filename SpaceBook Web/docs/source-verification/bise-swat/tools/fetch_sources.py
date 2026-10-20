#!/usr/bin/env python
"""Download the BISE Swat "Syllabus & Model Papers" files and extract their text.

    python -X utf8 fetch_sources.py [dest]          (default dest = ../sources, which is git-ignored: ~110 MB)

Reads https://www.bisess.edu.pk/site/home/syllabus-model-papers, downloads every PDF/JPEG it links (spaces in the
Board's file names are percent-encoded) plus the E-Answer Sheet, and runs `pdftotext -layout -enc UTF-8` into <dest>/txt8.
The scanned and Urdu files give no text; read those from page images (PyMuPDF: page.get_pixmap(dpi=70)).
"""
import os, re, subprocess, sys, urllib.parse, urllib.request

PAGE = 'https://www.bisess.edu.pk/site/home/syllabus-model-papers'
EXTRA = ['https://www.bisess.edu.pk/site/assets/attachments/6dee164ef85c0f9b5098b845825b9eec.pdf', 'https://www.bisess.edu.pk/site/assets/images/emarking-urdu.jpg']


def fetch(url, out):
    req = urllib.request.Request(urllib.parse.quote(url, safe=':/%?=&'), headers={'User-Agent': 'Mozilla/5.0'})
    import ssl
    ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE   # the Board's certificate chain is incomplete
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r, open(out, 'wb') as f:
        f.write(r.read())


def main():
    dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sources')
    os.makedirs(os.path.join(dest, 'txt8'), exist_ok=True)
    page = os.path.join(dest, 'page.html')
    fetch(PAGE, page)
    html = open(page, encoding='utf8').read()
    urls = sorted(set(re.findall(r'href="([^"]+\.(?:pdf|jpe?g))"', html))) + EXTRA
    for u in urls:
        rel = urllib.parse.unquote(re.sub(r'^.*/assets/', '', u)).replace('/', '__')
        rel = re.sub(r'[^\w.\-]', '_', rel)
        out = os.path.join(dest, rel)
        if not (os.path.exists(out) and os.path.getsize(out) > 500):
            try:
                fetch(u, out)
            except Exception as e:     # a file may be removed from the Board's site
                print('  !', u, e); continue
        if out.lower().endswith('.pdf'):
            subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', out, os.path.join(dest, 'txt8', os.path.splitext(rel)[0] + '.txt')], check=False)
    print(len(urls), 'files in', dest)


if __name__ == '__main__':
    main()
