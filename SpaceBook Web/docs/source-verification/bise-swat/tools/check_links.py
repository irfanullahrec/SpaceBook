#!/usr/bin/env python
"""Ask the Board's server whether each linked file can be fetched. Writes data/link_status.json ({url: http status}).

    python -X utf8 check_links.py [bise-page.html]      (default: data/page_syllabus_2026-10-20.html)

build_bise.py marks a file whose status is not 200 so that the app does not offer a dead link as if it worked.
The Board's server answered 403 for the three Class 11 Islamiat files on 2026-10-20.
"""
import json, os, re, ssl, sys, urllib.parse, urllib.request, concurrent.futures

HERE = os.path.dirname(os.path.abspath(__file__))
page = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'data', 'page_syllabus_2026-10-20.html')
html = open(page, encoding='utf8').read()
urls = sorted(set(u.replace(' ', '%20') for u in re.findall(r'href="([^"]+\.(?:pdf|jpe?g))"', html)))
urls.append('https://www.bisess.edu.pk/site/assets/attachments/6dee164ef85c0f9b5098b845825b9eec.pdf')
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE


def status(u):
    try:
        req = urllib.request.Request(urllib.parse.quote(u, safe=':/%?=&'), headers={'User-Agent': 'curl/8.4.0'})   # the Board's server answers 403 to a browser-like User-Agent and to Range requests
        with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
            r.read(1)
            return u, r.status
    except urllib.error.HTTPError as e:
        return u, e.code
    except Exception:
        return u, 0


with concurrent.futures.ThreadPoolExecutor(8) as ex:
    res = dict(ex.map(status, urls))
json.dump(res, open(os.path.join(HERE, '..', 'data', 'link_status.json'), 'w'), indent=0)
bad = {u: c for u, c in res.items() if c not in (200, 206)}
print(len(res), 'links;', len(bad), 'not available'); [print(' ', c, u[-90:]) for u, c in bad.items()]
