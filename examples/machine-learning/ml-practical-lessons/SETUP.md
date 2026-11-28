---
layout: default
title: "Set up Python for the course"
permalink: /examples/machine-learning/ml-practical-lessons/setup/
---

# Set up Python

Read [Start here](START-HERE.md) first. This page is for the Python route. You can do the paper tasks without installing Python.

Allow time for the first download. The time depends on your computer and internet connection. Stop after you see the first prediction. You can return another day.

## 1. Find the course folder

Open `ml-practical-lessons`. You should see `requirements-core-tested.txt` and `sample_code_folder`. If you do not, follow the download steps in [Start here](START-HERE.md#8-get-the-whole-course-folder).

Extract `002-your-first-prediction.zip` inside this course folder. Open the extracted folders until you see `lesson.py`, `sample.csv`, and `new_inputs.csv` together.

## 2. Install Python 3.12

Python runs the instructions in a `.py` file.

- Windows or Mac: get Python 3.12 from [Python.org](https://www.python.org/downloads/). Follow the installer steps. On Windows, enable the option to add Python to PATH if offered. PATH is the list of places your terminal searches for commands.
- Linux: use your system's Python 3.12 package. Some systems also need its matching `venv` package. Ask your computer's support person if you cannot install software.

Use the steps for your computer. Do not mix Windows and Mac/Linux commands.

## 3. Open a terminal in the course folder

On Windows, open the course folder in File Explorer. Click the address bar. Type `powershell`. Press Enter.

On a Mac or Linux, open Terminal. Type `cd ` with a space after it. Drag the course folder into the window. Press Enter. If dragging is not supported, type `cd` followed by the quoted full folder path.

`cd` means change directory: move the terminal into a folder. The terminal should now be in `ml-practical-lessons`.

## 4. Make a private place for course packages

A **virtual environment** is a folder with its own Python packages. It keeps the course packages together. We call this folder `.venv`.

On Windows, run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-core-tested.txt
.\.venv\Scripts\Activate.ps1
```

On a Mac or Linux, run:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-core-tested.txt
source .venv/bin/activate
```

Run one line at a time. Press Enter after each line. Wait until the prompt returns before typing the next line. `pip` installs packages. `-r` asks it to read the package list in the named file.

If PowerShell blocks `Activate.ps1`, do not change security settings. Open Command Prompt in the course folder instead. Run:

```bat
.venv\Scripts\activate.bat
```

You can also use the full Python path without activating. From a lesson folder directly inside the course folder, use `..\.venv\Scripts\python.exe` on Windows or `../.venv/bin/python` on Mac/Linux wherever a lesson says `python`.

## 5. Check which Python is running

In the activated terminal, run:

```bash
python -c "import sys; print(sys.executable)"
python --version
```

The first answer should include `.venv`. The second should say Python 3.12. If it does not, stop and activate the course environment in this terminal. Use the same terminal to install packages and run lessons.

Every `python` command in the course assumes this environment is active. Activation ends when you close the terminal. Next time, open the course folder and run only the activation command again. You do not need to recreate `.venv`.

## 6. Run the first lesson

Enter the folder that contains `lesson.py`:

```bash
cd 002-your-first-prediction
python lesson.py
```

If extraction made an extra folder with the same name, enter it too. Use `dir` on Windows or `ls` on Mac/Linux to list files. Stop moving folders when you see `lesson.py`.

Under **New delivery estimates**, find 4 km and **18.0 minutes**.

## 7. Change one value

1. Open `new_inputs.csv` in a plain text editor.
2. Change the first distance from `4` to `8`.
3. Keep the column name and the other rows.
4. Save with the same file name.
5. Run `python lesson.py` again.
6. The edited row should show **26.0 minutes**.

For help saving a CSV, use [the editing steps](START-HERE.md#9-open-and-edit-one-lesson).

## 8. Open another lesson

1. Keep the terminal open. Run `cd ..` to go back one folder. Repeat if needed until you are in the course folder.
2. Extract the next ZIP there.
3. Use `cd` to enter the folder with its script.
4. In the same active environment, run `python -m pip install -c ../requirements-core-tested.txt -r requirements.txt` if the lesson needs extra packages. The constraint file keeps common versions fixed. Adjust `../` if you extracted into a deeper folder.
5. Run the script named by the lesson. Most use `python lesson.py`. Lesson 071 also has separate training and prediction scripts.

Some extra lessons need large packages such as PyTorch. Read `requirements.txt` first. The main delivery course does not need those extra packages. Reading never needs Python.

## If something goes wrong

Read the last error line first. It often names the problem. An error is information, not a score for the learner.

| What you see | What to do |
| --- | --- |
| `python` or `py` is not found | Check the installation. Close and reopen the terminal. On Windows try `py -3.12` from step 4. |
| A file cannot be found | List files with `dir` or `ls`. Move to the folder that holds the named file. |
| `ModuleNotFoundError` | Check step 5. Install the lesson requirements with that same Python. |
| `KeyError` | A column name is missing or changed. Compare the CSV's first line with a fresh copy. |
| `ValueError` | A value has the wrong form. Check units, blanks, dates and numbers against the supplied example. |
| The output has not changed | Save your edit. Check you edited the copy in the folder you are running. |
| CSV columns look wrong | Use commas between cells. Keep text quoted if it contains a comma. Restore a fresh CSV if needed. |
| A server says its port is in use | Stop an old practice server with Ctrl+C. Or use another port as shown in the lesson. |
| Permission is denied | Use a normal folder you own. Ask your support person if installs are restricted. |
| A package cannot download | Check the internet connection. Keep the full error text. Do not delete Python to fix a download error. |

To undo edits, extract a fresh lesson into a new folder. Keep your changed copy if you want to compare them. Do not overwrite personal files.

## What has been checked

The original recorded environment is Python 3.12.14 on Linux. Its package list is in [tested-package-versions.csv](tested-package-versions.csv). Common versions are fixed in [requirements-core-tested.txt](requirements-core-tested.txt).

The course review also ran examples on Windows with Python 3.12.10 and different installed packages. See [the review evidence](course-review/verification.json). That is not a clean installation test of this recipe. Clean Windows and Mac installs and a study with new learners still need to be completed. [Release checks](TEACHING.md) explain how to record them.

## Saved models

A `.joblib` file can hold a trained model. Load only a file you made or trust. Loading it can run code. Keep the training data, script and package versions with it. See [model persistence](https://scikit-learn.org/stable/model_persistence.html).

Next: read [A small start with Python](PYTHON-BASICS.md), then open [the learning path](LEARNING-PATH.md).
