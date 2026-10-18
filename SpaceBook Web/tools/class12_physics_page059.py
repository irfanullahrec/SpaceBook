"""Checkpoint the duplicated scan on PDF page 59 after visual comparison."""
import json
from class12_source_review import ROOT,checkpoint

if __name__=='__main__':
 progress=json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))
 if progress['nextPage']==59:
  checkpoint(59,'verified_unchanged',[
   'phys13-electron-charge-mass-ratio-and-eq139106-107',
   'phys13-velocity-selector-intro-figure1321107'
  ],'Rendered PDF page 59 and compared its full printed-page spread against PDF page 58. Both scans contain the same printed pages 106–107, the same electron charge-to-mass derivation through Eq. 13.9, and the same Figures 13.20–13.21 and captions; no additional or changed source text was found. The existing verified lesson records therefore cover this duplicate scan without adding duplicate lesson content.',printed_pages=[106,107],chapter_number=13)
