# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 9 from source PDF 181-209 (printed 178-206)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit9_a, unit9_b, unit9_c
a = unit9_a.sections()          # slo, 9.1, 9.2, 9.3
b = unit9_b.sections(a[3])      # extends 9.3; returns 9.4, 9.5
secs = a + b + unit9_c.sections() + [unit9_c.keypoints_section()]
fields = dict(title='Transport', titleUrdu='نقل و حمل', titlePashto='لېږد', pageRange='Pages 178–206', badge='Source-verified (PDF 181–209)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(181, 210)), sourcePrintedPages=list(range(178, 207)),
              keyPoints=[k[0] for k in unit9_c.KEY_POINTS], exercise=unit9_c.exercise(), practicals=[],
              sourceReview=dict(complete=True, lastPdfPage=209, note='Unit 9 rebuilt verbatim from source with coded figures and tables.'))
T.upsert_unit(9, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
