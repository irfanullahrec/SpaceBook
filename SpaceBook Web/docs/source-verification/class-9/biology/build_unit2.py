# -*- coding: utf-8 -*-
"""Rebuild Class 9 Biology Unit 2 from source PDF 29-41 (printed 23-25, 27-36; printed 26 missing)."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import bio9_tools as T, unit2_a, unit2_b
secs = unit2_a.sections() + unit2_b.sections() + [unit2_b.keypoints_section()]
fields = dict(title='Solving a Biological Problem', titleUrdu='حیاتیاتی مسئلے کا حل', titlePashto='د بیولوژیکي ستونزې حل',
              pageRange='Pages 23–36', badge='Source-verified (PDF 29–41; printed p.26 missing in source)', status='completed',
              sourcePdf=T.SOURCE_PDF, sourcePdfPages=list(range(29, 42)), sourcePrintedPages=[23, 24, 25] + list(range(27, 37)),
              keyPoints=[k[0] for k in unit2_b.KEY_POINTS], exercise=unit2_b.exercise(), practicals=[],
              sourceReview=dict(complete=False, lastPdfPage=41, unresolved=['Printed page 26 missing from all local PDF copies (between PDF 31 and 32).'],
                                note='Unit 2 rebuilt verbatim; earlier paraphrase, invented ratio example and invented MCQs replaced.'))
T.upsert_unit(2, secs, fields)
print([s.id for s in secs]); print('ok' if T.check_js() else 'CHECK FAILED')
