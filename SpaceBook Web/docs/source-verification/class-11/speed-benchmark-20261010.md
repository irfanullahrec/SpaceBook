# Class 11 content speed benchmark

User target: 400 PDF pages/hour (about 9 seconds per page), while preserving sequential page review, exact source matching, coded visuals, aligned English/Urdu/Pashto translations, and verified checkpoints.

Measured batch: PDF pages 154–157 were rendered, visually inspected, implemented with paired translations and coded diagrams/equations, source-compared, syntax-checked, reader-checked, and checkpointed. The review-to-checkpoint interval was approximately 24 minutes for four pages, or about 10 pages/hour. This is end-to-end content throughput, not OCR throughput. The earlier cached full-book OCR benchmark was 896.8 pages/hour extraction-only and cannot be treated as content completion speed.

This sample is short and includes a new chapter/renderer setup. Continue measuring on later batches and reduce avoidable tool and setup overhead without skipping pages, guessing unreadable text, or marking unchecked pages verified. Next sequential page: PDF page 158.


Measured batch: PDF pages 158–161 completed from 2026-10-09 20:30:29 UTC to 21:03:05 UTC (32m36s), including rendering, visual review, translation, SVG/equation coding, source comparison, tests, and checkpoints. End-to-end throughput: 7.4 pages/hour. p159 remains unresolved for scan-edge clipping; it is counted as processed, not verified. Next page: 162.


Measured batch: PDF pages 162–165 completed from 2026-10-09 21:03:05 UTC to 21:12:00 UTC (8m55s), including batch rendering, visual review, translations, SVG/equation coding, source comparison, tests, and checkpoints. End-to-end throughput: 27.0 pages/hour. Page 165 is marked processed but unresolved for scan-edge clipping. Next page: 166.


Measured batch: PDF pages 166–169 completed from 2026-10-09 21:12:00 UTC to 21:16:20 UTC (4m20s), including visual review, translations, SVG/equation coding, source comparison, tests, and checkpoints. End-to-end throughput: 55.4 pages/hour. All four pages passed checks and were verified. Next page: 170.

Measured batch: PDF pages 170–177 completed from 2026-10-09 21:16:20 UTC to 21:22:02 UTC (5m42s), including visual review, translations, SVG/equation coding, OCR comparison, tests, and sequential checkpoints. End-to-end throughput: 84.2 pages/hour. Pages 170–172 and 174–177 passed review; page 173 is processed but unresolved for scan-edge clipping. OCR extraction is faster than end-to-end implementation; the 400 pages/hour target is not met by the measured content workflow. Next page: 178.


Measured batch: PDF pages 178–181 completed from 2026-10-09 21:22:02 UTC to 21:24:12 UTC (2m10s), including rendering, visual review, translations, SVG/equation coding, comparison, tests, and checkpoints. End-to-end throughput: 110.8 pages/hour. Page 181 had low OCR coverage (0.42) and was checked against the rendered source directly. Next page: 182.


Measured batch: PDF pages 182–185 completed from 2026-10-09 21:24:12 UTC to 21:26:16 UTC (2m04s), including rendering, visual review, translations, SVG/equation coding, source comparison, checks, and checkpoints. End-to-end throughput: 116.1 pages/hour. OCR flagged p183 and p185 for review; both were checked against the rendered pages. Next page: 186.


Measured batch: PDF pages 186–189 completed from 2026-10-09 21:26:16 UTC to 21:28:03 UTC (1m47s), including rendering, visual review, translations, SVG/equation coding, comparison, tests, and checkpoints. End-to-end throughput: 134.6 pages/hour. Pages 187–189 had lower OCR matching and were compared with the rendered pages. Next page: 190.


Measured batch: PDF pages 190–193 completed from 2026-10-09 21:28:03 UTC to 21:30:15 UTC (2m12s), including rendering, visual review, translations, formula coding, source comparison, tests, and checkpoints. End-to-end throughput: 109.1 pages/hour. Pages 192–193 retain scan-edge/unreadable exercise fragments and remain unresolved. Next page: 194.


Measured batch: PDF pages 194–197 completed from 2026-10-09 21:30:15 UTC to 21:39:08 UTC (8m53s), including review of dense questions/table, translations, chapter routing, testing, and checkpoints. End-to-end throughput: 27.0 pages/hour. p195 and p197 had low OCR coverage and were checked directly against the rendered pages. Next page: 198.


