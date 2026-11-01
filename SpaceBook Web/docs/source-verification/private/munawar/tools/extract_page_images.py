"""Copies the page pictures of the Munawar PDFs into content/munawar_pages/ for the reader's "Original page" view.

    python -P docs/source-verification/private/munawar/tools/extract_page_images.py            every book
    python -P docs/source-verification/private/munawar/tools/extract_page_images.py c4-eng     one book

The pictures are the ones inside the PDF, byte for byte (no re-encoding, no recolouring, no cropping): the licence of 15 October 2026
(docs/launch/CONTENT_RIGHTS.md) allows showing the pages as published, with the publisher credited. The sample PDFs hold one 437 x 547 (or
462 x 588) picture per page with the SAMPLE watermark; clean print-ready PDFs from the publisher give sharper pages (see pdf_to_pages.py).

Output: content/munawar_pages/<subject id>/pNNN.<ext>   (NNN = 0-based PDF page index; printed number = index + 1 unless the book data says otherwise)
        content/munawar_pages/index.json               {"<subject id>": {"count": N, "w": W, "h": H, "ext": "jpg", "units": [first printed page of each unit]}, ...}
"""
import json
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import registry  # noqa: E402

WEB = HERE.parents[4]            # SpaceBook Web
OUT = WEB / 'content' / 'munawar_pages'


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    OUT.mkdir(parents=True, exist_ok=True)
    index_path = OUT / 'index.json'
    index = json.loads(index_path.read_text(encoding='utf-8')) if index_path.exists() else {}
    for cls, code, pdf, pages in registry.BOOKS:
        bid = registry.book_id(cls, code)
        if only and only != bid:
            continue
        subject = 'cls%d-mun-%s' % (cls, code)
        doc = pymupdf.open(str(Path(registry.PDF_DIR) / pdf))
        folder = OUT / subject
        folder.mkdir(parents=True, exist_ok=True)
        ext, w, h, n = 'jpg', 0, 0, 0
        for i, page in enumerate(doc):
            # get_images() lists every picture in the page's resources, and some of these PDFs share one resource list between all pages
            # (the cover would be saved as every page): get_image_info() lists only the pictures the page really draws
            drawn = [im for im in page.get_image_info(xrefs=True) if im.get('xref')]
            if not drawn:
                print('no picture on page', i, 'of', subject)
                continue
            big = max(drawn, key=lambda im: (im['bbox'][2] - im['bbox'][0]) * (im['bbox'][3] - im['bbox'][1]))     # the page picture
            info = doc.extract_image(big['xref'])
            ext = info['ext'] if info['ext'] != 'jpeg' else 'jpg'
            w, h = info['width'], info['height']
            (folder / ('p%03d.%s' % (i, ext))).write_bytes(info['image'])
            n += 1
        starts = []                       # the first printed page of every unit (units.tsv): the reader locks pages by unit like the lessons
        tsv = HERE.parent / bid / 'units.tsv'
        if tsv.exists():
            for line in tsv.read_text(encoding='utf-8').splitlines():
                c = line.split('	')
                if line.startswith('#') or len(c) < 5 or not c[4].strip().isdigit():
                    continue
                starts.append(int(c[4]))
        index[subject] = {'count': n, 'w': w, 'h': h, 'ext': ext, 'units': starts}
        print('%-14s %3d pages  %dx%d  %s' % (subject, n, w, h, ext))
    index_path.write_text(json.dumps(index, indent=1, sort_keys=True) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
