# Accessibility (Phase 12, first part): what exists, how it is tested, what is not done

Written 2026-10-20. Everything below was tested in jsdom (a real DOM without a layout engine) and by static analysis; **nothing was tested with a screen reader or in a real browser**. Section "Not done" says what that leaves open.

## What the code does

| Area | Where | What |
|---|---|---|
| Tab bars | `js/core/a11y.js` | Every group of buttons whose class contains `tab-btn` or `top-tab` (and the sign-in tabs) is a `tablist` of `tab`s: `aria-selected` follows the active tab, one tab stop per bar (roving `tabindex`), arrow keys (mirrored in right-to-left pages), Home and End open the tab reached and keep the focus on it, also when opening it redraws or reorders the bar. The Word Stats button is in the bar as an action, outside the arrow-key cycle. |
| Things clicked that are not buttons | same | Subject cards, the brand in the header, and similar `onclick` elements become `role=button` with `tabindex=0` and answer Enter and Space. Done when the page is drawn (after the functions that draw bars, through SBHooks) and again on every Tab press, so what was drawn since is reachable before the browser moves the focus: no `MutationObserver`. |
| Card headers | same | Accordion and topic-card headers hold their own controls (full screen, language tabs) and controls may not nest in a button, so the **title** is the button (`aria-expanded` follows the card) and a click on it is a click on the header. A header with no control inside is the button itself. |
| Lesson sentences | same | 100+ sentences per chapter would be 100+ tab stops: the text is one tab stop and the arrow keys, Home and End move between sentences; Enter opens the translation. They get no role, so a screen reader keeps reading text as text. Quran verses keep their own role and tab stop. |
| Dialogs | `SBA11y.trap` | Tab stays inside, Escape closes, the focus returns to the opener; controls in hidden / `aria-hidden` / `inert` branches and in a closed `<details>` do not count as first or last. Used by the sign-in dialog, the account dialog, the Offline books dialog and the question / practice window. |
| Landmarks | `index.html` | The two `nav` landmarks have names; the practice window is a `dialog` with its title and a named close button. |
| Language and direction | `js/sb_rtl.js` | The reading areas that are laid out right to left now also say `lang="ur"` / `"ps"` / `"ar"`, taken from the subject's medium (`SBMedium`), not guessed from the script. Screen readers pick the voice from it. |
| Focus and motion | `css/a11y.css` | A visible focus ring on every focusable element; the focused sentence is highlighted; `prefers-reduced-motion` stops animations and transitions. |
| Text contrast | `tools/a11y_contrast.js` | 112 text/background pairs written in the stylesheets and in the `style=""` strings of the scripts were below AA (white on `#16a34a` is 3.3:1, the brand blue `#0284c7` with white is 4.1:1). Each was darkened by the smallest step (same hue) that reaches 4.5:1 (3:1 for large text); only colour values changed (verified line by line against the previous commit). 0 remain. |

## How it is tested

| Check | Command | CI |
|---|---|---|
| Tabs, keyboard, headers, sentences, dialogs, language (50 checks) | `node --max-old-space-size=6144 tests/a11y/tabs.js` | yes |
| Contrast tool (ratios, what fails, what the fix changes) | `node tests/a11y/contrast.js` | yes |
| No new low-contrast pair | `node tools/a11y_contrast.js --check` (baseline `tests/baseline/contrast.json`, now 0) | yes |
| axe-core (WCAG 2.0/2.1 A and AA plus best practice) on 15 views: home, class lists, Biology lesson, Maths, Class 5 Maths, Class 2 English, Class 10 Physics, Class 12 Chemistry and Urdu, Class 4 Urdu, Class 1 English, Tests Preparation, the sign-in dialog, the Offline books dialog | `node --max-old-space-size=8192 tests/a11y/axe.js` (4 minutes; baseline `tests/baseline/axe.json`, now empty) | yes |

axe found, and these were fixed: nested interactive controls in the card headers (serious, 55 nodes in the sampled views), two navigation landmarks without names, the practice window outside any landmark, the sign-in tab list without tabs (critical), a second banner landmark inside the Offline books dialog.

## Not done, and why

- **Screen readers and real browsers.** NVDA, JAWS, TalkBack and VoiceOver were not run; the focus ring, the tab order of the whole page and the dialogs on a 375 px phone were not looked at. jsdom has no layout, so axe cannot judge colour contrast, visibility by stylesheet, target size or focus order on screen. Run axe (the browser extension or Lighthouse) on the pages above once, with a real browser.
- **Contrast beyond what the source states.** The tool sees a rule or a `style=""` that sets both the text colour and the background as plain colours. Text whose background comes from a parent, a gradient, an image, `var()` or `opacity` is not seen. Most `style=""` strings set only one of the two.
- **Other pages and dialogs.** The word-statistics dialog, the translate popover, the account menu, the Papers views and the interactive MCQ widgets are not in the axe sample; only the sign-in, account, offline and practice dialogs use the focus trap.
- **Root `lang` and `dir`.** The page stays `lang="en"`; the reading areas carry the language of the open book (above). Moving to one render context that sets both for the whole reader is part of the Phase 5 second half (it also replaces the document-wide `MutationObserver` in `sb_rtl.js`).
- **Offline full-text search** (Phase 12) is not built: today's search matches titles and the first search loads the book data; a sharded index with Urdu / Pashto / Arabic normalisation is a separate piece of work.
- **Reduced motion** is global and blunt (animation and transition durations go to ~0); a per-component review was not done.
