"""Execute every runnable ML snippet and compare the exact reference stdout."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
labs = json.loads((ROOT/'source/ml-labs.json').read_text(encoding='utf-8'))
failed = []
for number, lab in labs.items():
    result = subprocess.run([sys.executable, '-B', '-c', lab['code']], cwd=ROOT/'exercises',
                            text=True, capture_output=True, encoding='utf-8')
    success = result.returncode == 0 and result.stdout.rstrip() == lab['expected'].rstrip()
    print(('PASS' if success else 'FAIL')+f' Topic {int(number):02} exact ML reference output')
    if not success:
        failed.append(number)
        print('ACTUAL', repr(result.stdout), 'EXPECTED', repr(lab['expected']), result.stderr)
print(f'{len(labs)-len(failed)}/{len(labs)} runnable ML snippets match their reference output; Python {sys.version.split()[0]}')
raise SystemExit(1 if failed else 0)
