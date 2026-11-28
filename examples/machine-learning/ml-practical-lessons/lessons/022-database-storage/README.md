# Database storage

**Lesson 022 · Practice**

## Your goal

Store orders in a database table and retrieve them with SQL.

## Before you start

Read a CSV header and count rows.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Collection brings recorded facts into a table. A database query, API request and web-page parser are different ways to obtain rows.

**Why and when.** Use a source whose fields, permissions and update times fit the question. Keep the original source identifiable.

**A worked example to follow.** The three order IDs in sample.csv are copied into an in-memory SQLite table and returned by a local API. The HTML example extracts the same zones from supplied tags. Count IDs at each step: a successful request alone does not prove every row arrived.

**Input and output.** The supplied sample fields are `order_id`, `zone`. In that field order, one original row is:

```text
1 | north
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Add one invented order with a unique ID. Before running, predict the CSV, database and local API row counts. Which source would you inspect if they disagree? Write a reason before running or opening the answer.

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
Rows from the CSV and database: 3 3

Orders returned by the local API
 order_id  zone
        1 north
        2 south
        3  west
Parsed HTML: ['north', 'south', 'west']
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add order_id 4 with zone west in sample.csv. Look for it in the database, API or page output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** The script uses local fixtures, not a live public API or web scraper. Real APIs may paginate, fail or change their schema. An HTML page can change its tags.

<details>
<summary>Check your choice and reason</summary>

Every complete copy should contain the extra order once. Trace its ID from the original CSV through each result. Investigate filtering, paging or parsing rather than silently accepting fewer rows.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| order_id | zone |
| --- | --- |
| 1 | north |
| 2 | south |
| 3 | west |

<!-- teaching-note:start -->
<!-- teaching-profile:collection -->
<!-- teaching-note:end -->
