# Convert Text to Numerical Representation

**Lesson 084 · Practice**

## Your goal

Compare plain word counts and weighted word counts for short messages.

## Before you start

Count parcel in three short messages.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Word counts record occurrences. TF-IDF changes weights using how common a word is across training messages.

**Why and when.** Use counts as a simple text baseline; compare TF-IDF when common words should contribute differently.

**A worked example to follow.** A known word has one fixed column. Its raw count may be 1 in a message; its TF-IDF value also depends on the training corpus and normalization. The script prints both values for parcel before predicting held-back categories.

**Input and output.** The supplied sample fields are `message`, `category`. In that field order, one original row is:

```text
MY Parcel Is Late!!! | delivery
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A new message contains only words absent from training. Does a predicted category establish that the text was understood? Write a reason before running or opening the answer.

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
CountVectorizer parcel feature: 1 predictions: ['delivery', 'billing']
                         message predicted
             The parcel is late!  delivery
I need a refund for two charges.   billing
          WHERE ARE MY PACKAGES?  delivery
TfidfVectorizer parcel feature: 0.52 predictions: ['delivery', 'billing']
                         message predicted
             The parcel is late!  delivery
I need a refund for two charges.   billing
          WHERE ARE MY PACKAGES?  delivery
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change message in new_inputs.csv, for example from The parcel is late! to WHERE ARE MY PACKAGES?. Compare the printed rows.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A TF-IDF weight is not a probability or a semantic meaning. Fit vocabulary and IDF on training only; a new message must not relearn them.

<details>
<summary>Check your choice and reason</summary>

No. Its representation can contain no known-word evidence. Inspect it, record the limitation and use an appropriate fallback or better training coverage.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| message | category |
| --- | --- |
| MY Parcel Is Late!!! | delivery |
| Where is my PACKAGE? | delivery |
| The parcel never arrived. | delivery |
| Please REFUND my payment! | billing |
| My invoice is WRONG? | billing |
| I was charged twice. | billing |
| Where is my parcel? | delivery |
| Please refund this charge! | billing |

## 📩 Supplied new inputs

| message |
| --- |
| The parcel is late! |
| I need a refund for two charges. |
| WHERE ARE MY PACKAGES? |

<!-- teaching-note:start -->
<!-- teaching-profile:word_counts -->
<!-- teaching-note:end -->
