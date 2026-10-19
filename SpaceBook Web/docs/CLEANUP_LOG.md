# Cleanup log (Phase 10, first part)

Done 2026-10-20 with `tools/cleanup/archive.js` and the plan `tools/cleanup/plan_2026-10-20.json`. **Nothing was deleted**: files were moved (renamed, same drive) to `D:\SpaceBook\SpaceBook_Archive\SpaceBook Web\<same relative path>`, after writing their path, size and SHA-256 to `D:\SpaceBook\SpaceBook_Archive\ARCHIVE_LOG_plan_2026-10-20.csv` (10,264 lines). The tool refuses tracked files, refuses to overwrite, and stops if a moved file does not arrive with the same size. To restore anything, move the same relative path back.

## What moved (all untracked or git-ignored; none was ever part of the deployed app)

| Group | Files | Size |
|---|---|---|
| `tmp/` (page renders, one-off scripts of earlier sessions) | 9,468 | 6,760 MB |
| `tools/source-review/` | 384 | 294 MB |
| `cover-replacement-staging/` (the `kptb_*.webp` covers it fed are committed: 137 tracked files) | 27 | 60 MB |
| `tools/` page images (`_m7_*.png`, scans), `*_aux.txt`, `__pycache__/` | 361 | 27 MB |
| `backup/` | 17 | 3 MB |
| root `doc1_p3.png`, `doc2_p1.png`, `urdu_p3..p7.png` | 7 | 22 MB |

Total: 10,264 files, 7,166 MB. The emptied folders `tmp/`, `backup/`, `cover-replacement-staging/` remain (empty), so scripts that write there still work.

## The three numbers

- **Working folder** (`SpaceBook Web`): **8.0 GB -> 1.4 GB** (what is left: `docs/` 862 MB (the source-verification material), `js/` 361 MB of book data, `covers/` 46 MB, `node_modules` 45 MB).
- **Production payload**: **unchanged**. These folders were never in git or in the deploy, so the live site and the CI upload are the same size as before. (The payload that matters for students is the lazy page: 1.6 MB compressed at start, books on demand.)
- **Disk actually freed**: **0**. The archive is on the same drive (D:), as the plan asks. When you are sure you do not need it, deleting `D:\SpaceBook\SpaceBook_Archive` frees ~6.7 GB; I never delete.

## Checked after the move

`node tools/validate.js` 999/0 and `node --max-old-space-size=8192 tools/smoke.js` 0 failed with the folders gone.

## Not done in Phase 10, and why

- Tracked files (`kotlin/`, `exercise-pages.json`, `biology-progress.json`, `docs/*-progress.json`, `js/math_12_book_data.js`, `js/unkeyed.json`): tiny, and `biology-progress.json` is referenced by a Class 11 checkpoint script; moving tracked files is a separate commit and I want you to see each.
- 114 unreferenced cover images (28.6 MB) and `assets/biology12`, `assets/physics12`, `assets/math9-agent1`, `assets/physics9-agent1` (5.7 MB): Appendix B asks for a 404 check / network log first; that needs a real browser session, which I do not have.
- Superseded data files (DATA-01, ~5.4 MB): only after the traces prove zero reads and parity passes (the tracer in `tests/trace` lists 69 data globals never read; that is a lead, not proof).
- `git gc --prune=now` (64 MB of garbage): only after a backup of `.git`, which is yours to confirm.
