# -*- coding: utf-8 -*-
"""Review sheets for the scans whose reviewed record runs on into the first page of the next scan:
    python -X utf8 spill.py KEY OUTDIR            (lists the scans, writes OUTDIR/sp_NNN.png with the TOP of the next scan's first page, three per sheet)
and prints the last units of that record so the words the next page starts with can be found:  'K N words' in splits_*.txt."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine


def spill_scans(b):
    out = []
    for k in sorted(b.by_pdf()):
        jp = b.pdf_jpgs(k)
        if not jp or len(jp) < 2:
            continue
        pp = [x for x in b.scan_pages(k)[1] if x]
        if not pp:
            continue
        top = max(pp)
        for s in b.by_pdf()[k]:
            if s['printed'] and max(s['printed']) > top:
                out.append(k)
                break
    return out


def main():
    b = engine.Book(sys.argv[1])
    outdir = Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)
    ks = spill_scans(b)
    by_pdf = b.by_pdf()
    sections = {s['id']: s for s in b.sections()}
    W = 620
    for n in range(0, len(ks), 3):
        grp = ks[n:n + 3]
        sheet = Image.new('RGB', (W * len(grp), 330), 'white')
        d = ImageDraw.Draw(sheet)
        for i, k in enumerate(grp):
            nj = b.pdf_jpgs(k)[-1] + 1
            im = Image.open(b.jpg_path(nj)).convert('RGB')
            w, h = im.size
            im = im.crop((0, 0, w, int(h * 0.40)))
            im.thumbnail((W, 310))
            sheet.paste(im, (i * W, 20))
            d.text((i * W + 4, 4), f'scan {k} runs on into JPG {nj} (p.{b.printed_of(nj)}) top', fill='red')
        sheet.save(outdir / f'sp_{grp[0]:03}.png')
    for k in ks:
        group = by_pdf[k]
        jp, pp = b.scan_pages(k)
        d_, stream = b.scan_streams(group, pp)
        units = [u for s in stream for u in b.units_of(s)]
        print(f'=== SCAN {k}  next page = JPG {jp[-1] + 1} (p.{b.printed_of(jp[-1] + 1)})  stream units {len(units)}')
        for ui in range(max(0, len(units) - 12), len(units)):
            u = units[ui]
            t = b.text_of(sections, u) if 'pi' in u else f'<{u["k"]} {u.get("id", "")}>'
            print(f'  [{ui}] {t[:150]}')
        nxt = by_pdf.get(k + 1, [])
        jp2, pp2 = b.scan_pages(k + 1) if nxt else (None, None)
        if nxt:
            d2, st2 = b.scan_streams(nxt, pp2)
            u2 = [u for s in (d2 and [x for _, x in d2] or []) + st2 for u in b.units_of(s)]
            print('  -- next record starts:')
            for u in u2[:3]:
                t = b.text_of(sections, u) if 'pi' in u else f'<{u["k"]} {u.get("id", "")}>'
                print(f'     {t[:110]}')


if __name__ == '__main__':
    main()
