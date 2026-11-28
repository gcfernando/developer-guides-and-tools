# Data type

**Lesson 024 · Practice**

## Your goal

Inspect the column types before sharing the delivery table.

## Before you start

Know what a file and folder are.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A file list records where each item is. Share only needed fields. Removing a contact field is one small sharing step, not proof of legal compliance.

## Guess first

Should a shared export include a contact field the task does not need? Write your answer before running the script.

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

Try changing order_id from 1 to 2 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Also check purpose, permission, access and retention with the data owner.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| order_id | minutes | contact |
| --- | --- | --- |
| 1 | 22 | sample1@example.invalid |
| 2 | 31 | sample2@example.invalid |
