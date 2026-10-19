# Baselines

- `html-YYYY-MM-DD/` — **HTML snapshot** (`node --max-old-space-size=8192 tools/snapshot_html.js`): for every class x subject x chapter x tab, tab labels in order and a hash of the rendered tab HTML (random sb_mcq ids normalised). No browser needed, ~1.5 min. Compare two runs with `node tools/snapshot_html.js --compare <dirA> <dirB>`; a refactor is accepted only if every difference is listed and intended. Does not see layout, fonts or what add-on scripts do to the live DOM.
- `run.js` — **Playwright baseline** (DOM text hashes, console errors, timings, screenshots at 1280x800 and 375x812). Needs about 1.5 GB of free RAM per page; not yet run to completion (see docs/PROGRESS_LOG.md).
