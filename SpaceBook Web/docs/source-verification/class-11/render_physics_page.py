"""Render one requested Physics source page for local inspection only."""
import pathlib
import sys
import pymupdf

page = int(sys.argv[1])
output = pathlib.Path(r"D:\SpaceBook\SpaceBook Web\tmp\class-11")
output.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(r"D:\SpaceBook\Books\11th\11th physics\pdf\physicsfull.pdf")
doc[page - 1].get_pixmap(matrix=pymupdf.Matrix(1.8, 1.8)).save(output / f"physics-p{page:03}.png")
