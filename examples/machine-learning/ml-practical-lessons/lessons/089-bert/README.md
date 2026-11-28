# BERT

**Lesson 089 · Practice**

## Your goal

Use a tiny BERT model to inspect how token vectors become one message vector.

## Before you start

Read a list of numbers as a vector; complete the network bridge in Extra topics.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

An embedding is a list of numbers representing an item. Its usefulness depends on how that representation was constructed or learned.

**Why and when.** Use embeddings when a validated representation captures information useful for your task. Compare with a word-count baseline.

**A worked example to follow.** Word2Vec learns tiny vectors from the supplied training messages and averages known-word vectors. The BERT exercise starts a random small encoder to show token vectors and pooling; it is not a pretrained language model.

**Input and output.** The supplied sample fields are `message`, `category`. In that field order, one original row is:

```text
MY Parcel Is Late!!! | delivery
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Which evidence would you need before replacing a word-count model with these vectors? Write a reason before running or opening the answer.

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
Training matrix: (6, 16)
Held-out predictions: ['delivery', 'billing']
                         message predicted
             The parcel is late!  delivery
I need a refund for two charges.  delivery
          WHERE ARE MY PACKAGES?  delivery
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Replace one message in new_inputs.csv. Include one delivery message and one billing message.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A returned array does not prove language understanding. The tiny corpus and random BERT weights do not justify claims about real message meaning.

<details markdown="1">
<summary>Check your choice and reason</summary>

Use the same untouched validation examples, report suitable errors and inspect new words/languages and failures. Check representation provenance. Do not choose from a single convenient prediction.

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

<!-- extra-lab:start -->
## Trace one update before a network

Read the [network bridge](../../ELECTIVES.md#a-bridge-before-networks-trace-one-learning-step) before the larger training loop. The complete [network_bridge.py](network_bridge.py) needs only Python:

```bash
python network_bridge.py
```

Its [recorded output](network-expected-output.txt) follows one input, a weighted sum, a squared mistake, and a change to the weight and bias. It does not measure performance on separate examples. In that practice file change `learning_rate = 0.1` to `learning_rate = 1.0`, save, and run again. This row's loss rises from 1 to 81: a larger step can make learning worse. Restore 0.1 afterward. Complete the array-shape paper task in Extra topics before reading frame or token tensors.
<!-- extra-lab:end -->


<!-- teaching-note:start -->
<!-- teaching-profile:word_vectors -->
<!-- teaching-note:end -->
