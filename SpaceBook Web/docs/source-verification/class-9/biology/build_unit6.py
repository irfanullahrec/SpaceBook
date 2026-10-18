# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 6 from source PDF 119-131 (printed 116-128)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit6
secs = unit6.sections() + [unit6.keypoints_section()]
fields = dict(title='Enzymes', titleUrdu='انزائمز (خامرے)', titlePashto='انزایمونه', pageRange='Pages 116–128', badge='Source-verified (PDF 119–131)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(119, 132)), sourcePrintedPages=list(range(116, 129)),
              keyPoints=[k[0] for k in unit6.KEY_POINTS], exercise=unit6.exercise(), practicals=[],
              sourceReview=dict(complete=True, lastPdfPage=131, note='Unit 6 rebuilt verbatim from source with coded figures and graphs.'))
T.upsert_unit(6, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
