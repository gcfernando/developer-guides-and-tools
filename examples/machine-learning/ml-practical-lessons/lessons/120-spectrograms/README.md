# Spectrograms

**Lesson 120 · Practice**

## Your goal

See how a tone’s frequencies appear in a spectrogram.

## Before you start

Finish the audio notes in Extra topics.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A sound can be shown over time or by its frequencies. The example makes tones locally. A short feature list summarizes them before comparing them.

## Guess first

Does a tone example prove the model recognizes everyday speech? Write your answer before running the script.

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
One MFCC row: 8
New WAV sound: ['high']
Decoded MP3 sound: ['high']
285 low
920 high
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change the frequency in new_inputs.csv to a value around 280 or 900. The script creates real WAV audio from those numbers and checks an MP3 round trip.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Speech is a much harder and different task.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| frequency_hz | label |
| --- | --- |
| 260 | low |
| 300 | low |
| 840 | high |
| 900 | high |

## 📩 Supplied new inputs

| frequency_hz |
| --- |
| 870 |
| 285 |
| 920 |
