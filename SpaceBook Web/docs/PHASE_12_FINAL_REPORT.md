# Phase 12 — final report (Classes 11/12 QA)

Status date: 2026-10-22. Branch `phase/p2-server`. All commits are local and unpushed.

## Done and verified against scans (details in `docs/QA_classes_11_12.md`)
- Urdu 11, Islamiat Lazmi 11, Ikhtiari 11, Mutalia 11, HPE 11: scans viewed, fixes logged in `docs/qa/proofreading_fixes.tsv`.
- English 12: viewed end to end except Truck Art p.35 onward, The Last Leaf p.43 and the Lord of the Flies summary scans 100–116.
- English 11: all 240 scan images viewed (printed pp.1–229). One wording fix (p.208 "Charlottee") and four page-note count fixes (pp.103, 104, 148, 169). Modern-author essays are summaries by design, so only their glossaries, questions and exercises were compared word for word.

## Not done
- English 12 gaps listed above.
- Phase 11: remaining word and sentence meanings; unanimated Maths chains (`node tools/qa/unanimated.js` lists them; many Maths 12 worked examples have OCR-damaged source text and need rebuilding from the scans); Physics 12 Unit 11 Q7, Q11, Q12 still unkeyed.
- Mutalia-e-Quran 12 scans 8–71 and 108–187: left open by instruction.
- Phase 10 (MT integration): the owner's job.

## Owner steps after merging
1. Review and push the local commits.
2. Regenerate shared files: `node tools/build/all.js --only mcq-bank,study-index,lexicon,lazy,search,offline`
3. Bump the cache in `index.html` as usual.
4. Browser-check the English 11 pages whose notes changed (pp.103, 104, 148, 169, 208).

## Environment note
C: reached 0 bytes free during the session (it later showed about 8.5 GB). The repo and scans are on D:.
