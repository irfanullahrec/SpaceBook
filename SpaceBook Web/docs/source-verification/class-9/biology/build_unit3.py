# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 3 from source PDF 42-65 (printed 37-41, 44-62; printed 42-43 missing)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit3_a, unit3_b
secs = unit3_a.sections() + unit3_b.sections() + [unit3_b.keypoints_section()]
fields = dict(title='Biodiversity', titleUrdu='حیاتیاتی تنوع', titlePashto='د ژوندیو تنوع', pageRange='Pages 37–62',
              badge='Source-verified (PDF 42–65; printed pp.42–43 missing in source)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(42, 66)), sourcePrintedPages=list(range(37, 42)) + list(range(44, 63)),
              keyPoints=[k[0] for k in unit3_b.KEY_POINTS], exercise=unit3_b.exercise(), practicals=[],
              sourceReview=dict(complete=False, lastPdfPage=65, unresolved=['Printed pages 42-43 missing from all local PDF copies (between PDF 46 and 47); includes figures numbered 3.2-3.5.'],
                                note='Unit 3 rebuilt verbatim from source.'))
T.upsert_unit(3, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
