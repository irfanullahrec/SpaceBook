# -*- coding: utf-8 -*-
"""Read the printed page numbers of the scans of several books, one after the other (slow: about 2 s per scan).
python -X utf8 run_footers.py islhist islopt ..."""
import sys, traceback
sys.path.insert(0, '.')
import engine
for k in sys.argv[1:]:
    try:
        engine.Book(k).footers()
    except Exception:
        traceback.print_exc()
