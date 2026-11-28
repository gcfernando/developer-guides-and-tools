# GDPR

**Lesson 028 · Practice**

## Your goal

Practice sharing only the fields the task needs. The sample uses fictitious contact details.

## Before you start

Tell a file name, folder and CSV field apart.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A file list records where items are. Metadata records how they were obtained and what they mean.

**Why and when.** Use these notes whenever someone else must find, reproduce or safely share the data. Keep only fields needed for the agreed purpose.

**A worked example to follow.** The exercise writes deliveries.csv without the fictional contact field. A manifest lists text, picture and video files. File size is measured in bytes; it does not tell you whether the facts are correct.

**Input and output.** The supplied sample fields are `order_id`, `minutes`, `contact`. In that field order, one original row is:

```text
1 | 22 | sample1@example.invalid
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Imagine the image file has a name but cannot be opened. Which checks should supplement its entry in the manifest? What should accompany a shared table? Write a reason before running or opening the answer.

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
{'source': 'original sample', 'method': 'created in Python', 'bytes': 27, 'types': {'order_id': 'int64', 'minutes': 'int64'}}
file_type  collected
     text       True
    image       True
    video       True
Image width and height: (16, 16)
Video frames read: 2
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change a fictional contact in sample.csv. Rerun. Open collection_demo/deliveries.csv and check that contact is still absent.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A local folder is not a cloud upload. Removing one contact field does not establish legal compliance, consent, access control or a retention policy. The named legal topics illustrate only this small data-sharing step.

<details markdown="1">
<summary>Check your choice and reason</summary>

Check that the file exists, can be decoded and has the expected content and dimensions. Share the needed table fields plus source, collection method, meanings, access permission and retention notes. Use the optional service walkthrough for actual cloud practice.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| order_id | minutes | contact |
| --- | --- | --- |
| 1 | 22 | sample1@example.invalid |
| 2 | 31 | sample2@example.invalid |

<!-- teaching-note:start -->
<!-- teaching-profile:files_metadata -->
<!-- teaching-note:end -->
