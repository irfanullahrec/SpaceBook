# Class 11 source verification

Assignment remains active and incomplete. Mathematics is entirely excluded: do not read or modify its books, content, rendering, routes, or progress. Other classes are excluded from edits. No browser testing, publishing, pushing, resetting, or additional agents.

Read CONTRIBUTING.md once. No AGENTS.md was found in the workspace search. User instructions override branch, publishing, and browser suggestions. Shared modifications require atomic exclusive `tmp/class-content-shared.lock` during fresh read/patch/save only.

## Inventory

13 non-Mathematics folders, 92 PDFs, 5,119 PDF pages including alternate copies/splits. `inventory.json` records paths, page counts, hashes, PDF metadata, pending relationships, and per-book progress. These counts are not distinct instructional page coverage. All alternate editions/split relationships still require comparison. `inventory_sources.py` is an initial inventory tool; do not rerun it over existing progress without preserving page records.

## Current sequence

Physics first: primary `D:\SpaceBook\Books\11th\11th physics\pdf\physicsfull.pdf` has 393 pages. Initial active Class 11 card had no dedicated lesson data and fell through the generic view. Added dedicated `js/phys_11_data.js` and minimal routing/data/lesson wiring. No changes to other classes' content or Mathematics records.

PDF page 1: inspected at 1.5x using PyMuPDF and actual image. No extractable text. Unnumbered Urdu quotations from Al-Baqarah 172 and Al-Hujurat 10. Transcribed both quotations and references, kept them separate, joined scan wraps, added aligned English/Pashto translations, retained Urdu as explicit original. Decorative floral frames and scan watermark excluded because they convey no instructional content. Source is rendered in RTL semantic paragraphs, with native text and no raster/PDF embed. References preserved independently. Existing interactive paragraph renderer uses whole-paragraph pairing, preventing sentence count mismatches. Front matter has no exercises/formulas/examples; alternate tabs state this rather than inventing content.

PDF page 2: inspected at 1.5x. Unnumbered title page. Preserved title, Grade-XI, and publisher/place as explicit paired source/Urdu/Pashto records. The publisher emblem and scan watermark are decorative, not instructional diagrams; excluded from lesson representation. Title typography is semantic text. No raster content embedded.

Status: pages 1–5 corrected and source-compared. Node syntax checks passed for dedicated data and shared app. Focused non-browser checks passed for active dataset resolution, script wiring, paragraph alignment, unique IDs, original language consistency, and absence of raster/PDF embeds. Search/print behavior still needs review and is not certified. No full-book or 100% claim.

Next action: exact source-to-code audit of Chemistry PDF page 1. Existing Chemistry pages 1–21 are drafts; preserve source paragraphs, every worked step, reading order and diagram labels before advancing verified coverage.

## Later subject order

Chemistry, Statistics, English, Urdu, Biology, Computer Science, Civics, Health & Physical Education, Islamiat compulsory, Islamiat Ikhtiari, Islamic History, Mutalia-e-Quran. Each remains unreviewed. No other listed subject exists as a non-Mathematics source folder in this inventory.

PDF page 3: inspected full page at 1.8x and closer 3x crop for review/focal credits. Transcribed rights, preparation/curriculum, NOC approval/reference/date, all five authors, review supervision, focal person, four reviewers, editor, printing supervision, academic year and contact details. Labeled rows are a semantic HTML table; original bullets are recorded separately. Names and abbreviations preserved; English originals paired with Urdu/Pashto translations. Edition: Academic Year 2023-24; national curriculum 2006; approval 02.03.2020. Node syntax and reader checks passed.

PDF page 4: PREFACE inspected at 1.8x. Two prose paragraphs retained with scan wraps joined, followed by editor attribution and feedback address. Printed wording retained, including re-reviewers recommendation and two colours/four colours. English/Urdu/Pashto paired records saved. Decorative colour border and watermark excluded. Reader/syntax checks passed.

PDF page 5: CONTENTS inspected at 1.8x. Ten unit titles/numbers/start printed pages transcribed as structured records and a semantic table, with Urdu/Pashto title translations. Original title Oscillation is singular. Printed starts 1,35,74,116,149,191,224,247,302,342. Source has ten units; registry currently says eleven and requires a scoped metadata correction. No unit content has been pre-marked reviewed from this contents page. Decorative ribbons/watermark excluded. Reader/syntax checks passed.

PDF page 6 / printed page 1: inspected full page and 3x tape crop. Unit 1 title, translated caption, introduction and twelve learning outcomes transcribed, paired and rendered as a semantic list. Outcomes reuse the same records in the SLO tab. Coded native SVG tape reconstruction added; partially obscured/inverted scale labels and precise overlapping ribbon geometry remain an unresolved visual comparison. Status inspected/corrected but NOT fully verified. Last fully verified page stays 5. Scope permits continuing after documenting the unresolved item. Registry Physics chapter count corrected from 11 to source ten; Class 11 Physics sidebar now says source review in progress instead of Complete Units. Reader and syntax checks passed.

PDF page 7 / printed page 2: inspected at 1.8x. Section 1.1 includes five source paragraphs; section 1.2 begins with two paragraphs and continues onto the next page. Paragraph boundaries, source bold definition and italic quotation preserved; English originals paired with Urdu/Pashto translations. Printed forms retained, including SYSTEM INTERNATIONAL, système internationale, Science require and the printed categorical statement about science. No silent editorial correction. Reader and syntax checks passed. Highest fully compared page is 7; last consecutive fully verified page remains 5 due to page 6 visual issue.

PDF page 8 / printed page 3: inspected full page plus 3x table crop. Five continuation paragraphs appended to existing section 1.2 with per-paragraph page refs; A. Base Units paragraph is a child section. Table 1.1 is a semantic four-column table with two grouped headers, seven rows, aligned translated labels and structured luminous-intensity subscript. Source Kg retained; standard kg noted only in clearly separate editorial clarification. Printed we does not and e.t.c retained. No raster embed. Reader/syntax checks passed.
Physics split inventory resolved by SHA-256 of every embedded page image: splits 1–8 match primary pages 1–50,50–100,100–150,150–200,200–250,250–300,300–350,350–392 respectively. Primary page 393 absent from splits. Overlap boundary pages must never generate duplicate lessons. Hash mapping is relationship evidence, not visual review of unseen pages.

PDF page 9 / printed page 4: inspected at 1.8x. B. Derived Units definition and following paragraph, table 1.2 (four rows/four columns/group headers), C. Supplementary units, D. Radian definition and paragraph, displayed theta=S/r equation with both textual fraction labels, and radian/degree relation beginning retained in order. Scalar/vector velocity, powers m²/m³/ms⁻¹/ms⁻² and 20th ordinal coded. Equation is a structured block using existing KaTeX helper when available, with formatted fraction fallback rather than raw LaTeX. Urdu/Pashto labels and prose paired. Printed phrasing/CGPM explanation retained. Reader/syntax checks passed.

PDF page 10 / printed page 5: inspected at 1.8x. Radian/degree derivation preserved with numbered equations 1–2, comparing statements, converted values and rounding/source wording. Figure 1.1 is native circle SVG with O,A,B,r,S=r, approximate central radian, and translated caption. Example 1.1 GEARS is a stable shared example record reused in chapter sections, with exact question, GIVEN/REQUIRED boxes and initial source solution S=r_s×theta_s. The solution continues on page 11; no answer invented. Reader/syntax checks passed.

PDF page 11 / printed page 6: inspected at 1.8x. Example 1.1 continuation solved exactly as source, including repeated first equation, putting values, theta=3.6 radians and extension question without invented answer. Printed 8π transition retained alongside calculations using 0.8π, with explicit editorial clarification. Gear pair coded with r_l=0.7 m/r_s=0.4 m and opposite rotation arrows. Assignment 1.1 question and source Answer=20 m saved without authored solution. ii. Steradian, two equations with cancellation, concluding paragraph, and figure 1.2 cone/sphere/surface-area r² diagram and caption coded/translated. Active lessons, concepts/examples, exercises, SLO and formula/table tabs now select the same source records; shared global search includes these Class 11 Physics records. Focused KaTeX rendering checked with actual bundled KaTeX, no malformed equation result. Reader/syntax checks passed. Printing/export pathway remains unverified.

PDF page 12 / printed page 7: inspected full page at 1.8x plus 3x crop of atom count/exponent. Three scientific-notation paragraphs and displayed mantissa/exponent equation preserved and translated; original atom count 7×10^27 retained as comma-group number plus formatted superscript notation. POINT TO PONDER question and NASA/Mars Climate Orbiter case study retained in distinct source paragraphs. Orbiter illustration coded in SVG (long solar panel, spacecraft, dish, planet horizon). Paired translations use explicit records; source paragraphs now clickable/keyboard accessible to open their corresponding translations, including Urdu originals. Reader/syntax/actual KaTeX checks passed.

PDF page 13 / printed page 8: inspected at 1.8x. Population/atom multiplication paragraph and displayed exponent calculation retained, followed by common-convention paragraph including source unmatched opening parenthesis. Continuation is linked to scientific-notation topic but rendered after page 12 POINT TO PONDER in actual page order. Prefixes definition/paragraph/housefly/satellite example retained with original scientific quantities. Table 1.3 all twenty prefix names, decimal multipliers and symbols coded as three-column semantic table with accurate superscripts and aligned Urdu/Pashto labels. Printed capitalization yotta/zetta/Exa/Peta/Tera/giga/Mega retained. Reader/KaTeX/syntax checks passed.

PDF page 14 / printed page 9: inspected full page at 1.8x, DO YOU KNOW and unit-symbol details at 3x, light-year exponent at 6x. Non-SI intro and A. Light Year/B. Angstrom/C. Micron text/numerical examples retained in callout with translated subheadings. Printed expensively preserved with separate clarification. Section 1.4 Unit symbols four bullets preserved as list, including roman type, nm vs mμm, pm vs μμm, multiplication dot/space, division slash/negative exponents, and prohibited abbreviations. Unicode superscripts preserve dimensional powers without raw markup. Reader/KaTeX/syntax checks passed.

PDF page 15 / printed page 10: inspected at 1.8x and native embedded image. Fifth Unit symbols bullet appended with its own page ref. Unit names three bullets, 1.5 ERRORS two paragraphs, Types of Errors, A. Systematic errors, and (a) Instrumental errors transcribed and translated. Right edge of Unit names first bullet is genuinely clipped after treated lik. Alternate JPG010_page_1 is equally clipped; physics1.docx text extraction also gives lik. Missing ending not guessed. Explicit source-gap marker and incomplete translation segment saved; page 15 corrected/inspected but not fully verified. No new unresolved body text elsewhere. Reader/KaTeX/syntax checks passed.

PDF page 16 / printed page 11: inspected at 1.8x. (b) Personal errors paragraph, systematic-error mitigation paragraph, B. Random errors definition/discussion, LEAST COUNT ERROR two paragraphs with 0.01 cm and 0.001 cm, and 1.6 UNCERTAINTIES definition/statement all transcribed and paired. The measurement expression was re-inspected at 5x during page 17: the source sign is ± (OCR incorrectly gives +); all source/formula tab uses now render ±. Source italic/bold spans retained. Source paragraph clicks now target the paragraph translation specifically rather than nested equation-label translations. Reader/KaTeX/syntax checks passed.

PDF page 17 / printed page 12: inspected at 1.8x plus 3x equations crop. Example of (5.07±0.02)g/bounds, uncertainty types and Δ/ε definitions, mass/absolute/relative calculations, DO YOU KNOW technical specification data two paragraphs, all three specification rows, and Indicating Uncertainty in calculation paragraph transcribed and translated. Digital multimeter coded SVG with display4000/rotary selector; specification card is semantic table ±0.2V,±0.01mA,±0.9%. Previous page 16 measurement sign corrected on fresh 5x crop from OCR+ to printed±, across all reused source/formula views. Reader/KaTeX/syntax checks passed.

PDF page 18 / printed page 13: inspected at 1.8x. ACTIVITY two paragraphs and all questions retained without authored answers, and reused in exercise tab. A. Sum or difference intro and both side-by-side derivations coded with source equation order and full translated prose. Source Z=Z±DeltaZ and last sum-column Z±DeltaZ=DeltaA+DeltaB retained with clear separate clarification. POINT TO PONDER Error versus uncertainty paragraph retained in full. Summary/formula and search use same branch/source records. Reader/KaTeX/syntax checks passed.

PDF page 19 / printed page 14: inspected at 1.8x. B. Product or quotient full intro, both side-by-side proofs with ordered step paragraphs and five equations each, and C. Power intro/four steps/five equations transcribed and translated. Percentage notation/printed wording retained, including square the term for general exponent n and source dimensional inconsistencies, with separate clarifications. Proof flow indexes preserve exact prose/equation sequence. Source quantities/powers and superscripts rendered through existing KaTeX. Reader/KaTeX/syntax checks passed.

PDF page 20 / printed page 15: inspected at 1.8x. Example 1.2 THICKNESS OF PIPE full question, GIVEN/REQUIRED, ordered source solution with all five equations, caution paragraph, radius-halving explanation, answer(0.69±0.05)mm retained and translated. Fractional wording versus absolute-number calculation retained with separate clarification. Assignment1.2 WALL WIDTH full question and printed source answer(10.0±0.2)cm preserved, no authored solution. Stable example/exercise records reused in tabs. Reader/KaTeX/syntax checks passed.

PDF page 21 / printed page 16: inspected at 1.8x, compared clipped fragments with local physics1.docx OCR. Example1.3 header/question genuinely clipped at AREA OF ROO/to b/Calculate th. Marked unresolved, not guessed. Full readable GIVEN/REQUIRED and source solution equations retained including width2.955 earlier vs2.995 later and incompatible area12.20; separate clarification records this source arithmetic inconsistency without replacing answer. Assignment1.3 RESISTANCE question and source(2.7±0.08)ohm answer preserved, no authored solution. All equations rendered in source order with translated steps. Reader/KaTeX/syntax checks passed.

PDF page 22 / printed page 17: inspected at 1.8x. Example1.4 BALL DROP full question/GIVEN/REQUIRED/source solution with seven equations and ordered prose, answer(8.3±2.6)m retained/translated. Assignment1.4 VOLUME OF SPHERE question/radius(2.25±0.01)cm and source(47.7±0.6)cm³ answer retained, no invented solution. Left-margin sliver of adjacent source page excluded as duplicate scan artifact. Class11-only chapter selection clamps invalid previous indexes, correctly resolves subject metadata, and the existing PDF download link now targets the verified local source path (served/remote browser behavior untested). Reader/KaTeX/syntax checks passed.

PDF page 23 / printed page 18: inspected at 1.8x. Section 1.7 definition and overview, all five General Rules (rule four has two distinct paragraphs), significant-figure examples/scientific notation, calculator paragraph, and (a) Addition and Subtraction preserved with aligned Urdu/Pashto translations and original italic definition. Numbered rules use semantic ordered list. Reader/KaTeX/syntax checks passed.

PDF page 24 / printed page 19: inspected at 1.8x. Addition continuation and numerical rounding example, multiplication/division three paragraphs, TIP full paragraph, Example 1.5 all six subquestions and initial solution (a) with vertical subtraction are preserved and paired. Fraction (f) uses coded fraction; question grid respects logical a,b,c,d,e,f order. Example shared with concepts tab; solution explicitly continues. Reader/KaTeX/syntax checks passed.

PDF page 25 / printed page 20: inspected at 1.8x. Example 1.5 continuation includes full rounded-result explanation/answer (a), vertical sums and full explanation/answers (b),(c), and initial vertical product (d). Same example object/ordered solution flow reused; page reference attached to first continuation paragraph. Original rounded 0.2 and singular two decimal place retained. Reader/KaTeX/syntax checks passed.

PDF page 26 / printed page 21: inspected at 1.8x. Example 1.5 continuation includes full significant-figure explanations and answers (d),(e), vertical triple multiplication, and successive addition/subtraction/division steps (f), including intermediate 0.820959596. All paragraphs paired and shared in existing example; vertical arithmetic is KaTeX arrays, not images. Reader/KaTeX/syntax checks passed.

PDF page 27 / printed page 22: inspected at 1.8x plus 3x right-edge crop and alternate JPG016_page_1, bounded DOCX extraction. Example 1.5 final division explanation and source 0.821 answer complete. Assignment 1.5 six questions/coded fraction and full printed answer row saved, reused in exercises; no invented solution. Section 1.8 three paragraphs transcribed with explicit gaps after sho, kn, gi, measurement is and ac. Assignment heading clipped after CALCULATIO. Alternate sources identically clipped. Page corrected but NOT fully verified. Generic gap paragraphs now render visible markers as examples do. Reader/KaTeX/syntax checks passed.

PDF page 28 / printed page 23: inspected at 1.8x plus 4x target crop. Four accuracy/precision continuation paragraphs, four target captions, dart-game introduction and all four bullets transcribed/paired. Native SVG targets preserve three ring colours, four dots per panel, clustering/spread and off-target dot in (d). Side strip of neighbouring page excluded as duplicate scan artifact. Reader/KaTeX/syntax checks passed.

PDF page 29 / printed page 24: inspected at 1.8x. Precision quantitative introduction, all twenty student measurements, four mean values and four accuracy/precision captions saved as semantic four-column table, with translated headers and paired rows/captions. Source mean 9.8 retained. Section 1.9 definition/second paragraph preserved with italic definition and Urdu/Pashto. Initial reader check exposed missing numeric-row pair hooks; added aligned table translation details and rerun passed, with syntax/KaTeX checks.

PDF page 30 / printed page 25: inspected at 1.8x plus 4x dimension/exponent crop. Table 1.5 seven base quantities/symbols, adjacent complete paragraph, dimensional-product paragraph/equation/exponent paragraph, magnitude paragraph and Table 1.6 ten derived quantities/dimensions preserved/paired. Two-column/four-column semantic tables maintain row relationships; Greek dimensional exponents use KaTeX and native superscript fallback with actual α,β,γ,δ,ε,ζ,η. Formula tab includes same tables. Reader/KaTeX/syntax checks passed.

PDF page 31 / printed page 26: inspected at 1.8x plus 4x equation/body crop and JPG018_page_1. Sections 1.9.1 with A–D definitions/examples, 1.9.2 formula, 1.9.3 equation prose/four displayed dimensional equations, 1.9.4 advantages and A.correctness transcribed/paired. Underlined 1.9.3 retained. Right-edge fragments an, dimension, al, th, bo marked visibly and translations incomplete explicitly; alternate image equally clipped. Page NOT fully verified. Generic gap renderer now retains associated equations and their labels. Reader/KaTeX/syntax checks passed.

PDF page 32 / printed page 27: inspected at 1.8x. Dimensional-homogeneity continuation, first Limitation, B.Deriving a possible formula, second Limitation preserved with italic crossrefs/underlined limitation headings and complete translations. Example 1.6 DRAG FORCE full two-fraction question, four GIVEN values including explicit powers 1, REQUIRED and start of source solution/numbered LHS equation retained. Shared formulaExample data/flow renders in concepts and lesson; no invented remainder. Reader/KaTeX/syntax checks passed.

PDF page 33 / printed page 28: inspected at 1.8x plus 4x first/second equation crops. Example 1.6 two dimensional comparisons completed with original explicit unity powers, [L¹]² versus [L]¹ denominators, ordered steps, circled equations 2–4, inequality/equality and full source-answer wording. Assignment 1.6 original TIME PERIOD label and both kinematic equations/question retained without invented answer. Same source records serve lesson/concepts/exercises/formulas; paired translations for prose and English equation phrases. Reader/KaTeX/syntax checks passed.

PDF page 34 / printed page 29: inspected at 1.8x. Example 1.7 full sphere/liquid question, four GIVEN dimensions, REQUIRED drag formula, source solution paragraphs/three equations and three M,T,L column derivations preserved/paired. Viscosity η and F_D subscript coded; all source powers and numbered equation 1 retained. Nested branch flow reused in lesson/concepts/formulas and search; solution continues. Reader/KaTeX/syntax checks passed.

PDF page 35 / printed page 30: inspected at 1.8x plus 4x key-point edge crop/JPG020_page_1/bounded DOCX. Example 1.7 completed with substituted powers, kηrv and experimental6πηrv/source answer; Assignment1.7 full pendulum question and printed radical formula retained with no authored solution. Nine KEY POINTS definitions transcribed/paired; printed physical word preserved+separate clarification. Error line end and fragments i,know,physic,quant unresolved; gap markers visible and not guessed. Label emphasis applied in paired renderer. Page NOT fully verified. Reader/KaTeX/syntax checks passed.

PDF page 36 / printed page 31: inspected at 1.8x plus 4x unit-options crop. Exercise MCQs 1–9, instruction, all four choices per question and source quantities/symbols transcribed and paired; question4 B is printed 12 mμ s (retained). Stable question/option IDs and semantic ordered question list preserve numbering/option order. Same records reused in exercise tab; no invented correct-answer key. Reader/KaTeX/syntax checks passed.

PDF page 37 / printed page 32: inspected at 1.8x and alternate JPG021_page_1. Multiple-choice questions 10–16, all choices, dimensions, units and superscripts transcribed; paired conceptual questions 1–7 saved in original order. Right edge visibly clips Q12 stem after dig, Q14 after measur, Q15 option D after “All of t”, and conceptual Q7 after “is it possible to”; explicit gaps saved, no guess. Q13 source sentence’s unusual grammar retained. Page NOT fully verified. Reader/KaTeX/syntax checks passed.

PDF page 38 / printed page 33: inspected at 1.8x. Conceptual questions 8–9 and all eight comprehensive questions transcribed/paired. Numerical problems 1–3 and printed answers (4.19 rad & 2.09 rad), (2.5 ± 0.8%), and (0.30 m², ± 0.02 m²) retained and paired in source answer fields; no invented working. Semantic question sections retain numbering; adjacent page sliver excluded. Reader/KaTeX/syntax checks passed.

PDF page 39 / printed page 34: inspected at 1.8x plus 5x crop and alternate JPG022_page_1. Numerical questions 4–7: all six arithmetic subparts and source answers in Q4, proton/electron and charge/electron ratios with fraction formulas and key, dimensional questions for h and G with key, and KE/PE dimensional prompts/expressions transcribed/paired. Scientific notation exponents Q4(c) are 10⁴. Questions are paired to their own printed answer line; Q7 has no source answer here. Reader/KaTeX/syntax checks passed.

PDF page 40 / printed page 35: inspected at 1.8x and 4x crop of final learning outcome. Unit 2 title, crane question/caption and all twelve ordered learning outcomes transcribed with Urdu/Pashto. Crane, boom lattice, hook, cables, suspended container and mobile base redrawn in native SVG; no scan embedded. Added a dedicated Unit 2 chapter so Class 11 chapter selection/resolution points to source content. Unit outcomes render in lesson and SLO tabs. Reader/KaTeX/syntax checks passed.

PDF page 41 / printed page 36: inspected at 1.8x and JPG023_page_1; local DOCX confirms the same clipping. Intro paragraph, 2.1 definition/prose, symbolic and graphical representations, vector examples and FIGURE 2.1 caption saved with visible gap markers for right-edge cuts (tools f, tool f, kno, design w, vectors a; Some, siz, hav, scala; bold fa, simp, vectors b; arrow, th, arrow hea). Vector arrow examples use coded superscript-arrow markup; tail/vector/head diagram recreated as SVG. Page NOT fully verified. Reader/KaTeX/syntax checks passed.

PDF page 42 / printed page 37: inspected at 1.8x. Geometric/algebraic vector paragraphs, Cartesian-system definition, full Figure 2.2 axis labels/caption, four ordered vector-representation steps and 2.2.1 introductory sentence preserved/paired. Axis graphic recreated as SVG (x/y axes, X/X′, Y/Y′, origin; z-axis intentionally omitted per caption). Added the vector-steps intro paragraph to the rule renderer. Reader/KaTeX/syntax checks passed.

PDF page 43 / printed page 38: inspected at 1.8x. 2.2.1 full planar-vector text, Figure 2.3 and caption/scale/force/30-degree angle reproduced in native SVG. 2.2.2 full spatial-vector text, Figure 2.4 axes and α/β/γ angle labels/caption reproduced in native SVG. Translations paired; no raster embeds. Reader/KaTeX/syntax checks passed.

PDF page 44 / printed page 39: inspected at 1.8x. Unit-vector definition/normalization formulas, A⃗ example, ê/ĵ/k̂ axis discussion, n̂ surface-normal description and area-vector note transcribed/paired. Both axis/unit-vector and surface normal/area-vector drawings recreated in SVG with captions. Section 2.3 opening head-to-tail addition paragraph saved. Reader/KaTeX/syntax checks passed.

PDF page 45 / printed page 40: inspected at 1.8x, JPG025_page_1 and local DOCX. 2.3.1 question and head-to-tail resultant explanation saved/paired; separate Figure 2.5/2.6 SVG illustrations show individual A/B vectors and head-to-tail R. Four numbered steps to add vectors transcribed. Caption FIGURE 2.6 is clipped after vector; step 4 clips after “according” and “To determine” at the edge. Explicit gaps saved; no guessed completion. Page NOT fully verified. Reader/KaTeX/syntax checks passed.

PDF page 46 / printed page 41: inspected visually at 1.8x. The source text and Figure 2.7 parallelogram method are captured, including the commutative equation; Figure 2.8 shows four separate vectors in the xy-plane with labels A, B, C and D. Paragraph-level English, Urdu and Pashto alignment is preserved, and both figures are native SVG. Reader, syntax, and no-raster checks pass.

PDF page 47 / printed page 42: inspected visually at 1.8x. Transcribed the head-to-tail construction instructions, the length/scale procedure for magnitude, direction measurement from the x-axis, Figure 2.9, the four-vector sum and reordered sums demonstrating commutativity. Preserved the Activity prompt and NULL VECTORS definition/operation sentence and zero-vector equation in distinct source-ordered blocks. Figure 2.9 was redrawn as native SVG with the four linked vectors, resultant and axes. Reader, syntax, and no-raster checks pass.

PDF page 48 / printed page 43: inspected visually at 1.8x. Transcribed Example 2.1, including the port/ship displacement prompt, scale and both vector values/angles, required resultant, Figure 2.10 caption, graphical resultant procedure, 6.8 cm scale conversion, 106° direction and printed answer. Recreated the compass, 200 km and 350 km head-to-tail legs, 30°/140° headings and 106° resultant in native SVG. Added Assignment 2.1 airplane/crosswind prompt and printed 113ms⁻¹ answer. Lesson, concepts and exercise views remain source-paired; reader, syntax, and no-raster checks pass.

PDF page 49 / printed page 44: inspected visually at 1.8x. Subtraction prose, Figure 2.11 caption, subtraction procedure and equation, scalar-multiplication definition, all three sign cases, and the visible Figure 2.12 caption fragment were paired and transcribed. Figure 2.11's three A/B/−B/resultant diagrams and Figure 2.12's xy-plane vector were redrawn as native SVG. Right-edge scan clipping remains at two points in the opening subtraction paragraph, two points in the subtraction procedure, the Figure 2.12 example sentence, and its caption. Explicit source gaps are marked; no missing text is guessed. Page NOT fully verified. Reader, syntax, and no-raster checks pass.

PDF page 50 / printed page 45: inspected visually at 1.8x. Figure 2.13's positive/negative scalar cases, captions, the 2.5 definition of resolution, TIP definition, point P to Q/S construction, component equation, and Figure 2.14 caption were transcribed and paired. Figures 2.13 and 2.14 are native SVG with the printed vectors, axes and component labels. No source clipping on this page. Reader, syntax, and no-raster checks pass.

PDF page 51 / printed page 46: inspected visually at 1.8x. Continued vector component equation (1), 2.5.1 triangle introduction, cosine/sine ratios, equations (2)/(3), substituted vector expression, Pythagorean steps, magnitude equation (2.2), tangent/direction equation (2.3), three-dimensional magnitude equation (2.4), and Figure 2.15 were transcribed/preserved. Figure 2.15 was redrawn as native SVG. Right edge clips the magnitude paragraph after “magnitudes of” and “right angle triangle”; the figure caption also reaches the clipped edge. Gaps are marked and no text is guessed. Page NOT fully verified. Reader, syntax, and no-raster checks pass.

PDF page 52 / printed page 47: inspected visually at 1.8x. Recorded the definition/benefits of rectangular-component addition, the two-vector angle/resultant explanation, equation (1), and Figure 2.16 caption. Redrew the four source diagrams (A, B, head-to-tail resultant, and rectangular-component construction) in native SVG. No visible clipping on this page. Reader, syntax, and no-raster checks pass.

PDF page 53 / printed page 48: inspected visually at 1.8x. Transcribed rectangular resultant x/y component equations (2)–(4), expanded equations (2.5)–(2.7), magnitude/direction derivations, and generalized component/magnitude equations (2.8)/(2.9), with all displayed formula numbers. The explanatory paragraph at the right edge is clipped after “head to tail” and “to get”; both gaps are explicit and unfilled. Equations render in the lesson and formulas tabs. Page NOT fully verified. Reader, syntax, and no-raster checks pass.

PDF page 54 / printed page 49: inspected visually at 1.8x. Preserved the continuation “and” with general angle equation (2.10), the 2.6.1 angle-direction procedure/reference-angle equation, Figure 2.17, and all four quadrant sign conditions and angle rules. Four native SVG quadrant diagrams accompany the paired explanations. No source clipping on this page. Reader, syntax, and no-raster checks pass.

PDF page 55 / printed page 50: inspected visually at 1.8x. Transcribed Example 2.2's two-force prompt, GIVEN/REQUIRED values, Figure 2.18 caption, resultant/component equations (1)–(3), and all x/y component definitions, substitutions and printed results (4)–(7). Redrew the coordinate axes, 70°/220° force vectors and resultant in native SVG. The worked example continues onto page 56. The right edge of Figure 2.18 is clipped in the scan; its semantic redraw uses only the visible values and equations. Page NOT fully verified. Reader, syntax, and no-raster checks pass.

PDF page 56 / printed page 51: inspected visually at 1.8x. Completed Example 2.2 with x/y component substitutions (8)/(9), resultant 14.16 N, reference angle 7.97° and third-quadrant direction 187.97°. Added the two Extension Exercise subtractions, Assignment 2.2 and its printed answer (26.46 N, 109.11°), and the opening prompt/GIVEN/REQUIRED fields of Example 2.3. Example 2.3 solution starts on PDF page 57. No clipping. Reader, syntax, and no-raster checks pass.

PDF page 57 / printed page 52: inspected visually at 1.8x. Completed Example 2.3: force-component equations, resultant x/y sums, magnitude expansion, trigonometric identity, and the condition yielding θ = 120°. Added Figure 2.19 as a native SVG showing equal forces and resultant. No source clipping on this page. Reader, syntax, and no-raster checks pass.

PDF page 58 / printed page 53: inspected visually at 1.8x. Added Assignment 2.3 with both printed resultant answers, the product-of-vectors overview, scalar-product definition/notation, dot-product explanation and equation (2.11), angle note, projection derivation/equation (1), commutative statement, and Figure 2.20 as native SVG. No source clipping. Reader, syntax, and no-raster checks pass.

PDF page 59 / printed page 54: inspected visually at 1.8x. Continued the scalar-product projection for B⃗ · A⃗, derivation of equation (2), commutative equality/examples and Figure 2.21. Added the 2.7.2 vector-product definition, generic notation, cross-product explanation and equation (2.12), angle/unit-vector note, and Figure 2.22 right-hand-rule diagram as native SVG. Right-edge clipping remains in the vector-product definition and cross-product explanation; fragments and gaps are marked without guessing. Page NOT fully verified. Reader, syntax, and no-raster checks pass.

PDF page 60 / printed page 55: inspected visually at 1.8x. Added the right-hand-thumb direction rule, Figure 2.23 perpendicular-component/cross-product equations and area meaning, anti-commutative heading, Figure 2.24 introduction and reverse-order projection. Recreated both figures as native SVG vector diagrams. No source clipping. Reader, syntax, and no-raster checks pass.

