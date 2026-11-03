"""Offline contract tests; no provider or account is contacted."""
import json
import unittest
from model_adapter import MockModel, RealModel, estimate_cost, observe, validate_response


class ModelAdapterTests(unittest.TestCase):
    def test_mock_three_observations(self):
        rows = observe(MockModel())
        self.assertEqual(len(rows), 3)
        self.assertEqual([r['response']['source'] for r in rows], ['public-hours']*3)
        self.assertTrue(all(r['seconds'] >= 0 for r in rows))

    def test_malformed_response_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_response(MockModel().generate('malformed'))

    def test_schema_contract_requires_fields_types_and_no_extras(self):
        for value in [[], {}, {'answer': 1, 'source': None}, {'answer': 'ok', 'source': False},
                      {'answer': 'ok', 'source': None, 'extra': 'field'}]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_response(json.dumps(value))
        self.assertEqual(validate_response('{"answer":"unknown","source":null}')['source'], None)

    def test_real_model_is_explicitly_unimplemented(self):
        with self.assertRaises(NotImplementedError):
            RealModel().generate('hours')

    def test_symbolic_cost_arithmetic_not_actual_provider_pricing(self):
        # Arbitrary fixture rates of 2 and 4 currency units, not market prices.
        self.assertEqual(estimate_cost(1_000_000, 500_000, 2, 4), 4)
        with self.assertRaises(ValueError):
            estimate_cost(-1, 0, 2, 4)
        for rate in (float('nan'), float('inf'), -1, True):
            with self.subTest(rate=rate), self.assertRaises(ValueError):
                estimate_cost(1, 1, rate, 4)


if __name__ == '__main__':
    unittest.main()
