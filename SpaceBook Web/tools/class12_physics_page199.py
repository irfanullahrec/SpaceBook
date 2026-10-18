from class12_source_review import ROOT,checkpoint
import json
p=json.loads((ROOT/"docs/source-verification/class-12/progress.json").read_text(encoding="utf-8"))
if p["nextPage"]==199: checkpoint(199,"excluded",[],"Rendered and visually inspected PDF page 199 (rotated feedback form, no printed page number). It is a blank textbook-feedback form with eight evaluation statements, comment/amendment table, general remarks and contact fields; no physics lesson content or filled responses to transcribe.",printed_pages=[],chapter_number=20)
