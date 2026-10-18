"""Replace `@@RAD centre|label...` (radial5.py) and `@@COLS title|Head:a;b|...` (cols5.py) lines in page files with SVG.  fillrad.py PAGEFILE..."""
import sys, subprocess
from pathlib import Path
TOOLS = {'@@RAD ': 'radial5.py', '@@COLS ': 'cols5.py', '@@TL ': 'timeline5.py', '@@GLOBE ': 'globe5.py'}
for f in sys.argv[1:]:
    p = Path(f); out = []
    for line in p.read_text(encoding='utf-8').split('\n'):
        for tag, script in TOOLS.items():
            if line.startswith(tag):
                args = line[len(tag):].split('|')
                line = subprocess.run([sys.executable, str(Path(__file__).with_name(script)), *args], capture_output=True, text=True, encoding='utf-8', env={**__import__('os').environ, 'PYTHONIOENCODING': 'utf-8'}).stdout.rstrip('\n')
                break
        out.append(line)
    p.write_text('\n'.join(out), encoding='utf-8')