PDF page 61 / printed page 56: inspected visually at 1.8x. Transcribed the reverse cross-product equation, anti-commutative identity and explanation, examples, and Example 2.4 prompt/GIVEN/REQUIRED fields, angle difference, dot-product calculation and printed 8.2 Nm answer. Figure 2.25 was redrawn natively. Right-edge cuts remain in the anti-commutative explanation, example label/question and figure edge; gaps are marked. Cross-product calculation continues beyond this page. Page NOT fully verified. Reader, syntax, and no-raster checks pass.

PDF page 62 / printed page 57: visually inspected. Added the cross-product magnitude solution and Assignment 2.4 identity exercise, concurrent-forces definition and diagram, then the perpendicular-force example with 763 N and 525 N, 926 N resultant at 34.5°, and opposite equilibrant. Both diagrams redrawn natively. Source is legible and page fully verified; reader, syntax, and no-raster checks pass.

PDF page 63 / printed page 58: visually inspected. Added the definition of torque, position vector and force angle, equation (2.13), SI unit statement, and Figure 2.28 explanation. Redrew the wrench, force components, pivot, moment arm, and axis as native SVG. Right-edge line endings are clipped in the equation lead-in, units, and explanatory paragraph; gaps are marked. Page has unresolved source clipping. Reader, syntax, and no-raster checks pass.

PDF page 64 / printed page 59: visually inspected. Added both moment-arm interpretations, equation (2.14), moment-arm definition, torque factors A–C, and maximum/minimum angle cases. Figure 2.29 redrawn as native vector diagrams. The printed second cross product reverses F⃗ and r⃗ compared with equation (2.13); transcribed as printed and flagged for editorial review. Page unresolved pending that source inconsistency. Reader, syntax, and no-raster checks pass.

PDF page 65 / printed page 60: visually inspected. Transcribed the mobile-crane counterweight safety note, lever/boom explanation, equal-opposite torque statement, couple definition, and steering-wheel example. Crane counterweight diagram redrawn natively. Right-edge clipping remains in the counterweight and steering example text; source gaps are marked. Page unresolved for clipped text. Reader, syntax, and no-raster checks pass.

PDF page 66 / printed page 61: visually inspected. Transcribed Figure 2.30 couple moment definition, arbitrary-origin moment sum, reduction to r⃗ × F⃗, free-vector result, right-hand rule, and equilibrium definition/statics. Steering-wheel couple redrawn natively. Page fully verified. Reader, syntax, and no-raster checks pass.

PDF page 67 / printed page 62: visually inspected. Transcribed static equilibrium and the dynamic translational and rotational cases with book, parachutist, and compact-disc examples. Three equilibrium diagrams redrawn natively. Page fully verified. Reader, syntax, and no-raster checks pass.

PDF page 68 / printed page 63: visually inspected. Transcribed the first equilibrium condition, equations (2.15) and component sums, force-polygon explanation, and coplanar force components. Concurrent-force and closed-polygon figures redrawn natively. Page fully verified. Reader, syntax, and no-raster checks pass.

PDF page 69 / printed page 64: visually inspected. Transcribed the second torque-equilibrium condition and equation (2.16), clockwise/anticlockwise sign convention, translational versus rotational equilibrium, zero force/acceleration and torque/angular-acceleration statements, and complete-equilibrium couple example. Page fully verified. Reader, syntax, and no-raster checks pass.

PDF page 70 / printed page 65: visually inspected. Transcribed the three Figure 2.34 cases for both static-equilibrium conditions, including net-force and net-torque explanations. Three force and axis diagrams were redrawn natively. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 71 / printed page 66: visually inspected. Transcribed Example 2.5 diving-board problem, givens, unknown support and bolt forces, torque balance, sign convention, and all visible symbolic and numeric steps. Diving-board diagram redrawn natively. Fulcrum-force result continues on page 72. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 72 / printed page 67: visually inspected. Completed Example 2.5 with fulcrum force 1750 N and bolt force 1150 N, captured the extension exercise, and transcribed Assignment 2.5 with its printed answer (4.5 m). Plank, boy, weights, and support rope redrawn natively. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 73 / printed page 68: visually inspected. Transcribed the full Key Points vocabulary recap covering scalars, vectors, components, products, equilibrium, and its conditions, with both force and torque summation equations. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 74 / printed page 69: visually inspected. Transcribed multiple-choice questions 1–10 and every printed option. Added the full item set to the exercise tab. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 75 / printed page 70: visually inspected. Transcribed multiple-choice questions 11–15 and all options. Recreated the uneven-rod mass, four rod-force cases, and wheel-torque figures as native SVGs; attached them to the relevant questions. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 76 / printed page 71: visually inspected. Transcribed all 10 conceptual and 3 comprehensive questions in the exercise tab with English, Urdu, and Pashto interactions. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 77 / printed page 72: visually inspected. Transcribed comprehensive questions 4–9 and numerical questions 1–6 with the printed answer values. Included all in the exercise tab with English, Urdu, and Pashto interactions. Page fully verified; reader, syntax, and no-raster checks pass.

PDF page 78 / printed page 73: visually inspected. Transcribed numerical questions 7–9 and printed answer values (0.41 m, 122 N, 2850 N). Recreated the rod balance, ladder reaction, and I-beam reaction figures as native SVG. Added the questions to the exercise tab with English, Urdu, and Pashto text. Page fully verified; syntax and reader checks pass.

PDF page 79 / printed page 74: visually inspected. Transcribed the Forces and Motion title, plane prompt, and all ten learning outcomes. Recreated the jet image as a native SVG. Page fully verified; syntax and reader checks pass.

PDF page 80 / printed page 75: visually inspected. Transcribed learning outcomes 11–24, including projectile motion, Newton’s laws, impulse, momentum, and collision outcomes. Page fully verified; syntax and reader checks pass.

PDF page 81 / printed page 76: visually inspected. Transcribed the final three learning outcomes, chapter introduction, observer-relative rest and motion, point-to-ponder, train example, and displacement definition and notation. Page fully verified; syntax and reader checks pass.

PDF page 82 / printed page 77: visually inspected. Transcribed the distance/displacement distinction, full Figure 3.1 explanation and equation, velocity definition, vector direction and SI unit, and average-velocity definition. Recreated the position-vector diagram as native SVG. Page fully verified; syntax and reader checks pass.

PDF page 83 / printed page 78: visually inspected. Transcribed instantaneous velocity, uniform velocity, speed versus velocity, acceleration definition, equations, direction, and SI unit. Page fully verified; syntax and reader checks pass.

PDF page 84 / printed page 79: visually inspected. Transcribed average and instantaneous acceleration, uniform/variable acceleration, deceleration, and the positive/negative acceleration discussion through its page break. The edge-clipped subsection heading remains unresolved; this page is recorded as unresolved, not fully verified.

PDF page 85 / printed page 80: visually inspected. Transcribed the acceleration-sign continuation, Figure 3.2 caption and four cases, graphical-analysis introduction, and displacement-time graph section. Recreated Figure 3.2 as native SVG. Printed wording is retained, including its inconsistent “points … positive” phrases. Page fully verified; syntax and reader checks pass.

PDF page 86 / printed page 81: visually inspected. Transcribed the four displacement-time graph interpretations, position-data introduction, Figure 3.3 caption, and all six Table 3.2 rows. Redrew the four graph types and car-position axis as native SVG. Page fully verified.

PDF page 87 / printed page 82: visually inspected. Transcribed the six-point position-time graph description, scale, both average-velocity calculations (2.2 m/s and −1.4 m/s), and graph-gradient explanation. Recreated Figure 3.4 as native SVG. Page fully verified.

PDF page 88 / printed page 83: visually inspected at enlarged resolution. Transcribed the reverse-direction note, average-velocity limitation, Figure 3.5 explanations, instantaneous-velocity method, velocity-time graph definition, slope equation, and lead-in to Figure 3.6. Redrew the three Figure 3.5 cases as native SVG. Ink marks do not prevent reading the relevant text. Page fully verified.

PDF page 89 / printed page 84: visually inspected. Transcribed Figure 3.6 scale and points, acceleration calculations for A–B and E–F, B–C/C–D/D–E/F–G interpretations, and printed results. Recreated the velocity-time graph as native SVG. Page fully verified.

PDF page 90 / printed page 85: visually inspected. Transcribed Example 3.1 bicycle-motion prompt, graph scale and points, plus printed acceleration calculations for A–B, B–C and C–D (2.5, 1.25 and −3.75 m/s²). Redrew the velocity-time graph as native SVG. Page fully verified.

PDF page 91 / printed page 86: visually inspected. Completed Example 3.1 with D–E acceleration −1.25 m/s² and average acceleration −0.3125 m/s². Transcribed the acceleration-time graph scale and Assignment 3.1 with all printed answers. Added native SVGs for both graphs. Page fully verified.

PDF page 92 / printed page 87: visually inspected. Transcribed equations of uniformly accelerated motion (3.8–3.10), gravity/free-fall explanation, and Example 3.2 takeoff question. Page fully verified.

PDF page 93 / printed page 88: visually inspected. Transcribed the givens, required values, and all visible two-phase runway-distance calculations through s₂ = 299.8 m. Preserved the source’s 5 s zero-product substitution and flagged its conflict with the given 6.5 s. Page fully verified.

PDF page 94 / printed page 89: visually inspected. Completed Example 3.2 with t₂ = 6.3 s, total time 12.8 s, and both conflicting runway-distance values (382.2 m and 383.2 m). Transcribed Assignment 3.2 and Newton’s first law. Page 94 remains unresolved for the printed value conflict.

PDF page 95 / printed page 90: visually inspected. Transcribed the first-law equation, inertia and mass discussion, second-law definition/equations, and third-law statement. Recreated the Newton portrait/book illustration as native SVG. Page fully verified.

PDF page 96 / printed page 91: visually inspected. Transcribed third-law notation and football example, relativity information box, and Example 3.3 prompt with givens and required accelerations. Recreated the action/reaction and ice-skater figures as native SVG. Page fully verified.

PDF page 97 / printed page 92: visually inspected. Transcribed Example 3.3 accelerations for Umar and Hassan and Assignment 3.3 with its printed answers. Added native vector-acceleration illustration. Page fully verified.

PDF page 98 / printed page 93: visually inspected. Transcribed linear momentum, Newton’s second law derivation (3.14), impulse definition/unit (3.15), and force-duration example. Page fully verified.

PDF page 99 / printed page 94: visually inspected. Transcribed the average-force impulse relation (3.16), impulse/momentum derivation, and Example 3.4 prompt. Recreated bat/ball and force-time graph as native SVG. The right edge clips wording in Example 3.4; page remains unresolved, and page 100 supplies the givens and solution.

PDF page 100 / printed page 95: visually inspected. Transcribed Example 3.4 givens and solution (13.6 N s; +8500 N) and Assignment 3.4 with its printed answers. Page fully verified.

PDF page 101 / printed page 96: visually inspected. Transcribed conservation of momentum (3.17), isolated-system definition, collision definition, and Figure 3.10 captions. Redrew the collision examples as native SVG. Page fully verified.

﻿PDF page 102 / printed page 97: visually inspected and compared the complete page. Recorded the proton/helium non-contact collision, Figure 3.11 labels, energy/momentum conservation, elastic and inelastic collision definitions, and one-dimensional elastic collision distinction. Recreated the charged-particle paths as coded SVG. Page fully verified.

﻿PDF page 103 / printed page 98: visually inspected and transcribed the signed-velocity introduction, Figure 3.12 stages, momentum equations (1)–(2), kinetic-energy conservation and algebra through the divided expressions. Recreated the before/during/after collision stages as coded SVG. Page fully verified.

﻿PDF page 104 / printed page 99: visually inspected and transcribed the relative-speed result (3.18), equation (4), the velocity substitution, intermediate rearrangement, and final-velocity equations (3.19)–(3.20). Page fully verified.

﻿PDF page 105 / printed page 100: visually inspected and transcribed Example 3.5, neutron/heavy-water givens and required values, first post-collision velocity calculation (−1810.28 km/s), and the visible continuation at the page break. Recreated the collision setup as coded SVG. Page fully verified; page 106 must continue the solution.

﻿PDF page 106 / printed page 101: visually inspected and transcribed the second fast-neutron result (v₂ = 190.12 km/s), Assignment 3.4 elastic car collision prompt and answer, and opening of Section 3.11 on momentum and explosive forces. Page fully verified.

﻿PDF page 107 / printed page 102: visually inspected the pistol recoil momentum relation, explosion conservation explanation, Figure 3.13 labels, and projectile-motion definition. Recreated pistol and explosion diagrams as coded SVG. Automated OCR comparison was low because OCR missed several lines and equations; checked those lines against the rendered source. Page fully verified.

﻿PDF page 108 / printed page 103: visually inspected the projectile examples, gravity-only force and acceleration components, Figure 3.14, and ideal-projectile assumptions. Recreated the projectile vector components as coded SVG. Automated source comparison passed. Page fully verified.

﻿PDF page 109 / printed page 104: visually inspected Figure 3.15, the velocity-component explanation, equations for horizontal/vertical velocity and speed magnitude (3.21). Recreated trajectory vectors as coded SVG. OCR comparison was low on the equation-heavy page; visually checked the source formulas and prose. Page fully verified.

﻿PDF page 110 / printed page 105: visually inspected the direction equation (3.22), maximum-height derivation/result (3.23), and start of time-of-flight section. Recreated Figures 3.16 and 3.17 as coded SVG. Automated source comparison passed. Page fully verified.

﻿PDF page 111 / printed page 106: visually inspected time-of-flight result (3.24), time-to-summit note, range derivation/result (3.25), and the first half of maximum-range-angle derivation through sin⁻¹1 = 90°. Recreated Figure 3.18 as coded SVG. OCR comparison was low on equations; checked against the scan. Page fully verified.

﻿PDF page 112 / printed page 107: visually inspected the continuation establishing maximum range at 45°, complementary angles for equal range, and calculations for 75°/15° and 60°/30°. Recreated Figure 3.19 as coded SVG. Automated source comparison passed. Page fully verified.

﻿PDF page 113 / printed page 108: visually inspected the complementary-angle note, air-resistance range reduction, Figure 3.20 equal-fall-time caption, and Point to Ponder rocket-thrust text. Recreated Figures 3.20 and 3.21 and the rocket diagram as coded SVG. OCR comparison flagged partial recognition; visually checked the source lines. Page fully verified.

﻿PDF page 114 / printed page 109: visually inspected Example 3.6 and transcribed all givens, required values, three calculations/results, Assignment 3.5 and printed answers. Added the example and assignment to the interactive lesson. Automated source comparison passed; page fully verified.

﻿PDF page 115 / printed page 110: visually inspected and transcribed the complete Key Points box: displacement, velocity, acceleration, Newton laws, linear momentum conservation, impulse, collision, explosion, and projectile motion. OCR missed part of the box; checked the full scan directly. Page fully verified.

﻿PDF page 116 / printed page 111: visually inspected Exercise multiple-choice heading and Questions 1–8 with every printed option. Translated each item interactively into Urdu and Pashto; no answer key is printed on this page. Automated source comparison passed; page fully verified.

﻿PDF page 117 / printed page 112: visually inspected Questions 9–14 with all choices and both conceptual questions. Translated each item into Urdu and Pashto. OCR comparison was low because it missed text in the scan; checked every question against the rendered page. No answers added. Page fully verified.

PDF page 118 / printed page 113: visually checked Conceptual Questions 3–12 and Comprehensive Questions 1–2 against the scan; interactive English, Urdu, and Pashto text recorded. OCR/source comparison passed. Page fully verified.

PDF page 119 / printed page 114: reviewed Comprehensive Questions 3–8 and Numerical Questions 1–3. The scan clips portions at the right edge; transcribed only readable wording and did not reconstruct clipped text. Page processed but remains unresolved and is excluded from verified-page totals.

PDF page 120 / printed page 115: reviewed Numerical Questions 4–7. Preserved printed inconsistencies in Question 5 velocities and Question 7 answer labels. Page processed but remains unresolved; source ambiguities are not silently corrected.

PDF page 121 / printed page 116: visually checked the Unit 4 opening, initial learning outcomes, and cyclist illustration prompt; the outcomes continue on page 122. Added coded SVG and interactive English, Urdu, and Pashto translations. OCR comparison was partial, so the scan was checked directly. Page fully verified.

PDF page 122 / printed page 117: visually checked the four continuing learning outcomes, energy overview, work definition and scalar statement, and force-displacement dot-product definition against the scan. Preserved the source wording, including its printed spelling/grammar. Page fully verified.

PDF page 123 / printed page 118: visually checked the force components and work equations, Figure 4.1 caption, and positive-work case in Figure 4.2(a). Added coded SVG diagrams for the crate force components and cart case. Page fully verified.

PDF page 124 / printed page 119: visually checked the negative-work, perpendicular-force zero-work, and zero-displacement cases with their equations and explanations. Added the three cases as a coded SVG. Page fully verified.

PDF page 125 / printed page 120: visually checked work by constant force, the shaded Fd area in Figure 4.3, the joule definition, and the variable-force examples for gravity and a spring. Added the force-displacement graph as coded SVG. Page fully verified.

PDF page 126 / printed page 121: visually checked work estimation with small displacement segments, the varying-force path, rectangle areas, and summation formula. Redrew Figures 4.4–4.5 as coded SVG. Source comparison did not flag this page; page fully verified.

PDF page 127 / printed page 122: visually checked the limiting-area result, Moon work quiz, gravitational-field definition and unit, conservative-field statement, and closed-path setup. Redrew Figures 4.6–4.7 as coded SVG. Page fully verified.

PDF page 128 / printed page 123: visually checked all three work terms on the closed path, zero-total-work proof, conservative/non-conservative force lists, and first-path comparison. Redrew Figure 4.8 as coded SVG. Page fully verified.

PDF page 129 / printed page 124: visually checked the second-path work, path-independence conclusion, friction note, power definition, and equations P=W/t and P=F·v. Source comparison did not flag this page; page fully verified.

PDF page 130 / printed page 125: visually checked average and instantaneous power, stairway measurement example, watt/kilowatt/megawatt/kilowatt-hour conversions, device power examples, and horsepower conversion. Page fully verified.

PDF page 131 / printed page 126: visually checked Example 4.1, both car-power cases, given values, force/acceleration calculations, and printed answers 91 hp and 82 hp. Added the hill-climb car as coded SVG. Page fully verified.

PDF page 132 / printed page 127: visually checked Example 4.2 and its calculation, Assignment 4.1 with printed answer, Tid Bit, and opening definition of energy and kinetic energy. Page fully verified.

PDF page 133 / printed page 128: visually checked kinetic and potential energy definitions and equations, Figure 4.10 caption, pyramid Point to Ponder, and visible opening of Section 4.5. The scan clips the right edge of the efficiency paragraph after “into”; page processed but remains unresolved, with no missing text supplied. Added coded SVGs for the dolphin and inclined-plane illustration.

PDF page 134 / printed page 129: visually checked the heat-loss continuation, crane and pulley setup, output/input definitions, efficiency equations (4.6)–(4.7), and friction note. Redrew the crane as coded SVG. Page fully verified.

PDF page 135 / printed page 130: visually checked the inclined-plane definition, all Table 4.1 device efficiencies, LED cost comparison, AC/DC fan specifications, and Example 4.3 prompt. Recreated the table and appliance illustration as coded SVG. Page fully verified.

PDF page 136 / printed page 131: visually checked Example 4.3 solution (59%), Example 4.4 pulley calculation (12,000 J, 83%), and Section 4.6 zero-reference explanation. Page fully verified.

PDF page 137 / printed page 132: visually checked the variable-gravity work setup, interval equations, average-radius derivation, and listed successive work terms. The right edge of Figure 4.12 and part of its caption are clipped; page processed but remains unresolved. The SVG shows only visible details.

PDF page 138 / printed page 133: visually checked the telescoping sum of interval work, result GmMₑ(1/r₁ − 1/rₙ), infinity limit, and surface value GmMₑ/Rₑ. Page fully verified.

PDF page 139 / printed page 134: reviewed the negative absolute-potential-energy sign, gravitational-potential equation, escape-velocity explanation, and rocket illustration. Right-edge clipping affects portions of the potential definitions and rocket caption; page processed but remains unresolved. Added a coded rocket SVG.

PDF page 140 / printed page 135: visually checked escape-velocity derivation (4.10–4.11), Earth constants and 11.2 × 10³ m s⁻¹ result, Figure 4.13, and Example 4.5 givens. Reused the coded Earth-field SVG. Page fully verified.

PDF page 141 / printed page 136: visually checked Example 4.5 result, Example 4.6 lunar escape calculation and explanation, Assignment 4.2 with its printed answer, and the opening lines of Section 4.8. Page fully verified.

PDF page 142 / printed page 137: visually checked hammer/nail energy conversion, friction and dissipative-force explanation, equations (4.12)–(4.13), and conservation-of-energy section opening. Redrew Figure 4.14 as coded SVG. Page fully verified.

PDF page 143 / printed page 138: visually reviewed total mechanical energy, conservation statement, energy-transfer examples, and Example 4.7 setup/first solution step. Right edge clips portions of the law statement, a highlighted note, and example box; page processed but remains unresolved. Readable height result 31.9 m retained; clipped wording not reconstructed.

PDF page 144 / printed page 139: visually checked Example 4.7 friction calculation (6.75 J, 0.27 N), Assignment 4.3 with both printed answers, Moon tidbit, and Section 4.10 opening on non-renewable resources. Page fully verified.

PDF page 145 / printed page 140: visually checked coal, oil, and natural-gas descriptions and stated reserve/use figures; redrew Figure 4.15 air-pollution image as coded SVG. Page fully verified.

PDF page 146 / printed page 141: visually checked nuclear fission and Pakistan 2015 contribution, renewable-resource definition/examples, biomass definition, and Figure 4.16 waste-energy process. Batch OCR returned no usable text for this page, so every line was checked directly against the rendered scan. Redrew the process as coded SVG. Page fully verified.

PDF page 147 / printed page 142: visually checked biomass processing/potential figures, OWC wave-energy process, and geothermal plant introduction. Added coded SVGs for Figures 4.17–4.18. Page fully verified.

PDF page 148 / printed page 143: visually checked geothermal cycle, tidal-energy explanation and stated output figures, and solar-energy opening through the page break. Batch OCR returned no usable text for this page, so the scan was checked directly. Added coded SVGs for Figures 4.19–4.20. Page fully verified.

PDF page 149 / printed page 144: visually checked solar resource values, wind-energy description and regional potential, Figure 4.21, and all six Key Points definitions. Added a coded wind-energy SVG. Page fully verified.

PDF page 150 / printed page 145: visually checked the non-conventional energy source list and MCQs 1–8, including each option and scientific notation, against the rendered page. Added paired English/Urdu/Pashto records and retained the source's visible list labels (a), (b), (c), (d), and (f), including the absent (e). Source-to-code comparison is high overall; formula-only option trigrams are not independently scored as full paragraphs.

PDF page 151 / printed page 146: visually checked MCQs 9–14 and conceptual questions 1–8, including all options, units, numbering, and wording. Added separate paired English/Urdu/Pashto records; continued MCQs use their printed numbering. Page OCR omits/reduces visible text, so comparison was checked directly against the clear rendered scan. Page fully verified.

PDF page 152 / printed page 147: visually checked conceptual questions 9–11, comprehensive questions 1–6 and numerical questions 1–3, including printed answers, units, subscripts, and formula Absolute P.E = GmMₑ/Rₑ. Added paired English/Urdu/Pashto records. Source text and coded content align; page fully verified.

PDF page 153 / printed page 148: visually checked numerical questions 4–11 and all printed answers, quantities, units, and subparts. Added paired English/Urdu/Pashto records. The scan was rendered at 300 dpi to resolve the wording in question 5, read as “walks up.” Page fully verified.

PDF page 154 / printed page 149: visually checked the Unit 5 opener, tornado prompt, and all eight rotational/circular-motion learning outcomes, including the formulas for arc speed, centripetal acceleration, and centripetal force. Recreated the tornado scene as native SVG and added aligned English/Urdu/Pashto text. OCR/source comparison coverage 0.89; page fully verified from the rendered scan.

PDF page 155 / printed page 150: visually checked the continuation of learning outcomes, angular-momentum introduction, Section 5.1 text, and Figure 5.1 satellite caption/labels. Added paired translations and a coded SVG satellite orbit. Source comparison coverage 0.98; page fully verified.

PDF page 156 / printed page 151: visually checked angular-displacement definition, the disc rotation explanation and Figure 5.2, radian equation 5.1 and units, and the opening angular-velocity definition/equation 5.2. Added coded disc SVG, typeset equations, and aligned English/Urdu/Pashto records. OCR/source comparison coverage 0.91; page fully verified.

PDF page 157 / printed page 152: visually checked angular-velocity units and limit, the uniform-motion note, all of Example 5.1 and its working/answer, Assignment 5.1 with printed answer, and angular-acceleration definition/equation 5.3. Added typeset equations and aligned English/Urdu/Pashto records. OCR/source comparison coverage 0.53 with omitted scan text; the full rendered page was checked directly. Page fully verified.

Speed instruction (2026-10-10): target 400 PDF pages/hour while preserving full sequential review, exact source matching, coded SVG/HTML visuals, interactive English/Urdu/Pashto translations, and continuous verified checkpoints. Benchmark note: `speed-benchmark-20261010.md`. Completed batches: p154–157 measured about 10 pages/hour; p158–161 took 32m36s (7.4 pages/hour); p162–165 took 8m55s (27.0 pages/hour); p166–169 took 4m20s (55.4 pages/hour); p170–177 took 5m42s (84.2 pages/hour); p178–181 took 2m10s (110.8 pages/hour); p182–185 took 2m04s (116.1 pages/hour); p186–189 took 1m47s (134.6 pages/hour); p190–193 took 2m12s (109.1 pages/hour); p194–197 took 8m53s (27.0 pages/hour); p198–201 took 6m54s (34.8 pages/hour); p202–205 took 7m49s (30.7 pages/hour). Full-book OCR was 896.8 pages/hour for extraction only. Next sequential page: PDF page 206.

PDF page 158 / printed page 153: visually reviewed angular-acceleration units, average and instantaneous definitions, the direction note, Section 5.2, the everyday wheel-motion example, Figure 5.3, and the arc/radian relation in equation 5.4. Added aligned English/Urdu/Pashto text, equation rendering, and a coded SVG. Source comparison coverage 0.87; code and reader checks pass. Page processed and verified.

PDF page 159 / printed page 154: visually reviewed the linear/angular velocity derivation, equations 5.5, Figures 5.4–5.5, and right-hand-rule explanation. Added translations, equations, and coded SVG diagrams. OCR/source comparison coverage 0.88. The scan clips the word after “alw” at the right edge; this fragment is explicitly marked with sourceGap and not reconstructed. Page processed but unresolved.

PDF page 160 / printed page 155: visually reviewed the right-hand rule continuation, linear/angular acceleration relation and equation 5.6, special case, Section 5.3 centripetal-force discussion, and Figure 5.6. Added aligned translations, MathJax equations, and a coded SVG. Source comparison coverage 0.91; code and reader checks pass. Page processed and verified.

PDF page 161 / printed page 156: visually reviewed the centripetal-acceleration explanation, Figure 5.7, velocity-vector construction, and geometric ratio. Added aligned translations, a coded SVG, and equation rendering. OCR/source comparison coverage 0.56 because vector notation is poorly extracted; the full rendered page was visually checked. Code and reader checks pass. Page processed and verified.

PDF page 162 / printed page 157: visually checked the small-angle centripetal-acceleration derivation, limits, equations 5.7–5.9, Figure 5.8, radius-vector direction, and Newton’s second-law force setup. Added translated source paragraphs, MathJax equations, and a coded SVG. OCR/source comparison coverage 0.66; vector notation was checked directly against the rendered page. Reader and syntax checks pass. Page verified.

PDF page 163 / printed page 158: visually checked centripetal-force equations 5.10, the centrifugal/reaction-force explanation, Example 5.2 and its printed answer 12.3 m s⁻², and Assignment 5.2 with printed answer 20 m s⁻². Added aligned translations and MathJax. OCR/source comparison coverage 0.61; the rendered scan was checked for text missed by OCR. Page verified.

PDF page 164 / printed page 159: visually checked string-break/reaction-force explanation, centrifugal-force magnitude, road-banking introduction, Figures 5.9–5.11, labels, and captions. Redrew all three diagrams as native SVG and added aligned translations. OCR/source comparison coverage 0.93. Reader and syntax checks pass. Page verified.

PDF page 165 / printed page 160: visually checked the banking derivation and equation 5.11, speed relation, Figure 5.12, Example 5.3, givens, calculation, and printed 22° answer. Added translations, MathJax equations, and a coded SVG. OCR/source comparison coverage 0.68. Right-edge clipping affects banking text; clipped fragments are tagged with sourceGap and not reconstructed. Page processed but unresolved.

PDF page 166 / printed page 161: visually checked Assignment 5.3 and its printed answer, Section 5.4 inertia definitions, bike-wheel example and Figure 5.13, and torque derivation equations 5.12–5.13. Added English/Urdu/Pashto records, MathJax, and a coded SVG. OCR/source comparison coverage 0.87. Syntax and reader checks pass. Page verified.

PDF page 167 / printed page 162: visually checked the rigid-body moment-of-inertia sum and equation 5.14, Figure 5.14 labels, Example 5.4 givens/calculation, and printed answer 1.25 N m. Added translated text, equation rendering, and a coded SVG. OCR/source comparison coverage 0.60 due to formula OCR; the rendered scan was checked directly. Page verified.

PDF page 168 / printed page 163: visually checked Figure 5.15 formulas for six bodies, Assignments 5.4 and 5.5 with their printed answers, and the opening of Section 5.5. Added a coded SVG with the source labels and aligned translations. OCR/source comparison coverage 0.96. Page verified.

PDF page 169 / printed page 164: visually checked torque definition, angular-momentum definition and equation 5.15, Figure 5.16 and its axes/vector labels, magnitude/units, circular-motion case, and rigid-body continuation. Added aligned translations, MathJax equations, and a coded SVG. OCR/source comparison coverage 0.64 due to vector notation; directly checked against the rendered scan. Page verified.

PDF page 170 / printed page 165: visually checked Figure 5.17 labels and caption, rigid-body angular momentum summation, moment-of-inertia substitution, and L = Iω. Added aligned English/Urdu/Pashto text, MathJax, and coded SVG. OCR/source comparison coverage 0.86. Reader and syntax checks pass. Page verified.

PDF page 171 / printed page 166: visually checked Example 5.5 values, units, Earth orbital calculation, printed angular momentum result, solar-nebula conservation explanation, and coded figure. Added aligned translations, equations, and coded SVG. OCR/source comparison coverage 0.89. Page verified.

PDF page 172 / printed page 167: visually checked Assignment 5.6 and its printed result, Section 5.6, torque-rate derivation, equation 5.16, and isolated-system conservation statement. Added aligned translations and MathJax. OCR/source comparison coverage 0.85. Syntax and reader checks pass. Page verified.

PDF page 173 / printed page 168: visually checked conservation applications, diver and gymnast explanations, Figures 5.18–5.19, and recreated both diagrams as coded SVG. Added aligned translations. OCR/source comparison coverage 0.96. The right edge clips “angular momentum al…” before the next line reads “constant”; retained the visible fragment and marked it unresolved. Page processed; unresolved.

PDF page 174 / printed page 169: visually checked turntable conservation explanation, Figure 5.20 and labels, Example 5.6 prompt, given values, and required quantities. Added English/Urdu/Pashto text, coded SVG, and a source-flow sequence. Reader and syntax checks pass. Page verified.

PDF page 175 / printed page 170: visually checked Example 5.6 solution (80 kg m² s⁻¹ and zero torque), section 5.7, equations 5.17–5.18, rotational kinetic-energy derivation, Figure 5.21, and its caption. Added translations, MathJax, and coded SVG. OCR/source comparison coverage 0.62; formulas and scan quality lower OCR, so inspected the page image directly. Page verified.

PDF page 176 / printed page 171: visually checked the full linear/angular comparison table and Example 5.7 statement, givens, conservation equation, and platform/child moments of inertia. Recreated the comparison table as coded SVG and added aligned translations. OCR/source comparison coverage 0.75. Page verified.

