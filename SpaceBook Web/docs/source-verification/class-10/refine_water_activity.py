from pathlib import Path
p=Path(r'D:\SpaceBook\SpaceBook Web\js\physics_10_source_data.js')
s=p.read_text(encoding='utf-8')
s=s.replace('amplitude:16,wavelength:90,phases:', 'amplitude:16,wavelength:90,pulseStarts:[55,77.5,100,122.5,145],phases:')
s=s.replace('const samples=Array.from({length:181},(_,n)=>{const x=35+n;return [x,y-16*Math.sin(2*Math.PI*(x-145)/90-phase)];});const corkY=y-16*Math.sin(-phase);', 'const pulseStart=cork19.geometry.pulseStarts[i];const surface=x=>(x<pulseStart||x>pulseStart+90)?y:y-16*Math.sin(2*Math.PI*(x-pulseStart)/90);const samples=Array.from({length:211},(_,n)=>{const x=35+n;return [x,surface(x)];});const corkY=surface(145);')
s=s.replace('L215 ${y+45}Z','L245 ${y+45}Z')
p.write_text(s,encoding='utf-8')
