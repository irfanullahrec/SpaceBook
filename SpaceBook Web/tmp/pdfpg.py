import sys, pymupdf
S=r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\15b92a1e-eca9-4e38-83dd-7da937d60a98\scratchpad'
d=pymupdf.open(r'D:\SpaceBook\Books\8th\8th MAths\PDF\Math Book for 8 class KPTBB.pdf')
q=sys.argv[1]
hits=[i for i,p in enumerate(d) if q.lower() in p.get_text().lower()]
print(hits)
if len(sys.argv)>2:
    i=int(sys.argv[2]); dpi=int(sys.argv[3]) if len(sys.argv)>3 else 200
    pix=d[i].get_pixmap(dpi=dpi); pix.save(S+rf'\pg{i}.png'); print(S+rf'\pg{i}.png', pix.width, pix.height)
