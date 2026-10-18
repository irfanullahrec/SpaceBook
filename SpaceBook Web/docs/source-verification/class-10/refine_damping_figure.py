from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
s=s.replace('<path d="M426 265H777M460 395V112" stroke="#111827" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#phys10-damping-arrow)"/>','<path d="M426 265H777" stroke="#111827" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#phys10-damping-arrow)"/><path d="M460 395V112" stroke="#111827" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#phys10-damping-arrow)"/>')
s=s.replace('<text x="729" y="244">Time</text>','<text x="725" y="315">Time</text>')
p.write_text(s,encoding='utf-8')
