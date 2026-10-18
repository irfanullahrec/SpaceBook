from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
s=s.replace('d="M${physics10SpringPath(60,120,64,8,18)}"','d="${physics10SpringPath(60,120,64,8,18)}"')
for title,height in [('Tyre, main suspension spring and shock absorber',280),('Spring surrounds an oil reservoir; a piston with holes moves through viscous oil',330),('Displacement versus time: underdamped oscillations cross equilibrium; critical damping returns fastest without oscillation; overdamping returns more slowly',240)]:
 needle=f'<title id="'+{'Tyre, main suspension spring and shock absorber':'phys10-suspension-title','Spring surrounds an oil reservoir; a piston with holes moves through viscous oil':'phys10-shock-cutaway-title'}.get(title,'phys10-damping-types-title')+'">'+title+'</title>'
 background=f'<rect width="340" height="{height}" fill="white"/>'
 if needle+background not in s: s=s.replace(needle,needle+background)
p.write_text(s,encoding='utf-8')
