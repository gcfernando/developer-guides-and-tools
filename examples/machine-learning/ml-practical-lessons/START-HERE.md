---
layout: default
title: "Start learning machine learning"
---

# Start here

You do not need to know machine learning. You do not need to know Python yet.

Machine learning is a way to find a useful pattern in examples. We give a computer some examples with known answers. It builds a rule from them. We then check the rule on other examples.

In this course, we often ask: **How many minutes might a delivery take?**

You can learn the ideas without running code. You can also learn to build a small model with Python. Python is a language for giving instructions to a computer.

## Choose your route

| Route | What you do | What you need |
| --- | --- | --- |
| Understand the ideas | Read this page. Do the paper tasks. Read the worked answers. | Paper or a spreadsheet. No Python. |
| Build with Python | Do the same tasks. Then run the lesson files. | A computer and the [setup steps](SETUP.md). |

Both routes start below. Later, use the [learning path](LEARNING-PATH.md). The large workbook is a library. You do not need to read all its lessons in order.

## 1. Meet one small table

A **table** holds facts in rows and columns.

- A row goes from left to right. Each row here is one finished delivery.
- A column goes from top to bottom. Each column holds one kind of fact.
- `km` means kilometres. `min` means minutes.

| Distance in km | Measured time in min |
| --- | --- |
| 1 | 12 |
| 2 | 14 |
| 3 | 16 |

We know the distance before a delivery starts. That makes it an **input**. You will also hear the word **feature**.

We want to guess the time. That is the **target**, or the answer we want to learn. For a finished delivery, we can record the measured time.

## 2. Make a guess before using a computer

Each extra kilometre adds two minutes in this made-up table.

**Your turn:** What time would you guess for 4 km? Write your answer before opening the box.

<details>
<summary>See the answer</summary>

18 minutes. The table follows this rule:

`time = 10 + 2 × distance`

At 4 km: `10 + 2 × 4 = 18`.

The 10 is the starting part of the rule. The 2 is how much the rule adds for one extra kilometre. Later, you will hear **intercept** for the starting part and **slope** for the amount added.

</details>

## 3. Learn what the computer does

We could type that rule ourselves. That would be a rule written by a person.

In machine learning, we give the computer the old distances and times. A model tries to find a rule that fits those examples. A **model** is the rule and the values it has learned.

**Training** means learning those values. A **prediction** is the model's guess for a new input.

Try three rules for 1 km and 3 km:

| Rule | Guess at 1 km | Guess at 3 km | Does it match both recorded times? |
| --- | --- | --- | --- |
| Always say 15 | 15 | 15 | No |
| 10 + 2 × distance | 12 | 16 | Yes |
| 10 + 4 × distance | 14 | 22 | No |

The computer compares mistakes while it learns. A mistake is also called an **error**. The smaller the mistakes on the training examples, the better that rule fits those examples. We still need a separate check.

## 4. Keep some answers for a fair check

Imagine doing a school test after seeing its answer sheet. A high score would not show how well you can answer new questions.

The same problem can happen with a model. Keep three groups of rows:

1. **Training rows:** teach the model.
2. **Validation rows:** help us choose a model or a setting.
3. **Test rows:** check the final choice. Do not use these answers to make the choice.

A **setting** changes how a model learns. For example, a decision tree can be allowed to make a few decisions or many decisions.

Later, we will choose groups that match the job. Future deliveries need a check on later dates. New customers may need a check on customers the model has never seen.

## 5. Expect real examples to be messy

Now add another 3 km delivery. It took 19 minutes, rather than 16 minutes.

**Your turn:** Does that prove the computer is broken?

<details>
<summary>See the answer</summary>

No. Traffic, waiting, and other facts can change a delivery time. Distance alone does not tell us everything. A recording can also contain a mistake. We need to check the source before changing it.

The first table was made simple to show one idea. Real data does not usually follow a perfect rule. A useful prediction is still a guess. It is not a promise.

</details>

## 6. Know what kind of answer you need

