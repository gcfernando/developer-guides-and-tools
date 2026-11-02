import unittest
from clean_data import clean


class CleaningTests(unittest.TestCase):
    def test_exact_duplicate_and_missing_value(self):
        row = {"customer_id": "2", "age": "", "city": "Stockholm"}
        accepted, conflicts = clean([row, row.copy()])
        self.assertEqual(accepted, [row])
        self.assertEqual(accepted[0]["age"], "")
        self.assertEqual(conflicts, [])

    def test_conflicting_identifier_quarantines_both_versions(self):
        rows = [{"customer_id": "2", "city": "Stockholm"},
                {"customer_id": "2", "city": "Gothenburg"}]
        accepted, conflicts = clean(rows)
        self.assertEqual(accepted, [])
        self.assertEqual(conflicts, rows)

    def test_missing_identifier_is_rejected(self):
        with self.assertRaises(ValueError):
            clean([{"customer_id": " ", "age": "34"}])
