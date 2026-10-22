"""gen_geom7.py - Class 7 Unit 9 circle / cylinder items (R9 Q2-7, 9.5 Q15) computed with the textbook's pi and written as key-checked DSL
lines (class-7/math/dsl/geom.txt)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
B = chr(92)
PI = 3.14


def r2(v):
    return f'{v:.4f}'.rstrip('0').rstrip('.')


def main():
    out = []
    T = B + 'times'
    # R9 Q2: area and circumference, pi = 3.14
    for no, r in zip('abcdef', (3.3, 4.3, 9.3, 5.8, 11.9, 23.3)):
        a = PI * r * r
        c = 2 * PI * r
        out.append(f"R9|2|{no} ~ A = {B}pi r^2 = 3.14 {T} {r}^2 = {r2(a)} ;; C = 2{B}pi r = 2 {T} 3.14 {T} {r} = {r2(c)} => A = {r2(a)} cm^2, C = {r2(c)} cm")
    # R9 Q3: cylinder surface area and volume
    for no, (r, h) in zip('abcd', ((3.3, 13), (9.3, 20), (4.2, 12), (5.3, 9))):
        sa = 2 * PI * r * (h + r)
        v = PI * r * r * h
        out.append(f"R9|3|{no} ~ {B}text{{Surface area}} = 2{B}pi r(h + r) = 2 {T} 3.14 {T} {r} {T} ({h} + {r}) = {r2(sa)} ;; V = {B}pi r^2 h = 3.14 {T} {r}^2 {T} {h} = {r2(v)} => Surface area {r2(sa)} cm^2, volume {r2(v)} cm^3")
    r, h = 5, 34
    out.append(f"R9|5| ~ {B}text{{Surface area}} = 2{B}pi r(h + r) = 2 {T} 3.14 {T} 5 {T} (34 + 5) = {r2(2 * PI * r * (h + r))} => {r2(2 * PI * r * (h + r))} cm^2")
    r, h = 9.5, 34
    out.append(f"R9|6| ~ r = {B}frac{{19}}{{2}} = 9.5 ;; {B}text{{Area}} = 2{B}pi r(h + r) = 2 {T} 3.14 {T} 9.5 {T} (34 + 9.5) = {r2(2 * PI * r * (h + r))} => {r2(2 * PI * r * (h + r))} cm^2")
    out.append(f"R9|7| ~ {B}text{{Walls}} = 2(4.5 + 3.5) {T} 3 = 48 ;; {B}text{{Floor}} = 4.5 {T} 3.5 = 15.75 ;; {B}text{{Area}} = 48 + 15.75 = 63.75 ;; {B}text{{Cost}} = 63.75 {T} 28 = 1785 => Rs 1785")
    # 9.5 Q15: 8 pillars, circumference 15 m, height 18 m
    r = round(15 / (2 * PI), 4)
    area = round(PI * r * r, 4)
    v8 = round(8 * area * 18, 4)
    cost = round(v8 * 745, 2)
    out.append(f"9.5|15| ~ r = {B}frac{{C}}{{2{B}pi}} = {B}frac{{15}}{{2 {T} 3.14}} = {r2(r)} ;; {B}text{{Area}} = {B}pi r^2 = 3.14 {T} {r2(r)}^2 = {r2(area)} ;; {B}text{{Volume of 8 pillars}} = 8 {T} {r2(area)} {T} 18 = {r2(v8)} ;; {B}text{{Cost}} = {r2(v8)} {T} 745 = {r2(cost)} => Rs {r2(cost)} (about Rs 1,921,800; the printed key keeps more decimals and gives Rs 1,921,815.29) %%")
    r = 78.3
    c = round(2 * 3.1416 * r, 2)
    out.append(f"R9|4| ~ {B}text{{Circumference}} = 2{B}pi r = 2 {T} 3.1416 {T} 78.3 = {c:.2f} ;; {B}text{{Cost}} = {c:.2f} {T} 112 = {c * 112:.2f} => Rs {c * 112:.2f} %%")
    (HERE / 'class-7' / 'math' / 'dsl' / 'geom.txt').write_text(chr(10).join(out) + chr(10), encoding='utf-8')
    print(len(out))


if __name__ == '__main__':
    main()
