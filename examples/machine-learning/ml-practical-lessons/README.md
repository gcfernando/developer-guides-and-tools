---
layout: default
title: "Machine Learning Practical Lessons — Python Workbook"
description: "Learn data preparation, model evaluation and local prediction services with a guided Python workbook, synthetic datasets and downloadable lessons."
permalink: /examples/machine-learning/ml-practical-lessons/guide/
---

# Machine learning practical lessons

[Developer guides and tools](../../../README.md) · [All examples](../../README.md) · [Machine learning path](../../../docs/learning-paths/machine-learning.md)

Predict delivery times, investigate data problems, evaluate models and build a local prediction service. Start with small synthetic CSV datasets, change one input and compare the result with the workbook's explanation.

[Open the browser workbook](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/Data-Science-and-Machine-Learning.html) · [Read the Markdown workbook](Data-Science-and-Machine-Learning.md) · [Set up Python](SETUP.md) · [Glossary](GLOSSARY.md)

## Start here

1. Keep this complete folder together. For offline reading, open `Data-Science-and-Machine-Learning.html` from your local copy; its diagrams and ZIP downloads need the adjacent folders.
2. Follow [Python setup](SETUP.md). The recorded environment uses Python 3.12; each lesson includes its own requirements.
3. Extract [lesson 002](sample_code_folder/002-your-first-prediction.zip) inside this workbook folder. Open a terminal in the extracted lesson folder and run the commands in its README.
4. Find the prediction of 18.0 minutes for 4 km. Change that distance to 8 km, rerun the lesson and compare the expected 26.0-minute estimate.
5. Follow the [nine Core lessons](Data-Science-and-Machine-Learning.md#core-course), then choose Practice or Reference lessons for a specific topic.

## What is included

| Material | Purpose |
| --- | --- |
| Markdown and HTML workbooks | Two reading formats for the same course, with explanations, worked outputs and lesson links |
| 447 numbered lessons | 9 Core, 395 Practice and 43 Reference entries; some entries intentionally share an exercise |
| 448 ZIP downloads | The numbered lessons plus a separate [train-and-test example](sample_code_folder/train-and-test.zip) |
| `sample_code_folder/` | Lesson archives containing scripts, sample data, requirements and instructions |
| `workbook-figures/` | 100 diagrams and charts, including mobile versions |
| [Lesson coverage](coverage.csv) | Lesson IDs, tracks, sample files, expected results and shared-exercise mappings |
| [Core requirements](requirements-core-tested.txt) and [recorded versions](tested-package-versions.csv) | The supplied dependency recipe and environment record |

## Follow the practical route

The Core route covers a first prediction, missing values, format cleaning, outlier decisions, scaling, appropriate data splits, rare-event cutoffs, regression evaluation and a [delivery-model capstone](Data-Science-and-Machine-Learning.md#lesson-447). The capstone trains and saves a model, checks requests and monitors a later batch. Its optional API runs locally and should be stopped after practice.

## Requirements and verification limits

The supplied setup guide records testing with Python 3.12.14 on Linux. Windows and macOS instructions are provided, but clean installs on those platforms are unverified. Common packages are pinned in the core requirements; individual lessons may need additional packages. Reading the workbook needs no Python installation.

These are teaching exercises with synthetic data. Recorded outputs do not establish real-world model quality or production readiness. Cloud walkthroughs require separate availability, access and cost checks. Load only Joblib models you trained or trust, because loading them can execute code.

No lesson scripts are executed by the repository's standard documentation build. Keep generated models, extracted practice folders and personal data in a separate working copy. Check the lesson README before running it.
