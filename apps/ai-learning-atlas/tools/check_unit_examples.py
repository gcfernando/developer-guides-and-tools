"""Recompute the authored unit reference arithmetic and observable Python traces.

These assertions check the supplied teaching examples, not a learner's work,
general model quality, or claims of production readiness. Python 3.10+ stdlib.
"""
import json
import math
from collections import Counter
from itertools import accumulate
from pathlib import Path
from statistics import mean, stdev

ROOT = Path(__file__).resolve().parents[1]
UNITS = json.loads((ROOT / 'source/units.json').read_text(encoding='utf-8'))
CHECKS = []


def check(topic, unit, actual, expected, explanation):
    if isinstance(expected, float):
        assert math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9), (topic, unit, explanation, actual, expected)
    else:
        assert actual == expected, (topic, unit, explanation, actual, expected)
    assert UNITS[str(topic)][unit - 1]['status'] == 'complete'
    CHECKS.append((topic, unit, explanation))


def mse(predicted, actual):
    return sum((p-y)**2 for p, y in zip(predicted, actual))/len(actual)


def cosine(a, b):
    return sum(x*y for x, y in zip(a, b))/math.sqrt(sum(x*x for x in a)*sum(y*y for y in b))


def main():
    check(2, 3, [4, 7, 9].index(9)+1, 3, 'linear-scan comparisons')
    check(2, 4, 1+2, 3, 'correct addition')
    check(2, 4, 1*2, 2, 'introduced multiplication regression')
    check(3, 2, dict(Counter(['red', 'blue', 'red'])), {'red': 2, 'blue': 1}, 'word frequencies')
    check(3, 3, [x*2 for x in [-1, 0, 2, 3] if x > 0], [4, 6], 'positive filter')
    check(3, 3, [x*2 for x in [-1, 0, 2] if x >= 0], [0, 4], 'nonnegative practice result')
    check(3, 4, int('12'), 12, 'integer conversion')
    try:
        int('twelve')
    except ValueError:
        check(3, 4, True, True, 'invalid integer raises ValueError')
    else:
        raise AssertionError('Expected ValueError')
    check(3, 5, sum([1, 2, 3]), 6, 'standard-library sum')
    check(4, 1, sum(a*b for a, b in zip([1, 0], [1, 1])), 1, 'dot product')
    check(4, 1, cosine([1, 0], [1, 1]), 1/math.sqrt(2), 'cosine')
    check(4, 1, cosine([1, 0], [2, 2]), cosine([1, 0], [1, 1]), 'positive-scale invariance')
    check(4, 1, round(cosine([1, 0], [1, 1]), 3), 0.707, 'displayed cosine rounding')
    for topic, unit in [(4, 2), (12, 2)]:
        check(topic, unit, 2*(0-3), -6, 'quadratic derivative')
        check(topic, unit, 0-0.1*2*(0-3), 0.6, 'gradient step')
        check(topic, unit, (0.6-3)**2, 5.76, 'updated loss')
        check(topic, unit, (0-3)**2, 9, 'initial loss')
        check(topic, unit, 0-2*2*(0-3), 12, 'overshooting weight')
        check(topic, unit, (12-3)**2, 81, 'overshooting loss')
    check(4, 2, 2*(1-3), -4, 'question derivative')
    check(4, 2, 1-0.1*2*(1-3), 1.4, 'question update')
    check(4, 2, (1.4-3)**2, 2.56, 'question loss')
    check(4, 3, round(100*8/(8+9)), 47, 'precision percent rounding')
    check(4, 3, 8/(8+2), 0.8, 'recall')
    check(4, 3, 8/(8+4), 2/3, 'changed false positives')
    check(4, 4, 4/5, 0.8, 'small observed rate')
    check(4, 4, 80/100, 0.8, 'large observed rate')
    check(4, 4, (5/5-4/5)*100, 20.0, 'fixed-n failure-to-success change n=5')
    check(4, 4, (81/100-80/100)*100, 1.0, 'fixed-n failure-to-success change n=100')
    check(4, 4, 5/5, 1.0, 'reclassified small-sample rate')
    check(4, 4, 81/100, 0.81, 'reclassified large-sample rate')
    check(4, 4, round(5/6, 6), 0.833333, 'appending a successful trial to 4/5')
    check(4, 4, round(81/101, 6), 0.801980, 'appending a successful trial to 80/100')
    check(4, 4, round((5/6-4/5)*100, 6), 3.333333, 'appended-trial percentage-point change n=5 to 6')
    check(4, 4, round((81/101-80/100)*100, 6), 0.198020, 'appended-trial percentage-point change n=100 to 101')
    check(4, 4, 3/5, 0.6, 'changed small sample')
    check(4, 4, 79/100, 0.79, 'changed large sample')
    check(4, 5, round(-math.log(0.5), 3), 0.693, 'log loss 0.5')
    check(4, 5, round(-math.log(0.9), 3), 0.105, 'log loss 0.9')
    check(5, 2, 3-len({(1, 20), (1, 20), (1, 21)}), 1, 'excess duplicate row')
    check(6, 2, 1+1, 2, 'low-cost route')
    check(6, 2, (1+1) < 10, True, 'cost versus edge count')
    check(6, 3, [(a,b,c) for a in [0,1] for b in [0,1] for c in [0,1] if a!=b and b!=c and c!=a], [], 'two-color triangle infeasibility')
    check(6, 5, 0.5*10, 5, 'expected payoff')
    check(6, 5, 0.3*10, 3, 'changed expected payoff')
    check(7, 2, mse([1, 3], [1, 3]), 0, 'perfect training fit')
    check(7, 2, mse([2, 2], [1, 3]), 1, 'mean baseline squared error')
    check(7, 3, [0,0,0,1].count(0)/4, 0.75, 'majority-class baseline')
    check(7, 4, 99/100, 0.99, 'imbalanced accuracy')
    check(7, 4, 0/(0+1), 0, 'zero positive recall')
    inputs, targets = [1, 2], [1, 3]
    predictions_a = [1*x for x in inputs]
    predictions_b = [1.5*x for x in inputs]
    check(8, 1, predictions_a, [1, 2], 'candidate A predictions')
    check(8, 1, predictions_b, [1.5, 3.0], 'candidate B predictions')
    check(8, 1, mse(predictions_a, targets), 0.5, 'candidate A MSE')
    check(8, 1, mse(predictions_b, targets), 0.125, 'candidate B MSE')
    check(8, 1, 0.5*1**2, 0.5, 'candidate A coefficient penalty')
    check(8, 1, 0.5*1.5**2, 1.125, 'candidate B coefficient penalty')
    check(8, 1, mse(predictions_a, targets)+0.5*1**2, 1.0, 'candidate A objective at lambda 0.5')
    check(8, 1, mse(predictions_b, targets)+0.5*1.5**2, 1.25, 'candidate B objective at lambda 0.5')
    check(8, 1, 0.1*1**2, 0.1, 'candidate A practice penalty')
    check(8, 1, 0.1*1.5**2, 0.225, 'candidate B practice penalty')
    check(8, 1, mse(predictions_a, targets)+0.1*1**2, 0.6, 'candidate A practice objective')
    check(8, 1, mse(predictions_b, targets)+0.1*1.5**2, 0.35, 'candidate B practice objective')
    check(8, 2, min([(abs(2-0), 'A'), (abs(2-10), 'B')])[1], 'A', 'one-neighbor decision')
    check(8, 3, int(sum([1,1,0]) > len([1,1,0])/2), 1, 'majority vote')
    # These are supplied fold-error fixtures, not claims of model training.
    fold_errors = {
        'training-mean baseline': ([4, 5, 6], 5, 1),
        'linear candidate': ([2, 3, 4], 3, 1),
        'tree candidate': ([1, 3, 2], 2, 1),
        'bagged candidate': ([2, 2, 5], 3, math.sqrt(3)),
    }
    for name, (errors, expected_mean, expected_sd) in fold_errors.items():
        check(8, 3, mean(errors), expected_mean, name+' supplied-fold mean MAE')
        check(8, 3, stdev(errors), expected_sd, name+' supplied-fold sample SD')
    check(8, 3, round(stdev([2, 2, 5]), 6), 1.732051, 'bagged sample SD display')
    check(8, 3, mean([2, 2, 8]), 4, 'changed bagged-fold mean')
    check(8, 3, stdev([2, 2, 8]), math.sqrt(12), 'changed bagged-fold sample SD')
    check(8, 4, 9/10, 0.9, 'matching baseline accuracy')
    check(9, 1, [min([0.5,9.5],key=lambda c:abs(x-c)) for x in [0,1,9,10]], [0.5,0.5,9.5,9.5], 'nearest-centroid groups')
    check(9, 3, 3/4, 0.75, 'association confidence')
    check(9, 3, 3/10, 0.3, 'association support')
    check(10, 2, 8/(8+2), 0.8, 'precision')
    check(10, 2, round(8/(8+4), 3), 0.667, 'recall rounding')
    check(10, 2, 2*8/(2*8+2+4), 8/11, 'F1')
    check(10, 2, round(2*8/(2*8+2+4), 3), 0.727, 'F1 rounding')
    check(10, 2, (8+6)/(8+2+4+6), 0.7, 'accuracy')
    check(10, 3, sum([0.8]*10)/10, 0.8, 'calibration mean forecast')
    check(10, 3, 6/10, 0.6, 'calibration observed frequency')
    check(10, 3, abs(0.8-0.6), 0.2, 'calibration observed gap')
    check(10, 4, 9-8, 1, 'one-case development difference')
    check(11, 1, sum([20,40])/2, 30, 'training-only mean')
    check(11, 1, round(sum([20,40,100])/3, 2), 53.33, 'leaked mean rounding')
    check(11, 1, sum([2,4])/2, 3, 'practice training mean')
    check(12, 1, 2*1+(-1)*3+2, 1, 'neuron preactivation')
    check(12, 1, max(0,2*1+(-1)*3+2), 1, 'ReLU output')
    check(12, 1, max(0,(-2)*1+1*3+2), 3, 'question neuron')
    check(12, 3, min(range(3),key=lambda i:[3,2.2,2.8][i])+1, 2, 'validation-selected checkpoint')
    check(12, 4, 2+0.5, 2.5, 'residual output')
    check(12, 4, 2+0, 2, 'identity residual')
    check(13, 1, [3-1,1-4], [2,-3], 'cross-correlation')
    check(13, 2, list(accumulate([2,-1,3])), [2,1,4], 'recurrent sum trace')
    check(15, 1, 0.25*2+0.75*6, 5, 'attention weighted sum')
    check(15, 1, 0.6*1+0.4*4, 2.2, 'practice attention')
    check(15, 2, [[int(j<=i) for j in range(3)] for i in range(3)], [[1,0,0],[1,1,0],[1,1,1]], 'causal visibility matrix')
    check(15, 3, [4**2,8**2], [16,64], 'dense position-pair counts')
    check(15, 3, 20**2/10**2, 4, 'doubling pair-count ratio')
    check(15, 4, list(range(5-2,5+1)), [3,4,5], 'sliding window including self')
    check(16, 2, 100-70, 30, 'hypothetical total token budget')
    check(17, 2, isinstance(json.loads('{"count":4}')['count'], int), True, 'JSON integer type')
    check(18, 1, round(cosine([1,0],[1,1]),4), 0.7071, 'embedding cosine rounding')
    check(18, 1, cosine([1,0],[2,2]), cosine([1,0],[1,1]), 'embedding scale invariance')
    check(18, 4, 1/2, 0.5, 'recall at cutoff')
    check(20, 2, 4*4, 16, 'full update entries')
    check(20, 2, 4*1+1*4, 8, 'rank-one factors')
    check(20, 2, 10*2+2*10, 40, 'practice factor entries')
    check(21, 2, 2+1, 3, 'known-noise corruption')
    check(21, 2, 3-1, 2, 'known-noise removal')
    check(22, 1, sum([0,100])/2, 50, 'pixel averaging')
    check(23, 1, 32000/16000, 2, 'audio duration')
    check(23, 1, 48000/16000, 3, 'practice duration')
    check(25, 1, 2+0.5*4, 4, 'discounted return')
    check(25, 1, 1+0.5*0+0.5**2*4, 2, 'practice discounted return')
    check(25, 2, 1+0.9*4, 4.6, 'Q target')
    check(25, 2, 2+0.5*(1+0.9*4-2), 3.3, 'Q update')
    check(25, 2, 2+0.5*(1-2), 1.5, 'terminal Q update')
    check(25, 3, max(range(2),key=[1,3].__getitem__), 1, 'greedy action B index')
    check(25, 3, sum([0.2,0.8]), 1, 'policy probability normalization')
    check(30, 4, 90+10, 100, 'request accounting')
    check(31, 1, 20/2, 10, 'batch throughput')
    check(31, 1, 24/2, 12, 'practice throughput')
    check(31, 2, 0.26*2, 0.52, 'full precision output')
    check(31, 2, 0.3*2, 0.6, 'rounded output')
    check(31, 2, abs(0.3*10-0.26*10), 0.4, 'practice rounding error')
    check(31, 3, 3+1, 4, 'cold-start total')
    check(31, 5, 10/8, 1.25, 'system A illustrative cost per success')
    check(31, 5, 12/12, 1, 'system B illustrative cost per success')
    check(31, 5, 12/6, 2, 'changed illustrative success rate')
    check(32, 2, 2*3*4, 24, 'effective batch size')
    check(32, 2, 3*3*2, 18, 'practice effective batch size')
    check(32, 3, (2+4)/2, 3, 'equal-size gradient mean')
    check(32, 3, (2*2+4*6)/8, 3.5, 'weighted gradient mean')
    check(33, 1, [3/4,1/4], [0.75,0.25], 'correct and abstention rates')
    human=['pass','fail','pass','fail']; judge=['pass','pass','pass','fail']
    check(33, 2, sum(a==b for a,b in zip(human,judge))/len(human), 0.75, 'raw judge-human agreement')
    check(35, 4, len(set(['a','a','b'])), 2, 'distinct events')
    check(35, 4, len(['a','a','b']), 3, 'delivered rows')
    check(36, 2, [2,1+3,2], [2,4,2], 'neighbor sums without self')
    check(36, 2, 1+2+3, 6, 'self-inclusive B update')
    check(37, 1, [10,20,11,21][-2:], [11,21], 'seasonal naive period two')
    check(37, 1, [3,8,4,9][-2:], [4,9], 'practice seasonal naive')
    check(37, 2, sum([2,4,6])/3, 4, 'moving-average forecast')
    check(37, 2, sum([6,8])/2, 7, 'practice moving average')
    # Both forecast rules receive only the expanding past, with horizon one.
    observations = [10, 20, 12, 22, 14, 24, 16]
    reference_rows = [(5, 14, 12, 2, 17, 3),
                      (6, 24, 22, 2, 18, 6),
                      (7, 16, 14, 2, 19, 3)]
    seasonal_errors, candidate_errors = [], []
    for origin, reference in zip([4, 5, 6], reference_rows):
        past = observations[:origin]
        seasonal_forecast = past[-2]
        candidate_forecast = mean(past[-2:])
        actual = observations[origin]
        seasonal_error = abs(actual-seasonal_forecast)
        candidate_error = abs(actual-candidate_forecast)
        check(37, 4, origin+1, reference[0], 'rolling-origin target time')
        check(37, 4, actual, reference[1], 'rolling-origin target value')
        check(37, 4, seasonal_forecast, reference[2], 'past-only seasonal-naive forecast')
        check(37, 4, seasonal_error, reference[3], 'seasonal-naive absolute error')
        check(37, 4, candidate_forecast, reference[4], 'past-only two-point candidate forecast')
        check(37, 4, candidate_error, reference[5], 'candidate absolute error')
        seasonal_errors.append(seasonal_error)
        candidate_errors.append(candidate_error)
    check(37, 4, mean(seasonal_errors), 2, 'seasonal-naive rolling-origin MAE')
    check(37, 4, mean(candidate_errors), 4, 'candidate rolling-origin MAE')
    check(37, 4, observations[-2], 24, 'origin-seven seasonal forecast')
    check(37, 4, mean(observations[-2:]), 20, 'origin-seven candidate forecast')
    check(37, 4, abs(26-observations[-2]), 2, 'origin-seven seasonal absolute error')
    check(37, 4, abs(26-mean(observations[-2:])), 6, 'origin-seven candidate absolute error')
    relevance = [True, False, True]
    check(38, 2, sum(relevance)/len(relevance), 2/3, 'precision at three')
    check(39, 3, sum([4,6])/2-sum([3,3])/2, 2, 'observed mean difference')
    check(39, 3, sum([4,2])/2-sum([3,3])/2, 0, 'changed observed difference')
    check(39, 4, 0.4*10-1, 3, 'expected net A')
    check(39, 4, 4-2, 2, 'certain net B')
    check(39, 4, 0.2*10-1, 1, 'changed expected net A')
    check(40, 1, [1+3,2+0], [4,2], 'coordinate translation')
    check(40, 1, [2+3,-1+4], [5,3], 'practice translation')
    check(40, 2, 2>1, True, 'body wider than gap')
    check(40, 3, 2*(5-3), 4, 'proportional command')
    check(40, 3, min(3,max(-3,2*(5-3))), 3, 'command saturation')
    check(42, 1, sum(a!=b for a in [False,True] for b in [False,True]), 2, 'exactly-one assignments')
    check(42, 2, [x+1 for x in [1,2]], [2,3], 'example-fitting program')
    check(43, 3, 8/10-4/10, 0.4, 'old-task regression size')
    check(44, 4, 4<=8<=6, False, 'held-out value outside interval')
    check(47, 2, 9/(9+1), 0.9, 'majority baseline')
    print(f'PASS {len(CHECKS)} numeric/Python reference assertions across {len(set((t,u) for t,u,_ in CHECKS))} authored units.')
    print('Checks cover worked calculations and numeric answer keys; illustrative IDs, dates, budgets and scenario constants are assumptions, not empirical claims.')


if __name__ == '__main__':
    main()
