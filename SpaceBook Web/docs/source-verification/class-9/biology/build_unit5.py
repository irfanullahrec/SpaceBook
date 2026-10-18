# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 5 from source PDF 102-118 (printed 99-115)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit5
secs = unit5.sections() + [unit5.keypoints_section()]
fields = dict(title='Cell Cycle', titleUrdu='خلوی چکر', titlePashto='حجروي دوره', pageRange='Pages 99–115', badge='Source-verified (PDF 102–118)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(102, 119)), sourcePrintedPages=list(range(99, 116)),
              keyPoints=[k[0] for k in unit5.KEY_POINTS], exercise=unit5.exercise(), practicals=[],
              sourceReview=dict(complete=True, lastPdfPage=118, note='Unit 5 rebuilt verbatim from source with coded figures.'))
T.upsert_unit(5, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
