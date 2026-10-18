import sys, os, pymupdf
d = pymupdf.open(sys.argv[1]); a, b, dpi = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_render'); os.makedirs(out, exist_ok=True)
for i in range(a, b + 1):
    d[i].get_pixmap(dpi=dpi).save(f"{out}/f{i:03d}.png")
print("ok", a, b)
