---
layout: default
title: "Python Setup for the Machine Learning Practical Lessons"
description: "Set up Python 3.12, install lesson requirements and run your first prediction using the practical workbook."
permalink: /examples/machine-learning/ml-practical-lessons/setup/
---

# ⚙️ Set up Python once

[← Back to the beginner path](Data-Science-and-Machine-Learning.md#beginner-path)

Open the complete workbook folder from your download or repository copy. You should see `requirements-core-tested.txt`, the workbook files, and the `sample_code_folder` directory. Find `002-your-first-prediction.zip` in that directory and extract it into the workbook folder. Keep `lesson.py`, `sample.csv`, and `new_inputs.csv` together in the extracted lesson folder.

If you already have a working Python environment, you can open a terminal in `002-your-first-prediction`, run `python -m pip install -r requirements.txt` once, and then run `python lesson.py`. To build the workbook’s tested Python environment from scratch, follow the steps for your computer below.

## 🪟 Windows

1. Install Python 3.12 from [Python.org](https://www.python.org/downloads/).
2. Open the extracted workbook folder in File Explorer. Type `powershell` in the address bar and press Enter. Run these commands. The first creates a private Python environment called `.venv`. The second installs the common packages into it.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-core-tested.txt
```

3. Enter the lesson folder and use that environment to run the lesson.

```powershell
cd .\002-your-first-prediction
..\.venv\Scripts\python.exe lesson.py
```

## 🍎 macOS or 🐧 Linux

1. Install or select Python 3.12. On macOS you can install it from [Python.org](https://www.python.org/downloads/).
2. Open Terminal and change into the extracted workbook folder. One way is to type `cd `, drag the folder into the terminal, and press Enter. Run these commands to create a private environment and install the common packages.

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-core-tested.txt
```

3. Enter the lesson folder and use that environment to run the lesson.

```bash
cd 002-your-first-prediction
../.venv/bin/python lesson.py
```

## ✅ Check your first prediction

| Where to look | What you should see |
| --- | --- |
| The terminal, under **New delivery estimates** | **18.0 minutes** for **4 km**. |
| `new_inputs.csv` | One row has a distance of **4**. Change it to **8**, save, and rerun the same Python command. |
| The terminal after you rerun the lesson | **26.0 minutes** for the edited row. |

## 📦 Open another lesson

Extract its ZIP directly inside the workbook folder, then open a terminal in the extracted lesson folder. Use the same Python executable for both commands. On Windows, start with `..\.venv\Scripts\python.exe`. On macOS and Linux, start with `../.venv/bin/python`. Add `-m pip install -r requirements.txt` once for the lesson, then use the script name in its README. For example, Lesson 071 has separate train and test scripts.

| If you see | What to check |
| --- | --- |
| Python cannot find `requirements-core-tested.txt` | Open the terminal in the extracted workbook folder and check the filename. |
| Python cannot find `lesson.py` or a CSV | Enter the extracted lesson folder. Check that the script and its CSVs kept their names. |
| `ModuleNotFoundError` | Install the lesson’s `requirements.txt` using the same Python executable you use to run the script. |
| The 4 km row still appears after you edited it | Check that you saved `new_inputs.csv` in the folder you are running the lesson from. |

## 🔁 Reproduce a result

The workbook was tested with **Python 3.12.14 on Linux**. See the [recorded package versions](tested-package-versions.csv) and [pinned core requirements](requirements-core-tested.txt). The core file supplies common data and plotting packages. Individual lesson ZIPs list extra packages for their exercises, including optional media and web tooling. The Windows and macOS steps are setup instructions. Clean installs on those systems are unverified.

With the supplied files and recorded environment, compare counts, overlap checks, and beginner path decisions to the workbook. Use the displayed rounding for scores and chart coordinates. Library versions, platforms, and edits to the data can affect numerical results.

## 💾 Save and reload a model

Load the `.joblib` file you just trained, or one from a verified, trusted source. Loading it can execute code. Keep the training script, data version, Python version, and package versions with the model. Retrain from that recipe when you change the environment. [Model persistence](https://scikit-learn.org/stable/model_persistence.html)
