"""Run added teaching labs and their documented changes in disposable copies."""

from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENV = {**os.environ, 'PYTHONUTF8': '1', 'MPLBACKEND': 'Agg',
       'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1'}


def run(folder, name):
    result = subprocess.run([sys.executable, str(folder / name)], cwd=folder,
                            env=ENV, capture_output=True, text=True,
                            encoding='utf-8', timeout=60)
    if result.returncode:
        raise AssertionError(f'{folder.name}/{name}: {result.stderr}')
    return result.stdout


def normalized(text):
    return re.sub(r'\s+', '', text)


def main():
    records = []
    sources = sorted((ROOT / 'lessons').glob('*/penalty_lab.py'))
    sources += sorted((ROOT / 'lessons').glob('*/network_bridge.py'))
    if not sources:
        raise SystemExit('No added teaching labs found.')
    with tempfile.TemporaryDirectory(prefix='ml-teaching-labs-') as temporary:
        parent = Path(temporary)
        for source in sources:
            folder = parent / source.parent.name
            if not folder.exists():
                shutil.copytree(source.parent, folder)
            output = run(folder, source.name)
            expected_name = 'penalty-expected-output.txt' if source.name == 'penalty_lab.py' else 'network-expected-output.txt'
            expected = source.parent / expected_name
            if not expected.is_file():
                raise AssertionError(f'Missing recorded output: {source.parent.name}/{expected_name}')
            if normalized(output) != normalized(expected.read_text(encoding='utf-8')):
                raise AssertionError(f'Recorded output differs: {source.parent.name}/{source.name}')
            if source.name == 'penalty_lab.py':
                import pandas as pd
                table = pd.read_csv(folder / 'coefficient-check.csv')
                high_penalty = table[(table['method'] == 'Lasso') & (table['alpha'] == 100)]
                assert len(high_penalty) == 1
                assert high_penalty[['km_coefficient', 'kg_coefficient']].abs().to_numpy().max() == 0
                winner = table.loc[table['validation_mae_minutes'].idxmin()]
                assert winner['method'] == 'Ridge' and winner['alpha'] == 1
                check = 'Coefficients shown, strong Lasso zeros observed, choice follows validation; separate frozen-choice test reported.'
            else:
                assert 'Before: prediction 2.00; squared-error loss 1.00.' in output
                assert 'After: squared-error loss 0.00.' in output
                # A larger learning rate can make this exact same training row worse.
                path = folder / source.name
                text = path.read_text(encoding='utf-8')
                assert 'learning_rate = 0.1' in text
                path.write_text(text.replace('learning_rate = 0.1', 'learning_rate = 1.0'), encoding='utf-8')
                changed = run(folder, source.name)
                assert 'After: squared-error loss 81.00.' in changed
                check = 'Original update matches output; learning-rate change to 1.0 raises loss to 81, showing updates need care.'
            records.append({'lesson': source.parent.name, 'script': source.name,
                            'expected_output_matches': True, 'behavior_check': check})
    report = {'python': sys.version.split()[0], 'checks': records,
              'method': 'Ran original examples and controlled changes in temporary copies.',
              'learner_study': 'Not performed.'}
    (ROOT / 'course-review' / 'teaching-example-checks.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'Added teaching examples passed: {len(records)}.')


if __name__ == '__main__':
    main()
