# Spectrograms

**Lesson 120 · Practice**

## Your goal

See how a tone’s frequencies appear in a spectrogram.

## Before you start

Read a time axis, a frequency in hertz, and a simple wave.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Audio samples record a changing signal. A spectrogram shows frequency content over time; MFCCs summarize a transformed frequency representation.

**Why and when.** Use a fixed sample rate and the same feature calculation when comparing recordings.

**A worked example to follow.** The script creates low and high tones, saves WAV, extracts frequency features and classifies pitch. A decoded MP3 is checked through the same feature function rather than treated as identical bytes.

**Input and output.** The supplied sample fields are `frequency_hz`, `label`. In that field order, one original row is:

```text
260 | low
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Two recordings have different sample rates. May you compare their feature columns without checking how those columns were constructed? Write a reason before running or opening the answer.

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

**Common mistakes and limits.** A tone classifier does not recognize speech. Compression and sample rate can change values. Extra FFmpeg/media dependencies must be available before running the audio tasks.

<details>
<summary>Check your choice and reason</summary>

No. Decode and prepare a consistent sample rate, channels and frame procedure, then check feature shape and validation behavior. The same column position must retain the same meaning.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

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

<!-- teaching-note:start -->
<!-- teaching-profile:audio -->
<!-- teaching-note:end -->
