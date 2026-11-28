"""Check both commands and the documented request change in a disposable copy."""
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import runpy
import shutil
import tempfile

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def run(path):
    output = io.StringIO()
    with redirect_stdout(output):
        runpy.run_path(str(path), run_name='__main__')
    return output.getvalue()


def main():
    with tempfile.TemporaryDirectory(prefix='ml-saved-workflow-') as temporary:
        folder = Path(temporary) / 'train-and-test'
        shutil.copytree(ROOT / 'lessons' / 'train-and-test', folder)
        training_output = run(folder / 'train_delivery_model.py')
        artifact = folder / 'delivery_model.joblib'
        saved_hash = hashlib.sha256(artifact.read_bytes()).hexdigest()
        original_output = run(folder / 'test_delivery_model.py')
        requests = pd.read_csv(folder / 'new_deliveries.csv')
        requests.loc[0, 'weight_kg'] = np.nan
        requests.loc[0, 'actual_minutes'] = np.nan
        requests.to_csv(folder / 'new_deliveries.csv', index=False)
        changed_output = run(folder / 'test_delivery_model.py')
        model = joblib.load(artifact)
        predictions = model.predict(requests[['distance_km', 'weight_kg', 'zone']])
        assert len(predictions) == len(requests) == 4
        assert np.isfinite(predictions).all()
        errors = (requests['actual_minutes'] - predictions).abs()
        assert errors.notna().sum() == 2
        assert f'{errors.mean():.2f} minutes.' in changed_output
        assert hashlib.sha256(artifact.read_bytes()).hexdigest() == saved_hash
    report = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'passed': True,
        'checks': ['Both documented commands run.',
                   'All four requests receive finite estimates, including a changed blank weight.',
                   'Error uses only the two remaining measured answers.',
                   'Prediction preserves the saved model bytes.'],
        'training_output': training_output,
        'original_request_output': original_output,
        'changed_request_output': changed_output,
        'method': 'Trusted local source; temporary copy. Not a learner study.'
    }
    (ROOT / 'course-review' / 'workflow-checks.json').write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('Saved-model workflow passed: training, prediction, blank weight, measured-only errors, unchanged artifact.')


if __name__ == '__main__':
    main()
