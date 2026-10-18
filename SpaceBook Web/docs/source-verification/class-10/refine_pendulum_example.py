from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
replacements={
 'displaced:[145,267]':'displaced:[126,271]',
 'M85 40L145 267':'M85 40L126 271',
 '0 0 0 145 267':'0 0 0 126 271',
 'M85 267H145':'M85 271H126',
 'cx="145" cy="267"':'cx="126" cy="271"',
 'M145 267V357':'M126 271V363',
 'M145 267L168 351L145 357':'M126 271L142 360',
 'M145 322A55 55 0 0 0 159 320':'M126 326A55 55 0 0 0 136 325',
 'x="65" y="328"':'x="35" y="328"',
 'M85 102A62 62 0 0 0 101 100':'M85 102A62 62 0 0 0 96 101',
}
for old,new in replacements.items(): s=s.replace(old,new)
needle='<path d="M126 326A55'
if '<path d="M142 360L126 363"' not in s:
 s=s.replace(needle,'<path d="M142 360L126 363" stroke="#111827" stroke-width="2" stroke-dasharray="3 3" marker-end="url(#phys10-pendulum-example-arrow)"/>'+needle)
p.write_text(s,encoding='utf-8')
