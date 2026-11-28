# Remove stop words (e.g., "the", "and", "is")

**Lesson 080 · Practice**

## Your goal

Drop selected common words such as the and is, then test a delivery or billing message.

## Before you start

Count a word in a short sentence.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A stop-word list removes selected common words before the model sees counts.

**Why and when.** Try it only if those words add little useful information for the task.

**A worked example to follow.** The explicit list removes the, and, is. The example keeps not, so the phrase not here retains a clue that the parcel is absent.

**Input and output.** The supplied sample fields are `message`, `category`. In that field order, one original row is:

```text
MY Parcel Is Late!!! | delivery
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Would a stop list that removes not be safe for distinguishing late from not late? Write a reason before running or opening the answer.

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
Before: ['the', 'parcel', 'is', 'not', 'here', 'and', 'am', 'waiting']
After: ['parcel', 'not', 'here', 'am', 'waiting']
Actual: ['delivery', 'billing']
Predicted: ['delivery', 'billing']
                         message predicted
             The parcel is late!  delivery
I need a refund for two charges.   billing
          WHERE ARE MY PACKAGES?  delivery
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Replace one message in new_inputs.csv. Include one delivery message and one billing message.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A general stop list may remove negation or words useful for your language and task. Shorter text is not automatically a better representation.

<details>
<summary>Check your choice and reason</summary>

Not without evidence. Those phrases could become identical. Compare token lists and validation mistakes before deciding.

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
<!-- teaching-profile:stop_words -->
<!-- teaching-note:end -->
