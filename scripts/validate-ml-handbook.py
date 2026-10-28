"""Validate the preserved ML bundle; --smoke runs the model in a temporary workspace."""
from pathlib import Path
import argparse
import ast
import csv
import hashlib
import importlib
import json
import math
import os
import sqlite3
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "examples/machine-learning/ml-handbook"
sys.dont_write_bytecode = True

def validate(smoke=False):
    records = []
    for file in sorted(BUNDLE.rglob("*")):
        if not file.is_file():
            continue
        rel = file.relative_to(BUNDLE).as_posix()
        if file.suffix == ".csv":
            with file.open(encoding="utf-8-sig", newline="") as stream:
                rows = list(csv.reader(stream))
            assert rows and rows[0], f"Missing CSV header: {rel}"
            assert all(len(row) == len(rows[0]) for row in rows), f"Inconsistent CSV columns: {rel}"
            records.append({"path":rel,"type":"csv","rows":len(rows)-1,"columns":rows[0]})
        elif file.suffix == ".jsonl":
            rows = [json.loads(line) for line in file.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
            assert rows and all(isinstance(row,dict) for row in rows), rel
            records.append({"path":rel,"type":"jsonl","rows":len(rows),"columns":list(rows[0])})
        elif file.suffix == ".db":
            with sqlite3.connect(file.resolve().as_uri()+"?mode=ro",uri=True) as connection:
                assert connection.execute("PRAGMA integrity_check").fetchone() == ("ok",), rel
                tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")]
                counts = {table:connection.execute('SELECT COUNT(*) FROM "'+table.replace('"','""')+'"').fetchone()[0] for table in tables}
            records.append({"path":rel,"type":"sqlite","tables":counts})
        elif file.suffix == ".py":
            ast.parse(file.read_text(encoding="utf-8-sig"),filename=rel)
    image_files = sorted((BUNDLE/"images").glob("*.png"))
    assert len(image_files) == 91, "Expected all 91 supplied figures"
    for file in image_files:
        assert file.read_bytes().startswith(bytes([137,80,78,71,13,10,26,10])), file
    report={"dataset_files":len(records),"images":len(image_files),"datasets":records,"python_syntax":"passed"}
    if smoke:
        os.environ.setdefault("OMP_NUM_THREADS","2")
        os.environ.setdefault("OPENBLAS_NUM_THREADS","1")
        sys.path.insert(0,str(BUNDLE/"tkinter_app"))
        service=importlib.import_module("model_service")
        artifacts=ROOT/"artifacts/ml-validation"
        artifacts.mkdir(parents=True,exist_ok=True)
        previous=Path.cwd()
        with tempfile.TemporaryDirectory(dir=artifacts) as temporary:
            try:
                os.chdir(temporary)
                version,metrics=service.train_first_model(BUNDLE/"tkinter_app/houses_2025.csv")
                assert version==1 and service.current_version()==1
                assert math.isfinite(metrics["mae"]) and math.isfinite(metrics["r2"])
                inputs={"area_m2":120,"bedrooms":3,"age_years":15,"distance_km":4,"has_garden":1}
                price,used=service.predict_price(inputs)
                assert used==1 and math.isfinite(price) and price>0
                try:
                    service.check_inputs({**inputs,"has_garden":2})
                    raise AssertionError("Invalid input was accepted")
                except ValueError:
                    pass
                updated=service.update_with_new_data(BUNDLE/"tkinter_app/houses_2026_new.csv")
                assert updated["new_version"]==2
                assert set(service.history()["version"])=={1,2}
                service.rollback(1)
                assert service.current_version()==1
                reloaded,reloaded_version=service.predict_price(inputs)
                assert reloaded_version==1 and math.isclose(price,reloaded)
                try:
                    service.update_with_new_data(BUNDLE/"tkinter_app/houses_2026_new.csv")
                    raise AssertionError("Repeated update was accepted")
                except ValueError:
                    pass
                report["model_smoke"]={"status":"passed","train_metrics":metrics,"first_prediction":price,"update":updated,"rollback":"passed","duplicate_update":"rejected","gui":"not opened"}
            finally:
                os.chdir(previous)
        import pandas,sklearn,joblib
        report["versions"]={"python":sys.version.split()[0],"pandas":pandas.__version__,"scikit-learn":sklearn.__version__,"joblib":joblib.__version__}
    return report

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke",action="store_true")
    parser.add_argument("--report",type=Path)
    args=parser.parse_args()
    report=validate(args.smoke)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,indent=2)+chr(10),encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="datasets"},indent=2))
