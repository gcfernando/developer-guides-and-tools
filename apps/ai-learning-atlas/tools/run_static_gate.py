"""Record real authoring checks after one workstream; browser checks run separately."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workstream')
    parser.add_argument('--final', action='store_true')
    args = parser.parse_args()
    folder = ROOT/'tools/results'
    folder.mkdir(exist_ok=True)
    stage = 'final' if args.final else 'ws1'
    commands = {
        'check': [sys.executable, '-B', 'tools/check_atlas.py', '--stage', stage],
        'runtime': ['node', '--test', 'runtime.test.cjs'],
        'examples': [sys.executable, '-B', 'tools/check_unit_examples.py'],
        'diff': ['git', 'diff', '--check'],
    }
    report = {'workstream': args.workstream,
              'page_sha256': hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(), 'checks': {}}
    for label, command in commands.items():
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, encoding='utf-8')
        output = result.stdout+result.stderr
        (folder/f'{args.workstream}-{label}.txt').write_text(output, encoding='utf-8')
        report['checks'][label] = {'exit': result.returncode, 'command': command}
        print(f'{label}: exit {result.returncode}; '+(output.strip().splitlines()[-1] if output.strip() else 'no output'))
    java = Path('C:/Program Files/Java/jdk-17/bin/java.exe')
    jar = REPO/'.runtime/atlas-tools/node_modules/vnu-jar/build/dist/vnu.jar'
    result = subprocess.run([str(java), '-jar', str(jar), '--format', 'json', str(ROOT/'index.html')],
                            text=True, capture_output=True, encoding='utf-8')
    validation = json.loads(result.stdout or result.stderr)
    (folder/f'{args.workstream}-nu.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    errors = [m for m in validation['messages'] if m['type'] == 'error']
    report['checks']['nu'] = {'exit': result.returncode, 'errors': len(errors),
                              'other_messages': len(validation['messages'])-len(errors), 'version': validation['version']}
    print(f'Nu: exit {result.returncode}; {len(errors)} errors; {len(validation["messages"])-len(errors)} other messages')
    (folder/f'{args.workstream}-static.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    return 1 if any(check['exit'] != 0 for check in report['checks'].values()) else 0


if __name__ == '__main__':
    raise SystemExit(main())