Measured batch: PDF pages 198–201 completed from 2026-10-09 21:39:08 UTC to 21:46:02 UTC (6m54s), including scan review, translations, equations, coded figures, comparison, checks, and checkpoints. End-to-end throughput: 34.8 pages/hour. Page 199 is processed but unresolved for right-edge clipping. Next page: 202.


Measured batch: PDF pages 202–205 completed from 2026-10-09 21:46:02 UTC to 21:53:51 UTC (7m49s), including page-image review, translations, formulas/table/graphs, comparison, checks, and checkpoints. End-to-end throughput: 30.7 pages/hour. Page 203 remains unresolved for clipped introductory text. Next page: 206.



Measured batch: PDF pages 206–209 completed from 2026-10-09 21:53:51 UTC to 21:59:48 UTC (5m57s), including scan review, translation, SVG/equation coding, source comparison, checks, and checkpoints. End-to-end throughput: 40.3 pages/hour. All four pages visually checked and resolved. Next page: 210.


Measured batch: PDF pages 210–213 completed from 2026-10-09 21:59:48 UTC to 22:03:20 UTC (3m32s), including scan review, translated content, coded Figure 6.8, equation work, comparison, checks, and checkpoints. End-to-end throughput: 67.9 pages/hour. All four scans were visually checked. Next page: 214.


Measured batch: PDF pages 214–217 completed from 2026-10-09 22:03:20 UTC to 22:06:45 UTC (3m25s), including scan review, translated content, four coded SVG diagrams, calculations, comparison, checks, and checkpoints. End-to-end throughput: 70.2 pages/hour. All four scans were visually checked. Next page: 218.


Measured batch: PDF pages 218–221 completed from 2026-10-09 22:06:45 UTC to 22:09:44 UTC (2m59s), including scan review, translations, three coded SVG figures, Venturi derivation, lift calculation, source comparison, checks, and checkpoints. End-to-end throughput: 80.4 pages/hour. All four scans were visually checked. Next page: 222.


Measured batch: PDF pages 222–225 completed from 2026-10-09 22:09:44 UTC to 22:13:17 UTC (3m33s), including scan review, English/Urdu/Pashto content, coded figures, chapter key points, nine complete MCQs, comparison, checks, and checkpoints. End-to-end throughput: 67.6 pages/hour. All four scans were visually checked. Next page: 226.


Measured batch: PDF pages 226–229 completed from 2026-10-09 22:13:17 UTC to 22:19:44 UTC (6m27s), including scan review, translations, full MCQs/conceptual/numerical exercise text, Unit 7 entry, coded illustrations, comparison, checks, and checkpoints. End-to-end throughput: 37.2 pages/hour. Page 229 remains unresolved because its final learning outcome continues beyond the page. Next page: 230.


Measured batch: PDF pages 230–233 completed from 2026-10-09 22:19:44 UTC to 22:36:27 UTC (16m43s), including scan review, full trilingual text, formula rendering, illustrations, comparison, checks, and checkpoints. End-to-end throughput: 14.3 pages/hour. Page 229 continuation was resolved against p230. Next page: 234.


Measured batch: PDF pages 234–237 completed from 2026-10-09 22:36:27 UTC to 22:42:24 UTC (5m57s), including direct scan review, translations, equations, three coded figures, comparison, reader checks, and checkpoints. End-to-end throughput: 40.3 pages/hour. Page 229 continuation is resolved. Next page: 238.


Measured batch: PDF pages 238–241 completed from 2026-10-09 22:42:24 UTC to 22:47:50 UTC (5m26s), including energy equations, resonance text, three coded SVG figures, translations, OCR comparison, reader checks, and checkpoints. End-to-end throughput: 44.2 pages/hour. Cross-page resonance text was resolved. Next page: 242.


Measured batch: PDF pages 242–245 completed from 2026-10-09 22:47:50 UTC to 22:55:11 UTC (7m21s), including source review, translations, equations and waveform/MRI/microwave diagrams, source comparison, checks, and checkpoints. End-to-end throughput: 32.7 pages/hour. Next page: 246.

Measured batch: PDF pages 246–249 completed with all scans reviewed, source-matched text and translations, coded damping/resonance plots, comparison, reader validation, and checkpoints. Throughput: 4 pages in approximately 7 minutes, about 34 pages/hour. PDF pages 250–257 completed over the following approximately 20 minutes while implementing full exercise pages, new Unit 8, wave SVGs, OCR/image comparison, reader checks, and checkpoints; throughput approximately 24 pages/hour. Current checkpoint: page 257; next page: 258. These verified rates remain well below the 400 pages/hour target.
