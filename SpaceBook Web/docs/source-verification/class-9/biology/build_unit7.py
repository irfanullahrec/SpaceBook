# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 7 from source PDF 132-149 (printed 129-146)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit7_a, unit7_b
a = unit7_a.sections()          # slo, 7.1, 7.2
b = unit7_b.sections(a[2])      # extends 7.2; returns 7.3, 7.4, 7.5
secs = a + b + [unit7_b.keypoints_section()]
fields = dict(title='Bio-energetics', titleUrdu='بائیو انرجیٹکس (حیاتیاتی توانائی)', titlePashto='بایوانرژیټیک', pageRange='Pages 129–146', badge='Source-verified (PDF 132–149)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(132, 150)), sourcePrintedPages=list(range(129, 147)),
              keyPoints=[k[0] for k in unit7_b.KEY_POINTS], exercise=unit7_b.exercise(), practicals=[],
              sourceReview=dict(complete=True, lastPdfPage=149, note='Unit 7 rebuilt verbatim from source with coded figures and tables.'))
T.upsert_unit(7, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