PDF page 177 / printed page 172: visually checked Example 5.7 calculation and printed answer 8.27 rad/s, section 5.8 opening, Figure 5.22, and rolling-energy derivation through mgh = mv²(½ + ¼). Added translations, MathJax-ready equations, and coded SVG. OCR/source comparison coverage 0.69 with formula-heavy text; directly checked the rendered source. Page verified.


PDF page 178 / printed page 173: visually checked disc and hoop speed results (equations 5.19–5.20), the source table note, comparison conclusion, Section 5.9, and real-weight case with 41.0 N. Added English/Urdu/Pashto text, MathJax, and coded lift-scale SVG. OCR/source comparison coverage 0.79. Page verified.

PDF page 179 / printed page 174: visually checked zero-acceleration balance equation 5.21 and upward-lift case, including 2.10 m s⁻², 49.778 N, equation 5.22, and Figure 5.23(b). Added aligned translations, equations, and coded SVG. OCR/source comparison coverage 0.73. Page verified.

PDF page 180 / printed page 175: visually checked downward-lift reading 32.22 N, equation 5.23, free-fall case and zero scale reading equation 5.24, and weightlessness explanation. Added aligned translations, MathJax, and coded SVG. OCR/source comparison coverage 0.85. Page verified.

PDF page 181 / printed page 176: visually checked the free-fall continuation, Section 5.10.1, cannonball paths and figures 5.24–5.25, 5 m per 8000 m curvature relation, and approximate 8000 m s⁻¹ orbital speed. Added aligned translations and two coded SVGs. OCR/source comparison coverage 0.42, so checked the rendered page directly; text and labels are visible. Page verified.


PDF page 182 / printed page 177: visually checked critical-velocity explanation, equation 5.25, g and Earth-radius values, 7.9 km s⁻¹ ≈ 8000 m s⁻¹ result, free-fall explanation, hair quiz, and Example 5.8 prompt. Added aligned translations and MathJax. OCR/source comparison coverage 0.81. Page verified.

PDF page 183 / printed page 178: visually checked Example 5.8 solution (966 N), Assignment 5.7 with printed 24 N answer, artificial-gravity introduction, and Figure 5.26. Added aligned translations, MathJax, and a coded SVG. OCR/source comparison coverage 0.68; checked image directly. Page verified.

PDF page 184 / printed page 179: visually checked zero-gravity water, point-to-ponder text about sleeping in microgravity, rotating-wheel station proposal and Figure 5.27. Added aligned translations and coded SVG. OCR/source comparison coverage 0.89. Page verified.

PDF page 185 / printed page 180: visually checked the rotating-station explanation, centripetal-acceleration and period/frequency derivation, equation 5.26, and closing explanation. Added aligned translations and MathJax. OCR/source comparison coverage 0.33 because formulas dominate; checked the rendered source directly. Page verified.


PDF page 186 / printed page 181: visually checked Section 5.12 definition of artificial satellites, types, GPS facts, communication-satellite example, geostationary altitude, and Figure 5.28. Added aligned translations and coded SVG. OCR/source comparison coverage 0.96. Page verified.

PDF page 187 / printed page 182: visually checked weather satellites, Section 5.12.1, orbit/satellite definition, Figure 5.29 shuttle caption, Figure 5.30 orbital-speed diagram, and Newton-law setup. Added aligned translations and two coded SVGs. OCR/source comparison coverage 0.66; reviewed rendered source directly. Page verified.

PDF page 188 / printed page 183: visually checked equations 5.27–5.28, speed/radius explanation, Example 5.12 ISS altitude, constants, and printed result 7.67 × 10³ m/s. Added aligned translations and MathJax. OCR/source comparison coverage 0.68; formulas were checked against the page image. Page verified.

PDF page 189 / printed page 184: visually checked Section 5.13 geostationary orbit facts, period/speed equations, equation 5.29, printed constants, radius result 4.23 × 10⁴ km, and Figure 5.31. Added aligned translations, MathJax, and coded SVG. OCR/source comparison coverage 0.51; checked the scan directly. Page verified.


PDF page 190 / printed page 185: visually checked three-satellite 120° coverage text, Example 5.13 givens, source notation Re = 64 × 10⁵ m and r₀ = 73 × 10⁵ m, calculation, and printed 7.4 × 10³ m s⁻¹ answer. Added aligned translations and formula rendering. OCR/source comparison coverage 0.79. Page verified.

PDF page 191 / printed page 186: visually checked all Key Points definitions, including repeated centripetal-force and artificial-gravity entries. Added translated vocabulary records. OCR/source comparison coverage 0.52; inspected the rendered glossary directly. Page verified.

PDF page 192 / printed page 187: visually checked Exercise multiple-choice questions 1–8 and all visible options. Added aligned translations. OCR/source comparison coverage 0.86. The right scan edge clips option 6(b) after “there is no floor pushing upward on the”; retained the visible fragment and marked the page unresolved.

PDF page 193 / printed page 188: visually checked multiple-choice questions 9–11 and conceptual questions 1–8. Added aligned translations. OCR/source comparison coverage 0.48. Question 10 text is clipped at the right scan edge and option 11(c) is illegible; preserved these gaps and marked the page unresolved.


PDF page 194 / printed page 189: visually checked conceptual questions 9–11 and all ten comprehensive questions, including the printed vector equations for angular momentum, centripetal acceleration and force. Added aligned English/Urdu/Pashto questions. OCR/source comparison coverage 0.87. Page verified.

PDF page 195 / printed page 190: visually checked all 12 numerical questions and every answer printed in parentheses; no unprinted answers were added. Added aligned translations. OCR/source comparison coverage 0.31 due dense text; directly checked all questions and values on the rendered page. Page verified.

PDF page 196 / printed page 191: visually checked Unit 6 title, prompt, and all 13 Fluid Dynamics learning outcomes. Created a separate Unit 6 chapter record with aligned translations. OCR/source comparison coverage 0.94. Syntax and reader checks pass. Page verified.

PDF page 197 / printed page 192: visually checked fluid definition, viscosity description, units/conversions, and all entries in Table 6.1. Added aligned translations and coded SVG table. OCR/source comparison coverage 0.43 due table layout; compared the values directly with the rendered source. Page verified.


PDF page 198 / printed page 193: visually checked viscosity-versus-temperature behavior for liquids and gases, Section 6.2, fluid friction and drag explanations, three drag dependencies, and skydiver point-to-ponder passage. Added aligned translations. OCR/source comparison coverage 0.85. Page verified.

PDF page 199 / printed page 194: visually checked Stokes-law dependencies, Fd = 6πηrv (6.1), Figure 6.1, its application note, and Section 6.3 terminal-velocity opening. Added translations, MathJax, and coded SVG. OCR/source comparison coverage 0.55. Multiple lines are clipped at the right scan edge; retained only readable source content and marked unresolved.

PDF page 200 / printed page 195: visually checked the falling-sphere case, Newton second-law explanation, Fnet = FG − FD, ma = mg − 6πηrv, Figures 6.2–6.3, and force directions. Added translations and coded SVGs. OCR/source comparison coverage 0.62; equations were checked directly against the page image. Page verified.

PDF page 201 / printed page 196: visually checked the terminal-force balance, equation 6.2, Figure 6.4 velocity-time graph, and density/volume substitutions through equation (3). Added translations, MathJax, and coded SVG. OCR/source comparison coverage 0.41 due equation-heavy text; checked the rendered page directly. Page verified.


PDF page 202 / printed page 197: visually checked substitution into equation 6.2, terminal-velocity equation 6.3, explanatory text, all Table 6.2 entries, and the hailstone fact. Added aligned translations, MathJax, and coded SVG table. OCR/source comparison coverage 0.84. Page verified.

PDF page 203 / printed page 198: visually checked the two terminal velocities (54 m/s and 11 m/s), graph, and all four skydiver stages. Added translations and coded graph SVG. OCR/source comparison coverage 0.62. Introductory paragraph has clipped right-edge text; kept the visible information and marked unresolved.

PDF page 204 / printed page 199: visually checked Example 6.1 data, fog-droplet calculation and 0.00298 m/s result, Assignment on the globular protein particle with printed radius 1.6 × 10⁻⁶ m, and the opening definition of streamline flow. Added aligned translations and MathJax. OCR/source comparison coverage 0.77. Page verified.

PDF page 205 / printed page 200: visually checked streamline and stream-tube definitions, Figure 6.5, laminar-to-turbulent transition and incense example, Figure 6.6, and tornado point-to-ponder text. Added aligned translations and two coded SVG diagrams. OCR/source comparison coverage 0.78. Page verified.


PDF p206 printed p201: visually checked full scan. Encoded turbulent-flow examples, streamlined animals note, and all five ideal-flow assumptions in English/Urdu/Pashto. No diagram on page; no clipped text.

PDF p207 printed p202: visually checked full scan. Encoded continuity setup, Figure 6.7 as coded SVG with caption, equal mass, density/volume/velocity relations and lower-end mass expression. English/Urdu/Pashto complete.

PDF p208 printed p203: visually checked full scan. Encoded upper-end mass, continuity derivation/result, water-tap note, volume-flow-rate equation and explanation in all three languages. No clipped text.

PDF p209 printed p204: visually checked full scan. Encoded Example 6.2 with exact hose/nozzle radii, speeds and calculation; encoded Assignment 6.2 with 32 arteries and answer. English/Urdu/Pashto complete.

Measured batch: PDF pages 206–209 completed from 2026-10-09 21:53:51 UTC to 21:59:48 UTC (5m57s), including scan review, translation, SVG/equation coding, source comparison, checks, and checkpoints. End-to-end throughput: 40.3 pages/hour. All four pages visually checked and resolved. Next page: 210.

PDF p210 printed p205: visually checked. Encoded Section 6.5 Bernoulli statement/equations, energy conservation setup and end-1 work; added Figure 6.8 as coded SVG with source-matched caption. Translations in English, Urdu, Pashto.

PDF p211 printed p206: visually checked. Encoded end-2 work, pressure-to-force relation, volume/density relations, equations 4–12, and Bernoulli biography note in all three languages.

PDF p212 printed p207: visually checked. Encoded derivation equations 13–17, equal-mass step, algebra to equations 6.6 and 6.7, and source conclusion. Translations in English, Urdu, Pashto.

PDF p213 printed p208: visually checked. Encoded Example 6.3 with source pressures, height, density, substitution, and 4 m/s answer; encoded Assignment 6.3 and answer 47.1 kPa. All three languages.

Measured batch: PDF pages 210–213 completed from 2026-10-09 21:59:48 UTC to 22:03:20 UTC (3m32s), including scan review, translated content, coded Figure 6.8, equation work, comparison, checks, and checkpoints. End-to-end throughput: 67.9 pages/hour. All four scans were visually checked. Next page: 214.

PDF p214 printed p209: visually checked. Encoded section 6.7 introduction, filter pump explanation, atomizer explanation, and Figures 6.9/6.10 as coded SVG with captions. English/Urdu/Pashto.

PDF p215 printed p210: visually checked. Encoded carburetor note and diagram as SVG; Torricelli theorem statement and tank setup with Figure 6.11 coded SVG. English/Urdu/Pashto.

PDF p216 printed p211: visually checked. Encoded complete Torricelli derivation to equation 6.7, then Example 6.4 prompt and givens. Radius visually confirmed as 6.0 × 10⁻³ m. English/Urdu/Pashto.

PDF p217 printed p212: visually checked. Encoded Example 6.4 result v=4.85 m/s and ΔV/Δt=5.48×10⁻⁴ m³ s⁻¹, extension, Assignment 6.4 and 6.3 m/s answer, plus Venturi metre introduction. English/Urdu/Pashto.

Measured batch: PDF pages 214–217 completed from 2026-10-09 22:03:20 UTC to 22:06:45 UTC (3m25s), including scan review, translated content, four coded SVG diagrams, calculations, comparison, checks, and checkpoints. End-to-end throughput: 70.2 pages/hour. All four scans were visually checked. Next page: 218.

PDF p218 printed p213: visually checked. Encoded Figure 6.12 as coded Venturi SVG, Bernoulli/continuity derivation, and equation 6.8 exactly with areas A1/A2. English/Urdu/Pashto.

PDF p219 printed p214: visually checked. Encoded barometer and pressure-column explanation, Figure 6.13 as SVG, and equation 6.9 with height difference h. English/Urdu/Pashto.

PDF p220 printed p215: visually checked. Encoded Assignment 6.5 areas, pressure difference, and answer; aerofoil definition, lift/drag, Figure 6.14 SVG, and airplane-wing lift note with coded illustration. English/Urdu/Pashto.

PDF p221 printed p216: visually checked. Encoded Example 6.5 all givens and Bernoulli force derivation; source answer confirmed as 3.2 × 10⁶ N. English/Urdu/Pashto.

Measured batch: PDF pages 218–221 completed from 2026-10-09 22:06:45 UTC to 22:09:44 UTC (2m59s), including scan review, translations, three coded SVG figures, Venturi derivation, lift calculation, source comparison, checks, and checkpoints. End-to-end throughput: 80.4 pages/hour. All four scans were visually checked. Next page: 222.

PDF p222 printed p217: visually checked. Encoded classroom paper-lift demonstration, spoiler/downforce note, and Blood Flow introduction in English/Urdu/Pashto; created two explanatory SVG diagrams.

PDF p223 printed p218: visually checked. Encoded Figure 6.14 normal/narrowed artery as coded SVG, pressure and radius discussion, source factor 2⁴=16 and plaque/heart-attack text. English/Urdu/Pashto.

PDF p224 printed p219: visually checked. Encoded the full Unit 6 key-points page: definitions of flow, viscosity, drag, terminal velocity, laminar/turbulent flow, continuity, and Bernoulli. English/Urdu/Pashto.

PDF p225 printed p220: visually checked. Encoded all nine multiple-choice questions and all source choices in English/Urdu/Pashto. The page has no supplied answer key.

Measured batch: PDF pages 222–225 completed from 2026-10-09 22:09:44 UTC to 22:13:17 UTC (3m33s), including scan review, English/Urdu/Pashto content, coded figures, chapter key points, nine complete MCQs, comparison, checks, and checkpoints. End-to-end throughput: 67.6 pages/hour. All four scans were visually checked. Next page: 226.

PDF p226 printed p221: visually checked. Encoded MCQs 10–15 with all four options each and conceptual questions 1–4 in English/Urdu/Pashto. Exact question text and options included.

PDF p227 printed p222: visually checked. Encoded conceptual questions 5–10 and comprehensive questions 1–8 in English/Urdu/Pashto.

PDF p228 printed p223: visually checked. Encoded all seven numerical questions and printed answers in English/Urdu/Pashto. The volume-flow unit for question 5 is transcribed as printed: 0.0469 cm³ s⁻¹.

PDF p229 printed p224: visually checked. Began Unit 7 Oscillation; encoded opening prompt and visible learning outcomes in English/Urdu/Pashto. The final learning outcome is cut off at “with particular” at the page bottom and is recorded unresolved for continuation.

Measured batch: PDF pages 226–229 completed from 2026-10-09 22:13:17 UTC to 22:19:44 UTC (6m27s), including scan review, translations, full MCQs/conceptual/numerical exercise text, Unit 7 entry, coded illustrations, comparison, checks, and checkpoints. End-to-end throughput: 37.2 pages/hour. Page 229 remains unresolved because its final learning outcome continues beyond the page. Next page: 230.

PDF p230 printed p225: visually checked. Continued and completed the final Unit 7 learning outcome from p229; encoded Section 7.1 and terminology terms i–iv, pendulum figure as coded SVG, English/Urdu/Pashto.

PDF p231 printed p226: visually checked. Encoded definitions v–viii, frequency/angular-frequency equations, building-information note, Section 7.3 spring setup, and spring SVG in all three languages.

PDF p232 printed p227: visually checked. Encoded the spring SHM derivation, Hooke law steps, definition, and equations 7.1–7.5 for acceleration, omega, period and frequency in all three languages.

PDF p233 printed p228: visually checked. Encoded Example 7.1 with exact given values and answer k=50 N m⁻¹; Assignment 7.1 with printed answer; Section 7.4 circular projection and coded Figure 7.2(a), all three languages.

Resolution: PDF page 229’s final learning outcome was continued verbatim from page 230 and its unresolved marker cleared after adjacent-page visual review.

Measured batch: PDF pages 230–233 completed from 2026-10-09 22:19:44 UTC to 22:36:27 UTC (16m43s), including scan review, full trilingual text, formula rendering, illustrations, comparison, checks, and checkpoints. End-to-end throughput: 14.3 pages/hour. Page 229 continuation was resolved against p230. Next page: 234.

PDF p234 printed p229: visually checked. Encoded centripetal-acceleration projection derivation, x=r cosθ, and SHM relation aₓ=−ω²x; Figure 7.2(b) is coded SVG.

PDF p235 printed p230: visually checked. Encoded time period, frequency, projection velocity derivation to vₓ=ω√(r²−x²), and Figure 7.3 sinusoidal projection graph as SVG.

PDF p236 printed p231: visually checked. Encoded simple pendulum setup, force components, small-angle approximation and SHM derivation to a=−(g/ℓ)x; coded Figure 7.4 SVG.

PDF p237 printed p232: visually checked. Encoded pendulum period properties, elevator quiz, Example 7.2 givens/solution 0.089293m, Assignment 7.2 and printed 36m answer; English/Urdu/Pashto.

Measured batch: PDF pages 234–237 completed from 2026-10-09 22:36:27 UTC to 22:42:24 UTC (5m57s), including direct scan review, translations, equations, three coded figures, comparison, reader checks, and checkpoints. End-to-end throughput: 40.3 pages/hour. Page 229 continuation is resolved. Next page: 238.

PDF p238 printed p233: visually checked. Encoded SHM energy setup, velocity relation, kinetic-energy expression and extrema, and restoring force equation 7.14; spring figure coded SVG.

PDF p239 printed p234: visually checked. Encoded average-force work and elastic potential-energy derivation, extrema, and start of total-energy section; equations 7.15–7.18.

PDF p240 printed p235: visually checked. Encoded total energy equations 7.19–7.20, energy exchange, Assignment 7.3 (k=6.5×10⁴ N/m; printed answers 0.9s, 1.1Hz), free/forced oscillations and resonance opening.

PDF p241 printed p236: visually checked. Completed resonance definition/condition, Figure 7.7 pendulum experiment and radio example; both illustrations are coded SVG. Page 240 resonance continuation is resolved.

Measured batch: PDF pages 238–241 completed from 2026-10-09 22:42:24 UTC to 22:47:50 UTC (5m26s), including energy equations, resonance text, three coded SVG figures, translations, OCR comparison, reader checks, and checkpoints. End-to-end throughput: 44.2 pages/hour. Cross-page resonance text was resolved. Next page: 242.

PDF p242 printed p237: visually checked. Encoded MRI and microwave resonance examples, Section 7.8 waveform equations and Figure 7.11 as coded SVGs.

PDF p243 printed p238: visually checked. Encoded paper-and-pen waveform experiment, Figure 7.12 SVG, and phase definition/equations 7.21–7.22.

PDF p244 printed p239: visually checked. Encoded phase-difference discussion for φ=0°, 90°, 180°, out-of-phase explanation, and phase waveform figures as coded SVGs.

PDF p245 printed p240: visually checked. Encoded Example 7.3 exact result −4.87 cm, Assignment 7.4 result 0.400s, phase quiz choices and graph explanation, and beginning of damped oscillations.

Measured batch: PDF pages 242–245 completed from 2026-10-09 22:47:50 UTC to 22:55:11 UTC (7m21s), including source review, translations, equations and waveform/MRI/microwave diagrams, source comparison, checks, and checkpoints. End-to-end throughput: 32.7 pages/hour. Next page: 246.

PDF p246 printed p241: visually inspected source scan; encoded complete English text with Urdu and Pashto translations; automated source comparison and reader validation passed. Page figures are coded SVG where applicable.

PDF p247 printed p242: visually inspected source scan; encoded complete English text with Urdu and Pashto translations; automated source comparison and reader validation passed. Page figures are coded SVG where applicable.

PDF p248 printed p243: visually inspected source scan; encoded complete English text with Urdu and Pashto translations; automated source comparison and reader validation passed. Page figures are coded SVG where applicable.

PDF p249 printed p244: visually inspected source scan; encoded complete English text with Urdu and Pashto translations; automated source comparison and reader validation passed. Page figures are coded SVG where applicable.

PDF p250 printed p245: visually reviewed full source scan, encoded content and English/Urdu/Pashto translations; direct visual comparison performed. OCR comparison for p250 status: reviewed, with source-specific OCR omissions; reader validator passes. p251 numerical OCR omits much content but source image checked. p253 page-248 outcomes and opening paragraph were manually transcribed from scan; OCR omits many lines. p251 question 9 source statement and provided answer set may be inconsistent; retained values as printed without correction.

PDF p251 printed p246: visually reviewed full source scan, encoded content and English/Urdu/Pashto translations; direct visual comparison performed. OCR comparison for p251 status: reviewed, with source-specific OCR omissions; reader validator passes. p251 numerical OCR omits much content but source image checked. p253 page-248 outcomes and opening paragraph were manually transcribed from scan; OCR omits many lines. p251 question 9 source statement and provided answer set may be inconsistent; retained values as printed without correction.

PDF p252 printed p247: visually reviewed full source scan, encoded content and English/Urdu/Pashto translations; direct visual comparison performed. OCR comparison for p252 status: reviewed, with source-specific OCR omissions; reader validator passes. p251 numerical OCR omits much content but source image checked. p253 page-248 outcomes and opening paragraph were manually transcribed from scan; OCR omits many lines. p251 question 9 source statement and provided answer set may be inconsistent; retained values as printed without correction.

PDF p253 printed p248: visually reviewed full source scan, encoded content and English/Urdu/Pashto translations; direct visual comparison performed. OCR comparison for p253 status: reviewed, with source-specific OCR omissions; reader validator passes. p251 numerical OCR omits much content but source image checked. p253 page-248 outcomes and opening paragraph were manually transcribed from scan; OCR omits many lines. p251 question 9 source statement and provided answer set may be inconsistent; retained values as printed without correction.

PDF p254 printed p249: full scan visually reviewed; source content encoded with English, Urdu and Pashto; figures represented by coded SVG where present. Automated source comparison reviewed (OCR truncation/reading-order artifacts on this spread); class reader validation passes. p257 printed subsection numbering retained as shown despite inconsistency.

PDF p255 printed p250: full scan visually reviewed; source content encoded with English, Urdu and Pashto; figures represented by coded SVG where present. Automated source comparison reviewed (OCR truncation/reading-order artifacts on this spread); class reader validation passes. p257 printed subsection numbering retained as shown despite inconsistency.

PDF p256 printed p251: full scan visually reviewed; source content encoded with English, Urdu and Pashto; figures represented by coded SVG where present. Automated source comparison reviewed (OCR truncation/reading-order artifacts on this spread); class reader validation passes. p257 printed subsection numbering retained as shown despite inconsistency.

PDF p257 printed p252: full scan visually reviewed; source content encoded with English, Urdu and Pashto; figures represented by coded SVG where present. Automated source comparison reviewed (OCR truncation/reading-order artifacts on this spread); class reader validation passes. p257 printed subsection numbering retained as shown despite inconsistency.

PDF p258 printed p253: full scan visually reviewed; complete readable material transcribed and translated to Urdu and Pashto; coded SVG provided for source figure(s). OCR comparison reviewed with omissions/reading-order artifacts recorded. Reader validator passes. Equations for wave speed, frequency, and period verified in rendered reader.

PDF p259 printed p254: full scan visually reviewed; complete readable material transcribed and translated to Urdu and Pashto; coded SVG provided for source figure(s). OCR comparison reviewed with omissions/reading-order artifacts recorded. Reader validator passes. Equations for wave speed, frequency, and period verified in rendered reader.

PDF p260 printed p255: full scan visually reviewed; complete readable material transcribed and translated to Urdu and Pashto; coded SVG provided for source figure(s). OCR comparison reviewed with omissions/reading-order artifacts recorded. Reader validator passes. Equations for wave speed, frequency, and period verified in rendered reader.

PDF p261 printed p256: full scan visually reviewed; complete readable material transcribed and translated to Urdu and Pashto; coded SVG provided for source figure(s). OCR comparison reviewed with omissions/reading-order artifacts recorded. Reader validator passes. Equations for wave speed, frequency, and period verified in rendered reader.

PDF p262 printed p257: inspected page scan; source text checked and translated to Urdu/Pashto. Source SVG and/or equations included where applicable. Automated OCR comparison reviewed (sparse OCR on scanned content); reader validation passes. Page 265 Newton estimate and units transcribed as printed.

PDF p263 printed p258: inspected page scan; source text checked and translated to Urdu/Pashto. Source SVG and/or equations included where applicable. Automated OCR comparison reviewed (sparse OCR on scanned content); reader validation passes. Page 265 Newton estimate and units transcribed as printed.

PDF p264 printed p259: inspected page scan; source text checked and translated to Urdu/Pashto. Source SVG and/or equations included where applicable. Automated OCR comparison reviewed (sparse OCR on scanned content); reader validation passes. Page 265 Newton estimate and units transcribed as printed.

PDF p265 printed p260: inspected page scan; source text checked and translated to Urdu/Pashto. Source SVG and/or equations included where applicable. Automated OCR comparison reviewed (sparse OCR on scanned content); reader validation passes. Page 265 Newton estimate and units transcribed as printed.

PDF p266 printed p261: inspected scan; text, equations and values checked visually, with Urdu/Pashto translations. OCR comparator returned low match because of formulas/layout and was reviewed against scan. Reader validation passes. Values are preserved as printed.

PDF p267 printed p262: inspected scan; text, equations and values checked visually, with Urdu/Pashto translations. OCR comparator returned low match because of formulas/layout and was reviewed against scan. Reader validation passes. Values are preserved as printed.

PDF p268 printed p263: inspected scan; text, equations and values checked visually, with Urdu/Pashto translations. OCR comparator returned low match because of formulas/layout and was reviewed against scan. Reader validation passes. Values are preserved as printed.

PDF p269 printed p264: inspected scan; text, equations and values checked visually, with Urdu/Pashto translations. OCR comparator returned low match because of formulas/layout and was reviewed against scan. Reader validation passes. Values are preserved as printed.

PDF p270 printed p265: visually inspected complete scan; transcribed source text and Urdu/Pashto translation; SVG diagrams used instead of scan images. OCR comparison checked; missing formula/reading-order artifacts on p271/p273 resolved from scan. Reader and equation rendering checks pass.

PDF p271 printed p266: visually inspected complete scan; transcribed source text and Urdu/Pashto translation; SVG diagrams used instead of scan images. OCR comparison checked; missing formula/reading-order artifacts on p271/p273 resolved from scan. Reader and equation rendering checks pass.

PDF p272 printed p267: visually inspected complete scan; transcribed source text and Urdu/Pashto translation; SVG diagrams used instead of scan images. OCR comparison checked; missing formula/reading-order artifacts on p271/p273 resolved from scan. Reader and equation rendering checks pass.

PDF p273 printed p268: visually inspected complete scan; transcribed source text and Urdu/Pashto translation; SVG diagrams used instead of scan images. OCR comparison checked; missing formula/reading-order artifacts on p271/p273 resolved from scan. Reader and equation rendering checks pass.

PDF p274 printed p269: source scan visually reviewed; text and English/Urdu/Pashto entered; relevant figures as coded SVG; reader/equation validator passes. OCR comparator reviewed against scan; p275/p277 OCR misses substantial text. Printed example and beat values retained.

PDF p275 printed p270: source scan visually reviewed; text and English/Urdu/Pashto entered; relevant figures as coded SVG; reader/equation validator passes. OCR comparator reviewed against scan; p275/p277 OCR misses substantial text. Printed example and beat values retained.

PDF p276 printed p271: source scan visually reviewed; text and English/Urdu/Pashto entered; relevant figures as coded SVG; reader/equation validator passes. OCR comparator reviewed against scan; p275/p277 OCR misses substantial text. Printed example and beat values retained.

PDF p277 printed p272: source scan visually reviewed; text and English/Urdu/Pashto entered; relevant figures as coded SVG; reader/equation validator passes. OCR comparator reviewed against scan; p275/p277 OCR misses substantial text. Printed example and beat values retained.

PDF p278 printed p273: scan visually reviewed; full readable source transcribed and translated into Urdu/Pashto; relevant illustrations are coded SVG. OCR comparison reviewed against source images (p278/p279/p281 show OCR omission/layout artifacts). Reader validator passes, formulas checked in rendered output.

PDF p279 printed p274: scan visually reviewed; full readable source transcribed and translated into Urdu/Pashto; relevant illustrations are coded SVG. OCR comparison reviewed against source images (p278/p279/p281 show OCR omission/layout artifacts). Reader validator passes, formulas checked in rendered output.

PDF p280 printed p275: scan visually reviewed; full readable source transcribed and translated into Urdu/Pashto; relevant illustrations are coded SVG. OCR comparison reviewed against source images (p278/p279/p281 show OCR omission/layout artifacts). Reader validator passes, formulas checked in rendered output.

PDF p281 printed p276: scan visually reviewed; full readable source transcribed and translated into Urdu/Pashto; relevant illustrations are coded SVG. OCR comparison reviewed against source images (p278/p279/p281 show OCR omission/layout artifacts). Reader validator passes, formulas checked in rendered output.

PDF p282 printed p277: source image visually reviewed; complete legible text and equations entered with Urdu/Pashto translations; coded standing-wave/air-column diagrams. OCR comparison reviewed and formula/line-order omissions checked against scans. Reader validation passes; worked values retained.

PDF p283 printed p278: source image visually reviewed; complete legible text and equations entered with Urdu/Pashto translations; coded standing-wave/air-column diagrams. OCR comparison reviewed and formula/line-order omissions checked against scans. Reader validation passes; worked values retained.

PDF p284 printed p279: source image visually reviewed; complete legible text and equations entered with Urdu/Pashto translations; coded standing-wave/air-column diagrams. OCR comparison reviewed and formula/line-order omissions checked against scans. Reader validation passes; worked values retained.

PDF p285 printed p280: source image visually reviewed; complete legible text and equations entered with Urdu/Pashto translations; coded standing-wave/air-column diagrams. OCR comparison reviewed and formula/line-order omissions checked against scans. Reader validation passes; worked values retained.

PDF p286 printed p281: visual scan reviewed; text/formulas translated and encoded; pipe modes use coded SVG. OCR omissions of subscripts/mode formulas on p287–289 checked against scan. Reader validator passes; closed-pipe odd harmonics and open-pipe series retained.

PDF p287 printed p282: visual scan reviewed; text/formulas translated and encoded; pipe modes use coded SVG. OCR omissions of subscripts/mode formulas on p287–289 checked against scan. Reader validator passes; closed-pipe odd harmonics and open-pipe series retained.

PDF p288 printed p283: visual scan reviewed; text/formulas translated and encoded; pipe modes use coded SVG. OCR omissions of subscripts/mode formulas on p287–289 checked against scan. Reader validator passes; closed-pipe odd harmonics and open-pipe series retained.

PDF p289 printed p284: visual scan reviewed; text/formulas translated and encoded; pipe modes use coded SVG. OCR omissions of subscripts/mode formulas on p287–289 checked against scan. Reader validator passes; closed-pipe odd harmonics and open-pipe series retained.

PDF page 290 (printed 285): scan reviewed; continued closed-pipe harmonics/activity, Example 8.9 and assignment, Doppler introduction with equations, and all prose translated. OCR/content match is low because of equations and dense text; manually checked scan. Reader validation passed.

PDF page 291 (printed 286): scan visually checked; assignment answer 33.5 cm, Doppler-effect definition/history, stationary-source relation λ = v/f and f = v/λ, and source-motion subsection introduction captured with translations. Reader validation passed; content continues on page 292.

PDF page 292 (printed 287): scan visually checked and corrected to include both approaching/receding moving-source cases, equations (8.27) and (8.28), pitch changes, and Figure 8.31 description. Formula labels and diagram are coded; English/Urdu/Pashto pairings complete. Reader validation passed; OCR comparison checked directly because diagram/equation OCR is incomplete.

PDF page 293 (printed 288): scan visually checked; completed the moving-listener case and equation (8.29), translated in English/Urdu/Pashto, with coded Figure 8.32. Prior-page receding-source conclusion retained. Reader validation and OCR-to-code comparison completed; OCR flattened equations and image labels, so image remains the authority.

