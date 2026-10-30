---
title: "Data Science and Machine Learning Handbook"
description: "Set up a Python data science and machine learning handbook with local datasets, 91 figures and a Tkinter house-price example. Review validation limits."
permalink: /examples/machine-learning-handbook/
---

[Developer guides and tools](../../../README.md)

# Data Science and Machine Learning Handbook

Study data science and machine learning with a Python handbook, local datasets and a Tkinter house-price example. This bundle preserves the complete supplied MLHandbook folder: 125 original files, including 91 figures, CSV/JSONL data, SQLite databases and desktop application source.

[Read the published handbook source](../../../docs/data-science/machine-learning-handbook.md) · [Original handbook](Data_Science_Handbook.md) · [Machine learning path](../../../docs/learning-paths/machine-learning.md)

## What you can study

The handbook starts with Python, NumPy, pandas, charts and statistics, then follows data cleaning, feature engineering, splitting, training, evaluation, deployment and monitoring. Later sections cover dataset exercises, machine learning categories and algorithms, a model-versioning desktop example, and database/JSON workflows.

The recorded outputs and figures are supplied teaching material. They are not a new verification of every exercise or every library version. Some chapters download additional public datasets or use optional packages.

<a id="guide-files"></a>

## Files

| Path | Purpose |
|---|---|
| [Data_Science_Handbook.md](Data_Science_Handbook.md) | Complete original handbook |
| [datasets/](datasets/) | CSV, JSONL and SQLite inputs for exercises |
| [images/](images/) | 91 diagrams, charts and application screenshots |
| [tkinter_app/](tkinter_app/) | Python house-price engine, desktop UI and two CSV inputs |
| [requirements.txt](requirements.txt) | Main notebook packages; later chapters describe optional dependencies |
| [Tkinter requirements](tkinter_app/requirements.txt) | Smaller dependency set for the desktop example and model smoke check |

## Set up a practice environment

Python 3.12 is a suitable starting point for the instructions supplied with the handbook. From this bundle folder:

~~~sh
python -m venv .venv
~~~

Activate it using the command appropriate to your terminal, then:

~~~sh
python -m pip install -r requirements.txt
jupyter lab
~~~

Launch notebooks with this bundle folder as the working directory; code that opens datasets/ expects that location. Use a separate practice copy if you want to preserve the bundled exercise data.

The notebook dependencies do not install Tk itself. A desktop Python installation with Tk support is needed for the graphical example. Linux distributions may provide Tk separately.

<a id="guide-run-the-desktop-example"></a>

## Run the desktop example

From this bundle folder, after installing the smaller dependency set:

~~~sh
python -m pip install -r tkinter_app/requirements.txt
cd tkinter_app
python house_price_app.py
~~~

Start by training on houses_2025.csv. Predict a price, update with houses_2026_new.csv, inspect history and choose an earlier version to roll back. Models and training-history data are written beneath the current working directory.

The input range checks are in [model_service.py](tkinter_app/model_service.py). This is a teaching application for the supplied practice data. Only load model artifacts you trust; joblib model loading is intended for your own saved bundles.

<a id="guide-validation"></a>

## Validation

From the repository root:

~~~sh
npm test
python scripts/validate-ml-handbook.py --smoke
node scripts/verify-migration.cjs --sources ../
~~~

The Python check parses all CSV/JSONL files, checks SQLite integrity, compiles both application files, and can exercise training, prediction, update, persistence and rollback in a temporary workspace. It does not execute every notebook block or open the graphical window.

The original dataset attributions and download links remain in the handbook. A filename or its presence here does not establish a dataset reuse license; consult the original source terms.