| Question | Answer | Technical name |
| --- | --- | --- |
| How many minutes will this take? | A number | Regression |
| Is this order urgent or regular? | One of some known names | Classification |
| Which shoppers have similar habits? | Groups we have not named in advance | Clustering |
| Which move helps a robot reach a goal? | An action learned from rewards | Reinforcement learning |

**Your turn:** Which kind of task is “guess tomorrow's number of orders”? Which is “sort a message into billing or delivery”?

<details>
<summary>See the answers</summary>

The first asks for a number, so it is regression. The second chooses between known names, so it is classification. A familiar word such as “regression” is a name to learn, not an extra step to perform.

</details>

## 7. Learn the computer words you will need

Skip running code for now if you chose the ideas route.

| Word | Plain meaning |
| --- | --- |
| File | One saved item, such as a table or a Python script. |
| Folder | A place that holds files and other folders. |
| File name | The name shown for a file, such as `sample.csv`. |
| Extension | The ending of a file name. `.csv` is a table file. `.py` is a Python file. |
| ZIP | One package that holds several files. Extract it to get those files out. |
| CSV | A plain text table. Commas separate the cells. |
| Script | A file of instructions. `lesson.py` is a script. |
| Terminal | A window where you type a command, then press Enter. |
| Command | One instruction to run, such as `python lesson.py`. |
| Package | Extra Python tools that another person has written. |

In a CSV, the small table above looks like this:

```text
distance_km,minutes
1,12
2,14
3,16
```

The first line names the columns. Each later line is one row. Keep the first line when editing the file.

## 8. Get the whole course folder

If you already have this folder, go to the next step.

1. Open the [repository page](https://github.com/gcfernando/developer-guides-and-tools).
2. Select the **Code** button. Select **Download ZIP**.
3. Find that ZIP in your Downloads folder.
4. On Windows, right-click it and select **Extract All**. On a Mac, double-click it. On Linux, open it with the archive app and select **Extract**.
5. Open the extracted folder. Then open `examples`, `machine-learning`, and `ml-practical-lessons` in that order.
6. Keep this whole folder. Do not move the HTML file away from its pictures and lesson files.

You should see these items:

```text
ml-practical-lessons/
    START-HERE.html
    SETUP.html
    Data-Science-and-Machine-Learning.html
    sample_code_folder/
    workbook-figures/
```

You do not need to install Git. Git is a tool for tracking file changes. It is used by the course author, not required for these lessons.

## 9. Open and edit one lesson

1. Open `sample_code_folder`.
2. Find `002-your-first-prediction.zip`.
3. Extract it directly inside `ml-practical-lessons`. Open the extracted folder.
4. If you see a second folder with the same name, open it. Stop when you see `lesson.py` and `new_inputs.csv` together.
5. Keep a fresh ZIP. You can extract another copy if you want to undo an edit.
6. Follow [SETUP](SETUP.md) before running the script.

To edit a CSV safely:

1. On Windows, right-click the CSV and choose **Open with**, then **Notepad**. On a Mac, use a plain text editor. In TextEdit, select **Format**, then **Make Plain Text** first.
2. Change only the value named by the task. Keep the commas and column names.
3. Select **Save**. Keep the name `new_inputs.csv`. Do not add `.txt`.
4. Close the file and open it again. Check that your change is still there.
5. Run the lesson again with the same command.

If you use a spreadsheet, keep the column names. Choose **CSV** when saving. A message that some formatting will be lost is about colours and fonts, not the cell values. Use a dot for a decimal in these supplied files, such as `2.5`. A blank cell means a value is unknown. Zero is a known number; it is not the same as a blank.

## 10. Check yourself

Before the next module, explain these ideas in your own words:

- Which column is an input? Which column holds the answer?
- What is the difference between training a model and asking it for a prediction?
- Why do we keep some answers away from training?
- Why might two trips with the same distance take different times?

If these are still hard, repeat steps 1 to 6 with a friend. If they make sense, open the [learning path](LEARNING-PATH.md). For the code route, complete [SETUP](SETUP.md) next.
