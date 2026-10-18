"""Expand figure placeholders.

    fillfig.py PAGEFILE...            in place
    fillfig.py --to OUTFILE SRCFILE   write expanded SRCFILE to OUTFILE
Placeholders: `@@FIG name` (sci5_figs.FIGS), `@@MM centre|id|top|bottom|left|right` (mindmap5.py).
"""
import sys, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sci5_figs


def expand(text):
    out = []
    for line in text.split('\n'):
        if line.startswith('@@FIG '):
            out.append(sci5_figs.FIGS[line[6:].strip()]())
        elif line.startswith('@@MM '):
            out.append(subprocess.run([sys.executable, str(Path(__file__).with_name('mindmap5.py')), *line[5:].split('|')],
                                      capture_output=True, text=True, encoding='utf-8').stdout.rstrip('\n'))
        else:
            out.append(line)
    return '\n'.join(out)


args = sys.argv[1:]
if args and args[0] == '--to':
    Path(args[1]).write_text(expand(Path(args[2]).read_text(encoding='utf-8')), encoding='utf-8')
else:
    for f in args:
        p = Path(f)
        p.write_text(expand(p.read_text(encoding='utf-8')), encoding='utf-8')