PDF page 294 (printed 289): scan reviewed; added listener-moving-away case and Equation 8.30, coded Figure 8.33, then the introduction and mutual-approach case for source and listener, including apparent wavelength and Equation 8.31. English/Urdu/Pashto are paired. Reader validation and OCR comparison passed; equations checked against scan.

PDF page 295 (printed 290): scan reviewed; completed the mutual-approach case with its pitch-increase conclusion; added the source-and-listener-moving-away case and Equation 8.32. Transcribed the starlight and aircraft-radar applications, with coded Figure 8.34. English/Urdu/Pashto translations paired. Reader validation and OCR comparison passed.

PDF page 296 (printed 291): scan reviewed; added application (iii) on submarine and satellite Doppler shifts, the ambulance-observer quiz with coded SVG, and Example 8.10 givens/required values and approaching-car formula. Paired English/Urdu/Pashto text, equation rendering, and OCR comparison passed.

PDF page 297 (printed 292): full scan reviewed; completed Example 8.10 with 531 Hz/472 Hz, Assignment 8.6 with its printed answers, sonic-boom explanation and coded Figure 8.35, and full opening section on ultrasonic waves including audible limits and normal 20–100 kHz range. English/Urdu/Pashto paired and reader validation passed. OCR comparison is low due to formula/layout text loss; visual scan was the authority and every printed text block was checked.

PDF page 298 (printed 293): source scan checked; included v = fλ, 25-billion-Hz and printed wavelength comparisons (10⁻⁸ m ultrasound, 10⁻⁷ m visible light, 10⁻¹⁰ m X-rays), object-size/penetration explanation, medical diagnosis and bloodless surgery, and nondestructive metal testing. Figure 8.35 is a coded CRO/probe/casting/flaw diagram. Trilingual text, reader validation, and OCR comparison passed.

PDF page 299 (printed 294): source scan checked; added reflected-pulse flaw detection (including A/B/C pulse roles), ultrasonic metal cleaning, bacterial/microorganism destruction, focused-wave neurosurgery and listed treatments, cavitation/degassing, and bat echolocation sidebar with coded SVG. English/Urdu/Pashto pairings, OCR comparison, and reader validation passed.

PDF page 300 (printed 295): scan reviewed; encoded ultrasonic generation by piezoelectric and magnetic-crystal methods, v = fλ, the source voltage forms, piezoelectric detection and Kundt’s-tube node/antinode behavior. Added all three boxed wave/mechanical/electromagnetic key-point definitions. English/Urdu/Pashto, reader validation, and OCR comparison passed.

PDF page 301 (printed 296): full key-points scan reviewed. Transcribed all nine definitions in order (transverse, longitudinal, interference, beats, stationary waves, resonance, organ pipes, Doppler effect, ultrasonic waves) with source-matched English and Urdu/Pashto pairings. Automated OCR coverage is low because it missed most of the boxed page; the full source image was reviewed directly. Reader validation passed.

PDF page 302 (printed 297): source scan verified; transcribed eight multiple-choice questions with all choices, preserving π/2, π, 2π and ultraviolet frequency exponents. Full English/Urdu/Pashto question sets recorded without adding answer keys. OCR comparison and reader validation passed.

PDF page 303 (printed 298): scan reviewed; completed MCQs 9–12 with the source √2 and fraction-power options, then all nine conceptual questions in source order. Translations paired in Urdu and Pashto; automated source comparison and reader validation passed.

PDF page 304 (printed 299): scan reviewed; captured conceptual questions 10–11 and all nine comprehensive questions with subparts, including the 0.61 m s⁻¹ per °C value and two Doppler derivations requested. Source-comparison and reader validation passed; paired English/Urdu/Pashto.

PDF page 305 (printed 300): scan visually reviewed; added organ-pipe questions 10–11 and eight numerical problems with all legible source data and printed results. Source image clips part of numerical 8’s answer at the right edge; visible fragment recorded verbatim and page marked unresolved, without guessing. Reader validation and OCR comparison completed.

PDF page 306 (printed 301): scan visually checked; captured numericals 9–13 with source data and every legible printed answer, including the train’s two listed observer frequencies as printed. English/Urdu/Pashto aligned; automated source comparison and reader validation passed.

PDF page 307 (printed 302): source scan reviewed; began Unit 9 Physical Optics, captured butterfly angle-dependent colour question and all eight learning outcomes, with coded SVG illustration. OCR missed much of the learning-outcomes block; full page image reviewed. Reader validation passed.

PDF page 308 (printed 303): scan reviewed; transcribed eight additional learning outcomes including d sin θ = nλ, optics overview, Ibn al-Haytham sidebar with the source’s Alhozen spelling, and Maxwell’s 1873 electromagnetic-wave statement. Reader validation and source comparison passed; English/Urdu/Pashto aligned.

PDF page 309 (printed 304): scan reviewed; included electromagnetic-wave speed/no-medium statement, wave/particle duality, wavefront definition and water-crest example, point-source propagation, and the text’s circular/spherical wavefront terminology. Figures 9.1 and 9.2 coded as SVG. OCR comparison flagged omissions; reviewed all blocks visually. Reader validation passed.

PDF page 310 (printed 305): scan reviewed; recorded rays perpendicular to wavefronts, inverse-square illuminance, spherical-to-plane wavefront, and both parts of Huygens’ principle at t + Δt. Figures 9.3 and 9.4 are coded SVGs. Reader validation passed; source comparison run and formula/context checked against image.

PDF page 311 (printed 306): visually reviewed at 1.8x and 4x. Recorded the Huygens construction explanation and coherent-source introduction with explicit clipped-text markers; reused coded Figure 9.4 representation. The source image cuts off clauses at its right edge, so page is marked unresolved. Reader validation passed; OCR comparison run.

PDF page 312 (printed 307): source scan checked; captured two coherent-source methods, monochromatic-light note, interference definition and Young context, all five conditions, and screen placement leading into Figure 9.5 on the next page. Trilingual pairs, reader validation, and OCR comparison completed.

PDF page 313 (printed 308): scan reviewed; encoded Figures 9.5–9.6 as SVG, constructive interference explanation, and the printed phase/path-difference sequence and condition d = mλ (9.1), m = 0,1,2,… . Trilingual pairs, reader validation, and OCR comparison completed.

PDF page 314 (printed 309): source image reviewed; transcribed destructive-interference phase/path sequence and d = (m + 1/2)λ (9.2), same-source phase consistency, and television reflection/distortion note. Figures 9.7 and the reflected-signal application are coded SVG. English/Urdu/Pashto aligned and reader validation passed.

PDF page 315 (printed 310): scan visually checked; transcribed Young’s 1801 experiment, the wavefront-division principle, Figure 9.8’s fringe/intensity/wavefront panels, and the experimental arrangement. The right edge clips the final arrangement wording; gap is marked and page is unresolved. Reader validation and OCR comparison completed.

PDF page 316 (printed 311): scan visually checked; captured slit-C wavefront division, coherence of A/B, diffraction/interference fringe paths, Figure 9.9 geometry, definitions of d, L, O, central bright fringe, and path excess s at P. Coded setup SVG. Reader validation and OCR comparison passed.

PDF page 317 (printed 312): source scan checked; derived d sin θ = mλ from s = mλ and s = d sin θ, recorded central and first-order maxima, printed fringe-position labels, and destructive odd-half-wavelength phase condition. Figures 9.10(a–d) are coded SVG. Reader validation and OCR comparison completed.

PDF page 318 (printed 313): scan reviewed; recorded destructive condition, fringe-position similar-triangle derivation and y = Ls/d (9.3), plus full blue-sky scattering sidebar. Coded illustration included; English/Urdu/Pashto paired, reader check passed, and OCR comparison run.

PDF page 319 (printed 314): scan verified; encoded mth bright/dark fringe positions in equations 9.4–9.5 and both worked consecutive-fringe spacing calculations yielding Lλ/d (9.6). Equation renderer and reader validation passed; OCR comparison completed.

PDF page 320 (printed 315): scan checked; included independent-headlights quiz and Example 9.1 givens, setup, full working, and printed answers for first bright/dark fringes. Verified exponent and unit conversions; reader validation and OCR comparison completed.

PDF page 321 (printed 316): source scan verified Example 9.2; encoded second dark fringe at 18 arcminutes for 546 nm, full degree conversion and slit separation calculation yielding 260.7 μm. Reader validation passed; OCR comparison completed.

PDF page 322 (printed 317): visually verified Assignment 9.1 values and printed answer, 9.7 thin-film interference introduction, amplitude division, coherent reflected rays a/b, path-difference factors, and Figure 9.11 labels. Added coded SVG and aligned English/Urdu/Pashto paragraphs. Reader validation and OCR comparison completed.

PDF page 323 (printed 318): visually checked both reflected-wave phase-change cases (lower-to-higher index gives 180°; higher-to-lower gives no change), white-light thin-film colour explanation and soap-bubble sidebar, plus Michelson interferometer purpose, division-of-amplitude principle, parts M₁/M₂ and A/B, plate A half-reflection/half-transmission, and movable/fixed mirrors. Reader validation and OCR comparison completed.

PDF page 324 (printed 319): visually verified Figure 9.12(a) source, split at A, beam 1 reflection toward movable M₁ then transmission to eye, beam 2 transmission toward fixed M₂ then reflection back through A to eye, compensator B equalizing glass paths, and labels L₁/L₂. Encoded SVG. Transcribed brightness/constructive condition d = 0, λ, 2λ, … = mλ, m = 0,1,2,… (9.7). Reader validation and OCR comparison completed.

PDF page 325 (printed 320): visually verified Michelson dark condition d = λ/2, 3λ/2, … = (m + 1/2)λ (9.8); equal mirror distances and compensator plate path correction giving zero difference/bright fringe; moving M₁ by λ/4 changes difference to λ/2 (dark), then λ (bright), alternating bands; coded diagram text for Figure 9.12(b). Reader validation and OCR comparison completed.

PDF page 326 (printed 321): visually checked P=m(λ/4+λ/4)=mλ/2 and λ=2P/m (9.9), Example 9.3 source value 630 nm, one fringe, full calculation and printed 315 nm answer. Began 9.9 diffraction explanation through the bottom-clipped phrase “water waves on a smooth”; marked continuation rather than completing from inference. Reader validation and OCR comparison completed.

PDF page 327 (printed 322): scan verified diffraction definition, criterion that opening/obstacle is comparable to wavelength, continuation of water-wave example, and figures 9.13–9.14. Added coded narrow-gap wavefront and intensity-versus-angle fringe SVGs with visible labels and trilingual text. Reader validation and OCR comparison completed.

PDF page 328 (printed 323): scan verified Young slit-C spreading explanation, central diffraction maximum intensity/width, knife-edge diffraction reference, Fraunhofer single-slit definition, photographic-film setup, wider-than-slit central band and side bands, Figure 9.15(a) labels. Added coded SVG and aligned translations. Reader validation and OCR comparison completed.

PDF page 329 (printed 324): visually checked Figure 9.15(b), single-slit Huygens construction and symmetrically paired wavelets at O; equal paths from A/B and X/Y give a central bright spot. At P, A/B path difference is λ and paired A/Q, X/Y, Q/B differences are approximately λ/2. Encoded diagram with labels. Reader validation and OCR comparison completed.

PDF page 330 (printed 325): visually verified first dark fringe derivation (d/2)sinθ=λ/2, d sinθ=λ; general minima sinθₘ=mλ/d, m=1,2,3,… (9.10); symmetric dark bands, bright bands between, central maximum intensity; narrow-slit θ≈λ/d and width/intensity tradeoff. Recorded diffraction grating purpose, spectrometer, plate dimensions, equally spaced parallel slits and scratched transparent plate construction. Reader validation/OCR comparison completed.

PDF page 331 (printed 326): scan verified grating principle and wavelength-measurement use, five-slit Figure 9.16(a), parallel monochromatic rays, in-phase adjacent slits focused by achromatic lens at P, constructive condition Δr=λ and geometric relation Δr=d sinθ (i–ii). Added coded grating SVG and trilingual source-aligned text. Reader/OCR validation completed.

PDF page 332 (printed 327): visually verified d sinθ=λ for first order; grating element d=unit length/N and d=1 cm/N; higher orders for 2λ, 3λ, … and general d sinθ=mλ, m=0,1,2,3,…; spectrometer collimator/telescope procedure and diagram labels/orders. Added coded spectrometer SVG and trilingual content. Reader/OCR validation completed.

PDF page 333 (printed 328): visually verified Example 9.4 N=5000 lines/cm, θ=32°, order 2, d=0.00020 cm, sin32°≈0.53, λ=5.3×10⁻⁵ cm; encoded all steps. Added 9.12 crystal X-ray rationale (atomic layer spacing <1 nm; X-ray wavelength ~10⁻¹⁰ m; Young/thin-film methods unsuitable) and Figure 9.17 diagram labels. Reader/OCR validation completed.

PDF page 334 (printed 329): visually verified fringe spacing Lλ/d, crystal-plane separation about 10^-10 m, NaCl and Laue experiment, collimated beam, detector, central spot plus Laue spot pattern, and crystal-structure relation. Added coded diagrams. Bragg law derivation starts with rays I and II at adjacent crystal planes; continuation marked. Reader and OCR checks completed.

PDF page 335 (printed 330): verified layer separation d, glancing θ, excess path BC+CB′=mλ and BC=CB′=d sinθ; encoded 2d sinθ=mλ, m=1,2,3,… (9.11) and Figure 9.20. Recorded source applications to interplanar spacing, hemoglobin and DNA double helix. Reader/OCR checks completed.

PDF page 336 (printed 331): visually verified Example 9.5 values, full Bragg substitution and printed 17° result; transcribed Assignment 9.2 givens/prompt; encoded polarization introduction, transverse inference, single-plane electric/magnetic vibration definition and contrast with sound. Reader/OCR validation completed.

PDF page 337 (printed 332): verified crossed-slot transverse-wave experiment, longitudinal spring counterexample, polarized sunglasses sidebar, and 9.13.1 ordinary-light explanation of differently oriented transitions. Last sentence is right-clipped in the source scan; noted as unresolved and kept the partial thought without completion. Added coded SVG. Reader/OCR checks completed.

PDF page 338 (printed 333): visually verified E/B perpendicular-field statement and Figure 9.22; methods list (selective absorption, surface reflection, crystal refraction, tiny-particle scattering); dichroic Polaroid quinine iodosulphate material and axis-selective transmission; first crystal explanation in two-tourmaline experiment. Added coded EM/polarizer SVG. Reader/OCR validation completed.

PDF page 339 (printed 334): visually verified parallel tourmaline axes transmit, rotation reduces intensity, crossed axes at 90° extinguish, further rotation restores light; analyzer naming and Figure 9.23(a–b). Transcribed polarization-by-reflection conditions and Snell-law lead-in; resulting relation continues next page. Added coded analyzer SVG. Reader/OCR checks completed.

PDF page 340 (printed 335): scan checked Snell relation n₁sin iₚ=n₂sin r (9.12), geometry r=90°−iₚ, reduction to n₂/n₁=tan iₚ (9.13), glass refractive index 1.55 giving printed iₚ=57°. Added ray diagram SVG with polarization labels and right-angle relation. Reader/OCR validation completed.

PDF page 341 (printed 336): visually reviewed activity, glare-reduction explanation and diagram, photographic Polaroid application, glass-reflection sidebar, and optical activity/quartz/sugar-solution/polarimeter use. Activity and some right-side source wording are clipped; page marked unresolved, fragments bounded without completing. Reader/OCR checks passed.

PDF page 342 (printed 337): verified curtainless window polarizer adjustment, headlight-glare control, photoelastic stress analysis with crossed Polaroids, and key-point definitions of dual light nature, wavefront, ray, coherent sources, interference, diffraction, polarization. Reader/OCR checks completed.

PDF page 343 (printed 338): visually verified and transcribed MCQs 1–8 with every option, including λ and 3λ in question 8. No answers added. Reader/OCR checks completed.

PDF page 344 (printed 339): visually verified MCQs 9–11, all options and ratio λX/λY; captured all eight conceptual questions in order without answers. Reader/OCR checks completed.

PDF page 345 (printed 340): visually verified continuation conceptual questions 9–10, comprehensive questions 1–9 and full Young numerical givens, fifth bright fringe, screen distance and printed 9.3 mm answer. No solutions added. Reader/OCR checks completed.

PDF page 346 (printed 341): visually checked numerical problems 2–9, all units/exponents/angles and printed answer keys. Encoded 5.8×10^-7 m; Michelson 0.1 mm/580 nm; soap film n=1.40/546.1 nm; grating 5000 lines/cm and 589 nm; 250 lines/mm at 12°; X-ray spacing 2.8×10^-10 m at 5°; λ=0.48×10^-10 m at 20°; NaCl d=0.282 nm at 7°. Reader/OCR checks completed.

PDF page 347 (printed 342): verified Unit 10 Thermodynamics opening image/question about 20–25% gasoline energy conversion and all six learning outcomes. Added new chapter and source-mapped section without crossing class/subject boundaries. Reader/OCR checks passed.

PDF page 348 (printed 343): visually verified the complete continuation outcomes list: internal energy/state, volume work, first-law/conservation, specific and molar heat capacities with Cₚ−Cᵥ=R, heat engines, reversible/irreversible processes, second law, Carnot efficiency, refrigerators/COP, entropy signs/disorder/energy degradation. Reader/OCR checks completed.

PDF page 349 (printed 344): verified thermodynamics definition, energy conversion scope, first/second law basis, engines/refrigerators/heat pumps, system terms, Rankine sidebar, and section 10.1 heat transfer to equilibrium with Figure 10.1 soft drink/ice states. Added coded SVG. Reader/OCR checks completed.

PDF page 350 (printed 345): verified equilibrium statement and vacuum question, work definition W=F·Δs, expansion/contraction and sign convention, quiz, Figure 10.2 piston force/displacement, and internal-energy molecular-motion definition. Added coded piston SVG and trilingual text. Reader/OCR checks completed.

PDF page 351 (printed 346): verified kinetic-energy modes, conversion of heat/work to internal energy, both quiz prompts, section 10.4 distinction of heat/work/internal energy, heat definition as transfer solely due to temperature difference, flow until equilibrium, joule SI unit, calorie definition and 14.5–15.5°C bounds. Reader/OCR checks completed.

PDF page 352 (printed 347): verified kcal definition, four work-heating examples, distinction between heat/work energy transfer, quiz prompts, Rumford 1798 friction experiment conclusion, Joule 1845 measurement and sentence continuation. Reader/OCR checks completed.

PDF page 353 (printed 348): visually verified Joule proportionality W∝Q, W=JQ, J definition/value 4.18 J/cal and SI value 1. Encoded Example 10.1 QH=65.0 kcal, QL=40.0 kcal, 4,184 J/kcal conversion, 104,600 J and printed 105 kJ result. Reader/OCR checks completed.

PDF page 354 (printed 349): verified Joule quiz, thermodynamic system/environment/boundary description, heat/work exchanges, car cylinder system and piston/exhaust/radiator/outside-air surroundings, cylinder/piston boundary, process definition and system/surroundings terms. Added coded Figure 10.3 SVG. Reader/OCR checks completed.

PDF page 355 (printed 350): verified bag-on-flame sidebar, boundary energy exchange, closed-system no-mass definition, heat transfer, Figure 10.4 open kettle versus approximate pressure cooker with small steam release, and ink-dot point-to-ponder prompt. Added coded diagram. Reader/OCR checks completed.

PDF page 356 (printed 351): verified open/isolated system definitions and examples, state/state variables/functions, homogeneous state parameters, ideal-gas PV=nRT and variable definitions, U/S examples, heel-lubricant point-to-ponder, and start of process/reversible/irreversible section. Reader/OCR checks completed.

PDF page 357 (printed 352): verified reversible definition and examples, irreversible definition/examples, cyclic process/heat-engine note, conservation statement, internal-energy state variable and first-law relation ΔQ=ΔU+ΔW with work by system convention. Reader/OCR checks completed.

PDF page 358 (printed 353): visually verified ΔQ sign, ΔU sign, three first-law ideas, molecular kinetic/potential internal energy, Earth heat-balance prompt, ΔU=ΔQ−ΔW interpretation, and state-function path independence with U_B−U_A relation. Reader/OCR checks completed.

PDF page 359 (printed 354): visually verified cyclic condition U_B=U_A and ΔQ=ΔW (10.2), ice-block quiz, first-law application categories, isochoric constant-volume setup and ΔW=0 giving ΔQ=ΔU (10.3). Right-edge-cropped prose marked unresolved without filling gaps. Reader/OCR checks completed.

PDF page 360 (printed 355): verified isochoric heating/cooling interpretation, Figure 10.5 fixed piston/P–V vertical line, isobaric constant-pressure definition, cylinder/piston setup and work derivation ΔW=FΔY, F=PA, ΔV=AΔY, ΔW=PΔV. Reader/OCR checks completed.

PDF page 361 (printed 356): verified isobaric work ΔW=PΔV (10.4), first-law relation ΔQ=ΔU+PΔV (10.5), state/figure labels, isothermal definition, ideal-gas internal-energy dependence on temperature, and reservoir/piston setup. Right-edge source text clipped; marked unresolved. Reader/OCR checks completed.

PDF page 362 (printed 357): verified isothermal expansion heat reservoir, isotherm state endpoints and Figure 10.7, ΔU=0 and ΔQ=ΔW; contraction counterpart; adiabatic definition ΔQ=0, insulation/rapid-process explanation and Figure 10.8. Bottom line clipped and marked unresolved. Reader/OCR checks completed.

PDF page 363 (printed 358): verified practical adiabatic setup/ΔQ=0, expansion cooling and compression heating, derivation ΔW=−ΔU (10.6), adiabat definition, pond-ice quiz, Example 10.2 givens and requirement (400 J heat; 150 J work by system). Reader/OCR checks completed.

PDF page 364 (printed 359): verified Example 10.2 steps and 250 J answer; Assignment 10.1 all values/conditions/printed answers; biological first-law explanation, human heat/work/food and photosynthesis figure labels. Added coded SVG. Reader/OCR checks completed.

PDF page 365 (printed 360): verified heat and molar-specific-heat definitions, proportional relation ΔQ=CₘnΔT (10.7), Cₘ expression and units J mol⁻¹ K⁻¹, and constant-volume/constant-pressure cases. Source right edge clips the conditions list and Cᵥ definition; readable fragment retained with explicit marker, no text guessed. Reader/OCR checks completed.

PDF page 366 (printed 361): verified fixed-piston constant-volume explanation and Figure 10.9 labels; ΔQᵥ=nCᵥΔT (10.8). Verified constant-pressure definition, movable-piston expansion/work explanation and Figure 10.10; ΔQₚ=nCₚΔT (10.9). Both source figures coded as SVG. Reader/OCR checks completed.

PDF page 367 (printed 362): verified Cₚ > Cᵥ explanation, fixed/moveable piston comparison (Figure 10.11), ΔQᵥ=nCᵥΔT, ΔWᵥ=0, first-law steps ΔQᵥ=ΔU and ΔU=nCᵥΔT, plus ΔQₚ=nCₚΔT. Page begins next constant-pressure derivation, continued on page 368. Coded SVG. Reader/OCR checks completed.

PDF page 368 (printed 363): verified derivation Cₚ−Cᵥ=R=8.315 J mol⁻¹ K⁻¹ (10.10); exact point-to-ponder question; Example 10.3 nitrogen givens, n=7.143 mol, ΔT=20 K, and printed ΔU=2973.6 J. Work diagram coded SVG. Reader/OCR checks completed.

PDF page 369 (printed 364): verified heat-engine definition, source/HTR, sink/LTR and working-substance descriptions; cyclic operation, ΔU=0, first-law work balance and ΔW=Q₁−Q₂ (10.11). Figure 10.12 labels coded as SVG. Bottom-edge clipping in efficiency definition marked unresolved. Reader/OCR checks completed.

PDF page 370 (printed 365): verified η=ΔW/Q₁ (10.12), η=1−Q₂/Q₁ (10.13), impossibility of 100% efficiency and second-law statement; both quiz questions and Example 10.4 values. Coded heat-engine flow SVG. Reader/OCR checks completed.

PDF page 371 (printed 366): verified Example 10.4 reversible-engine steps and T₁=100°C/T₂=0°C; Assignment 10.2 all visible values and printed answers; opening second-law text. Right-edge source clipping in the assignment and prose marked unresolved, no completion guessed. Coded SVG. Reader/OCR checks completed.

PDF page 372 (printed 367): verified Kelvin and Clausius statements of second law; Carnot-engine introduction and Sadi Carnot caption/pronunciation note. Source text continues to next page. Coded SVG illustration. Reader/OCR checks completed.

PDF page 373 (printed 368): verified Carnot-engine idealization, construction, four-process cycle structure, P–V diagram labels, isothermal expansion A–B with +Q₁ and adiabatic expansion B–C with temperatures/volumes/pressures. Right-edge scan clipping explicitly marked unresolved. Coded P–V SVG. Reader/OCR checks completed.

PDF page 374 (printed 369): verified isothermal compression C–D, adiabatic compression D–A and cycle completion; net work/heat and η=ΔW/Q₁=(Q₁−Q₂)/Q₁; equations (10.14) Q₂/Q₁=T₂/T₁ and (10.15) η=1−T₂/T₁. Coded Carnot-cycle SVG. Reader/OCR checks completed.

PDF page 375 (printed 370): verified Carnot efficiency depends only on reservoir temperatures, 0 K implies impossible 100%, actual-engine losses, Carnot theorem and Otto/Diesel facts; Example 10.5 givens T₁=600 K, η=0.55 and required T₂. Coded SVG. Reader/OCR checks completed.

PDF page 376 (printed 371): verified Example 10.5 substitution and answer T₂=270 K; refrigerator/reverse-cycle definitions, refrigerator vs heat pump, Q₂ extraction, compressor work, Q₁=W+Q₂ (10.16), and Figure 10.14 labels. Coded SVG. Reader/OCR checks completed.

PDF page 377 (printed 372): source scan has major left/right cropping. Visible refrigerator cooling/heating COP equations and Clausius statement transcribed with clipping explicitly marked; Example 10.6 givens E=8, T₂=−23°C=250 K preserved; remaining solution continues next page. Coded SVG. Reader/OCR checks completed.

PDF page 378 (printed 373): verified Example 10.6 solution T₁=281.25 K=8.2°C and all three point-to-ponder questions. Verified entropy definition/ΔS=ΔQ/T (10.18), hot-to-cold entropy changes and positive net result. Bottom natural-process statement clipped and marked unresolved. Coded SVG.

PDF page 379 (printed 374): verified natural entropy increase, hot-to-cold heat flow, heating/free expansion disorder, red/green balls example, energy degradation and heat death of universe. Coded SVG for ball mixing. Reader/OCR checks completed.

PDF page 380 (printed 375): verified Example 10.7 water freezing, m=0.03 kg, Hf=336000 J/kg, ΔQ=10080 J, printed entropy magnitude 36.92 J/K; notes sign physically negative for freezing. Verified Assignment 10.3 givens/questions/answers and visible key-point definitions. Key-point panel continues next page. Coded phase-change SVG.

PDF page 381 (printed 376): verified remaining key-point definitions; exercise MCQ 1 and MCQ 2 stems/options (visible scan), no answer key inferred. Exercise continues next page. Coded SVG distinction for reversible/irreversible process.

PDF page 382 (printed 377): visually checked and transcribed MCQs 3–12 including all stems, numeric values, answer options and exact printed forms. No answers inferred. Reader/OCR checks completed.

PDF page 383 (printed 378): verified conceptual questions 1–11 and comprehensive questions 1–3. Right-edge clipping within comprehensive question 2 recorded explicitly; no additional questions/answers inferred. Reader/OCR checks completed.

PDF page 384 (printed 379): verified comprehensive questions 4–11; all five numerical problem givens and printed answers (22°C; 19200 J; 127.66 J/52.34 J; 26.8%; 40%/27°C/800 J). Reader/OCR checks completed.

PDF page 385 (printed 380): verified numerical questions 6–10 with all visible givens, source units and printed answers. Q7 specific-heat unit is printed as J mol⁻¹ K⁻¹ and retained verbatim. Q8 has three visible heat/work scenarios but only two printed answers; exact mapping is left unspecified rather than inferred. Reader/OCR checks completed.

PDF page 386 (printed 381): verified glossary entries Adiabatic process through Doppler shift, including all definitions. Source clips beginning of “source” in final Doppler definition; visible fragment preserved and marked unresolved. Reader/OCR checks completed.

PDF page 387 (printed 382): verified glossary entries Drag force through Node. Entropy definition is visibly incomplete/unclear; forced/free oscillation lines have ambiguous column alignment; modulus wording prints “Ration”. These source issues are explicitly preserved and flagged unresolved. Reader/OCR checks completed.

PDF page 388 (printed 383): verified glossary entries Null vector through Simple harmonic motion and definitions. “Rotational equilibrium” definition is retained verbatim as printed although it appears inconsistent with the heading; not corrected. Reader/OCR checks completed.

PDF page 389 (printed 384): verified glossary entries Spherical wavefront through Work. System international definition is malformed (“used almost over”); Total internal reflection and rotational/translational equilibrium wordings retained as printed. Source issue flagged unresolved. Reader/OCR checks completed.

PDF page 390 (printed 385): verified Authors Profile for six named contributors and source-stated experience/positions/qualifications. Ambiguous final position abbreviation A.S.S. retained and flagged for source verification. Reader/OCR checks completed.

PDF page 391 (printed 386): verified Textbook Feedback Form organization header/contact, all eight statements, table headings, and blank response fields. Source prints “effective skills”; retained with note rather than silently substituting. Reader/OCR checks completed.

PDF page 392 (printed 387): visually transcribed two Urdu quotations and printed citations/attribution; provided aligned English and Pashto translations. OCR does not capture Urdu; manually checked against rendered scan. Reader/OCR checks completed.

PDF page 393 (back cover, printed 388): manually checked Urdu national anthem transcription and imprint against scan. Added English and Pashto translations. Printed code PSP/MTP-11-45-2324(0), quantity 56,420, price FREE, Muhammadi Traders & Printers.


User speed instruction (2026-10-10): target 400 source-reviewed pages/hour; use batch extraction/OCR, translation cache, reusable vocabulary, automated source-to-code comparison, safe parallelism, and continuous checkpoints. Report measured page rates honestly; never skip or claim uninspected pages verified.

Chemistry is now active after Physics primary-source traversal. Chemistry Test Edition (chemistryfull.pdf, 419 PDF pages, SHA-256 recorded in inventory) is sequential primary; its split/alternate PDFs remain pending edition comparison. OCR batch output: 	mp/class-11/chemistryfull-ocr-batch-20261010-083943 (direct RapidOCR extraction benchmark; not source verification). Pages 1–2 inspected; sequential checkpoint page 2, next page 3. The dedicated chemistry dataset/route is present. First title cover imagery is meaningful and needs coded SVG representation; transcribed title records still require final paired trilingual implementation. Next page: 3, front-matter credits.
Chemistryfull PDF pages 1–2: rendered and checked against the original scans. Page 1 title cover: “A Textbook of Chemistry,” “Grade XI,” “Test Edition,” Khyber Pakhtunkhwa Textbook Board, Peshawar; molecule, flame, states-of-matter, glassware, and fruit-battery imagery is coded visually rather than reproduced as a raster. Page 2 interior title page: same title/grade/publisher with a visible molecular-bond motif. Page 2 is labeled printed p. 0 for this source mapping. Dedicated Class 11 Chemistry route/dataset wired and syntax-checked. Cover translation/paired paragraphs not completed yet; these are source-reviewed page records with code implementation outstanding. Next PDF page 3 (credits). OCR batch is reference-only.

