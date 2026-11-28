# Video (Frames, Sequences)

**Lesson 122 · Practice**

## Your goal

Make a short video from frames and classify which way an object moves.

## Before you start

Understand one image, array shapes and basic network training.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

A video is a sequence of frames. The order matters for motion. The extra lesson uses a network to read each frame and another to read the sequence.

## Guess first

Can reversing the same frames change the motion? Write your answer before running the script.

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
Clips × frames × channels × height × width: (8, 4, 1, 6, 6)
Decoded MP4 direction: [1]
Directions for all new clips: [1, 0]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing direction from 1 to 0 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

Yes. Keep frames from a source clip together when checking a model.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| direction | row |
| --- | --- |
| 0 | 1 |
| 0 | 2 |
| 0 | 3 |
| 0 | 4 |
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 1 | 4 |

## 📩 Supplied new inputs

| direction | row |
| --- | --- |
| 1 | 0 |
| 0 | 5 |

## 📊 Read the visual

![Extract frames. Read the video as a sequence of pictures. → Measure each frame. Use the same image model for every frame. → Read the sequence. Use the order of the frames to predict left or right.](video-feature-steps.png)

**👀 Read the visual.** Keep the pictures in time order so movement stays visible.

**👉 What to do.** Check frame order when direction matters. A picture shows position and the sequence shows movement.
