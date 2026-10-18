# -*- coding: utf-8 -*-
"""Add Class 9 Biology back matter (glossary, index, references, authors) as a final chapter."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, backmatter
data = T.load_bio()
recs = [s.record() for s in backmatter.sections()]
unit = dict(id='bio_backmatter', number='G', title='Glossary, Index & References', titleUrdu='فرہنگ، اشاریہ اور حوالہ جات', titlePashto='لغتنامه، لړلیک او سرچینې',
            pageRange='Pages 207–220', badge='Source-verified (PDF 210–223)', status='completed', description='Back matter of the Class 9 Biology textbook.',
            sections=recs, keyPoints=[], exercise={}, sloBank=[], practicals=[], sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(210, 224)), sourcePrintedPages=list(range(207, 221)),
            sourceReview=dict(complete=True, lastPdfPage=223, note='Back matter transcribed from source; PDF 224 (blank feedback form) and 225 (back cover) recorded as excluded.'))
data = [u for u in data if u.get('id') != 'bio_backmatter'] + [unit]
T.save_bio(data)
print([s['id'] for s in recs]); print('ok' if T.check_js() else 'CHECK FAILED')
