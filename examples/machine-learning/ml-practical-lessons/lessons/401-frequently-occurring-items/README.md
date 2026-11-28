# Frequently occurring items

**Lesson 401 · Practice**

## Your goal

Add a shopping basket and see which item pairs remain common.

## Before you start

Count baskets and fractions.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Support measures co-occurrence share; confidence conditions on a rule’s starting item.

**Why and when.** Explore item patterns, then check whether they support a useful action.

**A worked example to follow.** Milk and bread in 3 of 5 baskets give 60% pair support. If 4 baskets contain milk, milk→bread confidence is 3/4 = 75%. Apriori and FP-Growth search frequent sets differently.

**Input and output.** The supplied sample fields are `items`. In that field order, one original row is:

```text
milk|bread
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Follow the chosen measurements through their preparation and fitted grouping, projection or review rule. Read the resulting representation or flag using the explanation above; do not invent confirmed group answers. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Must milk→bread and bread→milk have equal confidence? Write a reason before running or opening the answer.

## Run one step at a time

1. Extract this ZIP. Open folders until you see `lesson.py`.
2. Open a terminal in that folder. Activate the course environment as shown in Setup. Every `python` below means that environment's Python.
3. The main path uses the common course packages. If this lesson needs more, use the same Python to install `requirements.txt` with the course constraint file. See Setup step 8. Do not install optional media packages just to read a lesson.
4. Run these lines one at a time. Wait for each to finish.

```bash
python lesson.py
```

## Check the result

Read the column names and units before the numbers. The original files produced this example. Your deliberate data edits may change it.

```text
apriori [(('bread', 'milk'), 0.6)]
fpgrowth [(('bread', 'milk'), 0.6)]
Milk to bread confidence: 0.75
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add or change a basket in sample.csv. Use | between items. The printed support is the share of baskets that contain the item set.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Confidence is not cause and may be high for a common consequent. Five baskets cannot establish a stable retail policy.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. They have different conditional denominators. Their pair support is the same.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| items |
| --- |
| milk\|bread |
| milk\|bread\|eggs |
| bread |
| milk\|bread |
| milk\|apples |

<!-- teaching-note:start -->
<!-- teaching-profile:association -->
<!-- teaching-note:end -->
