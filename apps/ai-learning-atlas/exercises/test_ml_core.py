"""Independent expected arithmetic for the bounded ML fixtures."""
import unittest
import ml_core as ml


class MLCoreTests(unittest.TestCase):
    def test_leakage_changes_validation_predictions(self):
        result = ml.leakage()
        self.assertEqual(result['train_only'], ([0, 1], 0.0))
        self.assertEqual(result['leaked_all'], ([1, 0], 1.0))

    def test_overfitting_measured_trend(self):
        linear, quadratic, interpolating = ml.overfitting()
        self.assertLess(quadratic[2], linear[2])
        self.assertLess(interpolating[1], quadratic[1])
        self.assertGreater(interpolating[2], quadratic[2])

    def test_confusion_denominators(self):
        result = ml.confusion()
        self.assertEqual([result[x] for x in ('TP', 'FP', 'FN', 'TN')], [2, 1, 1, 2])
        for metric in ('precision', 'recall', 'F1'):
            self.assertAlmostEqual(result[metric], 2/3)

    def test_calibration_bins(self):
        self.assertEqual(ml.calibration(), [(0.2, 0.5), (0.8, 1.0)])

    def test_wilson_independent_reference_values(self):
        for pair, expected in [((4, 5), (0.3755346, 0.9637759)),
                               ((80, 100), (0.7111708, 0.8666331))]:
            result = ml.wilson(*pair)
            for actual, reference in zip(result, expected):
                self.assertAlmostEqual(actual, reference, places=5)

    def test_gradient_and_overshoot(self):
        self.assertAlmostEqual(ml.gradient_descent()[1][1], 0.6)
        self.assertAlmostEqual(ml.gradient_descent()[1][2], 5.76)
        self.assertEqual(ml.gradient_descent(2, 1)[1], (1, 12.0, 81.0))

    def test_clustering_update(self):
        self.assertEqual(ml.clustering(), ([0, 0, 1, 1], [1.0, 9.0]))

    def test_cv_has_baseline_and_sample_sd(self):
        self.assertEqual(ml.cross_validation(), {'baseline_MAE': (3.0, 0.0), 'fitted_linear_MAE': (0, 0.0)})


if __name__ == '__main__':
    unittest.main()