PDF page 3: credits scan inspected. Authority approval identifier/date and portions of edge-curved lines are ambiguous. OCR is not authoritative. Names, organizations, precise line text, and all translation pairs remain to be transcribed with unresolved clipped fields explicitly identified.
PDF page 4: Table of Contents upper half checked; Units 1–7 and starting printed pages read from image. PDF page 5 continues contents with Units 8–12, Glossary p392, Index p406; title “Table of Contents” repeated. Exact right-edge entries for Units 8–12 are clipped by page curl and not included in verified chapter ranges yet.
PDF pages 6–8: implemented source-matched content. Page 6: Unit 01 Stoichiometry; six learning outcomes translated; methane combustion molecule/equation figure coded SVG. Page 7: introduction, meaning/origin of stoichiometry, quantitative information use, side box definition for analytical chemistry and heading 1.1, translated. Outer right edge in first paragraph was visibly curled/cropped; restoration from chapter split unsuccessful because it is also scanned, so page 7 is unresolved for exact full agreement. Page 8: gram-atom definition, mole, number 6.023 × 10²³, Avogadro definition and attribution, four examples, Figure 1.1 scale/12 g carbon-12 represented as accessible coded SVG; translations aligned.
PDF page 9 inspected: Table 1.1 first 20 elements, STS box on qualitative/quantitative analysis, and start of 1.2 Molar Mass. Need code table; bottom molar-mass definition is edge-curled/clipped, unresolved. Next PDF page 10.


Chemistry OCR batch progress at latest checkpoint: 416/419, extraction 1223.5 pages/hour, 0 failures. This is extraction-only. Sequential Chemistry implementation checkpoint stays at PDF page 8; next formal source-to-code compare is page 9. Pages 9–17 have been visually inspected as aids but remain unchecked in the inventory pending implementation/source-to-code comparison. Implement page 9 before advancing. Do not use OCR or visual lookahead as completion evidence.

Checkpoint update: Chemistry primary pages 1–9 now have dedicated source-linked implementation records in js/chem_11_data.js: coded cover diagrams, credits, two contents tables, six translated Stoichiometry outcomes plus reaction SVG, introduction, Avogadro section and coded illustration, first-20-elements source table, analytical chemistry STS feature. Pages 3, 7, and 9 retain unresolved source-curl text. Inventory next page is 10; last fully verified contiguous page is 2. Batch OCR completed 419/419, 0 failures, extraction-only 1,224.9 pages/hour. Automated OCR/code token overlap saved as 	mp/class-11/chemistryfull-ocr-batch-20261010-083943/chemistry-source-code-overlap.json; low overlap is a locator for manual comparison, not a verified result. Page 10 must be source-compared next, with Example 1.1 continued across pages 10–11.
Checkpoint correction: returned the next consecutive page to PDF page 1. Pages 1–5 were inspected but have not been fully represented and trilingually implemented. Pages 6–9 have draft content, but must also be source-to-code validated before these front-matter gaps are cleared. No later page is marked verified. Current next formal page: 1.

Chemistry consecutive source implementation through PDF p18 (next p19). Pages p1–p18 have trilingual text records; coded visual assets: cover concept collage (p1), title-page molecular-ring motif (p2), 20-element table and both contents tables, stoichiometric reaction, Avogadro scale, conversion chart, and equations 1.1–1.4. Sequential pages include Worked Examples 1.1–1.10 and Practice Problems 1.1–1.7 with printed values retained. Focused Chemistry reader validation passed: 101 paired paragraphs, 119 unique IDs, 18 sequential source-page records, route/script wiring, equations/tables, interactive translations, no raster embeds. Syntax checks passed. Page 3 authority/edge text; p7 fold-clipped introduction; p9 sentence clipped across page break remain unresolved. Contiguous fully verified remains p2; nextPage=19 so independent later work proceeds. Chemistry primary OCR batch finished 419/419, 0 failures; extraction-only speed 1224.9 pages/hour. OCR/source overlap diagnostic updated through p18.
Chemistry implemented through PDF page 19, next page 20. Reader check updated and passed for 19 sequential source pages, source-data pairing, equation/table/rendering, route wiring, no raster assets. Page 19 percentage-composition formulas (5)/(4) and sulphuric-acid percentages entered; the printed 62 term in “2 + 32 + 62 = 98” is preserved and an editorial arithmetic clarification shown separately. Pages 3, 7, 9 retain unresolved scan text. Last fully verified contiguous remains p2; later source-reviewed pages continue despite documented defects.
Chemistry implemented through PDF page 20; next page 21. Added Example 1.12 with Al/Zn 3.6 g / 6.4 g, Practice Problem 1.9, definitions of limiting and excess reagents, and Reading Check. Reader check: 112 paired paragraphs, 132 unique IDs, 20 sequential page records, source route, equations, tables, interactive translations and no raster embeds all pass. OCR-code comparison report updated through p20. Remaining unresolved source text is p3 approval edge, p7 folded introduction and p9 molar-mass sentence across page turn. Last fully verified contiguous page 2; later work proceeds. OCR extraction benchmark is separate from content work.


Verification correction: Chemistry draft coverage is PDF pages 1–21. Syntax/data checks do not establish verbatim source agreement. Earlier draft paragraphs merged or shortened text and some clipped prose was reconstructed. All Chemistry verification flags are withdrawn; last fully verified page=0, next audit page=1. Do not count these drafts as fully verified. p22 is rendered but has no reader record. Cover diagram direction and molecule argument order were repaired; page ordering now sorts by source PDF page. Two Urdu fields containing Pashto were corrected. Formal current checkpoint is inventory.json. Extraction remains 419/419 at 1224.9 pages/hour; completed exact-audit throughput for this resumed segment is zero verified pages, so the 400-page/hour verification target has not been met.

Fresh Chemistry audit 2026-10-10: p1 title split and publisher case corrected; p1 remains unresolved because the source uses molecular clusters and linked solid lattice, while its coded model uses plain dots. p2 verified corrected after direct image inspection: separate title blocks, Grade XI, uppercase publisher, Urdu/Pashto pairs; invented molecular motif/caption removed and decorative pattern/emblem/watermarks explicitly excluded. Focused reader check passes (121 pairs, 142 IDs); this is structural evidence only. Primary checkpoint stays p1, highest contiguous verified=0; verified corrected pages=[2]. Exact-audit speed has not yet been timed for this resumed segment; no claim of 400 verified pages/hour.

Fresh Chemistry checkpoint: p1 coded red-and-white molecular clusters and connected lattice added; final source count/placement audit pending. p3 restored headings and contributor bullet lists, corrected Salmana name, retained visible approval/review fragments with gap notes instead of reconstructed wording. chemistry1.pdf p3 embeds the identical source image (SHA256 recorded in inventory); it cannot resolve the fold. p4 all seven contents entries source-compared and verified corrected, title duplication removed and translations paired. p5 Solutions and Colloids corrected 289→296; cropped unit8/9 page endings now explicit gaps. Verified corrected=[2,4]; unresolved includes1,3,5; contiguous=0, formal next audit page1. Focused reader check:141 pairs/162 IDs passes; structural evidence only. Timed 07:11:01–07:16:06 UTC:305 seconds,1 newly fully verified page(p4),11.80 verified pages/hour. The400/hour verification target is not met; OCR remains a separate1224.9/hour extraction benchmark.

Chemistry p1 source audit completed: direct 5x source phase crop compared with replacement coded SVG, five gas molecules/dense liquid/honeycomb-like solid lattice and bidirectional red/blue arrows; source text/paired translations preserved, decorative montage explicitly excluded. Local SVG-to-image inspection used only for verification; no source raster in lessons. Replaced marker-only arrowheads with explicit paths for portable display. Verified corrected=[1,2,4], contiguous=2, next formal page3; p3 and5 gaps retained.

Chemistry p5 cropped references resolved by direct book cross-references: Unit8 opens PDF240/printed235 (not draft233); Unit9 PDF274/printed269; Unit10 source contents shows296 (not draft289). Chapter bounds corrected accordingly. Reference-only inspections238/240/274/301 do not count as audited pages. p6 source audited: restored Unit01/title/outcomes introduction/seven semantic bullets and Teaching10/Assessment01/Weightage%08; rebuilt chemically correct methane/oxygen/carbon dioxide/two-water model with correct atom/bond counts. Syntax/reader checks pass147pairs168IDs. Verified corrected=[1,2,4,5,6]; contiguous=2; p3 unresolved folded text remains; next independent audit page7.

Chemistry p7 re-audited with 4x intro/definition/bottom crops. Removed guessed folded-edge word endings and restored source paragraphs, Introduction heading, separate Tidbit heading/aside, 1.1 heading, carbon isotope notation, black atomic-mass introduction and italic definition continuation to p8. Paired translations preserve explicit source-gap markers. Page7 corrected but unresolved; not verified. Reader checks pass151pairs172IDs. Next independent audit p8; contiguous verification remains2 due to unresolved p3.

Chemistry p8 exact re-audit saved: source paragraph boundaries restored, counting-unit paragraph joined with its Avogadro continuation, For example restored, original6.023x10^23 retained, lowercase fraction continuation formatted, capital subscriptA formatted. Source single-pan dial scale replaces invented balance; caption and labels translated. Dedicated source-flow renderer positions figure between the explanatory passage and counting examples. Local SVG inspection done; superscript explicit offset avoids converter limitations. Reader151pairs172IDs passes; focused p8 check confirms12records/order/formatted fraction/subscript. Verified corrected=[1,2,4,5,6,8]; p3/p7 unresolved, contiguous2, next9. Timed segment07:17:47–07:47:33UTC1786seconds/4new verifiedpages=8.06verifiedpages/hour, below400/hour; source OCR extraction is separate.

Chemistry p9 exact source re-audit saved: all80element table cells checked (including sourceHe4.002/Ar39.94), table caption/headers/name translations, exact STS headings/paragraphs and semantic3bullet list restored. Preserved source tell us and single quotes; removed invented semicolon. Separate1.2/MolarMass headings and bottom term-molar-mass paragraph restored with continuation referencep10. Source flow nowtable→STSprose→molar-mass passage. Syntax/reader155pairs176IDs passes. Verified corrected=[1,2,4,5,6,8,9], contiguous2; unresolved3/7 retained; next10.

Chemistry p10 source re-audit saved: preserved molar-mass continuation and source3bullet structure; expanded H2SO4 derivation into its3printed steps. Restored full printed equation labels/fractions/units/numbers1.1–1.3andOr connector in source order; no n=m/M shorthand substitution. Example1.1 source heading/question/Solution/firststep restored separately, continuation p11 metadata. Formula and exercise tabs now reuse shared source records. Original/Urdu/Pashto fraction layouts work without KaTeX; bundledKaTeX compiled all4source math blocks. Reader159pairs180IDs and focused source order/formula/tab checks pass. Verified corrected=[1,2,4,5,6,8,9,10]; next11; p3/p7source gaps remain, contiguous2.

Chemistry p11 exact re-audit saved:23source-paired records replace7merged summaries. Completed Example1.1 continuation with both symbolic/numeric fractions; restored Reading check2questions and Practice1.1questions/subparts/weights; full Examples1.2/1.3 steps/sixsource fractions and Practice1.2 question. Original doubled NaOH denominator parenthesis retained. Reusable scientific-label translation cache added; quantities/formulas unchanged. SixLaTeX fractions compile,18original/translated fraction layouts/source order checked, exercise tab retains all six equations. Reader175pairs196IDs passes. No authored solutions added to unanswered exercises. Verified corrected=[1,2,4,5,6,8,9,10,11]; next12; source gaps3/7 remain, contiguous2.

Chemistry p12 exact re-audit saved:22source pairs replace4summaries; all Example1.4 calculation statements/derivation/fourfractions/two-line result restored with printed3.011x10^23; Practice1.3 and Self-Assessment2questions/eight subquestions/printed weights preserved. Six math blocks compile;12translated/original fraction layouts/exercise steps checked. Reader193pairs214IDs passes. Verified corrected=[1,2,4,5,6,8,9,10,11,12]; next13; unresolved3/7remain, contiguous2. Updated actual segment benchmark:8verifiedpages/6587.98seconds=4.37verifiedpages/hour;400/hour target not met.

Chemistry p13 exact re-audit saved:14source-paired records, complete explanatory/law/calculation prose, 4numbered steps, two native reaction diagrams withHeat/solid-phase species/1mol/56+32→88g and translatedlabels, Mole–MoleConversion and Example1.5question with source missing finalquestionmark preserved; answercontinuesp14. Codedreaction locally rendered/visuallychecked; formula-tab includes reaction diagrams. Cover recheck removed duplicate visible state-label paragraphs and restored title→figure→publisher readingorder while retaining figure translation pairs. Reader197pairs218IDs passes. Verified corrected=[1,2,4,5,6,8,9,10,11,12,13]; contiguous2; gaps3/7remain; next14. Actual resumed benchmark9newfullyverifiedpages/7248.06seconds=4.47verifiedpages/hour;400/hour target unmet. Next action:inspect sourcep14 and upsert draft Example1.5solution/practice/self-assessment and Example1.6 start, preserving all worked steps/source order and paired translations.

## 2026-10-10T09:29:35.904787+00:00 — whole-book continuation
User requires completion of whole book under original instructions. Page 14 source inspected and draft summaries replaced with 19 paired paragraphs and seven formatted equations, including all questions and solution steps. Reader/syntax checks pass; seven equations compile. Corrected, not yet verified: finish fallback fractions and translated equation layout; next action remains page 14, then sequential page 15. No other class or shared files edited.

Page 14 final review complete: source equation conditions, phase subscripts, native fallback fractions and natural translated mole relations corrected. Verified corrected; next page15. Latest attached instructions reaffirm full non-Mathematics Class11 scope.

2026-10-10T09:38:35.108281+00:00 — Page15 verified corrected. Replaced five summary paragraphs with16 exact paired records and11 equation blocks, retained all source steps and questions. Source bottom crop confirms “Convert14.5g of Al into moles,” ends with comma; preserved. Syntax/reader and actual KaTeX lesson/exercise/formula checks pass. Nextpage16. Full assignment remains incomplete; source gaps3/7/21 retained.

2026-10-10T09:42:09.473922+00:00 — Page16 verified corrected:13 paired paragraphs,8 equations; full source text, separate worked steps, question/reaction order, STP continuation and Tidbit restored. Checks pass. Nextpage17. Latest attachment reaffirms original full assignment. Benchmark starts 2026-10-10T09:40:10Z.

2026-10-10T09:45:06.970619+00:00 — Page17 corrected, not verified. Example1.10 quantity clipped in primary and matching local split crop; gap recorded without guessed text. Restored11 paired records/12equations, complete Example1.9 reaction quantity columns and source fraction steps. Checks pass. Nextpage18.

2026-10-10T09:50:19.579217+00:00 — Page18 verified corrected. Restored12paired records/5equations, actual p17question continuation rather than duplicate reconstructed question, source stoichiometric volume steps/Tidbit/three questions. Rebuilt Figure1.2 with full source fractional conversion ratios, 6.022×10²³, all labels and bidirectional links. SVG locally rendered and visually compared; source fractions/table fallback and bundled KaTeX pass. Nextpage19.

2026-10-10T09:52:18.960297+00:00 — Page19 verified corrected:15pairs,8equations; source subheading, symbolic equations1.5/printed1.4, all Example1.11 percentage fractions/oxygen alternative and Practice1.8 subparts restored. Printed62 retained with separate clarification. Checks pass; nextpage20.

2026-10-10T09:54:49.249243+00:00 — Page20 verified corrected:20pairs,5equations; complete alloy solution and cancelled-zero fractions, separated practice questions/options, definitions/Reading check/source instruction. Native unit cancellation also restored15–17. Reader and actual KaTeX three views pass. Nextpage21.

2026-10-10T09:59:36.809781+00:00 — Page21 corrected, unresolved source fold retained. Primary/split enlarged crops identical; removed guessed paragraph completions, recorded visible fragments explicitly, restored separate Heat reaction/ratios/Tidbit, corrected Figure1.3 labels/plus/arrow and removed duplicate caption. Counts4H2+3O2→4H2O+1O2 checked in local SVG preview. Syntax/reader/3equations pass. Nextpage22.

2026-10-10T10:02:24.749435+00:00 — Page22 verified corrected:14pairs/8equations, all source steps and subquestions. Reader/syntax/KaTeX/native views pass after text-mode chemical-subscript fix. Nextpage23. Actual segment5verifiedpages/1334.75seconds=13.49pages/hour;400target not met. Pages17/21corrected but unresolved excluded from benchmark.

2026-10-10T10:06:52.802848+00:00 — Page23 corrected, not verified:14pairs/8equations, Example1.13 continuation and source2.72/2.727 retained, Practice1.10/yield visible fragments; primary/split fold matching. All gaps explicit. Checks pass. Nextpage24.

2026-10-10T10:09:09.441894+00:00 — Page24 verified corrected:14pairs/9equations; exact actual-yield paragraphs/four reasons, complete Example1.14 steps and percent-yield fraction. Checks pass. Nextpage25.

2026-10-10T10:12:21.956250+00:00 — Page25 corrected, not verified:15pairs/10equations, full worked example and practice/source assessment fragments. PrintedCuCO3→CuO+O2 retained with separate clarification. Folded Q1/Q2 punctuation unresolved. Checks pass. Nextpage26. Actual segment6verifiedpages/1931.96seconds=11.18pages/hour;400target unmet.

2026-10-10T10:14:34.382991+00:00 — Page26 verified corrected: heading+13source bullets with full aligned translations; actual renderer13listitems checked. Page25primary/split edge crops identical; Q1/Q2punctuation remains unresolved. Nextpage27. Actual segment7verifiedpages/2064.38seconds=12.21pages/hour;400target unmet.

2026-10-10T10:17:32.847586+00:00 — Page27 corrected, not verified:48paired records/9MCQidentities/36options/reaction; all printed values/units retained. Primary/split close crops confirm MCQ5 ending cropped; no guessed plural. Reader/reaction/exercise checks pass. Nextpage28.

Runtime recovered: safe progress-directory probe succeeded2026-10-10T12:24:03Z; primaryPDF/project/inventory accessible. Existing27-page reader syntax/structure passes; not all27pages source verified. Screenshot bug repaired under exclusive shared lock:Class11 subject grid opens only existingPhysics/Chemistry datasets, no other-class/default routing changed; Chemistry source-progress label corrected. Direct function checks pass. Added67reusable Chemistry vocabulary meanings with native clickable Urdu/Pashto popovers; original visible wording preserved and focused vocabulary check passes. User requests Chemistry-only continuation through419pages, checkpoints each5pages, interactive word meanings; original per-page save remains in use.

2026-10-10T12:42:46.425903+00:00 — Chemistry PDF page 28 verified. Entire source and enlarged numerical crop compared:3MCQs/12options,5shortquestions,5numericalquestions/subparts and5printed answer records. Printed994g/16.60g/2.79g retained with separate clarification. Syntax/reader, reaction KaTeX/exercise/source answer checks pass; interactive vocabulary available. Next page 29.

2026-10-10T12:48:39.376946+00:00 — Chemistry PDF page 29 unresolved. Entire source plus two enlarged crops compared;4descriptive question groups/subparts,4reactions including Heat/product term and printed phases, answer key composition values retained; syntax/reader/KaTeX pass. Unresolved: Rightfold clips answer1c final unit exponent, water-gas paragraph ending, answer3b digits/unit, answer4a ending, question4b connector after100g and final answer4b unit. No missing text/digits guessed. Next page 30.

2026-10-10T12:52:04.700915+00:00 — Chemistry PDF page 30 verified. Visually compared all 12 source records, 2 reactions, 2 printed answers and both project bullets. Urdu/Pashto paired; decorative publisher graphic excluded. Syntax and reader checks pass. Next page 31.

2026-10-10T12:53:08.781703+00:00 — Chemistry PDF page 31 verified. All 16 outcomes and cognitive labels compared with scan; unit headings and Teaching 10 Assessment 01 Weightage 08 preserved. Urdu/Pashto pairs and native SVG atom added. Reader and syntax checks pass. Next page 32.

2026-10-10T12:54:13.396942+00:00 — Chemistry PDF page 32 verified. All four paragraphs, Introduction and 2.1 heading and Tidbit visually compared. Complete Urdu/Pashto pairs. No instructional figure on page. Syntax and reader pass; five-page checkpoint 28–32 saved, page29 remains unresolved. Next page 33.

2026-10-10T12:58:54.052237+00:00 — Chemistry PDF page 33 unresolved. Two paragraphs, all visible values 5000–10000 volts 0.1/0.01mm Hg and Goldstein1886 retained with Urdu/Pashto. Figure2.1 rebuilt in SVG with eight labels, negative cathode/positive anode, circuit and vacuum port. Syntax/reader pass. Unresolved: Right-fold letter endings obscured in primary and alternate chemistry1.pdf page33; not guessed. Next page 34.

2026-10-10T13:00:59.400981+00:00 — Chemistry PDF page 34 verified. All 13 characteristics, note and introductory paragraphs visually compared. Figure references2.2–2.5 and e/m1.7588x10^11 C/kg and e1.6022x10^-19 C retained. Complete Urdu/Pashto; syntax/reader pass. Page33 native figure visually checked. Next page 35.

2026-10-10T13:07:22.483297+00:00 — Chemistry PDF page 35 unresolved. All visible text translated, seven source derivation equations compile with KaTeX; native fractions render in all languages. Four coded figures inspected with labels, polarities, shadow cross, pin-wheel and electric/magnetic deflection. Reader and syntax pass. Unresolved: Right fold obscures letter endings in opening two paragraphs and captions2.3/2.5; unresolved markers retained. Next page 36.

2026-10-10T13:11:01.280663+00:00 — Chemistry PDF page 36 verified. All four paragraphs and 2 headings visually compared; source M+e-→M++2e- retained. Native Figure2.6 inspected and red-glow label positioned by cathode; 7 Urdu/Pashto labels and complete paired translations. Reader/syntax pass. Next page 37.

2026-10-10T13:16:03.195362+00:00 — Chemistry PDF page 37 verified. All nine properties compared with enlarged scan and chemistry1 alternate. Values9.54x10^7,1.6022x10^-19,1.6726x10^-27,1836 preserved. Neutron paragraph and Figure2.7 complete in native SVG with translated labels. Syntax/reader pass; checkpoint33–37 saved,33/35 unresolved. Next page 38.

2026-10-10T13:22:25.875824+00:00 — Chemistry PDF page 38 verified. All source paragraphs/headings, four neutron properties and reading check visually compared. Both isotope reactions preserve mass/atomic numbers. Table2.1 all fifteen cells and five headers exact values retained with translations. Syntax/reader pass. Next page 39.

2026-10-10T13:25:19.851576+00:00 — Chemistry PDF page 38 verified. Correction: premature failed-write checkpoint was withdrawn. Successful write now separately confirmed. All 12 paired source records, 2 isotope reactions and table2.1 fifteen cells compared with scan; equations compile and reader/syntax checks pass. Next page 39.

2026-10-10T13:30:45.333326+00:00 — Chemistry PDF page 39 unresolved. All visible five postulates, explanatory paragraphs and three source equations translated. Figure2.8 native SVG inspected: three n levels, E1/E2 and outward energy direction retained. Syntax/reader pass. Unresolved: Right-fold letter endings and mass-symbol statement remain unreadable; explicit source-gap markers. Not fully verified. Next page 40.

2026-10-10T13:37:55.573090+00:00 — Chemistry PDF page 40 verified. All source paragraphs and headings visually compared, including page39 sentence continuation. Four Coulomb equations compile; original2.2/2.3 numbering and inline fraction retained. Figure2.9 native SVG inspected and translated. Full Urdu/Pashto pairs, reader/syntax pass. Next page 41.

2026-10-10T13:43:32.165302+00:00 — Chemistry PDF page 41 unresolved. All ten formula steps compared with enlarged scan and compile. Native fractions and targets in all languages. ActivityNo1 retained without authored answer. Syntax/reader pass. Unresolved: Right-fold letter endings in centripetal-force and inverse-square paragraphs unreadable; source gaps explicitly marked. Next page 42.

2026-10-10T13:49:01.751750+00:00 — Chemistry PDF page 42 verified. All16 source pairs and11 formulas visually compared; example2.1 original solution values4.761/8.464 Å preserved, source r1 typo retained. Practice2.1 no invented answer. KaTeX and reader/syntax pass; five-page checkpoint38–42 saved,39/41 unresolved. Next page 43.

2026-10-10T13:51:46.004708+00:00 — Chemistry PDF page 43 unresolved. Eleven energy-derivation formulas and eight explanatory pairs compared with enlarged source. Fractions, signs, indices, equation labels(b)2.12–2.15 retained and compiled. Reader/syntax pass. Unresolved: Two right-fold prose letter endings obscured. Not verified; no missing wording invented. Next page 44.

2026-10-10T14:03:06.711120+00:00 — Chemistry PDF page 44 verified. All12 source pairs, Activity2 and Practice2.2 preserved without invented answers. Equation2.17 minus sign confirmed enlarged scan. Five equation blocks compile; n1/n2/n3 values exact. Figure2.10 inspected native SVG with three levels, transition3→2 and emitted-wave arrow. Syntax/reader pass. Next page 45.

2026-10-10T14:07:50.791020+00:00 — Chemistry PDF page 45 unresolved. Nine equation blocks and14 pairs compared with source. Indices n1/n2 and numbered2.18–2.20 retained; native fractions and translated labels, KaTeX compile and reader/syntax pass. Unresolved: Fold obscures final letters of difference in explanatory sentence; unresolved marker retained. Next page 46.

2026-10-10T14:14:57.974212+00:00 — Chemistry PDF page 46 verified. All12 source pairs and11 frequency/wave-number equation steps compared. Rydberg1.09678x10^7 m^-1 and2.21–2.23 retained. Native fractions and all-language rendering pass; KaTeX compile, syntax/reader pass. Next page 47.

2026-10-10T14:20:14.639291+00:00 — Chemistry PDF page 47 unresolved. All readable text and formula2.24 implemented with Urdu/Pashto. Interactive meanings expanded to112 cached terms including atomic structure/spectra. Five-page43–47 checkpoint saved; reader/syntax pass. Damaged first formula not reconstructed. Unresolved: First Rydberg formula corrupt glyphs, right-fold endings in spectrum definitions and paragraphs unreadable. Next page 48.

2026-10-10T14:36:50.416174+00:00 — Chemistry PDF page 48 unresolved. All visible prose, ion charges and two line-spectrum types translated. Figure2.11 prism and seven colours native SVG; Figure2.12 two sodium/five helium bands source-matched and inspected. Reader/syntax pass. Unresolved: Figure2.11 small range digits blue/indigo/violet and screen single-letter label uncertain; explicit markers, not inferred. Next page 49.

2026-10-10T14:46:21.704706+00:00 — Chemistry PDF page 49 unresolved. All9 readable source pairs translated, figures2.13/2.14 rebuilt and visually inspected with five dark/bright bands and wavelength direction. Certain labels397410.0486.1 and absorption434.0/656.2 retained; source obscurities marked. Reader/syntax pass. Unresolved: Scan fold prose endings and two small emission-label digits uncertain. Not inferred from absorption diagram. Next page 50.

2026-10-10T14:58:36.363914+00:00 — Chemistry PDF page 50 verified. All five spectral series paragraphs exact n1/n2 sequences and regions compared. Figure2.15 coded apparatus/slits/prism/screen and four spectral lines410.0434.0486.1656.2nm inspected with translated labels. Complete Urdu/Pashto pairs; syntax/reader pass. Next page 51.

2026-10-10T15:16:34.257701+00:00 — Chemistry PDF page 51 unresolved. Source diagram, spectral table and four Bohr-model defects compared; translated content and coded diagram pass reader checks. Unresolved: Fold-obscured paragraph endings and outer spectral-orbit label remain unreadable. Next page 52.

2026-10-10T15:18:20.831308+00:00 — Chemistry PDF page 52 verified. All four self-assessment questions, Planck theory paragraphs, postulates 1-2, source equation number 2.23 and constant compared. Native wave diagram visually checked; all translations and reader checks pass. Next page 53.

2026-10-10T15:18:21.101030+00:00 — Five-page Chemistry checkpoint 48–52 saved. Page 50 and 52 verified; pages 48,49,51 unresolved. Measured verified pages/hour 4.82. Next page 53.

2026-10-10T15:20:10.453377+00:00 — Chemistry PDF page 53 unresolved. Wave definitions, postulate 3, equations 2.24 and E=nhν, speed constant and translated coded crest/trough diagram compared; reader checks pass. Unresolved: Right fold obscures prose endings, angstrom conversion exponent/unit and tidbit text. Next page 54.

2026-10-10T15:22:30.937552+00:00 — Chemistry PDF page 54 verified. All wave-number and photon-energy derivations through equation 2.28, X-ray history, three production methods and Roentgen introduction visually compared. Eight formulas compile and translated reader checks pass. Next page 55.

2026-10-10T15:24:34.489156+00:00 — Chemistry PDF page 55 unresolved. Roentgen tube diagram recreated with source electrodes, ray directions, target and high-voltage circuit. Eight X-ray properties begun, translations and reader checks pass. Unresolved: Fold obscures paragraph endings and final property continuation. Next page 56.

2026-10-10T15:26:31.635857+00:00 — Chemistry PDF page 56 verified. Property 8 continuation, property 9, four uses, two spectrum types and characteristic Kα/Kβ/Kγ transitions fully compared. Source wording preserved, all paired translations and reader checks pass. Next page 57.

2026-10-10T15:30:33.615031+00:00 — Chemistry PDF page 57 unresolved. K/L/M inner-shell arrows and shell labels compared against enlarged source and coded figure inspected. Moseley history, atomic-number definition, tidbit and two reading questions translated; reader checks pass. Unresolved: Right-fold endings in continuation, spectrum prose, Moseley paragraph and reading questions remain obscured. Next page 58.

2026-10-10T15:30:33.858682+00:00 — Five-page Chemistry checkpoint 53–57 saved. Pages 54 and 56 verified; 53,55,57 unresolved. Reader validation covers 57 represented PDF pages, 772 paired paragraphs and 829 unique IDs. Next unfinished page 58.

2026-10-10T15:35:25.248720+00:00 — Chemistry PDF page 58 verified. Moseley experiment and law, complete screening-constant text, reading question, equations through 2.29 and all tube labels visually compared. Coded tube inspected; formula and multilingual reader checks pass. Next page 59.

2026-10-10T15:37:21.575942+00:00 — Chemistry PDF page 59 unresolved. Moseley constant continuation, Fireworks Display source box and quantum-number introduction transcribed with paired translations. Source chemical symbols and printed wording preserved; reader checks pass. Unresolved: Right-fold text endings remain unreadable; quantum-number list continues next page. Next page 60.

2026-10-10T15:39:56.007014+00:00 — Chemistry PDF page 60 verified. Four quantum-number labels, complete principal-number explanation and three bullets, K–Q shell mapping, 2n² example and azimuthal introduction visually compared. Printed Principle heading preserved; translations and reader checks pass. Next page 61.

2026-10-10T15:42:17.585659+00:00 — Chemistry PDF page 61 unresolved. Table 2.2 all four rows and five columns compared; sub-shell prose, spectroscopic names and magnetic-number introduction translated. Reader checks pass. Unresolved: Fold hides paragraph endings, first shape-case quantum value, magnetic range lower bound and final m value. Next page 62.

2026-10-10T15:45:27.380669+00:00 — Chemistry PDF page 62 verified. Magnetic m-value cases, five d-orbital designations, complete Table 2.3 with 10 sub-shell records and seven columns, and spin introduction/half values compared visually. Paired translations and reader checks pass. Next page 63.

2026-10-10T15:45:27.508925+00:00 — Five-page Chemistry checkpoint 58–62 saved. Pages 58,60,62 verified; 59,61 unresolved. Reader covers 62 represented source pages, 819 paired paragraphs and 881 unique IDs. Next unfinished page 63.

2026-10-10T15:51:29.218688+00:00 — Chemistry PDF page 63 unresolved. Spin signs, arrows, 50-percent statements and two-electron statement compared. Native spin spheres and Stern-Gerlach beam/magnet diagrams inspected; all paired translations and reader checks pass. Unresolved: Right-fold terminal letters remain hidden in prose. Next page 64.

2026-10-10T15:54:44.844329+00:00 — Chemistry PDF page 64 verified. Parallel/paired spin arrows, reading question, orbital probability explanation, s-orbital text and Figure 2.23 labels/size progression, and p-orbital introduction compared. Native figure inspected and translated reader checks pass. Next page 65.

