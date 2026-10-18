# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 8 from source PDF 150-180 (printed 147-177)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit8_a, unit8_b, unit8_c, unit8_d
a = unit8_a.sections()          # slo, 8.1, 8.2, 8.3
b = unit8_b.sections(a[3])      # extends 8.3 (water b-g); returns 8.4, 8.5
secs = a + b + unit8_c.sections() + unit8_d.sections() + [unit8_d.keypoints_section()]
fields = dict(title='Nutrition', titleUrdu='غذائیت', titlePashto='تغذیه', pageRange='Pages 147–177', badge='Source-verified (PDF 150–180)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(150, 181)), sourcePrintedPages=list(range(147, 178)),
              keyPoints=[k[0] for k in unit8_d.KEY_POINTS], exercise=unit8_d.exercise(), practicals=[],
              sourceReview=dict(complete=True, lastPdfPage=180, note='Unit 8 rebuilt verbatim from source with coded figures and tables.'))
T.upsert_unit(8, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
