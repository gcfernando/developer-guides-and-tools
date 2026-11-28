# Spot, check, and handle an outlier

**Lesson 069 · Core**

## Your goal

Review a recorded 90 kg parcel, correct it using the weighing slip, and compare the two predictions on a graph.

## Before you start

Sort numbers. The middle half is the values between the lower and upper quarters.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

An outlier is an unusual value. A flag says check it. It does not say it is wrong. Use the source to keep, correct or set it aside.

## Guess first

Does an outlier flag prove a recording error? Write your answer before running the script.

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
Training review range: -3.5 to 12.5 kg.
Training records outside that range
 parcel  weight_kg
      5         90

Decision: CORRECT
The slip confirms 5 kg. Change 90 kg to 5 kg.

Check parcel 8
      Training data  Predicted minutes  Actual minutes
   Original records               17.7              26
After source review               26.0              26
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In weighing_slip.csv, change the verified weight from 5 to 90 for KEEP. Clear the second cell for FLAG.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. A very heavy parcel can be real. Ask for a source check.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| parcel | weight_kg | minutes |
| --- | --- | --- |
| 1 | 1 | 12 |
| 2 | 2 | 14 |
| 3 | 3 | 16 |
| 4 | 4 | 18 |
| 5 | 90 | 20 |
| 6 | 6 | 22 |
| 7 | 7 | 24 |
| 8 | 8 | 26 |

## Try all three decisions

Leave sample.csv unchanged. Edit only the second cell in the data row of weighing_slip.csv, save, and run the same command.

| Verified weight on the slip | Expected decision | What the script does |
| --- | --- | --- |
| 5 | CORRECT | Uses 5 kg and predicts 26.0 minutes on the check parcel. |
| 90 | KEEP | Keeps 90 kg and predicts 17.7 minutes. |
| Blank | FLAG | Sets the row aside for this practice run and asks for a source check. |

Open [the weighing slip](weighing_slip.csv). Keep the parcel ID as 5.

## 📊 Read the visual

![Parcel 5 is plotted at 90 kg above the 12.5 kg review limit. Every other parcel is below the limit.](spot-check-and-handle-an-outlier-1.png)

**👀 Read the visual.** Find parcel 5 along the bottom. Its orange diamond is at **90 kg**. The dashed line shows the **12.5 kg** upper review limit learned from the seven training parcels.

**👉 What to do.** **Flag parcel 5 for review.** The plot tells you which record to check.

![Use the weighing slip to choose an action. A confirmed 5 kg means correct the entry. A confirmed 90 kg means keep it. A missing slip means flag for review.](outlier-source-decision.png)

**👀 Read the visual.** Follow the branch that matches the source. In this exercise the weighing slip shows **5 kg**, so the 90 kg entry gets corrected.

**👉 What to do.** Keep a confirmed 90 kg. If the source is missing, request a reweigh and leave the value flagged.

![For the same 8 kg test parcel, the original model predicted 17.7 minutes and the corrected model predicted 26.0 minutes. The dashed line shows the actual 26 minutes.](spot-check-and-handle-an-outlier-2.png)

**👀 Read the visual.** The dashed line is the real time for **parcel 8**, which was kept aside. The orange bar ends at **17.7 min**. The teal bar reaches **26.0 min**.

**👉 What to do.** Use the verified training correction, then check more kept-back deliveries before trusting the improvement in an app.
