# A small start with Python

[Back to the learning path](LEARNING-PATH.md)

Read [Start here](START-HERE.md) and finish [Setup](SETUP.md) first. This page explains the Python you will see in the first lessons. You do not need to remember every symbol.

## 1. Give a value a name

```python
distance = 4
minutes = 10 + 2 * distance
print(minutes)
```

The first line stores 4 under the name `distance`. The second line calculates a time. Python uses `*` for multiplication. `print` shows a result. This prints `18`.

`=` means “store this value”. It is not a question about whether two values are equal.

**Try it:** Change 4 to 8. Predict the answer first. It should print 26.

## 2. Keep several values in a list

```python
distances = [1, 2, 3]
print(distances[0])
```

Square brackets can hold a list. Python starts counting positions at zero, so position 0 holds the first value, 1.

## 3. Read a table

```python
import pandas as pd
table = pd.read_csv("sample.csv")
print(table)
```

`import` makes extra tools available. `pandas` is a package for tables. `pd` is a short name for it. `read_csv` reads a CSV file. A Python table from pandas is called a **DataFrame**.

The quoted text `"sample.csv"` is a **string**: text rather than a number. Keep the quotes around text in code.

For this example, put the script beside `sample.csv` and run it from that folder.

## 4. Select the input and the answer

```python
inputs = table[["distance_km"]]
answers = table["minutes"]
```

The model wants inputs in a table. Two pairs of brackets keep `distance_km` as a one-column table. One pair selects `minutes` as one column of answers.

The column names must exactly match the first line of the CSV. `Distance` and `distance_km` are different names.

## 5. Select some rows

```python
training = table.iloc[:3]
checking = table.iloc[3:]
```

`iloc` selects rows by position. `:3` means the rows before position 3: positions 0, 1 and 2. `3:` means position 3 and all rows after it. No row is in both groups here.

This is an easy first example. Later lessons choose splits that match the real job. Do not always take the first three rows of an unfamiliar dataset.

## 6. Train and predict

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(training[["distance_km"]], training["minutes"])
guesses = model.predict(checking[["distance_km"]])
print(guesses)
```

`LinearRegression` is a model that learns a straight-line rule. `model = LinearRegression()` creates an empty model. `fit` trains it from the inputs and answers. `predict` uses what it learned. It does not learn the check answers.

The dot in `model.fit` asks that object to do a job. The words inside parentheses are what we give to that job. A job like this is called a **method**.

## 7. Reuse a small rule

```python
def estimate(distance):
    return 10 + 2 * distance

print(estimate(4))
```

`def` defines a **function**: a named set of steps. `return` gives back an answer. The spaces at the start of the `return` line show that it belongs to the function. Keep those spaces. This example is a rule we wrote, rather than one learned by a model.

## 8. Understand a pipeline

A **pipeline** keeps several steps together. For example:

1. Fill a missing weight with the middle training weight.
2. Turn zone names into number columns.
3. Give the result to a trained model.

`fit` learns the needed values from training rows. `transform` applies a learned change. `predict` runs the preparation and asks the model for an answer. Reuse the same fitted steps for new rows.

## 9. Run a tiny practice script

1. Open a plain text editor.
2. Copy the three lines from step 1.
3. Save them as `first_steps.py` inside your extracted lesson folder. Keep the `.py` ending.
4. Open a terminal in that folder. Run `python first_steps.py` after activating the environment from Setup.
5. Check that it prints 18. Change the distance to 8. Save and run again.

Type terminal commands in the terminal. Put Python code in the `.py` file. Do not type the Markdown backticks into either place.

## Check your understanding

1. What does `fit` do? It learns from training examples.
2. Does `predict` need the true answer for a new request? No. It uses the inputs.
3. Why keep a preparation step with the model? New inputs need the same rules used during training.
4. What is position zero? The first item.

Next: follow the first module in [the learning path](LEARNING-PATH.md).
