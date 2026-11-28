# Geospatial (Lat/Long, Addresses)

**Lesson 106 · Practice**

## Your goal

Look up coordinates for three depots and use them to estimate delivery time.

## Before you start

Read latitude and longitude as two different coordinates.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Geocoding finds coordinates for a named place. A local lookup only knows its listed places.

**Why and when.** Use coordinates when location is relevant and the match is verified. Live geocoding is a separate service step.

**A worked example to follow.** North Depot maps to the supplied coordinate pair. Unknown Depot remains unlocated; the script does not invent a point or make a live request.

**Input and output.** The supplied sample fields are `address`, `weight_kg`, `minutes`. In that field order, one original row is:

```text
North Depot | 2 | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

An unknown address gets coordinates 0,0 from a guessed fallback. Is that a safe representation of missing location? Write a reason before running or opening the answer.

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
      address  weight_kg             latitude            longitude    estimated_minutes
  North Depot          3                59.35                18.06                 22.5
  South Depot          2                59.28                18.02                 23.0
Unknown Depot          2 address needs review address needs review address needs review
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change address in new_inputs.csv, for example from North Depot to Unknown Depot. Compare the printed rows.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Ambiguous place names can resolve incorrectly. Latitude/longitude degrees do not directly give travel distance. Do not send personal addresses to an unapproved service.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. 0,0 is an actual location. Keep the match unresolved and request a source lookup or use a separately tested missing-location policy.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| address | weight_kg | minutes |
| --- | --- | --- |
| North Depot | 2 | 19 |
| South Depot | 1 | 21 |
| River Depot | 2 | 27 |
| North Depot | 5 | 29 |
| South Depot | 3 | 25 |

## 📩 Supplied new inputs

| address | weight_kg |
| --- | --- |
| North Depot | 3 |
| South Depot | 2 |
| Unknown Depot | 2 |

<!-- teaching-note:start -->
<!-- teaching-profile:geography -->
<!-- teaching-note:end -->