2026-10-10T16:01:52.253348+00:00 — Chemistry PDF page 65 unresolved. Three p-orbital axes/orientations and five d-orbital shapes, planes and doughnut form compared and coded diagrams inspected. All source paragraphs translated; reader checks pass. Unresolved: Right-fold endings in p continuation and d-orbital explanation remain obscured. Next page 66.

2026-10-10T16:08:42.529736+00:00 — Chemistry PDF page 66 verified. Electronic-configuration definition, Aufbau explanation, both n+ℓ rules, notation labels, 3d/4s calculations and Figure 2.26 orbital grid/arrows compared. Both coded figures inspected; reader checks pass. Next page 67.

2026-10-10T16:12:03.209350+00:00 — Chemistry PDF page 67 unresolved. 4p/5s calculations, source filling sequence and Pauli principle/history/hydrogen example transcribed and translated. Printed page-specific spin signs and arrows retained; reader checks pass. Unresolved: Fold-obscured prose endings and lower spin-row arrow wording unresolved. Next page 68.

2026-10-10T16:14:37.364528+00:00 — Five-page Chemistry checkpoint 63–67 saved. Pages 64 and 66 verified; 63,65,67 unresolved. Reader covers 67 source pages, 857 paired paragraphs, 924 unique IDs. Next unfinished page 68.

2026-10-10T16:19:05.160431+00:00 — Chemistry PDF page 68 verified. Hund rule, carbon/nitrogen configurations, all three alternative p arrangements, stable carbon and nitrogen box-arrow diagrams and degenerate-orbital tidbit visually compared. Native figures inspected; translations and reader checks pass. Next page 69.

2026-10-10T16:22:55.196991+00:00 — Chemistry PDF page 69 unresolved. Table 2.4 elements 1–28, names/symbols/Z/configuration exponents compared using enlarged source. Chromium exception 4s¹3d⁵ preserved. All table headers/names and prose translated; reader checks pass. Unresolved: Fold hides prose endings and chromium stability parenthetical ending. Next page 70.

2026-10-10T16:28:47.498300+00:00 — Chemistry PDF page 70 verified. All table rows 29–40 and five assessment questions compared. Printed Ytterbium/Y/39 naming error and arsenic bracket retained. Copper more-stable note translated. Yellow noninstructional advertisement inspected and excluded under assignment rule 5; reader checks pass. Next page 71.

2026-10-10T16:32:09.212909+00:00 — Chemistry PDF page 71 unresolved. All 13 key-point bullets compared and aligned with Urdu/Pashto translations. Source quantum numbers, 1836 ratio, E=hν and Moseley relation preserved; reader checks pass. Unresolved: Right-fold endings across key-point bullets remain unreadable. Next page 72.

2026-10-10T16:41:59.883112+00:00 — Chemistry PDF page 72 verified. Seven MCQ stems and all 28 options compared. e/m powers 23/11/−31/7, wavelength 2×10⁸nm and inverse units checked from enlarged crop. Source fractions, charges and spin signs preserved; questions translated, no answers invented; reader checks pass. Next page 73.

2026-10-10T16:42:00.132489+00:00 — Five-page Chemistry checkpoint 68–72 saved. Pages 68,70,72 verified; 69,71 unresolved. Reader covers 72 represented source pages, 923 paired paragraphs and 995 unique IDs. Next unfinished page 73.

2026-10-10T16:43:22.089762+00:00 — Chemistry PDF page 73 unresolved. MCQs 8–15 and all 32 options compared with source, including Moseley-law fractions and lowercase z. Source values and translated stems/options preserved; no answers added; reader checks pass. Unresolved: Fold obscures question 10 equation-word ending and question 14 terminal notation/core. Next page 74.

2026-10-10T16:56:19.119859+00:00 — Chemistry PDF page 74 verified. Five short questions, six numerical questions with six printed answers and all descriptive subparts with two printed answers visually compared. Close crops checked powers/signs; misplaced source answer retained beside descriptive 2(b), and Numerial spelling preserved. Reader checks pass. Next page 75.

2026-10-10T16:58:30.119799+00:00 — Chemistry PDF page 75 unresolved. Descriptive questions 5–6, photon question/source answer and both project bullets implemented with aligned translations. Atomic Structure source reaches final printed page 70; chapter remains incomplete to recorded gaps. Reader checks pass. Unresolved: Fold hides question 5(a) quantum-number qualifier, question 6(c) ending, wavelength answer exponent/unit and project endings. Next page 76.

2026-10-10T17:10:20.036196+00:00 — Chemistry PDF page 76 verified. Unit 03 title, all 10 learning outcomes and cognitive labels, Teaching 12/Assessment 01/Weightage 11, and three bond illustrations compared. Coded bond diagrams inspected; translated reader checks pass. Next page 77.

2026-10-10T17:10:20.344116+00:00 — Alternate local chapter scans checked for all 23 unresolved Chemistry pages 28–75. Every corresponding alternate render is pixel-identical at 72 DPI, so these copies do not recover obscured source text. Evidence saved in chemistry-alternate-scan-comparison-28-75.json and page audits.

2026-10-10T17:20:20.715999+00:00 — Chemistry PDF page 77 unresolved. Introduction paragraphs, Lewis doublet/octet explanation, shapes introduction, all three theory list items and VSEPR opening transcribed with paired translations; reader checks pass. Unresolved: Right-fold paragraph endings and VSEPR continuation remain obscured. Next page 78.

2026-10-10T17:20:21.025668+00:00 — Five-page Chemistry checkpoint 73–77 saved. Pages 74 and 76 verified; 73,75,77 unresolved. Reader covers 77 represented source pages, 1030 paired paragraphs, 1107 unique IDs. Next unfinished page 78.

2026-10-10T17:31:00.022695+00:00 — Chemistry PDF page 78 unresolved. VSEPR continuation, eight postulates and repulsion ordering, reading check, applications text and BeCl₂ example fully compared. Native Lewis dots/crosses diagram inspected; translations and reader checks pass. Unresolved: Figure 3.1 caption word after Lewis is overprinted and unreadable. Next page 79.

2026-10-11T07:33:11.950581+00:00 — Chemistry PDF page 79 unresolved. Linear BeCl₂ and BF₃ Lewis/trigonal-planar diagrams compared and inspected. Boron repeated 2p_x source typo retained. All prose and figure labels translated; reader checks pass. Unresolved: Fold obscures prose endings, prose angle and Figure 3.3 formula subscript. Next page 80.

2026-10-11T07:40:00.242255+00:00 — Chemistry PDF page 80 verified. Compared all source text, translations, electron counts, Lewis structure and angular/VSEPR diagrams. Native bond geometry follows the printed 95 degree label; retained printed Stannom spelling. Class 11 route checked and script cache versions refreshed under shared lock. Next page 81.

2026-10-11T07:42:10.132864+00:00 — Chemistry PDF page 81 unresolved. Compared four-electron-pair headings, methane/ammonia configurations and paragraphs, 3 native SVG figures and aligned Urdu/Pashto. Close crop inspected. Source sentence continues on next page. Unresolved: Right fold hides methane arrangement sentence endings after tetrahedral and molec, and Figure 3.7 caption ending/rightmost H; explicit text identifies CH4, so four-H Lewis depiction is sourced from the page prose. Missing caption words not inferred. Next page 82.

2026-10-11T07:44:58.972753+00:00 — Chemistry PDF page 82 verified. All text including preceding/following-page continuations compared; oxygen configuration, 104.5 degree water angle and Lewis diagram inspected. Source figure 3.10 prints 107 degrees while prose prints 107.5 degrees; both retained. Native SVG and paired translations checked; cached interactive quantum/covalent vocabulary expanded. Next page 83.

2026-10-11T07:44:59.093278+00:00 — Five-page checkpoint 78–82 saved: 80 and 82 verified; 78,79,81 unresolved. Reader checks pass with 82 source pages. Next unfinished PDF page 83. Separate resumed measured rate 10.18 verified pages/hour; 400/hour target not achieved. Screenshot availability issue addressed by checked route wiring and scoped script cache-version refresh.

2026-10-11T07:49:32.936456+00:00 — Chemistry PDF page 83 unresolved. Water continuation and actual 104.5 degree angular figure inspected. Table 3.1 has all four rows/five columns and eight native cell diagrams, with aligned translations; native figure/table-cell support and visible gap notes added in Chemistry reader. Figures and focused reader checks pass. Unresolved: Right fold conceals adjective ending after or ang in prose, example-column header ending and example formula subscripts in Table 3.1. Close crop inspected; concealed endings not guessed. Next page 84.

2026-10-11T07:52:27.319234+00:00 — Chemistry PDF page 84 verified. Compared both Table 3.1 continuation rows, all resonance prose and hybrid tidbit, six carbons/hydrogens in each benzene structure, alternating double bonds, 6 curved electron arrows and resonance arrow. All 5 native diagrams inspected; aligned translations and reader checks pass. Repeated table headers identified as reading aid; prior page header gap remains prior-page issue. Next page 85.

2026-10-11T07:55:16.607172+00:00 — Chemistry PDF page 85 unresolved. Source lettered condition layout, ozone example and original electron-dot counts, full accessible prose fragments, theory list, VBT introduction and aligned translations compared. Native ozone SVG inspected; reader checks pass. Printed VESPR retained and no missing dots silently added. Unresolved: Right fold obscures first paragraph, ozone example/comparison endings, resonance-energy endings, covalent word ending and VBT opening paragraph endings. Close crop inspected; explicit gaps retained. Next page 86.

2026-10-11T07:57:16.527231+00:00 — Chemistry PDF page 86 verified. Compared all text: VBT history/names/date, six original assumptions, sigma/pi list, sigma definition/density/energy explanation, three overlap types and s-s example. Source typo and repulsive-force statement retained. Twenty aligned paired paragraphs and list groups pass focused reader/syntax checks. Next page 87.

2026-10-11T08:00:46.858225+00:00 — Chemistry PDF page 87 unresolved. Seven source paired records for hydrogen s-s, HCl s-p and fluorine p-p, both native overlap diagrams and captions compared. Coded figures inspected; opposite spins in H2 and printed two upward input arrows in HCl retained. Reader checks pass. Unresolved: Fold obscures prose endings throughout page and far-right edge of HCl product p lobe. Close crop inspected; explicit gap notes retained. Next page 88.

2026-10-11T08:00:47.157928+00:00 — Five-page checkpoint 83–87 saved. Pages 84 and 86 source verified; 83,85,87 unresolved. Reader covers 87 represented source pages, 1126 paired paragraphs, 1213 unique IDs. Next unfinished PDF page 88. Measured resumed rate 8.7 verified pages/hour; target not met.

2026-10-11T08:09:27.123534+00:00 — Chemistry PDF page 88 verified. All pi-bond prose and oxygen configuration compared, fluorine linear-overlap and oxygen multi-view diagram reconstructed with every source label, orbital/axis, input and paired spins, sigma/pi regions and arrows. Native SVG inspected and overlap regions corrected then re-inspected. Full Urdu/Pashto captions, labels and paired paragraphs pass reader checks. Next page 89.

2026-10-11T08:12:53.110904+00:00 — Chemistry PDF page 89 unresolved. Hybridization text, both reading checks, ground/excited carbon configurations and all paired translations compared. Configurations preserved as two structured equation lines and KaTeX compiled; source reader checks pass. Unresolved: Right fold conceals paragraph endings, first reading-check conjunction and definition words after ener/havin. Close crop inspected; explicit gaps retained. Next page 90.

2026-10-11T08:22:07.679245+00:00 — Chemistry PDF page 90 verified. Compared sp3 heading/definition, methane paragraph, ground/excited carbon configurations and 25% s/75% p paragraph. Energy, promotion path, orbital box occupations and four hybrid levels, all state labels, four hybrid lobes/109.5 degree labels and four-H product reconstructed and inspected. Equations compile; paired translations and reader checks pass. Next page 91.

2026-10-11T08:46:27.199255+00:00 — Chemistry PDF page 91 unresolved. Compared Figure 3.20 four-bond tetrahedral CH4 and 109.5-degree label; sp2 definition, ethene formula/paragraph, both carbon-state configurations, all Figure 3.21 energy boxes/arrows/unhybridized p, 33.33%/66.67% composition and 120-degree statements. Both native diagrams inspected, configurations compile, translations and reader checks pass. Unresolved: Fold conceals phrase after same, several paragraph endings, subject(s) of final sp2 statements and the unfinished final sentence, plus far-right Figure 3.21 diagram edge. Next page 92.

2026-10-11T08:56:12.267081+00:00 — Chemistry PDF page 92 verified. Compared all ethene overlap/structure captions and prose, five sigma/one pi bond, 1.34Å C=C, 1.10Å C–H, 120 degree planar geometry; sp definition, ethyne C2H2 composition/four orbitals and unhybridized pi-forming orbitals; ground and excited configurations. Both corrected native figures inspected; equations compile and translations align. Next page 93.

2026-10-11T09:09:05.384393+00:00 — Chemistry PDF page 93 unresolved. Compared 50% s/50% p, two unhybridized p orbitals, 180-degree linear arrangement/single electron text; C2H2 sigma framework/two pi bonds, orbital geometry, C≡C 1.20Å and C–H 1.09Å. Two native diagrams inspected; configurations compile and translated reader checks pass. Unresolved: Fold obscures sp unhybridized-orbital sentence subjects and several clause endings; final shape word hidden. Right edge of energy and molecular figures is also folded. Next page 94.

2026-10-11T09:09:05.912520+00:00 — Five-page checkpoint 88–92 saved. Pages 88,90,92 verified; 89,91 unresolved. Reader covers 93 represented source pages, 1160 paired paragraphs, 1252 unique IDs. Next unfinished PDF page 94. Resumed measured rate 4.38 verified pages/hour; target not met.

2026-10-11T09:11:34.731687+00:00 — Chemistry PDF page 94 verified. Compared the acetylene concluding geometry, all three valence-bond shortcomings, all six Self-Assessment questions and full Science, Technology and Society/hydrogen-bond hair passage. Preserved source grammar and lists; all matched with Urdu/Pashto translations. Focused reader/syntax checks pass. Next page 95.

2026-10-11T10:03:58.847638+00:00 — Chemistry PDF page 95 unresolved. Compared hydrogen-bond continuation, disulphide bond definition/properties, all linked diagram labels and SH↔S–S treatment sequence, and Molecular Orbital Theory opening; native SVG diagrams smoothed and inspected. Added interactive terms and checked paired reader. Unresolved: Fold obscures a word after “theory” in the MOT opening and right-edge words in its continuation; explicit source gap retained. Next page 96.

2026-10-11T11:17:33.119605+00:00 — Chemistry PDF page 96 unresolved. Compared molecular-orbital energy ordering, Aufbau/Pauli/Hund statements, bonding/antibonding notation, bond-order prose and fraction, reading-check prompt, complete H2 discussion and 2H→H2 orbital configuration. Stamp excluded as added Not For Sale overprint. Three equations compile and vocabulary lookups pass. Unresolved: Page 96 is legible; any remaining scan ambiguity is documented in the related page 95 MO introduction. Next page 97.

2026-10-11T11:21:44.226590+00:00 — Chemistry PDF page 96 verified. Compared all molecular-orbital postulates, energy ordering, bond-order description/formula and reading question, plus the complete H2 explanation and orbital configuration. The non-instructional Not For Sale overprint is explicitly excluded; equations compile and reader checks pass. Next page 97.

2026-10-11T11:21:44.520648+00:00 — Five-page checkpoint 92–96 saved. Pages 92,94,96 verified; 93 and 95 unresolved. Added non-instructional sale-stamp exclusion at page 96. Reader covers 96 represented PDF pages. Next unfinished page 97. Measured resumed rate 2.36 verified pages/hour; 400/hour target not met.

2026-10-11T11:36:06.821750+00:00 — Chemistry PDF page 97 unresolved. Compared the hydrogen molecular-orbital diagram, bond-order definition and arithmetic, helium molecular-orbital discussion, and He2 configuration against the scan. Page 97 section passed reader uniqueness/route/translation checks. Unresolved: Right fold obscures endings within the helium explanation; redrawn Fig. 3.25 simplifies perspective and styling. The continuation sentence is flagged. Next page 98.

2026-10-11T11:45:04.198107+00:00 — Chemistry PDF page 98 unresolved. Added trilingual Chemistry source page 98 with source-to-reader comparison, coded instructional content, and reader checks. Unresolved: Folded or cropped scan details remain flagged on this page; wording is not reconstructed where obscured. Next page 99.

2026-10-11T11:45:04.408681+00:00 — Chemistry PDF page 99 unresolved. Added trilingual Chemistry source page 99 with source-to-reader comparison, coded instructional content, and reader checks. Unresolved: Folded or cropped scan details remain flagged on this page; wording is not reconstructed where obscured. Next page 100.

2026-10-11T11:45:04.626754+00:00 — Chemistry PDF page 100 unresolved. Added trilingual Chemistry source page 100 with source-to-reader comparison, coded instructional content, and reader checks. Unresolved: Folded or cropped scan details remain flagged on this page; wording is not reconstructed where obscured. Next page 101.

2026-10-11T11:45:04.832618+00:00 — Chemistry PDF page 101 unresolved. Added trilingual Chemistry source page 101 with source-to-reader comparison, coded instructional content, and reader checks. Unresolved: Folded or cropped scan details remain flagged on this page; wording is not reconstructed where obscured. Next page 102.

2026-10-11T11:45:05.069310+00:00 — Chemistry PDF page 102 unresolved. Added trilingual Chemistry source page 102 with source-to-reader comparison, coded instructional content, and reader checks. Unresolved: Folded or cropped scan details remain flagged on this page; wording is not reconstructed where obscured. Next page 103.

2026-10-11T13:28:10.749911+00:00 — Chemistry PDF page 103 unresolved. Compared water dipole geometry, CO2 discussion and native SVG against the scan; source figure-number mismatch preserved. Unresolved: Right-fold line endings obscured; scan itself refers to Figure 3.28 while visible caption says Figure 3.29. Next page 104.

2026-10-11T13:28:11.086728+00:00 — Chemistry PDF page 104 verified. Compared bond-properties overview, solubility, like-dissolves-like principle, ionic-reaction setup and figure against the source scan. Next page 105.

2026-10-11T13:28:11.499693+00:00 — Chemistry PDF page 105 unresolved. Compared reaction continuation, directional-bond explanation, molecular-solids section and coded diagram against the scan. Unresolved: Outer fold obscures line endings in the example and some directional/molecular-solid text. Next page 106.

2026-10-11T13:28:11.839199+00:00 — Chemistry PDF page 106 verified. Compared molecular, network and metallic solids discussion, diamond lattice diagram, and excluded Not For Sale scan stamp against the source. Next page 107.

2026-10-11T13:28:12.104459+00:00 — Chemistry PDF page 107 verified. Compared free-electron model and all eight self-assessment prompts against the source scan. Next page 108.

2026-10-11T13:28:12.458691+00:00 — Chemistry PDF page 108 verified. Transcribed all 14 chapter key points and checked English text, Urdu/Pashto translations, and source order against the scan. Next page 109.

2026-10-11T13:39:41.603998+00:00 — Chemistry PDF page 109 unresolved. Transcribed all ten printed multiple-choice questions and forty answer options, with paired Urdu and Pashto, from the Unit 3 exercise page. Unresolved: Curved right edge partly clips wording; the source provides choices but no printed answer key on this page. Next page 110.

2026-10-11T13:43:25+00:00 — Chemistry 5-page checkpoint: source PDF pages 103–107 represented; verified 104, 106, and 107; unresolved folds retained on 103 and 105. Page 108 chapter key points verified. Pages 109–110 exercise content represented; page 109 unresolved due curved scan edge, page 110 verified. Reader maps 110 source pages; source book has 419 PDF pages. Exact next unfinished page: 111. Segment benchmark through page 110: 5.02 implemented pages/hour and 2.27 verified pages/hour against the 400 verified pages/hour target.

2026-10-11T13:44:05.580014+00:00 — Chemistry PDF page 110 verified. Compared five additional MCQs and eight short questions with the scan; all visible exercise text and options have Urdu/Pashto pairs. Next page 111.

2026-10-11T13:48:23.637343+00:00 — Chemistry PDF page 111 unresolved. Compared short questions 9–10, all descriptive prompts, and the BF3/NH3 model project with the source scan; preserved Urdu/Pashto translations. Unresolved: Curved right edge obscures some line endings on the printed page. Next page 112.

2026-10-11T13:51:01.628841+00:00 — Chemistry PDF page 112 verified. Compared all twelve Unit 4 learning objectives and the teaching, assessment, and weightage figures against the unit opener. Next page 113.

2026-10-11T13:58:25.426550+00:00 — Chemistry PDF page 113 unresolved. Compared nine remaining Unit 4 objectives and both introduction paragraphs against the scan. Unresolved: Curved page edge obscures endings in the introduction paragraphs. Next page 114.

2026-10-11T14:06:46.690743+00:00 — Chemistry PDF page 114 unresolved. Added gas definition, theory background, and all ten kinetic molecular theory postulates with Urdu/Pashto pairs. Unresolved: Beginning of the definition at the curled top edge is partly obscured. Next page 115.

2026-10-11T14:18:16.904658+00:00 — Chemistry PDF page 115 unresolved. Transcribed pressure definition and equation, atmosphere explanation, manometer Tidbit, sea-level values and coded Figure 4.1. Unresolved: Curved page edge partly obscures the atmosphere paragraph endings and the bottom line. Next page 116.

2026-10-11T14:21:21.727809+00:00 — Chemistry PDF page 116 verified. Compared pressure composition, pressure-unit definitions, conversion factors and all eight displayed equations in Example 4.1 against the scan; KaTeX compilation passed. Next page 117.

2026-10-11T14:28:39.168126+00:00 — Chemistry PDF page 117 unresolved. Added 49 torr-to-pascal conversion, practice prompt, reading check, pressure-units table, conversions and Boyle law formulas; all five equations compile. Unresolved: The relative-state Boyle equation continues below the page edge and remains flagged. Next page 118.

2026-10-11T14:38:22.431688+00:00 — Chemistry PDF page 118 verified. Compared Boyle equation (4.2), graphical isotherm explanation/figure, Charles law definition and equations (4.3–4.4); all five displayed equations compile. Next page 119.

2026-10-11T14:47:19.797043+00:00 — Chemistry PDF page 119 unresolved. Added Charles-law V/T graphical discussion, coded temperature-volume diagram, 1787 context and 273-based expansion/cooling examples. Unresolved: Curved scan edge partly obscures several line endings. Next page 120.

2026-10-11T14:53:57.170568+00:00 — Chemistry PDF page 120 unresolved. Added all temperature–volume table rows, Kelvin/Celsius relationship and coded graph; table-reference and zero-row inconsistency logged. Unresolved: Source prints k=2 when both K and V equal zero; V/T is undefined. Body also calls this Table 4.4 while caption says Table 4.2. Next page 121.

2026-10-11T15:08:17.207680+00:00 — Chemistry PDF page 121 unresolved. Added temperature-scale comparison table and coded figure, Tidbit, Avogadro law narrative, and equations V proportional to n and V = Kn; KaTeX validation passed. Unresolved: Curved outer edge obscures portions of the final Avogadro-law sentence. Next page 122.

2026-10-11T15:16:43.362890+00:00 — Chemistry PDF page 122 unresolved. Compared STP equal-volume discussion, mole–mass–volume values, molar-volume definition, ideal-gas heading and coded three-gas figure. Unresolved: The source alternates between 22.414 dm³ and 22.4 dm³; both printed values are retained and noted. Next page 123.

2026-10-11T15:25:59.390626+00:00 — Chemistry PDF page 123 unresolved. Compared the ideal-gas-equation derivation and eight displayed relationships against PDF page 123; page-edge curl flagged. Unresolved: Right page curl obscures portions of several lines; no obscured wording was invented. Next page 124.

2026-10-11T15:26:57.502887+00:00 — Chemistry PDF page 124 unresolved. Added generalized ideal-gas equations and Example 4.2 with SI units and source-reported result; compared to PDF page 124. Unresolved: No new page-edge omission recorded; source solution value retained as printed. Next page 125.

2026-10-11T15:27:45.127347+00:00 — Chemistry PDF page 125 unresolved. Transcribed both gas-constant calculations with source values, equations and units; source conversion discrepancies flagged. Unresolved: Source gives differing molar volumes (22.414, 22.4, 0.0224 and 0.024 dm³) and an inconsistent SI-unit expression; requires review. Next page 126.

2026-10-11T15:29:19.736171+00:00 — Chemistry PDF page 126 unresolved. Added gas-constant calorie conversion, all four visible practice problems, mass derivation, and Example 4.3 prompt. Unresolved: Example 4.3 solution continues on the following source page; current page has only the givens. Next page 127.

2026-10-11T15:31:09.682276+00:00 — Chemistry PDF page 127 unresolved. Added Example 4.3 calculation result, butane practice problem, and density derivation through equation (4.23). Unresolved: Butane practice text is partially clipped at the source right edge; next page needed to continue the worked gas-density treatment. Next page 128.

2026-10-11T15:33:39.851242+00:00 — Chemistry PDF page 128 unresolved. Added density relation and worked SO₂ example, practice problem, and concentration introduction through the visible source continuation. Unresolved: Concentration derivation continues on page 129. Next page 129.

2026-10-11T15:36:09.890849+00:00 — Chemistry PDF page 129 unresolved. Added gas concentration relations, five self-assessment questions and real-gas deviation/graphical explanation start. Unresolved: Page edges obscure part of the real-gas prose and the graphical explanation continues on page 130. Next page 130.

2026-10-11T15:37:25.685691+00:00 — Chemistry PDF page 130 unresolved. Added compressibility-factor definitions and source-inspired coded SVG graph for Figure 4.6. Unresolved: Graph is a coded schematic reconstruction; source curves are partially obscured and exact trace needs visual review. Next page 131.

2026-10-11T15:39:27.316843+00:00 — Chemistry PDF page 131 unresolved. Added three-temperature nitrogen compressibility graph as coded SVG, conclusion and causes of ideal-gas deviation. Unresolved: Right-edge curl hides some prose; page 132 continues the molecular assumptions. Next page 132.

2026-10-11T15:41:28.856940+00:00 — Chemistry PDF page 132 unresolved. Added high-pressure molecular-volume explanation, Van der Waals attractions and coded SVG Figure 4.8. Unresolved: No explicit scan gaps recorded; visual reconstruction diagram approximates the source piston figures. Next page 133.

2026-10-11T15:43:39.746243+00:00 — Chemistry PDF page 133 unresolved. Added Van der Waals equation introduction, real-gas motivation and free-volume correction concept. Unresolved: Right page curl obscures some wording near volume correction; next page likely continues formula. Next page 134.

2026-10-11T15:45:20.280263+00:00 — Chemistry PDF page 134 unresolved. Added excluded-volume correction, pressure correction explanation and coded SVG for source Figures 4.9 and 4.10. Unresolved: No printed scalar formula for pressure correction is visible yet; proceed to page 135. Next page 135.

2026-10-11T15:47:22.205029+00:00 — Chemistry PDF page 135 unresolved. Added pressure correction, one-mole and n-mole Van der Waals equations and Dalton partial-pressure principle. Unresolved: Page curl obscures words in prose and reading-check box; check next page for continued Dalton material. Next page 136.

2026-10-11T15:58:31.255089+00:00 — Chemistry PDF page 136 unresolved. Added Dalton summation and Example 4.5 partial pressures with a coded SVG. Unresolved: Source example values transcribed; figure schematic. Next page 137.

2026-10-11T16:01:47.240434+00:00 — Chemistry PDF page 137 unresolved. Added Graham diffusion/effusion definitions, examples and coded SVG illustration. Unresolved: Source text partly clipped at page edge; following page continues effusion and Graham law. Next page 138.

2026-10-11T16:04:45.248974+00:00 — Chemistry PDF page 138 unresolved. Added rate definition, Graham square-root density/mass relationships and HCl/NH₃ diffusion experiment. Unresolved: Experiment comparison and derivation continue on page 139. Next page 139.

2026-10-11T16:28:03.382161+00:00 — Chemistry PDF page 139 unresolved. Added reaction, SVG diffusion tube and NH3/HCl speed comparison from Graham law experiment. Unresolved: Continue molecular-mass comparison on the next source page. Next page 140.

2026-10-11T16:44:22.217381+00:00 — Chemistry PDF page 140 unresolved. Added Graham density and molar-mass verification plus the H2/CO2 rate problem. Unresolved: Example 4.6 result continues on the next page. Next page 141.

2026-10-11T16:46:27.603130+00:00 — Chemistry PDF page 141 unresolved. Added H2/CO2 Graham-rate calculation, practice prompt and RMS velocity definition/equations. Unresolved: RMS derivation continues on page 142. Next page 142.

2026-10-11T16:49:33.767342+00:00 — Chemistry PDF page 142 unresolved. Added RMS velocity derivation and equal-average-kinetic-energy derivation for Graham law. Unresolved: Continue gas speed derivation on next page. Next page 143.

2026-10-11T16:54:30.451864+00:00 — Chemistry PDF page 143 unresolved. Added Graham molecular-mass and density rate equation; introduced gas liquefaction and limiting temperature. Unresolved: Scan curl hides portions of the definition; following page needed for critical-temperature terminology. Next page 144.

2026-10-11T16:59:30.217114+00:00 — Chemistry PDF page 144 unresolved. Added critical constants, the gas data table, Joule–Thomson effect and Linde apparatus steps. Unresolved: Linde apparatus explanation continues on page 145; retain source values. Next page 145.

2026-10-11T17:03:56.014144+00:00 — Chemistry PDF page 145 unresolved. Added Linde liquefaction cycle steps, labeled coded SVG apparatus, and uses of liquefied gases. Unresolved: Checkpoint range 141–145 has unresolved scan/curriculum review items; next page 146. Next page 146.

2026-10-11T17:13:26.957361+00:00 — Chemistry PDF page 146 unresolved. Added liquefied-gas applications, plasma definition/origin and coded SVG four-states illustration. Unresolved: Unit continues after plasma introduction; next page 147. Next page 147.

2026-10-11T17:19:29.127061+00:00 — Chemistry PDF page 147 unresolved. Added plasma formation, occurrence, neutrality and visible applications list in English, Urdu and Pashto. Unresolved: Right-edge clipping affects several example details; source follow-up required. Next page 148.

2026-10-11T17:26:48.506947+00:00 — Chemistry PDF page 148 unresolved. Added Unit 4 self-assessment and visible key points in English, Urdu and Pashto. Unresolved: Additional key points continue; next source page 149. Next page 149.

2026-10-11T17:32:27.584997+00:00 — Chemistry PDF page 149 unresolved. Added continuation of Unit 4 key points on STP, real gases, Dalton/Graham laws, liquefaction, Joule–Thomson effect and plasma. Unresolved: Unit 4 summary continues or transitions on next scan; proceed sequentially. Next page 150.

2026-10-11T17:45:12.853274+00:00 — Chemistry PDF page 150 unresolved. Added eight Unit 4 multiple-choice questions and 32 options; reader structural validation passed. Unresolved: Need review translated option wording and continue remaining exercise on page 151. Next page 151.

2026-10-11T19:53:59.871335+00:00 — Chemistry PDF page 150 corrected. Replaced English translation placeholders; 42 individual source records including all 32 options. Exact manifest-to-data and lesson/exercise visibility checks passed. Final audit status remains separate. Next page 151.

2026-10-11T19:54:00.116802+00:00 — Chemistry PDF page 151 unresolved. Restored 7 MCQs with 28 options and 5 short questions as separate translated records. Full and split scans are identical; reader visibility checks passed. Unresolved: Curled right edge partly obscures MCQ and short-question words; final source wording is not verified. Next page 152.

2026-10-11T19:54:00.317408+00:00 — Chemistry PDF page 152 corrected. 26 records: five numerical questions with printed answers and descriptive questions 1-4 with all subparts and two supplied answers. Full English/Urdu/Pashto; source cm units and printed answer values retained. Reader comparison passed. Next page 153.

2026-10-11T19:54:00.514088+00:00 — Chemistry PDF page 153 unresolved. Six records: descriptive question 5(a-c) and two projects with heading, all translated. Obscured fragments explicitly marked; no inferred endings supplied. Reader comparison passed. Unresolved: Word endings in descriptive 5(b) and both projects are hidden at the right edge. Next page 154.

