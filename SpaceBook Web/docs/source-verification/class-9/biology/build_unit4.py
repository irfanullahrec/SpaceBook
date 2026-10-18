# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 4 from source PDF 66-101 (printed 63-98)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit4_a, unit4_b, unit4_c, unit4_d, unit4_e, unit4_ex
a = unit4_a.sections()                 # slo, 4.1
b = unit4_b.sections(a[1])             # adds Fig 4.4 to 4.1; returns 4.2, 4.3
unit4_c.extend_4_3(b[1])
d = unit4_d.sections()                 # 4.4, 4.5, 4.6
unit4_e.extend_4_6(d[2])
e = unit4_e.sections()                 # 4.7, 4.8
secs = a + b + d + e + [unit4_ex.activity_section(), unit4_ex.keypoints_section()]
fields = dict(title='Cells and Tissues', titleUrdu='خلیات اور بافتیں', titlePashto='حجرې او نسجونه', pageRange='Pages 63–98', badge='Source-verified (PDF 66–101)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(66, 102)), sourcePrintedPages=list(range(63, 99)),
              keyPoints=[k[0] for k in unit4_ex.KEY_POINTS], exercise=unit4_ex.exercise(), practicals=[],
              sourceReview=dict(complete=True, lastPdfPage=101, note='Unit 4 rebuilt verbatim from source with coded figures 4.1-4.28.'))
T.upsert_unit(4, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
