"""Render one requested Class 11 Chemistry source page for local inspection."""
import pathlib,sys,pymupdf
page=int(sys.argv[1]);out=pathlib.Path(r"D:\SpaceBook\SpaceBook Web\tmp\class-11");out.mkdir(parents=True,exist_ok=True)
doc=pymupdf.open(r"D:\SpaceBook\Books\11th\11th chemisty\pdf\chemistryfull.pdf")
doc[page-1].get_pixmap(matrix=pymupdf.Matrix(1.8,1.8)).save(out/f"chemistry-p{page:03}.png")
