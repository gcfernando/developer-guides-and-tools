# K-Means Classifier

**Lesson 381 · Practice**

## Your goal

Find clusters first, then use known labels to name each cluster.

## Before you start

Distinguish a discovered cluster ID from a confirmed class.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A cluster-to-class mapping adds a supervised decision rule to an unsupervised grouping.

**Why and when.** Use it as a specific constructed baseline, not as a claim that ordinary K-Means is supervised.

**A worked example to follow.** The script forms two clusters from training inputs, then maps each to its most common known training label. New cluster IDs are translated using that saved mapping.

**Input and output.** The supplied sample fields are `x`, `y`, `label`. In that field order, one original row is:

```text
1 | 1 | local
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

If cluster 0 mostly contains the class long, can you call every future cluster 0 long after refitting? Write a reason before running or opening the answer.

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
Cluster IDs: [0, 1, 0]
Mapped class predictions: ['local', 'long', 'local']
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing x from 1.5 to 4 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Clusters need not correspond to classes. Do not use test labels to assign the cluster names or choose K.

<details markdown="1">
<summary>Check your choice and reason</summary>

Not automatically. Cluster IDs may change between fits. Learn and save the mapping with each training procedure.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| x | y | label |
| --- | --- | --- |
| 1 | 1 | local |
| 2 | 1 | local |
| 1 | 2 | local |
| 8 | 8 | long |
| 9 | 8 | long |
| 8 | 9 | long |

## 📩 Supplied new inputs

| x | y |
| --- | --- |
| 1.5 | 2 |
| 9 | 9 |
| 4 | 5 |

<!-- teaching-note:start -->
<!-- teaching-profile:cluster_classifier -->
<!-- teaching-note:end -->
