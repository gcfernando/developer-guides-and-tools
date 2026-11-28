# Convert Text to Numerical Representation

**Lesson 084 · Practice**

## Your goal

Compare plain word counts and weighted word counts for short messages.

## Before you start

Read a message as text. Start with counting one word.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A model needs numbers. Counts make one column for a known word. TF-IDF gives different weights to common and less common words. Cleanup can lose meaning.

## Guess first

Should we always remove the word not? Write your answer before running the script.

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

<details>
<summary>Read the answer after trying</summary>

No. Removing it can reverse meaning. Test cleanup for the task.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


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