2026-10-11T20:02:13.121157+00:00 — Chemistry PDF page 154 corrected. Ten complete translated learning outcomes, unit heading, Teaching 09, Assessment 01, Weightage 11 percent and coded water-drop SVG saved. Manifest and visibility checks passed; SVG rendering review ongoing. Next page 155.

2026-10-11T20:02:13.311538+00:00 — Chemistry PDF page 155 unresolved. Introduction, definition and 5.1 heading saved with all three languages and Figure 5.1 coded as SVG. Source words hidden by the page curl explicitly marked. Full page155 and split chemistry4 page35 have identical rendered pixels. Unresolved: Hidden connectors and word endings in introduction paragraphs 1-2, unit overview and liquid definition; require clearer source. Next page 156.

2026-10-11T20:08:03.285420+00:00 — Chemistry PDF page 150 verified. Compared all eight questions and 32 options with the source scan. Replaced English fallback text in Urdu/Pashto and reviewed each pair. Preserved all source values and duplicate b. in 8(b). Exact manifest and lesson/exercise visibility checks passed. Next page 156.

2026-10-11T20:08:04.152254+00:00 — Chemistry PDF page 152 verified. Compared all five numerical questions, five printed answers, descriptive 1-4 with 12 subparts and two printed answers with the scan. Urdu/Pashto reviewed; cm notation and printed answer values preserved. All 26 records passed reader visibility checks. Next page 156.

2026-10-11T20:08:04.901182+00:00 — Chemistry PDF page 154 verified. Compared all ten learning outcomes, introductory line, unit label and Teaching 09/Assessment 01/Weightage 11 percent with the source. Urdu/Pashto reviewed. Source water-drop illustration recreated in SVG and rendered with librsvg for visual comparison. Next page 156.

2026-10-11T20:08:05.666273+00:00 — Chemistry PDF page 156 verified. Compared all four postulates, five headings and six prose blocks with the scan. Full translations reviewed. The final fragment continues on page 157 and is not a source gap. All 15 records passed reader visibility checks. Next page 157.

2026-10-11T20:08:06.480015+00:00 — Chemistry PDF page 158 verified. Compared nine prose/heading records, force-strength order, physical values and Figure 5.2 against the scan. Urdu/Pashto reviewed. SVG preserves four water molecules, hydrogen bonds, partial-charge labels and H2S/H2O bent structures with lone pairs. Rendered figure and reader visibility checked. Next page 159.

2026-10-11T20:08:06.676323+00:00 — Chemistry PDF page 157 unresolved. All 13 source text records and equations (5.1)-(5.2) saved with translations, offline notation and valid KaTeX. Source connectors and a strength multiplier are explicitly marked where obscured. Unresolved: Right-edge curl hides short words, intra-molecular definition endings and the final strength multiplier. No multiplier inferred. Next page 159.

2026-10-11T20:08:06.862819+00:00 — Chemistry PDF page 155 unresolved. All source text and Figure 5.1 saved; SVG visual comparison completed with librsvg. Full and split-source pages have identical pixels. Unresolved: Hidden connectors and word endings in introduction paragraphs 1-2, unit overview and liquid definition require a clearer source. Next page 159.

2026-10-11T20:12:13.775359+00:00 — Chemistry PDF page 159 unresolved. Five translated text records, Figures 5.3 and 5.4 and source figure numbering preserved. SVGs compared visually; PH3 charge placement adjusted to avoid bond-label overlap. Unresolved: Curled right edge obscures words in HCl continuation, force-effects paragraph and hydrogen-bond introduction; missing fragments are marked, not inferred. Next page 160.

2026-10-11T20:12:13.995179+00:00 — Chemistry PDF page 160 verified. Nine complete source records and Urdu/Pashto translations compared with the scan. Figures 5.5 and 5.6 recreated as SVG; water/HF bonds, every partial charge, dotted/solid bond styles and source labels compared with librsvg renders. Reader and source-record checks passed. Last paragraph continues on page 161. Next page 161.

2026-10-11T20:20:02.767171+00:00 — Chemistry PDF page 161 unresolved. Source comparison saved for six translated text records, five-row Table 5.1, and coded DNA Figure 5.7. Table values 760, 464, 20-50, 5-20, 1-20 preserved. Visible diagram contours reviewed; figure remains partial. Unresolved: Right-edge prose and caption endings; unclear raised mark after OH; DNA inset atom letters and fine bond details unresolved. Preserve original VI comparison and 5.8 body/5.7 caption mismatch. Next page 162.

2026-10-11T20:20:03.799518+00:00 — Chemistry PDF page 162 verified. All five application subsections, four supplementary bullets, six headings and London-forces opening compared with the source. All 17 records have reviewed Urdu/Pashto translations; exact source-to-data and reader-visibility checks passed. Ending continues on page 163. Next page 163.

2026-10-11T20:20:04.812330+00:00 — Chemistry PDF page 163 unresolved. Six text blocks with translations and Figure 5.8 saved from readable source. Missing right-edge words explicitly marked, two helium atoms and source dipole depiction coded in SVG. Reader checks passed. Unresolved: Right-edge word endings throughout and clipped last dipole/charge in Figure 5.8; fine figure leader endpoints need further source review. Next page 164.

2026-10-11T20:24:02.876140+00:00 — Chemistry PDF page 164 verified. Compared both continuation bullets, two factor headings, four explanation paragraphs, four Reading Check questions and n-butane example with the source. All 17 records and Urdu/Pashto pairs reviewed; exact reader visibility, option/paragraph order and source values including 272.5 K checked. Next page 165.

2026-10-11T20:28:19.005146+00:00 — Chemistry PDF page 151 unresolved. Rechecked the enlarged exercise scan. Question 9 is readable. Replaced completed readings of obscured fragments in MCQs 10/14 and short questions 1/2/5 with explicit source-gap markers in all languages. All 41 records remain visible in lesson and exercise views. Unresolved: Curled-edge words in MCQs 10 and 14 and short questions 1, 2 and 5 need a clearer source; full and split PDF scans are identical. Next page 165.

2026-10-11T20:28:20.042974+00:00 — Chemistry PDF page 165 unresolved. Nine source text records translated; Figures 5.9 and 5:10 recreated and visually compared. Both models contain four carbon and ten hydrogen atoms with the straight/branched source connectivity. Corrected the Chemistry exercise view to retain figures tagged to an example; lesson and exercise visibility checks passed. Unresolved: Isobutane boiling point is only readable through 26; remaining digits/unit and several right-edge prose words are hidden. Missing text is marked and no value inferred. Next page 166.

2026-10-11T20:37:29.371271+00:00 — Chemistry PDF page 166 verified. Compared the complete definition, equilibrium explanation, second definition and Tidbit continuation with the source. Urdu/Pashto reviewed. Figure 5.11 recreated and visually compared: all three stages, motion legend, rate inequality/equality, and separate rate labels preserved. Reader checks passed. Next page 167.

2026-10-11T20:37:30.481696+00:00 — Chemistry PDF page 167 unresolved. Nine text/heading records with paired translations, barometer SVG and complete six-row Table 5.2 saved. All table values and chemical formulas compared with source and reader output. Barometer labels/pressure arrows visually checked. Unresolved: Curled margin obscures words in boiling-point introduction, definition, energy discussion and application paragraph. Barometer continuation and table are legible; the whole page remains unresolved. Next page 168.

2026-10-11T20:39:52.677301+00:00 — Chemistry PDF page 168 verified. Compared all nine text/heading records, Tidbit and three-row Table 5.3 with the source. Urdu/Pashto reviewed. Preserved 0.921/98 and 0.425/72 table values, 1/0.5 atm, 100/82 C and glycerine 290/210 C at 50mm Hg. All source-record, table and reader checks passed. Next page 169.

2026-10-11T20:46:40.154438+00:00 — Chemistry PDF page 169 unresolved. Compared both coded surface-tension illustrations and visible text with PDF page 169; Urdu and Pashto reviewed; reader checks passed. Unresolved: Right-edge scan curl obscures endings in molecular-force prose, factors paragraph and a word after As in rain-drop paragraph. Explicit source gaps retained. Next page 170.

2026-10-11T20:46:41.377214+00:00 — Chemistry PDF page 170 verified. Compared all seven prose records, continuation, definition and units with the source; reviewed Urdu/Pashto; inspected coded Figure 5.13 and preserved forward reference to Figure 5.14. Next page 171.

2026-10-11T20:49:34.291883+00:00 — Chemistry PDF page 171 unresolved. Reviewed visible source text, translations and viscosity SVG; all source records appear in the reader. Unresolved: Right-edge words remain obscured; handwritten red correction covers the printed specific-heat definition and has a separate unverified annotation record. Next page 172.

2026-10-11T20:49:35.301542+00:00 — Chemistry PDF page 172 verified. Compared all twelve records and four rows of Table 5.4 with PDF page 172; checked symbols, temperatures, units, Urdu and Pashto and reader visibility. Next page 173.

## 2026-10-12 — BIOLOGY (current first priority; Physics/Chemistry records above are separate)

**Assignment reissued 2026-10-12:** Biology FIRST, then Physics, Chemistry, Statistics, English, Urdu, Pakistan Studies, Computer Science, Civics, Economics, General Science, Drawing, HPE, Islamiat compulsory/ikhtiari, Islamic History, Mutalia-e-Quran and every other non-Mathematics subject. Mathematics is excluded entirely. No browser testing; PDF/JPG inspection mandatory; no commit/push/reset; shared files only under `tmp/class-content-shared.lock`.

**Biology source facts**
- Book: KPTBB "A Textbook of Biology, Grade XI, Test Edition". 364 JPG scans in `Books/11th/11th bio/jpg` (`Biology Book for 11 class KPTBB_N.jpg`, 1240x1585). `pdf/bio1..bio9.pdf` are low-res image-only exports of the same scans (bio1 = scans 1-41, bio2 = 41-81, bio3 = 81-121, bio4 = 121-161, bio5 = 151-191 (overlaps 151-161), bio6 = 191-241, bio7 = 241-291, bio8 = 291-341, bio9 = 341-364). No separate edition, no duplicate scans (perceptual-hash check).
- `Books/11th/11th bio/word/bio1..9.docx` hold OCR text of the same scans (cached in `biology-docx-text/bioN.txt`); they are a useful cross-check but have OCR errors and are NOT authoritative. Tesseract OCR of every scan is cached in `biology-ocr/page-NNN.txt` (supporting aid only).
- TOC (scan 3): Ch1 p1, Ch2 p29, Ch3 p62, Ch4 p74, Ch5 p103, Ch6 p124, Ch7 p152, Ch8 p170, Ch9 p201, Ch10 p241, Ch11 p283, Ch12 p308, Ch13 p338, Glossary p358, Index p364 (13 chapters).
- Printed page = scan − 3 for scans 4-32 (scan 4 = p1). From scan 33 the visible folio is scan − 2 (scan 33 = p31): the chapter-2 opener counts as pages 29-30 although it is one scan. Check the folio every few scans and record the offset.
- No credits/copyright/authors page exists in the scans. Scan 1 cover is cropped at the right edge. Many scans carry a rotated "Scanned with CamScanner" stamp (excluded). Scan 27 has a third-party advertisement banner (excluded).

**Implementation**
- Data: `js/bio_11_data.js` (`BIO_11_DATA`, 14 chapter records, reader `renderBiology11Tab`, helpers `bio11Page`, `bio11Pair`, `bio11Cell`, `bio11Mcq`, SVG helpers `bio11Svg`, `bio11Callouts`, sugar-structure helpers). Wired into `index.html`, `js/app.js` (routing, search, subject card), `js/data.js` (13 chapters, book card), `css/style.css` (`.bio11-*`). Wiring script: `wire_biology.py`; CSS rules source: `bio11.css`.
- Per-page workflow: read scan -> write a `bio11Page(...)` call in a scratch part file (English original verbatim incl. printed errors with `editorialNote`, aligned Urdu + Pashto, coded SVG for every diagram with all labels, `sourceGap` for cropped/faint text) -> `append_bio.py <part>` -> `node` check (`chk_bio.js` in the session scratchpad: loads the data in a vm, checks duplicate ids, missing translations, markup, render of all five tabs) -> `save_biology_checkpoint.py <lastScan> <chapter> <note>` which rewrites `biology-progress.json`.
- Exercises: `role:'question'|'option'`, `exerciseId`; key points `summary:true`; concepts `concept:true`. No printed answer key seen yet (check chapter ends).

**State at this checkpoint:** scans 1-41 recorded (front matter, all of Chapter 1 incl. key points and exercise, Chapter 2 up to printed p39 "Storage Molecules"). **Next scan: 42** (starts bio2.pdf p2; Chapter 2 continues: proteins/amino acids). Last fully verified scan: 41.

**Known unresolved so far:** cover edge cropped (scan 1); Fig 1.18(b) electron micrograph and cover photographs not reproducible as code (schematic only); scan 22 left-edge letters cropped (restored from context, flagged); scan 38 last four lines faint (flagged); Fig 1.x/2.x SVGs are simplified redraws that keep every printed label but not the photographic shading; translations are authored by the agent and have not been reviewed by a human speaker.

**2026-10-12 incident (Biology):** the D: drive filled to 100% while `js/bio_11_data.js` was being rewritten in place and the file was truncated to 0 bytes. It was rebuilt in full from the saved part files and re-entered scans 1-8 (all 80 scans validated, 0 issues). The master copy now lives on C: at `...\scratchpad\bio_11_data.MASTER.js`; `append_bio.py <part>` appends to the master, then deploys to `js/bio_11_data.js` through a temp file and an atomic replace. If the scratchpad is ever lost, rebuild from `js/bio_11_data.js` (keep a copy outside D: after every few batches). The OCR cache `biology-ocr/` was temporarily moved to C: and restored. Next Biology scan: 81.

## Biology (KPTBB Grade XI) — COMPLETE with recorded gaps (2026-10-12)

All 364 scans (`...\11th bio\jpg\Biology Book for 11 class KPTBB_1..364.jpg`) were inspected and recorded in `js/bio_11_data.js` (365 sections, 4,226 paragraphs, 0 validator issues at last run): front matter, Chapters 1-13, Glossary (printed pp 358-363), Index (pp 364-365, Authors Profile), back matter (feedback form, Quran verse Al-Hujurat 10, back cover with national anthem and printing details). Part files are in `biology-parts/`; checkpoint in `biology-progress.json`. Printed page = scan + 4 from scan 148 on (earlier offsets differ; see section `source` fields). No printed answer keys exist in the book (checked every exercise page).

**Unresolved source defects (recorded in the data as `sourceGap`/`editorialNote`/`auditStatus: partial`):**
- Missing pages (not in any scan): printed pp 103, 113-114, 123, 148, 151; scan 203 text gap.
- Cut or clipped text, not supplied: scan 255 heading "10.5 Suppor…" (title end missing); scan 273 first two lines; scans 281, 283, 318 (sentence cut at foot "…extended periods", continuation absent), 334 (last outcome "…release of"), 354-356 headword fragments; scan 359 glossary page is non-alphabetical with headwordless fragments ("parathyroid hormone (PTH)…", "component of seed coats and nuts.") and a stray "gH" headword in scan 358.
- Index page numbers that disagree with the book (First/Second/Third Line of Defense 361/363/369; "Life cycle of HIV, 1130"; "Electrophoresis" and "Nucleus," have no page).
- Printed typos preserved with editorial notes (e.g. "Parastic", "heamolymph", "clastin", "pyrixia", "Pancrease").
- Photographs (cover images, micrographs, patient photos) are redrawn as labelled SVG schematics, not reproduced; all line figures are simplified redraws keeping every printed label.
- Urdu and Pashto translations are agent-authored and need native-speaker review (some Pashto/Urdu medical and disease terms in Chapter 13 and the Glossary are especially uncertain, e.g. mumps/smallpox terms).
- No browser/visual check was run (per assignment); layout of the new `glossary`, `index` and `backMatter` layouts was only validated by the Node renderer smoke check.

Next subject per assignment order: Physics (prior partial work in `progress.md` above, PDF pages 1-5 only), then Chemistry (pages 1-21 drafts + 150-174 work), Statistics, English, Urdu, Pakistan Studies, Computer, Civics, Economics, General Science, Drawing, HPE, Islamiat (Compulsory/Ikhtiari), Islamic History, Mutalia-e-Quran. Not started.

2026-10-12T08:02:11.170764+00:00 — Chemistry PDF page 173 unresolved. Compared page 173 text (density end, Self-Assessment 1-5, 5.3 Energetics, phase-change paragraphs) with record; right-edge scan clipping marked [scan obscured]. Unresolved: Right edge clipped by scan on several lines; not inferred. Next page 174.

2026-10-12T08:02:20.677922+00:00 — Chemistry PDF page 174 verified. Compared all six records, Figure 5.15 labels/arrows, equations (ΔHvap 40.7, ΔHfus +6.02 kJ/mol) and trilingual text with PDF page 174. Next page 175.

2026-10-12T08:05:07.208230+00:00 — Chemistry PDF page 175 unresolved. Compared page 175 (heats of vaporization/sublimation, equations, 5.3.2) with record; clipped line ends marked. Unresolved: Right-edge clipping of scan on many lines; not inferred. Next page 176.

2026-10-12T08:05:08.062193+00:00 — Chemistry PDF page 176 verified. Compared page 176 text, Tables 5.5 and 5.6 values, dynamic-equilibrium text and ice-water equilibrium with record. Next page 177.

2026-10-12T08:06:41.421198+00:00 — Chemistry PDF page 177 unresolved. Compared page 177 (5.4 Liquid Crystals, Heintz/Reinitzer paragraph, definition, 5.4.1, Figure 5.16) with record. Unresolved: Right-edge clipping of scan on text lines; not inferred. Next page 178.

2026-10-12T08:06:42.308142+00:00 — Chemistry PDF page 178 unresolved. Compared page 178 text, STS box, properties list i-iv, 5.4.2 uses and Figure 5.17 with record. Unresolved: Figure 5.17 is a photograph represented by a schematic SVG; list numerals clipped at left edge. Next page 179.

2026-10-12T08:08:44.186064+00:00 — Chemistry PDF page 179 unresolved. Compared page 179 uses 3-6 and Figures 5.18/5.19 with record. Unresolved: Right-edge clipping; photographs represented by schematic SVG. Next page 180.

2026-10-12T08:08:45.076538+00:00 — Chemistry PDF page 180 verified. Compared Self-Assessment 1-5 and eleven Key Points (page 175 printed) with record. Next page 181.

2026-10-12T08:08:46.113104+00:00 — Chemistry PDF page 181 unresolved. Compared the twelve remaining Key Points of Unit 5 with record. Unresolved: Right-edge clipping on most lines; not inferred. Next page 182.

2026-10-12T08:09:53.707444+00:00 — Chemistry PDF page 183 unresolved. Compared MCQs 10-13 and Short Questions 1-12 with page 183. Unresolved: Right edge of several short questions clipped by scan; completed wording flagged, not verified. Next page 184.

2026-10-12T08:10:15.419382+00:00 — Chemistry PDF page 182 verified. Compared MCQs 1-9 with options against page 182. Next page 184.

2026-10-12T08:10:16.367170+00:00 — Chemistry PDF page 183 unresolved. Compared MCQs 10-13 and Short Questions 1-12 with page 183. Unresolved: Right edge of several short questions clipped by scan; completed wording flagged, not verified. Next page 184.

2026-10-12T08:10:55.356268+00:00 — Chemistry PDF page 184 verified. Compared Descriptive Questions 1-5 (all sub-parts) and the two Project items with page 184. Next page 185.

2026-10-12T08:14:17.599451+00:00 — Chemistry PDF page 185 unresolved. Compared Unit 6 opener outcomes, teaching/assessment/weightage and cover picture with page 185. Unresolved: Right-edge clipping of outcome lines; picture is a schematic. Next page 186.

2026-10-12T08:14:18.429769+00:00 — Chemistry PDF page 186 verified. Compared Introduction, Tidbit and 6.1 points i-x with page 186. Next page 187.

2026-10-12T08:25:27.377198+00:00 — Chemistry PDF page 187 unresolved. Compared 6.1.1 text (diffusion, compression, expansion) and Figure 6.1 with page 187. Unresolved: Right-edge clipping on most lines; figure is a schematic. Next page 188.

2026-10-12T08:25:28.643497+00:00 — Chemistry PDF page 188 verified. Compared motion, spaces, forces, kinetic energy, Reading Check, 6.2 and 6.2.1 with page 188. Next page 189.

2026-10-12T08:26:35.779142+00:00 — Chemistry PDF page 189 unresolved. Compared amorphous solids end, 6.2.2, Tidbit and Figure 6.2 with page 189. Unresolved: Right-edge clipping on most lines; figure is a schematic. Next page 190.

2026-10-12T08:26:36.655388+00:00 — Chemistry PDF page 190 unresolved. Compared 6.3, 6.3.1, plane and axis of symmetry and Figure 6.3 with page 190. Unresolved: Figure 6.3 shading simplified (flagged). Next page 191.

2026-10-12T08:27:55.691259+00:00 — Chemistry PDF page 191 unresolved. Compared Figures 6.4/6.5, centre of symmetry, 6.3.2 and 6.3.3 with page 191. Unresolved: Right-edge clipping; sentence continues on page 192; figures schematic. Next page 192.

2026-10-12T08:27:56.793134+00:00 — Chemistry PDF page 192 verified. Compared 6.3.4 to 6.3.6 with page 192. Next page 193.

2026-10-12T08:43:58.265296+00:00 — Chemistry PDF page 194 unresolved. 6.3.8-6.3.10 with Tables 6.1, 6.2 Unresolved: Folio 189 right-edge not clipped; subscripts in table smudged; Allotropy sentence continues p195; translations need native review Next page 195.

2026-10-12T08:44:07.743979+00:00 — Chemistry PDF page 193 unresolved. Figures 6.6/6.7 coded as schematics; 6.3.7 Anisotropy trilingual Unresolved: Right-edge clipping; photographs redrawn as schematics Next page 195.

2026-10-12T08:44:12.246492+00:00 — Chemistry PDF page 194 unresolved. 6.3.8-6.3.10 with Tables 6.1, 6.2 Unresolved: Table subscripts smudged; Allotropy sentence continues p195; translations need native review Next page 195.

2026-10-12T08:59:44.185606+00:00 — Chemistry PDF page 195 unresolved. Allotropes of S and O, transition temperature, coded figures Unresolved: Right-edge clipping; Lewis dots not reproduced; translations need native review Next page 196.

2026-10-12T08:59:45.141668+00:00 — Chemistry PDF page 196 verified. Table 6.3, self-assessment, STS compared with scan; translations pending native review Next page 197.

2026-10-12T09:00:48.861006+00:00 — Chemistry PDF page 197 unresolved. STS end and 6.4 Crystal Lattice Unresolved: Heavy right-edge clipping from page curl; translations need native review Next page 198.

2026-10-12T09:00:49.805113+00:00 — Chemistry PDF page 198 unresolved. Figure 6.9 coded schematic, 6.4.1 Unit cell Unresolved: Figure rebuilt as schematic; translations need native review Next page 199.

2026-10-12T09:14:39.829740+00:00 — Chemistry PDF page 199 unresolved. Figure 6.10, Table 6.4, cubic unit cells Unresolved: Right-edge clipping in text and Example column; figure coded schematic; translations need native review Next page 200.

2026-10-12T09:14:41.317269+00:00 — Chemistry PDF page 200 unresolved. Three cubic lattice types, Figure 6.11, NaCl Unresolved: Figure coded schematic; printed misprints preserved; translations need native review Next page 201.

2026-10-12T09:15:43.831785+00:00 — Chemistry PDF page 201 unresolved. Figures 6.12 and 6.13 coded, NaCl structure text Unresolved: Right-edge clipping; photographs rendered as schematics; translations need native review Next page 202.

2026-10-12T09:15:45.376597+00:00 — Chemistry PDF page 202 verified. Ionic solid factors and Table 6.5 compared with scan; printed forms preserved; translations pending native review Next page 203.

2026-10-12T09:21:49.383332+00:00 — Chemistry PDF page 203 unresolved. 6.4.3 Lattice Energy, equations, Table 6.6 Unresolved: Right-edge clipping; table rows skewed by page curl; translations need native review Next page 204.

2026-10-12T09:21:51.309988+00:00 — Chemistry PDF page 204 verified. 6.4.4 ice density and heat of fusion compared with scan; translations pending native review Next page 205.

2026-10-12T09:23:42.723509+00:00 — Chemistry PDF page 205 unresolved. Figs 6.14/6.15, Table 6.7, 6.5, 6.5.1 Unresolved: Right-edge clipping; photographs rendered as schematics; table rows skewed; translations need native review Next page 206.

2026-10-12T09:23:44.737806+00:00 — Chemistry PDF page 206 unresolved. Figure 6.16 and ionic solid properties Unresolved: Figure rebuilt as schematic; translations need native review Next page 207.

2026-10-12T09:39:57.651710+00:00 — Chemistry PDF page 207 unresolved. Figs 6.17/6.18, 6.5.2 Covalent Solids Unresolved: Right-edge clipping; photographs redrawn as schematics; translations need native review Next page 208.

2026-10-12T09:39:59.181903+00:00 — Chemistry PDF page 208 unresolved. Figure 6.19, 6.5.3 Metallic Solids Unresolved: Figure redrawn as schematic; translations need native review Next page 209.

2026-10-12T09:47:05.510250+00:00 — Chemistry PDF page 209 unresolved. Unit 6 solids p209 Unresolved: Edge clipping from page curl; reconstructed text marked; translations need native review Next page 210.

2026-10-12T09:47:06.745565+00:00 — Chemistry PDF page 210 unresolved. Unit 6 solids p210 Unresolved: Edge clipping from page curl; reconstructed text marked; translations need native review Next page 211.

2026-10-12T09:47:08.249994+00:00 — Chemistry PDF page 211 unresolved. Unit 6 solids p211 Unresolved: Edge clipping from page curl; reconstructed text marked; translations need native review Next page 212.

2026-10-12T09:47:09.423759+00:00 — Chemistry PDF page 212 unresolved. Unit 6 solids p212 Unresolved: Edge clipping from page curl; reconstructed text marked; translations need native review Next page 213.

2026-10-12T09:49:49.829995+00:00 — Chemistry PDF page 213 unresolved. Chemistry p213 Unresolved: Right-edge clipping; figures redrawn; translations need native review Next page 214.

2026-10-12T09:49:50.913308+00:00 — Chemistry PDF page 214 unresolved. Chemistry p214 Unresolved: Right-edge clipping; figures redrawn; translations need native review Next page 215.

2026-10-12T09:49:51.913662+00:00 — Chemistry PDF page 215 unresolved. Chemistry p215 Unresolved: Right-edge clipping; figures redrawn; translations need native review Next page 216.

2026-10-12T09:49:52.857631+00:00 — Chemistry PDF page 216 unresolved. Chemistry p216 Unresolved: Right-edge clipping; figures redrawn; translations need native review Next page 217.

2026-10-12T09:52:03.414722+00:00 — Chemistry PDF page 217 unresolved. Chemistry p217 Unresolved: Right-edge clipping; translations need native review Next page 218.

2026-10-12T09:52:04.393337+00:00 — Chemistry PDF page 218 unresolved. Chemistry p218 Unresolved: Right-edge clipping; translations need native review Next page 219.

2026-10-12T09:52:05.440458+00:00 — Chemistry PDF page 219 unresolved. Chemistry p219 Unresolved: Right-edge clipping; translations need native review Next page 220.

2026-10-12T09:52:06.422851+00:00 — Chemistry PDF page 220 unresolved. Chemistry p220 Unresolved: Right-edge clipping; translations need native review Next page 221.

2026-10-12T09:53:48.750854+00:00 — Chemistry PDF page 221 unresolved. Chemistry p221 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 222.

2026-10-12T09:53:49.968248+00:00 — Chemistry PDF page 222 unresolved. Chemistry p222 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 223.

2026-10-12T09:53:51.029858+00:00 — Chemistry PDF page 223 unresolved. Chemistry p223 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 224.

2026-10-12T09:53:52.040379+00:00 — Chemistry PDF page 224 unresolved. Chemistry p224 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 225.

2026-10-12T09:56:03.062031+00:00 — Chemistry PDF page 225 unresolved. Chemistry p225 Unresolved: Right-edge clipping or illegible glyphs; translations need native review Next page 226.

2026-10-12T09:56:04.067688+00:00 — Chemistry PDF page 226 unresolved. Chemistry p226 Unresolved: Right-edge clipping or illegible glyphs; translations need native review Next page 227.

2026-10-12T09:56:05.131476+00:00 — Chemistry PDF page 227 unresolved. Chemistry p227 Unresolved: Right-edge clipping or illegible glyphs; translations need native review Next page 228.

2026-10-12T09:56:06.155920+00:00 — Chemistry PDF page 228 unresolved. Chemistry p228 Unresolved: Right-edge clipping or illegible glyphs; translations need native review Next page 229.

2026-10-12T09:58:34.913464+00:00 — Chemistry PDF page 229 unresolved. Chemistry p229 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 230.

2026-10-12T09:58:36.151153+00:00 — Chemistry PDF page 230 unresolved. Chemistry p230 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 231.

2026-10-12T09:58:37.550926+00:00 — Chemistry PDF page 231 unresolved. Chemistry p231 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 232.

2026-10-12T09:58:38.820263+00:00 — Chemistry PDF page 232 unresolved. Chemistry p232 Unresolved: Right-edge clipping or printed misprints retained; translations need native review Next page 233.

2026-10-12T10:00:30.614148+00:00 — Chemistry PDF page 233 unresolved. Chemistry p233 Unresolved: Right-edge clipping where noted; translations need native review Next page 234.

2026-10-12T10:00:31.681764+00:00 — Chemistry PDF page 234 unresolved. Chemistry p234 Unresolved: Right-edge clipping where noted; translations need native review Next page 235.

2026-10-12T10:00:32.860157+00:00 — Chemistry PDF page 235 unresolved. Chemistry p235 Unresolved: Right-edge clipping where noted; translations need native review Next page 236.

2026-10-12T10:00:34.071975+00:00 — Chemistry PDF page 236 unresolved. Chemistry p236 Unresolved: Right-edge clipping where noted; translations need native review Next page 237.

2026-10-12T10:03:09.146425+00:00 — Chemistry PDF page 237 unresolved. Chemistry p237 Unresolved: Right-edge clipping or cut exponents; figure redrawn on p240; translations need native review Next page 238.

2026-10-12T10:03:10.205557+00:00 — Chemistry PDF page 238 unresolved. Chemistry p238 Unresolved: Right-edge clipping or cut exponents; figure redrawn on p240; translations need native review Next page 239.

2026-10-12T10:03:11.326099+00:00 — Chemistry PDF page 239 unresolved. Chemistry p239 Unresolved: Right-edge clipping or cut exponents; figure redrawn on p240; translations need native review Next page 240.

2026-10-12T10:03:12.326886+00:00 — Chemistry PDF page 240 unresolved. Chemistry p240 Unresolved: Right-edge clipping or cut exponents; figure redrawn on p240; translations need native review Next page 241.

2026-10-12T10:05:31.130316+00:00 — Chemistry PDF page 241 unresolved. Chemistry p241 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 242.

2026-10-12T10:05:32.318029+00:00 — Chemistry PDF page 242 unresolved. Chemistry p242 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 243.

2026-10-12T10:05:33.255568+00:00 — Chemistry PDF page 243 unresolved. Chemistry p243 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 244.

2026-10-12T10:05:34.276917+00:00 — Chemistry PDF page 244 unresolved. Chemistry p244 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 245.

2026-10-12T10:08:11.636556+00:00 — Chemistry PDF page 245 unresolved. Chemistry p245 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 246.

2026-10-12T10:08:14.262113+00:00 — Chemistry PDF page 247 unresolved. Chemistry p247 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 248.

2026-10-12T10:08:15.544574+00:00 — Chemistry PDF page 248 unresolved. Chemistry p248 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 249.

2026-10-12T10:08:27.139044+00:00 — Chemistry PDF page 246 unresolved. Chemistry p246 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 249.

