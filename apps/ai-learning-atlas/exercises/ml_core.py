"""Tiny, deterministic ML calculations. Python 3.10+, standard library only.

These are teaching fixtures, not estimates of deployment performance.
Run: python ml_core.py
"""
from math import sqrt


def wilson(successes, n, z=1.959963984540054):
    """Two-sided 95% Wilson interval for independent Bernoulli trials."""
    p = successes / n
    denominator = 1 + z*z/n
    center = (p + z*z/(2*n)) / denominator
    radius = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / denominator
    return center-radius, center+radius


def leakage():
    # Split before learning any preprocessing parameters. Labels are synthetic.
    train = [(0, 0), (1, 1)]
    train_y = [0, 1]
    validation = [(0.9, 0), (0.1, 100)]
    validation_y = [1, 0]
    test = [(0.8, 0), (0.2, 90)]  # Kept out of the correct scaler fit.

    def score(fit_rows):
        lo = [min(row[j] for row in fit_rows) for j in range(2)]
        span = [max(row[j] for row in fit_rows)-lo[j] for j in range(2)]
        def scale(row):
            return [(row[j]-lo[j])/(span[j] or 1) for j in range(2)]
        transformed = [scale(row) for row in train]
        predictions = []
        for row in validation:
            value = scale(row)
            distances = [sum((a-b)**2 for a, b in zip(value, candidate)) for candidate in transformed]
            predictions.append(train_y[min(range(len(distances)), key=distances.__getitem__)])
        return predictions, sum(a == b for a, b in zip(predictions, validation_y))/len(validation_y)

    return {'train_only': score(train), 'leaked_all': score(train+validation+test)}


def solve(matrix, vector):
    """Small pivoted Gaussian elimination; unsuitable for ill-conditioned large data."""
    a = [list(row)+[value] for row, value in zip(matrix, vector)]
    n = len(vector)
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(a[row][column]))
        a[column], a[pivot] = a[pivot], a[column]
        divisor = a[column][column]
        if abs(divisor) < 1e-12:
            raise ValueError('Singular teaching system')
        a[column] = [v/divisor for v in a[column]]
        for row in range(n):
            if row != column:
                factor = a[row][column]
                a[row] = [v-factor*w for v, w in zip(a[row], a[column])]
    return [row[-1] for row in a]


def overfitting():
    xs = [-1, -0.6, -0.2, 0.2, 0.6, 1]
    noise = [0.1, -0.1, 0.1, -0.1, 0.1, -0.1]
    ys = [x*x+e for x, e in zip(xs, noise)]
    validation = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9]
    rows = []
    for degree in (1, 2, 5):
        matrix = [[sum(x**(i+j) for x in xs) for j in range(degree+1)] for i in range(degree+1)]
        vector = [sum(y*x**i for x, y in zip(xs, ys)) for i in range(degree+1)]
        coefficients = solve(matrix, vector)
        def predict(x):
            return sum(c*x**i for i, c in enumerate(coefficients))
        train_mse = sum((predict(x)-y)**2 for x, y in zip(xs, ys))/len(xs)
        validation_mse = sum((predict(x)-x*x)**2 for x in validation)/len(validation)
        rows.append((degree, train_mse, validation_mse))
    return rows


def confusion():
    actual = [1, 1, 1, 0, 0, 0]
    predicted = [1, 0, 1, 1, 0, 0]
    tp = sum(y == 1 and p == 1 for y, p in zip(actual, predicted))
    fp = sum(y == 0 and p == 1 for y, p in zip(actual, predicted))
    fn = sum(y == 1 and p == 0 for y, p in zip(actual, predicted))
    tn = sum(y == 0 and p == 0 for y, p in zip(actual, predicted))
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    return {'TP': tp, 'FP': fp, 'FN': fn, 'TN': tn,
            'precision': precision, 'recall': recall,
            'F1': 2*precision*recall/(precision+recall)}


def calibration():
    probabilities = [0.2, 0.2, 0.8, 0.8]
    outcomes = [0, 1, 1, 1]
    # These two fixed bins each contain two cases. A curve plots these pairs.
    return [(sum(probabilities[i:i+2])/2, sum(outcomes[i:i+2])/2) for i in (0, 2)]


def gradient_descent(rate=0.1, steps=6):
    # Linear regression through the origin: y = w*x, x=1 and target y=3.
    # The mean squared error is L=(w-3)^2, gradient=2*(w-3).
    weight = 0.0
    trace = [(0, weight, (weight-3)**2)]
    for step in range(1, steps+1):
        weight -= rate*2*(weight-3)
        trace.append((step, weight, (weight-3)**2))
    return trace


def clustering():
    # One-dimensional k-means, specified starting centers, deterministic ties.
    points, centers = [0, 2, 8, 10], [0, 8]
    assignments = [min(range(2), key=lambda j: abs(x-centers[j])) for x in points]
    updated = [sum(x for x, group in zip(points, assignments) if group == j)/assignments.count(j) for j in range(2)]
    return assignments, updated


def cross_validation():
    # Three predefined folds: training-mean baseline versus fitted y=slope*x.
    data = [(0, 0), (1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
    baseline, model = [], []
    for fold in range(3):
        train = [row for i, row in enumerate(data) if i % 3 != fold]
        validation = [row for i, row in enumerate(data) if i % 3 == fold]
        mean_y = sum(y for _, y in train)/len(train)
        slope = sum(x*y for x, y in train)/sum(x*x for x, _ in train)
        baseline.append(sum(abs(mean_y-y) for _, y in validation)/len(validation))
        model.append(sum(abs(slope*x-y) for x, y in validation)/len(validation))
    from statistics import mean, stdev
    return {'baseline_MAE': (mean(baseline), stdev(baseline)),
            'fitted_linear_MAE': (mean(model), stdev(model))}


def main():
    print('Leakage:', leakage())
    for degree, training, validation in overfitting():
        print(f'Polynomial degree {degree}: train MSE={training:.6f}; validation MSE={validation:.6f}')
    print('Confusion:', confusion())
    print('Calibration (mean probability, observed frequency):', calibration())
    for successes, n in ((4, 5), (80, 100)):
        lower, upper = wilson(successes, n)
        print(f'Wilson 95% {successes}/{n}: [{lower:.6f}, {upper:.6f}]')
    print('Gradient descent eta=0.1 (step, weight, loss):', gradient_descent())
    print('Overshoot eta=2 (step, weight, loss):', gradient_descent(2, 3))
    print('K-means (assignments, updated centers):', clustering())
    print('Three-fold fixture mean/sample SD:', cross_validation())


if __name__ == '__main__':
    main()
