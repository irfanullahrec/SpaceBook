"""Replace `@@MM centre|id` lines in page files with SVG from mindmap5.py.  fillmm.py PAGEFILE..."""
import sys, subprocess
from pathlib import Path
for f in sys.argv[1:]:
    p = Path(f); out = []
    for line in p.read_text(encoding='utf-8').split('\n'):
        if line.startswith('@@MM '):
            args = line[5:].split('|')
            out.append(subprocess.run([sys.executable, str(Path(__file__).with_name('mindmap5.py')), *args], capture_output=True, text=True, encoding='utf-8').stdout.rstrip('\n'))
        else:
            out.append(line)
    p.write_text('\n'.join(out), encoding='utf-8')
