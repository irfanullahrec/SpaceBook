# Hand-written solutions with animated boards: progress log

Goal (owner request 2026-10-24): every question that has no real worked solution gets one, written by hand per question, with its own board animation. Never invent mathematics: values are computed in code and compared with the book's printed answer; a disagreement is reported (docs below), the printed answer is preserved.

## Mechanism
- `SBSOL.add({ q, steps, board })` (`js/vr_auto.js`): a pack is found by the question text; the steps are shown row by row, the board (Venn, mapping, graph, unit circle...) is attached above the rows. Builders: `js/sol_sets.js` (sets + Venn), `js/sol_rel.js` (relations/functions + mapping diagrams). Pack files `js/sol_m10_*.js` (Class 10 Maths).
- Fix 2026-10-24: Class 1 and Class 10 problems store the printed answer as `finalAnswer`; the renderer showed an empty Answer pill. `app.js` now shows it.
- Check: `node tools/vr/check_packs.js [unit]` (which problems still have no pack; builder warnings = disagreements with the book).

## Done
- Class 10 Maths Units 5-13: 260/260 problems have a hand-written pack (`node tools/vr/check_packs.js` prints "260 | with a pack: 260 | still missing: 0", no builder warnings).
  - Unit 5 Sets/Functions (`sol_sets.js`, `sol_rel.js`, `sol_m10_u5_*.js`): Venn + mapping boards.
  - Unit 6 Statistics (`sol_stats.js`, `sol_m10_u6.js`): histograms, polygons, ogives, bar charts; every mean/median/mode/SD computed and checked.
  - Unit 7 Trigonometry (`sol_m10_u7.js`, `sol_m10_u7b.js`): conversions, arcs, identities (each identity checked numerically), applications.
  - Units 8-12 geometry (`sol_geo.js` + `sol_m10_u8_9.js`, `sol_m10_u10_11.js`, `sol_m10_u12.js`): diagrams drawn to scale from the lengths. Figure values for Ex 10.1, Review 10, Ex 11, Review 11, Ex 12, Review 12 were read from the scanned pages (Books/10th/10th Maths/JPG, scan = printed page + 2 here).
  - Unit 13 constructions (`sol_geocons.js` + `sol_m10_u13.js`): ruler-and-compass strokes replayed step by step (arcs, bisectors, circles, tangents).
- Question text key: the packs for Units 10-13 take the question text of the data in order (`DQ` array at the top of each file); if a data question changes, regenerate that array with the helper in tools (node dump of the unanswered questions).

- Class 9 Maths: all 109 problems whose stored solution was under 90 characters or had no equation (`node tools/vr/check_packs9.js` -> 109 | with a pack: 109). Files: `sol_m9_alg.js` (Review 4 from the book page), `sol_m9_fac.js` (Units 4-5 algebra and factorization, each factorization re-multiplied numerically), `sol_m9_misc.js` (Units 1, 2, 3, 7, 9), `sol_m9_graph.js` (Unit 8: coordinate boards, conversion graphs, intersections), `sol_m9_geo.js` (proof diagrams, one construction). Questions were checked against the scans (Books/9th/9th MTHA/JPG, scan = printed + 13); where the stored question differed from the book both versions are solved.
- Class 12 Maths: all 38 short-solution items (`node tools/vr/check_packs12.js` -> 38 | with a pack: 38). `sol_m12_hand.js` = hand-checked calculations (related rates, sign charts, domains, partial derivatives by finite differences, circular-motion model); `sol_m12_flag.js` = the stored paragraph explanations split into steps for the multiple-choice items.
- Validation: `node tools/vr/validate_packs.js` builds every pack's spec and renders every written row with KaTeX: 407 packs, 3343 rows, 0 TeX errors. Beware: in this Windows shell a Bash heredoc halves backslashes, so TeX must be written with the Write/Edit tools (a TeX string with lost backslashes still renders, as italic text, and passes the KaTeX check; grep the pack files for `'\angle` style strings when appending).

## Source discrepancies found (printed answers kept; the pack explains the difference)
- Class 10 Ex 5.5 Q2 (iv): printed "function, many-one onto"; with codomain {a,b,c,d} the relation {(a,b),(b,c),(c,b),(d,a)} never reaches d, so it is many-one into.
- Class 10 Review 5 Q3 (iv): "distributive property of union over union" is a printing slip (already noted in the data).
- Chemistry 10 c10chem-s241: equation unbalanced as printed.
- Ex 6.3 Q6 (printed total 30 but frequencies sum to 31); Ex 6.3 Q5 (says 9 workers, lists 8); Review 6 project: raw scores are not in the data, grouped values differ slightly from the printed 40.83/66.29/8.14.
- Ex 7.4 Q9 (i): printed 19.25 and 25.57; correctly rounded 19.26 and 25.56. Ex 7.4 Q4: sin 460° is in quadrant II (printed I); Q6 (vi) cosθ<0, tanθ<0 is quadrant II (printed III). Ex 7.3: fine. Ex 7.5 Q14 "(siny+cosy)/siny+(cosy-siny)/cosy = secy cosecy" is not an identity (y=30°: 3.155 vs 2.309). Ex 10.2/9: all numeric answers agree.
- Review 12 (iv): printed 40°; from the printed ∠SPT=100°, ∠PQS=40° the angle ∠PRQ is 60°. Review 12 Q2 (ii): 3y=76° gives y=25.33° (printed 25). Review 12 Q4 (v): the answer line says y but the unknown is x (=12°). Ex 11 Q1 (v): the figure shows legs 12 and 16 from O although O is the centre; the printed answer follows the right triangle.
- Review 12 Q3 and Ex 13: the data wrote the Pitot theorem with arc symbols; the book prints segment bars (sides), the pack proves the side version.

- Class 9: Review 4 Q7 (printed 1360, computed 800), Q9 (book asks a difference of cubes, printed answer has a plus sign), Q10 (printed 8/(x²−16), correct −8/(x⁴−16)); Ex 5.2 Q8 (printed 3xy should be xy), Ex 5.3 Q9 (printed −(3t−2)(4t+1) should be −(3t+2)(4t−1)), Review 5 Q8 (printed quotient/remainder do not match the division: 2x²−6x+14, −26); Ex 3.6 Q1(v) (printed key does not match the expression); Review 8 Q6 (the printed points form a parallelogram, not a rectangle), Q10 (stored x+y=1, book x+y=2), Q8 (stored y=x, book y=3), Q5 (stored square differs from the book's, both are squares); Ex 7.2 Q6 stored expression was wrong (book: 2√(5x)−3=7); Review 1 Q3 stored orders wrong (3×1 and 2×3).
- Class 12 (Review 6 iv): no printed option is correct (already stated in the data; the pack explains).

## Remaining (problems without steps)
- Source missing: Class 9 pages 144-158 of the book are not in the scans (Ex 5.6, Review 5 Q9-Q10): those items give the method and the printed result only. Classes 1-8 and 11 Mathematics and the other subjects (Statistics, CS, Biology, Class 11-12 Physics/Chemistry) were not audited in this pass for items with no real solution.
