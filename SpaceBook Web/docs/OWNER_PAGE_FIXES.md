# Owner's page-by-page fixes

The owner tests page by page on the website and the app and sends a screenshot with the fixes. Each fix is listed here as it arrives,
with what was done on Web and on App. A fix that is still open stays at the top of its own row until it is done.

| # | Date | Screen | Fix asked | Web | App | State |
|---|---|---|---|---|---|---|
| 1 | 2026-11-02 | Class 12 Maths, Unit 1 (Maple), Pages 1–2 | In every subject the first page keeps only the book's opening (unit title, Student Learning Outcomes); the Introduction starts on page 2 | `js/sb_book_spread.js` `openerAlone()`: on a unit's first page everything after the opening section (or after the outcomes list, an Introduction heading) moves to the top of the unit's next page; affects about 170 units (Class 12 Maths 1 and 4, Class 9 Chemistry 6-8, Class 9 Maths, Class 10 Physics 11, HPE 7/8/10, Class 2 GK and Islamiat, Pakistan Studies 9, Islamiat Ikhtiari 10, ...) | Same file; reaches the app with the next `sync_app.js` run | Web done; App waits for the sync |