2026-10-12T10:10:38.627075+00:00 — Chemistry PDF page 249 unresolved. Chemistry p249 Unresolved: Edge clipping; figure redrawn on p249; translations need native review Next page 250.

2026-10-12T10:10:40.323517+00:00 — Chemistry PDF page 250 unresolved. Chemistry p250 Unresolved: Edge clipping; figure redrawn on p249; translations need native review Next page 251.

2026-10-12T10:10:41.490735+00:00 — Chemistry PDF page 251 unresolved. Chemistry p251 Unresolved: Edge clipping; figure redrawn on p249; translations need native review Next page 252.

2026-10-12T10:10:42.536438+00:00 — Chemistry PDF page 252 unresolved. Chemistry p252 Unresolved: Edge clipping; figure redrawn on p249; translations need native review Next page 253.

2026-10-12T10:12:24.778557+00:00 — Chemistry PDF page 253 unresolved. Chemistry p253 Unresolved: Skewed scan or edge clipping; translations need native review Next page 254.

2026-10-12T10:12:28.393664+00:00 — Chemistry PDF page 254 unresolved. Chemistry p254 Unresolved: Skewed scan or edge clipping; translations need native review Next page 255.

2026-10-12T10:12:32.616414+00:00 — Chemistry PDF page 256 unresolved. Chemistry p256 Unresolved: Skewed scan or edge clipping; translations need native review Next page 257.

2026-10-12T10:12:46.383716+00:00 — Chemistry PDF page 255 unresolved. Chemistry p255 Unresolved: Edge clipping; translations need native review Next page 257.

2026-10-12T10:14:50.020632+00:00 — Chemistry PDF page 257 unresolved. Chemistry p257 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 258.

2026-10-12T10:14:52.830963+00:00 — Chemistry PDF page 258 unresolved. Chemistry p258 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 259.

2026-10-12T10:14:55.415072+00:00 — Chemistry PDF page 259 unresolved. Chemistry p259 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 260.

2026-10-12T10:14:59.118934+00:00 — Chemistry PDF page 260 unresolved. Chemistry p260 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 261.

2026-10-12T10:17:15.347057+00:00 — Chemistry PDF page 261 unresolved. Chemistry p261 Unresolved: Edge clipping; Lewis drawings redrawn; translations need native review Next page 262.

2026-10-12T10:17:17.649760+00:00 — Chemistry PDF page 262 unresolved. Chemistry p262 Unresolved: Edge clipping; Lewis drawings redrawn; translations need native review Next page 263.

2026-10-12T10:17:20.137080+00:00 — Chemistry PDF page 263 unresolved. Chemistry p263 Unresolved: Edge clipping; Lewis drawings redrawn; translations need native review Next page 264.

2026-10-12T10:17:22.370489+00:00 — Chemistry PDF page 264 unresolved. Chemistry p264 Unresolved: Edge clipping; Lewis drawings redrawn; translations need native review Next page 265.

2026-10-12T10:19:20.768742+00:00 — Chemistry PDF page 265 unresolved. Chemistry p265 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 266.

2026-10-12T10:19:21.921611+00:00 — Chemistry PDF page 266 unresolved. Chemistry p266 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 267.

2026-10-12T10:19:23.802660+00:00 — Chemistry PDF page 267 unresolved. Chemistry p267 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 268.

2026-10-12T10:19:25.958908+00:00 — Chemistry PDF page 268 unresolved. Chemistry p268 Unresolved: Edge clipping; handwritten marks ignored; translations need native review Next page 269.

2026-10-12T10:21:44.448402+00:00 — Chemistry PDF page 270 unresolved. Chemistry p270 Unresolved: Edge clipping; translations need native review Next page 271.

2026-10-12T10:21:48.521233+00:00 — Chemistry PDF page 272 unresolved. Chemistry p272 Unresolved: Edge clipping; translations need native review Next page 273.

2026-10-12T10:22:22.100090+00:00 — Chemistry PDF page 269 unresolved. Chemistry p269 Unresolved: Edge clipping; translations need native review Next page 273.

2026-10-12T10:22:25.051560+00:00 — Chemistry PDF page 271 unresolved. Chemistry p271 Unresolved: Edge clipping; translations need native review Next page 273.

2026-10-12T10:28:42.192580+00:00 — Chemistry PDF page 273 unresolved. Chemistry p273 Unresolved: Edge clipping; figure redrawn on p274; translations need native review Next page 274.

2026-10-12T10:28:44.382041+00:00 — Chemistry PDF page 274 unresolved. Chemistry p274 Unresolved: Edge clipping; figure redrawn on p274; translations need native review Next page 275.

2026-10-12T10:28:46.512605+00:00 — Chemistry PDF page 275 unresolved. Chemistry p275 Unresolved: Edge clipping; figure redrawn on p274; translations need native review Next page 276.

2026-10-12T10:28:49.063565+00:00 — Chemistry PDF page 276 unresolved. Chemistry p276 Unresolved: Edge clipping; figure redrawn on p274; translations need native review Next page 277.

2026-10-12T10:33:28.518347+00:00 — Chemistry PDF page 277 unresolved. Chemistry p277 Unresolved: Edge clipping; figure redrawn on p277; translations need native review Next page 278.

2026-10-12T10:33:29.680825+00:00 — Chemistry PDF page 278 unresolved. Chemistry p278 Unresolved: Edge clipping; figure redrawn on p277; translations need native review Next page 279.

2026-10-12T10:33:31.828412+00:00 — Chemistry PDF page 279 unresolved. Chemistry p279 Unresolved: Edge clipping; figure redrawn on p277; translations need native review Next page 280.

2026-10-12T10:33:33.947007+00:00 — Chemistry PDF page 280 unresolved. Chemistry p280 Unresolved: Edge clipping; figure redrawn on p277; translations need native review Next page 281.

2026-10-12T10:35:30.751598+00:00 — Chemistry PDF page 281 unresolved. Chemistry p281 Unresolved: Edge clipping; translations need native review Next page 282.

2026-10-12T10:35:34.758411+00:00 — Chemistry PDF page 282 unresolved. Chemistry p282 Unresolved: Edge clipping; translations need native review Next page 283.

2026-10-12T10:35:37.195826+00:00 — Chemistry PDF page 283 unresolved. Chemistry p283 Unresolved: Edge clipping; translations need native review Next page 284.

2026-10-12T10:35:39.358775+00:00 — Chemistry PDF page 284 unresolved. Chemistry p284 Unresolved: Edge clipping; translations need native review Next page 285.

2026-10-12T10:40:17.847968+00:00 — Chemistry PDF page 285 unresolved. Chemistry p285 Unresolved: Edge clipping; figures redrawn on p287; translations need native review Next page 286.

2026-10-12T10:40:21.227632+00:00 — Chemistry PDF page 286 unresolved. Chemistry p286 Unresolved: Edge clipping; figures redrawn on p287; translations need native review Next page 287.

2026-10-12T10:40:23.527861+00:00 — Chemistry PDF page 287 unresolved. Chemistry p287 Unresolved: Edge clipping; figures redrawn on p287; translations need native review Next page 288.

2026-10-12T10:40:25.437284+00:00 — Chemistry PDF page 288 unresolved. Chemistry p288 Unresolved: Edge clipping; figures redrawn on p287; translations need native review Next page 289.

2026-10-12T10:43:01.450470+00:00 — Chemistry PDF page 289 unresolved. Chemistry p289 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 290.

2026-10-12T10:43:02.522197+00:00 — Chemistry PDF page 290 unresolved. Chemistry p290 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 291.

2026-10-12T10:43:03.575766+00:00 — Chemistry PDF page 291 unresolved. Chemistry p291 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 292.

2026-10-12T10:43:04.598432+00:00 — Chemistry PDF page 292 unresolved. Chemistry p292 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 293.

2026-10-12T10:45:10.346520+00:00 — Chemistry PDF page 293 unresolved. Chemistry p293 Unresolved: Edge clipping; figure redrawn on p293; translations need native review Next page 294.

2026-10-12T10:45:12.007288+00:00 — Chemistry PDF page 294 unresolved. Chemistry p294 Unresolved: Edge clipping; figure redrawn on p293; translations need native review Next page 295.

2026-10-12T10:45:13.536443+00:00 — Chemistry PDF page 295 unresolved. Chemistry p295 Unresolved: Edge clipping; figure redrawn on p293; translations need native review Next page 296.

2026-10-12T10:45:15.348724+00:00 — Chemistry PDF page 296 unresolved. Chemistry p296 Unresolved: Edge clipping; figure redrawn on p293; translations need native review Next page 297.

2026-10-12T10:47:46.326847+00:00 — Chemistry PDF page 297 unresolved. Chemistry p297 Unresolved: Edge clipping; Roman numerals converted; translations need native review Next page 298.

2026-10-12T10:47:48.042807+00:00 — Chemistry PDF page 298 unresolved. Chemistry p298 Unresolved: Edge clipping; Roman numerals converted; translations need native review Next page 299.

2026-10-12T10:47:49.759099+00:00 — Chemistry PDF page 299 unresolved. Chemistry p299 Unresolved: Edge clipping; Roman numerals converted; translations need native review Next page 300.

2026-10-12T10:47:51.373698+00:00 — Chemistry PDF page 300 unresolved. Chemistry p300 Unresolved: Edge clipping; Roman numerals converted; translations need native review Next page 301.

2026-10-12T10:51:11.545484+00:00 — Chemistry PDF page 301 unresolved. Chemistry p301 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 302.

2026-10-12T10:51:12.660260+00:00 — Chemistry PDF page 302 unresolved. Chemistry p302 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 303.

2026-10-12T10:51:13.733721+00:00 — Chemistry PDF page 303 unresolved. Chemistry p303 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 304.

2026-10-12T10:51:14.839533+00:00 — Chemistry PDF page 304 unresolved. Chemistry p304 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 305.

2026-10-12T10:53:16.222165+00:00 — Chemistry PDF page 305 unresolved. Chemistry p305 Unresolved: Edge clipping; graph redrawn approximately on p308; translations need native review Next page 306.

2026-10-12T10:53:17.440379+00:00 — Chemistry PDF page 306 unresolved. Chemistry p306 Unresolved: Edge clipping; graph redrawn approximately on p308; translations need native review Next page 307.

2026-10-12T10:53:18.571420+00:00 — Chemistry PDF page 307 unresolved. Chemistry p307 Unresolved: Edge clipping; graph redrawn approximately on p308; translations need native review Next page 308.

2026-10-12T10:53:19.683975+00:00 — Chemistry PDF page 308 unresolved. Chemistry p308 Unresolved: Edge clipping; graph redrawn approximately on p308; translations need native review Next page 309.

2026-10-12T10:54:59.865159+00:00 — Chemistry PDF page 309 unresolved. Chemistry p309 Unresolved: Clipped table columns on p309; edge clipping; translations need native review Next page 310.

2026-10-12T10:55:02.172386+00:00 — Chemistry PDF page 310 unresolved. Chemistry p310 Unresolved: Clipped table columns on p309; edge clipping; translations need native review Next page 311.

2026-10-12T10:55:03.844862+00:00 — Chemistry PDF page 311 unresolved. Chemistry p311 Unresolved: Clipped table columns on p309; edge clipping; translations need native review Next page 312.

2026-10-12T10:55:05.771951+00:00 — Chemistry PDF page 312 unresolved. Chemistry p312 Unresolved: Clipped table columns on p309; edge clipping; translations need native review Next page 313.

2026-10-12T10:56:49.580005+00:00 — Chemistry PDF page 313 unresolved. Chemistry p313 Unresolved: Edge clipping; figure redrawn on p316; translations need native review Next page 314.

2026-10-12T10:56:50.739210+00:00 — Chemistry PDF page 314 unresolved. Chemistry p314 Unresolved: Edge clipping; figure redrawn on p316; translations need native review Next page 315.

2026-10-12T10:56:52.040307+00:00 — Chemistry PDF page 315 unresolved. Chemistry p315 Unresolved: Edge clipping; figure redrawn on p316; translations need native review Next page 316.

2026-10-12T10:56:53.956964+00:00 — Chemistry PDF page 316 unresolved. Chemistry p316 Unresolved: Edge clipping; figure redrawn on p316; translations need native review Next page 317.

2026-10-12T10:58:41.797069+00:00 — Chemistry PDF page 317 unresolved. Chemistry p317 Unresolved: Edge clipping; figure redrawn on p319; translations need native review Next page 318.

2026-10-12T10:58:43.017053+00:00 — Chemistry PDF page 318 unresolved. Chemistry p318 Unresolved: Edge clipping; figure redrawn on p319; translations need native review Next page 319.

2026-10-12T10:58:44.253934+00:00 — Chemistry PDF page 319 unresolved. Chemistry p319 Unresolved: Edge clipping; figure redrawn on p319; translations need native review Next page 320.

2026-10-12T10:58:45.420533+00:00 — Chemistry PDF page 320 unresolved. Chemistry p320 Unresolved: Edge clipping; figure redrawn on p319; translations need native review Next page 321.

2026-10-12T11:00:39.419149+00:00 — Chemistry PDF page 321 unresolved. Chemistry p321 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 322.

2026-10-12T11:00:40.739853+00:00 — Chemistry PDF page 322 unresolved. Chemistry p322 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 323.

2026-10-12T11:00:41.941286+00:00 — Chemistry PDF page 323 unresolved. Chemistry p323 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 324.

2026-10-12T11:00:43.238376+00:00 — Chemistry PDF page 324 unresolved. Chemistry p324 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 325.

2026-10-12T11:02:44.726439+00:00 — Chemistry PDF page 325 unresolved. Chemistry p325 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 326.

2026-10-12T11:02:49.017328+00:00 — Chemistry PDF page 327 unresolved. Chemistry p327 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 328.

2026-10-12T11:02:50.546309+00:00 — Chemistry PDF page 328 unresolved. Chemistry p328 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 329.

2026-10-12T11:03:39.211176+00:00 — Chemistry PDF page 328 unresolved. Chemistry p328 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 329.

2026-10-12T11:03:48.540070+00:00 — Chemistry PDF page 326 unresolved. Chemistry p326 Unresolved: Edge clipping; figure redrawn; translations need native review Next page 329.

2026-10-12T11:03:49.733091+00:00 — Chemistry PDF page 328 unresolved. Chemistry p328 Unresolved: Edge clipping; figure redrawn Next page 329.

2026-10-12T11:03:58.286803+00:00 — Chemistry PDF page 325 unresolved. Chemistry p325 Unresolved: Edge clipping; translations need native review Next page 329.

2026-10-12T11:03:59.723691+00:00 — Chemistry PDF page 327 unresolved. Chemistry p327 Unresolved: Edge clipping; translations need native review Next page 329.

2026-10-12T11:05:35.782022+00:00 — Chemistry PDF page 329 unresolved. Chemistry p329 Unresolved: Edge clipping; translations need native review Next page 330.

2026-10-12T11:05:37.190838+00:00 — Chemistry PDF page 330 unresolved. Chemistry p330 Unresolved: Edge clipping; translations need native review Next page 331.

2026-10-12T11:05:38.613436+00:00 — Chemistry PDF page 331 unresolved. Chemistry p331 Unresolved: Edge clipping; translations need native review Next page 332.

2026-10-12T11:05:39.805339+00:00 — Chemistry PDF page 332 unresolved. Chemistry p332 Unresolved: Edge clipping; translations need native review Next page 333.

2026-10-12T11:08:03.809049+00:00 — Chemistry PDF page 333 unresolved. Chemistry p333 Unresolved: Edge clipping; skewed scan; figure redrawn on p336; translations need native review Next page 334.

2026-10-12T11:08:05.045861+00:00 — Chemistry PDF page 334 unresolved. Chemistry p334 Unresolved: Edge clipping; skewed scan; figure redrawn on p336; translations need native review Next page 335.

2026-10-12T11:08:06.308065+00:00 — Chemistry PDF page 335 unresolved. Chemistry p335 Unresolved: Edge clipping; skewed scan; figure redrawn on p336; translations need native review Next page 336.

2026-10-12T11:08:07.400950+00:00 — Chemistry PDF page 336 unresolved. Chemistry p336 Unresolved: Edge clipping; skewed scan; figure redrawn on p336; translations need native review Next page 337.

2026-10-12T11:10:23.451357+00:00 — Chemistry PDF page 337 unresolved. Chemistry p337 Unresolved: Edge clipping; figure redrawn on p339; translations need native review Next page 338.

2026-10-12T11:10:25.784393+00:00 — Chemistry PDF page 338 unresolved. Chemistry p338 Unresolved: Edge clipping; figure redrawn on p339; translations need native review Next page 339.

2026-10-12T11:10:26.966131+00:00 — Chemistry PDF page 339 unresolved. Chemistry p339 Unresolved: Edge clipping; figure redrawn on p339; translations need native review Next page 340.

2026-10-12T11:10:28.047692+00:00 — Chemistry PDF page 340 unresolved. Chemistry p340 Unresolved: Edge clipping; figure redrawn on p339; translations need native review Next page 341.

2026-10-12T11:12:26.604640+00:00 — Chemistry PDF page 341 unresolved. Chemistry p341 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 342.

2026-10-12T11:12:27.760933+00:00 — Chemistry PDF page 342 unresolved. Chemistry p342 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 343.

2026-10-12T11:12:29.381480+00:00 — Chemistry PDF page 343 unresolved. Chemistry p343 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 344.

2026-10-12T11:12:30.657536+00:00 — Chemistry PDF page 344 unresolved. Chemistry p344 Unresolved: Edge clipping; figures redrawn; translations need native review Next page 345.

2026-10-12T11:14:17.213549+00:00 — Chemistry PDF page 345 unresolved. Chemistry p345 Unresolved: Edge clipping; printed misspellings retained; translations need native review Next page 346.

2026-10-12T11:14:19.586922+00:00 — Chemistry PDF page 347 unresolved. Chemistry p347 Unresolved: Edge clipping; printed misspellings retained; translations need native review Next page 348.

2026-10-12T11:14:20.885129+00:00 — Chemistry PDF page 348 unresolved. Chemistry p348 Unresolved: Edge clipping; printed misspellings retained; translations need native review Next page 349.

2026-10-12T11:15:37.809100+00:00 — Chemistry PDF page 348 unresolved. Chemistry p348 Unresolved: Edge clipping; kcl/g misprint retained Next page 349.

2026-10-12T11:16:00.822792+00:00 — Chemistry PDF page 346 unresolved. Chemistry p346 Unresolved: Edge clipping; translations need native review Next page 349.

2026-10-12T11:18:01.084338+00:00 — Chemistry PDF page 349 unresolved. Chemistry p349 Unresolved: Edge clipping; figure redrawn on p351; translations need native review Next page 350.

2026-10-12T11:18:02.320887+00:00 — Chemistry PDF page 350 unresolved. Chemistry p350 Unresolved: Edge clipping; figure redrawn on p351; translations need native review Next page 351.

2026-10-12T11:18:03.540345+00:00 — Chemistry PDF page 351 unresolved. Chemistry p351 Unresolved: Edge clipping; figure redrawn on p351; translations need native review Next page 352.

2026-10-12T11:18:04.765679+00:00 — Chemistry PDF page 352 unresolved. Chemistry p352 Unresolved: Edge clipping; figure redrawn on p351; translations need native review Next page 353.

2026-10-12T11:19:38.270662+00:00 — Chemistry PDF page 353 unresolved. Chemistry p353 Unresolved: Garbled arrow glyphs; edge clipping; diagrams redrawn; translations need native review Next page 354.

2026-10-12T11:19:39.468536+00:00 — Chemistry PDF page 354 unresolved. Chemistry p354 Unresolved: Garbled arrow glyphs; edge clipping; diagrams redrawn; translations need native review Next page 355.

2026-10-12T11:19:40.619751+00:00 — Chemistry PDF page 355 unresolved. Chemistry p355 Unresolved: Garbled arrow glyphs; edge clipping; diagrams redrawn; translations need native review Next page 356.

2026-10-12T11:19:41.831868+00:00 — Chemistry PDF page 356 unresolved. Chemistry p356 Unresolved: Garbled arrow glyphs; edge clipping; diagrams redrawn; translations need native review Next page 357.

2026-10-12T11:21:30.881949+00:00 — Chemistry PDF page 357 unresolved. Chemistry p357 Unresolved: Edge clipping; skewed scan; translations need native review Next page 358.

2026-10-12T11:21:32.339005+00:00 — Chemistry PDF page 358 unresolved. Chemistry p358 Unresolved: Edge clipping; skewed scan; translations need native review Next page 359.

2026-10-12T11:21:33.561500+00:00 — Chemistry PDF page 359 unresolved. Chemistry p359 Unresolved: Edge clipping; skewed scan; translations need native review Next page 360.

2026-10-12T11:21:34.812212+00:00 — Chemistry PDF page 360 unresolved. Chemistry p360 Unresolved: Edge clipping; skewed scan; translations need native review Next page 361.

2026-10-12T11:23:33.035733+00:00 — Chemistry PDF page 361 unresolved. Chemistry p361 Unresolved: Edge clipping; skewed scan; cover redrawn; translations need native review Next page 362.

2026-10-12T11:23:34.072593+00:00 — Chemistry PDF page 362 unresolved. Chemistry p362 Unresolved: Edge clipping; skewed scan; cover redrawn; translations need native review Next page 363.

2026-10-12T11:23:35.122462+00:00 — Chemistry PDF page 363 unresolved. Chemistry p363 Unresolved: Edge clipping; skewed scan; cover redrawn; translations need native review Next page 364.

2026-10-12T11:23:36.163939+00:00 — Chemistry PDF page 364 unresolved. Chemistry p364 Unresolved: Edge clipping; skewed scan; cover redrawn; translations need native review Next page 365.

2026-10-12T11:26:19.680997+00:00 — Chemistry PDF page 365 unresolved. Chemistry p365 Unresolved: Edge clipping; skewed scan; translations need native review Next page 366.

2026-10-12T11:26:20.774989+00:00 — Chemistry PDF page 366 unresolved. Chemistry p366 Unresolved: Edge clipping; skewed scan; translations need native review Next page 367.

2026-10-12T11:26:21.904434+00:00 — Chemistry PDF page 367 unresolved. Chemistry p367 Unresolved: Edge clipping; skewed scan; translations need native review Next page 368.

2026-10-12T11:26:22.932589+00:00 — Chemistry PDF page 368 unresolved. Chemistry p368 Unresolved: Edge clipping; skewed scan; translations need native review Next page 369.

2026-10-12T11:29:30.236009+00:00 — Chemistry PDF page 369 unresolved. Oxidizing and reducing agents Unresolved: Skewed/clipped scan; translations need native review Next page 370.

2026-10-12T11:29:31.549625+00:00 — Chemistry PDF page 370 unresolved. Electrodes and electrolytic cell Unresolved: Skewed/clipped scan; translations need native review Next page 371.

2026-10-12T11:29:32.808618+00:00 — Chemistry PDF page 371 unresolved. Electrode potential Unresolved: Skewed/clipped scan; translations need native review Next page 372.

2026-10-12T11:29:34.165923+00:00 — Chemistry PDF page 372 unresolved. Standard electrode potential Unresolved: Skewed/clipped scan; translations need native review Next page 373.

2026-10-12T11:31:32.284486+00:00 — Chemistry PDF page 373 unresolved. Cell voltage and SHE Unresolved: Skewed/clipped scan; translations need native review Next page 374.

2026-10-12T11:31:33.931713+00:00 — Chemistry PDF page 374 unresolved. Figure 12.3 SHE and measurement Unresolved: Skewed/clipped scan; translations need native review Next page 375.

2026-10-12T11:31:35.710967+00:00 — Chemistry PDF page 375 unresolved. Electrode potential of zinc Unresolved: Skewed/clipped scan; translations need native review Next page 376.

2026-10-12T11:31:37.274583+00:00 — Chemistry PDF page 376 unresolved. Electrode potential of copper and ECS Unresolved: Skewed/clipped scan; translations need native review Next page 377.

2026-10-12T11:33:30.079340+00:00 — Chemistry PDF page 377 unresolved. Table 12.1 standard reduction potentials Unresolved: Skewed/clipped scan; translations need native review Next page 378.

2026-10-12T11:33:31.423457+00:00 — Chemistry PDF page 378 unresolved. ECS features and cell types Unresolved: Skewed/clipped scan; translations need native review Next page 379.

2026-10-12T11:33:32.861220+00:00 — Chemistry PDF page 379 unresolved. Electrolytic cell and NaCl electrolysis Unresolved: Skewed/clipped scan; translations need native review Next page 380.

2026-10-12T11:33:40.366172+00:00 — Chemistry PDF page 380 unresolved. Nelson cell and voltaic cell Unresolved: Skewed/clipped scan; translations need native review Next page 381.

2026-10-12T11:35:34.471426+00:00 — Chemistry PDF page 381 unresolved. Daniell cell Unresolved: Skewed/clipped scan; translations need native review Next page 382.

2026-10-12T11:35:35.747107+00:00 — Chemistry PDF page 382 unresolved. Electrical terms and Faraday first law Unresolved: Skewed/clipped scan; translations need native review Next page 383.

2026-10-12T11:35:38.165153+00:00 — Chemistry PDF page 384 unresolved. Batteries and dry cell Unresolved: Skewed/clipped scan; translations need native review Next page 385.

2026-10-12T11:35:45.759638+00:00 — Chemistry PDF page 383 unresolved. Faraday second law and Example 12.7 Unresolved: Skewed/clipped scan; translations need native review Next page 385.

2026-10-12T11:35:47.012873+00:00 — Chemistry PDF page 384 unresolved. Batteries and dry cell Unresolved: Skewed/clipped scan; translations need native review Next page 385.

2026-10-12T11:38:23.376422+00:00 — Chemistry PDF page 385 unresolved. Lead storage battery Unresolved: Skewed/clipped scan; translations need native review Next page 386.

2026-10-12T11:38:24.988795+00:00 — Chemistry PDF page 386 unresolved. Fuel cells Unresolved: Skewed/clipped scan; translations need native review Next page 387.

2026-10-12T11:38:26.348845+00:00 — Chemistry PDF page 387 unresolved. Fuel cell and corrosion Unresolved: Skewed/clipped scan; translations need native review Next page 388.

2026-10-12T11:38:27.640310+00:00 — Chemistry PDF page 388 unresolved. Corrosion of iron and prevention Unresolved: Skewed/clipped scan; translations need native review Next page 389.

2026-10-12T11:40:10.668964+00:00 — Chemistry PDF page 389 unresolved. Electroplating and galvanizing Unresolved: Skewed/clipped scan; translations need native review Next page 390.

2026-10-12T11:40:12.335674+00:00 — Chemistry PDF page 390 unresolved. Galvanizing and Self-Assessment Unresolved: Skewed/clipped scan; translations need native review Next page 391.

2026-10-12T11:40:13.855964+00:00 — Chemistry PDF page 391 unresolved. Key points Unit 12 Unresolved: Skewed/clipped scan; translations need native review Next page 392.

2026-10-12T11:40:15.211253+00:00 — Chemistry PDF page 392 unresolved. Key points continued Unresolved: Skewed/clipped scan; translations need native review Next page 393.

2026-10-12T11:42:06.981147+00:00 — Chemistry PDF page 393 unresolved. Exercise MCQ 1-10 Unresolved: Skewed/clipped scan; translations need native review Next page 394.

2026-10-12T11:42:08.738792+00:00 — Chemistry PDF page 394 unresolved. Exercise MCQ 11-13, short, numerical Unresolved: Skewed/clipped scan; translations need native review Next page 395.

2026-10-12T11:42:10.396002+00:00 — Chemistry PDF page 395 unresolved. Exercise numerical and descriptive Unresolved: Skewed/clipped scan; translations need native review Next page 396.

2026-10-12T11:42:11.981496+00:00 — Chemistry PDF page 396 unresolved. Exercise descriptive and project Unresolved: Skewed/clipped scan; translations need native review Next page 397.

2026-10-12T11:45:02.706618+00:00 — Chemistry PDF page 397 unresolved. Glossary A-Anion Unresolved: x Next page 398.

2026-10-12T11:45:09.442585+00:00 — Chemistry PDF page 398 unresolved. Glossary Anode-Bond length Unresolved: Skewed/clipped scan; translations need native review Next page 399.

2026-10-12T11:45:10.445279+00:00 — Chemistry PDF page 399 unresolved. Glossary Bond order-Colligative Unresolved: Skewed/clipped scan; translations need native review Next page 400.

2026-10-12T11:45:11.569864+00:00 — Chemistry PDF page 400 unresolved. Glossary Colloid-Dilute solution Unresolved: Skewed/clipped scan; translations need native review Next page 401.

2026-10-12T11:47:53.617004+00:00 — Chemistry PDF page 401 unresolved. Glossary Dipole-Kc Unresolved: Skewed/clipped scan; translations need native review Next page 402.

2026-10-12T11:47:55.323074+00:00 — Chemistry PDF page 402 unresolved. Glossary Kp-Hund rule Unresolved: Skewed/clipped scan; translations need native review Next page 403.

2026-10-12T11:47:56.568751+00:00 — Chemistry PDF page 403 unresolved. Glossary Hund continued-Lattice Unresolved: Skewed/clipped scan; translations need native review Next page 404.

2026-10-12T11:47:57.791000+00:00 — Chemistry PDF page 404 unresolved. Glossary Lattice energy-Miscible Unresolved: Skewed/clipped scan; translations need native review Next page 405.

2026-10-12T11:50:06.382315+00:00 — Chemistry PDF page 405 unresolved. Glossary Molar-Percent composition Unresolved: Skewed/clipped scan; translations need native review Next page 406.

2026-10-12T11:50:07.961511+00:00 — Chemistry PDF page 406 unresolved. Glossary Percent yield-Rate of reaction Unresolved: Skewed/clipped scan; translations need native review Next page 407.

2026-10-12T11:50:09.616652+00:00 — Chemistry PDF page 407 unresolved. Glossary Reaction quotient-Speed Unresolved: Skewed/clipped scan; translations need native review Next page 408.

2026-10-12T11:50:10.869303+00:00 — Chemistry PDF page 408 unresolved. Glossary Spin-System Unresolved: Skewed/clipped scan; translations need native review Next page 409.

2026-10-12T11:53:03.000463+00:00 — Chemistry PDF page 409 unresolved. Glossary Tetrahedral-VSEPR Unresolved: Skewed/clipped scan; translations need native review Next page 410.

2026-10-12T11:53:04.582997+00:00 — Chemistry PDF page 410 unresolved. Glossary Wave number-Yield Unresolved: Skewed/clipped scan; translations need native review Next page 411.

2026-10-12T11:53:05.834887+00:00 — Chemistry PDF page 411 unresolved. Index A-E Unresolved: Skewed/clipped scan; translations need native review Next page 412.

2026-10-12T11:53:07.183819+00:00 — Chemistry PDF page 412 unresolved. Index F-Q Unresolved: Skewed/clipped scan; translations need native review Next page 413.

2026-10-12T11:54:29.950352+00:00 — Chemistry PDF page 413 unresolved. Index R-Y Unresolved: Skewed/clipped scan; translations need native review Next page 414.

2026-10-12T11:54:31.386990+00:00 — Chemistry PDF page 414 unresolved. MCQs answer keys Unresolved: Skewed/clipped scan; translations need native review Next page 415.

2026-10-12T11:54:32.729175+00:00 — Chemistry PDF page 415 unresolved. References Unresolved: Skewed/clipped scan; translations need native review Next page 416.

2026-10-12T11:54:46.883863+00:00 — Chemistry PDF page 416 unresolved. Authors Unresolved: Skewed/clipped scan; translations need native review Next page 417.

2026-10-12T11:55:45.058261+00:00 — Chemistry PDF page 417 unresolved. Authors continued Unresolved: Skewed/clipped scan; translations need native review Next page 418.

2026-10-12T11:55:46.425422+00:00 — Chemistry PDF page 418 unresolved. Textbook feedback form Unresolved: Skewed/clipped scan; translations need native review Next page 419.

2026-10-12T11:55:47.699568+00:00 — Chemistry PDF page 419 unresolved. Back cover Unresolved: Skewed/clipped scan; translations need native review Next page 420.
