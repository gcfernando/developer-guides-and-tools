import tempfile
import unittest
from pathlib import Path
from inspect_data import profile


class DataTests(unittest.TestCase):
    def test_known_fixture(self):
        result = profile(Path(__file__).with_name("customers.csv"))
        self.assertEqual(result, {"rows": 4, "columns": 3, "missing": {
            "customer_id": 0, "age": 2, "city": 1}, "duplicate_rows": 1})

    def test_changed_fixture_is_measured(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "small.csv"
            path.write_text("id,value\n1,a\n2,b\n", encoding="utf-8")
            self.assertEqual(profile(path)["duplicate_rows"], 0)


if __name__ == "__main__":
    unittest.main()
