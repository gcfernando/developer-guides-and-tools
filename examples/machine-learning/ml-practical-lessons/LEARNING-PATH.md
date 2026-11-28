# Your learning path

[Start here](START-HERE.md) · [Setup](SETUP.md) · [Practice and answers](PRACTICE.md) · [Word list](GLOSSARY.md)

Follow this order. The workbook is a library of examples. Old numbers stay the same so links still work. Several numbers use the same example. You do not need to run it for every heading.

**Ideas route:** read and do the paper tasks. **Python route:** also run the named lessons after Setup. Finish a module when you can explain its check, not just copy its output.

Study one small part at a time. Time estimates have not been tested yet. Stop when you can explain the check. Write the date beside each box so you can return later.

## The required order

| Done | Module | Read or run | You can move on when you can… |
| --- | --- | --- | --- |
| [ ] | 0. Get ready | [Start here](START-HERE.md), [Setup](SETUP.md), [Python basics](PYTHON-BASICS.md) | Read a table, edit a CSV and explain a prediction by hand. |
| [ ] | 1. Make a prediction | Lesson 002 | Name the input and answer. Explain training and prediction. |
| [ ] | 2. Choose a useful question | Lessons 004 and 009; [Project choices](PROJECT-CHOICES.md) | Say what decision a result supports and whether a simple rule is enough. |
| [ ] | 3. Keep a fair check | Lessons 179 and 442 | Explain training, validation and test rows. Choose a split for later deliveries or new customers. |
| [ ] | 4. Find data problems | Lessons 032, 048, 050, 055 and 069 | Find a blank, a repeated record, a unit problem and a value needing a source check. |
| [ ] | 5. Prepare inputs | Lessons 035, 039, 044, 071 and 075 | Fill a blank from training values. Turn a zone into numbers. Reuse the same preparation. |
| [ ] | 6. Compare with a simple guess | Baseline task in [Practice](PRACTICE.md); [train-and-test example](sample_code_folder/train-and-test.zip) | Compare a model with always guessing the middle training time. |
| [ ] | 7. Spot memorizing | Lessons 443 and 194 | Explain why a low training error can hide worse results on other rows. |
| [ ] | 8. Read number errors | Lessons 208 and 446 | Calculate an error in minutes. Check small groups and large mistakes. |
| [ ] | 9. Count category mistakes | Lessons 205 and 444 | Count missed urgent orders and false alarms. Choose a cutoff using validation rows and team capacity. |
| [ ] | 10. Explain what helped | Lesson 207; [Project choices](PROJECT-CHOICES.md) | Say what a model relied on without claiming it proves a cause. |
| [ ] | 11. Save and use a model | Saved-model part of 071; lesson 232 | Explain a saved model, request and response. Send a valid and invalid request. |
| [ ] | 12. Watch later results | Lesson 447 monitoring; [Project choices](PROJECT-CHOICES.md) | Compare later errors and write a next action for an alert. |
| [ ] | 13. Finish the guided project | Lesson 447 | Explain all five parts of its ten-point check without reading the answers. |
| [ ] | 14. Try a new project | [Independent project](INDEPENDENT-PROJECT.md) | Choose, build, check and explain a model without a full solution script. |

## Two small reading bridges for the early split lessons

You will see a score while learning how to keep rows separate. You do not need a full metrics chapter yet.

- **Error in minutes:** an actual time of 30 and prediction of 27 differ by 3 minutes. MAE averages the sizes of such differences. Two mistakes of 2 and 4 minutes have MAE 3 minutes.
- **Balanced accuracy:** count the share correct within each class, then average the class shares. Catching 8 of 10 urgent orders and correctly leaving 18 of 20 regular orders unflagged gives `(0.8 + 0.9) ÷ 2 = 0.85`. These are worked arithmetic examples, not additional experimental results.

Use these to read lessons 179 and 442. First inspect what rows the split kept apart. A smaller score cannot repair a split that answers the wrong question. Module 8 and module 9 later explain the metrics more fully.

Find each ZIP in `sample_code_folder`. Extract it as shown in Start here. The [workbook](Data-Science-and-Machine-Learning.md#lesson-downloads) also has all links.

## Why this order matters

First decide what to predict and which rows give a fair check. Then learn fill values, scales and category lists from training rows only. Keep final test answers out of model choices.

A fixed unit conversion, such as pounds to kilograms, follows a known rule. A median fill value is different: it is learned from data. Learn that value from training rows.

## How to use a lesson

1. Read the goal. Say it in your own words.
2. Read the small table. Name the units.
3. Write what you expect before running anything.
4. Run the example, or follow its paper calculation.
5. Read the result. Explain what it means.
6. Change one thing. Do not change five things at once.
7. Answer the check question. If it is hard, use the linked help before moving on.

## Review what you learned

After modules 4, 8 and 12, close the notes. Do the matching review in [Practice](PRACTICE.md). Return a few days later and explain an old example without running it. Remember the idea, not the exact number printed by a script.

## Extra topics

You do not need every algorithm for a first model. Read [Extra topics](ELECTIVES.md) after this path. Each names the ideas you need first. Tiny drawings and toy robots show how steps work. They do not prove usefulness outside an exercise.

## What finishing means

The ideas route helps you ask useful questions about an ML project. The Python route helps you build and explain a small checked project. Neither means you have mastered every part of ML. Build more projects, get feedback and keep checking your assumptions.

## Grow toward ML engineering in stages

First explain a small result by hand. Next run and modify a complete example. Then finish a partly completed task without copying its answer. Finally build a new checked project and let someone else reproduce it. Those are different achievements: record which you actually demonstrated.

After the independent project, strengthen Python programming, data querying, mathematics as needed, software testing, version control, deployment operations and responsible data handling through further practice. Use the optional catalogue to answer a specific project need. Memorizing more algorithm names is not the same as being able to operate a reliable ML system.
