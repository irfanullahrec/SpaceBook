"""Update only this audit's Physics checkpoint after inspection and successful checks."""
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).parent
page = int(sys.argv[1])
note = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").strip()
inventory_path = root / "inventory.json"
inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
book = next(b for b in inventory["subjects"][0]["books"] if b["path"].endswith("physicsfull.pdf"))
assert page == book["nextPage"], "Checkpoint must advance consecutively"
book["correctedPages"].append(page)
if page not in book["unresolvedPages"]:
    if page not in book["verifiedCorrectedPages"]:
        book["verifiedCorrectedPages"].append(page)
    # Never let a later verified page jump over an unresolved page.
    verified = set(book["verifiedCorrectedPages"])
    highest = int(book["highestFullyVerifiedPage"])
    while highest + 1 in verified:
        highest += 1
    book["highestFullyVerifiedPage"] = highest
book["nextPage"] = page + 1
inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
progress_path = root / "progress.md"
progress = progress_path.read_text(encoding="utf-8")
unresolved = ",".join(map(str, book["unresolvedPages"]))
next_action = f"Next action: inspect PDF page {page + 1}, compare, correct/save/record, then page {page + 2} consecutively. Pages {unresolved} have unresolved source/visual items; resolve before any full-book completion claim. Continue all 393 pages before Chemistry."
progress = re.sub(r"Next action:.*", next_action, progress, count=1)
progress_path.write_text(progress + "\n" + note + "\n", encoding="utf-8")
